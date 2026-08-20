import discord
from discord import app_commands
from discord.ext import commands


class InfoCog(commands.Cog, name="info"):
    """Info commands"""

    def __init__(self, bot):
        self.bot = bot

    info_group = app_commands.Group(name="info", description="Lookup informational data and stubs")

    @info_group.command(name="github", description="GitHub lookup")
    async def github(self, interaction: discord.Interaction):
        """GitHub lookup."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="GitHub lookup", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="npm", description="NPM package")
    async def npm(self, interaction: discord.Interaction):
        """NPM package."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="NPM package", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="pypi", description="PyPI package")
    async def pypi(self, interaction: discord.Interaction):
        """PyPI package."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="PyPI package", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="youtube", description="YouTube info")
    async def youtube(self, interaction: discord.Interaction):
        """YouTube info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="YouTube info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="twitch", description="Twitch stream check")
    async def twitch(self, interaction: discord.Interaction):
        """Twitch stream check."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Twitch stream check", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="isup", description="Is website up?")
    async def isup(self, interaction: discord.Interaction):
        """Is website up?."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Is website up?", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="domain", description="Domain info")
    async def domain(self, interaction: discord.Interaction):
        """Domain info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Domain info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="ip", description="IP info")
    async def ip(self, interaction: discord.Interaction):
        """IP info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="IP info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="whois", description="Whois lookup")
    async def whois(self, interaction: discord.Interaction):
        """Whois lookup."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Whois lookup", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="dns", description="DNS lookup")
    async def dns(self, interaction: discord.Interaction):
        """DNS lookup."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="DNS lookup", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="port", description="Port check")
    async def port(self, interaction: discord.Interaction):
        """Port check."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Port check", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="headers", description="HTTP headers")
    async def headers(self, interaction: discord.Interaction):
        """HTTP headers."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="HTTP headers", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="ssl", description="SSL check")
    async def ssl(self, interaction: discord.Interaction):
        """SSL check."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="SSL check", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="covid", description="COVID stats")
    async def covid(self, interaction: discord.Interaction):
        """COVID stats."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="COVID stats", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="news", description="Latest news")
    async def news(self, interaction: discord.Interaction):
        """Latest news."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Latest news", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="reddit", description="Reddit info")
    async def reddit(self, interaction: discord.Interaction):
        """Reddit info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Reddit info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="instagram", description="Instagram info")
    async def instagram(self, interaction: discord.Interaction):
        """Instagram info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Instagram info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="tiktok", description="TikTok info")
    async def tiktok(self, interaction: discord.Interaction):
        """TikTok info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="TikTok info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="twitter", description="Twitter/X info")
    async def twitter(self, interaction: discord.Interaction):
        """Twitter/X info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Twitter/X info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="snapchat", description="Snapchat info")
    async def snapchat(self, interaction: discord.Interaction):
        """Snapchat info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Snapchat info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="spotify", description="Spotify track info")
    async def spotify(self, interaction: discord.Interaction):
        """Spotify track info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Spotify track info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="soundcloud", description="SoundCloud info")
    async def soundcloud(self, interaction: discord.Interaction):
        """SoundCloud info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="SoundCloud info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="bandcamp", description="Bandcamp info")
    async def bandcamp(self, interaction: discord.Interaction):
        """Bandcamp info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Bandcamp info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="apple", description="Apple Music info")
    async def apple(self, interaction: discord.Interaction):
        """Apple Music info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Apple Music info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="deezer", description="Deezer info")
    async def deezer(self, interaction: discord.Interaction):
        """Deezer info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Deezer info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="wikipedia", description="Wikipedia lookup")
    async def wikipedia(self, interaction: discord.Interaction):
        """Wikipedia lookup."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Wikipedia lookup", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="dictionary", description="Dictionary lookup")
    async def dictionary(self, interaction: discord.Interaction):
        """Dictionary lookup."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Dictionary lookup", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="thesaurus", description="Thesaurus lookup")
    async def thesaurus(self, interaction: discord.Interaction):
        """Thesaurus lookup."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Thesaurus lookup", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="translate", description="Translate text")
    async def translate(self, interaction: discord.Interaction):
        """Translate text."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Translate text", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="currency", description="Currency converter")
    async def currency(self, interaction: discord.Interaction):
        """Currency converter."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Currency converter", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="unit", description="Unit converter")
    async def unit(self, interaction: discord.Interaction):
        """Unit converter."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Unit converter", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="timezone", description="Timezone converter")
    async def timezone(self, interaction: discord.Interaction):
        """Timezone converter."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Timezone converter", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="calendar", description="Calendar info")
    async def calendar(self, interaction: discord.Interaction):
        """Calendar info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Calendar info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="holiday", description="Holiday info")
    async def holiday(self, interaction: discord.Interaction):
        """Holiday info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Holiday info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="phase", description="Moon phase")
    async def phase(self, interaction: discord.Interaction):
        """Moon phase."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Moon phase", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="sunrise", description="Sunrise/sunset")
    async def sunrise(self, interaction: discord.Interaction):
        """Sunrise/sunset."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Sunrise/sunset", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="tide", description="Tide info")
    async def tide(self, interaction: discord.Interaction):
        """Tide info."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Tide info", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="earthquake", description="Recent earthquakes")
    async def earthquake(self, interaction: discord.Interaction):
        """Recent earthquakes."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Recent earthquakes", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="aurora", description="Aurora forecast")
    async def aurora(self, interaction: discord.Interaction):
        """Aurora forecast."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="Aurora forecast", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)

    @info_group.command(name="iss", description="ISS location")
    async def iss(self, interaction: discord.Interaction):
        """ISS location."""
        from utils.embed_builder import make_embed
        embed = make_embed(title="ISS location", description="Command stub — implement me!", color=0x5865F2)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(InfoCog(bot))