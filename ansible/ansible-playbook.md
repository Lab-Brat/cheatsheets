### ansible-playbook
#### Inventory
* custom inventory ```ansible-playbook -i curom_inventory playbook.yaml```

#### Limit
* limit playbook to groups ```ansible-playbook playbook.yml --limit webservers```
* limit playbook to hosts ```ansible-playbook playbook.yml --limit test1.lab```

#### List
* list hosts ```ansible-playbook playbook.yaml --list-hosts```

#### Concurrency
* run tasks concurrently ```ansible-playbook init_config.yaml --forks=2```

#### Dry Run
* dry run ```ansible-playbook init_config.yaml --check```
