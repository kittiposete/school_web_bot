import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import account
import school_scr


def register_subject(want_to_register_subject):
    # start browser without GUI
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # browser = webdriver.Chrome(ChromeDriverManager().install())

    user_name = account.user_name
    password = account.password
    time_out = 15

    def connect_to_school_website_and_login():
        browser.get('http://161.200.155.233/cuds/TblStudentsInfo/Show-TblStudentsInfo-Table.aspx')

        start_time = datetime.datetime.now()
        while True:
            try:
                browser.find_elements(By.NAME, "ctl00$PageContent$UserName")[0].send_keys(user_name)
                break
            except:
                if (datetime.datetime.now() - start_time).seconds > time_out:
                    exit()

        start_time = datetime.datetime.now()
        while True:
            try:
                browser.find_elements(By.NAME, "ctl00$PageContent$Password")[0].send_keys(password)
                break
            except:
                if (datetime.datetime.now() - start_time).seconds > time_out:
                    exit()

        start_time = datetime.datetime.now()
        while True:
            try:
                browser.find_element(By.ID, "ctl00_PageContent_OKButton__Button").click()
                break
            except:
                if (datetime.datetime.now() - start_time).seconds > time_out:
                    exit()

        start_time = datetime.datetime.now()
        while True:
            try:
                browser.find_element(By.ID, "ctl00__Menu__SubjectsElectionMenuItem__Button").click()
                break
            except:
                if (datetime.datetime.now() - start_time).seconds > time_out:
                    exit()

    connect_to_school_website_and_login()

    list_of_position_of_subject = school_scr.filter_html_to_list_of_subject(browser.page_source)
    wait_to_click_id = []

    for subject in want_to_register_subject:
        for position in list_of_position_of_subject:
            if (str(subject["subject_id"]) == position["subject_id"] and str(subject["subject_name"]) == position[
                "subject_name"]) and str(subject["group"]) == str(position["group"]):
                wait_to_click_id.append(position['check_box_name'])

    count = 0
    for id in wait_to_click_id:
        print("click")
        start_time = datetime.datetime.now()
        while True:
            try:
                browser.find_element(By.NAME, id).click()
                break
            except:
                if (datetime.datetime.now() - start_time).seconds > time_out:
                    exit()


        start_time = datetime.datetime.now()
        while True:
            try:
                load_control = browser.find_element(By.ID, "ctl00_PageContent_UpdatePanel1_UpdateProgress1")
                break
            except:
                if (datetime.datetime.now() - start_time).seconds > time_out:
                    exit()
        start_time = datetime.datetime.now()
        start_load = False
        while True:
            if datetime.datetime.now() - start_time > datetime.timedelta(seconds=3):
                break
            try:
                if load_control.get_attribute("style") == "display: block;" and start_load == False:
                    start_load = True
                if load_control.get_attribute("style") == "display: none;" and start_load == True:
                    break
            except:
                pass
        print(want_to_register_subject[count]["subject_name"])
        # add subject id to complete.json
        # with open('complete.json', 'r') as f:
        #     data = json.load(f)
        #     data['complete'].append(want_to_register_subject[count])
        # with open('complete.json', 'w') as f:
        #     json.dump(data, f)
        # count += 1
        # time.sleep(10)


# register_subject(       [
#         {
#             "subject_id": "อ22236",
#             "subject_name": "กิจกรรมเพิ่มพูนคำศัพท์ภาษาอังกฤษ4",
#             "group": "1"
#         }
#     ])