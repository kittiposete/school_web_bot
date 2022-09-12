import platform
import json

# TODO: change your database to your json file
# you can see Structure in readme.md
database_path = '/Users/kittipos/Documents/database.json'

print(database_path)
database = json.load(open(database_path))
user_name = database['username']
password = database['password']
subject_list = database['subject_list']
