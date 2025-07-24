
Ein Port ist ein Begriff aus dem Englischen, der “Anschluss” oder “Durchlass” bedeutet. In der Netzwerktechnik bezeichnet ein Port eine Adresse, mit deren Hilfe sich UDP- oder TCP-Verbindungen eindeutig bestimmten Anwendungen zuordnen lassen. Ports ermöglichen es, dass Datenpakete eines Transportprotokolls zu einem Prozess zugeordnet werden können.

- **Portnummern**: Es gibt Portnummern im Bereich von 0 bis 65535. Jeder Port hat eine andere Nummer, die wie ein Adresszusatz dient, um herauszufinden, an welche Anwendung die Daten gesendet werden sollen.
- **Standard-Ports**: Ports 1 bis 1023 sind für bestimmte Funktionen bereits reserviert. Zum Beispiel wird der Port 80 für Anfragen für Webseiten verwendet, während der Port 25 für das Versenden von Nachrichten verwendet wird.
- **User-Ports**: Ports 1024 bis 49151 sind für spezielle Dienste registriert. Um sich eine Portnummer registrieren zu können, muss man bei der Organisation IANA anfragen.
- **Freie Ports**: Ports 49152 bis 65535 können jeder verwenden.

**Funktionen von Ports** Ports helfen Computern, den empfangenen Netzwerk-Traffic zu sortieren. Sie ermöglichen es, dass Datenpakete eines Transportprotokolls zu einem Prozess zugeordnet werden können. Ports sind softwarebasiert und werden vom Betriebssystem eines Computers verwaltet. Jeder Port ist mit einem bestimmten Prozess oder Dienst verbunden.

- **Netzwerkprotokolle**: Ports können auch Netzwerkprotokolle und entsprechende Netzwerkdienste identifizieren. Zum Beispiel verwendet ein Webbrowser standardmäßig den TCP-Port 443 für HTTPS-Verbindungen.
- **Verbindungsaufbau**: Ein Client fordert beim Betriebssystem normalerweise einen Socket mit einem zufälligen Port an, um eine ausgehende Verbindung aufbauen zu können. Das Betriebssystem weist in der Regel eine zufällige Portnummer ≥ 49.152 zu, da es in diesem Bereich keine registrierten Ports gibt.



# 

Standard-ports

Die Internet Assigned Numbers Authority (IANA) registriert und verwalgt die Zuordnung von Portnummern zu Netzwerkdiensten. Es gibt zwei Hauptkategorien von Portnummern: Well Known Ports und Registered Ports.

## Well Known Ports

Die Well Known Ports sind im Bereich von 0 bis 1023 (0 bis 210 − 1) registriert und werden von Systemprozessen verwendet, die breit genutzte Netzwerk-Dienste anbieten. Diese Ports sind für alle bekannt und festgelegt. Einige Beispiele für Well Known Ports sind:

- Port 21: FTP (File Transfer Protocol)
- Port 25: SMTP (Simple Mail Transfer Protocol)
- Port 53: DNS (Domain Name System)
- Port 80: HTTP (Hypertext Transfer Protocol)

## Registered Ports

Die Registered Ports sind im Bereich von 1024 bis 49151 (210 bis 215 + 214 − 1) registriert und werden von IANA für bestimmte Dienste zugewiesen, wenn eine Anfrage von einem Antragsteller stammt. Diese Ports können von normalen Nutzern ohne besondere Rechte verwendet werden.

Einige Beispiele für Registered Ports sind:

- Port 2535: Multicast Address Dynamic Client Allocation Protocol (MADCAP)
- Port 5025: scpi-raw (Standard Commands for Programmable Instruments)
- Port 5044: Lumberjack Protocol (Filebeats/Logstash)

## Dynamische Ports

Ports ab 49152 und höher sind dynamisch und werden nicht von IANA vergeben. Jede Anwendung kann einen solchen Port lokal oder global verwenden. Es kann jedoch vorkommen, dass einer dieser Ports bereits belegt ist.

Insgesamt gibt es über 65.000 mögliche Portnummern, von denen einige für bestimmte Netzwerkdienste reserviert sind, während andere dynamisch verwendet werden können. Es ist wichtig, dass Anwendungen und Systeme die richtigen Portnummern verwenden, um Konflikte zu vermeiden und die Kommunikation über das Internet zu ermöglichen.