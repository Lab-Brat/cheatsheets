# openssl

#### Generate
* `openssl genrsa -out server.key 2048` -> Generate key
* `openssl req -key domain.key -new -out server.csr` -> Generate CSR
* `openssl x509 -signkey domain.key -in domain.csr -req -days 365 -out cert.pem` -> Generate certificate


#### Inspect
* `openssl rsa -check -in server.key` -> Inspect key
* `openssl req -text -noout -verify -in server.csr` -> Inspect CSR
* `openssl x509 -text -noout -in cert.pem` -> Inspect certificate


#### Verify Certificate
* `openssl verify -verbose -CAfile ca.pem client-cert.pem` -> verify that a cert was signed by CA
