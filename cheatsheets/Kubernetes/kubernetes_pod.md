## Pod

### Intro
Pod - atomic unit of scheduling in Kubernetes.  

Why not just run containers instead of pods?  
**Pods are enhanced containers**  
For Kubernetes to be able to do all it's magic, it's needs 
to apply additional attributes to containers. For example: 
labels and annotations, restart policies, probes, affinity 
rules, termination control security policies, resource 
requests and limits...  

Some useful commands:
* `kubectl explain pods --recursive` -> To check all attributes
* `kubectl explain pod.spec.restartPolicy` -> Explain pod restart policy

All the additional attributes make it easy to schedule on 
which nodes to run pods and enable resource (file system, RAM etc.) 
sharing between containers in the pod.  

