### Deployment

Controller that helps release, rollout and deploy stateless apps. 
Deployment object only manages a single Pod template in multiple replicas. 
Abstractions of deployment object: 
```
Deployment ---> Replicaset ---> Pod ---> Container
Rollout &       Scaling &       Scheduling &  
Rollbacks       self-healing    resource sharing
```

Scaling and self-healing is achieved by state reconciliation. 
Namely, when desired state differs from observed (actual/current) state 
Kubernetes attempts to fix it. For example, If 10 replicas are defined 
but only 8 are currently online (for whatever reason), ReplicaSet 
controller brings up two more replicas.  

Consider rolling update and rollback procedure:
- `kubectl apply -f <deploy.yml,svc.yml>` -> deploy
- `kubectl <get,describe> <deploy/rs>` -> inspect
- update image version and reapply
- [optional] `kubectl rollout <pause/resume> deploy hello-deploy` -> pause rolling update
- watch update, pod num will change from 9-11 as defined in manifest
- `kubectl rollout history deployment hello-deploy` -> check rollout history
- `kubectl describe rs hello-deploy-<hash> | grep Image` -> check image version in revisions
- `kubectl rollout undo deployment hello-deploy --to-revision=1` -> roll back
- check final result


Deployment Manifest
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-deploy
spec:
  replicas: 10
  selector:
    matchLabels:
      app: hello-world
  revisionHistoryLimit: 5
  progressDeadlineSeconds: 300
  minReadySeconds: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-pod
        image: nigelpoulton/k8sbook:1.0
        ports:
        - containerPort: 8080
```
