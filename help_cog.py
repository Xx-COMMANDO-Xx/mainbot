import discord
from discord import app_commands
from discord.ext import commands
import config
from utils.embed_builder import make_embed, error_embed
from utils.dropdown_help import HelpView


class HelpCog(commands.Cog, name="help"):
    """📖 Interactive help system"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Show the interactive help menu.")
    @app_commands.describe(command="Optional: get help for a specific command")
    async def help(self, interaction: discord.Interaction, command: str = None):
        if command:
            await self._show_command(interaction, command)
        else:
            await self._show_overview(interaction)

    async def _show_overview(self, interaction):
        embeds_map = {}
        for key, meta in config.CATEGORIES.items():
            cmds = [c for c in self.bot.tree.walk_commands()]
            lines = [f"`/{c.qualified_name}` — {c.description or 'No description'}" for c in cmds if key in str(c.module)]
            if lines:
                embeds_map[key] = make_embed(
                    title=f"{meta['emoji']} {key.title()} Commands",
                    description="\n".join(lines[:50]),
                    color=config.PRIMARY,
                    footer="Showing up to 50 commands"
                )
        view = HelpView(self.bot, embeds_map)
        home = view.children[0]._build_home()
        await interaction.response.send_message(embed=home, view=view)

    async def _show_command(self, interaction, name):
        cmd = None
        for c in self.bot.tree.walk_commands():
            if c.qualified_name == name.lower():
                cmd = c
                break
        if not cmd:
            return await interaction.response.send_message(embed=error_embed(f"No command `{name}` found."))
        embed = make_embed(
            title=f"📖 /{cmd.qualified_name}",
            description=cmd.description or "No description.",
            color=config.PRIMARY,
            fields=[("Parameters", self._params(cmd), False)],
        )
        await interaction.response.send_message(embed=embed)

    def _params(self, cmd):
        if not cmd.parameters:
            return "None"
        lines = []
        for p in cmd.parameters:
            req = "✅" if p.required else "❌"
            lines.append(f"`{p.name}` {req} — {p.description or 'No description'}")
        return "\n".join(lines)


async def setup(bot):
    await bot.add_cog(HelpCog(bot))