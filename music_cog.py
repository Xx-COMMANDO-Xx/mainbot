import discord
from discord import app_commands
from discord.ext import commands
import yt_dlp
from collections import deque
import asyncio
import config
from utils.embed_builder import make_embed, success_embed, error_embed

# ─── Global storage ───
SONG_QUEUES = {}
NOW_PLAYING = {}

async def search_ytdlp_async(query, ydl_opts):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, lambda: _extract(query, ydl_opts))

def _extract(query, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(query, download=False)


class MusicCog(commands.Cog, name="music"):
    """🎵 Music playback & queue management"""

    def __init__(self, bot):
        self.bot = bot
        self.ydl_options = {
            "format": "bestaudio[abr<=96]/bestaudio",
            "noplaylist": True,
            "youtube_include_dash_manifest": False,
            "youtube_include_hls_manifest": False,
        }

    @app_commands.command(name="play", description="Play a song or add it to the queue.")
    @app_commands.describe(song_query="Search query or YouTube URL")
    async def play(self, interaction: discord.Interaction, song_query: str):
        await interaction.response.defer()

        if not interaction.user.voice:
            return await interaction.followup.send(embed=error_embed("You must be in a voice channel first."))

        voice_channel = interaction.user.voice.channel
        vc = interaction.guild.voice_client

        if vc is None:
            vc = await voice_channel.connect()
        elif voice_channel != vc.channel:
            await vc.move_to(voice_channel)

        query = "ytsearch1: " + song_query
        results = await search_ytdlp_async(query, self.ydl_options)
        tracks = results.get("entries", [])

        if not tracks:
            return await interaction.followup.send(embed=error_embed("No results found."))

        first_track = tracks[0]
        audio_url = first_track["url"]
        title = first_track.get("title", "Untitled")
        thumbnail = first_track.get("thumbnail")
        duration = first_track.get("duration", 0)
        m, s = divmod(duration, 60)
        duration_str = f"{m}:{s:02d}"

        guild_id = str(interaction.guild_id)
        if SONG_QUEUES.get(guild_id) is None:
            SONG_QUEUES[guild_id] = deque()

        SONG_QUEUES[guild_id].append((audio_url, title, thumbnail, duration_str))

        if vc.is_playing() or vc.is_paused():
            embed = make_embed(
                title="🎵 Added to Queue",
                description=f"**{title}**",
                color=config.MUSIC,
                fields=[
                    ("Position", str(len(SONG_QUEUES[guild_id])), True),
                    ("Duration", duration_str, True),
                ],
                thumbnail=thumbnail,
                footer=f"Requested by {interaction.user.display_name}",
            )
            await interaction.followup.send(embed=embed)
        else:
            embed = make_embed(
                title="▶️ Now Playing",
                description=f"**{title}**",
                color=config.MUSIC,
                fields=[("Duration", duration_str, True)],
                thumbnail=thumbnail,
            )
            await interaction.followup.send(embed=embed)
            await self._play_next(vc, guild_id, interaction.channel)

    @app_commands.command(name="skip", description="Skip the current song.")
    async def skip(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if vc and (vc.is_playing() or vc.is_paused()):
            vc.stop()
            await interaction.response.send_message(embed=success_embed("⏭️ Skipped the current song."))
        else:
            await interaction.response.send_message(embed=error_embed("Nothing is playing to skip."))

    @app_commands.command(name="pause", description="Pause playback.")
    async def pause(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if vc is None:
            return await interaction.response.send_message(embed=error_embed("I'm not in a voice channel."))
        if not vc.is_playing():
            return await interaction.response.send_message(embed=error_embed("Nothing is currently playing."))
        vc.pause()
        await interaction.response.send_message(embed=success_embed("⏸️ Playback paused!"))

    @app_commands.command(name="resume", description="Resume playback.")
    async def resume(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if vc is None:
            return await interaction.response.send_message(embed=error_embed("I'm not in a voice channel."))
        if not vc.is_paused():
            return await interaction.response.send_message(embed=error_embed("I'm not paused right now."))
        vc.resume()
        await interaction.response.send_message(embed=success_embed("▶️ Playback resumed!"))

    @app_commands.command(name="stop", description="Stop, clear queue, and disconnect.")
    async def stop(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if not vc or not vc.is_connected():
            return await interaction.response.send_message(embed=error_embed("I'm not connected to any voice channel."))

        guild_id = str(interaction.guild_id)
        SONG_QUEUES[guild_id] = deque()
        NOW_PLAYING[guild_id] = None

        if vc.is_playing() or vc.is_paused():
            vc.stop()
        await vc.disconnect()
        await interaction.response.send_message(embed=success_embed("⏹️ Stopped and disconnected!"))

    @app_commands.command(name="queue", description="Show the music queue.")
    async def queue(self, interaction: discord.Interaction):
        guild_id = str(interaction.guild_id)
        qlist = list(SONG_QUEUES.get(guild_id, []))
        np = NOW_PLAYING.get(guild_id)

        if not qlist and not np:
            return await interaction.response.send_message(embed=error_embed("The queue is empty."))

        desc = []
        if np:
            desc.append(f"**▶️ Now Playing:** {np}\n")
        if qlist:
            desc.append(f"**🎶 Upcoming ({len(qlist)} tracks):**\n")
            for i, (_, title, _, dur) in enumerate(qlist, 1):
                desc.append(f"`{i}.` **{title}** `[{dur}]`")

        embed = make_embed(
            title="🎵 Music Queue",
            description="\n".join(desc),
            color=config.MUSIC,
            footer=f"{len(qlist)} track{'s' if len(qlist)!=1 else ''} in queue"
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="nowplaying", description="Show the currently playing song.")
    async def nowplaying(self, interaction: discord.Interaction):
        np = NOW_PLAYING.get(str(interaction.guild_id))
        if np:
            await interaction.response.send_message(embed=make_embed(
                title="▶️ Now Playing", description=f"**{np}**", color=config.MUSIC,
            ))
        else:
            await interaction.response.send_message(embed=error_embed("Nothing is playing."))

    @app_commands.command(name="volume", description="Set volume (0-100).")
    @app_commands.describe(level="Volume level 0-100")
    async def volume(self, interaction: discord.Interaction, level: int):
        if not 0 <= level <= 100:
            return await interaction.response.send_message(embed=error_embed("Volume must be between 0 and 100."))
        vc = interaction.guild.voice_client
        if vc and vc.source:
            vc.source.volume = level / 100.0
        await interaction.response.send_message(embed=success_embed(f"🔊 Volume set to **{level}%**."))

    @app_commands.command(name="sync", description="Force re-sync slash commands (owner only).")
    async def sync(self, interaction: discord.Interaction):
        if interaction.user.id != config.OWNER_ID:
            return await interaction.response.send_message(embed=error_embed("Only the bot owner can use this."))
        guild = discord.Object(id=interaction.guild_id)
        synced = await self.bot.tree.sync(guild=guild)
        await interaction.response.send_message(embed=success_embed(f"✅ Synced {len(synced)} commands."))

    async def _play_next(self, vc, guild_id, channel):
        if SONG_QUEUES[guild_id]:
            audio_url, title, thumbnail, duration_str = SONG_QUEUES[guild_id].popleft()
            NOW_PLAYING[guild_id] = title

            ffmpeg_opts = {
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn -c:a libopus -b:a 96k",
            }

            source = discord.FFmpegOpusAudio(audio_url, **ffmpeg_opts, executable=config.FFMPEG_PATH)

            def after(error):
                if error:
                    print(f"[Music] Error: {error}")
                asyncio.run_coroutine_threadsafe(self._play_next(vc, guild_id, channel), self.bot.loop)

            vc.play(source, after=after)
        else:
            NOW_PLAYING[guild_id] = None
            if vc and vc.is_connected():
                await vc.disconnect()
            SONG_QUEUES[guild_id] = deque()


# ─── MODULE-LEVEL setup() FUNCTION ───
# This is OUTSIDE the class. This is what discord.py looks for.
async def setup(bot):
    await bot.add_cog(MusicCog(bot))