import discord
import random
import config
#import discord.Guild

class MyClient(discord.Client):
    top = ['Aatrox', 'Camille', 'Cho-gath', 'Darius', 'Dr.Mundo', 'Fiora', 'Gangplank', 'Garen', 'Gnar', 'Illaoi', 'Irelia', 'Jax', 'Jayce', 'Kayle', 'Kennen', 'Kled', 'Malphite', 'Maokai', 'Mordekaiser', 'Nasus', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Renekton', 'Riven', 'Rumble', 'Ryze', 'Sett', 'Shen', 'Singed', 'Sion', 'Teemo', 'Tryndamere', 'Urgot', 'Yorick']
    jgl = ['Amumu', 'Elise' ,'Evelynn', 'Fiddlesticks', 'Gragas', 'Graves', 'Hecarim', 'Ivern', 'Jarvan 4th', 'Jax', 'Karthus', 'Kayn', 'Kha-zix', 'Kindred', 'Lee sin', 'Master yi', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Rammus', 'Rek-sai', 'Sejuani', 'Shaco' ,'Shyvana', 'Skarner' ,'Taliyah', 'Trundle', 'Udyr', 'Vi', 'Volibear', 'Warwick', 'Wukong', 'Xin Zhao', 'Zac']
    mid = ['Ahri', 'Akali', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Brand', 'Cassiopeia', 'Corki', 'Diana', 'Ekko', 'Fizz', 'Galio', 'Heimerdinger', 'Kassadin', 'Katarina', 'Leblanc', 'Lissandra', 'Lux', 'Malzahar', 'Neeko', 'Oriana', 'Qiyana', 'Ryze', 'Swain', 'Sylas', 'Syndra', 'Talon', 'Twisted Fate', 'Veigar', 'Velkoz', 'Viktor', 'Vladimir', 'Xerath', 'Yasuo', 'Zed', 'Ziggs', 'Zoe']
    adc = ['Aphelios', 'Ashe', 'Caitlynn', 'Draven', 'Ezreal', 'Jinx', 'Jhin', 'Kaisa', 'Kalista', 'KogMaw', 'Lucian', 'Miss Fortune', 'Sivir', 'Tristana',  'Twitch', 'Varus', 'Vayne', 'Xayah']
    sup = ['Alistar', 'Bard', 'Blitzcrank', 'Braum',  'Janna', 'Karma', 'Leona', 'Lulu', 'Morgana', 'Nami', 'Nautilus', 'Pyke', 'Rakan', 'Senna', 'Sona', 'Soraka', 'Tahm Kench', 'Taric', 'Thresh', 'Yuumi', 'Zilean', 'Zyra']


    async def on_ready(self):
        print("Der Verwaltungsbot ist nun online und kann genutzt werden.")
    async def on_message(self, message):
        try:
            if(message.author == client.user):
                return
            elif(message.content.lower().replace(' ','') == 'verwaltung-help'):
                await message.channel.send("Neuer Channel: verwaltung-newchannel/NAME/USER_LIMIT\nNAME: Der Name des Channels\nLIMIT: Maximale Anzahl an Personen (0-99, wobei 0 unendlich für keine Begrenzung steht.)")
            elif(message.content.lower().replace(' ','').startswith('verwaltung-newchannel')):
                param = message.content.split('/')
                if(len(param) == 3):
                    await message.guild.create_voice_channel(name = str(param[1]), user_limit = int(param[2]), category = client.get_channel(705900865998946453).category)
                    print("Der Channel: "+str(param[1])+" wurde erstellt")
                else:
                    await message.channel.send("Geben sie nur den Namen und das User_Limit an.")
            elif(message.content.lower().replace(' ','').startswith('verwaltung-lol')):
                try:
                    param = message.content.split('/')
                    if(len(param) == 2):
                        value = param[1]
                        if value == "5":
                            await message.channel.send("top: " + random.choice(self.top)+"\njgl: " +random.choice(self.jgl) + "\nmid: " + random.choice(self.mid) + "\nadc: "+ random.choice(self.adc) + "\nsup: " + random.choice(self.sup))
                        else:
                            print(str(value))
                            await message.channel.send("" + value + ": "+self.getOneChamp(value))
                    else:
                        m = ""
                        for x in range(1, len(param)):
                            print(m)
                            m = m+param[x]+": "+self.getOneChamp(param[x])+"\n"
                        await message.channel.send(""+m)
                except:
                    print("Fehler: LoL")
                    await message.channel.send('''Es ist ein Fehler aufgetreten! Bitte schauen sie sich den Befehl im Bot Channel an oder rufen sie ueber verwaltung-help die Hilfe des Bots auf.''')
        except:
            await message.channel.send('''Es ist ein Fehler aufgetreten! Bitte schauen sie sich den Befehl im Bot Channel an oder rufen sie ueber verwaltung-help die Hilfe des Bots auf.''')
            print("Ein Fehler ist aufgetreten")
    async def on_member_update(self, before, after):
        if(before.guild.name == "Gamer"):
            channels = before.guild.channels
            for c in channels:
                if(c.type.name == 'voice'):
                    if(c.id != 724318660164059428 and c.id != 705899005766533256 and c.id != 500715863628972033 and c.id != 705900865998946453 and c.id != 530463694870675476 and c.id != 500738108631941140 and c.id != 500738344020344833):
                        if(len(c.members) == 0):
                            print("Der Channel "+str(c.name)+" wird nun geloescht")
                            await c.delete()
    def getOneChamp(self, s):
        if(s.lower() == "top"):
            return random.choice(self.top)
        elif(s.lower() == "jgl"):
            return random.choice(self.jgl)
        elif(s.lower() == "mid"):
            return random.choice(self.mid)
        elif(s.lower() == "adc"):
            return random.choice(self.adc)
        elif(s.lower() == "sup"):
            return random.choice(self.sup)
        return "Error"

client = MyClient()
client.run(config.token)