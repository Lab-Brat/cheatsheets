### fdisk

#### non-interactive commands
* `fdisk -l` -> list partitions

#### interactive commands
fdisk /dev/sdX
* `p` -> Display the partition table for the current disk.
* `n` -> Create a new partition.
* `d` -> Delete an existing partition.
* `t` -> Change a partition's type (e.g., to change filesystem type).
* `l` -> Display available partition types.
* `q` -> Quit without saving changes.
* `w` -> Write changes and exit.
