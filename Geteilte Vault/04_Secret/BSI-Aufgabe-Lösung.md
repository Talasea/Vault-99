---
created: 2025-02-03T01:00:00
updated: 2025-02-05T17:17
---
Die folgenden Aufgaben beschreiben Szenarien, in denen konkrete technische Maßnahmen anhand der Richtlinien des BSI (z. B. IT-Grundschutz-Bausteine) umgesetzt werden müssen.
Ziel ist es, die BSI-Empfehlungen **praktisch** anzuwenden und so ein Verständnis dafür zu entwickeln, wie technische Maßnahmen und organisatorische Vorgaben ineinandergreifen.

[Link zu den BSI-Bausteinen](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/IT-Grundschutz-Bausteine/Bausteine_Download_Edition.html)

## 1. Datensicherung

**Frage:**

> Welche Intervalle für Datensicherungen und welche Anforderungen an die verwendeten Speichermedien empfiehlt das BSI? Wo genau finde ich diese Informationen?

**Lösungshinweis:** Im Baustein **CON.3 „Datensicherungskonzept“**, insbesondere in der Maßnahme **CON.3.M5 (Regelmäßige Datensicherung)**, wird beschrieben, wie oft Backups durchgeführt werden sollten, welche Medien geeignet sind und welche organisatorischen Vorgaben zu beachten sind.

---

## 2. Active Directory

**Frage:**

> Welche Empfehlungen gibt das BSI für den sicheren Betrieb von Active Directory (AD)? Welche Rollen und Funktionen müssen besonders geschützt werden, und wo steht das im IT-Grundschutz?

**Lösungshinweis:** Im Baustein **APP.2.1 „Verzeichnisdienste“** (je nach Kompendiums-Version ggf. anders bezeichnet) werden Maßnahmen zum Schutz von Domänencontrollern, zur Rollenverteilung sowie zur Härtung kritischer AD-Komponenten beschrieben. Hier finden sich auch Hinweise zur Rechteverwaltung.

---

## 3. Passwort-Richtlinien (allgemein)

**Frage:**

> Welche Anforderungen stellt das BSI an die Vergabe und Verwaltung von Passwörtern? Welche Mindestlänge, Komplexität und Wechselintervalle werden empfohlen und in welcher Maßnahme steht das?

**Lösungshinweis:** In den Bausteinen rund um **ORP.4 „Identitäts- und Berechtigungsmanagement“** (bzw. bei älteren Versionen in den Maßnahmen zu „Sichere Passwörter“) findest du detaillierte Vorgaben. Dort stehen Hinweise zur Länge, Komplexität, Lebensdauer und sicheren Verwaltung von Passwörtern.

---

## 4. Netzwerksegmentierung

**Frage:**

> Welche Empfehlungen gibt das BSI, um Netzwerke sinnvoll zu segmentieren und damit die Sicherheit zu erhöhen? In welchem Baustein und unter welchen Maßnahmen ist das geregelt?

**Lösungshinweis:** Detaillierte Informationen zur **Netzwerksegmentierung** und zum **Zonenkonzept** findest du im Baustein **NET.1 oder NET.2** des IT-Grundschutz-Kompendiums (je nach Version). Dort wird beschrieben, wie man DMZ, internes Netz oder andere Segmente strikt voneinander trennt.

---

## 5. Firewall-Konfiguration

**Frage:**

> Welche grundlegenden Sicherheitsanforderungen stellt das BSI an Firewalls und deren Konfiguration? Wo steht beschrieben, wie die Regeln für ein- und ausgehenden Traffic gestaltet sein sollten?

**Lösungshinweis:** Im Baustein **NET.2 „Netzverbindungs- und Vermittlungskomponenten“** (oder in älteren Katalogen in den Maßnahmen rund um Firewalls) beschreibt das BSI, wie man Sicherheitsrichtlinien, Logging und Regelwerke für Firewalls aufbaut und pflegt.

---

## 6. Protokollierung und Monitoring

**Frage:**

> Wie empfiehlt das BSI, Protokollierung (Logging) und Monitoring in einer IT-Infrastruktur zu implementieren, um Sicherheitsvorfälle frühzeitig zu erkennen? Welcher Baustein gibt dazu konkrete Hinweise?

**Lösungshinweis:** Im Baustein **OPS.1 „Betrieb von IT-Systemen“** und ggf. im Baustein **CON.5 „Protokollierung“** (je nach IT-Grundschutz-Version) wird beschrieben, wie man sicherheitsrelevante Ereignisse erfasst und auswertet, um Angriffe oder Unregelmäßigkeiten frühzeitig zu erkennen.

---

## 7. Schutz vor Schadsoftware

**Frage:**

> Welche Maßnahmen empfiehlt das BSI, um Schadsoftware (Viren, Trojaner, Ransomware etc.) effektiv abzuwehren? In welchem Baustein finden sich Hinweise zur Konfiguration von Antivirensoftware und anderen Schutzmechanismen?

**Lösungshinweis:** Das Thema **Schutz vor Schadsoftware** wird insbesondere im Baustein **OPS.1.2 „Schutz vor Schadprogrammen“** behandelt. Dort finden sich Anforderungen an Virenscanner, Updates, zentrale Verwaltung von Signaturen und zusätzliche Schutzmaßnahmen wie Sandboxing.

---
## 8. Passwortrichtlinie (konkret)

**Frage:**

> Welche BSI-Policy fordert eine Mindestpasswortlänge von 12 Zeichen, Komplexitätsanforderungen (Groß-/Kleinbuchstaben, Sonderzeichen) und eine maximale Gültigkeitsdauer von 6 Monaten? Nennen Sie den BSI-Baustein und die konkrete Maßnahme.

**Antwort (Beispielhafte Zuordnung):**

- **Baustein:** ORP.4 „Identitäts- und Berechtigungsmanagement“
- **Mögliche Maßnahme:** ORP.4.M5 _„Sichere Passwörter und Passwortrichtlinien“_ (Name bzw. Nummer kann je nach Kompendiums-Version abweichen)

Dort wird u. a. eine Passwortrichtlinie mit einer Mindestlänge (empfohlen mind. 12 Zeichen), Komplexitätsanforderungen und regelmäßigen Wechselintervallen beschrieben.

---

## 9. Account-Lockout-Richtlinie

**Frage:**

> Welche BSI-Maßnahme schützt vor Brute-Force-Angriffen durch Sperrung von Benutzerkonten nach 5 fehlgeschlagenen Anmeldeversuchen für 15 Minuten? Geben Sie die Maßnahmen-ID an.

**Antwort (Beispielhafte Zuordnung):**

- **Baustein:** ORP.4 „Identitäts- und Berechtigungsmanagement“
- **Mögliche Maßnahme:** ORP.4.M6 _„Account-Lockout und Sperrung nach Fehlversuchen“_

Hier werden Vorgaben formuliert, dass nach einer definierten Anzahl von Fehlversuchen (z. B. 5) das Konto für eine gewisse Zeit (z. B. 15 Minuten) gesperrt wird, um Brute-Force-Angriffe zu erschweren.

---

## 10. Überwachungsrichtlinie

**Frage:**

> Welche Policy des BSI verlangt die Protokollierung von Zugriffen auf kritische Ressourcen (z. B. Finanzdaten) und die Speicherung der Logs für mindestens 7 Tage? Nennen Sie den Baustein und die Maßnahme.

**Antwort (Beispielhafte Zuordnung):**

- **Baustein:** CON.5 „Protokollierung“ (oder in manchen Versionen OPS.1 / SYS.4)
- **Mögliche Maßnahme:** CON.5.M2 _„Protokollierung sicherheitsrelevanter Ereignisse“_

Darin wird erläutert, wie Zugriffe auf sensible Daten protokolliert werden müssen und wie lange diese Protokolle aufzubewahren sind (mindestens 7 Tage, in vielen Fällen jedoch deutlich länger).

---

## 11. Benutzerrechtezuweisung (Remotedesktop)

**Frage:**

> Welches BSI-Prinzip besagt, dass nur autorisierte Benutzer Remotedesktopzugriff erhalten sollen, um das Risiko von Missbrauch zu minimieren? Nennen Sie die Maßnahme und den zugehörigen Baustein.

**Antwort (Beispielhafte Zuordnung):**

- **Baustein:** ORP.4 „Identitäts- und Berechtigungsmanagement“
- **Mögliche Maßnahme:** ORP.4.M2 _„Vergabe von Berechtigungen nach dem Need-to-know- bzw. Least-Privilege-Prinzip“_

Das BSI betont hier das **Least-Privilege-Prinzip**: Nur diejenigen Benutzerkonten, die für ihre Aufgaben tatsächlich Remotezugriff benötigen, dürfen entsprechende Rechte erhalten.

---

## 12. Organisatorische Einheit (OU) Finanzen

**Frage:**

> Welche BSI-Maßnahme rechtfertigt die Trennung von Finanzdaten in einer separaten OU mit strengen Zugriffsbeschränkungen? Geben Sie den Baustein an, der die Isolierung kritischer Ressourcen beschreibt.

**Antwort (Beispielhafte Zuordnung):**

- **Baustein:** ORP.4 „Identitäts- und Berechtigungsmanagement“ (teilweise auch NET-Bausteine, wenn es um Netzwerksegmentierung geht)
- **Mögliche Maßnahme:** ORP.4.M9 _„Trennung sensibler Daten in separaten Bereichen/OU“_ (sinngemäß)

Es gilt das Prinzip der **Isolation kritischer Ressourcen**. Das BSI empfiehlt, besonders schützenswerte Daten (z. B. Finanzdaten) in separaten Organisationseinheiten (OUs) zu verwalten und den Zugriff streng zu kontrollieren.

---

## 13. Sicherheitsoptionen (Anmeldehinweise)

**Frage:**

> Welche BSI-Maßnahme empfiehlt die Anzeige eines rechtlichen Hinweistextes bei der Anmeldung am System, um unbefugte Zugriffe abzuschrecken? Nennen Sie die Maßnahme und den Baustein.

**Antwort (Beispielhafte Zuordnung):**

- **Baustein:** ORP.1 „Organisation“ oder auch ORP.4, je nach Kompendiumsversion
- **Mögliche Maßnahme:** ORP.1.M5 _„Warn- und Hinweisbanner bei der Anmeldung“_

Hier geht es darum, dem Benutzer bereits vor der Anmeldung anzuzeigen, dass es sich um ein geschütztes System handelt und unbefugter Zugriff strafbar sein kann. So werden potenzielle Angreifer (zumindest formal) gewarnt.