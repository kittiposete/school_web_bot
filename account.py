import platform
import json


if platform.system() == 'Windows':
    database_path = 'C:\\Users\\user\\Document\\database.json'
else:
    database_path = '/Users/kittipos/Documents/database.json'

print(database_path)
database = json.load(open(database_path))
user_name = database['username']
password = database['password']
subject_list = database['subject_list']