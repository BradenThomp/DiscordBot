# DiscordBot
Text Chat Command Bot For Discord.

## Installation

Before installing the project an application must be registered from the discord developer portal.
Follow the tutorial here: https://discordpy.readthedocs.io/en/latest/discord.html

MongoDB must also be installed to run the project https://www.mongodb.com/

### For Pycharm Development and Windows Deployment:

1) Download and unzip the project.
2) Update the token in Main.py to the token of your application registered in the initial setup.
3) Run from command line (ex powershell)

```bash
python3.5 main
```

### For RaspberryPi Deployment:

1) Clone the project
2) Install Required Dependancies

```bash
pip3 install PyDictionary
pip3 install Discord.py
sudo apt-get install python3-numpy
pip3 install pymongo==3.4.0
```

3) Update the token in Main.py to the token of your application registered in the initial setup
4) Run from command line

```bash
python3.5 Main.py
```

On successful setup "Bot has connected to discord" will be displayed in command line

## Usage

This is a list of all commands that can be run from a discord text chat where all commands start waith a '~':

~dictionary "word" -- returns a definition of the input word

~team "num_teams,player_list" -- returns randomized team  (all players in player_list must be split by a comma)
