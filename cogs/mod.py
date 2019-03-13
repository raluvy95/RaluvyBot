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


class Mod():
        def __init__(self, bot):
                self.bot = bot




        @commands.command()
        @commands.has_permissions(kick_members=True)
        async def kick(self, ctx, member: discord.Member = None, *, message=None):
                try:
                     if member is None:
                          return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,kick <member>`!**")
                     else:
                          if member is ctx.author:
                               return await ctx.send("<:RaluvyError:489805076118896690> | **I can't kick you! ;-;**")
                          if member.guild_permissions.administrator is True:
                               return await ctx.send("<:RaluvyError:489805076118896690> | **I don't kick because that user is a Administrator permission**")
                          if message is None:
                               await member.kick(reason=f"Requested by {ctx.author}")
                               await ctx.send(f"**{member} was kicked!**")
                          else:
                               try:
                                  await member.kick(reason=f"{message} | {ctx.author}")
                                  await ctx.send(f"**{member} was kicked!\nReason:** {message}")
                               except:
                                  await member.kick(reason=f"Requested by {ctx.author}")
                                  await ctx.send(f"**{member} was kicked!**")
                except discord.Forbidden as owo:
                     return await ctx.send(f"Ops... I can't kick because\n`{owo}`")

        @commands.command()
        @commands.has_permissions(ban_members=True)
        async def softban(self, ctx, member: discord.Member = None, *, message=None):
                try:
                        if member is None:
                              return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,softban <member>`!**")
                        else:
                              if member is ctx.author:
                                      return await ctx.send("<:RaluvyError:489805076118896690> | **I can't softban you! ;-;**")
                              if member.guild_permissions.administrator is True:
                                      return await ctx.send("<:RaluvyError:489805076118896690> | **I don't softban because that user is a Administrator permission**")
                              if message is None:
                                      await member.ban(reason=f"Requested by {ctx.author}")
                                      await member.unban()
                                      await ctx.send(f"**{member} was kicked! (softban)**")
                              else:
                                      try:
                                          await member.ban(reason=f"{message} | {ctx.author}")
                                          await member.unban()
                                          await ctx.send(f"**{member} was kicked! (softban)\nReason:** {message}")
                                      except:
                                          await member.ban(reason=f"Requested by {ctx.author}")
                                          await member.unban()
                                          await ctx.send(f"**{member} was kicked! (softban)**")
                except discord.Forbidden as owo:
                        return await ctx.send(f"Ops... I can't kick because\n`{owo}`")

        @commands.command()
        @commands.has_permissions(ban_members=True)
        async def ban(self, ctx, member: discord.Member = None, *, message=None):
                try:
                        if member is None:
                              return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,ban <member>`!**")
                        else:
                              if member is ctx.author:
                                     return await ctx.send("<:RaluvyError:489805076118896690> | **I can't ban you! ;-;**")
                              if member.guild_permissions.administrator is True:
                                     return await ctx.send("<:RaluvyError:489805076118896690> | **I don't ban because that user is a Administrator permission**")
                              if message is None:
                                     await member.ban(reason=f"Requested by {ctx.author}")
                                     await ctx.send(f"**{member} was banned!**")
                              else:
                                   try:
                                        await member.ban(reason=f"{message} | {ctx.author}")
                                        await ctx.send(f"**{member} was banned!\nReason:** {message}")
                                   except:
                                        await member.ban(reason=f"Requested by {ctx.author}")
                                        await ctx.send(f"**{member} was banned!**")
                except discord.Forbidden as owo:
                                     return await ctx.send(f"Ops... I can't kick because\n`{owo}`")

        @commands.command(aliases=['nickname'])
        @commands.has_permissions(manage_nicknames=True)
        async def nick(self, ctx, member: discord.Member=None, *, uwu):
             try:
                  if uwu == "remove":
                      await member.edit(nick=member.name)
                      return await ctx.message.add_reaction('\U00002705')
                  if member is not None and uwu is not None:
                      await member.edit(nick=f'{uwu}')
                      return await ctx.send("Done! :white_check_mark: ")
                  if member is not None and uwu is None:
                      return await ctx.send(":x: Please use `,nick <mention> <new nick> [remove]`")
                  if member is None and uwu is None:
                      return await ctx.send(":x: Please use `,nick <mention> <new nick> [remove]`")
             except discord.Forbidden as owo:
                  return await ctx.send(f"**Ops... I can't change because:**\n`{owo}`")

        @commands.group(aliases=['rank'])
        @commands.has_permissions(manage_roles=True)
        async def role(self, ctx):
            if ctx.invoked_subcommand is None:
                return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please, use** `,role [add/remove] [role] [membru]`')

        @role.command()
        @commands.has_permissions(manage_roles=True)
        async def add(self, ctx, role: discord.Role, member: discord.Member):
            await member.add_roles(role)
            await ctx.send(f'<:RaluvySucces:489805130963615754> | **I added the rank `{role}` to `{member}`!**')

        @role.command()
        @commands.has_permissions(manage_roles=True)
        async def remove(self, ctx, role: discord.Role, member: discord.Member):
            await member.remove_roles(role)
            await ctx.send(f'<:RaluvySucces:489805130963615754> | **I removed the rank `{role}` to `{member}`!**')


        @commands.command(aliases=['prune', 'clear'])
        @commands.cooldown(1, 3, commands.BucketType.user)
        @commands.has_permissions(manage_messages=True)
        async def purge(self, ctx, number: int):
            if number>200:
                return await ctx.send("<:RaluvyError:489805076118896690> **Too many numbers! Try again!**")
            await ctx.message.delete()
            await ctx.channel.purge(limit=number)

def setup(bot):
        bot.add_cog(Mod(bot))
