import re
import bs4


def filter_html_to_list_of_subject(source):
    # get id = View_ElectListTableControlGrid from html
    soup = bs4.BeautifulSoup(source, 'html.parser')
    table = soup.find('table', id='View_ElectListTableControlGrid')
    list_of_position_of_subject = []

    # for loop tr in table.find_all('tr'):
    for tr in table.find_all('tr'):
        # for loop all tag in tr
        count = 0
        for tag in tr:
            count += 1
            print(tag)


    print(list_of_position_of_subject)