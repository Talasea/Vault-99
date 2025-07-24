---
created: 2025-01-08T12:08
updated: 2025-01-08T12:08
---
```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout server.key \
  -out server.crt -days 365 -subj "/CN=localhost"
```