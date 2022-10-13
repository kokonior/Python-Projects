import requests, re, time, json
from colorama import Fore, Back, Style
from langdetect import detect
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
journal = {}
journal_ind = {}

def checkFromIndonesia(text):
    return Fore.GREEN + "YES" if detect(str(text).lower()) == "id" else Fore.RED + "NOT"

def getpage(url):
    return requests.get(url, verify=False).text

def extract_url(content):
    u = {}
    # current_page = re.search(r"Page\s(\d+)\sof\s\d+\s\|\sTotal Records", content)[1]
    journal_name = re.findall(r"<dl class=\"uk-description-list-line\">\n\s+.*\n\s+.*class=\"paper-link\"\shref=\"(.*?)\".*>(.*?)<\/a>\n\s+.*\n\s+<dd>(.*?)<\/dd>\s+.*\n(.*?)<\/dd>", content)
    for i, k in enumerate(journal_name):
        check = checkFromIndonesia(str(k[1]).strip())
        print("\t[+] ["+ Fore.BLUE + str(k[1]) + Style.RESET_ALL +"] [ "+ Fore.YELLOW +"From Indonesia? : " + check + Style.RESET_ALL + " ]")
        u.update(
            {
                i: {
                    'journal_url': k[0],
                    'journal_name': k[1],
                    'journal_by': k[2],
                    'journal_index': k[3].strip(),
                    'journal_from_indo': True if re.search(r"YES", check) else False
                }
            }
        )
        if(re.search("YES", check)):
            s = open("journal_from_ind.txt", "a+")
            s.write("Journal Name : {}\nJournal URL : {}\nJournal Author : {}\n\n".format(str(k[1]), str(k[0]), str(k[2])))
            s.close()


def get_total_page(content):
    return int(re.search(r"of (\d+) | Total Records : \d+", content)[1])

def get_journal_index_name(content):
    return re.search(r"<div class=\"au-name\">(.*?)<\/div>", content)[1]

url = input("Main URL page 1 : ")

print("[+] Getting journal info....\n")
time.sleep(2)
getInfo = getpage(url)
print("[+] Journal Index Name : " + str(get_journal_index_name(getInfo)))
print("[+] Total Page : " + str(get_total_page(getInfo)))
print("[+] Rebuilding information for crawling mode...\n")
time.sleep(2)
journal = {i:{} for i in range(1, get_total_page(getInfo) + 1)}
for x in range(1, get_total_page(getInfo) + 1):
    print("[~] Crawling page " + str(x) + "...")
    new_url = re.sub("page=\d+&", "page="+ str(x) + "&", url)
    getInfo = getpage(new_url)
    extract_url(getInfo)