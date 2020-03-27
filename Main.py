import os
import Dictionary
import TeamRandomizer

import discord
from discord.ext import commands

# import token
TOKEN = 'NDg3MDgzMjc3NDUxMTMyOTQw.Xn1elQ.-OxpLwZgtZGAZ8lc4XQ4aQOBbCE'
print(TOKEN)

# Connect to client
bot = commands.Bot(command_prefix='~')


@bot.event
async def on_ready():
    print("Bot has connected to discord")


# Returns a Noun and Verb definition of a word if a definition is found
@bot.command(name='define')
async def _define(channel, word):

    embed = discord.Embed()

    definition = Dictionary.definition(word)

    # Set embed to error message if no definition is found
    if not definition:
        embed.color = 0xFF0000  # Red
        embed.title = "Unable to find a definition for '" + word + "'"

    # Set embed to noun or verb definitions
    else:
        embed.color = 0x00FF00  # Green
        embed.title = "Here is what I found for '" + word + "'"
        try:
            noun = definition['Noun'][0] + "\n\n"
            embed.add_field(name="Noun:", value=noun, inline=False)
        except:
            pass

        try:
            verb = definition['Verb'][0] + "\n\n"
            embed.add_field(name="Verb:", value=verb, inline=False)
        except:
            pass

    await channel.send(embed=embed)


# Takes a string in num_teams,player1,player2...player_n
# Returns a set of randomized teams as an embed
@bot.command(name='team')
async def _define(channel, msg):
    embed = discord.Embed()

    split_msg = msg.split(',')
    num_teams = split_msg[0]  # Gets the number of teams from input array
    players = []
    for i in range(1, len(split_msg)):  # Isolate all players from input array
        players.append(split_msg[i])
    teams = TeamRandomizer.get_teams(num_teams, players)  # Randomize teams

    embed.title = "Here are your teams:"

    team_number = 1
    for team in teams:  # Format embed output
        embed.add_field(name="Team " + str(team_number), value=str(team), inline=False)
        team_number = team_number + 1

    await channel.send(embed=embed)


# send TOKEN to client
bot.run(TOKEN)
