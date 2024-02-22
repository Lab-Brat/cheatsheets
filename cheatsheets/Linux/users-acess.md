#### User Management
* `useradd <name>` -> Create a user
* `usermod -aG <group> <name>` -> Add user to a group

#### User root access
visudo

#### ACL
* `getfacl ./` -> get ACL info of the current directory
* `setfacl -d -m user_name:rwx ./` -> give `user_name` rwx access to current directory
* `setfacl -m user_name:r-x ./` -> give `user_name` only read and execute access to directory
