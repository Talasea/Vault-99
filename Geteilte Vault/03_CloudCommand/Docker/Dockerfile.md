---
created: 2025-01-28T12:04
updated: 2025-01-28T12:05
---
```
FROM debian:12.9

RUN apt update && apt install -y python3

COPY arsenal /root/arsenal
```