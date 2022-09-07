
import json
import threading
import time
import account
import worker

print("starting system")
list_of_subject = account.subject_list
print("strating 2")
list_of_thread = []
complete_subject = []
max_thread = 60
# run worker as thread
# create json if file not exist
# with open('complete.json', 'w') as f:
#     json.dump({'complete': []}, f)

# start get_success_list
# get_t = threading.Thread(target=get_success_list.get_success_list, args=())
# get_t.start()


while True:
    # check is thread is close
    for thread in list_of_thread:
        if not thread.is_alive():
            list_of_thread.remove(thread)

    # check if thread is full
    if len(list_of_thread) >= max_thread:
        time.sleep(1)
        continue
    for subject in list_of_subject:
        t = threading.Thread(target=worker.register_subject, args=([subject],))
        list_of_thread.append(t)
        t.start()
    # load complete.json
    # with open('complete.json', 'r') as f:
    #     data = json.load(f)
    #     complete_subject = data['complete']
    # remove complete subject from list_of_subject
    for s in list_of_subject:
        if s in complete_subject:
            # list_of_subject.remove(s)
            pass
    # clear complete_subject
    complete_subject.clear()
    # print(list_of_subject)
    # if len(list_of_subject) == 0:
    #     break

    if len(list_of_thread) >= max_thread*0.8:
        time.sleep(1.75)
    elif len(list_of_thread) >= max_thread*0.5:
        time.sleep(1)
    else:
        time.sleep(0.5)
