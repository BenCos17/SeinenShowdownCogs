import discord
from redbot.core import commands

class NaofumiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'naofumi' in message.content.lower():
            response = 'Nenkai is the best naofumi main'
            await message.channel.send(response)

def setup(bot):
    bot.add_cog(NaofumiCog(bot))
