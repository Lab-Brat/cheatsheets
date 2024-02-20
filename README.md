## Cheatsheets
This repository is a collection of cheat sheets and notes on various topics, 
mainly focused around programming, Linux and DevOps.  

Cheat sheets can be accessed via an API:
```bash
# find cheat sheets will 'git' in the filename
curl https://labbrat.net/notes/find/git

# print cheat git.md sheet
curl https://labbrat.net/notes/git
```

Repo also has a Python CLI tool to validate `README.md` and show some info 
about cheat sheets. Here is what it can do now:
```bash
# Check if there are discrepancies between readme and files in ./cheatsheets 
./verfiy_readme 

# Check which files have less than 1 lines of content in it
./verfiy_readme -s

# Print help message
./verfiy_readme -h
```
  

#### cheatsheets
* `css-basics.md` - Really basic CSS stuff.
* `flutter_setup.md` - Set up Flutter and Android SDK on Arch Linux.
* `git.md` - Basic Git commands.
* `gpg.md` - GPG keys.
* `git_config.md` - Local git configuration.
* `gitlab.md` - GitLab configuration.
* `irc.md` - common tasks in IRC.
* `jenkins.md` - Jenkins configuration.
* `nginx.md` - Nginx configuration.
* `nvim.md` - Neovim keys.
* `nvim_plus.md` - NvChad and LunarVim keys.
* `pypi.md` - Some tips and memos on using PyPI.
* `vagrant.md` - Setup Vagrant box and run it.
* `vim.md` - vim command key bindings.
* `Ansible` - Directory of cheatsheets about Ansible.
  * `ansible-ad-hoc.md` - Ansible ad hoc commands.
  * `ansible-playbook.md` - run Ansible playbook and advanced concepts.
  * `ansible.md` - Ansible cli options and ad hoc commands.
* `Arch` - Arch Linux notes
  * `arch_install.md` - installation guide
  * `pacman.md` - Pacman and yay notes
* `BashScripts` - Handy bash scripts.
  * `clean_dir.sh` - Delete old filed in a directory.
  * `get_docker_images_du.sh` - Read docker images sizes that are older than 2w and sum it up.
  * `repo_on_off.sh` - Enable/disabled repositories on RHEL in bulk.
* `Containers` - Containerization theory and practice.
  * `containers_general.md` - Terminology guide.
  * `container_lifecycle.md` - Step-by-step lifecycle of a container.
  * `docker_commands.md` - Commands to administrate docker containers.
  * `namespace.md` - Understand namespaces and how it is used in Docker.
* `GoogleSRE` - notes on Site Reliability Engineering book,
  * `ch3_risk.md` - Chapter 3 Embracing Risk.
  * `ch5_toil.md` - Chapter 5 Eliminating Toil.
* `Gentoo`
  * `gentoo-chroot.md` - Chroot to Gentoo from Arch installation media.
  * `gentoo-install.md` - Gentoo installation walkthrough.
  * `gentoo-git.md` - Setting up Portage to sync packages with Git.
  * `gentoo-realtek.md` - Troubleshooting realtek wifi drivers
  * `Portage.md` - Gentoo package manager commands.
* `Kubernetes`
  * `kubectl_basics.md` - Basic kubecl commands.
  * `kubernetes_architecture.md` - Architecture cheatsheets.
  * `kubernetes_deployment.md` - Information on Deployments.
  * `kubernetes_pod.md` - Information on Pods.
  * `kubernetes_probes.md` - Information on Probes.
  * `kubernetes_resources.md` - Information on Resources.
  * `kubernetes_service.md` - Information on Services.
  * `minikube.md` - Install and use Minikube.
* `linux` - Directory of cheatsheets on various Linux topics.
  * `Arch.md` - Commands used to setup Arch Linux distribution.
  * `awk.md` - Use awk to parse command line output.
  * `beeper.md` - Play Empire Anthem on motherboard beeper.
  * `bash-conditions.md` - Conditionals in Bash.
  * `bash-control-flow.md` - Control flow in Bash.
  * `certificates.md` - Manage TLS certificates using certtool and openssl.
  * `one_liners.md` - One-line bash scripts.
  * `curl-wget.md` - Download files and read html page with curl and wget.
  * `diagnostics.md` - Disk usage and other system diagnostics.
  * `diagnostics-scripts.md` - Helpful scripts for Linus syst diagnostics.
  * `dnf-rpm.md` - DNF and YUM package manager commands.
  * `drivers.md` - Information on how drivers are processed in Linux.
  * `drivers-network.md` - Information on how to troubleshoot network dirvers.
  * `firewall-firewalld-scripts.md` - Bash scripts for firewalld configuration.
  * `firewall-firewalld.md` - RHEL specific firewalld and Debian specific ufw.
  * `firewall-iptables.md` - Firewall configuration with iptables.
  * `grep.md` - search and filter text with grep.
  * `grub.md` - Boot process and grub configuration.
  * `infra.md` - Infrastructure administrations tools, like ldapsearch, dig etc.
  * `kernel.md` - Modify and install custom Linux kernel.
  * `logs.md` - Manage logs and configuration of a centralized log server.
  * `network.md` - Basic network managing, such as configuration of network interfaces and ports.
  * `network-diagnostics.md` - Network diagnostics using mtp, traceroute and tracepath.
  * `process.md` - Find information about running processes and top utility.
  * `random.md` - Some random Linux commands, i.e copy CLI output to clipboard, check GUI session etc.
  * `sed.md` - sed command to edit cli output.
  * `shell_shortcuts.md` - Shortcuts in Bash/zsh.
  * `ssh.md` - Commands to setup ssh authentication between servers and it's configuration.
  * `tmux.md` - Tmux basic commands.
  * `top.md` - Systems stats with top command.
  * `users-acess.md` - Manage users, groups and their access.
* `Virtualization`
  * `vboxmanage.md` -> Cheat sheet on vboxmanage.
  * `virtualbox_issues.md` -> Common issues in Virtualbox
