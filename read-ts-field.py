import thingspeak
import simplejson as json

CHANNEL_ID = ''
WRITE_API_KEY  = ''
READ_API_KEY   = ''


channel = thingspeak.Channel(id=CHANNEL_ID,api_key=READ_API_KEY,write_key=WRITE_API_KEY)


try:
    val = channel.get_field_last(field='field1')
except:
    raise
    print "connection failed"

a = json.loads(val)
print (a.get('field1'))
