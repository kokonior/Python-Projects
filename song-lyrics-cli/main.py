from bs4 import BeautifulSoup as bs
import requests, os

os.system('clear')

print('''\033[1;32;49m

_    _   _ ____ _ ____ ____    ____ _    _ 
|     \_/  |__/ | |    [__  __ |    |    | 
|___   |   |  \ | |___ ___]    |___ |___ | v1.0
                                           
\033[1;37;49m''')

key = input('Keyword : ')

userAgent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
page      = requests.get(f'https://www.google.com/search?q=lirik+lagu+{key}', headers=userAgent)
s         = bs(page.content, 'html.parser')

try:
    mess      = s.find('a', class_='gL9Hy').text
    userAgent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    page      = requests.get(f'https://www.google.com/search?q={mess}', headers=userAgent)
    s         = bs(page.content, 'html.parser')

except Exception as e:
    pass
    

try:
    artis     = s.find('h2', class_='qrShPb').text
    judul     = s.find('div', class_='wwUB2c').text
    lirik     = s.find_all('span', jsname="YS01Ge")
except Exception as e:
    print('\n\033[1;31;49mLirik lagu tidak ditemukan\033[1;37;49m')
    exit()

print(f'\n{artis} - {judul}\n')
for l in lirik:
    print(l.text)
    pass


