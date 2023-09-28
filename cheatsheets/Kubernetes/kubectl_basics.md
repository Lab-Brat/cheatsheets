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

#### Probes
* `Livness`
* `Readiness`
* `Startup`

[Link](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) 
to official documentation on probes.  

#### Resources
* `Limits`
* `Requests`
* `Pod Priority`

[Link](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) 
to documentation on limits and requests.  

[Link](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) 
to documentation on pod priority.

**Note** Set requests and limits on all application and nodes, including 
master, for kubectl to correctly calculate total allocated resources. 
This is important becuase it will influence 
[quality of service](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)


#### Misc
* `kubectl compleltion bash > ~/.kube/compleltion.bash.inc` - add completion for kubectl bash commands 
