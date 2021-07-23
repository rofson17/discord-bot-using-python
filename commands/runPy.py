from discord.ext import commands
import io
import contextlib


class RunPy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="run")
    async def eval(self, ctx, *, code):
        str_obj = io.StringIO()
        try:
            with contextlib.redirect_stdout(str_obj):
                exec(code)
        except Exception as e:
            return await ctx.send(f"```{e.__class__.__name__}: {e}```")
        await ctx.send(f'```{str_obj.getvalue()}```')
