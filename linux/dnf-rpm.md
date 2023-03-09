### dnf
#### basic commands
* install `dnf install <package>`
* remove `dnf remove <package>`
* update `dnf update`

#### update
* check available updates `dnf check-update`
* install only security updates `dnf update --security`

#### searching
* info local `dnf info <package>`
* list all `dnf list installed`
  * example `dnf list installed vim*`
* info general `dnf provides <package>`
  * example: `dnf provides "*/nginx.conf"`
* search for keywords `dnf search <keyword>`
  * example `dnf search text editor>`
 

### repositories
#### basic commands
* view enabled repos `dnf repolist --enabled`
* view detailed info `dnf repolist -v epel`
* view all repos `dnf repolist --all`
* add repo `dnf config-manager --add-repo ...`
* enable repo `dnf config-manager --set-enabled ...`
* disable repo `dnf config-manager --set-disabled ...`

#### add repository manually
* create config `vim /etc/yum.repos.d/epel.repo`
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

#### extras
* to view dnf variables (run the Python script)
```python
import dnf, json
db = dnf.dnf.Base()
print(json.dumps(db.conf.substitutions, indent=2))
```
* list all available options for config `dnf config-manager --dump`

### rpm
* install `rpm -i <package>`
* remove `rpm -e <package>` 
* update `rmp -U <package>` 
* list all `rpm -qa`
* info local `rpm -qip`
* info general `rpm -qf`

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
