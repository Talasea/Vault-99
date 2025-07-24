---
created: 1970-01-01T01:00
updated: 2024-12-19T14:21
---
Die folgenden Aufgaben und Übungen diesen dazu euch im Umgang mit dem CLI (Command Line Interface) vertrauter zu machen. Ziel der Aufgaben ist es die Konfigurationen und Ergebnisse zu erzielen ohne die GUI zu verwenden. 
Die GUI kann gerne genutzt werden die Einstellungen zu prüfen. 

Notiert euch relevante Commands oder die Bedeutung von bestimmten Fehlermeldungen. Versucht diese zu Google oder euch die Informationen aus den relevanten Documentation zu entnehmen. Die meisten der Dokumentationen werden auf Englisch sein. 

Bitte löst die Aufgaben nicht via. Chat GPT oder ähnlichem. Gerade bei dieser Art Aufgabe ist das verfrühte Aufgeben und AI fragen besonders schädlich ;) 

## 0. Baut eine SSH Verbindung auf vom HOST zur Kali Maschine
0) Konfiguriert das Netzwerk so das der host die Linux Maschine anpingen kann
1) Installiert euch MobaXterm
	1) Schaut euch in der Software um
	2) Richtet eine SSH Verbindung zum Linux ein
	3) erstellt eine text Datei auf dem Desktop


## 1. SSH Zugänge anpassen
1) Verbindet euch mit dem Kali user via ssh auf die Maschine
2) Erstellt einen neuen User
	1) Informiert euch darüber was es bei der Erstellung zu beachten gibt
3) Gebt dem User die nötigen Rechte und passt die Konfiguration sodass es möglich ist eine SSH Verbindung mit diesem neuen User aufzubauen
  Bonus) Konfiguriert den User so das es möglich ist eine SICHERE Verbindung ohne Password abfrage herzustellen. (Stichwort KEYS)


## 2. Kleine Aufgabe in Kali Linux
Im Folgenden sollt ihr ein paar kleinere Aufgaben in Kali Linux erledigen, welche euch im Umgang mit Linux und der CLI helfen sollen.

1. **Erstellt einen Sicherungspunkt**
   - Erstellt einen Sicherungspunkt eures aktuellen Systems und dokumentiert den Vorgang mit einer sauberen Beschreibung.
2. **Logs lesen**
   - Findet heraus, wann ihr euch gestern zum ersten Mal via SSH eingeloggt habt. Prüft die entsprechenden Logs und notiert die Uhrzeit.
3. **Speicherplatz überprüfen**
   - Zeigt, wie viel Speicherplatz noch auf der Kali Maschine zur Verfügung steht. 
4. **Installiert das Tool NCDU**
   - Installiert das Tool `ncdu` und macht euch mit den grundlegenden Funktionen vertraut.
5. **Was kann man mit diesem Tool machen?**
   - Beschreibt ganz kurz die Hauptfunktionen und Anwendungsbereiche von `ncdu`.
6. **Prüft, welche Ports auf der Kali Maschine geöffnet sind**
7. **Konfiguriert eine SSH-Willkommensnachricht**
   - Erstellt eine individuelle Willkommensnachricht für SSH-Benutzer. Dies kann entweder eine freundliche Begrüßung oder eine Warnung an den Nutzer sein, keinen Unsinn zu machen.

## Bonus - NMAP
0. **Informiert euch über das Tool "nmap"**   
   - Recherchiert die grundlegenden Funktionen von `nmap`. Beschreibt kurz für euch, wofür das Tool genutzt wird und welche typischen Commands damit gebildet werden können.
1. **Baut über die Kali Maschine eine VPN-Verbindung zum LAB auf**
   - Richtet eine VPN-Verbindung von eurer Kali Maschine zum vorgesehenen LAB ein. Dokumentiert die Schritte und stellt sicher, dass die Verbindung stabil ist.
2. **Findet heraus, welche weiteren Maschinen in diesem Netzwerk sind**
   - Nutzt `nmap`, um das Netzwerk zu scannen und andere aktive Maschinen im Netzwerk zu identifizieren.
3. **Analysiert die neue Maschine, die ihr im Netzwerk findet (nicht eure :D )**
   - **Prüft, welche Ports offen sind**
     - Führt einen Portscan der entdeckten Maschine durch und dokumentiert die offenen Ports.
   - **Auf welche in der Maschine laufenden Anwendungen könnt ihr Rückschlüsse ziehen?**
     - Basierend auf den offenen Ports und den dazugehörigen Diensten, identifiziert und beschreibt die laufenden Anwendungen auf der Maschine

# VPN Informationen:
Die vpn Datei findet ihr im Google drive unter: 

Die Anmeldedaten des VPNs sind: Tmux Tigers/Software/VPN Config/F3-UDP4-40120-23-06-config
name: 23-06
password: VPNLab2306
In Zeile 10 die letzten zwei stellen ändern. 
Etwas zwischen 22 und 28
