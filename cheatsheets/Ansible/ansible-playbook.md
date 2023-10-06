### ansible-playbook
* Inventory
    * `ansible-playbook -i curom_inventory playbook.yaml` -> custom inventory 
* Limit
    * `ansible-playbook playbook.yml --limit webservers` -> limit playbook to groups 
    * `ansible-playbook playbook.yml --limit test1.lab` -> limit playbook to hosts 
* List
    * `ansible-playbook playbook.yaml --list-hosts` -> list hosts 
* Concurrency
    * `ansible-playbook init_config.yaml --forks=2` -> run tasks concurrently 
* Dry Run
    * `ansible-playbook init_config.yaml --check` -> dry run 
