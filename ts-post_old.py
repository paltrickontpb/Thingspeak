import httplib, urllib

WRITE_API_KEY = ''

def tspost(val1,val2):
    params = urllib.urlencode({'field1': val1, 'field2': val2,'key': WRITE_API_KEY})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept":  
        "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason

    data = response.read()
    conn.close()

if __name__ == "__main__":
    a = raw_input("Enter the first Number : ")
    b = raw_input("Enter the second Number : ")
    tspost(a,b)
