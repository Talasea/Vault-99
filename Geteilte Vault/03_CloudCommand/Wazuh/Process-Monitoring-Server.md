---
created: 2025-01-22T09:49
updated: 2025-01-22T09:57
---
In Datei `/var/ossec/etc/rules/local_rules.xml`

```xml
<group name="malware_detection,">
  <rule id="100012" level="0">
    <if_sid>530</if_sid>
    <match>^ossec: output: 'ps -auxw'</match>
    <description>Running processes</description>
  </rule>

  <rule id="100013" level="12">
    <if_sid>100012</if_sid>
    <match>malware</match>
    <description>Malware detected</description>
  </rule>
</group>
```