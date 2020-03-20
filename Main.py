import os
import Dictionary

import discord
from discord.ext import commands
from dotenv import Dotenv

# import token
env_values = Dotenv(os.path.join(os.path.dirname(__file__), ".env"))
TOKEN = env_values['DISCORD_TOKEN']
print(TOKEN)

# Connect to client
bot = commands.Bot(command_prefix='~')


@bot.event
async def on_ready():
    print("Bot has connected to discord")


@bot.command(name='define')
async def _define(channel, word):
    definition = Dictionary.definition(word)
    embed = discord.Embed(
        title="Here is what I found for " + word,
        description=definition
    )
    await channel.send(embed=embed)

# send TOKEN to client
bot.run(TOKEN)
