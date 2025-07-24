---
created: 2025-01-08T12:06
updated: 2025-01-08T17:06
---
```bash
openssl s_client \
    -connect 127.0.0.1:4433 \
    -tls1_3 \
    -keylogfile /tmp/sslkeyfile.log
```