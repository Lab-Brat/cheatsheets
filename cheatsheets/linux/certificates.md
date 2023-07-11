### TLS Certificates

#### Create self-signed TLS certificates
* Create CA template
```
cat <<EOF > ca.cfg
organization = "HomeLab"
unit = "Me"
country = "US"
state = "CA"
cn = "CA-Cert"
expiration_days = 3650
ca
signing_key
cert_signing_key
EOF
```

* Create client certificate template
```
cat <<EOF > client.cfg
organization = "HomeLab"
unit = "Me"
country = "US"
state = "CA"
cn = "client1.lab"
expiration_days = 3650
challenge_password = 
tls_www_client
tls_www_server
EOF
```

* Create CA
```
certtool --generate-privkey --outfile ca-key.pem
certtool --generate-self-signed    \
         --load-privkey ca-key.pem \
         --outfile ca.pem  \
         --template ca.cfg
```

* Create Certificate
```
certtool --generate-privkey \
         --outfile client-key.pem \
         --sec-param High
certtool --generate-request \
         --load-privkey client-key.pem \
         --outfile request.pem  \
         --template client.cfg
certtool --generate-certificate \
         --load-request request.pem   \
         --outfile client-cert.pem    \
         --load-ca-certificate ca.pem \
         --load-ca-privkey ca-key.pem \
         --template client.cfg
```

#### Verify Certificate
* Check CA - cert
```
openssl verify -verbose -CAfile ca.pem client-cert.pem
```
