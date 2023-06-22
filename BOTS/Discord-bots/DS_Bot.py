
from IDkeyCOINbruh import ID_coin as token
import discord
from discord.ext import commands

my_token = token.token_ds()

my_intents = discord.Intents.all()
bot = commands.Bot(command_prefix="--", intents=my_intents)

@bot.event
async def on_ready():
  print(f'{bot.user.name} запустился и готов к работе!')

@bot.event
async def on_message(message):
  if message.author.bot:
    return
  await bot.process_commands(message)

@bot.command()
async def test(ctx):
  await ctx.send('TEST is SUCK')

bot.run(token=my_token)
