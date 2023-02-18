

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

URL = r"https://ifconfig.me/"

chromedriver_autoinstaller.install()
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(URL) # подключаемся к сайту 

def ip_adress():
    result = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, """//*[@id="ip_address"]""")))
    time.sleep(2)
    result = driver.find_element(By.XPATH, """//*[@id="ip_address"]""")
    result = result.text # сохраняем результат в текстовом виде 

    return result

print("Ваш публичный IP-адрес: ", ip_adress()) # выводим результат 

k = input()