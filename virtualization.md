# Virtualization
#### VirtualBox
* add guest additions  
```
#shutdown vm  
#add /user/share/virtualbox/VBoxGuestAdditions.iso  
#boot vm  
mkdir /cdrom  
mount /dev/cdrom /cdrom ; cd /cdrom  
sh VBoxLinuxAdditions.run --nox11 
```

* run commands in vm  
```
vboxmanage guestcontrol <VM name> --username root --password <pass> <command>
```

* **\[ERROR\]** no kernel modules installed rc=-1908  
```
install linux-headers dkms  
sudo /sbin/rcvboxdrv  
```

* **\[ERROR\]** RTR3InitEx failed with rc=-1912 (rc=-1912)  
```
sudo apt-get purge virtualbox-dkms
sudo apt-get install dkms  
sudo /sbin/vboxconfig
```

* **\[ERROR\]** virtualbox interface problem  
```
sudo vboxreload
```


#### VboxManage
* `vboxmanage list vms` -> list vms
* `vboxmanage list runningvms` -> list running vms
* `vboxmanage start <VM name>` -> turn on VM
* `vboxmanage controlvm <VM name> poweroff` -> turn off VM
* `vboxmanage controlvm <VM name> reset` -> reset VM
* `vboxmanage showvminfo --details <VM ID> | fgrep MAC` -> get mac address
* `vboxmanage dhcpserver findlease --network NatNetwork --mac-address=08002783E8BB` -> get ip address
* enlarge disk  
First, go to `Files` -> `Tools` -> `Virtual Media Manager` 
and change the virtual size of the disk. Detatch the disk, and:
```bash
vboxmanage showmediuminfo <disk_name>.vdi
vboxmanage modifyhd <UUID> --resize <Capacity>
```


### Useful links
* Troubleshooting  
https://rhv.bradmin.org/ovirt-engine/docs/Installing_Red_Hat_Virtualization_as_a_self-hosted_engine_using_the_command_line/Troubleshooting_SHE_SHE_cli_deploy.html
* vdsm-client  
https://www.ovirt.org/develop/developer-guide/vdsm/vdsm-client.html
