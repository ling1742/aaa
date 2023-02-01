from urllib.request import urlopen

url='https://home.firefoxchina.cn/'
resp=urlopen(url)
print(resp.read().decode("utf-8"))
