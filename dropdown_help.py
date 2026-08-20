import discord
import config
from utils.embed_builder import make_embed


class HelpDropdown(discord.ui.Select):
    def __init__(self, bot, embeds_map):
        self.bot = bot
        self.embeds_map = embeds_map
        options = [
            discord.SelectOption(label="🏠 Home", description="Return to main menu", emoji="🏠", value="_home")
        ]
        for key, meta in config.CATEGORIES.items():
            options.append(discord.SelectOption(
                label=key.title(), description=meta["desc"],
                emoji=meta["emoji"], value=key
            ))
        super().__init__(placeholder="📂 Select a category...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction):
        if self.values[0] == "_home":
            embed = self._build_home()
        else:
            embed = self.embeds_map.get(self.values[0])
        await interaction.response.edit_message(embed=embed, view=self.view)

    def _build_home(self):
        total = len(list(self.bot.tree.walk_commands()))
        embed = make_embed(
            title="🏠 450+ Commands Bot",
            description=f"┌ **{total}** slash commands loaded\n├ {len(self.bot.cogs)} modules\n└ Use the dropdown below\n\n**📖 Categories:**",
            color=config.PRIMARY
        )
        for key, meta in config.CATEGORIES.items():
            embed.add_field(name=f"{meta['emoji']} {key.title()}", value=meta["desc"], inline=True)
        embed.set_footer(text="450+ Commands  •  /help")
        return embed


class HelpView(discord.ui.View):
    def __init__(self, bot, embeds_map, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(HelpDropdown(bot, embeds_map))

    @discord.ui.button(emoji="❌", style=discord.ButtonStyle.red, row=1)
    async def close(self, interaction, button):
        await interaction.response.edit_message(view=None)
        self.stop()