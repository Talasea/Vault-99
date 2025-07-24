Hier ist eine Schritt-für-Schritt-Anleitung, wie Sie die erfassten Dateien (z. B. eapol_capture.pcap und capture-01.cap) von Ihrem OpenWrt-Router auf Kali Linux oder Windows übertragen und für die weitere Analyse verwenden können:

1. Überprüfen der erfassten Dateien
Auf Ihrem OpenWrt-Router haben Sie folgende Dateien:

EAPOL-Handshakes: eapol_capture.pcap

Paket-Captures: capture-01.cap, capture-02.cap, etc.

Vergewissern Sie sich, dass die Dateien vollständig und korrekt erfasst wurden:

bash
ls -lh
1. Übertragen der Dateien auf Kali Linux oder Windows
a) Übertragung mit SCP (Kali Linux)
Öffnen Sie ein Terminal auf Ihrem Kali Linux-System.

Übertragen Sie die Dateien mit dem scp-Befehl:

bash
scp root@192.168.1.1:/root/eapol_capture.pcap .
scp root@192.168.1.1:/root/capture-01.cap .
Ersetzen Sie 192.168.1.1 durch die IP-Adresse Ihres OpenWrt-Routers.

Überprüfen Sie, ob die Dateien erfolgreich übertragen wurden:

bash
ls -lh
b) Übertragung mit WinSCP (Windows)
Laden Sie WinSCP herunter und installieren Sie es.

Verbinden Sie sich mit Ihrem Router:

Protokoll: SCP

Hostname: IP-Adresse des Routers (z. B. 192.168.1.1)

Benutzername: root

Passwort: (Ihr OpenWrt-Passwort)

Navigieren Sie zum Verzeichnis, in dem die Dateien gespeichert sind (z. B. /root/).

Ziehen Sie die Dateien (eapol_capture.pcap, capture-01.cap) auf Ihren Windows-PC.

1. Analyse der Dateien
a) Analyse mit Wireshark
Wireshark ist ein leistungsstarkes Tool zur Analyse von Netzwerkverkehr und EAPOL-Handshakes.

Öffnen Sie Wireshark auf Ihrem System.

Laden Sie die Datei eapol_capture.pcap:

Datei > Öffnen > Wählen Sie die .pcap-Datei aus.

Filtern Sie nach EAPOL-Paketen:

text
eapol
Überprüfen Sie, ob ein vollständiger WPA/WPA2-Handshake erfasst wurde:

Suchen Sie nach vier EAPOL-Paketen (Message 1 bis 4).

b) Cracken des WPA/WPA2-Schlüssels mit aircrack-ng
Falls ein vollständiger Handshake vorhanden ist, können Sie versuchen, den WPA/WPA2-Schlüssel zu knacken.

Wechseln Sie in das Verzeichnis, in dem sich die .cap-Dateien befinden:

bash
cd /path/to/captures/
Führen Sie aircrack-ng aus:

bash
aircrack-ng capture-01.cap -w /path/to/wordlist.txt
Ersetzen Sie /path/to/wordlist.txt durch den Pfad zu Ihrer Wörterbuchdatei (z. B., rockyou.txt).

Wenn der Schlüssel gefunden wird, wird er im Terminal angezeigt.

1. Alternativer Ansatz: PMKID-Angriff
Falls der Handshake unvollständig ist oder keine Clients verbunden sind, können Sie prüfen, ob PMKID-Daten im Capture vorhanden sind.

Schritte zur Extraktion von PMKID
Installieren Sie hcxtools auf Kali Linux:

bash
sudo apt install hcxtools
Extrahieren Sie PMKID-Daten aus der .cap-Datei:

bash
hcxpcapngtool -o pmkid_hash.hc22000 capture-01.cap
Cracken des PMKID mit Hashcat:

bash
hashcat -m 22000 pmkid_hash.hc22000 /path/to/wordlist.txt
1. Fehlerbehebung
Problem: "Couldn't determine current channel for mon0"
Dies tritt auf, wenn der Kanal des Monitor-Interfaces nicht korrekt eingestellt ist.

Lösung:

Setzen Sie den Kanal manuell:

bash
iw dev mon0 set channel <channel_number>
Wiederholen Sie den Deauthentifizierungsangriff und die Capture-Erfassung.

1. Präsentation vorbereiten
Für Ihre Präsentation können Sie folgende Punkte hervorheben:

Die Erfassung von EAPOL-Handshakes mit OpenWrt.

Die Übertragung der Daten auf ein leistungsfähigeres System (z.B., Kali Linux).

Die Analyse der Daten mit Wireshark und das Cracken mit aircrack-ng oder Hashcat.

Mit diesen Schritten können Sie Ihre erfassten Daten erfolgreich analysieren und für Ihre Präsentation nutzen!