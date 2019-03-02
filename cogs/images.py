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


class Images():
        def __init__(self, bot):
                self.bot = bot

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def hug(self, ctx, member: discord.Member=None):
              with open("data/hug.json", "r") as f:
                    res = json.load(f)
              if member is None:
                    return await ctx.send("**Tag a user to run this command.**")
              if member is not None:
                    em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
                    em.set_image(url=(random.choice(res['hug'])))
                    em.timestamp = datetime.datetime.utcnow()
                    return await ctx.send(embed=em)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def kiss(self, ctx, member: discord.Member=None):
              with open("data/kiss.json", "r") as f:
                      res = json.load(f)
              if member is None:
                      return await ctx.send("**Tag a user to run this command.**")
              if member is not None:
                      em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
                      em.set_image(url=(random.choice(res['hug'])))
                      em.timestamp = datetime.datetime.utcnow()
                      return await ctx.send(embed=em)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def lick(self, ctx, member: discord.Member=None):
              with open("data/lick.json", "r") as f:
                        res = json.load(f)
              if member is None:
                        return await ctx.send("**Tag a user to run this command.**")
              if member is not None:
                        em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
                        em.set_image(url=(random.choice(res['hug'])))
                        em.timestamp = datetime.datetime.utcnow()
                        return await ctx.send(embed=em)


        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def slap(self, ctx, member: discord.Member=None):
              with open("data/slap.json", "r") as f:
                        res = json.load(f)
              if member is None:
                        return await ctx.send("**Tag a user to run this command.**")
              if member is not None:
                        em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
                        em.set_image(url=(random.choice(res['hug'])))
                        em.timestamp = datetime.datetime.utcnow()
                        return await ctx.send(embed=em)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def pat(self, ctx, member: discord.Member=None):
              with open("data/pat.json", "r") as f:
                        res = json.load(f)
              if member is None:
                        return await ctx.send("**Tag a user to run this command.**")
              if member is not None:
                        em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
                        em.set_image(url=(random.choice(res['hug'])))
                        em.timestamp = datetime.datetime.utcnow()
                        return await ctx.send(embed=em)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def poke(self, ctx, member: discord.Member=None):
              with open("data/poke.json", "r") as f:
                        res = json.load(f)
              if member is None:
                        return await ctx.send("**Tag a user to run this command.**")
              if member is not None:
                        em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
                        em.set_image(url=(random.choice(res['hug'])))
                        em.timestamp = datetime.datetime.utcnow()
                        return await ctx.send(embed=em)


        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def logo(self, ctx, *, text):
             if len(text)>18:
                      return await ctx.send("**Your text is too long!** Try again.")
             a = random.choice(['scoobydoo','cnn', 'starWars', 'yahoo', '43things', 'batman', 'SpiderMan', 'harrypotter', 'army', 'blazed', '101puppies'])
             em = discord.Embed(colour=discord.Colour.blue(), title='Your custom logo:')
             brand = text.replace(" ","%20")
             em.set_image(url=f'http://createfunnylogo.com/logo/{a}/{brand}.jpg')
             await ctx.send(embed=em)

        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def doge(ctx, *message):
            if message is None:
                    return await ctx.send("**Please put a message to run this command!**")
            if message is not None:
                    i = ('http://dogr.io/' + '/'.join(message) + '/.png?split=false')
                    em = discord.Embed(title="Wow, much doge, such amazing!", color=0xe67e22)
                    em.set_image(url=i)
                    em.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=em)

        @commands.command(aliases=['cursed-images', 'cursedimage', 'cursedimages', 'cursed-image'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def cursed(self, ctx):
          with open("data/cursed.json", "r") as f:
             res = json.load(f)
             gay = random.choice(res['image'])
          embed = discord.Embed(title="Random Cursed Images", color=discord.Color.green())
          embed.set_image(url=gay)
          embed.timestamp = datetime.datetime.utcnow()
          await ctx.send(embed=embed)


        @commands.command(aliases=['mc', 'minecraft'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def achievement(self, ctx, *message):
         if message is None:
                 return await ctx.send("**Please put a message to run this command!**")
         if message is not None:
                 i = ('https://www.minecraftskinstealer.com/achievement/a.php?i=1&h=Achievement+get%21&t=' + '+'.join(message))
                 em = discord.Embed(title="", color=0xe67e22)
                 em.set_image(url=i)
                 await ctx.send(embed=em)

def setup(bot):
        bot.add_cog(Images(bot))
