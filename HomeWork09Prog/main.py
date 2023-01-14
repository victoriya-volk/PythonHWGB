import discord
from discord.ext import commands
from config import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTA2MzI1NzUyNTQzNDE5MTg5Mg.GuCOHu.tvMVhM2SZtIXrE7G3lem6hjAaxsswZr3KE0Hig')
