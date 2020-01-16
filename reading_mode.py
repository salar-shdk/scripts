import os
import notify2
import subprocess, signal

def clean():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.splitlines():
        if b'xflux' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)

notify2.init('test service')
f=open('/home/salar/scripts/bin/tmp_reading_mode.txt','r')
mode = int(f.read())
f.close()

clean()

f=open('/home/salar/scripts/bin/tmp_reading_mode.txt','w')
if mode == 1 :
    f.write('0')
    f.close()
    n = notify2.Notification('reading mode : OFF')
    n.show()
    os.system('faketime \'2018-02-24 16:16:16\' xflux -l 32.42 53.68')
else :
    f.write('1')
    f.close()
    n = notify2.Notification('reading mode : ON')
    n.show()
    os.system('faketime \'2018-02-24 23:23:23\' xflux -l 32.42 53.68')




