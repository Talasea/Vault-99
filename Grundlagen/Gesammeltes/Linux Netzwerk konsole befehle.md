
# 

Linux Netzwerkbefehle

Linux bietet eine Vielzahl von Netzwerkbefehlen, die Sie von der Kommandozeile aus verwenden können. Hier sind einige der wichtigsten:

- **ip addr**: Zeigt die Konfiguration der Netzwerkschnittstellen an und ermöglicht deren Verwaltung. Dieser Befehl ersetzt den veralteten `ifconfig` und unterstützt auch IPv6.
- **ifconfig**: Obwohl veraltet, kann dieser Befehl verwendet werden, um die Konfiguration der Netzwerkschnittstellen anzuzeigen und zu verwalten. Mit `ifconfig -a` werden alle Schnittstellen angezeigt, einschließlich inaktiver.
- **iwconfig**: Zeigt alle WLAN-Daten an und ermöglicht deren Verwaltung.
- **rfkill**: Erlaubt es, drahtlose Schnittstellen zu überprüfen, einzuschalten und auszuschalten. Mit `rfkill list` können Sie den Zustand aller drahtlosen Schnittstellen anzeigen.
- **ping**: Überprüft die Netzwerkverbindung und die Verfügbarkeit einer Webseite. Wenn Sie `ping www.google.de` eingeben, wird geprüft, ob eine Verbindung zum angegebenen Host hergestellt werden kann.
- **nslookup**: Wandelt eine Domainname in eine IP-Adresse um und umgekehrt.
- **dhclient**: Erlaubt es, eine neue IP-Adresse vom DHCP-Server zu beziehen. Mit `dhclient eth0` wird die IP-Adresse der angegebenen Schnittstelle erneuert.
- **netstat**: Zeigt die aktiven Netzwerkverbindungen an. Viele Linux-Administratoren bevorzugen den Befehl `ss`, der eine ähnliche Funktion hat und oft als Ersatz für `netstat` verwendet wird.
- **ssh**: Öffnet den Fernzugriff auf Server oder Linux-Desktops. Mit dem Schalter `-X` können Sie X11-Forwarding aktivieren, und mit `-p` können Sie den Port angeben, falls er vom Standardport 22 abweicht.
- **scp**: Ermöglicht das sichere Kopieren von Dateien zwischen Hosts. Der Hostname und der Verzeichnispfad werden durch einen Doppelpunkt getrennt.

Diese Befehle helfen Ihnen, die Netzwerkkonfiguration und -verbindung von der Kommandozeile aus zu überprüfen und zu verwalten.

## iPerf

Während ping die Verfügbarkeit eines Hosts prüft, hilft iPerf bei der Analyse und Messung der Netzwerkleistung zwischen zwei Hosts. Mit iPerf öffnen Sie eine Verbindung zwischen zwei Hosts und senden einige Daten. iPerf zeigt dann die verfügbare Bandbreite zwischen den beiden Hosts an.

Sie können iPerf über den Paketmanager Ihrer Distribution installieren. Bei Ubuntu-basierten Distributionen können Sie iPerf zum Beispiel wie folgt installieren:

```markup
$ sudo apt install iperf -y
```

Copy

Sobald Sie iPerf auf beiden Rechnern installiert haben, starten Sie den iPerf-Server auf einem der beiden Rechner. Das folgende Beispiel startet den iPerf-Server auf einem Rechner mit der IP-Adresse 10.0.0.51.

```markup
$ iperf -s
------------------------------------------------------------
Server lauscht auf TCP-Port 5001
TCP-Fenstergröße: 85.3 KByte (Standard)
------------------------------------------------------------
```

Copy

Starten Sie auf dem zweiten Rechner iPerf mit der Option -c. Dies stellt eine Verbindung mit dem Server her und sendet einige Daten.

```markup
$ iperf -c 10.0.0.51
------------------------------------------------------------
Client verbindet sich mit 10.0.0.51, TCP-Port 5001
TCP-Fenstergröße: 85.0 KByte (Standard)
------------------------------------------------------------
[3] lokaler 10.0.0.50 Port 42177 verbunden mit 10.0.0.51 Port 5001
[ ID] Intervall Übertragungsbandbreite
[ 3] 0.0-10.0 sec 1.13 GBytes 972 Mbits/sec
```

Copy

iPerf meldet sich in ein paar Sekunden mit den Ergebnissen der Bandbreite zurück.

## traceroute

Wenn ping fehlende Pakete anzeigt, sollten Sie traceroute verwenden, um zu sehen, welche Route die Pakete nehmen. Traceroute zeigt die Abfolge der Gateways an, die die Pakete durchlaufen, um ihr Ziel zu erreichen. Ein Beispiel: traceroute von meinem Rechner zu google.com zeigt das Folgende an:

```markup
$ traceroute google.com
traceroute zu google.com (172.217.167.46), maximal 64 Hops, 52 Byte Pakete
 1 dlinkrouter.dlink (192.168.0.1) 5,376 ms 2,076 ms 1,932 ms
 2 10.194.0.1 (10.194.0.1) 5.190 ms 5.125 ms 4.989 ms
 3 breitband.actcorp.in (49.207.47.201) 7.165 ms 5.749 ms 5.755 ms
 4 breitband.actcorp.in (49.207.47.225) 5.918 ms * 8.483 ms
...
 9 108.170.251.97 (108.170.251.97) 6.359 ms
    del03s16-in-f14.1e100.net (172.217.167.46) 5.448 ms
    108.170.251.97 (108.170.251.97) 6.400 ms
```

Copy

Zeile 4 in dieser Ausgabe zeigt ein * in den Round Trip Zeiten. Dies bedeutet, dass keine Antwort empfangen wurde. Dafür kann es viele Gründe geben – da die ICMP-Pakete von traceroute eine niedrige Priorität haben, werden sie möglicherweise von einem Router verworfen. Oder es liegt einfach eine Überlastung vor. Wenn Sie in allen Zeitfeldern für ein bestimmtes Gateway ein * sehen, dann ist das Gateway möglicherweise nicht erreichbar.

Mit vielen webbasierten Tools zur Routenverfolgung können Sie einen Traceroute in umgekehrter Richtung durchführen, d.h. von einer Website zu Ihrem Host. Sie können dies bei [traceroute.org](http://traceroute.org/) oder [Geekflare Traceroute](https://domsignal.com/traceroute-test) überprüfen.

## tcpdump

[tcpdump](https://geekflare.com/de/tcpdump-examples/) ist ein Packet-Sniffing-Tool und kann bei der Lösung von Netzwerkproblemen sehr hilfreich sein. Es hört den Netzwerkverkehr ab und gibt anhand der von Ihnen festgelegten Kriterien Paketinformationen aus.

Sie können zum Beispiel alle Pakete untersuchen, die von oder zu einem bestimmten Host gesendet werden, in diesem Beispiel Ubuntu18:

```markup
$ sudo tcpdump host ubuntu18 -n -c 5
tcpdump: ausführliche Ausgabe unterdrückt, verwenden Sie -v oder -vv für eine vollständige Protokolldekodierung
lauscht auf eth0, Link-Typ EN10MB (Ethernet), Capture-Größe 262144 Bytes
14:12:11.509092 IP 10.0.0.4.22 > 183.83.208.234.9633: Flags [P.], seq 2991049004:2991049112, ack 2956233368, win 501, options [nop,nop,TS val 292041322 ecr 405604219], length 108
14:12:11.509146 IP 10.0.0.4.22 > 183.83.208.234.9633: Flags [P.], seq 108:252, ack 1, win 501, options [nop,nop,TS val 292041322 ecr 405604219], length 144
14:12:11.509218 IP 10.0.0.4.22 > 183.83.208.234.9633: Flags [P.], seq 252:288, ack 1, win 501, options [nop,nop,TS val 292041322 ecr 405604219], length 36
14:12:11.509259 IP 10.0.0.4.22 > 183.83.208.234.9633: Flags [P.], seq 288:500, ack 1, win 501, options [nop,nop,TS val 292041322 ecr 405604219], length 212
14:12:11.509331 IP 10.0.0.4.22 > 183.83.208.234.9633: Flags [P.], seq 500:768, ack 1, win 501, options [nop,nop,TS val 292041322 ecr 405604219], length 268
5 Pakete abgefangen
6 Pakete vom Filter empfangen
0 vom Kernel verworfene Pakete
```

Copy

Standardmäßig löst tcpdump IP-Adressen in Hostnamen auf. Verwenden Sie das Flag `-n`, wenn Sie nicht möchten, dass tcpdump Namenssuchen durchführt.

tcpdump gibt für jedes Paket eine Zeile aus. Verwenden Sie das Flag `-c`, um die Ausgabe einzuschränken (5 im obigen Beispiel).

tcpdump ist nützlich für die Lösung von Netzwerkproblemen und auch für die Identifizierung potenzieller Probleme. Es ist eine gute Idee, gelegentlich einen tcpdump in Ihrem Netzwerk auszuführen, um zu überprüfen, ob alles in Ordnung ist.

## netstat

Mit dem Befehl netstat können Sie Netzwerkverbindungen, Routing-Tabellen sowie verschiedene Netzwerkeinstellungen und Statistiken untersuchen.

Verwenden Sie das Flag `-i`, um die Netzwerkschnittstellen auf Ihrem System aufzulisten.

Hier ist ein Beispiel:

```markup
$ netstat -i
Tabelle der Kernel-Schnittstellen
Iface MTU Met RX-OK RX-ERR RX-DRP RX-OVR TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0 1500 0 4001 0 0 0 2283 0 0 0 BMRU
eth1 1500 0 27154 0 0 0 838962 0 0 0 BMRU
lo 65536 0 0 0 0 0 0 0 0 LRU
```

Copy

Mit dem Flag `-r` wird die Routing-Tabelle angezeigt. Dies zeigt den für das Senden von Netzwerkpaketen konfigurierten Pfad an.

```markup
$ netstat -r
Kernel IP-Routing-Tabelle
Ziel-Gateway Genmask Flags MSS Window irtt Iface
standard 10.0.2.2 0.0.0.0 UG 0 0 0 eth0
10.0.0.0 * 255.255.255.0 U 0 0 0 eth1
10.0.2.0 * 255.255.255.0 U 0 0 0 eth0
```

Copy

Ein Sternchen in den letzten beiden Zeilen bedeutet, dass kein Gateway erforderlich ist, um Pakete an einen Host in diesen Netzwerken zu senden. Dieser Host ist direkt mit den Netzwerken 10.0.0.0 und 10.0.2.0 verbunden.

In der ersten Zeile ist das Ziel der Standardwert, d.h. jedes Paket, das für ein nicht in dieser Tabelle aufgeführtes Netzwerk bestimmt ist, wird vom Router 10.0.2.2 bearbeitet.

der Befehl netstat ohne Optionen zeigt eine Liste der offenen Sockets an. Verwenden Sie das Flag `-l`, um nur die lauschenden Sockets anzuzeigen, die standardmäßig nicht angezeigt werden. Mit dem Flag -a können Sie sich sowohl abhörende als auch nicht abhörende Sockets anzeigen lassen. Hier ist ein Beispiel:

```markup
$ netstat -a
Aktive Internetverbindungen (Server und bestehende)
Proto Recv-Q Send-Q Lokale Adresse Fremde Adresse Status      
tcp 0 0 *:ssh *:* LISTEN     
tcp 0 36 10.0.2.15:ssh 10.0.2.2:51017 ESTABLISHED
tcp6 0 0 [::]:ssh [::]:* LISTEN     
udp 0 0 *:bootpc *:*   
Aktive UNIX-Domain-Sockets (Server und eingerichtet)
Proto RefCnt Flags Typ Zustand I-Node Pfad
unix 3 [ ] DGRAM 8186 /run/systemd/notify
...
```

Copy

Weitere Netstat-Befehlsbeispiele [hier](https://geekflare.com/de/netstat/)

## ss

Bei Linux-Installationen werden standardmäßig viele Dienste ausgeführt. Diese sollten deaktiviert oder vorzugsweise entfernt werden, da dies dazu beiträgt, die Angriffsfläche zu verringern. Sie können mit dem Befehl netstat sehen, welche Dienste ausgeführt werden. Während netstat noch verfügbar ist, gehen die meisten Linux-Distributionen zum Befehl `ss` über.

verwenden Sie den Befehl ss mit den Flags `-t` und `-a`, um alle TCP-Sockets aufzulisten. Dadurch werden sowohl lauschende als auch nicht lauschende Sockets angezeigt.

```markup
$ ss -t -a
Zustand Recv-Q Send-Q Lokale Adresse:Port Peer-Adresse:Port   
LISTEN 0 128 *:sunrpc *:*   
LISTEN 0 128 *:http *:*   
LISTEN 0 128 *:ssh *:*   
LISTEN 0 128 *:60031 *:*   
ESTAB 0 0 10.0.2.15:ssh 10.0.2.2:51699   
ESTAB 0 0 10.0.2.15:ssh 10.0.2.2:51049   
LISTEN 0 128 :::sunrpc :::*    
LISTEN 0 128 :::http :::*    
LISTEN 0 128 :::ssh :::*    
LISTEN 0 128 :::54715 :::*
```

Copy

Um nur TCP-Verbindungen mit dem Status established anzuzeigen:

```markup
ss -a -t -o state established
Recv-Q Send-Q Lokale Adresse:Port Peer-Adresse:Port   
0 0 10.0.2.15:ssh 10.0.2.2:51699 timer:(keepalive,23min,0)
0 0 10.0.2.15:ssh 10.0.2.2:51049 timer:(keepalive,114min,0)
```

Copy

## ssh

mit ssh können Sie sich über das Internet sicher mit entfernten Hosts verbinden. Früher wurden rlogin und telnet verwendet, um sich mit entfernten Hosts zu verbinden und diese zu verwalten. Beide haben jedoch einen grundlegenden Fehler, nämlich dass sie alle Informationen, einschließlich Anmeldenamen und Kennwörter, im Klartext senden.

ssh ermöglicht eine [sichere Kommunikation](https://geekflare.com/de/linux-ssh-key-exchange/) über das Internet mit den folgenden zwei Funktionen:

- Es bestätigt, dass der entfernte Host derjenige ist, der er vorgibt zu sein.
- Es verschlüsselt die gesamte Kommunikation zwischen den Hosts.

Um eine Verbindung zu einem entfernten Host herzustellen, müssen Sie einen OpenSSH-Server auf dem entfernten Host laufen haben. Sie können ihn mit dem Paketmanager Ihrer Distribution installieren. Unter Ubuntu können Sie ihn zum Beispiel wie folgt installieren:

```markup
$ sudo apt install openssh-server
```

Copy

Das folgende Beispiel zeigt, wie Sie mit dem ssh-Befehl eine Verbindung zum entfernten Host 10.0.0.50 herstellen können:

```markup
me@ubuntu-xenial:~$ ssh 10.0.0.50
Die Authentizität des Hosts '10.0.0.50 (10.0.0.50)' kann nicht festgestellt werden.
Der Fingerabdruck des ECDSA-Schlüssels lautet SHA256:s2tNJQa/C1/W0SevGm7Rt3xoBZG1QL5yT3ff/ PMpnY.
Sind Sie sicher, dass Sie die Verbindung fortsetzen möchten (ja/nein)? ja
```

Copy

Sie erhalten eine Meldung, die besagt, dass die Authentizität des Hosts 10.0.0.50 nicht hergestellt werden kann. Dies liegt daran, dass zum ersten Mal eine Verbindung mit 10.0.0.50 (Server) hergestellt wird und der ssh-Client diesen entfernten Host noch nie gesehen hat. Geben Sie Ja ein, um die Verbindung fortzusetzen. Sobald die Verbindung hergestellt ist, werden Sie zur Eingabe eines Passworts aufgefordert:

```markup
Warnung: Der Liste der bekannten Hosts wurde '10.0.0.50' (ECDSA) dauerhaft hinzugefügt.
das Passwort von me@10.0.0.50:
```

Copy

```markup
Willkommen bei Ubuntu 14.04.6 LTS (GNU/Linux 3.13.0-170-generic x86_64)
 * Dokumentation: https://help.ubuntu.com/
..
me@vagrant-ubuntu-trusty-64:~$ 
```

Copy

Sie können diese Remote-Shell mit dem Befehl exit verlassen.

Außerdem können Sie mit ssh ganz einfach einen einzelnen Befehl auf dem entfernten Rechner ausführen. Um zum Beispiel df -h auf dem entfernten Rechner auszuführen:

```markup
$ ssh 10.0.0.50 df -h
das Passwort von me@10.0.0.50: 
Dateisystem Größe Used Avail Use% Gemountet auf
udev 241M 12K 241M 1% /dev
tmpfs 49M 384K 49M 1% /run
/dev/sda1 40G 1.6G 37G 5% /
...
keine 224G 113G 111G 51% /vagrant
me@ubuntu-xenial:~$
```

Copy

## scp und sftp

scp (secure copy) ist dem `cp-Befehl` zum Kopieren von Dateien sehr ähnlich, mit einem Zusatz – Sie können den Hostnamen der Gegenstelle in den Quell- oder Zielpfadnamen aufnehmen. Der Hostname und der Verzeichnispfad werden durch einen Doppelpunkt getrennt. Auf diese Weise können Sie Dateien in verschlüsselter Form sicher über das Netzwerk kopieren. Der folgende Befehl kopiert a.txt vom lokalen Rechner nach 10.0.0.50 :

```markup
me@ubuntu-xenial:~$ scp a.txt 10.0.0.50:/home/me
das Passwort von me@10.0.0.50: 
a.txt 100% 0 0.0KB/s 00:00
```

Copy

sftp (secure ftp) ist ebenfalls ein Programm zum Kopieren von Dateien ähnlich wie `ftp`. Es verwendet jedoch einen verschlüsselten SSH-Tunnel, um Dateien zu kopieren, anstatt alles im Klartext zu senden. Außerdem benötigen Sie keinen FTP-Server, der auf dem entfernten Host läuft. Sie benötigen lediglich einen SSH-Server. Hier ist ein Beispiel für eine Sitzung:

```markup
me@ubuntu-xenial:~$ sftp 10.0.0.50
das Passwort von me@10.0.0.50: 
Verbunden mit 10.0.0.50.
sftp> put kali-linux-2020.3-installer-netinst-i386.iso
Hochladen von kali-linux-2020.3-installer-netinst-i386.iso nach /home/me/kali-linux-2020.3-installer-netinst-i386.iso
kali-linux-2020.3-installer-netinst-i386.iso 100% 435MB 27.2MB/s 00:16    
sftp> Auf Wiedersehen
```

Copy

## Ifconfig

Meistens verwenden wir den Befehl `ifconfig`, um die dem System zugewiesene IP-Adresse zu überprüfen.

```markup
[root@lab ~]# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
        inet 209.97.137.171 Netzmaske 255.255.240.0 Broadcast 209.97.143.255
        inet6 fe80::c035:b2ff:fe9d:72d5 prefixlen 64 scopeid 0x20<link>
        ether c2:35:b2:9d:72:d5 txqueuelen 1000 (Ethernet)
        RX-Pakete 1333200 Bytes 167143230 (159,4 MiB)
        RX-Fehler 0 verworfen 0 Überläufe 0 Rahmen 0
        TX-Pakete 979666 Bytes 93582595 (89,2 MiB)
        TX-Fehler 0 verworfen 0 Überläufe 0 Träger 0 Kollisionen 0

lo: flags=73<UP,LOOPBACK,RUNNING> mtu 65536
        inet 127.0.0.1 Netzmaske 255.0.0.0
        inet6 ::1 prefixlen 128 scopeid 0x10<host>
        loop txqueuelen 1000 (Lokaler Loopback)
        RX-Pakete 16 Bytes 1392 (1.3 KiB)
        RX-Fehler 0 verworfen 0 Überläufe 0 Rahmen 0
        TX-Pakete 16 Bytes 1392 (1.3 KiB)
        TX-Fehler 0 verworfen 0 Überläufe 0 Träger 0 Kollisionen 0

[root@lab ~]#
```

Copy

## dig

dig (Domain Information Groper) ist ein flexibles Tool zur Abfrage von DNS-Nameservern.

Es führt [DNS-Abfragen](https://domsignal.com/dns-lookup) durch und zeigt die Antworten an, die von den Nameservern zurückgegeben werden.

```markup
[root@lab ~]# dig geekflare.com/de

; <<>> DiG 9.11.13-RedHat-9.11.13-5.el8_2 <<>> geekflare.com/de
;; globale Optionen: cmd
;; Antwort erhalten:
;; ->>HEADER<<- Opcode: QUERY, status: NOERROR, id: 12310
;; Flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; FRAGEABSCHNITT:
; geekflare.com/de. IN A

;; ANTWORT-ABSCHNITT:
geekflare.com/de. 30 IN A 104.27.119.115
geekflare.com/de. 30 IN A 104.27.118.115

;; Abfragezeit: 12 msec
;; SERVER: 67.207.67.2#53(67.207.67.2)
;; WHEN: Wed Sep 16 17:58:45 UTC 2020
;; MSG SIZE rcvd: 74

[root@lab ~]#
```

Copy

## telnet

telnet connect destination’s host and port via telnet protocol, wenn eine Verbindung zustande kommt, bedeutet das, dass die Verbindung zwischen zwei Hosts gut funktioniert.

```markup
[root@lab ~]# telnet gf.dev 443
Versucht 104.27.153.44...
Verbunden mit gf.dev.
Escape-Zeichen ist '^]'.
```

Copy

## nslookup

nslookup ist ein Programm zur Abfrage von Domain-Name-Servern und zur Auflösung der IP.

```markup
[root@lab ~]# nslookup relicflare.com
Server: 67.207.67.2
Adresse: 67.207.67.2#53

Nicht-autoritative Antwort:
Name: relicflare.com
Adresse: 192.64.119.178

[root@lab ~]#

```



# 

Linux Netzwerkbefehle und IP Adressen vergeben

Um eine IP-Adresse unter Linux über die Kommandozeile zu vergeben, gibt es mehrere Methoden. Hier sind einige der wichtigsten Befehle und Schritte:

- **ip addr add**: Dieser Befehl wird verwendet, um eine IP-Adresse temporär zu einem Netzwerkinterface hinzuzufügen. Beispiel: `ip addr add 192.168.1.2/24 dev eth0`. Dies fügt die IP-Adresse 192.168.1.2 mit einer Subnetzmaske von 24 Bit (255.255.255.0) zum Interface eth0 hinzu.
    
- **ifconfig**: Obwohl dieser Befehl veraltet ist, kann er weiterhin verwendet werden, um eine IP-Adresse zu einem Interface hinzuzufügen. Beispiel: `ifconfig eth0 192.168.1.2 netmask 255.255.255.0`. Dies setzt die IP-Adresse 192.168.1.2 mit der Netzmaske 255.255.255.0 auf das Interface eth0.
    
- **/etc/network/interfaces bearbeiten**: Für eine dauerhafte Änderung der IP-Adresse muss die Netzwerkkonfigurationsdatei bearbeitet werden. Öffnen Sie die Datei mit einem Texteditor, z.B. `sudo nano /etc/network/interfaces`, und fügen Sie die folgende Konfiguration hinzu:
    
    ```
    iface eth0 inet static
        address 192.168.1.2
        netmask 255.255.255.0
        gateway 192.168.1.1
    ```
    
    Diese Konfiguration setzt eine statische IP-Adresse für das Interface eth0.
    
- **dhclient**: Dieser Befehl kann verwendet werden, um eine neue IP-Adresse über DHCP zu erhalten. Beispiel: `sudo dhclient eth0`.
    
- **ip link**: Dieser Befehl zeigt die verfügbaren Netzwerkschnittstellen an. Beispiel: `ip link show`. Dies hilft, den Namen des Netzwerkschnittstelles zu bestimmen, bevor eine IP-Adresse hinzugefügt wird.


