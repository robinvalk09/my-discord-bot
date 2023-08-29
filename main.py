import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()

@bot.command()
async def quote(ctx):
    quotes = [
        "Now I am become Death, the destroyer of worlds.",
        "The atomic bomb made the prospect of future war unendurable. It has led us up those last few steps to the mountain pass; and beyond there is a different country.",
        "The optimist thinks this is the best of all possible worlds. The pessimist fears it is true.",
        # Add more quotes here
    ]
    
    random_quote = random.choice(quotes)
    await ctx.send(f'"{random_quote}"')

bot.run('youre discord token')

