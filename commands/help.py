from time import time
from discord.ext import commands
from discord import Embed, Color
from decouple import config

prefix = "."


class Help (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = Embed(title="!Help commands", description="Use {}help <command> to extended information of a command\n**`Command Prifix: {}`**".format(
            prefix, prefix), color=Color.gold())

        embed.add_field(
            name="Ping", value="See bot is active or not \n> `Command: {}ping`".format(prefix), inline=True)

        embed.add_field(
            name="Whois", value="See a member information \n> `Command: {}whois <mention>`".format(prefix), inline=True)

        embed.add_field(
            name="Wikipedia", value="Search on wikipedia \n> `Command: {}wiki <search words>`".format(prefix), inline=True)

        embed.add_field(
            name="Calcuator", value="Calcuate math\n> `Command: {}math <problem>`".format(prefix), inline=True)

        embed.add_field(
            name="Admin info", value="See info of admin\n> `Command: {}admin`".format(prefix), inline=True)

        embed.add_field(
            name="Tic Tac Toe", value="Play tic tac toe\n> `Command: {}ttt <mention>`\n> `{}place <position>`".format(prefix, prefix), inline=True)

        embed.add_field(
            name="Memes", value="See meme posts\n> `Command: {}meme`".format(prefix), inline=True)

        embed.add_field(
            name="Run python code", value="Run simple python code\n> `Command: {}run <python code>`".format(prefix), inline=True)

        embed.add_field(
            name="Admin info", value="See info of admin\n> `Command: {}admin`".format(prefix), inline=True)

        embed.add_field(
            name="Play music", value="Use this command to see how to play music in voice channel\n> `Command: {}help music`".format(prefix), inline=True)

        embed.add_field(
            name="Syntex higthlight", value="Highlight code syntex (c, cpp, cs, java, python, javascript, php, sql, html, css, bash) \n**Use shift+Enter for new line**\n> `Command: {}<language name> <code>`".format(prefix), inline=False)

        return await ctx.send(embed=embed)

    # ping command
    @help.command(name="ping")
    async def ping(self, ctx):
        embed = Embed(title="Help command",
                      description="To see the bot is online or ofline", color=Color.random())
        embed.add_field(name="Syntex", value="`{}ping`".format(prefix))
        return await ctx.send(embed=embed)

    # whois command
    @help.command(name="whois")
    async def whois(self, ctx):
        embed = Embed(title="Help command",
                      description="See a member information", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}whois <mention>`".format(prefix))
        return await ctx.send(embed=embed)

    # wikipedia command
    @help.command(name="wiki", aliases=["wikipedia"])
    async def wiki(self, ctx):
        embed = Embed(title="Help command",
                      description="Search on wikipedia", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}wiki <search words>`".format(prefix))
        return await ctx.send(embed=embed)

    # admin info command
    @help.command(name="admin")
    async def admin(self, ctx):
        embed = Embed(title="Help command",
                      description="See info of admin", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}admin`".format(prefix))
        return await ctx.send(embed=embed)

    # math command
    @help.command(name="math", aliases=["calculator"])
    async def math(self, ctx):
        embed = Embed(title="Help command",
                      description="Calcuate maths", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}math <problem>`".format(prefix))
        return await ctx.send(embed=embed)

    # tic tac toe game command
    @help.command(name="tictactoe", aliases=["ttt", "place"])
    async def tictactoe(self, ctx):
        embed = Embed(title="Help command",
                      description="Play tic tac toe game\nttt for start game and place for give your turn", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}ttt <mention>`".format(prefix))
        embed.add_field(
            name="Syntex", value="`{}place <position>`".format(prefix))
        return await ctx.send(embed=embed)

    # meme command
    @help.command(name="meme")
    async def meme(self, ctx):
        embed = Embed(title="Help command",
                      description="Show memes", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}meme`".format(prefix))
        return await ctx.send(embed=embed)

    # run command
    @help.command(name="run")
    async def run(self, ctx):
        embed = Embed(title="Help command",
                      description="Run python code", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}run <python code>`".format(prefix))
        return await ctx.send(embed=embed)

    # Song command

    @help.command(name="music", aliases=['song'])
    async def run(self, ctx):
        embed = Embed(title="Help command",
                      description="Play Song", color=Color.random())
        embed.add_field(
            name="Join bot to the voice channel", value="`{}joinor {}connect`".format(prefix, prefix), inline=True)
        embed.add_field(
            name="Play song", value="`{}paly <song name> or {}p <song name>`".format(prefix, prefix), inline=True)
        embed.add_field(
            name="Pause song", value="`{}pause`".format(prefix), inline=True)
        embed.add_field(
            name="Resume song", value="`{}resume`".format(prefix), inline=True)
        embed.add_field(
            name="Skip song", value="`{}skip`".format(prefix), inline=True)
        embed.add_field(
            name="Remove song from queue", value="`{}remove <song number>`".format(prefix), inline=True)
        embed.add_field(
            name="Clear Playlist", value="`{}clear or {}clr`".format(prefix, prefix), inline=True)
        embed.add_field(
            name="Show Playlist", value="`{}queue or {}q or {}playlist`".format(prefix, prefix, prefix), inline=True)
        embed.add_field(
            name="Volume", value="`{}vol <number> or {}volume <number>`".format(prefix, prefix), inline=True)
        embed.add_field(
            name="leave", value="`{}stop or {}leave`".format(prefix, prefix), inline=True)

        return await ctx.send(embed=embed)
