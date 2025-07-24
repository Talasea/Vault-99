
#### PING

Dient der Überprüfen der Netzverbindung zu einem bestimmten Host im IP-Netzwerk.

- zeigt die Zeitdauer der Datenpakete vom Sender zum Empfänger
- kann auf den lokalen Rechner ausgeführt werden (127.0.0.1) und zeigt damit ob TCP/IP installiert ist
- kann ggf. den Namen auflösen lassen (siehe Abbildung)

|   |
|---|
|C:\>ping www.schule.de<br><br>Ping www.schule.de [192.76.176.140] mit 32 Bytes Daten:<br><br>Antwort von 192.76.176.140: Bytes=32 Zeit=49ms TTL=51<br>Antwort von 192.76.176.140: Bytes=32 Zeit=48ms TTL=51<br>Antwort von 192.76.176.140: Bytes=32 Zeit=48ms TTL=51<br>Antwort von 192.76.176.140: Bytes=32 Zeit=47ms TTL=51<br><br>Ping-Statistik für 192.76.176.140:<br>    Pakete: Gesendet = 4, Empfangen = 4, Verloren = 0 (0% Verlust),<br>Ca. Zeitangaben in Millisek.:<br>    Minimum = 47ms, Maximum =  49ms, Mittelwert =  48ms<br><br>C:\>|

- auch wenn keine Antwort vom Empfänger kommt, kann die Netzverbindung funktionieren
- der Befehl kann mit STRG + C abgebrochen werden

---

#### IPCONFIG

Dient der Information über die aktuellen Netzwerkeinstellungen.

- die wichtigsten Informationen sind die IP-Adresse, die Subnetzmaske und der Standardgateway
- es werden Informationen zu allen Netzwerkadaptern (z.B. auch Modems oder ISDN-Karten) angezeigt
- Mit dem Konsolenbefehl **ipconfig /all** kann die vollständige IP-Konfiguration überprüft werden.

|   |
|---|
|C:\>ipconfig /all<br><br>Windows-IP-Konfiguration<br><br>        Hostname. . . . . . . . . . . . . : Hagrid<br>        Primäres DNS-Suffix . . . . . . . :<br>        Knotentyp . . . . . . . . . . . . : Broadcastadapter<br>        IP-Routing aktiviert. . . . . . . : Nein<br>        WINS-Proxy aktiviert. . . . . . . : Nein<br>        DNS-Suffixsuchliste . . . . . . . : Arbeitsgruppe<br><br>Ethernetadapter LAN-Verbindung:<br><br>        Verbindungsspezifisches DNS-Suffix: Arbeitsgruppe<br>        Beschreibung. . . . . . . . . . . : Intel(R) PRO/100 VE<br>        Physikalische Adresse . . . . . . : 00-30-05-50-02-2B<br>        DHCP-aktiviert. . . . . . . . . . : Ja<br>        Autokonfiguration aktiviert . . . : Ja<br>        IP-Adresse. . . . . . . . . . . . : 192.168.1.9<br>        Subnetzmaske. . . . . . . . . . . : 255.255.255.0<br>        Standardgateway . . . . . . . . . : 192.168.1.253<br>        DHCP-Server . . . . . . . . . . . : 192.168.1.253<br>        DNS-Server. . . . . . . . . . . . : 83.169.186.33<br>                                            192.168.1.253<br>        Lease erhalten. . . . . . . . . . : Samstag, 6. Oktober 2007 16:27:40<br>        Lease läuft ab. . . . . . . . . . : Samstag, 13. Oktober 2007 16:27:40<br><br>C:\>|

- es wird jetzt u.a. die physikalische Adresse (MAC-Adresse) angezeigt
- es werden die IP-Nummern der DNS-Server angezeigt
- es ist sichtbar, ob DHCP, aktiviert ist und wer (IP-Nummer des Servers) wann und für wie lange die IP-Adresse für den lokalen Ethernetadapters vergeben hat
- **ipconfig /release** gibt die aktuelle IP-Adresse frei
- **ipconfig /renew** erneuert die IP-Adresse

---

#### TRACERT (Windows)/TRACEROUTE (Unix)

Dient der Auflistung entsprechender Netzwerkknoten die ein Datenpaket zum Empfänger durchläuft.

|   |
|---|
|C:\>tracert www.schule.de<br><br>Routenverfolgung zu www.schule.de [192.76.176.140]  über maximal 30 Abschnitte:<br><br>  1   <10 ms   <10 ms   <10 ms  192.168.1.253<br>  2    16 ms     5 ms     8 ms  83-169-188-110-isp.superkabel.de [83.169.188.110]<br>  3     5 ms     5 ms    12 ms  83-169-181-14-isp.superkabel.de [83.169.181.14]<br>  4     7 ms     7 ms    10 ms  83-169-183-78-isp.superkabel.de [83.169.183.78]<br>  5     8 ms     8 ms    10 ms  88-134-251-70-isp.superkabel.de [88.134.251.70]<br>  6    11 ms    13 ms    14 ms  88-134-251-37-isp.superkabel.de [88.134.251.37]<br>  7    26 ms    20 ms    18 ms  83-169-128-14-isp.superkabel.de [83.169.128.14]<br>  8    39 ms    27 ms    25 ms  83-169-128-9-isp.superkabel.de [83.169.128.9]<br>  9    28 ms    27 ms    28 ms  83-169-128-129-isp.superkabel.de [83.169.128.129]<br> 10    47 ms    51 ms    48 ms  zr-pot1-te0-7-0-3.x-win.dfn.de [188.1.144.221]<br> 11    49 ms    52 ms    48 ms  xr-tub1-te2-3.x-win.dfn.de [188.1.144.222]<br> 12    43 ms    61 ms    42 ms  xr-hub1-te2-1.x-win.dfn.de [188.1.144.13]<br> 13    48 ms    46 ms    61 ms  kr-dfnbln.x-win.dfn.de [188.1.230.162]<br> 14    48 ms    48 ms    55 ms  ods.schule.de [192.76.176.140]<br><br>Ablaufverfolgung beendet.<br><br>C:\>|

- nicht alle Datenpakete müssen zwangsläufig diese Route wählen
- Hin- und Rückweg sind meist identisch
- wird verwendet um die Route der Datenpakete zu kontrollieren und eventuelle Fehler (z.B. Routing-Schleifen)
- lokalisiert ggf. ausgefallene Router und langsame Datenverbindungen

---

#### NSLOOKUP

Dient dazu, IP-Adressen abzufragen und Domain-Namen aufzulösen.  
(siehe auch [DNS](https://www.sachsen.schule/~dvt/lpe14/1412dns.htm#dns))

- standardmäßig wird dazu der eingestellte DNS-Server zur Auflösung verwendet

|   |
|---|
|C:\>nslookup<br>Standardserver:  l-quer-cns-1.technik.kabel-deutschland.de<br>Address:  83.169.186.33<br><br>> www.schule.de<br>Server:  l-quer-cns-1.technik.kabel-deutschland.de<br>Address:  83.169.186.33<br><br>Nicht autorisierte Antwort:<br>Name:    www.schule.de<br>Address:  192.76.176.140<br><br>> 192.76.176.140<br>Server:  l-quer-cns-1.technik.kabel-deutschland.de<br>Address:  83.169.186.33<br><br>Name:    ods.schule.de<br>Address:  192.76.176.140<br><br>> exit<br><br>C:\>|

- autoritative Nameserver können gesicherte Auskünfte zur Zone geben, in der sie sich befinden (im lokalen Netz)
- nicht-autoritative Nameserver beziehen ihre Informationen von anderen Nameservern, deren Information dann als "nicht autorisierte Antwort" (siehe oben) zur Verfügung gestellt wird.
- beendet wird die Abfrage mit EXIT

---

#### NETSTAT

Dient der Protokollstatistik und zeigt aktuelle TCP/IP-Netzwerkverbindungen an.

- **netstat - a** listet alle aktiven Verbindungen des lokalen Rechners auf.

|   |
|---|
|C:\>netstat -a<br><br>Aktive Verbindungen<br><br>  Proto  Lokale Adresse         Remoteadresse          Status<br>  TCP    Hagrid:epmap           Hagrid:0               ABHÖREN<br>  TCP    Hagrid:microsoft-ds    Hagrid:0               ABHÖREN<br>  TCP    Hagrid:1025            Hagrid:0               ABHÖREN<br>  TCP    Hagrid:netbios-ssn     Hagrid:0               ABHÖREN<br>  UDP    Hagrid:microsoft-ds    *:*<br>  UDP    Hagrid:1026            *:*<br>  UDP    Hagrid:1029            *:*<br>  UDP    Hagrid:1036            *:*<br>  UDP    Hagrid:netbios-ns      *:*<br>  UDP    Hagrid:netbios-dgm     *:*<br>  UDP    Hagrid:isakmp          *:*<br>  UDP    Hagrid:4500            *:*<br><br>C:\>|

- **netstat - e** listet die Ethernetstatistik
- **netstat - r** zeigt den Inhalt der Routingtabelle

# 

Netzwerkbefehle cmd ip adresse festlegen

Um die IP-Adresse mit dem Befehl `netsh` in der Windows-Kommandozeile (cmd) zu ändern, folgen Sie diesen Schritten:

1. Öffnen Sie eine Eingabeaufforderung mit Administratorrechten.
2. Bestimmen Sie den Namen der Netzwerkverbindung, indem Sie den Befehl `netsh interface ip show config` eingeben. Der Name der Verbindung wird unter “Name” angezeigt, z.B. “Ethernet”.
3. Setzen Sie die IP-Adresse statisch mit dem folgenden Befehl:
    
    ```
    netsh interface ipv4 set address name="Ethernet" static 192.168.178.10 255.255.255.0 192.168.178.1
    ```
    
    Dabei steht “Ethernet” für den Namen der Netzwerkverbindung, “192.168.178.10” für die neue IP-Adresse, “255.255.255.0” für die Subnetzmaske und “192.168.178.1” für das Gateway.
4. Optional können Sie die DNS-Adresse mit dem Befehl `netsh interface ip set dns "Ethernet" static 192.168.178.1` festlegen.
5. Überprüfen Sie die Konfiguration mit `ipconfig /all`.

Diese Schritte ermöglichen es Ihnen, die IP-Adresse, die Subnetzmaske, das Gateway und die DNS-Adresse für eine Netzwerkverbindung zu ändern.

