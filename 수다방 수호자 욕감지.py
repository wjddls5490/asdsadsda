import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('씨발'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('좆'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발련'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발놈'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발년'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발새끼'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발련아'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발년아'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('시발놈아'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('개새끼'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('십새기'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('십새끼'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('병신'):
        await message.channel.send(message.author.mention + " 욕하지마 X발")
    elif message.content.startswith('지유'):
        await message.channel.send(message.author.mention + " 금지어 언급하지 마세요")
        
client.run('NzY1ODkyMjIzMzM3MzY1NTY1.X4batw.10eezZjFkLqYAVhiX0ZbZ-ZmtoE')