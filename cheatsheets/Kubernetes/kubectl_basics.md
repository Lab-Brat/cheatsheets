### Basic kubectl commands

<object> == pod, replicaset, deployment etc.

#### Working with cluster
* `kubectl get nodes` - get control plane and worker nodes
* `kubectl describe node <node_name>` - show node information

#### Create / Delete
* `kubectl create -f <object_name>.yaml` - create an object from yaml manifest
* `kubectl delete <object> <object_name>` - delete a single object
* `kubectl delete <object> --all` - delete all objects
* `kubectl expose deployment <deployment_name> --type=NodePort` - attach a service to a deployment

#### Get Information
* `kubectl get <object>` - list active pods
* `kubectl get <object> --show-labels` - list active pods with a specific label
* `kubectl get <object> --watch` - interactively follow object launches
* `kubectl describe <object> <object_name>` - show additional pod info
* `kubectl describe pods spec.initContainers` - show a specific parameter of a pod
* `kubectl explain <object>` - describe fields and structure of various resources

#### Modify Existing Object
* `kubectl set image deployment <dep_name> '*=nginx:1.13'` -> update image version for all pods in the deployment
* `kubectl rollout undo deployment <dep_name>` -> roll back to nginx:1.12
* `kubectl scale --replicaset=2 replicaset <replicaset_name>` - scale to 2 replicasets
* `kubectl exec --stdin --tty <pod_name> -- /bin/sh` - open interactive shell to container

#### Misc
* `kubectl compleltion bash > ~/.kube/compleltion.bash.inc` - add completion for kubectl bash commands 
