---
created: 2025-01-10T19:16
updated: 2025-01-10T19:17
---
```bash
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-genericcloud-amd64.qcow2
# sudo apt-get install libguestfs-tools
virt-customize -a debian-12-genericcloud-amd64.qcow2 --install qemu-guest-agent,curl,wget,nano,vim
```