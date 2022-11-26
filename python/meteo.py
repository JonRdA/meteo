from urllib.request import urlopen

data_url = "http://www.climaynievepirineos.com/estaciones/canfranc/downld08.txt"

def download_data(url):
    data = urlopen(data_url)
    return data.read()

z = download_data(data_url).decode("utf-8")
print(type(z))
print(z[:5000])
