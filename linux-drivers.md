## Drivers

#### Basics
Usually drivers are accessed through device files in ```/dev``` directory, for example:
```console
labbrat@pop-os:~$ ls -l /dev/nvme0n1
brw-rw---- 1 root disk 259, 0 Sep 10 09:44 /dev/nvme0n1
```
in ```ls``` output of the device file, ```b``` stands for block device, 259 and 0 ```are m```ajor and minor numbers, 
which are used to map the file to actual driver by the kernel.  

Device files can be created manually with ```mknod``` command, 
but usually are created automatically and handled by ```udev``` daemon.  

```udevd``` uses device information from sysfs, which is mounted in ```/sys```. 
Sysfs is a virtual filesystem implemented by the kernel to provide detailed information about the system’s available devices.

The command ```udevadm``` is used to work with ```udev``` daemon, for example:
```console
labbrat@pop-os:~$ udevadm info -a -n /dev/nvme0n1
...
  looking at device '/devices/pci0000:00/0000:00:02.4/0000:02:00.0/nvme/nvme0/nvme0n1':
    KERNEL=="nvme0n1"
    SUBSYSTEM=="block"
    DRIVER==""
    ATTR{alignment_offset}=="0"
    ATTR{capability}=="0"
    ATTR{discard_alignment}=="0"
    ATTR{diskseq}=="9"
...
```  

Local rules can be created at ```/etc/udev/rules.d``` to modify default kernel actions on a device. 
For example using rule, it's possible to change default name and mount point of a USB device.
