from .naofumicog import NaofumicogCog


def setup(bot):
    bot.add_cog(NaofumicogCog(bot))