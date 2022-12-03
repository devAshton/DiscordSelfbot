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

@bot.command()
async def random_num(ctx, num1: int, num2: int):
    await ctx.send(f"Your random number is {random.randint(num1,num2)}")

@bot.command()
async def random_str(ctx):
    strings = ["This is a string", "This is another string", "This is a third string"]
    await ctx.send(f"Your random string is **{random.choice(strings)}**")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    if message.author == bot.user:
        return
    
    elif message.content.lower() == "hi" or message.content.lower() == "hello":
        await message.channel.send(f"Hello {message.author.mention}")

    elif "https://discord.gift/" in message.content.lower():
        print("Nitro link found!")
    
    elif message.content.lower() == "react":
        await message.add_reaction("👍")

@bot.command()
async def react(ctx, *, emoji):
    emoji = emoji.split()
    for e in emoji:
        await ctx.message.add_reaction(e)

@bot.command()
async def multi_react(ctx):
    emojis = {
        '1': '1️⃣',
        '2': '2️⃣',
        '3': '3️⃣',
        '4': '4️⃣',
        '5': '5️⃣',
        }
    for emoji in emojis.values():
        await ctx.message.add_reaction(emoji)

@bot.command()
async def ban(ctx, user: discord.User, *, reason=None):
    await ctx.guild.ban(user, reason=reason)
    embed = discord_self_embed.Embed(f'Banned {user.name}',
    description=f'Username: {user.name}#{user.discriminator}\nID: {user.id}\nReason: {reason}',
    colour='ce0100',
    )
    url = embed.generate_url(hide_url=True, shorten_url=False)
    await ctx.send(url)
    await asyncio.sleep(3)
    await ctx.message.delete()

@bot.command()
async def kick(ctx, user: discord.User, *, reason=None):
    await ctx.guild.kick(user, reason=reason)
    embed = discord_self_embed.Embed(f'Kicked {user.name}',
    description=f'Username: {user.name}#{user.discriminator}\nID: {user.id}\nReason: {reason}',
    colour='ce0100',
    )
    url = embed.generate_url(hide_url=True, shorten_url=False)
    await ctx.send(url)
    await asyncio.sleep(3)
    await ctx.message.delete()

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
