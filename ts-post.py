import thingspeak

CHANNEL_ID = ''
WRITE_API_KEY  = ''
READ_API_KEY   = ''

channel = thingspeak.Channel(id=CHANNEL_ID,api_key=READ_API_KEY,write_key=WRITE_API_KEY)

try:
    val = input("Enter the Value for updation : ")
    channel.update({1:val})
    print("Connection Made and Value uploaded")
except:
    print("Connection Error")
