import datetime

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import account
import  school_scr
import json

def get_success_list():
    # start browser without GUI
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # browser = webdriver.Chrome(ChromeDriverManager().install())

    user_name = account.user_name
    password = account.password

    def connect_to_school_website_and_login():
        browser.get('http://161.200.155.233/cuds/TblStudentsInfo/Show-TblStudentsInfo-Table.aspx')

        browser.find_elements(By.NAME, "ctl00$PageContent$UserName")[0].send_keys(user_name)
        browser.find_elements(By.NAME, "ctl00$PageContent$Password")[0].send_keys(password)
        browser.find_element(By.ID, "ctl00_PageContent_OKButton__Button").click()
        browser.find_element(By.ID, "ctl00__Menu__SubjectsElectionMenuItem__Button").click()

    connect_to_school_website_and_login()
    table = browser.find_element(By.ID, "View_ElectedTableControlGrid")
    rows = table.find_elements(By.TAG_NAME, "tr")
    success_list = []
    for row in rows:
        column_count = 0
        # for loop row
        for column in row.find_elements(By.TAG_NAME, "th"):
            if column_count == 4:
                success_list.append(column.text)
            column_count += 1
    return success_list

get_success_list()