import discord 
from discord.ext import commands 
import asyncio
import time
from discord.ext import tasks
from itertools import cycle
from discord import utils



 


Prefix = '>'
Bot  = commands.Bot(command_prefix=Prefix)
Bot.remove_command('help')

statuses = cycle (['Terraria',' CS:GO','Minecraft'])

async def my_background_task():
    await Bot.wait_until_ready()
    counter = 0
    channel = discord.Object(id='719219311839019050')
    while not Bot.is_closed:
        counter += 1
        await Bot.send_message('@everyone')
        await asyncio.sleep(60) # task runs every 60 seconds




a='A'
b='B'
c='C'

mesage  = discord.Message.content


@Bot.event

async def on_ready():
    print('Bot is online')

    await Bot.change_presence(status = discord.Status.online, activity = discord.Game('Cody the crazy'))

@Bot.command(pass_context = True)

async def hello(ctx):
    await ctx.send('Привет{} , я Cyrex, бот созданный хозяином сервера, меня можно найти только тут! '.format(ctx.message.author.mention))
    pass


@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)
    pass

@Bot.command(pass_context = True)
async def congratulation(ctx):
    await ctx.send('```Поздравляю```')

@Bot.command(pass_context = True)
async def GK(ctx):
    emb = discord.Embed(title = 'GameKings info',description = 'Вся информация о GameKings', colour = discord.Color.blurple())
    emb.add_field(name='Группа VK',value='https://vk.com/public195575450',inline = False)
    emb.add_field(name='YOUTUBE',value='https://www.youtube.com/channel/UCAo1DyHMCXxDFtN-Cu2ziJQ',inline = False)
    emb.set_image(url = 'https://sun9-29.userapi.com/c857628/v857628332/1ff7fd/jalkoCQ98xI.jpg')
    emb.set_thumbnail(url='https://sun9-29.userapi.com/c857628/v857628332/1ff7fd/jalkoCQ98xI.jpg')
    emb.set_footer(text = 'GameKings|VOVCHAN|2020')
    await ctx.send(embed = emb)
    pass

@Bot.command(pass_context = True)
async def Kvantorium(ctx):
    emb = discord.Embed(title = 'Kvantorium ',description = '"Кванториум"- детский технопарк алтайского края', colour = discord.Color.red())
    emb.add_field(name = 'Официальный сайт', value='http://kvant22.ru/',inline = False)
    emb.set_image(url='http://kvant22.ru/wp-content/uploads/2016/12/cropped-logo.png')
    await ctx.send(embed = emb)
    pass

@Bot.command(pass_context = True)


async def help(ctx):
    embed = discord.Embed(title = 'Сервер VOVCHAN', description = '```Информация```',colour = discord.Color.dark_gold())
    embed.add_field(name = ' Префикс Cyrex(>), у остальных ботов(!)',value='----')
    embed.add_field(name = 'Всек команды, которые умеет Cyrex',value='----')
    embed.add_field(name = '{}clear'.format(Prefix),value='```Очистить чат```',inline = False)
    embed.add_field(name = '{}GK'.format(Prefix),value='```Информация о GameKings```',inline = False)
    embed.add_field(name = '{}hello'.format(Prefix),value='```Приветствие```',inline = False)
    embed.add_field(name = '{}Kvantorium'.format(Prefix),value='```Информация о кванториуме```',inline = False)
    embed.add_field(name = '{}congratulation'.format(Prefix),value='```Поздравления```',inline = False)
    embed.add_field(name = '{}ls'.format(Prefix),value='```Личный привет```',inline = False)
    embed.add_field(name = '{}lsuser'.format(Prefix),value='```Весточка```',inline = False)
    embed.set_footer(text='VOVCHAN|2020',icon_url='https://cdn.discordapp.com/attachments/696697059410968597/715784983268163594/IMG_20200301_171031.jpg')
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/696697059410968597/715784983268163594/IMG_20200301_171031.jpg')

    



    await ctx.send(embed = embed)

@Bot.command

def ping(ctx):
    while True():
                
        time.sleep(1)


@Bot.command(pass_context = True)
async def  ls(ctx):
    await ctx.author.send('Привет')
    pass

@Bot.command(pass_context = True)
async def  lsuser(ctx,member: discord.Member):
    await member.send(f'{member.name} ,привет от @Cyrex.bot')
    pass







Bot.run('NzE0NzYxNzY2MzQ4NzgzNjQ2.XszX6w.rvImEr7Z0wajQh2RhO8QciujTk0')       