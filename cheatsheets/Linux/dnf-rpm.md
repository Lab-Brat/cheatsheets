### dnf
#### basic commands
* `dnf install <package>` -> install package
* `dnf remove <package>` -> remove package
* `dnf update` -> update all packages
* `dnf downgrade <package>-<version>` - downgrade package to a lower version

#### update
* `dnf check-update` -> check available updates 
* `dnf list available <package> -> list `
* `dnf update --security` -> install only security updates
* `dnf update --advisory=RHSA-2014:0159` -> install security updates from a specific advisory

#### searching
* `dnf info <package>` -> info about package
* `dnf list installed` -> list installed packages
  * example: `dnf list installed vim*`
* `dnf --showduplicates list available <package>` -> list all available versions
* `dnf provides <package>` -> info general about package
  * example: `dnf provides "*/nginx.conf"`
* `dnf search <keyword>` -> search for keywords in package names
  * example: `dnf search text editor>` 

### repositories
#### basic commands
* `dnf repolist --enabled` -> view enabled repos 
* `dnf repolist -v epel` -> view detailed info 
* `dnf repolist --all` -> view all repos 
* `dnf config-manager --add-repo ...` -> add repo 
* `dnf config-manager --set-enabled ...` -> enable repo 
* `dnf config-manager --set-disabled ...` -> disable repo

#### repo configuration file
* `vim /etc/yum.repos.d/epel.repo` -> create repository file
* append the following content
```ini
[epel]
name=Extra Packages for Enterprise Linux $releasever - $basearch
Everything/$basearch/
metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-$releasever&arch=$basearch&infra=$infra&content=$contentdir
enabled=1
gpgcheck=1
countme=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-$releasever
```
* append the following line to disable update for a specific package
```ini
exclude=<package>
```

#### extras
* to view dnf variables (run the Python script)
```python
import dnf, json
db = dnf.dnf.Base()
print(json.dumps(db.conf.substitutions, indent=2))
```
* list all available options for config `dnf config-manager --dump`

### rpm
* `rpm -i <package>` -> install
* `rpm -e <package>`  -> remove
* `rmp -U <package>`  -> update
* `rpm -qa` -> list all
* `rpm -qip` -> info local package
* `rpm -qf` -> info general 

#### common issues
* Error: rpmdb open failed
```bash
# create backups folder
mkdir ~/rpm_backups/
cp -avr /var/lib/rpm/ ~/rpm_backups

# clear rpm db
rm -f /var/lib/rpm/__db*
db_verify /var/lib/rpm/Packages
rpm --rebuilddb
yum clean all
```
