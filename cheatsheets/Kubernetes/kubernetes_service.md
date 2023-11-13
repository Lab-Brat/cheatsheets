### Services

Services are objects in Kubernetes that provides stable networking 
(IP, DNS name, port) for Pods. They are like having a static front-end 
and a dynamic back-end. The front-end consists of the IP, DNS name, and 
port that never changes. The back-end comprises the list of healthy Pods 
and can be constantly changing.  

Services are loosely coupled with Pods via labels and selectors, which 
means pods needs to have all labels the services is selecting on.  

Under the hood, service object uses EndpointSlice object to store the 
up-to-date list of active pods.  

Service types:
* ClusterIP: stable virtual IP that's only accessible from inside the cluster.
* NodePort: extension of ClusterIP, exposes a port to outside.
* LoadBalancer: grants external access via a public IP or DNS name.
