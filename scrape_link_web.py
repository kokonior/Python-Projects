import requests
from bs4 import BeautifulSoup

url = "https://e-mtq.bengkaliskab.go.id/assets/foto/"
def getData(url):
    r = requests.get(url)
    return r.text

def getUrllist(url):
    htmlData = getData(url)
    soup = BeautifulSoup(htmlData, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        print(link.get('href'))
        data = link.get('href')
        unionUrl = url + data
        f.write(unionUrl)
        f.write("\n")

f = open("test1.txt", "w")
getUrllist(url)
f.close()