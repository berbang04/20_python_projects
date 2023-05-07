import urllib
import urllib.request



def connect(host="https://www.todtv.com.tr/"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

print("connected" if connect() else "not connected")