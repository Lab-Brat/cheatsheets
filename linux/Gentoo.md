### Gentoo Linux
#### VirtualBox Installation (UEFI)
System Requirements
* RAM: 4GB
* CPU: 4
* Disk: 30GB  

Turn on SSH
```
rc-service sshd start
```  

Partition Disk
```
fdisk /dev/sda
g
n 1 _ +256M
t 1
n 2 _ +4G
t 2 19
n 3 _ _
p
w
```  

Write Filesystems
```
mkfs.vfat -F 32 /dev/sda1
mkfs.ext4 /dev/sda3
mkswap /dev/sda2
swapon /dev/sda2
```  

Mount Root Partition
```
mount /dev/sda3 /mnt/gentoo
```  

Download and Unpack Stage3
```
cd /mnt/gentoo
wget https://bouncer.gentoo.org/fetch/root/all/releases/amd64/autobuilds/20230205T170201Z/stage3-amd64-openrc-20230205T170201Z.tar.xz
tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner
```  

Select Mirrors
```
mirrorselect -i -o >> /mnt/gentoo/etc/portage/make.conf
mkdir --parents /mnt/gentoo/etc/portage/repos.conf
cp /mnt/gentoo/usr/share/portage/config/repos.conf /mnt/gentoo/etc/portage/repos.conf/gentoo.conf
```  

Copy DNS Info
```
cp --dereference /etc/resolv.conf /mnt/gentoo/etc/
```  

Mounting Filesystems Before Chroot
```
mount --types proc /proc /mnt/gentoo/proc
mount --rbind /sys /mnt/gentoo/sys
mount --make-rslave /mnt/gentoo/sys
mount --rbind /dev /mnt/gentoo/dev
mount --make-rslave /mnt/gentoo/dev
mount --bind /run /mnt/gentoo/run
mount --make-slave /mnt/gentoo/run
```  

Chroot
```
chroot /mnt/gentoo /bin/bash
source /etc/profile
export PS1="(chroot) ${PS1}"
```  

Mount Boot Partition
```
mount /dev/sda1 /boot
```  

Configure Portage
```
emerge-webrsync
emerge --sync
eselect news read
emerge --ask --verbose --update --deep --newuse @world
emerge --ask app-portage/cpuid2cpuflags
cpuid2cpuflags
echo "*/* $(cpuid2cpuflags)" > /etc/portage/package.use/00cpu-flags
echo "sys-kernel/linux-firmware @BINARY-REDISTRIBUTABLE" | tee -a /etc/portage/package.license
```  

Timezone
```
echo "Europe/Istanbul" > /etc/timezone
emerge --config sys-libs/timezone-data
```  

Locale
```
nano -w /etc/locale.gen
locale-gen
eselect locale set 4
env-update && source /etc/profile && export PS1="(chroot) ${PS1}"
```
