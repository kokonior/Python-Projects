import os
from re import T, findall
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import  datetime
import schedule
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json

os.environ['PATH'] += r"D:\All Software Zipp\Seleniumdriver"
opt=Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(chrome_options=opt)
driver.implicitly_wait(80)
driver.get("https://binomo-web.com/trading?token=ac2d9e3edbc1f5c16bda64b8abd9777c12bdf9d5c78cc7b201")

# Time Trade
timeNow = datetime.now()
timeConverted = timeNow.strftime("%H:%M")

def ha(): 
	saldo = ''
	afterSaldo = ''

	# get saldo awal
	print('Welcome kawan, pencari cuan!')
	before = driver.find_element(By.ID, "qa_trading_balance").text
	saldo += before
	print('saldo : ', saldo)

	# trade
	# time.sleep(2)
	trade = driver.find_element(By.XPATH, "/html/body/app-root/lib-platform-scroll/div/div/div/ng-component/main/div/app-panel/ng-component/binary-info/div[2]/div/vui-button[2]/button")
	ActionChains(driver).click(trade).perform()

	# get saldo after trade
	time.sleep(54) # masih perlu diadjust
	after = driver.find_element(By.ID, "qa_trading_balance").text
	afterSaldo += after
	print("Saldo Sekarang : ", afterSaldo)

	# checking saldo
	if afterSaldo < saldo:
		print('wkwkwkwk berkurang!')

		trade = driver.find_element(By.XPATH, "/html/body/app-root/lib-platform-scroll/div/div/div/ng-component/main/div/app-panel/ng-component/binary-info/div[2]/div/vui-button[2]/button")
		ActionChains(driver).click(trade).perform()
		ActionChains(driver).click(trade).perform()

		time.sleep(50) # masih perlu diadjust
		kompen = driver.find_element(By.ID, "qa_trading_balance").text

		if kompen < afterSaldo: 
			print('Yahh kompensasi gagal!')
			print( 'Tenang belum miskin mental :' , kompen)
			print('----', timeConverted , '----')
		else:
			print('Ngokey nggak jadi rugi ngab!')
			print( 'Ajib bener, mang :' , kompen)
			print('----', timeConverted , '----')
	else:
		# trade = driver.find_element(By.XPATH, "/html/body/app-root/lib-platform-scroll/div/div/div/ng-component/main/div/app-panel/ng-component/binary-info/div[2]/div/vui-button[1]/button")
		# ActionChains(driver).double_click(trade).perform()
		print('Cuan Cuan Cuan')
		print('----', timeConverted , '----')

# dummy signal
# with open('signal.json') as json_file: 
# 	signals = json.load(json_file)

# 	for item in signals: 
# 		tradeTime = item['openTime']
# 		tradeSignal = item['signal']

		# schedule.every().day.at(tradeTime).do(ha)

schedule.every().day.at('19:14').do(ha)
schedule.every().day.at('19:16').do(ha)
schedule.every().day.at('19:12').do(ha)
# schedule.every(5).seconds.do(ha)
# schedule.every(1).minutes.do(ha)


# when true
while True:
    schedule.run_pending()
    time.sleep(1)
