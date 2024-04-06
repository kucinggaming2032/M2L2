import discord
from discord.ext import commands
import os
import random
import requests
intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

organik = ['sisa makanan', 'bahan kimia','daun','kulit pisang','buah sisa']
anorganik = ['kaca','sterofoam','plastik','ban','karet','handphone']

@bot.command()
async def bapilih_sampah(ctx):
    await ctx.send("mo tau jenis sampah apa?")
    msg = await bot.wait_for("message")
    if msg.content in organik:
        await ctx.send("buang ada tempat sampah organik")
    elif msg.content in anorganik:
        await ctx.send("buang ada tempat sampah anorganik")







bot.run("MTIxODQyMTQ1NzQ3OTI3NDU1Ng.Ga8aaq.42uun5UbtmzTNOa0sRTfdIP_UPFBD4nw_BDHTA")