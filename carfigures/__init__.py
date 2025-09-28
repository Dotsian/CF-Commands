import asyncio

from .commands import stats


async def setup(bot):
    await asyncio.sleep(0.5)

    cog = bot.get_cog("Balls")
    cog.app_command.add_command(stats)

