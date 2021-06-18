#!/bin/bash

# Make sure your Android device is plugged in and accessible over adb.

#### Remember to enable virtual displays in xorg by adding the following to your configuration (e.g. /usr/share/X11/xorg.conf.d/20-virtual.conf)
# Section "Device"
#    Identifier "intelgpu0"
#    Driver "intel"
#    Option "VirtualHeads" "1"
#EndSection
#### If you use AMD or Nvidia, change the Identifier and Driver options to match your GPU.

W=1920      # Virtual display width
H=1080      # Virtual display height
O=VIRTUAL1  # The name of the virtual display (check using xrandr)
P=eDP1      # The name of your physical display (check using xrandr)
PW=1920

# Create the virtual display
gtf $W $H 60 | sed '3q;d' | sed 's/Modeline//g' | xargs xrandr --newmode
gtf $W $H 60 | sed '3q;d' | sed 's/Modeline//g' | awk '{print $1;}' | sed 's/^.\(.*\).$/\1/' | xargs xrandr --addmode $O
gtf $W $H 60 | sed '3q;d' | sed 's/Modeline//g' | awk '{print $1;}' | sed 's/^.\(.*\).$/\1/' | xargs xrandr --output $O --same-as $P --mode
    
# Forward the VNC port to your device and start a VNC session
#adb reverse tcp:5900 tcp:5900
#x11vnc -localhost -clip ${W}x${H}+${PW}+0
x11vnc -clip ${W}x${H}+${PW}+0
#vncserver -clip ${W}x${H}+${PW}+0
# When the session ends, turn off the virtual display
xrandr --output $O --off

