### Basic kubectl commands

#### Pods
* `kubectl create -f pod.yaml` - create pod from yaml manifest
* `kubectl get pod` - list active pods
* `kubectl get pod --show-labels` - list active pods with a specific label
* `kubectl delete pod --all` - delete all pods
* `kubdectl describe pod <pod_name>` - show additional pod info

#### Replicaset
* `kubectl create -f replicaset.yaml` create replicaset from yaml manifest
* `kubectl apply -f replicaset.yaml` apply yaml manifest changes to replicaset
* `kubectl get replicaset` - list active replicasets
* `kubectl scale --replicaset=2 replicaset <replicaset_name>` - scale to 2 replicasets
* `kubectl describe replicaset <replicaset_name>` - show additional info about replicaset

#### Deployment
* `kubectl create -f deployment.yaml` -> create deployment from yaml manifest
* `kubetctl get deploy` -> list active deployments
* `kubetctl set image deployment <dep_name> '*=nginx:1.13'` -> update image version for all pods in the deployment
* `kubetctl rollout undo deployment <dep_name>` -> roll back to nginx:1.12

#### Misc
* `kubectl compleltion bash > ~/.kube/compleltion.bash.inc` - add completion for kubectl bash commands 
