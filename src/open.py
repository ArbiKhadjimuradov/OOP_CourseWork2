import os

current_dir = os.path.dirname(__file__)

PATH_TO_FILE = os.path.join(current_dir, '..', 'data', 'vacancies.json')

print(PATH_TO_FILE)