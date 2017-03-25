import thingspeak

CHANNEL_ID = '246127'
WRITE_API_KEY  = 'FH09RW1R5V9QHGN5'
READ_API_KEY   = '8E56MY9VB88SRGOK'

channel = thingspeak.Channel(id=CHANNEL_ID,api_key=READ_API_KEY,write_key=WRITE_API_KEY)

try:
    val = input("Enter the Value for updation")
    channel.update({1:val})
    print("Connection Made and Value uploaded")
except:
    print("Connection Error")
