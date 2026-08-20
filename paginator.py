import discord


class PaginatorView(discord.ui.View):
    def __init__(self, embeds, timeout=180):
        super().__init__(timeout=timeout)
        self.embeds = embeds
        self.index = 0
        self._update()

    def _update(self):
        total = len(self.embeds)
        self.first.disabled = self.index == 0
        self.prev.disabled = self.index == 0
        self.next.disabled = self.index == total - 1
        self.last.disabled = self.index == total - 1
        self.counter.label = f"📄 {self.index + 1} / {total}"

    @discord.ui.button(emoji="⏪", style=discord.ButtonStyle.gray)
    async def first(self, interaction, button):
        self.index = 0
        self._update()
        await interaction.response.edit_message(embed=self.embeds[0], view=self)

    @discord.ui.button(emoji="◀️", style=discord.ButtonStyle.blurple)
    async def prev(self, interaction, button):
        self.index = max(0, self.index - 1)
        self._update()
        await interaction.response.edit_message(embed=self.embeds[self.index], view=self)

    @discord.ui.button(label="📄 1 / 1", style=discord.ButtonStyle.gray, disabled=True)
    async def counter(self, interaction, button):
        await interaction.response.defer()

    @discord.ui.button(emoji="▶️", style=discord.ButtonStyle.blurple)
    async def next(self, interaction, button):
        self.index = min(len(self.embeds) - 1, self.index + 1)
        self._update()
        await interaction.response.edit_message(embed=self.embeds[self.index], view=self)

    @discord.ui.button(emoji="⏩", style=discord.ButtonStyle.gray)
    async def last(self, interaction, button):
        self.index = len(self.embeds) - 1
        self._update()
        await interaction.response.edit_message(embed=self.embeds[-1], view=self)

    @discord.ui.button(emoji="❌", style=discord.ButtonStyle.red)
    async def close(self, interaction, button):
        await interaction.response.edit_message(view=None)
        self.stop()