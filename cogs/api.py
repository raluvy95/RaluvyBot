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


class API():
        def __init__(self, bot):
                self.bot = bot




        @commands.command(aliases=['shibainu'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def shiba(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false') as r:
                                res = await r.json()
                                embed = discord.Embed(color=0x000000)
                                embed.title = "Awww, a doge!"
                                embed.set_image(url=str(res).strip("[']"))
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)




        @commands.command(aliases=['woof'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def dog(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get("http://random.dog/woof.json") as r:
                                res = await r.json()
                                embed = discord.Embed(color=0x000000)
                                embed.title = '\U0001f436 Woof!'
                                embed.set_image(url=res['url'])
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)



        @commands.command(aliases=['meow'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def cat(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get('https://some-random-api.ml/img/cat') as r:
                                res = await r.json()
                                embed = discord.Embed(color=0x000000)
                                embed.title = "\U0001f431 Meoww...!"
                                embed.set_image(url=res['link'])
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)

        
        @commands.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def meme(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get("https://some-random-api.ml/meme") as r:
                                res = await r.json()
                                embed = discord.Embed(color=discord.Colour.red())
                                embed.title = (res['caption'])
                                embed.set_image(url=res['image'])
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)
                                
        @commands.command(aliases=['pokedex', 'poked'])
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def pokemon(self, ctx, name=None):
                if name is None:
                        return await ctx.send("**Emply? Try again with name of pokemon**")
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(f'https://some-random-api.ml/pokedex?pokemon={name}') as r:
                                res = await r.json()
                                try:
                                        bruh = ', '.join(g for g in res['type'])
                                        e = ', '.join(g for g in res['family']['evolutionLine'])
                                        embed = discord.Embed(title=f"ID: {res['id']} | {res['name']}", description=res["description"] ,color=0x000000)
                                        try:
                                            embed.set_thumbnail(url=res['sprites']['animated'])
                                        except:
                                            pass
                                        embed.set_author(name="Pokedex", icon_url='https://vignette.wikia.nocookie.net/freebeerz/images/8/86/Pokeball_Icon.png/revision/latest?cb=20120430172421')
                                        embed.add_field(name="Species", value=res['species'], inline=True)
                                        embed.add_field(name="Height", value=res['height'], inline=True)
                                        embed.add_field(name="Weight", value=res['weight'], inline=True)
                                        embed.add_field(name="Base exprerience", value=res['base_experience'], inline=True)
                                        embed.add_field(name="Type", value=bruh, inline=True)
                                        try:
                                            if res['family']['evolutionStage'] <= 0:
                                                embed.add_field(name="Gender ratio", value='null', inline=True)
                                            else:
                                                embed.add_field(name="Gender ratio", value=' | '.join(g for g in res['gender']), inline=True)
                                        except:
                                            embed.add_field(name="Gender ratio", value='null', inline=True)
                                        embed.add_field(name="Evolution", value=e, inline=True)
                                        await ctx.send(embed=embed)
                                except KeyError as key:
                                        await ctx.send(f"**Ops... `{name}` is not found in pokedex!**")

                                                        
        @commands.command(aliases=['pika'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def pikachu(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get("https://some-random-api.ml/pikachuimg") as r:
                                res = await r.json()
                                embed = discord.Embed(color=discord.Colour.red())
                                embed.title = 'Pika!'
                                embed.set_image(url=res['link'])
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)
                                
        @commands.command(aliases=['catfact'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def catfacts(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get("https://some-random-api.ml/facts/cat") as r:
                                res = await r.json()
                                await ctx.send(f":cat: **Did you know?**\n{res['fact']}")
                                               
        @commands.command(aliases=['dogfact'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def dogfacts(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get("https://some-random-api.ml/facts/dog") as r:
                                res = await r.json()
                                await ctx.send(f":dog: **Did you know?**\n{res['fact']}")







def setup(bot):
        bot.add_cog(API(bot))
