from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import account
import  school_scr

def register_subject(want_to_register_subject):
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
    wait_to_click_id = []

    for subject in want_to_register_subject:
        for position in list_of_position_of_subject:
            if (str(subject["subject_id"])== position["subject_id"] and str(subject["subject_name"]) == position["subject_name"]) and str(subject["group"]) == str(position["group"]):
                wait_to_click_id.append(position['check_box_name'])

    count = 0
    for id in wait_to_click_id:
        browser.find_element(By.NAME, id).click()
        load_control = browser.find_element(By.ID, "ctl00_PageContent_UpdatePanel1_UpdateProgress1")
        print(want_to_register_subject[count]["subject_name"])


    time.sleep(30)
