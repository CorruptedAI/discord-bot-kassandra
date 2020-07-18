import discord
from discord.ext import commands

from bot import COMMAND_PREFIX


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.description_length = 70
        self.formats = [".jpg", ".png", ".jpeg", ".webp"]

    @commands.command()
    @commands.guild_only()
    async def config(self, ctx, option: str = None):
        if option == "description":
            await ctx.channel.send(
                "Please enter a **description**. You have only 90sec to enter. If you want to cancel your action, send `cancel`:"
            )
        elif option == "background":
            await ctx.channel.send(
                f"Please enter a **background** link or send a picture right here. Supported formats: {' '.join(map(str, self.formats))}. You have only 90sec to enter. If you want to cancel your action, send `cancel`:"
            )
        else:
            return await ctx.channel.send(
                f":x: Choose what you want to change. To change the description, enter `{COMMAND_PREFIX}config description`. To change the background, enter `{COMMAND_PREFIX}config background`. Before entering both commands, please have a look at `{COMMAND_PREFIX}help config` command"
            )

        def check_author(message):
            if ctx.author == message.author:
                return True

        try:
            value = await self.bot.wait_for("message", check=check_author, timeout=90.0)
        except asyncio.TimeoutError:
            return

        if value:
            if value.content.lower() == "cancel":
                return await ctx.channel.send(
                    f":x: {option.capitalize()} change canceled"
                )
            if option == "description" and len(value.content) > self.description_length:
                return await ctx.channel.send(
                    f":x: Your description is too long! The maximum description length is {self.description_length}. Enter `{COMMAND_PREFIX}config description` to try again"
                )
            elif option == "background":
                check = False
                for form in self.formats:
                    if form in value.content:
                        check = True
                if not check:
                    return await ctx.channel.send(
                        f":x: You entered an unsupported format. Supported formats: {' '.join(map(str, self.formats))}. Enter `{COMMAND_PREFIX}config background` to try again"
                    )

            await self.bot.pg_con.execute(
                f"""
                UPDATE users
                SET {option} = $1
                WHERE user_id = $2
                AND guild_id = $3
                """,
                value.content,
                ctx.author.id,
                ctx.guild.id,
            )

            await ctx.channel.send(
                f"Your {option} has been changed! You can view your profile by entering `{COMMAND_PREFIX}profile` command"
            )


def setup(bot):
    bot.add_cog(Config(bot))
