### Services

Services are objects in Kubernetes that provides stable networking 
(IP, DNS name, port) for Pods, by providing a static front-end 
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

Although services can function as load balancer and a gateway, there 
are downside. NodePort only works in port range 30000-32767, and 
LoadBalancer requires 1-to-1 mapping between the service and cloud 
load-balancer, which can be very expensive.  


#### Links
- [[Link](https://kubernetes.io/docs/concepts/services-networking/service/)] - Service object documentation
- [[Link](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)] - EndpointSlices object documentation

