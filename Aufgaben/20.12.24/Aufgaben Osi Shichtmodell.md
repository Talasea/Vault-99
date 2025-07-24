  


#### Warum werden die Schichten des OSI-Modells in "Transport orientiert" und "Anwedungsorientiert" unterteilt?

![](https://lwfiles.mycourse.app/65ad12b06e5c564383a8e54b-public/c915a619917221d7b19b4f14400776c1.png)

Die Schichten des osi Models werden In Transport orientiert und Anwednugsorientiert unterteilt weil  unterschiedliche Funktionen und Aufgaben erfüllen.  
  
Die Tranzport-Schichten sich auf die Übertragung von Daten zwischen zwei Endgeräten über ein Netzwerk, unabhängig von der Anwendung, die die Daten sendet oder empfängt.  
  
Schicht 1 : Bitübertragungsschicht (Physical Layer)         
   
  
Schicht 2: Sicherungsschicht (Data Link Layer)  
   
  
Schicht3: Vermittlungsschicht (Network Layer)  
  
Schicht 4: Transportsschicht (Transport Layer)  
  
Die Anwendungsorientierte Schicht  konzentrieren sich auf die Kommunikation zwischen Anwendungen und die Übersetzung von Daten in eine Format, die von der Anwendung verstanden werden kann.  
  
Schicht 5: Sitzungsschicht (Session Layer)  
Schicht6 : Darstellungsschicht (Presentation Layer)  
Schicht 7: Anwendungsschicht (Application Layer)




#### Beschreibe in einigen Sätzen, welchen Weg ein Datenpaket gehen muss, um von einer Anwendung auf deinem Computer zu einer Anwendung eines anderen, lokalen Computer zu gelangen. Berücksichtige dabei auch die Verbindungsart zwischen den Computern.

![](https://lwfiles.mycourse.app/65ad12b06e5c564383a8e54b-public/fa5ac03208ecb300f8d14cc876954f69.png)

Ein Datenpaket muss von einer Anwendung auf deinem Computer über das lokale Netzwerk zu einer Anwendung auf einem anderen Computer gelangen. Dazu wird das Datenpaket in kleinere Pakete zerlegt und mit Steuerdaten für die Adressierung, Sendefolge und Fehlerkorrektur versehen.   
Die Pakete werden dann über eine Verbindungsart vom Ausgangs Rechner über zB Lan oder Wlan übertragen , dabei werden Mögliche Verbindungs -Punkte passiert (zB. switch , router Server ect )passiert.   
Sobald die Datenpakete beim ziel ankommen werden die in umgekehrter Reihenfolge wieder verarbeitet.







#### Nenne für jede Schicht eine Anwednung oder ein Protokoll, dass auf dieser Schicht kommuniziert und erkläre die Kommunikation zu den angrenzenden Schichten.

![](https://lwfiles.mycourse.app/65ad12b06e5c564383a8e54b-public/0aa2d5e8f21d9d92213142a519b2fd26.jpg)

Schicht 1: Bitübertragungsschicht (Physical Layer)   Protokoll: Ethernet, Wi-Fi, FDDI (Fiber Distributed Data Interface)Kommunikation: Die Bitübertragungsschicht überträgt die Bits eines Datenpakets über ein bestimmtes Übertragungsmedium (z.B. Kabel, Funk,)  
  
Schicht 2: Datenverlinkungsschicht (Data Link Layer) Protokoll: Ethernet II, PPP (Point-to-Point Protocol), HDLC (High-Level Data Link Control)Kommunikation:  
Die Datenverlinkungsschicht verantwortet die logische Verbindung zwischen zwei Geräten über ein bestimmtes Übertragungsmedium.   
  
  
Schicht 3: Netzwerksschicht (Network Layer)  Protokoll: IP (Internet Protocol), ICMP(Internet Control Message Protocol)Kommunikation: Die Netzwerksschicht verantwortet die Logik der Netzwerkverbindung und definiert die Adressierung von Geräten innerhalb eines Netzwerks.  
  
  
Schicht 4: Transportsschicht (Transport Layer) Protokoll: TCP (Transmission Control Protocol), UDP (User Datagram Protocol), SCTP (Stream Control Transmission Protocol) Kommunikation: Die Transportsschicht verantwortet die Zuordnung von Daten zu einer bestimmten Anwendung auf einem Rechner.  
  
Schicht 5: Sitzungsschicht (Session Layer) Protokoll: NetBIOS, SSH (Secure Shell), SSL/TLS (Secure Sockets Layer/Transport Layer Security)  Kommunikation: Die Sitzungsschicht verantwortet die logische Verbindung zwischen zwei Anwendungen auf verschiedenen Geräten.  
  
Schicht 6: Präsentationschicht (Presentation Layer) Protokoll:  SNMP (Simple Network Management Protocol) Kommunikation: Die Präsentationschicht verantwortet die Formatierung und Kodierung von Daten, um sie für eine bestimmte Anwendung auf einem Rechner verständlich zu machen.   
  
Schicht 7: Anwendungsschicht (Application Layer)  Protokoll: HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), SMTP (Simple Mail Transfer Protocol)Kommunikation: Die Anwendungsschicht verantwortet die direkte Kommunikation zwischen Anwendungen auf verschiedenen Geräten.  
  

#### Beim TCP/IP-Referenzmodell werden Schicht 1 und 2 zusammengefasst. Welchen Grund könnte es dafür geben? Wäre das auch sinnvoll beim OSI-Modell?

Insgesamt ist die Zusammenfassung von Schicht 1 und 2 bei TCP/IP-Referenzmodell eine praktische und einfache Lösung, die die Komplexität reduziert und die Verwendung von TCP/IP erleichtert.  
  
Bei OSI-Modell ist jedoch eine klare Trennung und Abgrenzung zwischen den Schichten notwendig, um die Präzision und die Klarheit des Modells zu erhalten.  
  
Das OSI-Modell definiert sieben Schichten, die klar voneinander abgegrenzt sind. Eine Zusammenfassung von Schicht 1 und 2 würde die Klarheit und die Präzision des Modells beeinträchtigen  
.