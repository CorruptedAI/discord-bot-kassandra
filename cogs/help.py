import discord
from discord.ext import commands

from bot import COMMAND_PREFIX


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

        self.invite_link = "bit.ly/kassandrabot"

    @commands.command(aliases=["h"])
    async def help(self, ctx, arg="default"):
        embed = discord.Embed(
            title=f"Command prefix: `{COMMAND_PREFIX}`",
            description=f"Use `{COMMAND_PREFIX}help [command]` to get more\ninformation about each command",
            color=self.bot.user.color,
        )

        embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        if ctx.guild:
            if arg == "default":
                embed.add_field(
                    name=":slot_machine: **Games**",
                    value="`blackjack` `slots`\n`baccarat` `mafia`",
                    inline=False,
                )
                embed.add_field(
                    name=":ticket: **Fun**",
                    value="`flip` `roll` `duel`\n`roulette` `8b`",
                    inline=False,
                )
                embed.add_field(
                    name=":satellite: **Social**",
                    value="`info` `profile` `daily`\n`balance` `shop` `gift`\n`leaderboard`",
                    inline=False,
                )
                embed.add_field(
                    name=":gear: **Utilities**",
                    value="`weather` `avatar`\n`config` `ping`",
                    inline=False,
                )

            elif arg == "help":
                embed = discord.Embed(
                    title="Help",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}help`
                    Aliases: `help` `h`
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "blackjack" or arg == "bj":
                embed = discord.Embed(
                    title="Blackjack",
                    description=f"""
                    You can learn more about this game [here](https://en.wikipedia.org/wiki/Blackjack).
                    Command syntax: `{COMMAND_PREFIX}blackjack [bet]`
                    Aliases: `blackjack` `bj`
                    
                    [bet] is an amount of Chips. You can see
                    your balance with `{COMMAND_PREFIX}balance command`.

                    In this version of the game dealer *must* stop when
                    it reaches 17 points or more.

                    Every game that you start, you start with new deck.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "slots" or arg == "slot":
                embed = discord.Embed(
                    title="The Slots",
                    description=f"""
                    You can learn more about this game [here](https://en.wikipedia.org/wiki/Slot_machine).
                    Command syntax: `{COMMAND_PREFIX}slots [bet]`
                    Aliases: `slots` `slot`
                    
                    [bet] is an amount of Chips. You can see
                    your balance with `{COMMAND_PREFIX}balance command`.

                    The Slots has 5 reels and 20 lines.

                    Each result is highlighted if you won.

                    Lines and win odds aren't available to the user
                    at the moment, but you can find it in the source code.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "baccarat" or arg == "baccara" or arg == "bac":
                embed = discord.Embed(
                    title="Baccarat",
                    description=f"""
                    You can learn more about this game [here](https://en.wikipedia.org/wiki/Baccarat_(card_game)).
                    Command syntax: `{COMMAND_PREFIX}baccarat [bet]`
                    Aliases: `baccarat` `baccara` `bac`
                    
                    [bet] is an amount of Chips. You can see
                    your balance with `{COMMAND_PREFIX}balance command`.

                    ...in development
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "mafia":
                embed = discord.Embed(
                    title="Mafia",
                    description=f"""
                    You can learn more about this game [here](https://en.wikipedia.org/wiki/Mafia_(party_game)).
                    Command syntax: `{COMMAND_PREFIX}mafia`
                    Aliases: `mafia`
                    
                    ...in development
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "flip":
                embed = discord.Embed(
                    title="Coin flipping",
                    description=f"""
                    You can learn more about it [here](https://en.wikipedia.org/wiki/Coin_flipping).
                    Command syntax: `{COMMAND_PREFIX}flip`
                    Aliases: `flip`
                    Cost: 1 ticket
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "roll":
                embed = discord.Embed(
                    title="Roll Dice",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}roll [faces]`
                    Aliases: `flip`
                    Cost: 1 ticket

                    [faces] is a number of faces of one Dice.
                    Default values is 6.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "duel":
                embed = discord.Embed(
                    title="Duel",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}duel [@Member]`
                    Aliases: `duel`
                    Cost: 1 ticket

                    ...in reworking
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "roulette":
                embed = discord.Embed(
                    title="Russian Roulette",
                    description=f"""
                    You can learn more about this game [here](https://en.wikipedia.org/wiki/Russian_roulette).
                    Command syntax: `{COMMAND_PREFIX}roulette`
                    Aliases: `roulette`
                    Cost: 1 ticket

                    If you die, you will be muted for
                    10 minutes and marked as Dead Man.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "8b":
                embed = discord.Embed(
                    title="Magic 8-Ball",
                    description=f"""
                    You can learn more about it [here](https://en.wikipedia.org/wiki/Magic_8-Ball).
                    Command syntax: `{COMMAND_PREFIX}m8b [question]`
                    Aliases: `8b`
                    Cost: 1 ticket
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "info":
                embed = discord.Embed(
                    title="Information",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}info [@Member]`
                    Aliases: `info`

                    Shows information about the [@Member].
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "profile":
                embed = discord.Embed(
                    title="Profile",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}profile [@Member]`
                    Aliases: `profile`

                    Shows [@Member] profile.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "daily":
                embed = discord.Embed(
                    title="Daily Reward",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}daily`
                    Aliases: `daily`
                    
                    Shows the status of receiving the daily 50-chip reward.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "balance":
                embed = discord.Embed(
                    title="Balance",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}balance`
                    Aliases: `balance` `bal`
                    
                    Shows the status of receiving the daily 50-chip reward.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "shop":
                embed = discord.Embed(
                    title="Shop",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}shop`
                    Aliases: `shop`
                    
                    Shows a shop with spellbooks, experiences and tickets.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "gift":
                embed = discord.Embed(
                    title="Gifting",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}gift [@Member] [amount]`
                    Aliases: `gift`
                    
                    Allows you to give the [@Member] [amount] chips.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "leaderboard":
                embed = discord.Embed(
                    title="Leaderboard",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}leaderboard [option]`
                    Aliases: `leaderboard`
                    
                    Shows the leaderboard.
                    [option] can be [local] and [global]
                    [local] is your server
                    [global] is all servers
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "weather":
                embed = discord.Embed(
                    title="Weather",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}weather [city]`
                    Aliases: `weather`
                    DM: +
                    
                    Shows the weather of the [city].
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "avatar":
                embed = discord.Embed(
                    title="Avatar",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}avatar [@Member]`
                    Aliases: `avatar`
                    
                    Shows the [@Member]'s avatar.
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "config":
                embed = discord.Embed(
                    title="Config",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}config [option]`
                    Aliases: `config`
                    
                    Allows you to customize the background
                    and profile description.

                    [option] can be [background] or [description].
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

            elif arg == "ping":
                embed = discord.Embed(
                    title="Pong",
                    description=f"""
                    Command syntax: `{COMMAND_PREFIX}ping`
                    Aliases: `ping`
                    DM: +
                    
                    Pong!
                    """,
                    color=self.bot.user.color,
                )

                embed.set_author(name="Help", icon_url=self.bot.user.avatar_url)

        else:
            embed.description = "In DM, only a few commands\nare available to you, since\nother commands are tied to\ncurrency, levels and profile.\nTo see the full list of commands,\nenter the `&help` command\non the server\n"
            embed.add_field(
                name=":gear: **Utilities**", value="`weather` `ping`", inline=False,
            )
            embed.add_field(
                name="If you want to see me on\nyour server, use this link",
                value=f"[{self.invite_link}](https://{self.invite_link})",
                inline=False,
            )

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
