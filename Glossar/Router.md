- **Kerndefinition:** Ein **Router** ist ein Netzwerkgerät, das auf der Vermittlungsschicht (Layer 3) des OSI-Modells arbeitet. Seine Hauptaufgabe ist es, Datenpakete zwischen verschiedenen Computernetzwerken zu empfangen, ihre Ziel-IP-Adresse zu analysieren und sie auf dem besten Weg zum Zielnetzwerk weiterzuleiten. Router sind die fundamentalen Geräte, die das Internet und andere große Netzwerke miteinander verbinden.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess (Routing):** Ein Router pflegt eine **Routing-Tabelle**, die wie eine Wegbeschreibung für Netzwerke funktioniert. Wenn ein Paket ankommt, prüft der Router die Ziel-IP-Adresse des Pakets, schlägt in seiner Routing-Tabelle den besten Weg (den nächsten Hop) zum Zielnetz nach und leitet das Paket an die entsprechende Schnittstelle (Port) weiter.
        
    - **Wegfindung:** Die Routing-Tabelle kann manuell durch **statische Routen** oder automatisch durch **dynamische Routing-Protokolle** (wie OSPF oder BGP) aufgebaut werden.
        
    - **Schlüsselfunktionen:**
        
        - **Netzwerktrennung:** Router trennen **Broadcast-Domänen**. Ein Broadcast, der in einem Netzwerksegment gesendet wird, wird vom Router nicht in andere Segmente weitergeleitet.
            
        - **Adressübersetzung (NAT):** Viele Router, insbesondere im Heimbereich, führen eine Network Address Translation durch, um mehrere Geräte mit privaten IP-Adressen über eine einzige öffentliche IP-Adresse mit dem Internet zu verbinden.
            
- **Einordnung in den Gesamtkontext:** Der Router ist intelligenter als Geräte auf den unteren Schichten:
    
    - Im Gegensatz zum **Hub** oder **Repeater** (Layer 1) analysiert er Adressen.
        
    - Im Gegensatz zum **Layer-2-Switch**, der Geräte innerhalb _eines_ Netzwerks basierend auf MAC-Adressen verbindet, verbindet der Router _verschiedene_ Netzwerke basierend auf IP-Adressen. Ein **Layer-3-Switch** kombiniert die Funktionen beider Geräte.
        
- **Sicherheitsaspekte:** Als Gerät, das an der Grenze zwischen Netzwerken steht (z. B. zwischen dem internen LAN und dem Internet), ist der Router eine zentrale Komponente der Netzwerksicherheit. Er ist der natürliche Ort für die Implementierung einer **Firewall** mithilfe von **Access Control Lists (ACLs)**, um den ein- und ausgehenden Verkehr zu filtern. Die Absicherung des Routers selbst (sichere Passwörter, aktuelle Firmware, Deaktivierung unnötiger Dienste) ist von entscheidender Bedeutung, da eine Kompromittierung des Routers einem Angreifer die Kontrolle über den gesamten Netzwerkverkehr ermöglichen würde.
    
- **Praxisbeispiel / Analogie:** Ein Router ist wie eine große Postverteilstelle an einer Autobahnkreuzung. Jedes Paket (Datenpaket) hat eine Zieladresse (IP-Adresse). Die Mitarbeiter der Verteilstelle (der Router) schauen auf die Postleitzahl (das Zielnetzwerk) und wissen genau, auf welche Autobahn (welche Schnittstelle) sie das Paket legen müssen, damit es seiner Zieldestination näherkommt.
    
- **Fazit / Bedeutung für IT-Profis:** Für Netzwerk-Ingenieure ist die Konfiguration und Verwaltung von Routern eine Kernaufgabe. Das Verständnis von IP-Adressierung, Subnetting und Routing-Protokollen ist die Grundlage für den Aufbau und Betrieb jeglicher Art von vernetzter IT-Infrastruktur. Vom kleinen Heimrouter bis zum massiven Core-Router, der das Rückgrat des Internets bildet, ist der Router das entscheidende Gerät, das die globale Kommunikation ermöglicht.