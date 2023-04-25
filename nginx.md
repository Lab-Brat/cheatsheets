### Nginx

#### Basic setup
* `vim /etc/yum.repos.d/nginx.repo` -> Add repository
```ini
[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
```
* `systemctl enable --now nginx` -> Start and enable
* Create content for virtual host
```bash
mkdir /var/www/www/assets.example.com
touch /var/www/www/assets.example.com/test.txt
echo 'TEST PASSED' > /var/www/www/assets.example.com/test.txt
```
* `vim /etc/nginx/conf.d/assets.example.com.conf` -> Create virtual host file
```
server {
  listen 80;
  server_name assets.example.com;
  root /var/www/assets.example.com/;
}
```
* `systemctl reload nginx` -> reload Nginx settings
* `curl --header "Host: assets.example.com" localhost/test.txt` -> test

#### With TLS redirect
* `mkdir /etc/nginx/ssl` -> Create directory for certificates
* Generate certificates:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout /etc/nginx/ssl/assets-private.key   \
        -out /etc/nginx/ssl/assets-cert.pem
```

* `vim /etc/nginx/conf.d/assets.example.com.conf` -> Update the virtual host config
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
