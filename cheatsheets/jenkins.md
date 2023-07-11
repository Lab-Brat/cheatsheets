### Jenkins Cheatsheet
#### Agent configuration
* Dashboard >> Manage Jenkins >> Manage nodes and clouds
* \+ New node >> Permanent Agent
* Configure following settings:
    * name: agent1
    * description: vagrant jenkins-agent1.lab host
    * Number of executors: 2
    * Remote root directory: /var/lib/jenkins
    * Launch method: SSH
        * 192.168.56.121
        * choose credentials, create if doesn't exist
        * Host Key Verification Strategy: Manually trusted key Verification Strategy
        * Advanced: JavaPath = /bin/java
* Save

#### Agent as a Docker container
To use Jenkins Agent as a Docker container:
* Install `Docker Pipeline` plugin
* Allow jenkins user to run Docker commands: `usermod -aG docker jenkins`
* Run `Jenkinsfile-docker-node` pipeline from the `jenkins-infra` repository.
    * `Dashboard` -> `New Item` -> `Pipeline`
    * `Pipleline` -> `Pipleline script from SCM`
    * `SCM`: Git
    * `URL`: https://github.com/Lab-Brat/jenkins-infra.git
    * `Credentials` -> anything, repo is available with https
    * `Branch`: Master
    * `Script Path`: jenkins-infra/jenkinsfiles/
<br>
