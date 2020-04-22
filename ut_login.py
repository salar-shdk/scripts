import requests, notify2, json


notify2.init('login service')

url = 'https://internet.ut.ac.ir/login'
check_url = 'http://acct.ut.ac.ir/IBSng/user/'

data_list = json.loads(open('/home/salar/scripts/ut_accounts.json').read()) 

def check_remaining_charge(data):
    data['normal_username'] = data['username']
    data['normal_password'] = data['password']

    response = requests.get(check_url,data)
    
    remaining_volume = response.text.split('Current Credit :')[1].split('2Col_light">')[1].split('MegaBytes')[0]
    
    return remaining_volume , not '-' in remaining_volume

for data in data_list:
    try:
        response = requests.post(url,data)
    except:
        n = notify2.Notification('login service', 'connect to ut network !')
        n.show()

    if 'You are logged in' in response.text:
        remaining_volume , any_volume_left = check_remaining_charge(data)
        n = notify2.Notification('login service', '{} logged in !\n{}Mb remained'.format(data['username'],remaining_volume))
        n.show()

        if(any_volume_left): break;
    elif 'already authorizing, retry later' in response.text:
        n = notify2.Notification('login service', 'u have 2 connected devices !')
        n.show()
    else :
        n = notify2.Notification('login service', 'error !')
        n.show()




