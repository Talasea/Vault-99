---
created: 2024-11-21T12:43
updated: 2024-11-21T16:54
---
# OSPF

Initial setup

```
enable
configure terminal
router ospf 10
```

Activate networks

```
network 192.168.1.0 0.0.0.255 area 0 # inverse Subnetzmaske!
network <network> <inv_snmask> area <area>
```
