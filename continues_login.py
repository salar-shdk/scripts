import requests
import notify2 , os , time

notify2.init('login service')

url = 'https://internet.ut.ac.ir/logout'

while(True):
    os.system('python ~/scripts/ut_login.py')
    time.sleep(60)
    response = requests.get(url);
    time.sleep(11)

