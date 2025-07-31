- **Kerndefinition:** **Multicast** ist eine Methode zur Datenübertragung in einem Computernetzwerk, bei der ein einzelnes Datenpaket von einem Sender an eine definierte Gruppe von Empfängern gesendet wird. Es ist eine Form der Eins-zu-Viele-Kommunikation, die die Netzwerklast im Vergleich zum Senden mehrerer einzelner Pakete erheblich reduziert.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Ein Sender adressiert seine Pakete an eine spezielle **Multicast-IP-Adresse** (im Bereich 224.0.0.0 bis 239.255.255.255). Empfänger, die diesen Datenstrom erhalten möchten, "abonnieren" die Gruppe mithilfe des **IGMP (Internet Group Management Protocol)**. Router im Netzwerk leiten die Multicast-Pakete dann nur an die Netzwerksegmente weiter, in denen sich mindestens ein abonnierender Empfänger befindet.
        
    - **Zweck:** Der Hauptzweck ist die Effizienz. Anstatt dass ein Server bei einem Videostream an 100 Empfänger 100 separate Streams senden muss (Unicast), sendet er nur einen einzigen Stream (Multicast), der von der Netzwerkinfrastruktur intelligent vervielfältigt und verteilt wird.
        
- **Einordnung in den Gesamtkontext:** Multicast ist eine von drei grundlegenden Übertragungsarten im IP-Netzwerk:
    
    - **Unicast:** Eins-zu-Eins-Kommunikation (z. B. eine Webseite aufrufen).
        
    - **Broadcast:** Eins-zu-Alle-Kommunikation innerhalb eines Subnetzes (z. B. eine DHCP-Anfrage).
        
    - **Multicast:** Eins-zu-Viele-Kommunikation (z. B. IPTV, Online-Gaming, Videokonferenzen).
        
- **Sicherheitsaspekte:** Die Verwaltung von Multicast-Verkehr erfordert eine sorgfältige Konfiguration, um eine Überlastung des Netzwerks zu vermeiden (sogenannte "Multicast-Stürme"). Aus Sicherheitssicht muss sichergestellt werden, dass nur autorisierte Geräte einer Multicast-Gruppe beitreten können, um unbefugtes Mithören zu verhindern. In vielen Unternehmensnetzwerken wird Multicast-Verkehr aus Sicherheits- und Stabilitätsgründen standardmäßig eingeschränkt oder blockiert und muss explizit für bestimmte Anwendungen freigegeben werden.
    
- **Praxisbeispiel / Analogie:** Stellen Sie sich einen Radiosender vor. Der Sender (Server) strahlt sein Programm auf einer bestimmten Frequenz (Multicast-Adresse) aus. Jeder, der ein Radio besitzt (ein netzwerkfähiges Gerät), kann diese Frequenz einstellen (der Gruppe beitreten) und das Programm hören (den Datenstrom empfangen). Der Radiosender muss sein Programm nicht einzeln an jeden Hörer persönlich schicken.
    
- **Fazit / Bedeutung für IT-Profis:** Für Netzwerkadministratoren ist Multicast eine leistungsstarke, aber komplexe Technologie. Das Verständnis von IGMP und PIM (Protocol Independent Multicast) ist für die Konfiguration und Fehlerbehebung von Multicast-Anwendungen wie IPTV, Videokonferenzsystemen oder der Verteilung von Finanzdaten unerlässlich. Eine korrekte Implementierung kann die Netzwerkleistung drastisch verbessern, während eine fehlerhafte Konfiguration zu erheblichen Problemen führen kann.