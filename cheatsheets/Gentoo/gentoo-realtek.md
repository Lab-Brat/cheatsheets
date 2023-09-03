### Troubleshoort Wi-Fi with Realtek

#### Troubleshoot
Kernel module output
```bash
lscpi -k
```

Modprobe output
```bash
modprobe
```

Kernel info
```bash
uname -r
eselect kernel list
```

#### Solution
According to [this](https://askubuntu.com/questions/1412450/network-driver-for-realtek-10ecb852) 
Stack Overflow post, solution is to use a 3rd party driver of upgrade to kernel > 6.2

Upgrade kernel
Steps:
* `echo 'sys-kernel/gentoo-sources ~amd64' > /etc/portage/package.keyword/gentoo-sources` -> Unmask latest kernel source
* `emerge --ask gentoo-sources` -> Install source
* `eselect kernel list #set <ID>` -> Select new kernel source
* Configure and build kernel following [documentation](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#Installation)
    * Configure iwlwifi drivers ([doc](https://wiki.gentoo.org/wiki/Iwlwifi))
    * Configure LUKS drivers ([doc](https://wiki.gentoo.org/wiki/Dm-crypt))
* Copy Kernel
```bash
cd /boot/efi/
mv vmlinuz.efi vmlinuz.efi.old
mv initramfs.img initramfs.img.old
cp /boot/vmlinuz-<v> ./vmlinuz.efi
cp /boot/initramfs-<v>.img ./initramfs.img
```

**3rd party drivers**  
Driver link: https://github.com/lwfinger/rtw89  
Steps to install:
```bash
git clone https://github.com/lwfinger/rtw89.git
cd rtw89
make
make install
mkdir /usr/lib/firmware/rtw89
cp  rtw8852a_fw.bin  /usr/lib/firmware/rtw89/
modprobe rtw89pci
```
Steps are take from [here](https://askubuntu.com/questions/1352260/wifi-adapter-not-found-realtek-10ec8852-on-ubuntu-21-04)


### Links
* [[Link](https://forums.gentoo.org/viewtopic-t-1074064-start-0.html)] - Gentoo Forums, similar issue
* [[Link](https://wiki.ubuntu.com/Kernel/Firmware)] - Ubuntu Wiki about firmware
