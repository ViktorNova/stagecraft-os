#!/bin/sh
setxkbmap us -option terminate:ctrl_alt_bksp &
sleep 2
/opt/bin/start-up &
#exec lxqt-session # IT'S BROKEN =(
exec xfce4-panel &

# Start audio apps
exec ~/SYSTEM/scripts/stagecraft_startup_gui.sh  &
node /home/guest/Desktop/NODE/node-rtpmidi-git/examples/rtpmidi-native-bridge.js &
qmidiroute ~/SYSTEM/GLOBAL/stagecraft-midi-router.qmr &
qmidiroute ~/SYSTEM/GLOBAL/stagecraft-midi-router2.qmr &
a2j_control ehw start  &
aj-snapshot -d /home/guest/SYSTEM/GLOBAL/GLOBAL-MIDI-PATCHBAY.xml &
tilda &
fdpowermon & 
xfce4-notes &
exec i3
#claudia &
#openbox-session
