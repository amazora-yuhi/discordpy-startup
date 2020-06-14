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
    if message.content == "dice":
    dice = random.randint(0, 100) #出る目を指定
    if 0 < dice < 50: #1～49
    await message.send_message(message.channel, "バカ")
    elif 51 < dice < 100: #50～99
    await message.send_message(message.channel, "アホ")
    elif dice == 0: #0が出たとき
    await message.send_message(message.channel, "ドジ")
else: #それ以外なので今回の場合100が出た時に処理される
    await message.send_message(message.channel, "マヌケ")
    
    
    
bot.run(token)
