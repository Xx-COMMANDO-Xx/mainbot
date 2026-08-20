import os
import sys
import discord
from discord.ext import commands
import config


class Bot450(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix=commands.when_mentioned_or("/"),
            intents=intents,
            owner_id=config.OWNER_ID,
            help_command=None,
            case_insensitive=True,
        )
        self._synced = False

    async def setup_hook(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        loaded = 0
        failed = 0
        for filename in sorted(os.listdir(cogs_dir)):
            if not filename.endswith(".py") or filename == "__init__.py":
                continue
            try:
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"[✓] Loaded cog: {filename[:-3]}")
                loaded += 1
            except Exception as e:
                print(f"[✗] Failed to load {filename}: {e}")
                failed += 1
        print(f"[✓] {loaded} cogs loaded, {failed} failed — {len(self.commands)} total commands")

    async def on_ready(self):
        print(f"[✓] Bot online: {self.user}")
        print(f"[✓] Serving {len(self.guilds)} guilds")
        print(f"[✓] {len(self.commands)} prefix commands available")

        # Only sync slash commands for the cogs that use them (music, help, moderation)
        if not self._synced:
            guild_obj = discord.Object(id=config.GUILD_ID)
            try:
                synced = await self.tree.sync(guild=guild_obj)
                print(f"[✓] Synced {len(synced)} slash commands to guild")
            except Exception as e:
                print(f"[!] Slash sync failed (non-critical): {e}")
            self._synced = True

        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="/help | 450+ Commands"
        )
        await self.change_presence(activity=activity)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error


if __name__ == "__main__":
    if not config.TOKEN:
        print("[✗] DISCORD_TOKEN not found in .env!")
        sys.exit(1)

    if not os.path.exists(config.FFMPEG_PATH):
        print(f"[!] FFmpeg not found at: {config.FFMPEG_PATH}")
    else:
        print(f"[✓] FFmpeg found at: {config.FFMPEG_PATH}")

    print(f"[✓] GUILD_ID: {config.GUILD_ID}")
    print(f"[✓] TOKEN: {config.TOKEN[:12]}...{config.TOKEN[-4:]}")

    bot = Bot450()
    bot.run(config.TOKEN)