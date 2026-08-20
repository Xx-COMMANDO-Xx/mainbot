import sys
import time
import datetime
import platform
import discord
from discord import app_commands
from discord.ext import commands

from utils.embed_builder import make_embed


class UtilityCog(commands.Cog, name="utility"):
    """Utility commands for users and server information."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot latency and API response time")
    async def ping(self, interaction: discord.Interaction):
        """Check bot latency."""
        start_time = time.perf_counter()
        
        # Acknowledge first to measure REST API latency
        await interaction.response.send_message("🏓 Pinging...")
        
        end_time = time.perf_counter()
        api_latency = round((end_time - start_time) * 1000)
        ws_latency = round(self.bot.latency * 1000)

        embed = make_embed(
            title="🏓 Pong!",
            description=(
                f"**WebSocket Latency:** `{ws_latency}ms`\n"
                f"**API Response Time:** `{api_latency}ms`"
            ),
            color=0x5865F2,
        )
        await interaction.edit_original_response(content=None, embed=embed)

    @app_commands.command(name="userinfo", description="Detailed information about a user")
    @app_commands.describe(user="Target user to view info for (defaults to yourself)")
    async def userinfo(
        self, interaction: discord.Interaction, user: discord.Member | discord.User = None
    ):
        """Detailed user information."""
        target = user or interaction.user
        guild = interaction.guild

        # Fetch guild-specific member data if available
        member = guild.get_member(target.id) if guild else None

        embed = make_embed(
            title=f"User Info - {target.name}",
            color=member.color if member and member.color.value else 0x5865F2,
        )
        embed.set_thumbnail(url=target.display_avatar.url)

        embed.add_field(name="Username", value=f"`{target.name}`", inline=True)
        embed.add_field(name="User ID", value=f"`{target.id}`", inline=True)
        embed.add_field(
            name="Account Created",
            value=f"<t:{int(target.created_at.timestamp())}:F> (<t:{int(target.created_at.timestamp())}:R>)",
            inline=False,
        )

        if member and member.joined_at:
            embed.add_field(
                name="Joined Server",
                value=f"<t:{int(member.joined_at.timestamp())}:F> (<t:{int(member.joined_at.timestamp())}:R>)",
                inline=False,
            )
            roles = [role.mention for role in member.roles if role.name != "@everyone"]
            roles_str = ", ".join(reversed(roles)) if roles else "None"
            embed.add_field(name=f"Roles [{len(roles)}]", value=roles_str, inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="serverinfo", description="Detailed information about this server")
    async def serverinfo(self, interaction: discord.Interaction):
        """Server information."""
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message(
                "This command can only be used inside a server.", ephemeral=True
            )
            return

        embed = make_embed(
            title=f"Server Info - {guild.name}",
            color=0x5865F2,
        )
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name="Server ID", value=f"`{guild.id}`", inline=True)
        embed.add_field(name="Owner", value=guild.owner.mention if guild.owner else "Unknown", inline=True)
        embed.add_field(
            name="Created On",
            value=f"<t:{int(guild.created_at.timestamp())}:D> (<t:{int(guild.created_at.timestamp())}:R>)",
            inline=False,
        )

        # Count text, voice, and category channels
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)

        embed.add_field(name="Members", value=f"`{guild.member_count}`", inline=True)
        embed.add_field(
            name="Channels",
            value=f"💬 `{text_channels}` Text | 🔊 `{voice_channels}` Voice | 📁 `{categories}` Categories",
            inline=True,
        )
        embed.add_field(name="Roles", value=f"`{len(guild.roles)}`", inline=True)
        embed.add_field(name="Boost Level", value=f"Level `{guild.premium_tier}` ({guild.premium_subscription_count} Boosts)", inline=True)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="botinfo", description="Information and statistics about this bot")
    async def botinfo(self, interaction: discord.Interaction):
        """Bot statistics and system information."""
        app_info = await self.bot.application_info()
        uptime_seconds = int(time.time() - getattr(self.bot, "start_time", time.time()))

        embed = make_embed(
            title=f"Bot Info - {self.bot.user.name}",
            description=app_info.description or "A versatile Discord bot.",
            color=0x5865F2,
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        embed.add_field(name="Owner", value=f"`{app_info.owner}`", inline=True)
        embed.add_field(name="Servers", value=f"`{len(self.bot.guilds)}`", inline=True)
        embed.add_field(name="Users", value=f"`{len(self.bot.users)}`", inline=True)

        embed.add_field(name="Python Version", value=f"`{platform.python_version()}`", inline=True)
        embed.add_field(name="discord.py Version", value=f"`{discord.__version__}`", inline=True)
        embed.add_field(name="Uptime", value=f"<t:{int(time.time() - uptime_seconds)}:R>", inline=True)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="avatar", description="View and download a user's avatar")
    @app_commands.describe(user="Target user to fetch avatar for")
    async def avatar(
        self, interaction: discord.Interaction, user: discord.Member | discord.User = None
    ):
        """Display a user's avatar."""
        target = user or interaction.user
        avatar_url = target.display_avatar.url

        embed = make_embed(
            title=f"{target.name}'s Avatar",
            color=0x5865F2,
        )
        embed.set_image(url=avatar_url)
        embed.description = f"[PNG]({target.display_avatar.replace(format='png').url}) | [JPG]({target.display_avatar.replace(format='jpg').url}) | [WEBP]({target.display_avatar.replace(format='webp').url})"

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(UtilityCog(bot))