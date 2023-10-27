### Resources
* `Limits`
* `Requests`
* `Pod Priority`

**Note** Set requests and limits on all application and nodes, including 
master, for kubectl to correctly calculate total allocated resources. 
This is important becuase it will influence 
[quality of service](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)

#### Links
- [[Link](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)] - documentation on limits and requests.  
- [[Link](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/)] - documentation on pod priority.
