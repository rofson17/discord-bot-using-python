import os
from dotenv import load_dotenv
load_dotenv()


import discord
from discord.ext import commands
from time import sleep
from commands.TicTacToe import TicTacToe
from commands.runPy import RunPy
from commands.code import Code
from commands.wiki import Wiki
from commands.misic import Music
from commands.asistent import Asistent
from commands.help import Help


bot = commands.Bot(command_prefix=.,
                   description="server maneger", intents=discord.Intents.all())
clientt = discord.Client()


# see bot is online or ofline
@ bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Server asistent"))
    print("logged in as {}".format(bot.user.name))


# on  wrong command show error
@ bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="Opps! Command Not Found",
                          description="Please enter right command", color=discord.Color.red())
    message = await ctx.send(embed=embed)
    sleep(3)
    await message.delete()


# add commands
bot.add_cog(Help(bot))
bot.add_cog(Asistent(bot))
bot.add_cog(Music(bot))
bot.add_cog(Wiki(bot))
bot.add_cog(Code(bot))
bot.add_cog(RunPy(bot))
bot.add_cog(TicTacToe(bot))

bot.run(os.environ["TOKEN"])
