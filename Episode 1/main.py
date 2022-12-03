import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import os
import discord_self_embed

load_dotenv()

bot = commands.Bot(command_prefix='>', self_bot=True)

@bot.event
async def on_ready():
    print('-' * 20)
    print('Logged in as')
    print(f'User: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('-' * 20)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def whois(ctx, user: discord.User):
    embed = discord_self_embed.Embed(f'Whois {user.name}',
    description=f'Username: {user.name}#{user.discriminator}\nID: {user.id}',
    colour='36393f',
    )
    embed.set_image(user.avatar_url)
    url = embed.generate_url(hide_url=True, shorten_url=False)
    await ctx.send(url)

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
