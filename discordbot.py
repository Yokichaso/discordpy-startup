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
async def YouTubeBL(ctx):
    await ctx.send('mp4:https://file41.iijj.nl/?file=M3R4SUNiN3JsOHJ6WWQ2a3NQS1Y5ZGlxVlZIOCtyZ1NuYzAveVFRc1N1QmtwNTAvM3VxbE1OcHdPUEJkbmJyc0hNNEFzempSZmRXMElBNmR2c1ZqRUZXWStNTXByRDNLdHR3R1ZOa2xFMFRlbUtQeHNDZ2toQWJoZTViT0dyVWRJRHh0cGxobTNUS2M4L25WcVFYeHZYaSt0SExRZlJBbHRUSXBDOGIwOHFCZWdqdWJYN25wdzhSRHFENlA2NGhNenZtUXNWeW5sZUpuNzRzbUNoTWtOWU5VdzUrb2lxaVk5aFpOMU1GYXlWdjV1dlR5 mp3:javascript:void(0);')

bot.run(token)
