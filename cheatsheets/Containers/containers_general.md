### Container Terminology and General Information

#### Container Runtime
At a high level, the container runtime is the software responsible for running containers. 
It's what allows you to create and manage containers on your system.

Low-Level vs High-Level Runtimes:
* `Low-Level Runtimes` -> These are responsible for the actual mechanics of running a container, such as interfacing with the OS to create the isolated environments. Examples include runc and crun. They handle the specifics of creating the namespaces, cgroups, etc., needed for isolation.
* `High-Level Runtimes` -> These provide additional features on top of the base container runtime, like pulling images, managing images, network setup, and higher-level orchestration. Docker and containerd are examples of high-level runtimes. They often utilize low-level runtimes (like runc) under the hood to actually run the containers.  

In many setups, a high-level runtime will call a low-level runtime. 
For example, Docker originally used runc under the hood to actually start the container process, 
but now it uses containerd. When containerd needs to start a new container, 
it invokes runc with the necessary specifications defined in an OCI bundle.  


#### OCI (Open Container Initiative)
To ensure compatibility and interoperability in the container ecosystem, 
OCI was formed to create open standards for container formats and runtimes. 
Tools like runc are OCI-compliant, meaning they adhere to these standards.  


#### OCI Bundle
When you request the creation of a container, the specifications for that container 
(e.g., root filesystem, environment variables, arguments) are assembled into an OCI bundle.  

This bundle contains a config.json, which is a detailed spec of the container, including the necessary namespaces, cgroups, capabilities, etc.  

runc uses this config.json to understand how to set up and run the container.  


#### Shims
A shim is often a lightweight process that sits between the container runtime and the container process itself. 
Its primary goal is to keep the container's STDIO and other resources open even if the container runtime crashes 
or is restarted. This allows for better process management and decouples the lifecycle of the container from 
that of the runtime.

In other words, when `runc` starts a container, it forks itself and the child process becomes the container's 
main process. This would mean that if `containerd` needs to track the container process, it'd have to keep 
`runc` running, which isn't efficient. To solve this, `containerd-shim` is used. 
It's a small binary that `containerd` starts, which then starts `runc` to run the container. 
This shim process remains alive for the life of the container, 
allowing `containerd` to not hang onto the runc process.


#### Namespaces
Namespaces are a feature of the Linux kernel that provide isolation for running processes. 
Different types of namespaces isolate different aspects of the system.  

When a container starts, it gets its own set of namespaces, which is what provides the isolation 
from other containers and the host system.  

To create a namespace, the clone() system call or the unshare() system call is used. 
For instance, invoking clone() with the CLONE_NEWPID flag will create a new PID namespace.  

When runc starts a container, it uses these system calls, as specified in the OCI bundle, 
to create the necessary namespaces for the container.  


#### cgroups (Control Groups)
While namespaces provide process isolation, cgroups are used to limit and monitor the resources 
a process or set of processes can use, like CPU, memory, I/O, etc. 
Together with namespaces, cgroups are fundamental to creating isolated container environments.  

runc, using the OCI spec, creates and manages cgroups for containers through the cgroup filesystem, 
usually mounted under /sys/fs/cgroup. For instance, when a container needs limited memory, 
runc will create an appropriate cgroup under /sys/fs/cgroup/memory and then adjust the settings 
in files like memory.limit_in_bytes.

