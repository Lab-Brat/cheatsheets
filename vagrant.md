# Vagrant
#### command line tool
* initialize box
```
vagrant init ubuntu/focal64
```  
find boxes at https://app.vagrantup.com/boxes/search

* basic commands
```
# start
vagrant up

# turn off
vagrant halt

# restart box
vagrant reload

# ssh into the box
vagrant ssh

# display ssh details
vagrant ssh-config <node>
```

#### sample config file with loops
```
Vagrant.configure("2") do |config|
  
  servers=[
    {
      :hostname => "node1",
	  :ip       => "192.168.0.98",
      :box      => "ubuntu/focal64",
      :key      => "/vagrant/vg_box.pub"
    },
    {
      :hostname => "node2",
	  :ip       => "192.168.0.97",
      :box      => "almalinux/8",
      :key      => "/vagrant/vg_box.pub"
    }
  ]

  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
      node.vm.box = machine[:box]
      node.vm.hostname = machine[:hostname]
      node.vm.network "public_network", 
	                  ip: machine[:ip], 
	                  bridge: "Intel(R) Wi-Fi 6 AX200 160MHz"
      
      node.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.memory = "1024"
        vb.cpus = 1

      node.vm.provision "shell" do |s|
	    s.inline = "cat $1 >> /home/vagrant/.ssh/authorized_keys"
        s.args = machine[:key] 
      end
    end
  end
end
end
```

#### basic and messy sample config file
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  config.vm.box = "ubuntu/focal64"

  # Network Settings
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  # config.vm.network "private_network", ip: "192.168.0.110"
  config.vm.network "public_network", bridge: "wlp4s0"
  
  # Folder Settings
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider Settings
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2048"
    vb.cpus = 2
  end
 
  # Provision Settings
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
```
