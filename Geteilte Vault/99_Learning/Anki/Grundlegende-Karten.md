---
created: 2024-11-22T09:51
updated: 2025-02-24T12:55
---
TARGET DECK: CC Essentials

START
Einfach
Vorderseite: Was ist ein wesentlich effizientere Ansatz als Passwort-Brute-Force?
Rückseite: Wörterbuch-Angriff (große Liste mit gängigen Passwörtern)
END

START
Einfach
Vorderseite: Was versteht man unter einem Passwort-Brute-Force Angriff?
Rückseite: Es werden **alle möglichen** Passwörter ausprobiert
Beispiel: 6-Zeichen langes Passwort, nur Kleinbuchstaben und Ziffern
26 (Kleinbuchstaben) + 10 (Ziffern) = 36
Für jede Stelle 36 Möglichkeiten -> 36\*36\*36\*36\*36\*36 = 2.176.782.336
END


START
Einfach
Vorderseite: Was sind Vorraussetzungen für eine sichere Datenkommunikation?
Rückseite: 
* Vertraulichkeit
* Integrität
* Authentizität
END

START
Einfach
Vorderseite: Was ist das BSI?
Rückseite: Bundesamt für Sicherheit in der Informationstechnik
<!--ID: 1740395190956-->
END

START
Einfach
Vorderseite: Passwörter im Klartext (ausgeschrieben) zu speichern ist immer eine schlechte Idee. Mit welcher Methode kann ich dies vermeiden?
Rückseite: Man verwendet eine Einwegfunktion (Hashfunktion) um das Passwort als Hashwert zu speichern.
<!--ID: 1740395190961-->
END

START
Einfach
Vorderseite: Was sind Unterschiede zwischen den Transportprotokollen TCP und UDP (2)
Rückseite:
* TCP ist verbindungsorientiert (3-Way-Handshake) - UDP verbindungslos
* TCP ist zuverlässig (Bestätigung empfangener Nachrichten) - UDP keinerlei Prüfung ob die Nachrichten wirklich angekommen sind
<!--ID: 1740395190968-->
END
 
START
Einfach
Vorderseite: Wie sieht in Active Directory der Zugriff auf eine Ressource mittels Kerberos aus? (3)
Rückseite:
1. Der Benutzer frägt nach einem **Ticket-Granting-Ticket (TGT)**
2. Mit dem TGT frägt der Benutzer nach einem **Service Ticket**
3. Mit dem Service Ticket wird der Zugriff auf eine Ressource durchgeführt
<!--ID: 1740395190972-->
END


START
Einfach
Vorderseite: Welche Schutzziele beinhaltet die CIA-Triade?
Rückseite:
* Vertraulichkeit
* Integrität
* Verfügbarkeit
<!--ID: 1740395190980-->
END


START
Einfach
Vorderseite: Was ist eine Zero-Day Schwachstelle?
Rückseite: Eine bisher unbekannte Sicherheitslücke in einem IT-Produkt
<!--ID: 1740395190990-->
END

START
Einfach
Vorderseite: Was ist eine Advanced Persistent Threat (APT)?
Rückseite: Eine extrem gut organisierte und fortschrittliche Hackergruppe mit nahezu unbegrenzten Ressourcen (manche u.a. auch staatlich unterstützt/gesteuert)
<!--ID: 1740395190993-->
END

START
Einfach
Vorderseite: Was ist ASCII?
Rückseite: Die 127 am häufigsten verwendeten Buchstaben und Zeichen werden als genormte Bitwerte dargestellt
(_American Standard Code for Information Interchange_)
<!--ID: 1740395190997-->
END

START
Einfach
Vorderseite: Wie viele Zustände kann ich mit 7 Bit darstellen?
Rückseite: 128
**Erklärung:** 7 bit = 2 Zustände pro bit = 2\*2\*2\*2\*2\*2\*2 = **128**
**Vorsicht:** Die größte Zahl die wir abbilden können ist **127** (wir zählen die 0 mit)
<!--ID: 1740395191000-->
END

START
Einfach
Vorderseite: Auf welchem Layer arbeitet eine herkömmliche stateless/statefull Firewall?
Rückseite: Auf Layer 3 (IP Adressen werden gefiltert) und Layer 4 (Ports werden gefiltert)
<!--ID: 1740395191002-->
END

START
Einfach
Vorderseite: Was ist Portforwarding?
Rückseite: Portforwarding (Portweiterleitung) dient dazu, Datenverkehr, der über das Internet auf einen bestimmten Port gelangt, an einen spezifischen Host im lokalen Netzwerk zu senden. So können hinter einem NAT-Gerät (Router) laufende Dienste extern erreichbar gemacht werden (z.B. Webserver).
<!--ID: 1740395191008-->
END

START
Einfach
Vorderseite: Was sind Well Known Ports?
Rückseite: Diese Ports (0–1023) sind für grundlegende Netzwerkdienste reserviert. Beispielsweise läuft HTTP standardmäßig auf Port 80, HTTPS auf 443 und SSH auf 22. Sie werden von der IANA verwaltet und gelten als offizielle Standardports für weit verbreitete Dienste.
<!--ID: 1740395191010-->
END

START
Einfach
Vorderseite: Was ist ein Port Scan?
Rückseite: Beim Port Scan werden alle Ports eines Geräts oder Servers durchgetestet, um herauszufinden, welche Ports offen und damit potenziell angreifbar sind. Tools wie nmap nutzen Port Scans zur Sicherheitsüberprüfung und Netzwerkdiagnose.
<!--ID: 1740395191014-->
END

START
Einfach
Vorderseite: Was ist ein Switch und wie unterscheidet er sich von einem Hub?
Rückseite: Ein Switch filtert und leitet Datenpakete anhand ihrer MAC-Adressen gezielt an das richtige Ziel weiter. Anders als ein Hub, der Daten an alle angeschlossenen Ports weiterreicht, sendet ein Switch Pakete nur an den zugehörigen Port. Dadurch wird das Netzwerk entlastet und die Bandbreite effizienter genutzt.
<!--ID: 1740395191017-->
END

START
Einfach
Vorderseite: Wofür wird UPnP genutzt?
Rückseite: Universal Plug and Play (UPnP) ermöglicht es Netzwerkgeräten, sich selbstständig zu erkennen und Ports automatisch auf dem Router freizugeben. Es vereinfacht den Netzwerkaustausch (z.B. bei Streaming-Geräten, Spielekonsolen etc.), birgt jedoch auch potenzielle Sicherheitslücken, wenn nicht richtig abgesichert.
<!--ID: 1740395191020-->
END

START
Einfach
Vorderseite: Was ist die Hauptmotivation hinter IPv6?
Rückseite: Da der IPv4-Adressraum (32 Bit) nahezu erschöpft ist, wurde mit IPv6 ein Protokoll eingeführt, das mit 128 Bit eine weitaus größere Anzahl möglicher IP-Adressen bereitstellt.
<!--ID: 1740395191022-->
END

START
Einfach
Vorderseite: Wie sieht das Format einer IPv6-Adresse aus und wie werden Ziffernfolgen abgekürzt?
Rückseite: Eine IPv6-Adresse besteht aus 8 Blöcken à 16 Bit (hexadezimal). Führende Nullen in jedem Block dürfen weggelassen werden und zusammenhängende Null-Blöcke können einmal pro Adresse durch :: ersetzt werden. Beispiel: 2001:0db8:0000:0000:0000:ff00:0042:8329 wird zu 2001:db8::ff00:42:8329.
<!--ID: 1740395191025-->
END

START
Einfach
Vorderseite: Wieso ist Subnetting sinnvoll?
Rückseite: Subnetting strukturiert ein größeres Netzwerk in mehrere kleinere Teilnetze. Das reduziert den Broadcast-Verkehr, verbessert die Verwaltung (z.B. nach Abteilungen), und sorgt für eine effizientere IP-Adressnutzung.
<!--ID: 1740395191028-->
END

START
Einfach
Vorderseite: Wofür sind Dateisysteme da und warum existieren mehrere?
Rückseite: Dateisysteme regeln die Organisation, Speicherung und Verwaltung von Daten auf Datenträgern. Je nach Plattform oder Einsatzzweck (Windows, Linux, mobile Geräte) entstehen unterschiedliche Standards wie NTFS, ext4 oder APFS, da sie verschiedene Features und Leistungsschwerpunkte bieten.
<!--ID: 1740395191032-->
END

START
Einfach
Vorderseite: Was versteht man unter einer Top-Level Domain (TLD)?
Rückseite: Unter TLD fallen die Endungen einer Internetadresse wie .com, .net oder .de. Sie bilden die oberste Ebene im Domain Name System (DNS). Es gibt generische TLDs (z.B. .org) und länderspezifische TLDs (z.B. .fr).
<!--ID: 1740395191034-->
END