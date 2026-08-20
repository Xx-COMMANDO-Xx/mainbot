import discord
from discord import app_commands
from discord.ext import commands


class LevelingCog(commands.Cog, name="leveling"):
    """Leveling commands"""

    def __init__(self, bot):
        self.bot = bot

    leveling_group = app_commands.Group(name="leveling", description="Leveling and XP system commands")

    @leveling_group.command(name="rank", description="Your rank")
    async def rank(self, interaction: discord.Interaction):
        """Your rank."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Your rank", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="leaderboard", description="Level leaderboard")
    async def leaderboard(self, interaction: discord.Interaction):
        """Level leaderboard."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Level leaderboard", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="level", description="Set level")
    async def level(self, interaction: discord.Interaction):
        """Set level."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Set level", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="xp", description="Set XP")
    async def xp(self, interaction: discord.Interaction):
        """Set XP."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Set XP", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="rewards", description="Level rewards")
    async def rewards(self, interaction: discord.Interaction):
        """Level rewards."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Level rewards", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="addreward", description="Add reward")
    async def addreward(self, interaction: discord.Interaction):
        """Add reward."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Add reward", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="remreward", description="Remove reward")
    async def remreward(self, interaction: discord.Interaction):
        """Remove reward."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Remove reward", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="xprate", description="XP rate")
    async def xprate(self, interaction: discord.Interaction):
        """XP rate."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="XP rate", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="xpboost", description="XP boost")
    async def xpboost(self, interaction: discord.Interaction):
        """XP boost."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="XP boost", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="xpblacklist", description="XP blacklist channel")
    async def xpblacklist(self, interaction: discord.Interaction):
        """XP blacklist channel."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="XP blacklist channel", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="xpwhitelist", description="XP whitelist channel")
    async def xpwhitelist(self, interaction: discord.Interaction):
        """XP whitelist channel."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="XP whitelist channel", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="announce", description="Level up announce")
    async def announce(self, interaction: discord.Interaction):
        """Level up announce."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Level up announce", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="card", description="Rank card")
    async def card(self, interaction: discord.Interaction):
        """Rank card."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Rank card", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="cardcolor", description="Rank card color")
    async def cardcolor(self, interaction: discord.Interaction):
        """Rank card color."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Rank card color", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="cardbg", description="Rank card background")
    async def cardbg(self, interaction: discord.Interaction):
        """Rank card background."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Rank card background", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="resetxp", description="Reset all XP")
    async def resetxp(self, interaction: discord.Interaction):
        """Reset all XP."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Reset all XP", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="resetlevel", description="Reset level")
    async def resetlevel(self, interaction: discord.Interaction):
        """Reset level."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Reset level", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="setxp", description="Set exact XP")
    async def setxp(self, interaction: discord.Interaction):
        """Set exact XP."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Set exact XP", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="addxp", description="Add XP to user")
    async def addxp(self, interaction: discord.Interaction):
        """Add XP to user."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Add XP to user", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @leveling_group.command(name="removexp", description="Remove XP from user")
    async def removexp(self, interaction: discord.Interaction):
        """Remove XP from user."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Remove XP from user", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(LevelingCog(bot))