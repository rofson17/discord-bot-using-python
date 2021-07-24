from discord.ext import commands
from discord import Member, Embed, Color, colour, embeds
from datetime import datetime
from memelib.api import DankMemeClient


class Asistent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping command
    @commands.command()
    async def ping(self, ctx):
        return await ctx.send("pong")

    # whois command
    @commands.command(aliases=["whois"])
    async def who(self, ctx, member: Member):
        roles = [role for role in member.roles]

        embed = Embed(title=f"Name: {member.name}",
                      desription=member.mention, color=Color.random(), timestamp=datetime.utcnow())

        embed.add_field(name="ID: ", value=member.id, inline=True)
        embed.add_field(
            name="Status", value=f"`{member.status}`", inline=True)
        embed.add_field(name="Activity",
                        value=f"`{member.activity}`", inline=False)
        embed.add_field(name="Created Account On:", value=member.created_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Roles:", value="".join(
            [role.mention for role in roles]), inline=False)

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f"Request by {ctx.author.name}")
        return await ctx.send(embed=embed)

    # admin information command
    @commands.command(name="admin")
    async def admin(self, ctx):
        embed = Embed(title=ctx.guild.owner.name,
                      description=f"ID: {ctx.guild.owner.id}", color=Color.dark_magenta(), timestamp=datetime.utcnow())
        embed.add_field(name="Activity", value=ctx.guild.owner.activity)
        embed.set_thumbnail(url=ctx.guild.owner.avatar_url)
        embed.set_footer(
            text=f"Requested by {ctx.message.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    # meme command
    @commands.command(name="meme")
    async def meme(self, ctx):
        await ctx.message.delete()
        async with ctx.typing():
            myclient = DankMemeClient()
            reditMeme = await myclient.async_meme(subreddit="dankmemes")
            embed = Embed(
                title=reditMeme["title"], description=f"[see post]({reditMeme['post_url']})")
            embed.set_image(url=reditMeme['img_url'])
            m = await ctx.send(embed=embed)
        await m.add_reaction("😂")
        await m.add_reaction("👍")
        await m.add_reaction("👎")

    # math canculate command
    @commands.command(name="math")
    async def math(self, ctx, *, problem):
        try:
            ans = eval(problem)
        except:
            return await ctx.reply("Syntex error")
        embed = Embed(title=f"Answer: {ans}", color=Color.blurple())
        return await ctx.reply(embed=embed)
