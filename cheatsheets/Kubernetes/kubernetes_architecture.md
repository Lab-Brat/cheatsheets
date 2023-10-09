### Architecture

#### Control Plane
Exposes the API, has a scheduler for assigning work, 
and is responsible for monitoring and  keeping apps 
healthy, i.e self-healing, autoscaling, rollouts and more.  

Components:
* `kube-apiserver` -> all (internal + external) cluster communications goes through it
* `etcd` -> The cluster store holding cluster state
* `scheduler` -> watches the API server for new work tasks and assigns them to appropriate healthy worker nodes
* `controller` -> process that ensures the observed state of the cluster matches the desired state
* `controller manager` -> multiple controllers packaged into a binary and used to monitor cluster components and respond to events
* `cloud controller manager` -> controller manager but for a public cloud provider


#### Worker Nodes
Every-day hard work of executing user applications.

Components:


#### Links
* [[Link](https://kubernetes.io/docs/concepts/architecture/)] - Kubernetes cluster architecture documentation

