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


#### With TLS redirect
* Create directory for certificates: `mkdir /etc/nginx/ssl`
* Generate certificates:
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout /etc/nginx/ssl/assets-private.key   \
        -out /etc/nginx/ssl/assets-cert.pem
```

* Update the virtual host config: `vim /etc/nginx/conf.d/assets.example.com.conf`
```
server {
  listen 80;
  server_name assets.example.com;
  return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name assets.example.com;
    root /var/www/assets.example.com;
    
    ssl_certificate /etc/nginx/ssl/assets-cert.pem;
    ssl_certificate_key /etc/nginx/ssl/assets-private.key;
} 
```

#### NGINXConfig Tool
DigitalOcean has an interactive [tool](https://www.digitalocean.com/community/tools/nginx) 
to create Nginx configuration file.
