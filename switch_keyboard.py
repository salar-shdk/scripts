import sys, getopt
import os

f = open('/home/salar/scripts/bin/current_keyboard.data','r')
current = f.read()
print(current)
f = open('/home/salar/scripts/bin/current_keyboard.data','w')
if 'us' in current:
    os.system('setxkbmap ir')
    f.write('ir')
elif 'ir' in current:
    os.system('setxkbmap us')
    f.write('us')
f.close()
