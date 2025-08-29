# 🔒 GOAD Lab - Phase 2: Weaponization & Delivery Analysis

> **Penetrationstester:** Timi  
> **Datum:** 27. August 2025  
> **Labor:** Game of Active Directory (GOAD)  
> **Phase:** 2 - Weaponization & Delivery (Cyber Kill Chain)

---

## 📋 Executive Summary

In Phase 2 der GOAD Lab Analyse wurden erfolgreich **mehrere kritische Schwachstellen** identifiziert und **gültige Credentials** durch **Kerberoasting** und **AS-REP Roasting** Angriffe erlangt. Der Zugriff auf **3 von 5 Zielsystemen** wurde erfolgreich etabliert.

### 🎯 **Kritische Erfolge:**
- ✅ **2 Benutzer-Credentials geknackt** (jon.snow, brandon.stark)
- ✅ **SMB-Zugriff auf 3 Systeme** etabliert
- ✅ **Sensible Dateien** in Shares entdeckt
- ✅ **100+ kritische CVEs** identifiziert

---

## 🌐 Network Discovery Results

### **Identifizierte Zielsysteme:**

| **IP-Adresse** | **Hostname** | **Rolle** | **Domain** | **OS** | **Status** |
|----------------|--------------|-----------|------------|---------|------------|
| 192.168.20.1 | Gateway | pfSense Router | - | FreeBSD | ✅ Active |
| 192.168.20.10 | KINGSLANDING | Primary DC | sevenkingdoms.local | Windows Server 2019 | ✅ Active |
| 192.168.20.11 | WINTERFELL | Child DC | north.sevenkingdoms.local | Windows Server 2019 | ✅ Active |
| 192.168.20.12 | MEEREEN | Forest DC | essos.local | Windows Server 2016 | ✅ Active |
| 192.168.20.22 | CASTELBLACK | SQL Server | north.sevenkingdoms.local | Windows Server 2019 | ✅ Active |
| 192.168.20.23 | BRAAVOS | SQL Server | essos.local | Windows Server 2016 | ✅ Active |

### **Domain-Struktur:**
```
🏰 sevenkingdoms.local (Root Forest)
├── 🏰 north.sevenkingdoms.local (Child Domain)
└── 🗡️ essos.local (Separate Forest - Trust Relationship)
```

---

## 🔑 Credential Harvesting

### **Kerberoasting Erfolge:**

| **Benutzer** | **Domain** | **SPN** | **Password** | **Status** |
|--------------|------------|---------|--------------|------------|
| **jon.snow** | north.sevenkingdoms.local | HTTP/thewall, CIFS/thewall | `iknownothing` | ✅ **GEKNACKT** |
| sansa.stark | north.sevenkingdoms.local | HTTP/eyrie | - | ❌ Nicht geknackt |
| sql_svc | north.sevenkingdoms.local | MSSQLSvc/castelblack:1433 | - | ❌ Nicht geknackt |

### **AS-REP Roasting Erfolge:**

| **Benutzer** | **Domain** | **Password** | **Status** |
|--------------|------------|--------------|------------|
| **brandon.stark** | north.sevenkingdoms.local | `iseedeadpeople` | ✅ **GEKNACKT** |

### **Zusätzliche Intelligence:**
- **samwell.tarly**: Password-Hinweis in Beschreibung: `"Heartsbane"`
- **hodor**: Kein Pre-Auth erforderlich (badpwdcount: 0)

---

## 🚪 Access Achievement

### **SMB Zugriff etabliert:**

| **System** | **Credentials** | **Verfügbare Shares** | **Berechtigungen** |
|------------|-----------------|----------------------|-------------------|
| **WINTERFELL** (192.168.20.11) | jon.snow:iknownothing | NETLOGON, SYSVOL | Domain User |
| **CASTELBLACK** (192.168.20.22) | jon.snow:iknownothing | all, public, ADMIN$ | Read/Write |
| **BRAAVOS** (192.168.20.23) | jon.snow:iknownothing | all, public, CertEnroll | Read/Write |

### **Interessante Findings:**
```bash
📁 Share-Analyse:
├── //192.168.20.22/all - "Basic RW share for all" ⚠️ 
├── //192.168.20.23/all - "Basic RW share for all" ⚠️
├── //192.168.20.23/CertEnroll - "AD Certificate Services share" 🎯
└── Entdeckte Dateien:
    ├── arya.txt (Persönliche Nachricht - Social Engineering Intel)
    ├── script.ps1 (PowerShell Script)
    └── secret.ps1 (Potenziell sensibles Script)
```

---

## 🛠️ Verwendete Tools & Techniken

### **Reconnaissance:**
- **Nmap** - Port-Scanning & Service-Detection
- **Naabu** - Schnelle Port-Discovery
- **Nuclei** - Vulnerability-Scanning (100+ CVEs gefunden)

### **Credential Attacks:**
- **GetUserSPNs.py** (Impacket) - Kerberoasting
- **GetNPUsers.py** (Impacket) - AS-REP Roasting  
- **John the Ripper** - Hash-Cracking
- **Hashcat** - Password-Recovery

### **Access & Enumeration:**
- **CrackMapExec** - SMB-Authentication & Domain-Enum
- **smbclient** - Share-Enumeration
- **ldapsearch** - LDAP-Queries

---

## 🎯 Nächste Schritte - Phase 3: Exploitation

### **Prioritäten für weitere Attacks:**

#### **🔥 Immediate Actions:**
1. **Lateral Movement:**
   ```bash
   # Nutze jon.snow Credentials für weitere Enumeration
   crackmapexec smb 192.168.20.0/24 -u jon.snow -p iknownothing --local-auth
   bloodhound-python -u jon.snow -p iknownothing -d north.sevenkingdoms.local -ns 192.168.20.11
   ```

2. **Privilege Escalation:**
   ```bash
   # Certificate Services Abuse (CertEnroll Share gefunden!)
   certipy find -u jon.snow -p iknownothing -dc-ip 192.168.20.23
   certipy req -u jon.snow -p iknownothing -target braavos.essos.local
   ```

3. **SQL Server Exploitation:**
   ```bash
   # SQL Service Account Testing
   mssqlclient.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.22
   # Teste sql_svc Account mit bekannten Schwachstellen
   ```

#### **🎯 Advanced Techniques:**

| **Technik** | **Tool** | **Ziel** | **Erwarteter Erfolg** |
|-------------|----------|-----------|----------------------|
| **BloodHound** | bloodhound-python | Attack Path Discovery | 🔥 Hoch |
| **Certificate Attacks** | Certipy | AD CS Abuse | 🔥 Hoch |
| **DCSync** | secretsdump.py | Domain Admin | 🎯 Möglich |
| **Golden Ticket** | ticketer.py | Persistence | 🎯 Möglich |
| **SQL Injection** | sqlmap | Database Access | 🔥 Hoch |

---

## ⚠️ Kritische Schwachstellen

### **High/Critical CVEs identifiziert:**
- **CVE-2021-44228** (Log4Shell) - CRITICAL
- **CVE-2015-9323** - CRITICAL  
- **CVE-2016-10033** - CRITICAL
- **CVE-2019-19781** (Citrix) - CRITICAL
- **100+ weitere High/Critical CVEs**

### **Misconfigurations:**
- ❌ **Anonymous LDAP Bind** möglich
- ❌ **SMB Signing nicht erforderlich** (BRAAVOS)
- ❌ **Schwache Service Account Passwords**
- ❌ **Offene File Shares** mit sensiblen Daten

---

## 📊 Tool-Empfehlungen für Phase 3

### **Must-Have Tools:**

```bash
# Domain Enumeration & Attack Path Discovery
bloodhound-python -c all -u jon.snow -p iknownothing -d north.sevenkingdoms.local -ns 192.168.20.11

# Certificate Services Attacks  
certipy find -u jon.snow -p iknownothing -dc-ip 192.168.20.23
certipy req -username jon.snow -password iknownothing -ca braavos-ca -template User

# Credential Dumping
secretsdump.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11

# SQL Server Exploitation
mssqlclient.py -windows-auth north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.22

# PowerShell Execution
evil-winrm -i 192.168.20.22 -u jon.snow -p iknownothing

# Kerberos Attacks
getTGT.py -dc-ip 192.168.20.11 north.sevenkingdoms.local/jon.snow:iknownothing
```

---

## 🔒 Defensive Recommendations

### **Immediate Fixes:**
1. **Deaktiviere Kerberos Pre-Authentication** für brandon.stark
2. **Ändere schwache Passwords** (jon.snow, brandon.stark)
3. **Konfiguriere SMB Signing** als required
4. **Beschränke Share-Berechtigungen** (/all, /public)
5. **Patche kritische CVEs** (Log4Shell, etc.)

### **Long-term Security:**
- Implementiere **Privileged Access Management (PAM)**
- **Honey Accounts** für Attack Detection
- **Advanced Threat Protection** für Kerberoasting-Detection
- **Certificate Template** Hardening

---

## 📈 Success Metrics

| **Metrik** | **Erreicht** | **Gesamt** | **Erfolgsrate** |
|------------|--------------|------------|-----------------|
| **Hosts identifiziert** | 6 | 6 | 100% ✅ |
| **Credentials geknackt** | 2 | ~15 | 13% 🎯 |
| **SMB Access** | 3 | 5 | 60% ✅ |
| **Domain Enum** | 3 | 3 | 100% ✅ |
| **Critical CVEs** | 100+ | - | ✅ |

---

## 🏁 Fazit

Phase 2 war **äußerst erfolgreich**. Die **Kerberoasting** und **AS-REP Roasting** Angriffe haben zu **validen Credentials** geführt, die **lateral movement** in **3 kritische Systeme** ermöglichten. 

**Die nächste Phase sollte sich auf Certificate Services Attacks, SQL Server Exploitation und BloodHound-basierte Attack Path Discovery konzentrieren.**

---

> **⚡ Next Phase Target:** Domain Admin Privileges via Certificate Template Abuse oder SQL Server Service Account Compromise

**Prepared by:** Timi - IT Security Expert & Penetration Tester  
**Classification:** CONFIDENTIAL - Internal Use Only