---
created: 2025-01-08T12:05
updated: 2025-01-08T12:05
---
```bash
openssl s_server \
    -accept 4433 \
    -cert server.crt \
    -key server.key \
    -tls1_3
```