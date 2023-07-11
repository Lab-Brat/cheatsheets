### Gitlab

#### Token
Token can be added to a restricted repository to gain clone rights.
* Open the repository main page.
* Go to `Settings` -> `Access Tokens`.
* Enter the following:
  * token name
  * expiration date
  * role (i.e developer)
  * scope (`read_repository` will suffice for cloning).
* `git clone https://${username}:${token}@gitlab.server.com/repo.git` -> use the token
