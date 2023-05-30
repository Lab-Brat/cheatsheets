### Set up Gentoo package repository with Git

Install git:
```
emerge --ask dev-vcs/git
```

Create `/etc/portage/repos.conf/gentoo.git`:
```ini
[gentoo]
location = /var/db/repos/gentoo
sync-type = git
sync-uri = https://github.com/gentoo/gentoo.git
sync-depth = 0
```

Remove existing repo db:
```
mkdir ~/repo_backup
mv /var/db/repos/gentoo/ ~/repo_backup
```

Clone and set up the repository
```
emerge --sync
cd /var/db/repos/gentoo/
git fetch --unshallow
```

Checkout an old Portage tree state
```
git rev-list -n 1 --before="2023-04-01" master
git checkout <hash>
```
