#!/bin/env python3
import os
import json
import disnake
from disnake.ext import commands

f = open("primes.json", "r")
primes = json.loads(f.read())

f = open("elementals.json", "r")
elementals = json.loads(f.read())

print("Champions read")

osPrimesUrl = "https://opensea.io/assets/0x13d15d8b7b2bf48cbaf144c5c50e67b6b635b5cd/"
caPrimeArtUrl = "https://www.champions.io/champions/nfts/art/"
peDetails = "https://www.champions.io/champion-details/"

osElementalsUrl = "https://opensea.io/assets/0x13d15d8b7b2bf48cbaf144c5c50e67b6b635b5cd/"
caElementalArtUrl = "https://www.champions.io/elementals/nfts/art/"
eeDetails = "https://www.champions.io/elemental-details/"

bot = commands.Bot(command_prefix=commands.when_mentioned)


@bot.slash_command(description="Shows Prime Eternal with the given ID")
async def prime(inter, id: commands.Range[1, 7622]):
    prime = next(filter(lambda p: str(p['id']) == str(id), primes))
    embed = disnake.Embed(title="Prime Eternal #" + str(id),
                          url=osPrimesUrl + str(id),
                          colour=0x710193)
    embed.set_image(url=caPrimeArtUrl + str(prime["id"]) + "/animation.gif")
    embed.add_field(name="Divinity", value=prime["divinity"], inline=True)
    embed.add_field(name="Purity", value=prime["purity"], inline=True)
    embed.add_field(name="Core Essence",
                    value=prime["core_essence"],
                    inline=True)
    embed.add_field(name="Family", value=prime["family"], inline=False)
    embed.add_field(name="Fangs", value=prime["fangs"], inline=True)
    embed.add_field(name="Claws", value=prime["claws"], inline=True)
    embed.add_field(name="Horns", value=prime["horns"], inline=True)
    embed.add_field(name="Tail", value=prime["tail"], inline=True)
    embed.add_field(name="Warpaint", value=prime["warpaint"], inline=True)
    embed.add_field(name="Wings", value=prime["wings"], inline=True)
    embed.add_field(name="Piercing", value=prime["piercing"], inline=True)
    embed.add_field(name="Hairstyle", value=prime["hairstyle"], inline=True)
    embed.add_field(name="Halo", value=prime["halo"], inline=True)
    embed.add_field(name="View on champions.io", value="[Details](" + peDetails + str(id) + ")",
                    inline=True)
    await inter.response.send_message(embed=embed)

@bot.slash_command(description="Shows Elemental Eternal with the given ID")
async def elemental(inter, id: commands.Range[1, 10000]):
    elemental = next(filter(lambda p: str(p['id']) == str(id), elementals))
    embed = disnake.Embed(title="Elemental Eternal #" + str(id),
                          url=osElementalsUrl + str(id),
                          colour=0x710193)
    embed.set_image(url=caElementalArtUrl + elemental["id"] + "/thumbnail.gif")
    embed.add_field(name="Sublime", value=elemental["Sublime"], inline=True)
    embed.add_field(name="Purity", value=elemental["Purity"], inline=True)
    embed.add_field(name="Core Essence",
                    value=elemental["Core Essence"],
                    inline=True)
    embed.add_field(name="Family", value=elemental["Family"], inline=False)
    embed.add_field(name="Fangs", value=elemental["Fangs"], inline=True)
    embed.add_field(name="Claws", value=elemental["Claws"], inline=True)
    embed.add_field(name="Horns", value=elemental["Horns"], inline=True)
    embed.add_field(name="Tail", value=elemental["Tail"], inline=True)
    embed.add_field(name="Warpaint", value=elemental["Warpaint"], inline=True)
    embed.add_field(name="Wings", value=elemental["Wings"], inline=True)
    embed.add_field(name="Piercing", value=elemental["Piercing"], inline=True)
    embed.add_field(name="Hairstyle", value=elemental["Hairstyle"], inline=True)
    embed.add_field(name="Halo", value="None", inline=True)
    embed.add_field(name="View on champions.io", value="[Details](" + eeDetails + str(id) + ")",
                    inline=True)
    await inter.response.send_message(embed=embed)

bot.run(os.getenv("botToken"))
