from discord.ext import commands
# from discord import Color, Embed


class Code(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # show python code
    @commands.command(name="python", aliases=['py'])
    async def pyCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```python\n{code}\n```")

    # show javascript code
    @commands.command(name="javascript", aliases=['js'])
    async def jsCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```javaScript\n{code}\n```")

    # show java code
    @commands.command(name="java")
    async def javaCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```java\n{code}\n```")

    # show c code
    @commands.command(name="c")
    async def cCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```c\n{code}\n```")

    # show c++ code
    @commands.command(name="cpp")
    async def cppCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```cpp\n{code}\n```")

    # show c# code
    @commands.command(name="cs")
    async def csCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```cs\n{code}\n```")

    # show python code
    @commands.command(name="php")
    async def phpCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```php\n{code}\n```")

    # show css code
    @commands.command(name="css")
    async def cssCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```css\n{code}\n```")

    # show html code
    @commands.command(name="html")
    async def htmlCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```html\n{code}\n```")

    # show bash code
    @commands.command(name="bash")
    async def bashCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```bash\n{code}\n```")

    # show sql code
    @commands.command(name="sql")
    async def sqlCode(self, ctx, *, code: str):
        await ctx.message.delete()
        await ctx.send(f"```sql\n{code}\n```")
