from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.instagram.com/")
driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("vroomeee")
driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("finfin09")
driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]/button').click()
try:
    driver.find_element("xpath", '//*[@id="mount_0_0_as"]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
except:
    print("fail-1")
driver.find_element("xpath", '//*[@id="mount_0_0_Ri"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div')
driver.find_element("xpath", '//*[@id="mount_0_0_as"]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[5]/a/div[1]').click()