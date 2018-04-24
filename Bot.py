import discord
import numpy as np
import datetime
import asyncio
import pickle

client= discord.Client()


async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed:
        
        file= open("chtime.pickle","rb")
        fload= pickle.load(file)
        fcheck= fload
        print(fcheck)
        file.close()
        timecheck=datetime.datetime.utcnow().replace(second=0,microsecond=0)
        for key in fcheck:            
            bosslist= fcheck[key]
            if timecheck>bosslist[0]:                  
                while datetime.datetime.utcnow().replace(second=0,microsecond=0)>bosslist[0]:                    
                    bosslist[0]=bosslist[0]+ datetime.timedelta(minutes=bosslist[1])
                    bosslist[2]=bosslist[2]+1                    
                fcheck[key]=bosslist
                file= open("chtime.pickle","wb")
                pickle.dump(fcheck,file)
                print(fcheck)
                file.close()
                file=open("chtime.pickle","rb")
                fload= pickle.load(file)
                fcheck=fload
                file.close()
            if timecheck==bosslist[0]: 
                await client.send_message(client.get_channel("436053682866356224"), "**{}** :is Due X : **{}** ".format(key,bosslist[2]))
                bosslist[0]=bosslist[0]+ datetime.timedelta(minutes=bosslist[1])
                bosslist[2]=bosslist[2]+1
                fcheck[key]=bosslist
                file= open("chtime.pickle","wb")
                pickle.dump(fcheck,file)
                print(fcheck)
                file.close()
                file=open("chtime.pickle","rb")
                fload= pickle.load(file)
                fcheck=fload
                file.close()
                await client.send_message(client.get_channel("436053682866356224"), "**{}** : time reseted ".format(key))
            if timecheck==bosslist[0]-datetime.timedelta(minutes=2): 
                print(key," is uppppp in 2 min")
                await client.send_message(client.get_channel("436053682866356224"), "**{}** is up in 2 min".format(key))
        file.close()
        await asyncio.sleep(60)
@client.event
async def on_message(message):          
    if message.content.startswith('.bosstime'):
        file= open("chtime.pickle","rb")
        fload= pickle.load(file)
        file.close()
        timenowutc= datetime.datetime.utcnow().replace(second=0,microsecond=0)
        for key in fload:
            btime=fload[key]
            bftime=btime[0]-timenowutc
            await client.send_message(client.get_channel("436053682866356224"), "**{}** time left : **{}** X **{}**".format(key,bftime,btime[2]))    
    file= open("chtime.pickle","rb")
    fload= pickle.load(file)
    fcheck=fload
    file.close()
    for key in fload:
        bosslist= fcheck[key]
        if message.content.startswith('.reset.{}'.format(key)): 
            bosslist[0]=datetime.datetime.utcnow().replace(second=0,microsecond=0)+ datetime.timedelta(minutes=bosslist[1])
            bosslist[2]=0
            fcheck[key]=bosslist
            file= open("chtime.pickle","wb")
            pickle.dump(fcheck,file)
            file.close()
            file= open("chtime.pickle","rb")
            fload= pickle.load(file)
            fcheck=fload
            file.close()
            await client.send_message(client.get_channel("436053682866356224"), "**{}** is Reseted".format(key))
    if message.content.startswith('.helpch'):
        await client.send_message(message.channel,"-   **.reset.boss** - reset the time of (boss=specified boss)")
        await client.send_message(message.channel,"-   **.bosstime**  - shows all boss time ")
        await client.send_message(message.channel,"-   **.f.bosstime**  - shows Frozen boss time ")                                  
        await client.send_message(message.channel,"-   **.dl.bosstime** - shows DL boss time")
        await client.send_message(message.channel,"## Bot will automatically reset time with a counter if not reseted manually ## ")
    if message.content.startswith('.f.bosstime'):        
        file= open("chtime.pickle","rb")
        fload= pickle.load(file)
        timenow=datetime.datetime.utcnow().replace(second=0,microsecond=0)
        file.close()
        for key in fload:
            bdata=fload[key]
            if bdata[3]=="f":
                bftime=bdata[0]-timenow
                await client.send_message(client.get_channel("436053682866356224"), "**{}** time left : **{}** X **{}**".format(key,bftime,bdata[2]))
    if message.content.startswith('.dl.bosstime'):        
        file= open("chtime.pickle","rb")
        fload= pickle.load(file)
        timenow=datetime.datetime.utcnow().replace(second=0,microsecond=0)
        file.close()
        for key in fload:
            bdata=fload[key]
            if bdata[3]=="dl":
                bftime=bdata[0]-timenow
                await client.send_message(client.get_channel("436053682866356224"), "**{}** time left : **{}** X **{}**".format(key,bftime,bdata[2]))
                            
            
            

client.loop.create_task(my_background_task())                    
                   
#client.run(process.env.BOT_TOKEN)
client.run(NDM1ODQxMjQ4MzI3MTA2NTYw.DcCcEA.ggMHY52pTe1b8Qc6YejBxD4XE-k)
    
   
