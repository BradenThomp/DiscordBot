# DiscordBot

Text Chat Command Bot For Discord.

## Installation

Before installing the project an application must be registered from the discord developer portal.
Follow the tutorial here: https://discordpy.readthedocs.io/en/latest/discord.html

MongoDB must also be installed to run the project https://www.mongodb.com/

### For Windows:

1. Download and unzip the project.
2. Update the token in Main.py to the token of your application registered in the initial setup.
3. Make Sure all references to RPi.GPIO are commented out. This can not be installed on windows and currently I have not found a way to enable/disable based on OS.
4. Enable Virtual Environment before running. This should contain all required packages.

```bash
env\scripts\activate
```

5. Run from command line (ex powershell)

```bash
python src/Main.py
```

### For RaspberryPi:

1. Clone the project.
2. Update the token in Main.py to the token of your application registered in the initial setup.
3. Make Sure all references to RPi.GPIO are NOT commented out. This can not be installed on windows and currently I have not found a way to enable/disable based on OS.
4. Enable Virtual Environment before running. This should contain all required packages.

```bash
env\scripts\activate
```

5. Run from command line (ex powershell)

```bash
python src/Main.py
```

On successful setup "Bot has connected to discord" will be displayed in command line

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
