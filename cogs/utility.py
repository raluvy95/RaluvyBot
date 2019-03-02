import discord
import random
from discord.ext import commands
import logging
import traceback
from datetime import datetime
import asyncio
import os
import aiohttp
from discord import opus
from asyncio import sleep
import datetime
import time
import json

start_time = time.time()

class Utility():
        def __init__(self, bot):
                self.bot = bot

        @commands.command(aliases=['av'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def avatar(self, ctx, member: discord.Member=None):
              if member is None:
                  member = ctx.author
              em = discord.Embed(description=f'{member.mention}\'s [avatar]({member.avatar_url})', color=discord.Colour.blurple())
              em.set_image(url=member.avatar_url)
              await ctx.send(embed=em)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def support(self, ctx):
              em = discord.Embed(title="", description="", color=discord.Colour.green())
              em.add_field(name='Join our support server!', value='[here]( https://discord.gg/bazhjYQ )')
              await ctx.send(embed=em)

        @commands.command(aliases=['h'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def help(self, ctx):
            embed = discord.Embed(title=f"All commands (Total: {len(ctx.bot.commands)})", description="Visit our [website]( http://raluvybot.coolpage.biz/ ) for more information about the commands!\nMore question? Join [Support Server!]( https://discordapp.com/invite/bazhjYQ )", color=0xe67e22)
            embed.add_field(name="<a:ablobdancewhite:464794007755685898> Fun", value="`8ball`  `gay`  `dice`  `slots`  `xd`  `choose`  `dogfact`   `mineswepper`  `catfact`  `emoji`  `respect`  `kill`", inline=False)
            embed.add_field(name=":ok: Text", value="`lenny`  `reverse`  `shrug`  `blobdance`  `jesussay`  `clap`  `sayd`  `say`  `space`  `owo`  `wumpus`  `parrot`", inline=False)
            embed.add_field(name=":hammer:  Moderation", value="`kick`  `ban`  `nickname`  `softban`  `purge`  `role`", inline=False)
            embed.add_field(name=":mountain_snow:  Images", value="`lick`  `slap`  `pat`  `shiba`  `cat`  `dog`  `hug`  `cursed`  `pika`  `achievement`  `meme`  `kiss`  `doge`  `logo`", inline=False)
            embed.add_field(name=":information_source: Info", value="`emojiinfo`  `status`  `roleinfo`  `membercount`  `serverinfo`  `pokemon`  `userinfo`  `stats`", inline=False)
            embed.add_field(name=":pushpin: Utility", value="`ping`  `uptime`  `vote`  `randomnumber`  `flipcoin`  `avatar`  `support`  `emojiavatar`  `search`  `invite`", inline=False)
            embed.set_footer(text='Use , before using commands')
            embed.timestamp = datetime.datetime.utcnow()
            try:
                await ctx.message.add_reaction("\N{WHITE HEAVY CHECK MARK}")
                await ctx.author.send(embed=embed)
            except discord.Forbidden as owo:
                return await ctx.send(embed=embed)

        @commands.command()
        @commands.cooldown(1, 2, commands.BucketType.user)
        async def uptime(self, ctx):
              current_time = time.time()
              difference = int(round(current_time - start_time))
              text = str(datetime.timedelta(seconds=difference))
              await ctx.send(text)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def invite(self, ctx):
              await ctx.send("""**You can add me here ->** http://bit.ly/InviteRaluvyBot""")

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def dbl(self, ctx):
              await ctx.send("**Vote me for more commands ->** https://discordbots.org/bot/489061565430235136/vote")

        @commands.command(aliases= ["number"])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def randomnumber(self, ctx, owo: int, uwu: int):
              if owo is None or uwu is None:
                   return await ctx.send("**Please use `,randomnumber <min> <max>`")
              boi = random.randint(owo, uwu)
              await ctx.send(f":1234: | **Your random number is `{boi}`!**")

        @commands.command(aliases=['roll', 'rolls', 'dic'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def dice(self, ctx):
              a = (random.choice(['1', '2', '3', '4', '5', '6']))
              await ctx.send(f":game_die: | **I rolled a `{a}`!**")

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def choose(self, ctx, option1, option2):
              if option1 is None or option2 is None:
                   return await ctx.send("**Please use `,choose <thing1> <thing2>`**")
              a = [option1, option2]
              if option1 == option2:
                  return await ctx.send("<:RaluvyError:489805076118896690> | **I can't choose the same things ;-;**")
              await ctx.send(f':thinking: | {ctx.author.mention}, i choose **' + random.choice(a) + '** !')

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def ping(self, ctx):
              t = await ctx.send(':ping_pong: | Pong!, Calculating...')
              await asyncio.sleep(1)
              await t.edit(content=f':ping_pong: | **Pong!** `{ctx.bot.latency * 1000:,.0f}MS`')

        @commands.command(aliases=['google'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def search(self, ctx, *, query):
            search = query
            URL = 'https://www.google.com/search?q='
            words = search.split(" ")
            num = 0
            for w in words:
                if num is 0:
                    URL = URL + w
                num = 1
            else:
                URL = URL + "+"+ w
            await ctx.send(URL)

def setup(bot):
      bot.add_cog(Utility(bot))
