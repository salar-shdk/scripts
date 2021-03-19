import requests , os
import notify2
import socket

notify2.init('Network Info')

url = 'https://internet.ut.ac.ir/login'

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

public_ip= requests.get('https://api.ipify.org/').content
f= open('/home/salar/scripts/bin/public_ip_temp.txt','w')
public_ip = public_ip.decode()
print(public_ip)
f.write(str(public_ip))

local_ip = get_ip()
f= open('/home/salar/scripts/bin/public_ip_temp.txt','r')
public_ip = f.read()


print(public_ip , local_ip) 
n = notify2.Notification('Network Info', 'local ip : {}\npublic ip : {}\n'.format(local_ip,public_ip))
n.show()

