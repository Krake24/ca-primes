import os
import discord 
import json
from discord.ext import commands

f = open("primes.json", "r")
primes = json.loads(f.read())

bot = commands.Bot(command_prefix="!")

osAssetUrl="https://opensea.io/assets/0x13d15d8b7b2bf48cbaf144c5c50e67b6b635b5cd/"
caArtUrl="https://champions.io/champions/nfts/art/"


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  content = message.content
  if content.startswith('!prime'):
    split = content.split(" ")
    if len(split) >= 2:
      if split[1].isnumeric():
        id = int(split[1])
        if id < 1 or id > 7622:
          await message.channel.send("usage: !prime [1-7622]")
        else:
          prime = primes[id - 1]
          embed = discord.Embed(
            title="Prime Eternal #" + str(id),
            link=osAssetUrl + str(id),
            color=0x710193 
          )
          embed.set_image(url = caArtUrl + prime["pic_code"] + "/thumbnail.gif")
          embed.add_field(name="Divinity", value=prime["divinity"], inline=True)
          embed.add_field(name="Purity", value=prime["purity"], inline=True)
          embed.add_field(name="Core Essence", value=prime["core_essence"], inline=True)
          embed.add_field(name="Family", value=prime["family"], inline=False)
          embed.add_field(name="Fangs", value=prime["fangs"], inline=True)
          embed.add_field(name="Claws", value=prime["claws"], inline=True)
          embed.add_field(name="Tail", value=prime["tail"], inline=True)
          embed.add_field(name="Warpaint", value=prime["warpaint"], inline=True)
          embed.add_field(name="Wings", value=prime["wings"], inline=True)
          embed.add_field(name="Horns", value=prime["horns"], inline=True)
          embed.add_field(name="Piercing", value=prime["piercing"], inline=True)
          embed.add_field(name="Halo", value=prime["halo"], inline=True)
          embed.add_field(name="Hairstyle", value=prime["hairstyle"], inline=True)
          embed.add_field(name="Wallpaper", value="[Wallpaper](" + caArtUrl + prime["pic_code"] + "/animation.mp4)", inline=True)
          embed.add_field(name="Gif", value="[Gif](" + caArtUrl + prime["pic_code"] + "/wallpaper.jpg)", inline=True)
          embed.add_field(name="Video", value="[Video](" + caArtUrl + prime["pic_code"] + "/thumbnail.gif)", inline=True)
          await message.channel.send(embed=embed)
      else:
        await message.channel.send("usage: !prime [1-7622]")

bot.run(os.getenv("botToken"))