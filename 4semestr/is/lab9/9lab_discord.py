import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import random
from config import discord_token

bot = commands.Bot(command_prefix='/')



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(
            f'{bot.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id})')

@bot.event
async def on_member_join( member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Привет, {member.name}!'
    )


sobaka=("собака","собаку","пёс","пёсик","пёсика","псину","собачку","шенка","шенят","собак","псов","псин","собачек")
kot=("кот","кота","котика","котёнка","котёнок","киса","котят","котята","кошку","кошка","кошки")


@bot.event
async def on_message( message):
    if message.author == bot.user:
        return
    if message.content.startswith("/random"):
        try:  
            a = random.randint(0, int(message.content[8:]))
        except:
            await message.channel.send(f'Ошибка')  
            return
        await message.channel.send(f'Ваше случайное число: {a}')
    elif message.content.startswith("/timer"):
        await message.channel.send(f'вернусь через : {message.content[7:]} секунд')
        await asyncio.sleep(int(message.content[7:]))
        await message.channel.send(f' {message.content[7:]} секунд прошло')
    elif "привет" in message.content.lower():
        author = message.author
        await message.channel.send(f'привет, {author.mention}!')
    elif  message.content.lower() in kot:
        file=open('4semestr\is\lab9\картинки для бота дискорда\koty.jpg',"rb") 
        picture = discord.File(file)
        await message.channel.send(file=picture)
        file.close()
    elif  message.content.lower() in sobaka:
        file=open('4semestr\is\lab9\картинки для бота дискорда\sobaka.jpeg',"rb") 
        picture = discord.File(file)
        await message.channel.send(file=picture)
        file.close()
    else:
        await message.channel.send("автоответчик")
        return





bot.run(discord_token)