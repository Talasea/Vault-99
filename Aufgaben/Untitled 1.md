Am Internet-Gateway
Dies ist die erste Verteidigungslinie. Ein IPS an dieser Stelle blockiert die große Masse an bekannten Angriffen, Scans und schädlichem Traffic aus dem Internet, _bevor_ sie überhaupt das interne Netzwerk erreichen. Es schützt die gesamte Infrastruktur vor externen Bedrohungen.

In der DMZ
In der DMZ stehen öffentlich erreichbare Server (z.B. Webserver, Lernplattform-Portal). Ein IDS/IPS überwacht den Verkehr zu und von diesen Servern. Es erkennt Angriffsversuche auf die Webanwendungen und schlägt Alarm, falls ein Server kompromittiert wird und versucht, Angriffe auf das interne Netz zu starten.

Zwischen internem Netz und dem Studenten-/Labor-Netzwerk(proxmox)
Dies ist ein kritischer Punkt für eine Akademie. Die Studierenden experimentieren, nutzen Security-Tools und erzeugen eventuell ungewöhnlichen Traffic.

- Ein **IDS (nur Erkennung)** ist hier oft besser als ein IPS, da es die Aktivitäten zur Analyse protokolliert, ohne legitime Lernübungen versehentlich zu blockieren.
    
- So können Dozenten nachvollziehen, was im Labor passiert, und echte Bedrohungen von gewollten Simulationen unterscheiden.


**Vor dem internen Server-Netzwerk**
Um die Kronjuwelen – die internen Server mit sensiblen Verwaltungs-, Prüfungs- und Personaldaten – besonders zu schützen. Ein IPS an dieser Stelle agiert als starke zweite Verteidigungslinie und wehrt Angriffe ab, die vom internen Mitarbeiternetz, dem Studentennetz oder einer kompromittierten DMZ ausgehen könnten (sogenannte laterale Bewegungen).

Direkt auf kritischen Servern
Ein HIDS/HIPS wird als Software direkt auf wichtigen Servern (z.B. Datenbankserver, Domain Controller) installiert. Es überwacht systeminterne Vorgänge wie Dateizugriffe und Prozessstarts und kann unautorisierte Änderungen sofort blockieren. Dies schützt vor Insider-Angriffen oder Malware, die alle Netzwerkbarrieren überwunden hat.