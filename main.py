from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json


# Initiate the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('http://161.200.155.233/cuds/TblStudentsInfo/Show-TblStudentsInfo-Table.aspx')

user_name = 64010
password =


browser.find_elements(By.NAME, "ctl00$PageContent$UserName")[0].send_keys(user_name)
browser.find_elements(By.NAME, "ctl00$PageContent$Password")[0].send_keys(password)
browser.find_element(By.ID, "ctl00_PageContent_OKButton__Button").click()
browser.find_element(By.ID, "ctl00__Menu__SubjectsElectionMenuItem__Button").click()




time.sleep(10)