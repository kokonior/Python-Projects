import os
import re
import sys
import math
try:
    import click
    import requests
    from bs4 import BeautifulSoup as bs
except ImportError:
    exit("- import error, you need install module first !")

r = requests.Session()

def download(url):
	try:
		req = r.get(url)
		origin = re.search('https://(.*?)/',url).group(1)
		if "(Math.pow(a, 3)+b)" in req.text:
			script = bs(req.text,'html.parser').findAll('script')
			for script in script:
				if '(Math.pow(a, 3)+b)' in str(script):
					var_a = re.search('var a = (.*?);', str(script)).group(1)
					break
			var_b = 3
			middle_math = int(math.pow(int(var_a),3) + var_b)
			elemen = re.search('document.getElementById\(\'dlbutton\'\).href = \"(.*?)\"\+(.*?)\+"(.*?)\";', req.text)
			url_download = "https://" + origin + elemen.group(1) + str(middle_math) + elemen.group(3)
		elif 'var a = function() {return 1};' in req.text:
			a = lambda: 1
			b = lambda: a() + 1
			c = lambda: b() + 1
			d = re.search('<span id="omg" class="(.*?)"',req.text).group(1)
			d = int(d) * 2
			elemen = re.search('document.getElementById\(\'dlbutton\'\).href\ = \"(.*?)\"\+\((.*?) \+ a\(\) \+ b\(\) \+ c\(\) \+ d \+ (.*?)\)\+"(.*?)"',req.text)
			first = int(eval(elemen.group(2)) + a() + b() + c() + d + eval(elemen.group(3)))
			url_download = 'https://' + origin + elemen.group(1) + str(first) + elemen.group(4)
		else:
			elemen = re.search('document.getElementById\(\'dlbutton\'\).href = \"(.*?)\" \+ \((.*?)\) \+ \"(.*?)\";',req.text)
			url_download = "https://" + origin + elemen.group(1) + str(eval(elemen.group(2))) + elemen.group(3)
		print("- redirect to browser !")
#		click.launch(url_download)
		print(url_download)
	except ValueError:
		sys.exit(f"- failed download from {url}")
	except AttributeError:
		sys.exit("- failed download file not found !")

def main():
	if len(sys.argv) < 2:
		print()
		print("- input url zippyshare !")
		url_download = input('- url : ')
	else:
		url_download = sys.argv[1]
	download(url_download)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()

