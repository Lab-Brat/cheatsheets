#### Script to check disk usage of fstab mount points
```bash
#!/bin/bash

function check_disk_usage() {
    # Read /etc/fstab
    while read -r line; do
        if [[ "${line}" = \#* ]] || [[ -z "${line}" ]]; then
            continue
        fi

        # Get the mount point
        mount_point=$(echo "${line}" | awk '{print $2}')

        if [[ ${mount_point} = "/tmp" || ${mount_point} = "swap" ]]; then
            continue
        fi

        if [[ ! -d "${mount_point}" ]]; then
            echo "Warning: mount point ${mount_point} does not exist."
            continue
        fi

        df -h "${mount_point}" |
            awk -v OFS=", " 'NR==2 {print "Disk usage for " "'"${mount_point}"'"" ===> Total=" $2, "Used=" $3, "Free=" $4, "Percent used=" $5}'

    done </etc/fstab
}

check_disk_usage
```
