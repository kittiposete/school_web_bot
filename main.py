# multi threading

import threading
import time
import account
import worker

list_of_subject = account.subject_list
list_of_thread = []

# run worker as thread
for subject in list_of_subject:
    t = threading.Thread(target=worker.register_subject, args=([subject],))
    list_of_thread.append(t)
    t.start()
