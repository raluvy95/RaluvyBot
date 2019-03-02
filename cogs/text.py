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
import json


class Text():
        def __init__(self, bot):
                self.bot = bot


        @commands.group()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def lenny(self, ctx):
            if ctx.invoked_subcommand is None:
                return await ctx.send('( ͡° ͜ʖ ͡°)')


        @lenny.command()
        async def help(self, ctx):
            await ctx.send('```Help lenny\n\nOriginal - ( ͡° ͜ʖ ͡°)\nHug - (つ ͡° ͜ʖ ͡°)つ\nAttack - (∩ ͡ ° ʖ ͡ °) ⊃-(===>\nFliptable - ( ͡° ͜ʖ ͡°) ╯︵ ┻─┻\nGlasses - ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ\nLove - ( ͡♥ 3 ͡♥)```')

        @lenny.command()
        async def original(self, ctx):
            await ctx.send('( ͡° ͜ʖ ͡°)')

        @lenny.command()
        async def hug(self, ctx):
            await ctx.send('(つ ͡° ͜ʖ ͡°)つ')

        @lenny.command()
        async def fliptable(self, ctx):
            await ctx.send('( ͡° ͜ʖ ͡°) ╯︵ ┻─┻')

        @lenny.command()
        async def attack(self, ctx):
            await ctx.send('(∩ ͡ ° ʖ ͡ °) ⊃-(===>')

        @lenny.command()
        async def glasses(self, ctx):
            await ctx.send('ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ')

        @lenny.command()
        async def love(self, ctx):
            await ctx.send('( ͡♥ 3 ͡♥)')

        @commands.command()
        async def xd(self, ctx, message=None, boi=None, kok=None):
          try:
            if message is not None and boi is None and kok is None:
                a = message
                return await ctx.send(f'```{a}           {a}    {a} {a}\n  {a}       {a}      {a}    {a}\n    {a}   {a}        {a}     {a}\n       {a}           {a}     {a}\n    {a}   {a}        {a}     {a}\n  {a}       {a}      {a}    {a}\n{a}           {a}    {a} {a}```')
            if message is not None and boi is not None and kok is None:
                a = message
                b = boi
                return await ctx.send(f'```{a}           {a}    {b} {b}\n  {a}       {a}      {b}    {b}\n    {a}   {a}        {b}     {b}\n       {a}           {b}     {b}\n    {a}   {a}        {b}     {b}\n  {a}       {a}      {b}    {b}\n{a}           {a}    {b} {b}```')
            if message is not None and boi is not None and kok is not None:
                a = message
                b = boi
                c = kok
                return await ctx.send(f'```{a}           {a}    {b} {c}\n  {a}       {a}      {b}    {c}\n    {a}   {a}        {b}     {c}\n       {a}           {b}     {c}\n    {a}   {a}        {b}     {c}\n  {a}       {a}      {b}    {c}\n{a}           {a}    {b} {c}```')
            if message is None:
                return await ctx.send("Please put a message...")
          except discord.HTTPException as fuck:
              return await ctx.send(f"**Ops... I can't send because:**\n`{fuck}`")

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def say(self, ctx, *, message):
               return await ctx.send(message)

        @commands.command(aliases=['sayembed', 'say-embed'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def saye(self, ctx, *, message):
              em = discord.Embed(color=discord.Color.blue())
              em.add_field(name=ctx.author.name, value=message)
              await ctx.send(embed=em)

        @commands.command(aliases=['poll'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def vote(self, ctx, *, message=None):
              if message is None:
                return await ctx.send("**Please use `,vote [question]`!**")
              em = discord.Embed(color=discord.Color.blue())
              em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
              em.add_field(name="Question:", value=message)
              em.timestamp = datetime.datetime.utcnow()
              try:
                bos = await ctx.send(embed=em)
                await bos.add_reaction('\U00002705')
                await bos.add_reaction('\U0000274c')
              except discord.HTTPException as fuck:
                return await ctx.send(f"**Ops... I can't send because:**\n`{fuck}`")

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def reverse(self, ctx, *, boi=None):
           if boi is None:
               return await ctx.send('Please put a message.')
           else:
               await ctx.send(boi[::-1])

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def sayd(self, ctx, *, message):
            await ctx.message.delete()
            await ctx.send(message)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def space(self, ctx, *, message=None):
            if message is None:
                return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Hey, please use `,space [message]`!**')
            await ctx.send(' '.join(message))

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def clap(self, ctx, *, message=None):
            if message is None:
                return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Hey, please use `,clap [message]`!**')
            await ctx.send(':clap:'.join(message))

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def parrot(self, ctx, *, message=None):
            if message is None:
                return await ctx.send('<a:parrot:491311653884002304>')
            await ctx.send('<a:parrot:491311653884002304>'.join(message))


        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def wumpus(self, ctx, *, message=None):
           if message is None:
               return await ctx.send('<a:aWumpus:479223216796336148>')
           await ctx.send('<a:aWumpus:479223216796336148>'.join(message))

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def blobdance(self, ctx, *, message=None):
           if message is None:
               return await ctx.send('<a:blobdance:535801229050118164>')
           await ctx.send('<a:blobdance:535801229050118164>'.join(message))

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def emoji(self, ctx):
            await ctx.send(random.choice(bot.emojis))


        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def shrug(self, ctx):
           await ctx.send("¯\_(ツ)_/¯")

        @commands.command(aliases=['jesus'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def jesussay(self, ctx, *, message=None):
           if message is None:
               return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please put the message what jesus says.**')
           embed=discord.Embed(color=0xd2cd68)
           embed.set_thumbnail(url="https://i.kym-cdn.com/entries/icons/facebook/000/009/556/jesus-bleu-mauve.jpg")
           embed.add_field(name="Jesus says", value=message, inline=False)
           embed.timestamp = datetime.datetime.utcnow()
           await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Text(bot))
