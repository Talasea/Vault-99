**1. Signaturbasierte Erkennung**

- **Vorteile:**
    
    - Sehr hohe Genauigkeit bei bekannten Bedrohungen.
        
    - Kaum Fehlalarme (False Positives), da nur exakte Übereinstimmungen gemeldet werden.
        
    - Geringer Ressourcenbedarf (CPU/Speicher), da der Abgleich einfach ist.
        
    - Einfach zu verstehen und zu implementieren.
        
- **Nachteile:**
    
    - Völlig wirkungslos gegen neue, unbekannte Angriffe (Zero-Day-Exploits).
        
    - Die Signatur-Datenbank muss permanent auf dem neuesten Stand sein, was Wartungsaufwand bedeutet.
        
    - Angreifer können ihre Malware leicht modifizieren, um der Erkennung zu entgehen.
        

---

**2. Anomaliebasierte Erkennung**

- **Vorteile:**
    
    - Kann neue und unbekannte Angriffe erkennen, die von signaturbasierten Systemen übersehen werden.
        
    - Proaktiver Ansatz, der das spezifische Netzwerk lernt und so maßgeschneiderte Bedrohungen aufspüren kann.
        
    - Kein Vorwissen über einen konkreten Angriffstyp notwendig.
        
- **Nachteile:**
    
    - Hohe Rate an Fehlalarmen (False Positives), da auch legitime, aber untypische Aktivitäten als Angriff gewertet werden können.
        
    - Benötigt eine Lernphase, um das "Normalverhalten" zu definieren; in dieser Zeit ist die Erkennung unzuverlässig.
        
    - "Normales" bösartiges Verhalten wird nicht erkannt, wenn es bereits während der Lernphase vorhanden war.
        

---

**3. Stateful-Protokollanalyse**

- **Vorteile:**
    
    - Erkennt komplexe Angriffe, die sich in den Feinheiten von Kommunikationsprotokollen verstecken.
        
    - Versteht den Kontext einer Verbindung und nicht nur isolierte Datenpakete.
        
    - Zuverlässiger als Signaturen bei der Erkennung von Protokoll-Manipulationen.
        
- **Nachteile:**
    
    - Sehr hoher Ressourcenbedarf durch das Verfolgen jeder einzelnen Verbindung (benötigt viel CPU und Arbeitsspeicher).
        
    - Hohe Komplexität in der Implementierung und Konfiguration.
        
    - Stößt bei durchgehend verschlüsseltem Verkehr an seine Grenzen, es sei denn, der Verkehr wird aktiv entschlüsselt.