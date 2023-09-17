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

**Additionally**  
Also install network manager to simplify wifi connections.
```bash
echo 'net-misc/networkmanager bluetooth dhclient iwd systemd tools wifi' >> /etc/portage/package.use/networkmanager
emerge --ask --quiet-build networkmanager

# disconnect previous connections in iwd
iwctl known-networks SSID forget

systemctl start --now NetworkManager
nmclie device wifi list
nmcli device wifi connect <SSID> password <password>
```


**Alternatively, install 3rd party drivers**  
Driver link: https://github.com/lwfinger/rtw89  
Steps to install:
```bash
git clone https://github.com/lwfinger/rtw89.git
cd rtw89
make
make install
```

And deactivate some module features by creating `/lib/modprobe.d/70-rtw.conf`
```bash
options rtw89pci disable_clkreq=y disable_aspm_l1=y disable_aspm_l1ss=y
options rtw89core disable_ps_mode=y
```


### Links
* [[Link](https://github.com/lwfinger/rtw89/issues/262)] - Github Issue 262
* [[Link](https://github.com/lwfinger/rtw89/issues/240)] - Github Issue 240
* [[Link](https://www.reddit.com/r/archlinux/comments/14bkwsu/rtw89_8852be_issues_on_kernel_638/)] - Reddit post about driver
* [[Link](https://forums.gentoo.org/viewtopic-t-1074064-start-0.html)] - Gentoo Forums, similar issue
* [[Link](https://wiki.ubuntu.com/Kernel/Firmware)] - Ubuntu Wiki about firmware
