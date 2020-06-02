import Dictionary
import TeamRandomizer
#from PiLEDController import PiLEDController
from RaspberryPi.BasePiLEDController import BasePiLEDController
from Database.MongoCollection import MongoCollection
from Database.BaseCollection import BaseCollection

import discord
from discord.ext import commands

### SETUP ###

USE_MONGO = False
USE_RPI = False

if USE_MONGO:
    print('Using MongoDB...')
    # Connect to MongoDB Collection
    comment_col = MongoCollection(dbstr='DiscordMessageDatabase', colstr='messages')
else:
    print('Using MockDB...')
    # Use the base collection for testing
    comment_col = BaseCollection()
    
if USE_RPI:
    print('Using Raspberry Pi GPIO...')
    # Set up Raspberry Pi LEDs
    #LED_21 = PiLEDController(21)    
else:
    print('Using Mock GPIO...')
    LED_21 = BasePiLEDController()

# import token
TOKEN = 'YOUR_TOKEN'
print(TOKEN)

# Connect to client
bot = commands.Bot(command_prefix='~')

### COMMANDS ###

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


# Turns an LED on a RaspberryPi on
@bot.command(name='LEDon')
async def _define(channel):
    LED_21.poweron()


# Turns an LED on a RaspberryPi off
@bot.command(name='LEDoff')
async def _define(channel):
    LED_21.poweroff()


@bot.event
async def on_message(msg):
    if msg[0] == '~':
        return
    if msg.author == bot.user:
        return
    await bot.process_commands(msg)  # process all commands
    print(msg)
    msg_dict = {'_id': msg.id, 'author_id': msg.author.id, 'author_name': msg.author.name,       # convert a message into a dictionary
                'author_discriminator': msg.author.discriminator, 'author_nick': msg.author.nick,
                'content': msg.content, 'created_at': msg.created_at}
    print(msg_dict)
    comment_col.save(msg_dict)  # save message to collection

# send TOKEN to client
bot.run(TOKEN)
