import thingspeak
import simplejson as json

CHANNEL_ID = '246127'
WRITE_API_KEY  = 'FH09RW1R5V9QHGN5'
READ_API_KEY   = '8E56MY9VB88SRGOK'


channel = thingspeak.Channel(id=CHANNEL_ID,api_key=READ_API_KEY,write_key=WRITE_API_KEY)


try:
    val = channel.get_field_last(field='field1')
except:
    raise
    print "connection failed"

a = json.loads(val)
print (a.get('field1'))
