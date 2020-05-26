# **Kassandra**
**Kassandra** is a bot with a small but interesting functionality. Most of them are casino mini games like Blackjack. In short, this is a gambling bot. The [past commits](https://github.com/Ghosteon/discord-bot-kassandra/tree/f2d8b270daa521e41a7adf9bae63fbaad7356578) of this repository contain the terminal based version of Blackjack that I made two years ago.

## Commands
The default command prefix is **`&`**. You can see the whole list of commands by **`&help`** command.

## Features
- Economy *(coming soon)*
- **Blackjack** [playing by emoji]
- Baccarat *(coming soon)*
- **Slots** [20 lines, 5 reels, wild symbol]
- **Mini games** [coinflip, roll, russian roulette, colors]

## Running

#### Requirements
1. python 3.6
2. async-timeout 3.0.1
3. discord.py 1.3.3
4. dotenv-python 0.0.1

#### Preparing
Create a **.env** file in the same directory where the *bot.py* file is stored. The file should contain your token in the following form: **`DISCORD_TOKEN=token`**

#### Launching
Start bot by running **bot.py** file.
