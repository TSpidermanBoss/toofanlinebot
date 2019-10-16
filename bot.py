from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait

k = -1001302468466
bot = "859744901:AAFCJdH4ln9fn2xFDyk1iL6LjmETdHNHouk"
app = Client (session_name="r",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = bot)                                   
bullet = -1001289914295                                              
ferrari = -1001453099412                                             
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( k,message.text)
 fie = open("ids.txt","a")
 fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
 fie.close()
@app.on_message(Filters.chat(ferrari) & Filters.edited)
def main(client, message):
   files = open("ids.txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(message.message_id)
    if id in x:
     try:
       if message.text == ".":
        client.delete_messages(k,int(x[x.index(id)+1]))
       else:
        client.edit_message_text(k,int(x[x.index(id)+1]),message.text)
     except FloodWait as e:
        time.sleep(e.x)
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( k,message.text)
 fie = open("ids.txt","a")
 fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
 fie.close()
@app.on_message(Filters.chat(bullet) & Filters.edited)
def main(client, message):
 files = open("ids.txt" , "r")
 d = files.readlines()
 files.close()
 for c in d:
  x = c.split()
  id = str(message.message_id)
  if id in x:
   try:
     if message.text == ".":   
      client.delete_messages(k,int(x[x.index(id)+1]))
     else:
      client.edit_message_text(k,int(x[x.index(id)+1]),message.text)
   except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command('clr'))
def forward(client, message):
  with open("ids.txt","w") as fie:
   fie.write("001 002")
   fie.close()
   message.reply("☢️ Done, Editing data cleared ✅✅")
app.run()
