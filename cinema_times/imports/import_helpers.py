import requests

def try_get_attrib(e, key):
    try:
        return e.attrib[key]
    except Exception:
        return ""

def get_url(url):
    req = requests.get(url)
    return req.content