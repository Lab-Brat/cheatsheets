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

Kernel (genkernel)
```
emerge --ask sys-kernel/linux-firmware
emerge --ask sys-kernel/gentoo-sources
eselect kernel list
eselect kernel set 1
ls -l /usr/src/linux
emerge --ask sys-kernel/genkernel
echo '/dev/sda1       /boot   ext4    defaults        0 2' >> /etc/fstab
genkernel all
ls /boot/vmlinu* /boot/initramfs*
```  

Update fstab
```
/dev/sda1   /boot        vfat    defaults,noatime     0 2
/dev/sda2   none         swap    sw                   0 0
/dev/sda3   /            ext4    noatime              0 1

/dev/cdrom  /mnt/cdrom   auto    noauto,user          0 0
```  

Set Hostname and Change Password
```
echo gentoo_v1 > /etc/hostname
passwd
```  

System Tools
```
emerge --ask net-misc/dhcpcd
rc-update add dhcpcd default
rc-service dhcpcd start

emerge --ask app-editors/vim

emerge --ask app-admin/sysklogd
rc-update add sysklogd default

emerge --ask sys-process/cronie
rc-update add cronie default
crontab /etc/crontab

emerge --ask sys-apps/mlocate
rc-update add sshd default

emerge --ask net-misc/chrony

rc-update add chronyd default
emerge --ask sys-fs/e2fsprogs
```  

Install Grub Bootloader
```
echo 'GRUB_PLATFORMS="efi-64"' >> /etc/portage/make.conf
emerge --ask sys-boot/grub
grub-install --target=x86_64-efi --efi-directory=/boot
echo 'GRUB_DISABLE_OS_PROBER=false' >> /etc/default/grub
grub-mkconfig -o /boot/grub/grub.cfg
```  

Exit
```
exit
cd
umount -l /mnt/gentoo/dev{/shm,/pts,}
umount -R /mnt/gentoo
reboot
```  
