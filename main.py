# from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
import time
import json
import platform
import account
import  school_scr

browser = None
if platform.system() == 'Windows':
    browser = webdriver.Opera(OperaDriverManager().install())
else:
    browser = webdriver.Chrome(ChromeDriverManager().install())

user_name = account.user_name
password = account.password

def connect_to_school_website_and_login():
    browser.get('http://161.200.155.233/cuds/TblStudentsInfo/Show-TblStudentsInfo-Table.aspx')

    browser.find_elements(By.NAME, "ctl00$PageContent$UserName")[0].send_keys(user_name)
    browser.find_elements(By.NAME, "ctl00$PageContent$Password")[0].send_keys(password)
    browser.find_element(By.ID, "ctl00_PageContent_OKButton__Button").click()
    browser.find_element(By.ID, "ctl00__Menu__SubjectsElectionMenuItem__Button").click()

connect_to_school_website_and_login()

list_of_position_of_subject = school_scr.filter_html_to_list_of_subject(browser.page_source)

time.sleep(10)
