### Linux Kernel

#### Download Linux sources
Linux sources: https://www.kernel.org

Download Linux 6.5.2
```bash
wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.5.2.tar.xz
```

#### Configure and Build
Configure kernel
```bash
cd /usr/src/linux
make menuconfig
```

Build kernel
```bash
make
make modules_install
make install
```

#### Switch Kernels
Deactivate old kernel and activate the new one
```bash
cd /boot/efi
mv vmlinuz mvlinuz.bak
cp ../vmlinux-6.5.2_x86 ./vmlinuz
```
