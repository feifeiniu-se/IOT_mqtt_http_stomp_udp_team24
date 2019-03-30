import requests
def HTTP_sender(light):

    url = 'http://47.103.20.207:5000/sender/light'
    payload = {'value': light}
    r = requests.get(url, params=payload)
    s = requests.session()
    s.keep_alive = False
    print (r.url, r.text)





