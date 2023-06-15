### Firewalld Scripts

#### Restore Docker zone
```bash
#!/bin/bash

# Create the zone
sudo firewall-cmd --permanent --new-zone=docker
sudo firewall-cmd --permanent --zone=docker --set-target=ACCEPT
sudo firewall-cmd --permanent --zone=docker --add-interface=docker0

# Get the bridge interface(s) that starts with br- followed by 12 characters
bridge_interfaces=$(ip -o link show | grep -oE 'br-[0-9a-f]{12}' | sort | uniq | tr '\n' ' ')

# Add the bridge interfaces to the docker zone
for bridge_interface in $bridge_interfaces; do
    sudo firewall-cmd --permanent --zone=docker --add-interface="$bridge_interface"
    echo "added ${bridge_interface} interface to docker zone"
done

# Reload firewalld to apply changes
sudo firewall-cmd --reload

# Show the configuration for the docker zone
sudo firewall-cmd --zone=docker --list-all


```
