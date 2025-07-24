Ein **offener** Port bedeutet, dass dort aktiv ein Dienst läuft und Verbindungen annimmt. Ist ein Port **geschlossen**, so ist er zwar erreichbar, aber es lauscht kein Dienst darauf. Bei einem **gefilterten** Port verhindert eine Firewall oder ein Filter den Zugriff, wodurch Nmap nicht feststellen kann, ob er offen oder geschlossen ist. Der Zustand **ungefiltert** schließlich besagt, dass der Port erreichbar (also nicht gefiltert) ist, Nmap aber mit der verwendeten Scanmethode (typischerweise beim ACK-Scan) nicht zwischen offen und geschlossen unterscheiden konnte.


Der Befehl startet einen **umfassenden Netzwerk-Scan** des lokalen Netzwerks `192.168.1.0/24`. Für jeden aktiven Host in diesem Netzwerk werden **alle 65535 TCP-Ports** gescannt. Für jeden Port, der als **offen** erkannt wird, versucht Nmap zusätzlich, den **laufenden Dienst und dessen Version** zu ermitteln.


- **Client → Server:** Sendet **SYN** (Synchronize) - "Ich möchte eine Verbindung aufbauen."
- **Server → Client:** Antwortet mit **SYN/ACK** (Synchronize/Acknowledge) - "Ok, ich bestätige deine Anfrage und möchte auch verbinden."
- **Client → Server:** Sendet **ACK** (Acknowledge) - "Ok, deine Bestätigung erhalten, Verbindung steht."



Eine Netzwerkschnittstelle (Interface) wie z.b `eth0` (Ethernet), `wlan0` (WLAN) oder `lo` ist der Punkt, an dem `tcpdump` den Netzwerkverkehr aufzeichnet.
Mit `-i  wählt man gezielt eine Schnittstelle aus, die Option `-i any` lauscht hingegen auf allen Schnittstellen gleichzeitign. Obwohl `-i any` einen schnellen Überblick bietet, sammelt sie ungenau und oft viel zu große datenmengen.