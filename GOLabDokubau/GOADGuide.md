# GOAD Lab Cyber Kill Chain Attack Guide

## Überblick

Diese Anleitung orientiert sich an der Cyber Kill Chain von Lockheed Martin und zeigt systematisch die Möglichkeiten auf, das GOAD Lab vollständig zu kompromittieren. Der Guide deckt alle relevanten Angriffspfade, Szenarien, Techniken und aktuelle Methoden für die Windows Server AD-Umgebung ab (2019/2016). Tools, Scripts und beispielhafte Kommandos sind jeweils mit aufgeführt.

---

## 1. Reconnaissance – Informationssammlung

- **Netzwerkscan & Enumeration**
  - Nmap: Services, Ports, OS-Fingerprinting (z.B. `nmap -sV -O 192.168.56.0/24`)
  - Host Identification ohne Ping (Defender blockiert ICMP): `nmap -Pn ...`
  - AD-Recon mit Bloodhound, PowerView, AD Module, SharpHound
  - User/Group Enumeration, SID Mapping, Service Principal Names (Kerberoasting)
  - GPO-Enum: `Get-DomainGPO`, `gpresult`
  - LAPS-Detection, ACLs, Trusts über Bloodhound

- **Sichtbare Wege & Szenarien
  - User mit SPN: Kerberoasting, ASREP-Roasting
  - Legacy-Protokolle: LLMNR/NTLM/SMB/NBNS Spoofing, Responder
  - GPOs: Schwachstellen, Writeable GPOs

---

## 2. Weaponization – Vorbereitung des Exploits

- **Angriffstools vorbereiten**: Mimikatz, Rubeus, Impacket, Responder, CrackMapExec, SharpGPOAbuse, Empire, PowerShell-Module, Exegol
- **Payloads bauen** (Reverse Shell, Credential Stealer)
- **Schwachstellen in Gruppenrichtlinien vorbereiten (gefundene Write-DACL, Scheduled Tasks etc.)**

---

## 3. Delivery – Angriffsvektoren initialisieren

- **Phishing (lab-intern): File-Upload auf IIS (castelblack)
  - Offenes ASPX Upload (Webshell auf castelblack installieren)
  - MSSQL: Login-Versuche mit gefundenen Usern
  - SMB Share Angriff (Pass-the-Hash, Credential-Stealing)
- **NTLM Relay mit Responder, Angriff auf LLMNR/NetBIOS
- **Kerberos-Preauth Bypass: ASREPRoasting für User mit NoPreauth

---

## 4. Exploitation – Schwachstellen ausnutzen

- **Lokale Privilege Escalation** (Windows Server 2019/2016 spezifische Potatoes)
  - PrintSpoofer, RoguePotato, JuicyPotato, SweetPotato abhängig vom OS
  - SeImpersonatePrivilege Abuse, Token Theft
- **GPO-Abuse**: Scheduled Tasks, Disable Defender, Push Malware via GPO (SharpGPOAbuse)
- **Unconstrained Delegation Abuse**: TGT-Stealing von Servern mit Delegation
- **Kerberoasting/ASREPRoast**: Hashes mit Rubeus/Mimikatz extrahieren und offline cracken (hashcat)
- **ADCS Abuse**: ESC1-16, Zertifikatsschwächen für Persistenz & PrivEsc (siehe xbz0n@sh)
- **SYSVOL/GPO Password Retrieval**: Passwords in SYSVOL oder GPO Preferences auslesen
  - Tools: gpp-decrypt, findstr, Bloodhound

---

## 5. Installation – Etablieren von Persistenz

- **Backdoors installieren**: Neue Benutzer/Serviceaccounts, scheduled tasks
- **Golden/Silver Ticket**: Mit Mimikatz generieren und ins Gedächtnis laden
- **Shadow Credentials/ACLS**: Write-DACL auf Objekte, msDS-AllowedToActOnBehalfOfOtherIdentity (RBCD)
- **AdminSDHolder Abuse**: Über Bloodhound angreifbare Objekte identifizieren
- **MSSQL Linked Servers Abuse**: Trusted MSSQL Links zwischen castelblack/braavos für RCE nutzen

---

## 6. Command & Control – Steuerung/Bewegung im Netzwerk

- **Lateral Movement**
  - Pass-the-Hash, Pass-the-Ticket, PsExec, PowerShell Remoting, WMI, WinRM
  - Tokens mit Mimikatz/Rubeus extrahieren & injizieren
- **MSSQL Trusted Link Abuse**: Von castelblack zu braavos mit xp_cmdshell (siehe mayfly277 Blog)
- **GPO ImmediateTasks, scheduled tasks für persistente C2
- **Reverse Shells über Webshell, SMB, Powershell

---

## 7. Actions on Objective – Zielerreichung

- **Domain Admin/Forest Admin Übernahme**: Komplette Kontrolle
- **Datendiebstahl, Ransomware Deployment, ACL Manipulation, Trust Abuse**
- **Cross Forest Attacks (AccrossTheSea, DragonsFriends, Spys-Group)**
- **Cleanup, Defenses umgehen, EDRs ausschalten, Audit Spuren verwischen

---

## Tools & Cheat Sheet

- **Recon**: Bloodhound, Powerview, SharpHound, Adalanche, CrackMapExec
- **Exploitation**: Mimikatz, Rubeus, Responder, gpp-decrypt, SharpGPOAbuse, Empire, Impacket (mssqlclient.py, secretsdump.py, wmiexec.py)
- **Persistence**: Mimikatz, Rubeus, scheduled tasks, backdoors
- **Lateral Movement**: PsExec, PowerShell, WinRM, SMB, MSSQL trusted links

## Szenarien/Beispiel-Angriffspfade (GOAD)

1. **Pass-the-Hash über SMB** (castelblack, admin jeor.mormont)
2. **Kerberoasting mit jon.snow auf castelblack**
3. **ASREP-Roast auf brandon.stark**
4. **NTLM Relay responder auf eddard.stark**
5. **IIS ASPX-Webshell auf castelblack bei offener Datei-Uploadmöglichkeit**
6. **Shadow Credentials/MachineAccountQuota Abuse**
7. **Unconstrained Delegation abuse auf winterfell/castelblack (GPO/Delegation)
8. **GPO Abuse mit Write-DACL auf STARKWALLPAPER
9. **MSSQL Trusted Link RCE mit jon.snow zwischen castelblack und braavos (siehe mayfly277 Blog)
10. **AdminSDHolder Abuse (Bloodhound-Suche)
11. **ADCS Abuse / Zertifikatmissbrauch (Siehe xbz0n.sh)

---

## Referenzen & Quellen

- https://orange-cyberdefense.github.io/GOAD/labs/GOAD/
- https://mayfly277.github.io/categories/goad/
- https://xbz0n.sh/blog/adcs-complete-attack-reference
- https://github.com/S1ckB0y1337/Active-Directory-Exploitation-Cheat-Sheet
- https://github.com/Integration-IT/Active-Directory-Exploitation-Cheat-Sheet
- https://www.semperis.com/blog/group-policy-abuse-explained
- https://michaelfirsov.wordpress.com/configuring-windows-server-2019-exploit-guard/
- https://blog.knowit.eu/active-directory-introduction

---

## Hinweis

Jeder Schritt ist im GOAD Lab reproduzierbar, da alle Common, aktuelle Techniken und reale Schwachstellen abgebildet sind. Tools wie Bloodhound, Mimikatz, Rubeus, SharpGPOAbuse, CrackMapExec etc. sind im Angriff mandatory und können auch zur Verteidigung genutzt werden (Purple Knight, AD Audit+).

---
