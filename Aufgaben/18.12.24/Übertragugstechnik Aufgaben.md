
![[Pasted image 20241219141512.png]]]]![[Pasted image 20241219144416.png]]

Für eine Stern-Topologie mit wenig Internet-Datenverkehr und vielen internen Berechnungen zwischen lokalen Geräten empfehle ich die Verwendung von Twisted Pair-Kabeln   oder Fiber Optic-Kabeln (Multimode oder Singlemode) für die Verkabelung zwischen den Geräten.  
﻿  
﻿Ein Twisted Pair-Kabel ist ein Netzwerkkabel, das aus acht paarweise verdrillten Kupferkabeln besteht.  
﻿  
﻿Als biespiel der bauweisen :   
﻿  
﻿UTP (Unshielded Twisted Pair): Ohne elektrischen Schirm, verwendet für einfache Netzwerkanwendungen das hest das nach dem ausenmattel imprinzip schon die einzeln kabel stränge kommen   
﻿  
﻿STP (Shielded Twisted Pair): Mit elektrischem Schirm, verwendet für Anwendungen, die hohe Schutzanforderungen haben   jedes kabelpaar ist einzend abgeschirmt   
﻿  
﻿Funktionen und Vorteile Die die Verdrillung der Adern paare im Twisted-Pair-Kabel:  
﻿Minimiert das Übersprechen zwischen den Adern paaren Schützt gegen elektromagnetische Störfelder Reduziert Interferenzen mit benachbarten verdrillten Kabeln Bietet einen besseren Schutz gegenüber elektrischen und magnetischen Störfeldern
﻿
Um die kosten zu senken würde ich ein Cat 5 oder cat 6 in diesem Fall verenden .   
﻿  
﻿CAT 5e-Kabel können eine Datenübertragungsgeschwindigkeit von bis zu 1 Gbit/s erreichen, während CAT 6-Kabel bis zu 10 Gbit/s erreichen können.
﻿
﻿
﻿![[Screenshot 2024-12-19 151657.png]]


Ein Hub  
﻿ ist eine premitiver Übermitller der einfach die Informationen die er von einem port bekommt und sendet sie  an alle anderen Ports. Er Arbeitet auf der 1. Schicht des OSI-Modells.  
﻿  
﻿  
﻿Layer 2 Switch:   
﻿  
﻿Ein Layer-2 Switch, auch bekannt als Ethernet-Switch, arbeitet auf der Schicht 2 des OSI-Modells.  
﻿Es kann MAC-Adressen (Hardware-Adressen) von Netzwerkgeräten lernen und speichert diese in seiner Adresstabelle.  
﻿Wenn ein Paket an den Switch gesendet wird, wird es direkt an den vorgesehenen Zielanschluss weitergeleitet, ohne dass es an alle anderen Ports gesendet wird  
﻿So nutzt er eine Punkt zu Punkt Verbindung.   
﻿Mann kann ihn also schon Als Postverteilzentrum sehen er unterscheidet da nur n der Adresse (MAC-Adresse)   
﻿  
﻿Ein Layer-3 Switch:  
﻿  
﻿Ein auch bekannt als Router-Switch oder Multilayer-Switch, er arbeitet auf der Schicht 3 des OSI-Modells und kann IP-Adressen lesen.   
﻿Zu der Fähigkeit MAC Adressen zu lesen kann dieser nun auch Ip- Adressen lesen und verarbeiten .   
﻿So verteilt er Informationen noch gezielter Er hat nicht nur die Adresse Sondern eben auch  jetzt einen Namen den er Zuordnen kann


![[Pasted image 20241219155126.png]]


![[Pasted image 20241219161755.png]]
Softwarebasierte Firewalls:  
﻿Diese Firewalls laufen auf einem Computer oder Server und nutzen die Ressourcen des Host-Geräts (Router oder PC/Endgerät) .  
﻿Sie bieten eine  abgestufte Kontrolle und ermöglichen es, die Kommunikation von und zu einem Programm zuzulassen oder zu verhindern (Portfreigabe) . Softwarebasierte Firewalls sind oft einfacher zu konfigurieren und weniger teuer als Hardwarebasierte Firewalls.  
﻿ Allerdings verbrauchen sie Systemressourcen und können das System verlangsamen.  
﻿  
﻿Hardwarebasierte Firewalls:  
﻿ Diese Firewalls sind eigenständige Geräte mit einer dedizierten CPU, Speicher und Software. Sie sind effizienter und schneller als Softwarebasierte Firewalls und können ein ganzes Netzwerk abdecken. Hardwarebasierte Firewalls sind oft teurer als Softwarebasierte Firewalls, aber sie bieten einen höheren Schutz und sind weniger anfällig für Angriffe.Im direkten Vergleich bieten Hardwarebasierte Firewalls einen höheren Schutz und sind effizienter, aber sie sind auch teurer. Softwarebasierte Firewalls sind einfacher zu konfigurieren und weniger teuer, aber sie verbrauchen Systemressourcen und bieten einen geringeren Schutz.  
﻿  
﻿Bei einem Unternehmen mit 10 Mitarbeiter würde ich aus kosten gründen Software Girewall  
﻿  
﻿Ab 100  eine reine Externe Firewall  
﻿Bei 1000 würde ich kombiniert nehmen  grade um Risiko von eigenen Mitarbeiter zu  minieren.