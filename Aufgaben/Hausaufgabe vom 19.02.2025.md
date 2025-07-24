
1. Beschreibe die Unterschiede zwischen cmdlets, Skripten und Modulen in PowerShell 

     Antwort: 
     Cmdlets: Das sind ein Befehle, die bestimmte Aufgaben ausführen. Sie bestehen aus einem Verb und einem Substantiv zb " get-help" 

       Skripte: sind Textdateien mit mehreren  
        Befehlen, die nacheinander ausgeführt 
        werden.
        Sie enden mit ".ps1" und können so 
        komplexere Aufgaben erledigen
 
      Module: Das sind Sammlungen von Cmdlets und Funktionen, die zusammengehören
      
Cmdlets sind einzelne Befehle, Skripte sind Befehlsfolgen, und Module sind größere Pakete mit vielen Funktionen.



2. Erkläre das Konzept der PowerShell-Pipelines und nenne ein Beispiel für die Verkekttung mehrerer Befehle. 

        Antwort:
         Pipelines sind eine Möglichkeit, mehrere
          Befehle miteinander zu verbinden.
           Dabei wird die Ausgabe eines Befehls als
            Eingabe für den nächsten Befehl 
            verwendet.
            Man benutzt dafür das Zeichen |
             zwischen den Befehlen
          
      Beispiel:
        
	```powershell
	Get-Process | Where-Object { $_.name -eq "iexplore" } | Format-Table ProcessName, WorkingSet
	
	 ````
	
    
	-  betrachtet alle laufenden Prozesse
      - Filtert dann nur den Internet Explorer-Prozess heraus
      - Zeigt am Ende den Prozessnamen und den Arbeitsspeicher in einer Tabelle


3. Welche vier Schritte umfasst der DHCP-Handshake (DORA-Prozess) und was passiert in jedem Schritt? 

Antwort 

       Der DHCP-Handshake, auch DORA-Prozess genannt,
     besteht aus vier Schritten.
          1. Discover (Entdecken): Der Computer 
           sendet eine Anfrage ins Netzwerk,
          um einen DHCP-Server zu finden
           
           2.Offer (Angebot): Der DHCP-Server 
           antwortet mit einem Angebot für eine 
           IP-Adresse und andere 
           Netzwerkeinstellungen
           
           3.Request (Anforderung): Der Computer 
           wählt ein Angebot aus und bittet um die 
           angebotene Ip und Einstellungen
           
           4.Acknowledge (Bestätigung): Der DHCP-
           Server bestätigt die Anforderung und 
           der Computer kann die Einstellungen nutzen

Dieser Prozess sorgt dafür, dass jeder Computer im Netzwerk automatisch die richtigen Einstellungen bekommt, ohne dass man sie manuell eingeben muss.

4. Welche Parameter kann ein DHCP-Server neben der IP-Adresse noch an Clients übermitteln? 

    1. Netzmaske: Legt fest, welcher Teil der IP-Adresse zum Netzwerk gehört.
    
    2. Gateway-Adresse: Die Adresse des Routers für den Internetzugang.
    
    3. DNS-Server-Adressen: Für die Umwandlung von Domainnamen in IP-Adressen.
    
    4. Rechnername: Ein Name für den Client 
      im Netzwerk.
    
    5. Lease-Zeit: Wie lange die zugewiesene 
      IP- Adresse gültig ist.
    
    6. Broadcast-Adresse: Für Nachrichten an alle Geräte im Netzwerk.



5. Welche DNS-Record-Typen gibt es und welche Funktion haben A, AAAA, CNAME, MX und TXT Records? 
 
      A-Record: Verknüpft einen Domainnamen mit einer IPv4-Adresse

      AAAA-Record: Verbindet einen Domainnamen mit einer IPv6-Adresse
      
      CNAME-Record: Erstellt einen Alias für eine Subdomain, der auf eine andere Domain verweist (www.heise.de -> heise.de)
    
     MX-Record: Gibt den Mailserver für eine Domain an
     
     TXT-Record: Enthält frei wählbaren Text, oft für Verwaltungsdaten oder SPF-Einträge verwendet


6. Erkläre den Unterschied zwischen einer OU (OrganizaƟonal Unit), einer Gruppe und einer Domäne in AD. 
     Unterschiede:
    
	 OUs dienen der Struktur und Verwaltung, Gruppen der Rechtevergabe, und Domänen bilden die übergeordnete Organisationseinheit im Netzwerk
     
     Organisationseinheit (OU):
    - Ein Teilbereich innerhalb einer Domäne
        
    - Dient zur logischen Gruppierung von Objekten
        
    - Ermöglicht die Anwendung von Gruppenrichtlinien
        
    - Erlaubt die Delegation von Verwaltungsrechten
        
        Gruppe:
    - Sammlung von Benutzern oder Computern
        
    - Wird für die Zuweisung von Berechtigungen verwendet
        
    - Erleichtert die Verwaltung von Zugriffsrechten
        
     Domäne:
    - Grundlegende Einheit in Active Directory
        
    - Enthält alle Objekte wie Benutzer, Computer und Gruppen
        
    - Wird von Domänencontrollern verwaltet
        
    - Bildet die Basis für die Netzwerkverwaltung
 
7. Welche Bedeutung haben die OSI-Schichten, und was passiert auf Layer 3 (Netzwerkschicht)? 
     Das OSI-Modell teilt die Netzwerkkommunikation in 7 Schichten auf, um sie verständlicher und standardisiert zu machen.  und erleichtert die Fehlersuche in Netzwerken 

   Layer 3, die Netzwerkschicht, hat folgende Hauptaufgaben:

8. Adressierung: Vergibt logische Adressen an die Geräte im Netzwerk.
    
2. Routing: Findet den besten Weg für Datenpakete im  Netzwerk.
    
3. Paketierung: Verpackt Daten in Pakete für den Transport.
    
4. Fragmentierung: Teilt große Datenpakete in kleinere Stücke auf
    

Diese Schicht ermöglicht die Kommunikation über verschiedene Netzwerke hinweg und ist entscheidend für den Datentransport  



8.  Eines der Routting Protokolle ist STP (Spanning Tree Protocol). Es existieren zwei Hauptaufgaben von STP. Finde sie heraus und erkläre diese. 
      Das Spanning Tree Protocol (STP) hat zwei Hauptaufgaben:

     1. Schleifenverhinderung: STP verhindert Schleifen in Netzwerken mit redundanten Pfaden. Es deaktiviert überflüssige Verbindungen, um endlose Weiterleitungen von Datenpaketen zu vermeiden
     
     2. Verhindert Broadcaststürme 
     
     Diese Aufgaben sorgen für ein stabiles und effizientes Netzwerk, indem sie Broadcast-Stürme verhindern und gleichzeitig die Verfügbarkeit durch redundante Pfade sicherstellen


9. Was ist der Zweck von Subneƫting, und welche Vorteile bringt es? 
     Subnetting teilt ein großes Netzwerk in kleinere Teilnetze auf. Die Hauptvorteile sind:

    1. Bessere Leistung: Reduziert Netzwerkverkehr und verbessert die Geschwindigkeit.
    
    2. Erhöhte Sicherheit: Ermöglicht die Isolierung sensibler Bereiche.
    
    3. Effiziente Ressourcennutzung: Optimiert die Verwendung von IP-Adressen.
    
    4. Vereinfachte Verwaltung: Erleichtert die Organisation und Fehlerbehebung im Netzwerk.
    
    5. Skalierbarkeit: Ermöglicht flexibles Wachstum des Netzwerks.
    

Subnetting hilft Unternehmen, ihre Netzwerke effizienter, sicherer und anpassungsfähiger zu gestalten




10. Wie viele Hosts können in einem Netzwerk mit der Subnetzmaske 255.255.255.240 existieren?

    In einem Netzwerk mit der Subnetzmaske 255.255.255.240 können 14 Hosts existieren
    
    Diese Subnetzmaske entspricht einem /28 CIDR-Präfix und bietet insgesamt 16 IP-Adressen.
     
    Davon sind jedoch zwei reserviert: eine für die Netzwerkadresse und für die Broadcast-Adresse. 
    
    !!Daher bleiben 14 nutzbare Adressen für Hosts übrig.!!