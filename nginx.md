### Nginx

#### Basic setup
* Add repository: `vim /etc/yum.repos.d/nginx.repo`
```
[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
```
* Start and enable: `systemctl enable --now nginx`
* Create content for virtual host
```
mkdir /var/www/www/assets.example.com
touch /var/www/www/assets.example.com/test.txt
echo 'TEST PASSED' > /var/www/www/assets.example.com/test.txt
```
* Create virtual host file: `vim /etc/nginx/conf.d/assets.example.com.conf`
```
server {
  listen 80;
  server_name assets.example.com;
  root /var/www/assets.example.com/;
}
```
* Reload Nginx settings: `systemctl reload nginx`
* Test: `curl --header "Host: assets.example.com" localhost/test.txt`

