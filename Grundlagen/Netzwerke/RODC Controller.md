Der Read-Only Domain Controller (RODC) ist ein spezieller Typ von Domain Controller, der seit Windows Server 2008 verfügbar ist. Er ist als Domain Controller für Standorte mit niedriger Sicherheitsstufe konzipiert, wie Zweigstellen oder kleine Außenbüros. Der RODC kann nur gelesen werden und unterstützt keine Schreibzugriffe auf die Active Directory DS-Datenbank. Schreibgeschützte Domain Controller bieten eine höhere Sicherheit, da sie keine sicherheitskritischen Daten, wie z.B. Kontokennwörter, speichern.

Einige Hauptmerkmale des RODC sind:

- Einidirektionale Replikation: Änderungen werden nur von einem beschreibbaren Domain Controller (RWDC) auf den RODC repliziert, aber nicht in die andere Richtung.
- Schreibgeschützter DNS: Der DNS auf dem RODC ist schreibgeschützt.
- Kennwortreplikation: Die Kennwortreplikation kann von Administratoren konfiguriert werden, um sicherzustellen, dass nur bestimmte Benutzerkonten lokal authentifiziert werden können.
- Filterter RODC-Attributsatz: Ein dynamischer Satz von Attributen, der nicht zu RODCs repliziert wird, um sensible Daten zu schützen.

Der RODC wird in Umgebungen eingesetzt, in denen physische Sicherheit für einen vollwertigen Domain Controller nicht gewährleistet ist. Dadurch wird die lokale Authentifizierung ermöglicht, selbst wenn die WAN-Verbindung mit der zentralen IT-Infrastruktur offline ist.