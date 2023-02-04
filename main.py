import discord
import pickle
import random
import os

intents = discord.Intents.default()
intents.members = True


token = "NjgxNjM4ODc2ODgzOTc2Mjcz.XlRXrA.HwKKAiDUHi_gvwCo63TqD5qz6Qw"

bot = discord.Client(intents=intents)

def create_embed(title, description, color=0, img="", thumb=""):
        embed = discord.Embed()
        embed.title = title
        embed.description = description
        embed.colour = color
        if(img != ""):
            embed.set_image(url = img)
        if(thumb != ""):
            embed.set_thumbnail(url = thumb)
        return embed

#load an save function 
def load_file(files):
    with open(files, 'rb') as f:
        p = pickle.load(f)
        return p

def save_file(files, save):
    with open(files, 'wb') as f:
        pickle.dump(save, f)

#search file by name
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

#On bot ready
@bot.event
async def on_ready():
    #Change Activity
    await bot.change_presence(activity=discord.Game('Humeur bot'))
    print("Author : Nzo\nVersion : 1.0")
    print("Bot is ready \n----------")



#On message 
@bot.event
async def on_message(message):
    msg_split = message.content.split(" ")
    if message.content.startswith("!nickname"):
        name_list = load_file("nickname_list.data")

        nbr = random.randint(0, len(name_list) - 1)
        nickname = name_list[nbr]
    
        #Embed creation 
        embed = discord.Embed( title= f"**{message.author}** Voici ton nouveau pseudo **{nickname}**", colour=discord.Colour.blue(),)

        
        for file in os.listdir("image/"):
            if file.startswith(f"{nickname}"):
                search_file = file

        try:
            file = discord.File(f"image/{search_file}", filename=f"{search_file}")
            embed.set_image(url=f"attachment://{search_file}")
            find = True
        except:
            find = False

        if find == True:
            await message.channel.send(file=file, embed=embed)

        else:
            await message.channel.send(embed=embed)

        
        #remove nickname from list 
        name_list.remove(nickname)
        save_file("nickname_list.data", name_list)

        await message.author.edit(nick=nickname)

    if message.content.startswith("!reaction"):
        await message.delete()
        embed = create_embed("Ajout réaction role", "Merci d'indiquer l'id du Message qui doit avoir la réaction !")  
        msg_embed = await message.channel.send(embed = embed)
        while True:
            msg_response = await bot.wait_for('message')
            if msg_response.author == message.author :
                await msg_embed.delete()
                await msg_response.delete()
                msg_reaction = await bot.get_channel(message.channel.id).fetch_message(int(msg_response.content))
                await msg_reaction.add_reaction('🧃')
                
                break
            else:
                continue 
        save_file("reaction_id.data", msg_response.content)
        
    
@bot.event
#on reaction add
async def on_raw_reaction_add(payload):
    #If user is bot 
    if payload.user_id == bot.user.id:
        return
    if payload.emoji.name == "🧃":
        reaction_message_id = load_file("reaction_id.data")
        if payload.message_id == int(reaction_message_id):
            guild = bot.get_guild(payload.guild_id)
            user = await bot.fetch_user(payload.user_id)
            ex_nickname = user.name
            channel = bot.get_channel(payload.channel_id)
            member = guild.get_member(int(payload.user_id))
            await member.edit(nick=f"🧃 {ex_nickname}")

bot.run(process.env.TOKEN)