### Minikube

Minikube is the best way to spin up a Kubernets cluster locally for practice and testing.  

#### Install and Deploy
First, make sure Docker is installed and running, since the cluster will be 
launched in Docker containers.  

Then install minikube with 2 commands:
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

To interact with the cluster, install `kubectl`:
```bash
sudo emerge --ask --quiet-build sys-cluster/kubectl
```

Before starting the cluster, install CSI drivers to be able to provision volumes in 
multi-node cluster:
```bash
minikube addons enable volumesnapshots
minikube addons enable csi-hostpath-driver
```

Spin up a 3 node cluser (control plane and 2 nodes):
```bash
minikube start --nodes 3 -p multinode
```

Check result:
```bash
kubectl get nodes
```


#### Links
- [[Link](https://minikube.sigs.k8s.io/docs/start/)] - Getting started doc
- [[Link](https://minikube.sigs.k8s.io/docs/tutorials/volume_snapshots_and_csi/)] - Installing CSI driver

