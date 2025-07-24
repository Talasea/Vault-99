## **Dokumentation: Vorgehensweise eines Hackers**

## **1. Informationsbeschaffung (Reconnaissance)**

- **Ziel**: Sammeln von Informationen über das Zielsystem oder die Zielperson.
    
- **Methoden**:
    
    - **Offene Quellenanalyse (OSINT)**: Nutzung öffentlich zugänglicher Informationen wie Social-Media-Profile, Unternehmenswebsites oder Foren.
        
    - **Metadatenanalyse**: Extrahieren von Metadaten aus Dokumenten (z. B. PDF, Word) für Details wie Autor, Softwareversion oder Dateipfade[1](https://outpost24.com/blog/metadata-hackers-best-friend/).
        
    - **Netzwerkscans**: Tools wie _Nmap_, um offene Ports und Dienste zu identifizieren.
        

## **2. Schwachstellenanalyse**

- **Ziel**: Finden von Schwachstellen im System oder in der Infrastruktur.
    
- **Methoden**:
    
    - **Automatisierte Scans**: Nutzung von Tools wie Nessus oder OpenVAS.
        
    - **Manuelle Analyse**: Überprüfung auf bekannte Exploits, z. B. durch Nutzung der Exploit-Datenbank _Exploit-DB_.
        
    - **Analyse von Webanwendungen**: Identifikation von Schwachstellen wie SQL-Injections oder Cross-Site-Scripting (XSS)[
        

## **3. Angriffsplanung**

- **Ziel**: Erstellung eines detaillierten Plans basierend auf den gesammelten Informationen und Schwachstellen.
    
- **Beispiele für Angriffsvektoren**:
    
    - Phishing-Angriffe über E-Mails mit manipulierten Anhängen (z. B. Office-Dokumente mit eingebetteten Makros)
        
    - Brute-Force-Angriffe auf Login-Seiten mit Tools wie Hydra oder Burp Suite[
        
    - Social Engineering zur Manipulation von Zielpersonen
        

## **4. Angriffsdurchführung**

- **Ziel**: Ausnutzung der Schwachstellen, um Zugriff zu erhalten.
    
- **Techniken**:
    
    - **SQL-Injection**: Einschleusen von SQL-Befehlen in Webformulare, um Datenbanken auszulesen oder zu manipulieren
    - **Malware-Einsatz**: Verbreitung von Trojanern oder Ransomware über manipulierte Dateien oder Webseiten[
        
    - **Man-in-the-Middle-Angriffe (MitM)**: Abfangen und Manipulieren von Datenverkehr zwischen zwei Parteien
        
    - **DDoS-Angriffe**: Überlastung eines Systems durch massiven Datenverkehr
        

## **5. Zugriffserweiterung**

- **Ziel**: Vertiefung des Zugriffs und Sicherung der Kontrolle.
    
- **Methoden**:
    
    - Installation von Backdoors für späteren Zugriff.
        
    - Nutzung von Privilege Escalation, um Administratorrechte zu erlangen.
        

## **6. Spurenverwischung**

- **Ziel**: Verschleierung der Aktivitäten, um eine Entdeckung zu vermeiden.
    
- **Techniken**:
    
    - Löschen oder Manipulieren von Logdateien.
        
    - Nutzung verschlüsselter Kommunikationstools wie VPNs oder Tor.
        

## **Werkzeuge eines Hackers**

1. **Reconnaissance & Scanning**:
    
    - _Nmap_, _Shodan_, _Maltego_.
        
2. **Exploitation & Angriffe**:
    
    - _Metasploit_, _SQLmap_, _Burp Suite_.
        
3. **Passwort-Cracking**:
    
    - _Hydra_, _John the Ripper_, _Hashcat_.
        
4. **Malware-Erstellung**:
    
    - Erstellung manipulierter Office-Dokumente mit Tools wie Empire7.
        
5. **Spurenverwischung & Anonymität**:
    
    - Nutzung von Proxy-Chains, VPNs und Tor.
        

## Beispielangriff: Phishing mit manipulierten Office-Dokumenten

1. Erstellung eines Word-Dokuments mit eingebettetem bösartigem VBA-Code (Makro)7.
    
2. Versand des Dokuments per E-Mail mit einer überzeugenden Nachricht (z. B. gefälschte Rechnung oder Jobangebot).
    
3. Sobald das Opfer das Dokument öffnet und Makros aktiviert, wird der Code ausgeführt und eine Verbindung zum Angreifer hergestellt.





**Spezifische Aspekte für deine Beispiele:**

**1. Bypass einer KI:**

Hier ist es besonders wichtig, den Denkprozess und die angewandten Methoden detailliert zu dokumentieren, da KI-Systeme oft komplex und undurchsichtig sind.

- **Zielsetzung:** Definiere klar das Ziel des KI-Bypasses. Was soll erreicht werden (z.B. Umgehen einer bestimmten Sicherheitsfunktion, Hervorrufen einer Fehlfunktion, Erlangen unautorisierter Informationen)?
- **Hypothesen:** Welche Annahmen hast du getroffen, bevor du mit dem Test begonnen hast? Warum glaubst du, dass ein bestimmter Ansatz funktionieren könnte?
- **Methoden und Techniken:** Beschreibe detailliert die Methoden und Techniken, die du angewendet hast. Dazu gehören:
    - **Art der Interaktion:** Wie hast du mit der KI interagiert (z.B. über eine API, eine Benutzeroberfläche, direkte Eingaben)?
    - **Eingaben und Prompts:** Dokumentiere die spezifischen Eingaben, Prompts oder Daten, die du verwendet hast, um den Bypass zu versuchen.
    - **Tools und Skripte:** Falls du spezielle Tools oder Skripte verwendet hast, dokumentiere deren Namen, Versionen und ggf. Anpassungen.
- **Beobachtungen und Ergebnisse:** Notiere genau, was passiert ist, als du die verschiedenen Methoden angewendet hast. Dazu gehören:
    - **Antworten und Reaktionen der KI:** Welche Ausgaben hat die KI generiert? Wie hat sie auf deine Eingaben reagiert?
    - **Fehlermeldungen und Anomalien:** Gab es unerwartete Fehler oder Verhaltensweisen?
    - **Erfolgreiche Bypass-Schritte:** Wenn du einen Bypass erreicht hast, beschreibe genau, wie und warum er funktioniert hat.
- **Analyse:** Analysiere die Ergebnisse. Warum hat ein bestimmter Ansatz funktioniert oder nicht funktioniert? Welche Schwachstellen hast du identifiziert?
- **Reproduzierbarkeit:** Beschreibe, wie der Bypass reproduziert werden kann. Dies ist entscheidend, damit die Schwachstelle behoben werden kann.
- **Empfehlungen:** Gib konkrete Empfehlungen, wie die identifizierte Schwachstelle behoben und zukünftige Bypässe verhindert werden können.

**2. Eindringen in ein Netzwerk:**

Bei der Penetration eines Netzwerks ist eine strukturierte und umfassende Dokumentation essenziell, um den gesamten Prozess und die gefundenen Schwachstellen nachvollziehbar zu machen.

- **Auftrag und Scope:** Dokumentiere den genauen Auftrag und den Umfang (Scope) des Penetrationstests. Welche Systeme und Netzwerke dürfen getestet werden? Welche Ziele sollen erreicht werden?
- **Regeln des Engagements (Rules of Engagement):** Halte alle vereinbarten Regeln fest, z.B. Zeitfenster, erlaubte Techniken, Eskalationsverfahren.
- **Informationsbeschaffung (Reconnaissance):** Dokumentiere alle Schritte der Informationsbeschaffung, z.B.:
    - **Passive Reconnaissance:** Welche öffentlich zugänglichen Informationen wurden gesammelt (z.B. DNS-Einträge, Whois-Informationen)?
    - **Aktive Reconnaissance:** Welche Scans wurden durchgeführt (z.B. Portscans, Netzwerk-Scans)? Welche Informationen wurden dabei gewonnen?
- **Schwachstellenanalyse (Vulnerability Analysis):** Dokumentiere alle identifizierten Schwachstellen, einschließlich:
    - **Tools und Methoden:** Welche Tools und Methoden wurden zur Schwachstellenanalyse verwendet (z.B. Vulnerability Scanner)?
    - **CVE-Nummern:** Falls zutreffend, notiere die entsprechenden CVE-Nummern der gefundenen Schwachstellen.
    - **Bewertung der Schwachstellen:** Bewerte die Schwachstellen nach ihrem Risikopotenzial (z.B. kritisch, hoch, mittel, niedrig).
- **Exploitation:** Dokumentiere alle Versuche und erfolgreichen Exploits, einschließlich:
    - **Angewendete Exploits:** Welche Exploits wurden verwendet? Woher stammen sie?
    - **Erfolgreiche Zugriffe:** Auf welche Systeme oder Daten konnte zugegriffen werden?
    - **Beweismittel (Proof of Concept):** Erstelle Beweismittel, die den erfolgreichen Zugriff demonstrieren (z.B. Screenshots, Logdateien).
- **Post-Exploitation:** Dokumentiere alle Aktivitäten nach einem erfolgreichen Exploit, z.B.:
    - **Lateral Movement:** Wie wurde versucht, sich im Netzwerk weiterzubewegen?
    - **Privilege Escalation:** Wie wurde versucht, höhere Berechtigungen zu erlangen?
    - **Datenzugriff:** Auf welche Daten wurde zugegriffen oder kopiert?
- **Bereinigung (Cleanup):** Dokumentiere alle Schritte, die unternommen wurden, um das System nach dem Test in den ursprünglichen Zustand zurückzusetzen.
- **Ergebnisse und Fazit:** Fasse die wichtigsten Ergebnisse des Penetrationstests zusammen und ziehe ein Fazit.
- **Empfehlungen:** Gib detaillierte und priorisierte Empfehlungen zur Behebung der gefundenen Schwachstellen und zur Verbesserung der Netzwerksicherheit.

**Tools und Formate für die Dokumentation:**

- **Texteditoren:** Einfache Texteditoren (z.B. Notepad, TextEdit) für schnelle Notizen.
- **Word-Prozessoren:** Umfangreichere Dokumente können mit Word-Prozessoren (z.B. Microsoft Word, LibreOffice Writer) erstellt werden.
- **Markdown:** Ein leichtgewichtiger Auszeichnungsformat, das sich gut für technische Dokumentationen eignet.
- **Wiki-Systeme:** Für kollaborative Dokumentation und Wissensmanagement (z.B. MediaWiki, Confluence).
- **Spezialisierte Reporting-Tools:** Es gibt auch kommerzielle Tools, die speziell für die Erstellung von Penetrationstest-Berichten entwickelt wurden.
- **Screenshots und Screencasts:** Visuelle Beweismittel sind oft sehr hilfreich.
- **Diagramme:** Netzwerkdiagramme oder Flussdiagramme können komplexe Sachverhalte veranschaulichen.