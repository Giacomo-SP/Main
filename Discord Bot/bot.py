import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


#assegno alla variabile bot il bot
bot = commands.Bot(command_prefix = "-")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is Online")

@bot.command()
async def ciao(ctx):
    await ctx.message.channel.send("Ciao " + ctx.message.author.mention)

@bot.command(aliases = ["cls" , "cl"])
async def clear(ctx , righe) :
    ruolo_owner = discord.utils.get(ctx.guild.roles , name = "Owner")
    if ruolo_owner in ctx.message.author.roles:
        await ctx.channel.purge(limit = int(righe) + 1)

    else :
        await ctx.channel.send("**NON hai i PERMESSI NECESSARI** per eseguire questo **COMANDO**. ")

@bot.command(aliases = ["cla"])
async def clearall(ctx) :
    ruolo_owner = discord.utils.get(ctx.guild.roles , name = "Owner")
    if ruolo_owner in ctx.message.author.roles:
        await ctx.channel.purge(limit = 1000)

    else :
        await ctx.channel.send("**NON hai i PERMESSI NECESSARI** per eseguire questo **COMANDO**. ")

@bot.command(aliases = ["orario" , "iss" , "galileogalilei" , "ggalilei"])
async def scuola(ctx):
    await ctx.channel.send("**Guarda qui:**\nhttp://www.iisgalilei.eu\n")

 #, file = discord.File("logo_iss.png") per inserire immagine

@bot.command()
async def nick(ctx , utente:discord.Member , nick):
    ruolo_owner = discord.utils.get(ctx.guild.roles , name = "Owner")
    if ruolo_owner in ctx.message.author.roles:

        if str(utente) == "JackSP_#7028" :
            await ctx.channel.send("**ATTENZIONE:** Non puoi cambiare il Nickname al **Founder!**")

        else : 
            await utente.edit(nick = str(nick))
            await ctx.channel.send("Nickname cambiato con **SUCCESSO!**")
    
    else :
        await ctx.channel.send("**NON hai i PERMESSI NECESSARI** per eseguire questo **COMANDO**. ")

@bot.command()
async def search(ctx , * , nome_search):
    nome_search = str(nome_search)
    nome_search = nome_search.replace(" " , "+")
    link = "https://www.google.com/search?q=" + nome_search
    await ctx.channel.send("Ecco i **RISULTATI più RILEVANTI:** \n" + link)

@bot.command()
async def wiki(ctx , lingua,  * , nome_search = None):
    if str(lingua).lower() == "italiano" :
        nome_search = str(nome_search)
        nome_search = nome_search.replace(" " , "_")
        link = "https://it.wikipedia.org/wiki/" + nome_search
        await ctx.channel.send("Ecco i **RISULTATI più RILEVANTI** da **Wikipedia** in Italiano: \n" + link)

    elif str(lingua).lower() == "inglese" :
        nome_search = str(nome_search)
        nome_search = nome_search.replace(" " , "_")
        link = "https://en.wikipedia.org/wiki/" + nome_search
        await ctx.channel.send("Ecco i **RISULTATI più RILEVANTI** da **Wikipedia** in Inglese: \n" + link)

    elif str(lingua).lower() == "help" :
        await ctx.message.author.send()

    else:
        await ctx.channel.send("**Inserire una LINGUA valida.** (-wiki <lingua> <ricerca>)\nLingue SUPPORTATE: **ITALIANO | INGLESE**.")


#easter egg

@bot.command()
async def paparoski(ctx):
    await ctx.message.author.send("**GO PAPAROSKI!!!!** https://www.youtube.com/watch?v=YWTyAdZQDSs")

@bot.command(aliases = ["easter_egg"])
async def easteregg(ctx):
    await ctx.message.author.send("**EASTER EGG SCOPERTO!**")
    await ctx.message.channel.send("**ATTENZIONE:** Comando **NON TROVATO**.")

@bot.command()
async def papa(ctx):
    await ctx.message.author.send("**AMEN FRATELLO!**")
    await ctx.message.channel.send("**ATTENZIONE:** Comando **NON TROVATO**.")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.message.channel.send("**ATTENZIONE:** Comando **NON TROVATO**.")

bot.run(TOKEN)
