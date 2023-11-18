# VirtualBox
## List of Issues
* add guest additions  
```
#shutdown vm  
#add /user/share/virtualbox/VBoxGuestAdditions.iso  
#boot vm  
mkdir /cdrom  
mount /dev/cdrom /cdrom ; cd /cdrom  
sh VBoxLinuxAdditions.run --nox11 
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

## Useful links
* [[Link]](https://rhv.bradmin.org/ovirt-engine/docs/Installing_Red_Hat_Virtualization_as_a_self-hosted_engine_using_the_command_line/Troubleshooting_SHE_SHE_cli_deploy.html) - Troubleshooting
* [[Link]](https://download.virtualbox.org/virtualbox/) - VDSM client 
* [[Link]](https://download.virtualbox.org/virtualbox/) - VirtualBox Downloads page

