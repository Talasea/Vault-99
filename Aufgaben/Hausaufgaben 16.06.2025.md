1. Welche Kenntnisse über das Netzwerk oder das Endgerät kannst du aus folgenden IP-Adressen gewinnen? 
          10.200.200.18/16, Broadcast 10.200.255.255      
                  gehört zum privaten Adressbereich
                          https://www.rfc-editor.org/rfc/rfc1918 
                    
                 Die CIDR-Notation /16 bedeutet, dass die ersten 16 Bits für das                     Netzwerk reserviert sind, was einer Subnetzmaske von 
                     255.255.0.0 entspricht

             Das Netzwerk 10.200.0.0/16 kann insgesamt 65.534 Host-Adressen 
             verwalten (2^16 - 2, abzüglich Netzwerk- und Broadcast-Adresse)



         localhost 
                  "localhost" ist ein Hostname, der standardmäßig auf die IP-
                   Adresse 127.0.0.1 aufgelöst wird

                   Diese Adresse gehört zum Loopback-Adressbereich 127.0.0.0/8, 
                   der für interne Kommunikation auf demselben Gerät reserviert
                    ist

                 Der Loopback-Mechanismus ermöglicht es Anwendungen, mit sich 
                 selbst oder anderen Prozessen auf demselben System zu 
                 kommunizieren, ohne das physische Netzwerk zu beanspruchen

                 In IPv6-Umgebungen entspricht localhost der Adresse ::1

             

         0.0.0.0 

                    Die IP-Adresse 0.0.0.0 ist eine reservierte IPv4-Adresse mit 
                    spezieller Bedeutung gemäß RFC 5735

                 Diese Adresse wird häufig als Standardroute in Routing-Tabellen 
                 verwendet, um anzuzeigen, dass Pakete an das Default Gateway 
                 weitergeleitet werden sollen

                 




         192.168.2.105 
                  Basierend auf üblichen Konfigurationspraktiken ist anzunehmen, 
                  dass diese Adresse zu einem /24 Subnetz 192.168.2.0/24 gehört

                   Dies würde 254 verfügbare Host-Adressen 192.168.2.1 bis 
                   192.168.2.254 ermöglichen.


         192.168.0.1 
                   192.168.0.1 ist eine der am häufigsten verwendeten Standard-
                   Gateway-Adressen für Router und andere Netzwerkgeräte
                   und gehört zum Privaten Adressbereich

                   Über diese Adresse können Benutzer auf die admin
                   Weboberfläche des Routers zugreifen 
           
                   Consumer-Router 

					
                   
2) 2.Im Rahmen eines Netzwerkscans, der sowohl nach IPv4, als auch nach IPv6 Adressen sucht, werden ausschließlich IPv4-Adressen gefunden. Ihr wisst allerdings, dass auch IPv6 verwendet wird. Woran könnte das liegen? 

                  dem scan nicht angewiesen ipv6 mit abzudecken 
                  IPv6-Netzwerkscans funktionieren grundlegend anders als IPv4-
                  Scans.  Während IPv4-Netzwerke oft per Brute-Force durchsucht 
                  werden können, ist dies bei IPv6 aufgrund des enormen 
                  Adressraums (2^64 Adressen in einem /64-Netz) praktisch 
                  unmöglich
   
3) 3.Recherchiere und erkläre, wie 'Tunneling' zwischen IPv4 und IPv6 funktioniert.

                  IPv6-Tunneling funktioniert durch die Kapselung (Encapsulation) von 
         IPv6-Datenpaketen in IPv4-Pakete, wodurch eine virtuelle 
         Punkt-zu-Punkt-Verbindung zwischen zwei IPv6-Knoten über ein 
         IPv4-Netzwerk entsteht

             der Prozess besteht aus drei wesentlichen Schritten:
             1. Eingangsknoten des Tunnels: Erstellt einen kapselnden IPv4-Header 
               und überträgt das gekapselte Paket
    
             2. Übertragung: Das gekapselte Paket wird durch das 
               IPv4-Netzwerk geroutet
    
             3. Ausgangsknoten des Tunnels: Empfängt das gekapselte Paket,
                entfernt den IPv4-Header und verarbeitet das ursprüngliche 
                 IPv6-Paket weiter

4) 4.Befindet sich die jeweilige IP im gegebenen Subnetz? 

       1) IP: 214.80.54.2, Subnetz: 172.30.148.16/24            nein         
       2) IP:192.168.178.5, Subnetz: 192.168.178.2/32           nein 
       3) IP:192.168.178.105, Subnetz: 192.168.178.0/24          ja
       4) IP: 10.9.0.0, Subnetz: 10.8.0.0/12                     ja
       5) IP: 10.0.0.254, Subnetz: 10.0.0.0/24                   ja
       6) IP: 172.16.5.32, Subnetz: 172.16.5.0/27               nein


 


6. Privatanwender können in der Regel keine statischen IPs beziehen. Informiere dich über DynDNS und erkläre die Funktionsweise.

     Als Privatanwender kann man in der Regel keine statische IP-Adresse von seinem Internetanbieter beziehen. Hier kommt DynDNS (Dynamic Domain Name System) ins Spiel, ein Dienst, der dieses Problem elegant löst.

     DynDNS ermöglicht es, Ihren Heimanschluss, der alle 24 Stunden eine neue, dynamische IP-Adresse erhält, trotzdem dauerhaft unter einem festen und leicht zu merkenden Domainnamen (z.B. `mein-zuhause.dyndns.org`) erreichbar zu machen.

      Funtkion:
      - **Meldung:** Ihr Router bemerkt, dass er eine neue IP-Adresse von Ihrem Internetanbieter bekommen hat.
      - **Update:** Der Router meldet diese neue IP-Adresse automatisch an den DynDNS-Dienst.
     - **Verknüpfung:** Der Dienst aktualisiert seinen Eintrag sofort, sodass Ihr fester Name nun auf die neue IP-Adresse zeigt.



7. Recherchiere Ethernet- und TCP Frames. Beschreibe den Aufbau des TCP-Headers. Wozu dienen sogenannte "Flags" und welche TCP-Flags gibt es? 

          Zweck und Arten der TCP-Flags

         Sogenannte **Flags** sind einzelne Bits im TCP-Header, die als Schalter             dienen, um bestimmte Zustände oder Informationen über die Verbindung zu             signalisieren. Sie steuern den Auf- und Abbau sowie den Verlauf einer               Verbindung.

         Es gibt hauptsächlich sechs wichtige Flags:

         - SYN (Synchronize):** Wird nur beim Verbindungsaufbau (Drei-Wege-                    Handschlag) genutzt, um die Sequenznummern zu synchronisieren.
         - ACK (Acknowledgement):** Zeigt an, dass die Bestätigungsnummer im Header            gültig ist. Nach dem Verbindungsaufbau ist dieses Flag bei fast allen               Paketen gesetzt.
         - FIN (Finish):** Signalisiert dem Gegenüber, dass der Sender keine 
         weiteren Daten mehr senden wird und die Verbindung geordnet beenden                 möchte.
         - RST (Reset):** Setzt die Verbindung abrupt zurück. Dies geschieht bei
         Fehlern oder wenn ein Paket an einen Port gesendet wird, der nicht auf 
         eine Verbindung wartet.
        - PSH (Push):** Weist den Empfänger an, die Daten sofort an die Anwendung
         weiterzugeben und nicht zu puffern.
        - URG (Urgent):** Zeigt an, dass das Paket "dringende" Daten enthält, die             vom Empfänger vorrangig verarbeitet werden sollen.




          Aufbau des TCP-Headers

Der **TCP-Header** ist die Steuerzentrale für die TCP-Verbindung. Er hat eine Mindestgröße von **20 Bytes** und enthält die folgenden Felder:

- **Quell-Port** (16 Bit): Portnummer der Anwendung auf dem sendenden Gerät.
- **Ziel-Port** (16 Bit): Portnummer der Anwendung auf dem empfangenden Gerät.
- **Sequenznummer** (32 Bit): Eine Nummer, die die Reihenfolge der Datenpakete sicherstellt, damit der Empfänger sie wieder korrekt zusammensetzen kann.
- **Bestätigungsnummer (Acknowledgement Number)** (32 Bit): Bestätigt den Empfang von Datenpaketen. Sie enthält die Sequenznummer des nächsten erwarteten Datenbytes.
- **Data Offset** (4 Bit): Gibt die Länge des TCP-Headers in 32-Bit-Wörtern an, um zu wissen, wo die eigentlichen Nutzdaten beginnen.
- **Reserviert** (6 Bit): Für zukünftige Verwendungen reserviert und standardmäßig auf null gesetzt.
- **Flags** (6 Bit): Steuerbits zur Verwaltung der Verbindung.
- **Fenstergröße (Window Size)** (16 Bit): Dient der Flusskontrolle. Der Empfänger teilt dem Sender mit, wie viele Daten er noch empfangen kann.
- **Prüfsumme** (16 Bit): Dient zur Erkennung von Übertragungsfehlern im Header und in den Nutzdaten.
- **Urgent Pointer** (16 Bit): Zeigt auf dringende Daten, die vorrangig behandelt werden sollen (nur wenn das URG-Flag gesetzt ist).
- **Optionen** (variabel): Optionale Felder für erweiterte Funktionen wie die maximale Segmentgröße (MSS).





8. Ihr bekommt den Auftrag, einen Router so zu konfigurieren, dass alle 5 Geräte im Heimnetz ihre eigene Website unter Port 80/443 betreiben können. Der Kunde möchte alle Geräte parallel betreiben und wünscht sich daher eine Skizze, wie eure Lösung aussehen wird.



Einrichten eines Reverse Proxy 

- **Einrichtung eines Reverse Proxy:** Ein Gerät im Netzwerk (z. B. ein kleiner Server wie ein Raspberry Pi oder eine NAS, die Docker unterstützt) wird als Reverse Proxy konfiguriert. Wir empfehlen hierfür eine schlanke Software wie **NGINX Proxy Manager** oder **Traefik**, da diese einfach zu verwalten sind.
- **Router-Konfiguration (Port-Weiterleitung):** Im Router werden die Ports **80 (HTTP)** und **443 (HTTPS)** nicht mehr auf die einzelnen Geräte, sondern **ausschließlich** auf die IP-Adresse des Reverse Proxy weitergeleitet.
- **DNS-Konfiguration:** Für jedes der fünf Geräte muss eine eigene Subdomain eingerichtet werden (z. B. `gerät1.ihredomain.de`, `gerät2.ihredomain.de` usw.). Alle diese Subdomains müssen auf die **eine öffentliche IP-Adresse** Ihres Internetanschlusses zeigen.
- **Reverse Proxy Konfiguration:** Im Reverse Proxy wird für jede Subdomain eine Regel erstellt. Diese Regel legt fest, an welche interne IP-Adresse des jeweiligen Geräts die Anfrage weitergeleitet werden soll. Der Reverse Proxy kümmert sich auch um die SSL-Zertifikate (Let's Encrypt), sodass jede Seite sicher über HTTPS erreichbar ist.