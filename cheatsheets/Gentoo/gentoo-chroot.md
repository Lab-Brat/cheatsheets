### Chroot Gentoo For Troubleshooting

* `iwctl station wlan0 connect <wifi-name>` -> Configure WiFi on the host machine
* `cryptsetup open /dev/nvme0n1p3 part_main` ->  If the disk is encrpyted, first step is to decrypt it
* `mkdir /mnt/gentoo && mount /dev/mapper/part_main /mnt/gentoo/` -> Mount the main partition with Gentoo:
* `mount --types proc /proc /mnt/gentoo/proc` -> Mount proc
* `for part in sys dev run; do mount --rbind /$part /mnt/gentoo/$part && mount --make-rslave /mnt/gentoo/$part; done` -> Mount proc, dev, run and sys
* `chroot /mnt/gentoo /bin/bash` -> Chroot
* `source /etc/profile` -> Source environment
* `export PS1="(chroot) ${PS1}"` -> Configure prompt

### Links
- [[Link](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting)] - Gentoo wiki on chrooting
