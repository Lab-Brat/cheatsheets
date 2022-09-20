### Gitlab

#### Token
Token can be added to a restricted repository to gain clone rights.
* Open the repository main page.
* Go to ```Settings``` -> ```Access Tokens```.
* Enter token name, expiration date, role (i.e developer) and scope (```read_repository``` will suffice for cloning).
* Copy the token.  

To use the token, use the following command
```console
labbrat@pop-os:~$ git clone https://${username}:${token}@gitlab.server.com/repo.git
```
