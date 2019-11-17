import urllib.request, json

def dollar():
    try:
        with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/rates/a/usd/") as url:
            data = json.loads(url.read().decode())

            return(data['rates'][0]['mid'])
    except:
        print("error")
def euro():
    try:
        with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/rates/a/eur/") as url:
            data = json.loads(url.read().decode())

            return(data['rates'][0]['mid'])
    except:
        print("error")

def pound():
    try:
        with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/rates/a/gbp/") as url:
            data = json.loads(url.read().decode())

            return(data['rates'][0]['mid'])
    except:
        print("error")

def franc():
    try:
        with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/rates/a/chf/") as url:
            data = json.loads(url.read().decode())

            return(data['rates'][0]['mid'])
    except:
        print("error")