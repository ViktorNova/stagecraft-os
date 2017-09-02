stagecraft-os
=============

Real-time pro-audio appliance OS for modern electronic musicians and multimedia performances built on Linux, with a user interface designed to "boot and play" like pro-audio hardware does (this is not a 'desktop OS').

Features such as network MIDI, OSC routing & OSC <=> MIDI translation, DMX lighting control, pattern based groove sequencer, drum sampler, and high-quality softsynths/effects, are all pre-configured and ready to go out of the box (among many others)

#Extra repositories
**PPAs**
````
#Stagecraft OS - custom Ubuntu packages
add-apt-repository ppa:viktornova/stagecraftos

#Qt5 Configuration Tool
add-apt-repository ppa:hda-me/qt5ct

````

**Other repositories**
````
#Stagecraft OS non-launchpad repo
wget -qO - https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
sudo echo deb https://dl.bintray.com/viktornova/stagecraft-os / > /etc/apt/sources.list.d/stagecraft-os.list
sudo echo deb https://dl.bintray.com/viktornova/stagecraft-os-64 / >> /etc/apt/sources.list.d/stagecraft-os.list

````

##Todo: add KXstudio repos

