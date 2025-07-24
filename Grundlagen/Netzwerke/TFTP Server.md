
# 

TFTP Erklärung

Ein TFTP-Server (Trivial File Transfer Protocol) ist ein einfaches Protokoll zur Übertragung von Dateien zwischen Computern. Es ist einfacher zu handhaben als das File Transfer Protocol (FTP), aber weniger leistungsfähig. TFTP wird üblicherweise in lokalen Netzwerken (LAN) verwendet, nicht jedoch zur Übertragung von Dateien über das Internet, da es deutlich weniger sicher ist als FTP und SFTP.

TFTP verwendet das verbindungslose Protokoll User Datagram Protocol (UDP) und nicht wie FTP das Transmission Control Protocol (TCP). Ein TFTP-Server ist immer über Port 69 für alle eingehenden Anfragen des TFTP-Clients erreichbar. Das bedeutet, dass der TFTP-Server jedes Mal, wenn ein TFTP-Client eine Datei herunterladen möchte, einen Prozess erstellt und startet.

TFTP unterstützt insgesamt fünf Typen von Paketen, die sich jeweils durch ein eigenes, 16 Bit langes „Opcode“-Feld (Operations-Code) mit dem entsprechenden Wert ankündigen:

- **RRQ (Read Request)**: Anfrage für Lesezugriff
- **WRQ (Write Request)**: Anfrage für Schreibzugriff
- **DATA**: Datenpaket
- **ACK (Acknowledgment)**: Bestätigungsnachricht
- **ERROR**: Fehlernachricht

TFTP ist ein sehr einfaches Client-Server-Protokoll, das den Transfer von Dateien in Computernetzwerken regelt. Eine erste Spezifikation wurde im Juni 1981 in RFC 783 veröffentlicht. Der aktuelle Standard ist im 1992 erschienenen RFC 1350 nachzulesen. Das TFTP-Protokoll wurde extra so konzipiert, dass es möglichst klein und leicht zu implementieren ist.