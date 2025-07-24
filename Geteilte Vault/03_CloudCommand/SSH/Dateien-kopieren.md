---
created: 2025-01-22T11:23
updated: 2025-01-22T11:25
---
Allgemein

```bash
scp $Datei $user@$remote:$Pfad
scp $user@$remote:$RemotePfad $LokalerPfad
```

Von Windows Host zu Kali Agent

```bash
scp .\malware kali@192.168.22.101:/home/kali
```

Von Kali Agent zu Windows Host

```bash
scp kali@192.168.22.101:/home/kali/malware .\Desktop\
```