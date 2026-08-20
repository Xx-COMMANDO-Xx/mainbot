import discord
import config
from datetime import datetime


def make_embed(title=None, description=None, color=config.PRIMARY,
               fields=None, footer=None, footer_icon=None,
               thumbnail=None, image=None, author_name=None,
               author_icon=None, timestamp=None):
    embed = discord.Embed(
        title=title, description=description, color=color,
        timestamp=timestamp or discord.utils.utcnow(),
    )
    if fields:
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
    embed.set_footer(text=footer or "450+ Commands  •  /help", icon_url=footer_icon)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if image:
        embed.set_image(url=image)
    if author_name:
        embed.set_author(name=author_name, icon_url=author_icon)
    return embed


def success_embed(desc, title="✅ Success"):
    return make_embed(title=title, description=desc, color=config.SUCCESS)


def error_embed(desc, title="❌ Error"):
    return make_embed(title=title, description=desc, color=config.ERROR)


def warning_embed(desc, title="⚠️ Warning"):
    return make_embed(title=title, description=desc, color=config.WARNING)