#this is the file you will start on boot in myscript.service

#!/bin/sh - #use sh shell
sudo pkill -f 'dns' # kill dns processes to avoid dns conflicts
sudo create_ap -n -g 192.168.1.1 wlan0 PocketDSTR dstrdstr & # create an AP on 192.168.1.1
                                                             # Network SSID: PocketDSTR
                                                             # Network password: dstrdstr
                                                             # & makes it run in the background
sudo python3 /home/debian/PocketDSTR/DSTR.py # run IO script for robotics purposes
                                             # use the 'DSTR Controller' app on the Play Store
