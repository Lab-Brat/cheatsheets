### Combined Commands and One-Liners

* `for f in *_prefix_*.epub; do mv "$f" "${f/_prefix_}"; done` -> remove `_prefix_` from all filenames
* `grep 'Host '  ~/.ssh/config | awk '{$1=""; print $0}' | sed 's/^ //'` -> print all Hosts from config file and remove trailing space
* `for i in $(seq 46 -1 36); do history -d $i; done` -> delete history lines 46->36
* `cat ~/.ssh/<key>.pub | ssh <hostname.com> "sudo bash -c 'cat >> /root/.ssh/authorized_keys'"` -> add SSH key to root user
* `cat ~/.ssh/id_rsa | ssh <hostname> "sudo bash -c 'cat >> /root/.ssh/authorized_keys'"` -> apped key to root user via ssh
* `for f in $(ls src/*.py); do wc -l $f; done | awk '{sum += $1} END {print sum}'` -> count the total lines of code in .py files
