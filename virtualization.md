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
* list vms
```
vboxmanage list vms
vboxmanage list runningvms
```

* turn on and off
```
vboxmanage start <VM name>
vboxmanage controlvm <VM name> poweroff
```

* extra
```
vboxmanage showvminfo --details 46ec9075-f49b-4d16-9867-d56710b6a3da | fgrep MAC
vboxmanage dhcpserver findlease --network NatNetwork --mac-address=08002783E8BB
```


#### KVM+libvirt+qemu
* basic commands 
```
virsh start <VM name>
virsh list

virsh shutdown <VM name>
virsh destroy 
virsh undefine 
```

* configure network 
```
virsh net-dumpxml default > default.xml
#change: name, uuid, bridge name, mac, ip, ip range, and rename file nat2.xml
virsh net-define nat2.xml
virsh net-start nat2.xml
virsh net-autostart nat2.xml
virt net-list
```

#### Ovirt
##### installing ovirt-engine-sdk-python
* use python version 3.9, update pip
* install prerequisites:
    * pip: ```python -m pip install pycurl```
    * Debian: ``` sudo apt install libcurl4-openssl-dev libssl-dev libxml2-dev libxslt1-dev```
    * RHEL: ```sudo dnf install libcurl-devel libxslt-devel libxml-devel libxml2-devel```
* install sdk: ```python -m pip install ovirt-engine-sdk-python```

* pycurl ImportError fix
    * ```python -m pip uninstall pycurl```
    * add following to /etc/bashrc
    ```
    export PYCURL_SSL_LIBRARY=openssl
    export PYCURL_SSL_LIBRARY=nss
    export CPPFLAGS=-I/usr/local/opt/openssl/include
    export LDFLAGS=-L/usr/local/opt/openssl/lib
    ```
    * exit session, reinstall pycurl

### Useful links
* Troubleshooting  
https://rhv.bradmin.org/ovirt-engine/docs/Installing_Red_Hat_Virtualization_as_a_self-hosted_engine_using_the_command_line/Troubleshooting_SHE_SHE_cli_deploy.html
* vdsm-client  
https://www.ovirt.org/develop/developer-guide/vdsm/vdsm-client.html
