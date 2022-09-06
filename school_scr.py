# get checkbox name from subject name
# this load subject name from school website as list of string

# web scraping
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())

user_name = account.user_name
password = account.password


def connect_to_school_website_and_login():
    browser.get('http://161.200.155.233/cuds/TblStudentsInfo/Show-TblStudentsInfo-Table.aspx')

    browser.find_elements(By.NAME, "ctl00$PageContent$UserName")[0].send_keys(user_name)
    browser.find_elements(By.NAME, "ctl00$PageContent$Password")[0].send_keys(password)
    browser.find_element(By.ID, "ctl00_PageContent_OKButton__Button").click()
    browser.find_element(By.ID, "ctl00__Menu__SubjectsElectionMenuItem__Button").click()

def get_checkbox_subject_name_as_list_of_string():
    