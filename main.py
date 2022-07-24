import os
import json
import disnake
from disnake.ext import commands
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'alive'


app.run(host='0.0.0.0', port=5000, debug=True)

f = open("primes.json", "r")
primes = json.loads(f.read())

osAssetUrl = "https://opensea.io/assets/0x13d15d8b7b2bf48cbaf144c5c50e67b6b635b5cd/"
caArtUrl = "https://champions.io/champions/nfts/art/"

bot = commands.Bot(command_prefix=commands.when_mentioned)


@bot.slash_command(description="Shows Prime Eternal with the given ID")
async def prime(inter, id: commands.Range[1, 7622]):
    prime = next(filter(lambda p: p['id'] == id, primes))
    embed = disnake.Embed(title="Prime Eternal #" + str(id),
                          url=osAssetUrl + str(id),
                          colour=0x710193)
    embed.set_image(url=caArtUrl + prime["pic_code"] + "/thumbnail.gif")
    embed.add_field(name="Divinity", value=prime["divinity"], inline=True)
    embed.add_field(name="Purity", value=prime["purity"], inline=True)
    embed.add_field(name="Core Essence",
                    value=prime["core_essence"],
                    inline=True)
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
    embed.add_field(name="Wallpaper",
                    value="[Wallpaper](" + caArtUrl + prime["pic_code"] +
                    "/animation.mp4)",
                    inline=True)
    embed.add_field(name="Gif",
                    value="[Gif](" + caArtUrl + prime["pic_code"] +
                    "/wallpaper.jpg)",
                    inline=True)
    embed.add_field(name="Video",
                    value="[Video](" + caArtUrl + prime["pic_code"] +
                    "/thumbnail.gif)",
                    inline=True)
    await inter.response.send_message(embed=embed)


bot.run(os.getenv("botToken"))
