
**Business Impact Analyse (BIA) für einen Online-Passwortmanager**

**Szenario:**

Ihr Unternehmen bietet einen Online-Passwortmanager an, der es Benutzern ermöglicht, ihre Passwörter sicher zu speichern und zu verwalten.

**Ressourcen:**

- **Produktionslabor:** Betrieb der Server und Infrastruktur für den Passwortmanager.
- **Entwicklungslabor:** Arbeitsort der Entwickler zur Verbesserung und Erweiterung des Passwortmanagers.
- **Heimlabor des Chefentwicklers:** Heimarbeitsplatz des Chefentwicklers mit Zugriff auf Entwicklungsressourcen.

**Anforderungen:**

- Alle Entwickler müssen von zu Hause aus arbeiten können.
- Der Passwortmanager muss ständig verfügbar sein.
- Die Sicherheit der Benutzerdaten muss gewährleistet sein.
---
**Ziele der BIA:**

- **Identifizierung kritischer Geschäftsprozesse:** Welche Prozesse sind unerlässlich für den Betrieb des Passwortmanagers?

- **Bewertung der Auswirkungen von Ausfällen:** Welche Schäden entstehen durch Ausfälle kritischer Prozesse?

- **Festlegung von Wiederherstellungszeiten (RTO) und -punkten (RPO):** Wie lange dürfen Ausfälle dauern und wie viel Datenverlust ist akzeptabel?

- **Priorisierung von Ressourcen und Sicherheitsmaßnahmen:** Welche Ressourcen und Massnahmen sind am wichtigsten?

---

**Anwendung der BIA auf den Online-Passwortmanager:**

**1. Identifizierung kritischer Geschäftsprozesse:**

- **Bereitstellung des Passwortmanagers (Kernfunktion):** Ständiger Zugriff der Benutzer zum Generieren, Speichern, Abrufen und Verwalten von Passwörtern.

- **Authentifizierung der Benutzer:** Sichere und zuverlässige Benutzeranmeldung für den Passwortzugriff. Auch 2.Faktor möglich !

- **Verschlüsselung und sichere Speicherung der Passwörter:** Maximaler Schutz und Vertraulichkeit der Benutzerpasswörter.

- **Entwicklung und Wartung des Passwortmanagers:** Kontinuierliche Weiterentwicklung, Aktualisierung und Wartung zur Gewährleistung von Sicherheit und Funktionalität. mögliche Backdoors schließen und Bucks beheben !

- **Kundensupport (ggf. kritisch (Auslegungssache) ):** Unterstützung der Benutzer bei Problemen und Aufrechterhaltung des Vertrauens.

---

**2. Bewertung der Auswirkungen von Ausfällen (Impact Analyse):**

| Geschäftsprozess                           | Ausfall-Szenario                                 | Auswirkungen                                                                                                                                                                                                                                                                                                                                                                  |
| :----------------------------------------- | :----------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bereitstellung Passwortmanager**         | Ausfall Produktionslabor (Server, Infrastruktur) | **Finanziell:** Umsatzverluste, SLA-Verletzungen. **Reputationsschaden:** Vertrauensverlust, negative Presse. **Operativ:** Benutzer können nicht auf Passwörter zugreifen. **Rechtlich:** Schadenersatzforderungen.                                                                                                                                                          |
| **Authentifizierung der Benutzer**         | Ausfall Authentifizierungssystem                 | **Finanziell:** Geringere direkte finanzielle Schäden. **Reputationsschaden:** Vertrauensverlust in die Sicherheit. **Operativ:** Benutzer können sich nicht einloggen. **Sicherheit:** Potenzielle Sicherheitslücke durch alternative Authentifizierung.                                                                                                                     |
| **Verschlüsselung/Speicherung Passwörter** | Kompromittierung/Datenverlust Passwortdatenbank  | **Finanziell:** Sehr hohe Schäden durch Bussgelder (DSGVO), Schadenersatz, Imageverlust. **Reputationsschaden:** Katastrophaler Vertrauensverlust. **Operativ:** Vollständiger Vertrauensverlust, ggf. Betriebsaufgabe. **Rechtlich:** Schwerwiegende Konsequenzen, Bussgelder, Strafverfolgung. **Sicherheit:** Maximaler Schaden für Benutzer, Offenlegung sensibler Daten. |
| **Entwicklung/Wartung Passwortmanager**    | Ausfall Entwicklungslabor (z.B. Ransomware)      | **Finanziell:** Verzögerung von Updates, neue Features. **Reputationsschaden:** Geringerer Reputationsschaden (wenn nicht öffentlich). **Operativ:** Verzögerung von Fehlerbehebungen, Sicherheitsupdates, Wettbewerbsnachteile. **Sicherheit:** Erhöhtes Risiko durch fehlende Sicherheitsupdates.                                                                           |
| **Kundensupport**                          | Ausfall Kundensupport-Systeme                    | **Finanziell:** Geringere direkte finanzielle Schäden. **Reputationsschaden:** Verschlechterung Kundenservice, negative Bewertungen. **Operativ:** Erhöhte Belastung verbleibenden Personals, längere Reaktionszeiten. **Sicherheit:** Indirektes Sicherheitsrisiko durch unsichere Praktiken der Benutzer aufgrund fehlenden Supports.                                       |



**Bewertung der Ressourcen in hin zu Ziehung  der BIA:**

- **Produktionslabor:** **Extrem kritisch.** Ausfall bedeutet Ausfall des Kerngeschäfts. Höchste Priorität für Schutz und Wiederherstellung.

- **Entwicklungslabor:** **Kritisch, aber weniger zeitkritisch.** Ausfall behindert Entwicklung. Hohe Priorität für Schutz und Wiederherstellung, aber etwas längere Wiederherstellungszeiten akzeptabel.

- **Heimlabor Chefentwickler:** **Weniger kritisch.** Ausfall behindert Arbeit des Chefentwicklers. Mittlere Priorität für Schutz und Wiederherstellung. 
  Relevanz durch die Anforderung der Heimarbeit.

**CIA-Triade und IT-Grundschutz:**

- **CIA-Triade (Vertraulichkeit, Integrität, Verfügbarkeit):** Alle drei Säulen sind **extrem wichtig** für einen Passwortmanager. Die BIA hilft zu priorisieren, wo diese Schutzziele am wichtigsten sind.

- **IT-Grundschutz-Kompendium:** Bietet einen umfassenden Katalog an Sicherheitsmaßnahmen, die **auf kritische Infrastrukturen zugeschnitten** sind. 

- Die BIA liefert die **Grundlage, um den IT-Grundschutz zielgerichtet anzuwenden.**

**3. Festlegung von Wiederherstellungszeiten (RTO) und -punkten (RPO):**
[[RTO - Recovery Time Objective]] in der Vault unter Rechtliches 

|Geschäftsprozess|Maximale Ausfallzeit (RTO)|Maximaler Datenverlust (RPO)|Begründung|
|:--|:--|:--|:--|
|**Bereitstellung Passwortmanager**|< 4 Stunden (Ideal < 1h)|< 1 Stunde|Geschäftskritischste Funktion. Erhebliche finanzielle und reputative Schäden bei längeren Ausfällen. Minimaler Datenverlust zur Datenkonsistenz.|
|**Authentifizierung der Benutzer**|< 8 Stunden|< 1 Stunde|Kritisch für Nutzung, aber kurzfristig tolerierbar. Minimaler Datenverlust im Authentifizierungssystem.|
|**Verschlüsselung/Speicherung Passwörter**|< 24 Stunden (Notfall)|< 1 Stunde (Ideal 0)|Extremer Notfall. Schnellstmögliche Wiederherstellung, um weiteren Schaden zu minimieren. Datenverlust inakzeptabel (Ideal RPO = 0).|
|**Entwicklung/Wartung Passwortmanager**|< 3 Tage|< 24 Stunden|Wichtige Funktion, aber weniger zeitkritisch für unmittelbaren Betrieb. Längere Ausfälle behindern langfristige Entwicklung.|
|**Kundensupport**|< 2 Tage|< 24 Stunden|Kundenbetreuung wichtig, aber weniger kritisch als Kernfunktionen. Temporär eingeschränkter Support tolerierbar.|



**4. Priorisierung von Ressourcen und Sicherheitsmaßnahmen:**

- **Höchste Priorität:** Schutz und Hochverfügbarkeit des **Produktionslabors** und der **Passwortdatenbank**. Umfassende Sicherheitsmaßnahmen nach IT-Grundschutz, Redundanz, Notfallwiederherstellungspläne, regelmässige Backups (RPO beachten!).

- **Hohe Priorität:** Schutz und Wiederherstellung des **Entwicklungslabors**. Sicherheitsmaßnahmen nach IT-Grundschutz, weniger aufwendige Redundanz als im Produktionslabor. Fokus auf Integrität und Verfügbarkeit der Entwicklungsumgebung.

- **Mittlere Priorität:** Sicherer Arbeitsplatz des **Chefentwicklers im Heimlabor**. Grundlegende Sicherheitsmaßnahmen nach IT-Grundschutz für Homeoffice. Fokus auf Vertraulichkeit und Integrität der Entwicklungsdaten.

- **Kundensupport:** Angemessene Sicherheitsmaßnahmen und Wiederherstellungspläne. Geringere Priorität als Kernfunktionen.

---

**Checkliste zur Durchführung der BIA für den Online-Passwortmanager:**

**Vorbereitung und Planung:**

- [ ] BIA-Team zusammenstellen (IT, Geschäftsleitung, Fachabteilungen).
- [ ] Umfang und Ziele der BIA definieren (Fokus auf kritische Prozesse des Passwortmanagers).
- [ ] Zeitplan und Ressourcen festlegen.
- [ ] Dokumentationsvorlagen erstellen.

**Identifizierung kritischer Geschäftsprozesse:**

- [ ] Liste aller relevanten Geschäftsprozesse erstellen (Bereitstellung, Authentifizierung, etc.).
- [ ] Kritische Geschäftsprozesse identifizieren (Priorisierung nach Wichtigkeit). **(Hinweis: Fokus auf Verfügbarkeit und Sicherheit)**.
- [ ] Prozesseigner benennen.
- [ ] Abhängigkeiten zwischen Prozessen dokumentieren.

**Impact Analyse (Bewertung der Auswirkungen):**

- [ ] Ausfall-Szenarien für jeden kritischen Prozess definieren.
- [ ] Auswirkungen in Schadenskategorien bewerten:
    - [ ] Finanzielle Auswirkungen
    - [ ] Reputationsschaden
    - [ ] Operative Auswirkungen
    - [ ] Rechtliche Auswirkungen
    - [ ] **Sicherheitsauswirkungen (CIA-Triade bewerten)**
- [ ] Ressourcen für jeden kritischen Prozess identifizieren. **(Hinweis: Ressourcenliste aus Aufgabenstellung nutzen)**.
- [ ] Kritische Ressourcen für jeden Prozess bewerten.
- [ ] Abhängigkeiten zwischen Prozessen und Ressourcen dokumentieren.

**Festlegung von RTOs und RPOs:**

- [ ] Maximale Ausfallzeit (RTO) für jeden kritischen Prozess festlegen. **(Hinweis: Verfügbarkeitsanforderung beachten!)**.
- [ ] Maximal akzeptablen Datenverlust (RPO) für jeden kritischen Prozess festlegen. **(Hinweis: Sicherheitsanforderung beachten!)**.
- [ ] RTOs und RPOs mit Prozesseignern abstimmen und dokumentieren.
- [ ] Begründungen für RTOs und RPOs dokumentieren.

**Ergebnisse und Maßnahmen:**

- [ ] BIA-Bericht erstellen (kritische Prozesse, Auswirkungen, RTOs, RPOs, Ressourcen).
- [ ] Ergebnisse mit Management und Stakeholdern besprechen.
- [ ] **BIA-Ergebnisse nutzen, um Sicherheitsmaßnahmen zu priorisieren (IT-Grundschutz Kompendium!).**
- [ ] **Wiederherstellungsstrategien und Notfallpläne entwickeln oder überprüfen (basierend auf RTOs und RPOs).**
- [ ] BIA-Dokumentation regelmässig überprüfen und aktualisieren (jährlich oder bei Änderungen).


---


## IT-Grundschutz-Bausteine 


**Zweck der Bausteine:**

- **Strukturierung:** Komplexe IT-Landschaften werden in verständlicheren kleinere  Einheiten aufgeteilt.

- **Verknüpfung mit Sicherheitsanforderungen:** Jeder Baustein ist mit einem Katalog spezifischer Sicherheitsanforderungen verknüpft.

- **Wiederverwendbarkeit:** Bausteine können mehrfach verwendet werden.

- **Standardisierung und Best Practices:** Basieren auf Best Practices und dem aktuellen Stand der Technik.

**Kategorisierung in Prozess- und System-Bausteine (mit Beispielen [[IT-Grundschutz -Bausteine Übersicht und Download]] Vault unter Rechtliches ) :**

**1. Prozess-Bausteine (Prozess-Schichten):**

Prozess-Bausteine fokussieren auf **organisatorische und prozessuale Aspekte** der Informationssicherheit.

- **ORP (Organisatorische Prozesse):** Allgemeine organisatorische Sicherheitsmassnahmen und Rahmenbedingungen.
    - **Beispiel: ORP.1 "Sicherheitsmanagement"**: Organisatorische Verankerung der IT-Sicherheit, Verantwortlichkeiten, Sicherheitsrichtlinien.
    - **Beispiel: ORP.4 "Vertragsbeziehungen"**: Sicherheitsaspekte in Vertragsverhältnissen mit externen Dienstleistern.
    - **Beispiel: ORP.7 "Notfallmanagement"**: Planung, Vorbereitung und Durchführung des Notfallmanagements.
    
- **CON (Compliance und Revision):** Compliance-Anforderungen, Revision und Überprüfung der Sicherheitsmassnahmen.
    - **Beispiel: CON.1 "Compliance-Management"**: Umsetzung von Compliance-Anforderungen in der Organisation.
    - **Beispiel: CON.3 "Revision"**: Regelmässige Überprüfung der Wirksamkeit der Sicherheitsmassnahmen.
    
- **OPS (Operative Prozesse):** Operative Sicherheitsprozesse im täglichen IT-Betrieb.
    - **Beispiel: OPS.1 "Basis-Sicherheitsmaßnahmen"**: Grundlegende operative Sicherheitsmassnahmen (Datensicherung, Patch-Management, Berechtigungsmanagement).
    - **Beispiel: OPS.2 "Benutzerbetrieb"**: Sichere Durchführung des Benutzerbetriebs und sicherer Umgang der Benutzer mit IT-Systemen.
    - **Beispiel: OPS.3 "Incident Management"**: Prozess zum Umgang mit Sicherheitsvorfällen (Incidents).

**2. System-Bausteine (System-Schichten):**

System-Bausteine fokussieren auf **technische IT-Systeme und Komponenten**.

- **APF (Anwendungsplattformen):** Grundlegende Software-Plattformen.
    - **Beispiel: APF.1 "Betriebssysteme"**: Sichere Konfiguration und Betrieb von Betriebssystemen.
    - **Beispiel: APF.2 "Datenbanken"**: Sichere Konfiguration und Betrieb von Datenbankmanagementsystemen.
    - **Beispiel: APF.4 "Virtualisierung"**: Sicherheitsaspekte beim Einsatz von Virtualisierungstechnologien.

- **SYS (Systeme):** Generische IT-Systeme und Geräte.
    - **Beispiel: SYS.1 "Server-Systeme"**: Sicherheit von Servern im Allgemeinen (Webserver, Datenbankserver, etc.).
    - **Beispiel: SYS.2 "Client-Systeme"**: Sicherheit von Client-Arbeitsplatzrechnern (Desktop-PCs, Laptops).
    - **Beispiel: SYS.5 "Mobile Geräte" (DER.MOBI)**: Sicherheit von mobilen Endgeräten wie Smartphones und Tablets.

- **IND (Industrielle IT):** Spezielle IT-Systeme im industriellen Umfeld (OT - Operational Technology).
    - **Beispiel: IND.1 "Leittechnik-Systeme"**: Sicherheit von Leittechniksystemen (z.B. SCADA, SPS) in Produktionsumgebungen.
    - **Beispiel: IND.3 "Industrielle Kommunikationsnetze"**: Sicherheit von Netzwerken in industriellen Umgebungen.

- **NET (Netze):** Netzwerkinfrastruktur und Kommunikationswege.
    - **Beispiel: NET.1 "Lokale Netze (LAN)"**: Sicherheit von lokalen Netzwerken.
    - **Beispiel: NET.2 "Weitverkehrsnetze (WAN)"**: Sicherheit von Weitverkehrsnetzen (z.B. Internetanbindung, VPN-Verbindungen).
    - **Beispiel: NET.3 "Drahtlose Netze (WLAN)"**: Sicherheit von drahtlosen Netzwerken (WLAN).

- **INF (Infrastruktur):** Physische IT-Infrastruktur und deren Umgebung.
    - **Beispiel: INF.1 "Serverraum"**: Physische Sicherheit von Serverräumen und Rechenzentren.
    - **Beispiel: INF.2 "Gebäude"**: Allgemeine Sicherheitsmassnahmen für Gebäude, in denen IT-Systeme betrieben werden.

- **DER (Geräte):** Endgeräte und spezielle Geräteklassen.
    - **Beispiel: DER.1 "Arbeitsplatzrechner"**: Desktop-PCs und Laptops am Arbeitsplatz.
    - **Beispiel: DER.2 "Peripheriegeräte"**: Sicherheit von Peripheriegeräten wie Drucker, Scanner, USB-Sticks.
    - **Beispiel: DER.MOBI "Mobile Geräte"**: (Siehe auch SYS.5 Mobile Geräte) – Sicherheit von Smartphones, Tablets etc.

---
### Ergänzungen Erklärungen 

---
SLA (Service Level Agreement)  =**Dienstgütevereinbarung**, ist ein **vertraglicher Bestandteil** zwischen einem **Dienstleister** (Service Provider) und einem **Kunden** (Service Consumer). Es definiert **messbare Kennzahlen (Service Levels)**, welche die **Qualität und Verfügbarkeit** der vom Dienstleister erbrachten Services beschreiben 

RTO und RPO = Die Festlegung von Ausfallzeiten, insbesondere die **Festlegung von Wiederherstellungszeiten (RTO)** und 
**Wiederherstellungspunkten (RPO)**, ist ein kritischer Bestandteil der Planung für Geschäftskontinuität und Disaster Recovery. Diese Werte bestimmen, wie schnell und wie umfassend Ihr Unternehmen nach einer Störung den Betrieb wieder aufnehmen muss.

Disaster Recovery = **Disaster Recovery (DR),  "Notfallwiederherstellung",** bezeichnet den **Prozess der Planung, Vorbereitung und Durchführung von Maßnahmen, um die IT-Infrastruktur und kritischen Geschäftsprozesse eines Unternehmens im Falle eines katastrophalen Ereignisses wiederherzustellen und fortzuführen.** Das Ziel von Disaster Recovery ist es, die **Ausfallzeit (Downtime) so gering wie möglich zu halten und Datenverlust zu minimieren**, um die Geschäftskontinuität zu gewährleisten.

