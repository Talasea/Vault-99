Aufgabe 1: 

1.1 Erkläre: 
    Wie funktoniert der Domain Name Service? 
    Was sind DNS-Records? 
    Wieviel gibt es und wozu dienen sie?
    Was ist eine Forward Zone? 
    Was ist eine Reverse Zone? 

1.2 Was bedeutet FQDN? 
    Erkläre dies mit eigenen Worten. 

1.3 Erkläre die vier Schritte, die beim DHCP-Prozess durchlaufen werden. 

1.4 Erkläre DHCP-Failover. 

Aufgabe 2: 

2.1 Installiere Windows 2022 Server in der Std.-Editon mit grafischem UI

     . 2.2 Erstelle nach der Installation einen Prüfpunkt.
     
     
     


Antworten:

## 1.1 Der Domain Name Service funktioniert so das er numerische Ip-Adressen in lesbare Adressen umwandelt.
Das geschieht in verschiedenen schritten:

Wir senden eine anfrage an den Dns server 
 www.heise.de
  der Dns server  entschlüsselt diese zurück zu einer ip adresse in der Forward Zone
  und sendet diese anfrage dan raus bis zur  ziel Adresse 
  die sendet die gewünschten Informationen zurück an den Dns Server
  der nimmt diese in der revers Zone an und leitet sie für uns lesbar gemacht zum Clint weiter .

   Was sind DNS-Records? 
   
   DNS-Records sind Datensätze im DNS die DNS IP adressen zu ordnen und verscheidene Arten von Service Konfigurationen definieren.

## Wieviel gibt es und wozu dienen sie?


**A-Record**: Ordnet eine Domain einer 32-Bit-IPv4-Adresse zu und erleichtert so die Verbindung zwischen dem Domain-Namen und dem Server, auf dem die Website gehostet wird.

 **AAAA-Record**: Ordnet eine Domain einer 128-Bit-IPv6-Adresse zu und ermöglicht so die Verbindung zwischen dem Domain-Namen und dem Server, auf dem die Website in der IPv6-Architektur gehostet wird.

 **MX-Record**: Leitet E-Mails an den/die richtigen E-Mail-Server für eine Domain weiter, wobei die Priorität jedes Servers für den E-Mail-Empfang festgelegt wird.

**CNAME-Record**: Ermöglicht die Zuordnung mehrerer Domain-Namen zu derselben Server-IP-Adresse ohne zusätzliche A- oder AAAA-Records. Wird häufig für Subdomains wie „www“ oder „mail“ verwendet.
 
 **TXT-Record**: Stellt Textinformationen für externe Quellen bereit, die in der Regel für die Angabe von SPF-Daten, die Überprüfung von Domain-Inhabern und andere Sicherheitshinweise verwendet werden.

 **NS-Record**: Delegiert eine Domain oder Subdomäne an eine bestimmte Gruppe von DNS-Servern und gibt die für eine bestimmte DNS-Zone zuständigen autoritativen Nameserver an.

 **SRV-Record**: Gibt den Standort von Diensten an, einschließlich des Hostnamens und der Portnummer für bestimmte Dienste innerhalb von Domains, wie E-Mail oder VoIP.

 **SOA-Record**: Stellt wichtige Domaininformationen wie E-Mail-Kontakt und Aktualisierungsrate bereit.
  
 **CAA-Record**: Gibt an, welche Zertifizierungsstellen Zertifikate für eine Domain ausstellen können.

 **PTR-Record**: Ordnet eine IP-Adresse einer Domain zu, hauptsächlich für Reverse-DNS-Lookups.


## Was ist eine Forward Zone? 

Eine Forward Zone, ist ein bestandteil  des DNS. und dient dazu Domain namen (www.heise.de) 
in IP Adressen umzuwandeln.
Diese Umwandlung  ist entscheidend für die Kommunikation zwischen Geräten und Diensten in einem Netzwerk. Wenn ein Client eine bestimmte IP-Adresse für einen Domänennamen anfordert, konsultiert der DNS-Server seine Forward Zone, um die entsprechende IP-Adresse bereitzustellen.

Die Forward Zone enthält eine Zuordnung zwischen Hostnamen und IP-Adressen.
www.cnn.com hat die ip 157.166.255.19


### Was ist eine Reverse Zone? 

Die Reverse Zone hat die selbe Aufgabe wie die Forward Zone nur eben in umgekehrter Funktion.
Wandelt also IP adressen in den Hostnamen um .
Diese Zone ist wichtig für die Fehlerbehebung im Netzwerk, Sicherheitsanalysen und die umgekehrte Zuordnung von IP-Adressen zu den entsprechenden Domänennamen.

### 1.2 Was bedeutet FQDN? 

FQDN (Fully Qualified Domain Name) ist die vollständige und eindeutige Adresse einer Webseite und setzt sich aus dem Hostnamen und der Domain zusammen.

![[Pasted image 20250122153541.png]]

## 1.3 Erkläre die vier Schritte, die beim DHCP-Prozess durchlaufen werden. 

1. **Discover**: Der DHCP-Client sendet eine Broadcast-Nachricht (DHCPDISCOVER) ins Netzwerk, um einen DHCP-Server zu finden. Diese Nachricht hat die Quell-Adresse 0.0.0.0 und die Zieladresse 255.255.255.255, da der Client noch keine IP-Adresse besitzt und seine Anfrage an alle im Netzwerk richtet.
    
2. **Offer**: DHCP-Server im Netzwerk reagieren auf diese Anfrage mit einem DHCP-OFFER, das eine IP-Adresse und andere relevante Konfigurationsdetails enthält. Der Server sendet diese Nachricht an die MAC-Adresse des Clients.
    
3. **Request**: Der Client wählt eines der Angebote aus und sendet eine DHCP REQUEST-Nachricht zurück, um zu bestätigen, dass er die angebotene IP-Adresse akzeptiert. Diese Nachricht enthält die MAC-Adresse des Clients und die IP-Adresse, die der Client akzeptiert.
    
4. **Acknowledge**: Schließlich bestätigt der Server mit einer DHCP ACK-Nachricht (DHCPACK) die Zuteilung der IP-Adresse an den Client. Diese Nachricht beinhaltet die Konfigurationsparameter, die dem Client zugewiesen wurden.


## 1.4 Erkläre DHCP-Failover. 

DHCP-Failover ist eine Funktion, die es ermöglicht, zwei DHCP-Server zu koppeln, um eine höhere Verfügbarkeit und Ausfallsicherheit für den DHCP-Dienst zu gewährleisten.

![[Pasted image 20250122154428.png]]



Nun gibt es 2 verscheiden ansetze :

![[Pasted image 20250122154518.png]]



![[Pasted image 20250122154558.png]]
Hotstandby

Beide Server teilen denselben Adresspool und synchronisieren ihre Daten. Sollte einer der Server ausfallen, übernimmt der andere Server automatisch die Ausgabe von IP-Adressen und andere DHCP-Dienste.

