### Namespace

Docker uses namespaces to provide the isolated workspace, i.e container. 
When a container is launched, Docker creates a set of namespaces for it:
* `pid` namespace -> Process isolation
* `net` namespace -> Managing network interfaces
* `ipc` namespace -> Managing access to IPC resources
* `mnt` namespace -> Managing filesystem mount points
* `uts` namespace -> Different host and domain names
* `user` namespace -> Isolate security-related identifiers

#### Links
* [[Link](https://docs.docker.com/engine/security/userns-remap/)] - Docker documentation

