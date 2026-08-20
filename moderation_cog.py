import discord
from discord import app_commands
from discord.ext import commands
import config
from utils.embed_builder import success_embed, error_embed


class ModerationCog(commands.Cog, name="moderation"):
    """🛠️ Server moderation"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick a member.")
    @app_commands.describe(member="Member to kick", reason="Reason")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction, member: discord.Member, reason: str = "No reason"):
        if member.top_role >= interaction.user.top_role and interaction.user.id != config.OWNER_ID:
            return await interaction.response.send_message(embed=error_embed("Cannot kick that member."))
        await member.kick(reason=reason)
        await interaction.response.send_message(embed=success_embed(f"👢 Kicked **{member}** | {reason}"))

    @app_commands.command(name="ban", description="Ban a member.")
    @app_commands.describe(member="Member to ban", reason="Reason")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction, member: discord.Member, reason: str = "No reason"):
        await member.ban(reason=reason)
        await interaction.response.send_message(embed=success_embed(f"🔨 Banned **{member}** | {reason}"))

    @app_commands.command(name="unban", description="Unban a user by ID.")
    @app_commands.describe(user_id="User ID")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(self, interaction, user_id: str):
        try:
            uid = int(user_id)
            user = await self.bot.fetch_user(uid)
            await interaction.guild.unban(user)
            await interaction.response.send_message(embed=success_embed(f"🔓 Unbanned **{user}**"))
        except:
            await interaction.response.send_message(embed=error_embed("Invalid ID or user not banned."))

    @app_commands.command(name="purge", description="Delete messages.")
    @app_commands.describe(amount="Number (1-1000)")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def purge(self, interaction, amount: int = 10):
        amount = max(1, min(1000, amount))
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(embed=success_embed(f"🧹 Deleted **{len(deleted)}** messages."))

    @app_commands.command(name="mute", description="Timeout a member.")
    @app_commands.describe(member="Member", duration="Minutes", reason="Reason")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def mute(self, interaction, member: discord.Member, duration: int = 10, reason: str = "No reason"):
        until = discord.utils.utcnow() + discord.timedelta(minutes=duration)
        await member.timeout(until, reason=reason)
        await interaction.response.send_message(embed=success_embed(f"🔇 **{member}** timed out {duration}m | {reason}"))

    @app_commands.command(name="unmute", description="Remove timeout.")
    @app_commands.describe(member="Member")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def unmute(self, interaction, member: discord.Member):
        await member.timeout(None)
        await interaction.response.send_message(embed=success_embed(f"🔊 **{member}** unmuted."))

    @app_commands.command(name="lock", description="Lock channel.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lock(self, interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
        await interaction.response.send_message(embed=success_embed("🔒 Channel locked."))

    @app_commands.command(name="unlock", description="Unlock channel.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def unlock(self, interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
        await interaction.response.send_message(embed=success_embed("🔓 Channel unlocked."))

    @app_commands.command(name="slowmode", description="Set slowmode in seconds.")
    @app_commands.describe(seconds="Seconds (0=off)")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def slowmode(self, interaction, seconds: int = 0):
        await interaction.channel.edit(slowmode_delay=seconds)
        state = f"**{seconds}s**" if seconds else "**OFF**"
        await interaction.response.send_message(embed=success_embed(f"🐢 Slowmode {state}."))


async def setup(bot):
    await bot.add_cog(ModerationCog(bot))