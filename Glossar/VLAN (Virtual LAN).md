- **Kerndefinition:** Ein **VLAN (Virtual Local Area Network)** ist eine Technik, um ein physisches Netzwerk logisch in mehrere, voneinander isolierte Teilnetze (Broadcast-Domänen) zu unterteilen. Geräte im selben VLAN können miteinander kommunizieren, als wären sie an einem einzigen, gemeinsamen Switch angeschlossen, auch wenn sie sich physisch an unterschiedlichen Switches befinden.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** An einem managebaren Switch werden die einzelnen Ports einer bestimmten VLAN-ID (z. B. 10, 20, 30) zugewiesen. Der Switch sorgt dafür, dass der Datenverkehr eines Ports nur an andere Ports mit derselben VLAN-ID weitergeleitet wird.
        
    - **Inter-VLAN-Routing:** Die Kommunikation _zwischen_ verschiedenen VLANs ist standardmäßig blockiert. Um sie zu ermöglichen, wird ein Gerät der Schicht 3 benötigt – typischerweise ein **Router** oder ein **Layer-3-Switch**, der als zentraler Kontrollpunkt agiert.
        
- **Einordnung in den Gesamtkontext:** VLANs sind eine Technologie der Schicht 2 (Sicherungsschicht) und ein fundamentaler Baustein für das Design moderner, skalierbarer Netzwerke. Sie ermöglichen die **Netzwerksegmentierung**, ohne dass dafür separate physische Hardware für jedes Segment angeschafft werden muss. Die Kommunikation über mehrere Switches hinweg wird durch **Trunking (802.1Q)** realisiert.
    
- **Sicherheitsaspekte:** Die Segmentierung durch VLANs ist eine der wichtigsten grundlegenden Sicherheitsmaßnahmen in einem Netzwerk. Sie dient dazu, die Angriffsfläche zu verkleinern und die seitliche Ausbreitung von Angriffen (Lateral Movement) zu verhindern. Indem man z. B. Gäste-WLAN, IoT-Geräte, Mitarbeiter-PCs und kritische Server in separate VLANs aufteilt, kann man den Zugriff zwischen diesen Zonen streng über eine Firewall kontrollieren.
    
- **Praxisbeispiel / Analogie:** Stellen Sie sich ein großes, offenes Bürogebäude (ein physisches LAN) vor. Durch das Aufstellen von Trennwänden (VLAN-Konfiguration) schaffen Sie separate Abteilungen wie "Marketing" (VLAN 10), "Buchhaltung" (VLAN 20) und "Geschäftsführung" (VLAN 30). Die Mitarbeiter einer Abteilung können frei miteinander reden. Um mit einer anderen Abteilung zu sprechen, müssen sie jedoch durch die zentrale Rezeption (den Router) gehen, wo ihr Anliegen geprüft wird.
    
- **Fazit / Bedeutung für IT-Profis:** Für Netzwerkadministratoren ist die Planung und Konfiguration von VLANs eine tägliche Aufgabe und eine Kernkompetenz. Sie sind unerlässlich, um Netzwerke übersichtlich, performant und vor allem sicher zu gestalten.