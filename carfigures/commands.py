import discord
from discord import app_commands

from ballsdex.core.utils.transformers import BallEnabledTransform

CONFIG = {
    "Embed Color": discord.Color.blurple(),
    "Line Symbol": "⋄"
}

@app_commands.command()
async def stats(interaction: discord.Interaction, countryball: BallEnabledTransform):
    """
    Displays a specific countryball's statistics.

    Parameters
    ----------
    countryball: Ball
        The countryball you want to inspect.
    """
    await countryball.fetch_related("regime", "economy")

    emoji = interaction.client.get_emoji(countryball.emoji_id) or ""

    embed = discord.Embed(
        title=f"{emoji} {countryball.country} Information:",
        description=(
            f"⋄ **Short Name:** {countryball.short_name}\n"
            f"⋄ **Catch Names:** {countryball.catch_names}\n"
            f"⋄ **Regime:** {countryball.regime}\n"
            f"⋄ **Economy:** {countryball.economy}\n"
            f"⋄ **Rarity:** {countryball.rarity}\n"
            f"⋄ **Attack:** {countryball.attack}\n"
            f"⋄ **Health:** {countryball.health}\n"
            f"⋄ **Capacity Name:** {countryball.capacity_name}\n"
            f"⋄ **Capacity Description:** {countryball.capacity_description}\n"
            f"⋄ **Image Credits:** {countryball.credits}\n"
        ).replace("⋄", CONFIG["Line Symbol"]),
        color=CONFIG["Embed Color"]
    )

    await interaction.response.send_message(embed=embed)

