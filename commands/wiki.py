from discord.ext import commands
import wikipediaapi
from discord import Embed, Color


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wiki")
    async def wiki(self, ctx, *, message: str):
        async with ctx.typing():
            w = wikipediaapi.Wikipedia('en')
            page = w.page(message)
            if page.exists():
                embed = Embed(
                    title=page.title, description=f"{page.summary[0:500]} [more]({page.fullurl})", color=Color.light_gray())
                return await ctx.send(embed=embed)
            return await ctx.send("Sorry can't find it")
