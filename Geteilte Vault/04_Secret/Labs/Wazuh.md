---
created: 2024-09-02T19:28
updated: 2025-01-13T13:17
---
# Überblick
 `Wazuh` ist ein _Open Source SIEM_, das einen ähnlichen Funktionsumfang wie kommerzielle Softwarelösungen bereitstellt.
 
## Wunschliste
* [ ] Detektieren einer SQLi in `GET` request zu `apache` Server ([Docs](https://documentation.wazuh.com/current/proof-of-concept-guide/detect-web-attack-sql-injection.html))
* [ ] Malware Detection mithilfe von `YARA` ([Docs](https://documentation.wazuh.com/current/proof-of-concept-guide/detect-malware-yara-integration.html))
* [ ] Einen bestimmten Inhalt in einer Datei detektieren ([Docs](https://documentation.wazuh.com/current/user-manual/capabilities/sec-config-assessment/use-cases.html#detecting-keyword-in-a-file))
* [ ] Überwachung von Änderungen in Windows Registry ([Docs](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/windows-registry-monitoring.html))
* [ ] Signed Binary Proxy Execution ([Docs](https://documentation.wazuh.com/current/user-manual/manager/event-logging.html#use-case-detecting-signed-binary-proxy-execution))
 
# Anwendungsfälle
## Endpoint Security
* File Integrity Monitoring in Kombination mit Regeln für Malware Detection z.B. mit `YARA`
* Rootkit Detection ([Docs](https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/rootkits-behavior-detection.html))
## Threat Intelligence
* Vulnerability Detection
* Alarme gruppiert auf Basis von MITRE ATT&CK
* Integration mit VirusTotal
## Cloud Security 
* Integration mit dre GitHub-Audit API um Änderungen der Berechtigungen von Repositories zu detektieren
* Integration mit Azure, AWS und Google Cloud
* Überwachung von Docker Containern
## Compliance mit bestehenden Standards
* DSGVO/GDPR
* PCI DSS
* NIST 800-53, HIPAA, TSC

# Konfiguration 🦚
Der Server, sowie alle Agents haben **jeweils eine eigene** `ossec.conf` Datei

Linux Pfad: `/var/ossec/etc/ossec.conf`   
Windows Pfad: `/C:\Program Files (x86)\ossec-agent\ossec.conf`  

Konfigurationen müssen in **der korrekten** Konfigurationsdatei vorgenommen werden, entweder auf dem Server oder auf dem jeweiligen Agent, **abhängig von der Funktion**, die konfiguriert werden soll.

## Globale Konfiguration
Es kann auch eine **globale Konfigurationsdatei auf dem Server** verwendet werden.

Es muss dazu **auf dem Agent** in der Datei `/var/ossec/etc/local_internal_options.conf` folgende Zeile hinzugefügt werden:

```xml
wazuh_command.remote_commands=1
```

Alle Dateien der `default` Gruppe im Pfad `/var/ossec/etc/shared/default` werden in den Ordner `/var/ossec/etc/shared/` kopiert

## File Integrity Monitoring
Auf den Agents im `<syscheck>` Block der Konfigurationsdatei die zu überwachenden Dateien oder Ordner angeben

```xml
<syscheck>
   <directories><FILEPATH_OF_MONITORED_FILE></directories>
   <directories realtime="yes"><FILEPATH_OF_MONITORED_DIRECTORY></directories>
</syscheck>
```

Neu starten: `systemctl restart wazuh-agent`

## Active Response 🍁
[Custom Scripts Docs](https://documentation.wazuh.com/current/user-manual/capabilities/active-response/custom-active-response-scripts.html)
###### Wann - `rules_id`, `rules_group` oder `level`   
* When a specific **level** of severity (ranging from 1 to 16) is crossed
* An event listed in a specified **rules_group** fires
* A specific rule specified by **rules_id** fires
###### Wo - `location`  
* `local` - runs the command on the agent that generated the event.
* `server` - runs the command on the Wazuh manager.
* `defined-agent` - runs the command on a specific agent identified by agent_id.
* `all` - runs the command on all agents, not including the manager. Use with caution.
###### Konfiguration auf Agent
Skripte in `/var/ossec/active-response/bin`
Permissions required: `750`
Ownership required: `root:wazuh`
Beispielskript in `Kioku/src/Code/Python/custom-ar.py`
Agent neustarten nicht vergessen
Auf Lineendings achten: `dos2unix` ausführen
###### Konfiguration auf Server
1. Mit einem `<command>` Block ein neues Kommando definieren

```xml
<command>
  <name>super-active-response</name>
  <executable>custom-ar.py</executable>
  <timeout_allowed>yes</timeout_allowed>
</command>
```

2. Add an `<active-response>` block (local indicates to run the script on the agent)

```xml
<active-response>
  <command>super-active-response</command>
  <location>local</location>
  <rules_id>503</rules_id> #wazuh agent started
  <timeout>600</timeout>
</active-response>
```

Service neu starten: `systemctl restart wazuh-manager`

## Protokollieren von Docker Events 🐬

Create a new Python virtual environment and install the following packages

```bash
pip3 install docker==7.1.0 urllib3==2.2.2 requests==2.32.2 
```

Change shebang in `/var/ossec/wodles/docker/DockerListener` to point to virtual env

Add the following to the `ossec.conf` on the **Wazuh Agent**

```xml
<ossec_config>
  <wodle name="docker-listener">
    <interval>10m</interval>
    <attempts>5</attempts>
    <run_on_start>yes</run_on_start>
    <disabled>no</disabled>
  </wodle>
</ossec_config>
```

## Malware Detection mit `YARA`

## Network Monitoring mit `Suricata`
Follow [the Docs](https://documentation.wazuh.com/current/proof-of-concept-guide/integrate-network-ids-suricata.html)
1. `Suricata` mit zusätzlichen Rules erweitern
2. Config Datei in `/etc/suricata/suricata.yaml` anpassen
3. Folgenden Block in die `ossec.conf` Datei einfügen 
```xml
<ossec_config>
  <localfile>
    <log_format>json</log_format>
    <location>/var/log/suricata/eve.json</location>
  </localfile>
</ossec_config>
```

Active Response für einen spezifischen `Suricata` Alert auslösen [hier](https://wazuh.com/blog/responding-to-network-attacks-with-suricata-and-wazuh-xdr/)

Add the following rules to the `/var/ossec/etc/rules/local_rules.xml` file:

```xml
<group name="custom_active_response_rules,">
  <rule id="100200" level="12">
    <if_sid>86600</if_sid>
    <field name="event_type">^alert$</field>
    <match>ET DOS Inbound GoldenEye DoS attack</match>
    <description>GoldenEye DoS attack has been detected. </description>
    <mitre>
      <id>T1498</id>
    </mitre>
  </rule>
  <rule id="100201" level="12">
    <if_sid>86600</if_sid>
    <field name="event_type">^alert$</field>
    <match>ET SCAN Nmap Scripting Engine User-Agent Detected (Nmap Scripting Engine)</match>
    <description>Nmap scripting engine detected. </description>
    <mitre>
      <id>T1595</id>
    </mitre>
  </rule>
</group>
```

Die neu definierten Rule IDs können nun in einem Active Response Block verwendet werden

```xml
<ossec_config>  
  <active-response>
    <command>firewall-drop</command>
    <location>local</location>
    <rules_id>100200, 100201</rules_id>
    <timeout>180</timeout>
  </active-response>
</ossec_config>
```