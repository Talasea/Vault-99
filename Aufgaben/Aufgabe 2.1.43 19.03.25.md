

**A. Standortauswahl und Gebäudeumgebung (basierend auf INF.1):**

- **A.1. Äußere Gefahren:**
    - **Abstand zu Risikobereichen:** Nicht in unmittelbarer Nähe zu hochfrequentierten Bereichen, Hauptverkehrsstraßen, bekannten Gefahrenquellen (z.B. Industrieanlagen mit Gefahrstofflagerung, Überschwemmungsgebiete, Einflugschneisen von Flughäfen).
    - **Natürliche Barrieren nutzen:** Wenn möglich, Platzierung abseits leicht zugänglicher Bereiche des Geländes (z.B. nicht direkt am Haupteingang).
    - **Einsehbarkeit:** Reduzierung der direkten Einsehbarkeit des potenziellen Serverraumbereichs von außen.
    - **Zufahrtskontrolle zum Gelände:** Überprüfung und gegebenenfalls Anpassung der Geländezufahrtskontrollen (Zäune, Tore, Wachdienst).

- **A.2. Gebäudeinfrastruktur:**
    - **Tragwerksicherheit:** Auswahl eines Gebäudebereichs mit solider Bausubstanz und Schutz vor äußeren Einwirkungen (z.B. Sturm, Erschütterungen).
    - **Anbindung an Versorgungsinfrastruktur:** Gute Anbindung an zuverlässige Stromversorgung (idealerweise mit Redundanz), Telekommunikationsleitungen und gegebenenfalls Kühlwasserversorgung.
    - **Löschwasserversorgung:** Nähe zu oder einfache Anbindung an die Löschwasserversorgung (Hydranten).

**B. Platzierung innerhalb des Gebäudes (basierend auf INF.1 & INF.2):**

- **B.1. Interne Lage:**
    - **Geschosslage:** Bevorzugt innenliegende Räume in mittleren oder oberen Geschossen (nicht im Erdgeschoss oder direkt unter dem Dach wegen Einbruchs- und Umweltrisiken).
    - **Abgeschiedenheit:** Platzierung in einem weniger frequentierten Bereich des Gebäudes, abseits von öffentlich zugänglichen Zonen (z.B. Besucherbereiche, Kantinen).
    - **Pufferzonen:** Möglichkeit zur Schaffung von vorgelagerten Sicherheitsbereichen/Schleusen vor dem eigentlichen Serverraum.
    - **Fluchtwege:** Sicherstellung, dass die Platzierung die Hauptfluchtwege nicht behindert, aber auch keine direkten Fluchtwege durch den Serverraum führen.

- **B.2. Räumliche Anforderungen:**
    - **Ausreichende Größe:** Planung für aktuelle und zukünftige Anforderungen an IT-Systeme und deren Peripherie (Kühlung, Stromversorgung).
    - **Bodenbelastung:** Berücksichtigung der hohen Last durch Serverschränke und Klimaanlagen.
    - **Raumhöhe:** Ausreichende Höhe für die Installation und Wartung der Geräte sowie für die Luftzirkulation der Klimaanlagen.

**C. Schutzmaßnahmen des Serverraums (basierend auf INF.1 & INF.2):**

- **C.1. Physische Sicherheit (Außenhülle des Raumes):**
    - **Wände, Decke, Boden:** Robuste Bauweise (Massivbau), gegebenenfalls mit erhöhter Widerstandsfähigkeit gegen Durchbruch und Feuer.
    - **Türen:** Sicherheitstüren mit Mehrfachverriegelung und Einbruchschutz (entsprechend VdS oder EN-Normen). Installation von Zutrittskontrollsystemen (z.B. Chipkarte, Biometrie).
    - **Fenster:** Vermeidung von Fenstern. Falls unvermeidbar, einbruchhemmende Verglasung und gegebenenfalls zusätzliche Schutzmaßnahmen (z.B. Gitter).
    - **Kabeleinführungen:** Sichere und abgedichtete Durchführung von Kabeln und Leitungen, um unbefugten Zutritt zu verhindern und Brandschutz zu gewährleisten.

- **C.2. Zutrittskontrolle (INF.2):**
    - **Mehrfaktor-Authentifizierung:** Einsatz von mindestens zwei verschiedenen Authentifizierungsmerkmalen für den Zutritt.
    - **Protokollierung:** Lückenlose Aufzeichnung aller Zutritte und Zutrittsversuche.
    - **Berechtigungskonzept:** Klare Zuweisung von Zutrittsberechtigungen nach dem Prinzip der minimalen Rechte.
    - **Überwachung:** Installation von Überwachungskameras im Vorbereich und gegebenenfalls im Serverraum (unter Beachtung des Datenschutzes).

- **C.3. Umweltschutz (INF.2):**
    - **Klimatisierung:** Redundante und präzise Klimatisierung zur Aufrechterhaltung der optimalen Temperatur und Luftfeuchtigkeit.
    - **Brandmeldeanlage:** Frühzeitige Erkennung von Bränden durch automatische Rauch- und/oder Brandmelder, Aufschaltung auf eine Leitstelle.
    - **Brandbekämpfung:** Installation einer automatischen Brandlöschanlage (z.B. Gaslöschanlage, die für IT-Geräte unschädlich ist) und/oder Bereitstellung geeigneter Handfeuerlöscher.
    - **Wasserschadensprävention:** Maßnahmen zur Vermeidung von Wasserschäden (z.B. keine Wasserleitungen über dem Serverraum, Leckageerkennungssysteme).
    - **Staubschutz:** Maßnahmen zur Reduzierung von Staubentwicklung und Eindringen von Staub.

- **C.4. Stromversorgung (INF.2):**
    - **Unterbrechungsfreie Stromversorgung (USV):** Redundante USV-Anlagen zur Überbrückung von Stromausfällen.
    - **Notstromaggregat:** Installation eines Notstromaggregats für längere Stromausfälle.
    - **Getrennte Stromkreise:** Aufteilung der Stromversorgung auf separate, abgesicherte Kreise.
    - **Überspannungsschutz:** Installation von Überspannungsschutzmaßnahmen.

- **C.5. Überwachung und Alarmierung (INF.2):**
    - **Monitoring-System:** Kontinuierliche Überwachung relevanter Parameter (Temperatur, Luftfeuchtigkeit, Stromversorgung, Zutritt, Einbruch, Brand).
    - **Alarmierungskonzept:** Definition von Eskalationsstufen und Benachrichtigungsprozessen im Falle von Störungen oder Sicherheitsvorfällen.




----
-----



**Standortauswahl & Sicherheit Serverraum**

**A. Standortauswahl & Gebäudeumgebung**  
├── 🌍 _Äußere Gefahren_  
│ ├── Abstand zu Risikobereichen  
│ ├── Nutzung natürlicher Barrieren  
│ ├── Reduzierte Einsehbarkeit  
│ ├── Zufahrtskontrolle zum Gelände  
│  
├── 🏢 _Gebäudeinfrastruktur_  
│ ├── Tragwerksicherheit  
│ ├── Anbindung an Strom & Telekommunikation  
│ ├── Löschwasserversorgung

**B. Platzierung innerhalb des Gebäudes**  
├── 🏗 _Interne Lage_  
│ ├── Mittlere oder obere Geschosse  
│ ├── Abgeschiedenheit & Pufferzonen  
│ ├── Keine Beeinträchtigung von Fluchtwegen  
│  
├── 📏 _Räumliche Anforderungen_  
│ ├── Ausreichende Größe & Tragfähigkeit  
│ ├── Raumhöhe & Luftzirkulation

**C. Schutzmaßnahmen des Serverraums**  
├── 🔐 _Physische Sicherheit_  
│ ├── Robuste Bauweise (Wände, Boden, Decke)  
│ ├── Sicherheitstüren & Zutrittskontrolle  
│ ├── Vermeidung von Fenstern / Schutzmaßnahmen  
│ ├── Sichere Kabeleinführungen  
│  
├── 🛑 _Zutrittskontrolle_  
│ ├── Mehrfaktor-Authentifizierung  
│ ├── Protokollierung & Berechtigungen  
│ ├── Überwachungskameras  
│  
├── 🌡 _Umweltschutz_  
│ ├── Klimatisierung & Luftfeuchtigkeit  
│ ├── Brandmelde- & Brandlöschanlage  
│ ├── Wasserschutz & Staubschutz  
│  
├── ⚡ _Stromversorgung_  
│ ├── USV & Notstromaggregat  
│ ├── Getrennte Stromkreise & Überspannungsschutz  
│  
├── 🚨 _Überwachung & Alarmierung_  
│ ├── Monitoring-System  
│ ├── Eskalationsstufen & Alarmierung



## Bürogrundriss mit Berücksichtigung der Anforderungen

## **Raumaufteilung**

1. **4 Einzelbüros**:
    
    - Größe: Jeweils ca. 10–15 m² pro Büro (entspricht den Mindestanforderungen der Arbeitsstättenverordnung).
        
    - Ausstattung: Schreibtisch, Bürostuhl, Aktenschrank, ergonomische Einrichtung gemäß INF.7.
        
    - Lage: Entlang der Fassade für Tageslichtzugang.
        
2. **2 WC-Räume (Männer und Frauen)**:
    
    - Größe: Jeweils ca. 6–8 m².
        
    - Ausstattung: Waschbecken, Toilette, Spiegel.
        
    - Lage: Zentral, nahe dem Aufenthaltsraum und Großraumbüro.
        
3. **Kaffeeküche**:
    
    - Größe: Ca. 10–12 m².
        
    - Ausstattung: Pantryküche mit Spüle, Kühlschrank, Mikrowelle und Kaffeemaschine.
        
    - Lage: Nähe des Aufenthaltsraums.
        
4. **Aufenthaltsraum**:
    
    - Größe: Ca. 20–25 m².
        
    - Ausstattung: Sitzgelegenheiten, Tisch, Möglichkeit zur Erholung.
        
    - Lage: Zentral gelegen für alle Mitarbeiter zugänglich.
        
5. **Großraumbüro mit 6 Arbeitsplätzen**:
    
    - Größe: Ca. 90–120 m² (15–20 m² pro Arbeitsplatz).
        
    - Ausstattung: Schreibtische, ergonomische Stühle, Trennwände zur Geräuschreduzierung.
        
    - Lage: Hauptbereich des Büros.
        
6. **Serverraum**:
    
    - Größe: Ca. 10–15 m².
        
    - Ausstattung: Klimatisierung, Zugangskontrolle gemäß INF.1 und INF.2.
        
    - Lage: Abseits der Hauptarbeitsbereiche.
        
7. **Überwachungsraum**:
    
    - Größe: Ca. 15–20 m².
        
    - Ausstattung: Monitore für Überwachungssysteme, gesicherter Zugang gemäß INF.1.
        
    - Lage: Nähe des Serverraums für technische Integration.
        

## **Berücksichtigung der BSI-Bausteine**

- **INF.1 Allgemeines Gebäude**:
    
    - Brandschutzmaßnahmen (z.B., Brandschott-Kataster).
        
    - Zutrittskontrollen für sensible Bereiche wie Serverraum und Überwachungsraum.
        
    - Optimale Stromversorgung und Verkabelung.
        
- **INF.2 Serverraum**:
    
    - Sicherstellung von Klimatisierung und Schutz vor unbefugtem Zutritt.
        
    - Verwendung von Sicherheitsmaßnahmen wie Alarmanlagen und Zugangskontrollen.
        

## **Zusätzliche Hinweise**

- Verkehrswege müssen mindestens 0,9 m breit sein (Fluchtweg) gemäß Arbeitsstättenverordnung.
    
- Ergonomische Gestaltung aller Arbeitsplätze gemäß INF.7.
    
- Räume sollten so angeordnet werden, dass Mitarbeiter kurze Wege zwischen den Bereichen haben.
    

## **Visualisierung**

Ein zentraler Flur verbindet alle Räume:

- Einzelbüros sind entlang der Außenfassade angeordnet.
    
- Großraumbüro liegt im Zentrum.
    
- Aufenthaltsraum und Kaffeeküche sind nebeneinander positioniert.
    
- Serverraum und Überwachungsraum befinden sich in einem separaten Bereich mit gesichertem Zugang.


[[de4d640e096c8e8d9bfcffc1fa756771_MD5.jpeg|Open: Pasted image 20250319142115.png]]
![[de4d640e096c8e8d9bfcffc1fa756771_MD5.jpeg]]



[[7de3694c46f82026270d2476b38254ee_MD5.jpeg|Open: Pasted image 20250319142925.png]]
![[7de3694c46f82026270d2476b38254ee_MD5.jpeg]]