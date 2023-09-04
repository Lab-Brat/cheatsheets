### Linux Network Drivers

Check Network card: 
* `lspci` -> check all connected devices on PCI
* `lspci -k` -> check all connected devices and which drivers are used
* `lspci -k | grep -A3 -i network` -> check drivers used for network card
* `lshw -C network` -> Check network info with lshw

Check drivers:
* `lsmod` -> list kernel modules. Drivers will often be loaded as modules.
* `modinfo <module-name>` -> show detailed module info
