from discord.ext import commands
from discord import Member, Embed
import os
from random import randint
import re
import requests
import urllib.request


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player1 = ""
        self.player2 = ""
        self.turn = ""
        self.gameOver = True
        self.board = [],
        self.count = 0
        self.winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

    @commands.command(name="ttt", aliases=['tictactoe'])
    async def tictactoe(self, ctx, member: Member):
        if not self.gameOver:
            return
        self.board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                      ":white_large_square:", ":white_large_square:", ":white_large_square:",
                      ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        self.turn = ""
        self.gameOver = False
        self.count = 0

        self.player1 = ctx.message.author
        self.player2 = member
        line = ""

        for x in range(len(self.board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + self.board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + self.board[x]

        num = randint(1, 2)
        if num == 1:
            self.turn = self.player1
            myEmbed = Embed(title="GAME IN PROGRESS", description="IT IS <@" +
                            str(self.player1.id) + ">'s TURN.", color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif num == 2:
            self.turn = self.player2
            myEmbed = Embed(title="GAME IN PROGRESS", description="IT IS <@" +
                            str(self.player2.id) + ">'s TURN.", color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        else:
            myEmbed = Embed(title="GAME IN PROGRESS",
                            description="A GAME IS STILL IN PROGRESS. FINISH IT BEFORE STARTING A NEW ONE", color=0xe74c3c)
            await ctx.send(embed=myEmbed)

    @commands.command(name="place", aliases=['turn'])
    async def place(self, ctx, pos: int):
        if not self.gameOver:
            mark = ""
            if self.turn == ctx.author:
                if self.turn == self.player1:
                    mark = ":regional_indicator_x:"
                elif self.turn == self.player2:
                    mark = ":o2:"
                if 0 < pos < 10 and self.board[pos - 1] == ":white_large_square:":
                    self.board[pos - 1] = mark
                    self.count += 1

                    line = ""
                    for x in range(len(self.board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + self.board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + self.board[x]

                    self.checkWinner(self.winningConditions, mark)
                    if self.gameOver == True:
                        myEmbed = Embed(title="WINNER!",
                                        description=mark + " :crown: ", color=0xf1c40f)
                        await ctx.send(embed=myEmbed)
                    elif self.count >= 9:
                        self.gameOver = True
                        myEmbed = Embed(
                            title="TIE", description="IT'S A TIE :handshake:", color=0xf1c40f)
                        await ctx.send(embed=myEmbed)

                    if self.turn == self.player1:
                        self.turn = self.player2
                    elif self.turn == self.player2:
                        self.turn = self.player1
                else:
                    myEmbed = Embed(
                        title="PLACE ERROR!", description="BE SURE TO CHOOSE AN INTEGER BETWEEN 1 AND 9 (INCLUSIVE) AND AN UNMARKED TILE. ", color=0xe74c3c)
                    await ctx.send(embed=myEmbed)
            else:
                myEmbed = Embed(title="TURN ERROR!",
                                description="IT'S NOT YOUR TURN", color=0xe74c3c)
                await ctx.send(embed=myEmbed)
        else:
            myEmbed = Embed(
                title="START GAME", description="TO START A NEW GAME, USE -tictactoe COMMAND", color=0x2ecc71)
            await ctx.send(embed=myEmbed)

    @commands.command(name="exit")
    async def exit(self, ctx):
        # if ctx.message.author == self.player1 or ctx.message.author == self.player2 or :
        if ctx.message.author == ctx.guild.owner:
            self.player1 = ""
            self.player2 = ""
            self.turn = ""
            self.gameOver = True
            self.board = [],
            self.count = 0
            return await ctx.send("This game is over")
        return await ctx.reply("You are not in the game")

    def checkWinner(self, winningConditions, mark):
        for condition in winningConditions:
            if self.board[condition[0]] == mark and self.board[condition[1]] == mark and self.board[condition[2]] == mark:
                self.gameOver = True

    @tictactoe.error
    async def tictactoe_error(ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            myEmbed = Embed(title="MENTION ERROR!",
                            description="PLEASE MENTION 2 USERS", color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif isinstance(error, commands.BadArgument):
            myEmbed = Embed(
                title="ERROR!", description="PLEASE MAKE SURE TO MENTION/PING PLAYERS (ie. <@688534433879556134>)", color=0xe74c3c)
            await ctx.send(embed=myEmbed)

    @place.error
    async def place_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            myEmbed = Embed(
                title="NO POSITION", description="PLEASE ENTER A POSITION TO MARK", color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif isinstance(error, commands.BadArgument):
            myEmbed = Embed(title="INTEGER ERROR!",
                            description="PLEASE MAKE SURE IT'S AN INTEGER", color=0xe74c3c)
            await ctx.send(embed=myEmbed)
