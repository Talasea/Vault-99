---
created: 2025-01-20T16:32
updated: 2025-02-24T12:48
---
TARGET DECK: CC Essentials::Netzwerktechnik

# Allgemein
##### Topologie Heimnetzwerk
START
Einfach
Vorderseite: In einem typischen Heimnetz mit einem Router, welche Netzwerktopologie habe ich?
Rückseite: Stern-Topologie
END

##### Erste Schicht OSI Modell
START
Einfach
Vorderseite: Was ist die erste Schicht im OSI-Layer Modell?
Rückseite: Bitübertragunsschicht oder physikalische Schicht
Hier werden die Informationen als physikalisches Signal (Elementarteilchen im Kabel, Radiowellen für Funk) übertragen
END

##### Kommunikationsarten
START
Einfach
Vorderseite: Von Unicast Kommunikation spricht man, wenn lediglich zwei Gesprächspartner involviert sind. Welche beiden anderen Kommunikationsarten haben wir kennengelernt?
Rückseite: 
* Multicast: ein Sender, **mehrere** Empfänger
* Broadcast: ein Sender, **alle** Teilnehmer im Netz sind Empfänger
END

# Routing
##### Dynamische Routing Protokolle
START
Einfach
Vorderseite: Was für dynamische Routing-Protokolle haben wir kennengelernt?
Rückseite: RIP, OSPF
END

# Firewall
##### Funktionsweise Firewall
START
Einfach
Vorderseite: Wie funktioniert eine Firewall?
Rückseite: Sicherheitsmaßnahme, prüft/**filtert** den Datenverkehr innerhalb eines Netzwerkes oder zwischen Netzwerken. Grundsätzlich eine Liste mit einzelnen Filterregeln.
END
##### Firewallarten
START
Einfach
Vorderseite: Was für Firewallarten haben wir kennengelernt? (2)
Rückseite: 
* Stateless (statuslos) und 
* Statefull (Zustand beachtende) Firewall
END

# Abläufe
##### Webseitenaufruf über HTTPS
START
Einfach
Vorderseite: 
An welcher Stelle wird ein TLS-Handshake durchgeführt, wenn ich eine Webseite über HTTPS aufrufe?
Rückseite: 
1. Domainname wird mittels DNS aufgelöst
2. TCP Verbindung aufbauen (3 way handshake)
3. **TLS Handshake (vom Client mit Client-Hello gestartet)**
4. Im Anschluss gesicherte Kommunikation über HTTPS
END


START
Einfach
Vorderseite: Welcher Schlüssel wird bei SSH-Authentifizierung vom Client verwendet?
Rückseite: Der private Schlüssel
END