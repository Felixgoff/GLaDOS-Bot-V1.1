from tkinter import W
from discord.ext import commands
import discord
import asyncio
import random
from asyncio import sleep

activity = discord.Activity(name='Cheetos Diss Track', type=discord.ActivityType.listening)

TOKEN = 'OTU3MTc2MjUyNzE0ODUyMzgy.G864qN.72cF4D-9b8MZYkE2Wm1E3acmgXvOVOwael-3Pg'

bot = commands.Bot(command_prefix = '-', activity=activity)

@bot.event
async def on_ready():
    print('Still Alive.')
@bot.command(name='join')
async def join(ctx):
    voicestate = ctx.author.voice
    if voicestate is None:
        return print('you aint in a vc')
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name="gone")
async def gone(ctx):
    voicestate = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if voicestate is None:
        return  print('aint in a vc')
    await ctx.voice_client.disconnect()   

@bot.command(name="joe")
async def joe(ctx):
    await ctx.send('mama')

@bot.command(name="play")
async def play(ctx):
    for attachment in ctx.message.attachments:
        if attachment.content_type in ('audio/mpeg'):
            voice_channel = ctx.author.voice.channel
            vc = await voice_channel.connect()
            source = attachment.url
            vc.play(discord.FFmpegPCMAudio(source), after= await tricky(ctx, attachment))
            while vc.is_playing():
                await sleep(3)
            await vc.disconnect()
async def tricky(ctx, attachment):
    await ctx.send(attachment.filename)

@bot.command(name="shit")
async def shit(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    source = 'https://cdn.discordapp.com/attachments/904291192664117268/985491244094459914/shit.mp3'
    vc.play(discord.FFmpegPCMAudio(source), after=None)
    while vc.is_playing():
        await sleep(3)
    await vc.disconnect()

@bot.command(name="fart")
async def fart(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    source = 'https://cdn.discordapp.com/attachments/904291192664117268/985487924508364830/fart.mp3'
    vc.play(discord.FFmpegPCMAudio(source), after=None)
    while vc.is_playing():
        await sleep(3)
    await vc.disconnect()

@bot.command(name="creepa")
async def creepa(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    source = 'https://cdn.discordapp.com/attachments/904291192664117268/985487924311236678/creepa.mp3'
    vc.play(discord.FFmpegPCMAudio(source), after=None)
    while vc.is_playing():
        await sleep(3)
    await vc.disconnect()

@bot.command(name="cheetos")
async def cheetos(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    source = 'https://cdn.discordapp.com/attachments/708431474239733832/1003384218132430928/cheetos.mp3'
    vc.play(discord.FFmpegPCMAudio(source), after=None)
    while vc.is_playing():
        await sleep(3)
    await vc.disconnect()

@bot.command(name="nuke")
async def nuke(ctx, arg):
   x = ctx.guild.text_channels
   z = ctx.guild.voice_channels
   for i in range (10000):
    print(i)
    await random.choice(x).send(arg)







bot.run(TOKEN)