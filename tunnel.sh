#!/usr/bin/expect


eval spawn "ssh -fN -D 6666 salar@49.12.6.2 -p 22222"
expect "assword:"   # matches both 'Password' and 'password'
send "salarglx110\r";
interact
