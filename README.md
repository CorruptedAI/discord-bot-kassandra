<p align="center" style="margin: 10px;"><a href="https://top.gg/bot/708690846735663184"><img src="https://top.gg/api/widget/708690846735663184.svg?usernamecolor=000000&topcolor=ffffff"></a></p>
<p align="center">
    <a href="https://github.com/Ghosteon/discord-bot-kassandra"><img src="https://img.shields.io/badge/deployed%20on-heroku-997fbc?style=flat-square"></a>
    <a href="https://github.com/Ghosteon/discord-bot-kassandra"><img src="https://img.shields.io/badge/python-3.8-blue?style=flat-square"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-black?style=flat-square"></a>
    <a href="https://github.com/Ghosteon/discord-bot-kassandra/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-a31f34?style=flat-square"></a>
</p>
    
**Kassandra** is a field for experimentation. Here I implement any interesting ideas, improve the finished functionality and learn from my mistakes. This source code is far from the standard and contains a lot of things that you better not see. From the functionality of this bot, you can distinguish a couple of: full-featured gambling, weather parsing, moderation commands, etc. Btw, the [past commits](https://github.com/Ghosteon/discord-bot-kassandra/tree/f2d8b270daa521e41a7adf9bae63fbaad7356578) of this repository contain the terminal based version of Blackjack that I made two years ago.

## Commands
The default command prefix is **`&`**. You can see the whole list of commands by **`&help`** command.

## Running

#### Preparing
Create a **.env** file in the same directory where the *bot.py* file is stored. The file should contain your tokens in the following form:
```
DISCORD_TOKEN=token
OPENWEATHER_TOKEN=token
```

#### Launching
Start bot by running **bot.py** file.
