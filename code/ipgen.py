import random
import requests
from multiprocessing.dummy import Pool

def genip():

	brapa = input('How Much IP? ')
	for i in range(0, int(brapa)):
		a = random.randrange(0, 255, 1)
		b = random.randrange(0, 255, 1)
		c = random.randrange(0, 255, 1)
		d = random.randrange(0, 255, 1)
		ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
		print('RANDOM IP ->', ip)
		open('ip.txt', 'a').write(ip+'\n')
	print('[+] SUCCESS GENERATE IP!! ')

def yoy():

	lis = input('Your IP List -> ')
	tol = open(lis, 'r').readlines()
	for i in tol:
		yaa = i.strip()
		part = yaa.split('.')
		a = '.'

		start = 0
		end = 255
		for j in range(start, end + 1):
			for k in range(start, end + 1):
				ale = part[0] + a + part[1] + a + str(j) + a + str(k)
				open('ranged.txt', 'a').write(ale+'\n')
		print(yaa, '-> RANGED!!')


def valid(hayuk):

		try:
			r = requests.get('http://{}'.format(hayuk), timeout=3)
			if r.status_code == 200:
				print(hayuk, '-> LIVE IP')
				open('liveip.txt', 'a').write(hayuk+'\n')
			elif '<title>' in r.text:
				print(hayuk, '-> LIVE IP')
				open('liveip.txt', 'a').write(hayuk+'\n')
			else:
				pass
		except Exception:
			print(hayuk, '-> DEAD')




def thread(li):
	ase = open(li, 'r').read().splitlines()
	p = Pool(100)
	p.map(valid, ase)

if __name__ == "__main__":

	print("""


  ___     _____         _    
 |_ _|_ _|_   _|__  ___| |___
  | || '_ \| |/ _ \/ _ \ (_-<
 |___| .__/|_|\___/\___/_/__/
     |_|                      
 

  Author : SinonX
  Family Attack Cyber & Tatsumi Crew                     

		"""+'\n')

	print('(+) 1. GENERATE IP')
	print('(+) 2. RANGE IP')
	print('(+) 3. IP CHECKER'+'\n')

	pilih = input('Select Options -> ')

	if pilih == '1':
		genip()
	elif pilih == '2':
		yoy()
	elif pilih == '3':
		diem = input('Input Your IP LIST -> ')
		thread(diem)
	else:
		print('No Options!')

