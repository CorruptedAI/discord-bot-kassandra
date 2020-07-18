<p align="center" style="margin: 10px;"><a href="https://top.gg/bot/708690846735663184"><img src="https://top.gg/api/widget/708690846735663184.svg?usernamecolor=000000&topcolor=ffffff"></a></p>
<p align="center">
    <a href="https://github.com/Ghosteon/discord-bot-kassandra"><img src="https://img.shields.io/badge/python-3.8-blue?style=flat-square"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-black?style=flat-square"></a>
    <a href="https://github.com/Ghosteon/discord-bot-kassandra/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-a31f34?style=flat-square"></a>
</p>
    
**Kassandra** is a field for experimentation. Here I implement any interesting ideas, improve the finished functionality and learn from my mistakes. This source code is far from the standard and contains a lot of things that you better not see. From the functionality of this bot, you can distinguish a couple of: full-featured gambling, weather parsing, moderation commands, etc. Btw, the [past commits](https://github.com/Ghosteon/discord-bot-kassandra/tree/f2d8b270daa521e41a7adf9bae63fbaad7356578) of this repository contain the terminal based version of Blackjack that I made two years ago.

## Commands
The default command prefix is **`&`**. You can see the whole list of commands by **`&help`** command.

## Running

#### Preparing
##### Setup .env
Create a **.env** file in the same directory where the *bot.py* file is stored. The file should contain your data in the following form:
```
DISCORD_TOKEN=token
POSTGRESQL_HOST=host
POSTGRESQL_PORT=port
POSTGRESQL_PASSWORD=password
OPENWEATHER_TOKEN=token
TOPGG_TOKEN=token
```
If you use Postgre on your local machine, database data should look like this:
```
POSTGRESQL_HOST=localhost
POSTGRESQL_PORT=5432
POSTGRESQL_PASSWORD=password
```
##### Database Schema
Create *kassandra_economy* database with the following Table:
```
CREATE TABLE public.users
(
    user_id bigint NOT NULL,
    guild_id bigint NOT NULL,
    level integer NOT NULL,
    exp integer NOT NULL,
    coins double precision NOT NULL,
    tickets integer NOT NULL,
    daily character varying COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    background character varying COLLATE pg_catalog."default" NOT NULL,
    language character varying COLLATE pg_catalog."default" NOT NULL
)
```
##### Install dependencies
In this step, just enter `pip install -U -r requirements.txt`.

#### Launching
Start bot by running **bot.py** file.
