---
created: 2025-01-29T10:31
updated: 2025-01-29T10:32
---
```yaml
services:
  webserver1:
    image: httpd:latest
    container_name: webserver1
    ports:
      - "8080:80"

  webserver2:
    image: httpd:latest
    container_name: webserver2
    ports:
      - "8081:80"
```