- **Kerndefinition:** Ein **SRV-Record (Service Record)** ist ein Eintragstyp im Domain Name System (DNS), der detaillierte Informationen über den Standort von Servern für einen bestimmten Netzwerkdienst bereitstellt. Er ermöglicht es einem Client, einen Dienst zu finden, ohne den genauen Hostnamen des Servers kennen zu müssen, und unterstützt dabei Priorisierung und Lastverteilung.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Aufbau und Prozess:** Eine Anfrage für einen SRV-Record hat das Format `_service._proto.name` (z. B. `_sip._tcp.example.com`). Die Antwort enthält mehrere Informationen:
        
        - **Priorität:** Ein niedrigerer Wert wird bevorzugt. Clients versuchen immer zuerst, den Server mit der niedrigsten Prioritätsnummer zu erreichen (z. B. für primäre und Backup-Server).
            
        - **Gewichtung (Weight):** Dient der Lastverteilung zwischen Servern mit derselben Priorität. Ein Server mit höherem Gewicht erhält prozentual mehr Anfragen.
            
        - **Port:** Die Portnummer, auf der der Dienst auf dem Zielserver läuft.
            
        - **Ziel (Target):** Der tatsächliche Hostname des Servers, der den Dienst anbietet.
            
    - **Anwendungsfälle:** SRV-Records sind entscheidend für Protokolle wie **SIP** und **XMPP** (VoIP und Instant Messaging), **LDAP** und insbesondere für **Microsoft Active Directory**, wo Clients Domänencontroller über SRV-Records finden.
        
- **Einordnung in den Gesamtkontext:** Der SRV-Record ist ein spezifischer Typ von **Resource Record (RR)**, der die Funktionalität von einfacheren Einträgen wie A- oder CNAME-Records erweitert. Während ein A-Record nur einen Namen auf eine IP-Adresse abbildet, fügt der SRV-Record die Konzepte von Dienst, Protokoll, Port, Priorität und Gewichtung hinzu, was eine wesentlich flexiblere Dienstarchitektur ermöglicht.
    
- **Sicherheitsaspekte:** Wie alle DNS-Einträge sind auch SRV-Records anfällig für Spoofing- und Cache-Poisoning-Angriffe, wenn das Netzwerk nicht durch **DNSSEC** geschützt ist. Ein Angreifer könnte einen Client durch manipulierte SRV-Einträge auf einen bösartigen Server umleiten, um beispielsweise Anmeldeinformationen abzufangen oder VoIP-Gespräche mitzuhören.
    
- **Praxisbeispiel / Analogie:** Stellen Sie sich vor, Sie rufen die Zentrale einer großen Firma an. Ein A-Record wäre die direkte Durchwahl zu einem bestimmten Mitarbeiter. Ein SRV-Record ist wie die Frage an die Vermittlungszentrale: "Ich möchte mit der Buchhaltung (_service) über das Telefon (_proto) sprechen." Die Vermittlung antwortet: "Nehmen Sie Frau Meier (Priorität 10, Ziel 1), sie ist die Chefin. Wenn sie nicht da ist, nehmen Sie Herrn Schmidt (Priorität 20, Ziel 2). Beide erreichen Sie unter der Durchwahl -500 (Port)."
    
- **Fazit / Bedeutung für IT-Profis:** Für Administratoren, die Dienste wie Active Directory, VoIP-Systeme oder andere moderne Netzwerkprotokolle verwalten, ist das Verständnis und die korrekte Konfiguration von SRV-Records unerlässlich. Sie sind ein Schlüsselmechanismus für die Ausfallsicherheit und Skalierbarkeit von Diensten und eine häufige Fehlerquelle, wenn sie nicht korrekt eingerichtet sind.