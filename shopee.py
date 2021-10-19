import lxml.etree
import lxml.html
import requests

def shopee():
	r = requests.get("https://shopee.co.id/puffy_id")
	root = lxml.html.fromstring(r.content)
	nama = root.xpath('//div[@class="shop-page-shop-description__shop-name"]/text()')
	print("Nama toko: '{}'".format(nama[0].text.strip()))

if __name__ == '__main__':
	shopee()