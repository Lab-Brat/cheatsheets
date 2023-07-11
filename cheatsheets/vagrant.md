# Vagrant
#### Common Tasks
* `vagrant init ubuntu/focal64` -> initialize box
* `vagrant up` -> start boxes
* `vagrant halt` -> stop boxes
* `vagrant reload` -> reload boxes
* `vagrant ssh` -> use Vagran's credentials to SSH into the box
* `vagrant ssh-config <node>` -> display SSH config details
* find boxes at https://app.vagrantup.com/boxes/search


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
	                  bridge: "wlp4s0"
      
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
