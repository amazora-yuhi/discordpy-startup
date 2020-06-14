from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.command()
async def inu(ctx):
    await ctx.send('わん')
    
import random #ランダムモジュール忘れずに

if message.content == "dice":
    dice = random.randint(1, 6) #出る目を指定
    await message.send_message(message.channel, str(dice))
    
bot.run(token)
