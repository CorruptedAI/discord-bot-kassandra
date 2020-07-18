import discord
from discord.ext import commands


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.invite_link = "bit.ly/kassandrabot"

    @commands.command()
    @commands.guild_only()
    async def info(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        roles = [role for role in member.roles]
        del roles[0]

        embed = discord.Embed(color=member.color)
        embed.set_author(name=f"{member}")
        embed.set_thumbnail(url=member.avatar_url)

        embed.add_field(
            name="Account created",
            value=member.created_at.strftime("%a, %#d %B %Y, %H:%M:%S"),
            inline=False,
        )

        embed.add_field(
            name="Joined at",
            value=member.joined_at.strftime("%a, %#d %B %Y, %H:%M:%S"),
            inline=False,
        )

        embed.add_field(
            name="Join position",
            value=sum(
                m.joined_at < member.joined_at
                for m in ctx.guild.members
                if m.joined_at is not None
            )
            + 1,
            inline=False,
        )

        val = ", ".join([role.mention for role in roles])
        embed.add_field(
            name=f"Roles [{len(roles)}]",
            value="None" if val == "" else val,
            inline=False,
        )

        embed.add_field(
            name="Bot",
            value=":white_check_mark:" if member.bot else ":x:",
            inline=False,
        )

        embed.add_field(
            name="Invite link",
            value=f"[{self.invite_link}](https://{self.invite_link})",
            inline=False,
        )

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
