import discord
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(color=self.bot.user.color) 
        embed.set_image(url=self.bot.user.avatar_url)
        await ctx.channel.send(
            '''
Hi, I'm Kassandra, my father is **Ghosteon#2776**. I was created to bring pleasure and fun. But my
father said that he was just testing the Discord API and remaking his old mini project... In any case, I'm
glad that I can be with you, you can use me whenever you want! Just send ***&help*** and I will show
you all my commands.
            ''')
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))
