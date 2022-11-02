# Arch Linux
#### OS Installation. 
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

* install packages
```
vim /etc/pacman.conf
pacstrap /mnt base base-devel linux linux-firmware sudo parted NetworkManager neovim git man-db
```

* generate an fstab file
```
genfstab /mnt -U >> /mnt/etc/fstab 
# (from arch-installation-scripts)
```

* chroot
```
arch-chroot
usradd -m oxxo
passwd 
nvim /etc/locale-gen
locale-gen
pacman -S grub efibootmgr os-prober
grub-install
grub-mkcobfig -o 
```

* Fix linux not found
```
mkinitcpio -p linux
pacman -S linux
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id="GRUB" 
grub-mkconfig -o /boot/grub/grub.cfg
(pacstrap didn't install linux correctly)
```

#### Post installation
* packages to install 
```
pacman -S usbutils fakeroot go 
```

* install xorg + gnome
```
pacman -S xf86-video-amdgpu xorg xorg-init gnome
```

* add AUR packages
```
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
