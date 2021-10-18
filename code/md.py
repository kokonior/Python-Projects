from bs4 import BeautifulSoup
from markdown import markdown

def md_to_text(md):
    html = markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()

def reformattext(text):
    return text.replace("~","").replace("_","").replace("*","").replace("`","")
