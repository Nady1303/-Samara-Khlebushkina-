from discord_config import TOKEN
import discord
import requests
import random

class Mushketer(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        msg = message.content.lower()
        if message.author != self.user:
            if 'кот' in msg or 'кошк' in msg:
                response = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
                await message.channel.send(response)
            elif 'собак' in msg or 'пёс' in msg or 'пус' in msg or 'пес' in msg:
                response = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']
                await message.channel.send(response)
            elif msg == "Кто я из мушкетёров":
                a = ['Ты не мушкетёр, зай', 'Атос', 'Портос', 'Арамис', "Д'Артаньян"]
                s = random.choice(a)
                print(s)
                await message.channel.send(s)


intents = discord.Intents.all()
client = Mushketer(intents=intents)
client.run(TOKEN)
