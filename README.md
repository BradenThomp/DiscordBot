# DiscordBot

Text Chat Command Bot For Discord.

## Installation

Before installing the project an application must be registered from the discord developer portal.
Follow the tutorial here: https://discordpy.readthedocs.io/en/latest/discord.html

MongoDB is an optional install https://www.mongodb.com/

The following instructions require Docker to execute: https://www.docker.com/

1. Download and unzip the project.
2. Update the token in Main.py to the token of your application registered in the initial setup.
3. If not running from a raspberry pi make sure all references to RPi.GPIO are commented out. This cannot be installed on any OS besides raspian and currently I have not found a way to enable/disable based on OS.
4. If not using MongoDB set USE_MONGO = False in Main.py to mock the database.
5. Create a Docker image.

```bash
docker build -t discord-bot .
```

5. Run Container (can specify -d to free up command line)

```bash
docker run -it --rm --name discord-bot discord-bot
```

On successful setup "Bot has connected to discord" will be displayed in command line.

### Installation without docker

If installing without Docker, make sure all dependancies in requirements.txt are installed either in a virtual environment or globally.

## Usage

### MongoDB:

This Application uses MongoDB. If you do not have MongoDB installed, please set USE_MONGO = False in Main.py to use a Mock Database.

### Raspberry Pi GPIO:

If not running on the Raspberry Pi, set USE_RPI = False in Main.py to use a Mock GPIO. You will also have to comment out all references to RPi.GPIO as the application will not run on Operating System's that don't support this library.

### Commands:

This is a list of all commands that can be run from a discord text chat where all commands start waith a '~':

~dictionary "word" -- returns a definition of the input word

~team "num_teams,player_list" -- returns randomized team (all players in player_list must be split by a comma)

~LEDon -- turns on the Bat Signal (Just a LED)

~LEDoff -- turns off the Bat Signal (Also just a LED)
