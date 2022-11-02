### Arch Linux
#### OS Pre-Installation
* connect to wifi
```
iwctl 
device list
station device get-networks
station device connect SSID
iwctl --passphrase passphrase station device connect SSID
```

* set time
```
timedatectl set-ntp true
timedatectl set-timezone Eurpoe/Istanbul
```

* create boot and encrypted main partitions
```
# write random data on disk
shred --random-source=/dev/urandom --iterations=1 /dev/nvme0n1

# create a partition table
parted -s /dev/nvme0n1 mklabel gpt

# create a boot partition
parted -s /dev/nvme0n1 mkpart boot fat32 1MiB 257MiB
parted -s /dev/nvme0n1 set 1 esp on
mkfs.fat -F 32 /dev/nvme0n1p1

# create encrypted lvm parition
parted -s /dev/nvme0n1 mkpart cryptlvm 257MiB '100%'
cryptsetup luksFormat /dev/nvme0n1p2
# enter 'YES', and enter a strong password
cryptsestup open /dev/nvme0n1p2 cryptlvm
pvcreate /dev/mapper/cryptlvm
vgcreate volgrp /dev/mapper/cryptlvm

# create swap partition
lvcreate -L 8G volgrp -n swap
mkswap /dev/volgrp/swap

# create main partition
lvcreate -l '100%FREE' volgrp -n system
mkfs.ext4 -F /dev/volgrp/system
```

* mount partions
```
mount /dev/volgrp/system /mnt
mkdir /mnt/boot
mount /dev/nvme0n1p1 /mnt/boot
swapon /dev/volgrp/swap
```

#### OS Installation
* install the system and some packages
```
pacstrap /mnt base base-devel linux linux-firmware lvm2
```

* generate an fstab file
```
genfstab /mnt -U >> /mnt/etc/fstab 
# (from arch-installation-scripts)
```

* chroot and change root password and install essentials
```
arch-chroot /mnt
passwd 
pacman -S NetworkManager git vim
```

* set locales
```
echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
locale-gen
echo 'LANG=en_US.UTF-8' > /etc/locale.conf
```

* install boot-loader
```
# install bootloader
systemd-machine-id-setup
bootctl --path=/boot install

# Get UUID of the boot partition
uuid=$(blkid | grep 'crypto_LUKS' | egrep -o ' UUID="[^"]+"')
uuid=$(echo $uuid | awk -F '=' '{ print $2 }' | tr -d '"')

# create bootloader configs
cat <<EOF >/boot/loader/entries/arch.conf
title   Arch Linux
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options cryptdevice=UUID=${uuid}:cryptlvm root=/dev/volgrp/system
EOF

cat <<EOF >/boot/loader/loader.conf
default arch
timeout 0
editor  0
EOF
```

* create ramdisk environment (for encryption to work)
```
vim /etc/mkinitcpio.conf
# change line -->
# HOOKS=(base udev autodetect modconf block filesystems keyboard fsck encrypt lvm2)
mkinitcpio -P
```

* install grub [alternative to bootctl]
```
pacman -S grub efibootmgr os-prober
grub-install
grub-mkcobfig -o 
```

* Fix linux not found [if install grub fails]
```
mkinitcpio -p linux
pacman -S linux
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id="GRUB" 
grub-mkconfig -o /boot/grub/grub.cfg
(pacstrap didn't install linux correctly)
```

#### Post installation
* install xorg + gnome
```
pacman -S xf86-video-amdgpu xorg xorg-init gnome
```

* add AUR packages
```
pacman -S base-devel
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si
```

* Install nvidia drivers
```
sudo pacman -S nvidia
sudo pacman -S nvidia nvidia-libgl nvidia-settings
sudo systemctl enabel nvidia-persistenced.service
reboot
lspci -k | grep -A 2 -E "(VGA|3D)"
nvidia-smi
```

#### Using OS
* core.df unrecognized format (add mirrors)
```
#Get mirrorlist from archlinux.org/mirrorlist
#Select only Russian mirrors
rm -R /var/lib/pacman/sync*
pacman -Syyu
```

* Install old linux-headers
```
pacman -U /var/cache/pacman/pkg/linux-h...
# if it's not there, download from archive.archlinux.org/packages
```
