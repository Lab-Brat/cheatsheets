# VboxManage

* `vboxmanage list vms` -> list vms
* `vboxmanage list runningvms` -> list running vms
* `vboxmanage start <VM name>` -> turn on VM
* `vboxmanage controlvm <VM name> poweroff` -> turn off VM
* `vboxmanage controlvm <VM name> reset` -> reset VM
* `vboxmanage guestproperty <VM name> "/VirtualBox/GuestInfo/Net/<interface ID>/V4/IP"` -> get IP address
* `vboxmanage showvminfo --details <VM ID> | grep MAC` -> get mac address
* `vboxmanage guestcontrol <VM name> --username root --password <pass> <command>` -> run command in a VM
* enlarge disk  
First, go to `Files` -> `Tools` -> `Virtual Media Manager` 
and change the virtual size of the disk. Detatch the disk, and:
```bash
vboxmanage showmediuminfo <disk_name>.vdi
vboxmanage modifyhd <UUID> --resize <Capacity>
```
