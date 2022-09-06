import bs4


def filter_html_to_list_of_subject(source):
    # get id = View_ElectListTableControlGrid from html
    soup = bs4.BeautifulSoup(source, 'html.parser')
    table = soup.find('table', id='View_ElectListTableControlGrid')
    list_of_position_of_subject = []

    count_row = 0
    for row in table.find_all('tr'):
        count_row += 1
        if count_row == 1:
            continue

        count_item = 0
        subject_name = ""
        subject_id = ""
        check_box_name = ""
        group = ""
        for item in row:
            count_item += 1
            if count_item == 1:
                if item.string == "\n":
                    count_item -= 1
                    continue
                check_box_name = item.find('input')['name']
            elif count_item == 2:
                if item.string == "\n":
                    count_item -= 1
                    continue
                subject_data = item.string
                subject_data = subject_data.replace(" ", "")
                subject_data = subject_data.split("\n")
                subject_id = subject_data[0]
                subject_name = subject_data[1]
            elif count_item == 6:
                if item.string == "\n":
                    count_item -= 1
                    continue

                # get value before </span>
                group = item.find('span').string
                group = group.replace("\n", "")

        list_of_position_of_subject.append({
            "subject_id": subject_id,
            'subject_name': subject_name,
            'check_box_name': check_box_name,
            'group': group
        })
    return list_of_position_of_subject
