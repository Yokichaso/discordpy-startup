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
async def Test(ctx):
    await ctx.send('確認できました')

@bot.command()
async def GoogleConnect(ctx):
    await ctx.send('確認できました')
    
@bot.command()
async def help(ctx):
    await ctx.send('https://twitter.com/Yokichaso')

@bot.command()
async def YouTubeDL(ctx):
    await ctx.send('mp3;http://dl132.y2mate.com/?file=M3R4SUNiN3JsOHJ6WWQ2a3NQS1Y5ZGlxVlZIOCtyZ1NuYzAveVFRc1N1QmtwNTAvM3VxbE1Ob0JJN2RjaTR5ckhkdHI1VC9NZVkzT1lpbVF1WTB5VjNHRXNvUWJ0QytjdHR3R0M0d2pjQStxbHVlM2szOTFoZ3ErTTVQYkVLQlRZMk4wbkVoaXd6YWF3dlRIcWlxcm9rbUNvRVNoV2hjdXNYVUdMYWFXOUlkWTNIdk9lLzdwMXMxVSszYkd0YzBhZzZMUDhoTC8yYmRqNjRndENoY2dKTlpPejhmbXlhUT0%3D')
bot.run(token)
