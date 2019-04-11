# Pocketbeagle Wi-fi Hotspot Walk-through

**BELOW IS A STEP BY STEP GUIDE ON ENABLING INTERNET THROUGH USB AND DOWNLOADING HOSTAPD.
IT ALSO INCLUDES HOW TO AUTOMATE A WIFI HOTSPOT USING YOUR POCKETBEAGLE.**
First, enable Ethernet through USB on your Pocketbeagle by plugging it into your computer. 
Follow these steps to do so: 

1. Download PuTTy: https://www.putty.org/ 

2. Download the latest Debian version for Pocketbeagle at https://beagleboard.org/latest-images. 
I used the following image on this project: 
https://debian.beagleboard.org/images/bone-debian-9.3-iot-armhf-2018-03-05-4gb.img.xz 

3. Use Etcher and a SD card adapter to transfer the Debian .xz image into the SD card: https://www.balena.io/etcher/
 
4. Once flashed onto the SD card, plug the SD card into your pocketbeagle

5. Navigate to your control panel 

6. Go to Network and Sharing Center 

7. Go to 'Change adapter settings'

8. Go to your main Wi-Fi/ethernet connection and right click, click Properties 

9. Go to the Sharing tab 

10. Click the box that says 'Allow other network users to connect through this computer's Internet connection' 
and choose the 'Home networking connection' as the title of the Pocketbeagle's indentification, 
usually it should say 'Remote NDIS Compatible Device #X' 

11. Save your changes, 
go back to the network connections page and 
right click on your Pocketbeagle device's network and go to Properties. 

12. Left click on 'Internet Protocol Version 4 (TCP/IPv4)' and go to Properties below 

13. Use the following IP address (this is the gateway from your computer to the Pocketbeagle): 

IP address: ```192.168.7.1``` 
Subnet mask: ```255.255.255.0```

Leave everything else blank, even the preferred DNS server and press OK to save your changes. 

14. Start PuTTY 

15. Use ```192.168.7.2``` as your host name and ```22``` as your port number, and then connect

16. Login as: ```debian```, the password will be ```temppwd``` upon default 

17. Check connectivity. 
Type the following command: 

```
sudo nano /etc/resolv.conf
```


This will prompt you for the password, which is temppwd, and you will have an empty file. 
In the file you write: 
```
domain localdomain 
domain searchdomain 
nameserver 8.8.8.8 
nameserver 8.8.4.4 
```
Press ctrl+X and then Y to save and exit this file. 
This file sets up DNS resolution so you can ```ping google.com``` instead of ```ping 8.8.8.8```. 
Next in the terminal you will type:

```
sudo /sbin/route add default gw 192.168.7.1
```

This will set up the gateway to the internet. Next, test your connection to the internet by using the command: 

```
ping google.com
```

in your terminal. You should see packets starting to flow. Use ctrl+c to stop this. 

18. Go to this repository link and follow the instructions to install HostAPD:

https://github.com/IntelOpenDesign/MakerNode/wiki/Hostapd:-compiling-instructions




This next portion will describe the steps to create and automate your WiFi script.

1. Create a new file to hold your AP script. Name this whatever you choose.


Navigate to /home/debian/create_ap to create your new file in that folder.
```
cd /home/debian
sudo mkdir create_ap
cd create_ap
sudo nano filename.sh
```
If prompted, the password will be temppwd upon default.

2. In this file, type the following commands:
(to ensure sh will be used to interpret the script)
```
!/bin/sh -
```
(to resolve any domain name server issues because of create_ap)
```
sudo pkill -f 'dns'
```
(creating the AP to run in the background on 192.168.1.1 with the network named 'networkid' and having 'password' as password)

```
sudo create_ap -n -g 192.168.1.1 wlan0 networkID password &
```

(running the script in the background)
Navigate to ```/etc/systemd/system```

```
cd /etc/systemd/system
sudo nano myscript.service
```

within the script:
```
[Service]
Type=simple
ExecStart=/home/debian/create_ap/filename.sh
CPUSchedulingPolicy=rr
CPUSchedulingPrioty=27
[Install]
WantedBy=multi-user.target graphical.target
```
ctrl+x and y to save
set up service daemon to run on boot

```systemctl daemon-reload; systemctl enable myscript; systemctl start myscript```

It should now run in the background upon boot.
Within your filename.sh script you can also include any IO script you would like to run on boot after the create_ap command.
The scripts folder contains the scripts used in the Pocketbeagle DSTR project for reference.




