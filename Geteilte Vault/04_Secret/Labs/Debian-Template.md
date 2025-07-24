---
created: 2025-01-10T19:13
updated: 2025-01-10T19:14
---
```bash
!#/bin/bash

path="/mnt/pve/BX41/template/cloud-init/"
name="debian-12-genericcloud-amd64.qcow2"
tid="950"


qm create $tid --name debian12-cloudinit --net0 virtio,bridge=vmbr2 --scsihw virtio-scsi-pci --machine q35
qm set $tid --scsi0 local:0,discard=on,ssd=1,format=qcow2,import-from=$path$name
qm disk resize $tid scsi0 24G
qm set $tid --boot order=scsi0
qm set $tid --cpu host --cores 1 --memory 2048
qm set $tid --bios ovmf --efidisk0 local:1,format=qcow2,efitype=4m,pre-enrolled-keys=1
qm set $tid --ide2 local:cloudinit
qm set $tid --agent enabled=1

qm template $tid
```