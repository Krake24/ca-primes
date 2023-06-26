#!/bin/env python3
import os
import json
import disnake
from disnake.ext import commands

f = open("primes.json", "r")
primes = json.loads(f.read())

f = open("elementals.json", "r")
elementals = json.loads(f.read())

f = open("pets.json", "r")
pets = json.loads(f.read())

print("metadata loaded")

osPrimesUrl = "https://opensea.io/assets/matic/0xe22575fAd77781D730C6Ed5d24dD1908d6D5b730/"
caPrimeArtUrl = "https://www.champions.io/champions/nfts/art/"
peDetails = "https://www.champions.io/champion-details/"

osElementalsUrl = "https://opensea.io/assets/matic/0xc615bfb753fc2bab65065987391d046105673284/"
caElementalArtUrl = "https://www.champions.io/elementals/nfts/art/"
eeDetails = "https://www.champions.io/elemental-details/"

osPetsUrl = "https://opensea.io/assets/matic/0x58481864048671c833a0cee0d467d34534171713/"
caPetArtUrl = "https://www.champions.io/pets/nfts/art/"
petDetails = "https://www.champions.io/pet-details/"

footerText = "©《Pirre》- The Prime Syndicate"

bot = commands.Bot(command_prefix=commands.when_mentioned)


@bot.slash_command(description="Shows Prime Eternal with the given ID")
async def prime(inter, id: commands.Range[1, 7622]):
    prime = next(filter(lambda p: str(p['id']) == str(id), primes))
    embed = disnake.Embed(title="Prime Eternal #" + str(id),
                          url=osPrimesUrl + str(id),
                          colour=0x710193)
    embed.set_image(url=caPrimeArtUrl + str(id) + "/animation.gif")
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
    embed.add_field(name="View on champions.io", value="[Details](" + peDetails + str(id) + ")", inline=False)
    embed.set_footer(text=footerText)

    await inter.response.send_message(embed=embed)

@bot.slash_command(description="Shows Elemental Eternal with the given ID")
async def elemental(inter, id: commands.Range[1, 10000]):
    elemental = next(filter(lambda p: str(p['id']) == str(id), elementals))
    embed = disnake.Embed(title="Elemental Eternal #" + str(id),
                          url=osElementalsUrl + str(id),
                          colour=0x710193)
    embed.set_image(url=caElementalArtUrl + str(id) + "/thumbnail.gif")
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
    embed.add_field(name="View on champions.io", value="[Details](" + eeDetails + str(id) + ")", inline=False)
    embed.set_footer(text=footerText)
    
    await inter.response.send_message(embed=embed)
    
@bot.slash_command(description="Shows Pet with the given ID")
async def pet(inter, id: commands.Range[1, 22750]):
    pet = next(filter(lambda p: str(p['id']) == str(id), pets))
    embed = disnake.Embed(title="Pet #" + str(id),
                          url=osPetsUrl + str(id),
                          colour=0x710193)
    embed.set_image(url=caPetArtUrl + str(id) + "/pfp.png")
    embed.add_field(name="Family", value=pet["Family"], inline=True)
    embed.add_field(name="House Banner", value=pet["House Banner"], inline=True)
    embed.add_field(name="Favorite Family", value=pet["Favorite Family"], inline=True)
    embed.add_field(name="Personality", value=pet["Personality"], inline=True)
    embed.add_field(name="Favorite Toy", value=pet["Favorite Toy"], inline=True)
    embed.add_field(name="Favorite Food", value=pet["Favorite Food"], inline=True)
    embed.add_field(name="View on champions.io", value="[Details](" + petDetails + str(id) + ")", inline=False)
    embed.set_footer(text=footerText)
    
    await inter.response.send_message(embed=embed)

bot.run(os.getenv("botToken"))