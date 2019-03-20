print("Connecting...")
import discord
import random
import datetime
import traceback
import aiohttp
import asyncio
from discord import opus
import async_timeout
from random import randint
from discord.ext import commands
from discord.utils import find
from asyncio import sleep
import logging
import time
import os
import json

with open("data/config.json", "r") as f:
    kek = json.load(f)

print("Loading commands...")
bot = commands.Bot(command_prefix=kek['prefix'])
logging.basicConfig(level='INFO')
bot.remove_command('help')
bot.load_extension("cogs.admin")
bot.load_extension("cogs.api")
bot.load_extension("cogs.mod")
bot.load_extension("cogs.mineswepper")
bot.load_extension("cogs.utility")
bot.load_extension("cogs.info")
bot.load_extension("cogs.images")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.text")
# only in v0.3 bot.load_extension("cogs.music")
# only in v0.2 bot.load_extension("cogs.sound")

@bot.event
async def on_guild_join(guild):
    print (f"+1 {guild.name}| ID {guild.id}")
    em = discord.Embed(title=f"+1 server (Total: {len(bot.guilds)})", color=0xe67e22)
    em.add_field(name="Name Server", value=guild.name, inline=True)
    em.add_field(name="ID", value=guild.id, inline=True)
    em.add_field(name="Owner Server", value=guild.owner, inline=True)
    em.add_field(name="Members", value=guild.member_count, inline=True)
    em.add_field(name="New members on the bot", value=len(bot.users), inline=True)
    em.set_thumbnail(url=guild.icon_url)
    em.timestamp = datetime.datetime.utcnow()
    await bot.get_guild(489498283194974210).get_channel(520218875493744660).send(embed=em)

    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('**Thanks for added me! <a:ablobdancewhite:464794007755685898>\nMy prefix is `,` Use `,help` for list commands!\nSo if you found a bug/glitch command(s) or have a question about this bot, use `,support` for join our support server! Enjoy!** :hugging:')


@bot.event
async def on_guild_remove(guild):
    print (f"-1 {guild.name}| ID {guild.id}")
    em = discord.Embed(title=f"-1 server (Total: {len(bot.guilds)})", color=0xe67e22)
    em.add_field(name="Name Server", value=guild.name, inline=True)
    em.add_field(name="ID", value=guild.id, inline=True)
    em.add_field(name="Owner Server", value=guild.owner, inline=True)
    em.add_field(name="Members", value=guild.member_count, inline=True)
    em.add_field(name="New members on the bot", value=len(bot.users), inline=True)
    em.set_thumbnail(url=guild.icon_url)
    em.timestamp = datetime.datetime.utcnow()
    await bot.get_guild(489498283194974210).get_channel(520218875493744660).send(embed=em)

@bot.listen()
async def on_member_remove(member):
    if member.guild.id == 464783042310045707:
        em = discord.Embed(color=discord.Colour.red())
        em.add_field(name='Goodbye!', value=f"<a:Leave:503203313076928518> {member.mention}", inline=False)
        em.add_field(name='Info', value='Ne-a parasit... Speram sa revii, esti mereu bine venit :sob:', inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await bot.get_guild(464783042310045707).get_channel(464783042310045709).send(embed=em)
    if member.guild.id != 464783042310045707:
        return

@bot.listen()
async def on_member_join(member):
    if member.guild.id == 464783042310045707:
        em = discord.Embed(color=discord.Colour.green())
        em.add_field(name='Welcome', value=f"<a:Join:503203359097094154> {member.mention}", inline=False)
        em.add_field(name='Info', value='Nu uita sa citesti <#464789280368230400> inainte de a scrii pe chat!\n**Nu poti sa scrii aici? Intra pe <#532601194670063619> si apasa pe reactia.**', inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await bot.get_channel(464783042310045709).send(embed=em)
    if member.guild.id != 464783042310045707:
        return

@bot.event
async def on_ready():
 print('Logged in as')
 print(bot.user.name)
 print(bot.user.id)
 print("Discord.py API version:", discord.__version__)
 with open("data/config.json", "r") as f:
     nvm = json.load(f)
 print("Bot's prefix is " + nvm['prefix'])

@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      return
    print(f'\'{ctx.author}\' used command \'{ctx.command}\' on \'{ctx.guild.name} and got this error: \n{error}')
    em = discord.Embed(title=f"Error!", color=discord.Color.red())
    em.add_field(name="Command name", value=ctx.command, inline=False)
    em.add_field(name="User", value=ctx.author, inline=True)
    em.add_field(name="User ID", value=ctx.author.id, inline=True)
    em.add_field(name="Channel name", value=ctx.channel.name, inline=True)
    em.add_field(name="Channel ID", value=ctx.channel.id, inline=True)
    em.add_field(name="Server name", value=ctx.guild.name, inline=True)
    em.add_field(name="Server ID", value=ctx.guild.id, inline=True)
    em.add_field(name="Error:", value=error, inline=False)
    em.timestamp = datetime.datetime.utcnow()
    await bot.get_guild(489498283194974210).get_channel(530107395247177740).send(embed=em)
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(f':no_entry:  | This command is on cooldown... **[{int(error.retry_after)} seconds]**', delete_after=5)
    if isinstance(error, commands.NotOwner):
        return await ctx.send('<:RaluvyWarning:489805114224410625> | **You do not own this bot!**')
    if isinstance(error, commands.BadArgument):
        return await ctx.send(f'<:RaluvyError:489805076118896690> | **{error}**')
    if isinstance(error, commands.MissingPermissions):
        return await ctx.send('<:RaluvyForbidden:489805084650110976> | **You are missing permission to execute this command!**')
    if isinstance(error, commands.BotMissingPermissions):
        return await ctx.send('<:RaluvyForbidden:489805084650110976> | **I am missing permission to perform this command!**')


@bot.listen()
async def on_message(message):
    if message.content.lower() == '<@489061565430235136>' and message.author != bot.user:
        await message.channel.send('**My prefix is `,` | Use `,help` for show commands.**')
    else:
        return

@bot.listen()
async def on_message(message):
    if message.content.lower() == '<@!489061565430235136>' and message.author != bot.user:
        await message.channel.send('**My prefix is `,` | Use `,help` for show commands.**')
    else:
        return
@bot.command(hidden=True)
async def new(ctx, *, oame=None):
    if ctx.author.guild.id == 464783042310045707:
        if oame is None:
            return await ctx.send("**Please use `,new {think}`**")
        else:
            boi = await ctx.guild.create_text_channel(name=oame)
            owo = discord.utils.get(ctx.guild.roles, name="@everyone")
            await boi.set_permissions(ctx.author, read_messages=True)
            await boi.set_permissions(owo, read_messages=False)
            await ctx.send(f"**Done! Please check in {boi.mention}!**")
    else:
        return

async def presence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        a = 0
        for i in bot.guilds:
            for u in i.members:
                if u.bot == False:
                    a = a + 1

        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="i like cookies || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=",invite || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="Noice || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.users)} users || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers || ,help"))
        await sleep(30)


bot.loop.create_task(presence())
bot.run(os.getenv("TOKEN"))
