# Virtual Private Network
VPN ist ein logisches privates Netzwerk auf einer öffentlich zugänglichen Infrastruktur. Nur die Kommunikationspartner, die zu diesem privaten Netzwerk gehören, können miteinander kommunizieren und Informationen und Daten austauschen.

Eine allgemein gültige Definition für VPN gibt es allerdings nicht. Der Begriff und die Abkürzung VPN stehen für eine Vielzahl unterschiedlicher Techniken. So werden VPN-Verbindungen oft als sicher angesehen, obwohl Aspekte wie Verschlüsselung oder Authentifizierung in manchen Protokollen, Produkten und Lösungen keine Rolle spielen.

Damit VPN-Verbindungen sicher sind müssen Authentizität, Vertraulichkeit und Integrität sichergestellt sein. Authentizität bedeutet die Identifizierung von autorisierten Nutzern und die Überprüfung der Daten, dass sie nur aus der autorisierten Quelle stammen. Vertraulichkeit und Geheimhaltung wird durch Verschlüsselung der Daten hergestellt. Mit der Integrität wird sichergestellt, dass die Daten von Dritten nicht verändert wurden.

### VPN-Typen und unterschiedliche Bezeichnungen

- End-to-Site-VPN
    - Host-to-LAN-VPN
    - Host-to-Gateway-VPN
    - Remote-Access-VPN
    - Road-Warrior-Szenario
- Site-to-Site-VPN
    - LAN-to-LAN-VPN
    - Gateway-to-Gateway-VPN
    - Branch-Office-VPN
- End-to-End-VPN
    - Host-to-Host-VPN
    - Remote-Desktop-VPN

### End-to-Site-VPN / Remote-Access-VPN

![End-to-Site-VPN / Remote-Access-VPN](https://www.elektronik-kompendium.de/sites/net/bilder/05120418.gif)

End-to-Site-VPN beschreibt ein VPN-Szenario, bei dem Heimarbeitsplätze oder mobile Benutzer (Außendienst) in ein Unternehmensnetzwerk eingebunden werden. Der externe Mitarbeiter soll so arbeiten, wie wenn er sich im Netzwerk des Unternehmens befindet. Man bezeichnet dieses VPN-Szenario auch als Remote-Access-VPN oder spricht vom Road-Warrior-Szenario.  
Die VPN-Technik stellt eine logische Verbindung, den VPN-Tunnel, zum entfernten lokalen Netzwerk über ein öffentliches Netzwerk her. Hierbei muss ein VPN-Client auf dem Computer des externen Mitarbeiters installieren sein.  
Im Vordergrund steht ein möglichst geringer, technischer und finanzieller Aufwand für einen sicheren Zugriff auf das entfernte Netzwerk.

- [RAS - Remote Access Service](https://www.elektronik-kompendium.de/sites/net/0907081.htm)

### Site-to-Site-VPN / LAN-to-LAN-VPN / Branch-Office-VPN

![Site-to-Site-VPN / LAN-to-LAN-VPN/ Branch-Office-VPN](https://www.elektronik-kompendium.de/sites/net/bilder/05120419.gif)

Site-to-Site-VPN und LAN-to-LAN-VPN, oder auch Branch-Office-VPN genannt, sind VPN-Szenarien, um mehrere lokale Netzwerke von Außenstellen oder Niederlassungen (Filialen) zu einem virtuellen Netzwerk über ein öffentliches Netz zusammenzuschalten.  
Netzwerke, die sich an verschiedenen Orten befinden lassen sich über eine angemietete Standleitung direkt verbinden. Diese Standleitung entspricht in der Regel einer physikalischen Festverbindung zwischen den beiden Standorten.  
Da jedes Netzwerk in der Regel auch eine Verbindung zum Internet hat, bietet es sich an, diese Internet-Verbindung zur Zusammenschaltung von zwei oder mehr Netzwerken mit VPN-Technik (LAN-to-LAN-Kopplung) zu nutzen. Bei VPNs über das Internet entstehen einmalige Kosten für die Einrichtung und laufende Kosten nur die, die für den Internet Service Provider zu bezahlen sind.

Virtuelle private Netze (VPN) werden immer öfter über das Internet aufgebaut. Das Internet wird so zur Konkurrenz zu den klassischen WAN-Diensten der Netzbetreiber. VPNs lassen sich über das Internet billiger und flexibler betreiben.

Eine Variante von Site-to-Site-VPN ist das Extranet-VPN. Während ein Branch-Office-VPN nur mehrere lokale Netzwerke einer Firma verbindet, ist ein Extranet-VPN ein virtuelles Netzwerk, das die Netzwerke unterschiedlicher Firmen miteinander verbindet. In der Regel geht es darum bestimmte Dienste fremder Unternehmen ins eigene Netzwerk zu integrieren oder Dienste für fremde Unternehmen anzubieten. Zum Beispiel für Geschäftspartner, Lieferanten und Support-leistende Unternehmen. Dabei gewährt man dem externen Unternehmen Zugriff auf Teilbereiche des eigenen Netzwerks. Die Zugriffsbeschränkung erfolgt mittels einer Firewall zwischen dem lokalen Netzwerk und dem Dienstenetzwerk. Extranet-VPNs ermöglichen eine sichere Kommunikation bzw. einen sicheren Datenaustausch zwischen den beteiligten Unternehmen.

### End-to-End-VPN / Host-to-Host-VPN / Remote-Desktop-VPN

![End-to-End-VPN / Host-to-Host-VPN](https://www.elektronik-kompendium.de/sites/net/bilder/05120417.gif)

End-to-End-VPN beschreibt ein VPN-Szenario, bei dem ein Client auf einen anderen Client in einem entfernten Netzwerk zugreift. Hierbei deckt der VPN-Tunnel die gesamte Verbindung zwischen zwei Hosts ab. Auf beiden Seiten muss eine entsprechende VPN-Software installiert und konfiguriert sein. In der der Regel ist der Verbindungsaufbau nur durch die Unterstützung einer zwischengeschalteten Station möglich. Das bedeutet, eine direkter Verbindungsaufbau von Host zu Host ist nicht möglich. Statt dessen bauen beide Seiten eine Verbindung zu einem Gateway auf, dass die beiden Verbindungen dann zusammenschaltet.  
Typische Anwendung eines End-to-End-VPN ist Remote-Desktop über öffentliche Netze. Während RDP und VNC sich wegen der fehlenden Verschlüsselung nur für den Einsatz in lokalen Netzwerken eignet, gibt es für Remote-Desktop-VPNs meist nur propritäre und kommerzielle Lösungen. Zum Beispiel Teamviewer, GotoMyPC und Anydesc.

### VPN-Tunnel und VPN-Endpunkt

![Tunneling-Prinzip](https://www.elektronik-kompendium.de/sites/net/bilder/14101412.gif)

Um eine gesicherte Datenübertragung über das unsichere Internet zu gewährleisten, wird mit einem Tunneling-Protokoll eine verschlüsselte Verbindung, der VPN-Tunnel, aufgebaut. Der Tunnel ist eine logische Verbindungen zwischen beliebigen Endpunkten. Meist sind das VPN-Clients, VPN-Server oder VPN-Gateways. Man nennt diese virtuellen Verbindungen Tunnel, weil die Nutzdaten in einer virtuellen Verbindung getunnelt werden.

Ein VPN-Endpunkt ist die Stelle an der der VPN-Tunnel endet bzw. beginnt. Der Endpunkt ist der Host, der für die Einhaltung von Authentizität, Vertraulichkeit und Integrität zuständig ist. Ein VPN-Endpunkt kann ein Router, Gateway oder auch ein Software-Client sein.

- [VPN-Tunnel / VPN-Endpunkt (Tunneling)](https://www.elektronik-kompendium.de/sites/net/1410141.htm)

### VPN-Endpunkt: VPN-Router / VPN-Gateway / VPN-Server

VPN-Lösungen gibt es als Hardware (VPN-Router), Software (VPN-Server) oder auch als Service (Layer-2-VPN vom Netzbetreiber). Typischerweise setzt man an VPN-Endpunkten einen VPN-Router oder ein VPN-Gateway ein. Es gibt aber auch Server, auf denen VPN-Dienste oder VPN-Software installiert sind. Diese VPN-Server dienen dann als VPN-Endpunkte. Ein eigenständiger VPN-Server ist eher selten nötig. VPN-Gateway-Funktionen finden sich auch in Routern und Firewalls.  
VPN-Gateways und -Router können VPN-Verbindungen und normale Verbindungen verarbeiten. Die VPN-Verbindungen erkennen sie am Header der Datenpakete oder an der IP-Protokollnummer.  
Eine Sonderform sind VPN-Services von Netzbetreibern, die keine Installation zusätzlicher Hardware notwendig macht.

### VPN-Protokolle und VPN-Lösungen

Ein Protokoll legt fest, wie zwei Teilnehmer einer Verbindung miteinander kommunizieren. Bei VPN-Protokollen gibt es zusätzlich noch Methoden zur Verschlüsselung der Verbindung und gegenseitiger Authentifizierung der Teilnehmer.

- [VPN-Protokolle und VPN-Lösungen](https://www.elektronik-kompendium.de/sites/net/2601131.htm)

Die meisten VPN-Protokolle sind in eine VPN-Lösung eingebettet. Das heißt, in Kombination mit Hardware und Software zu nutzen. Wie genau die Lösung aussieht hängt vom Hersteller ab. Parallel dazu gibt es Open-Source-Software, die sich flexibel zu einer VPN-Lösung arrangieren lässt.

- [WireGuard](https://www.elektronik-kompendium.de/sites/net/2502231.htm)
- [IPsec](https://www.elektronik-kompendium.de/sites/net/0906191.htm)
- [PPTP](https://www.elektronik-kompendium.de/sites/net/0906141.htm)
- [L2TP](https://www.elektronik-kompendium.de/sites/net/0906131.htm)
- [L2TP over IPsec](https://www.elektronik-kompendium.de/sites/net/1410061.htm)
- [SSL-VPN](https://www.elektronik-kompendium.de/sites/net/1410151.htm)
- [Hamachi](https://www.elektronik-kompendium.de/sites/net/1706191.htm)
- [OpenVPN (Software, kein Protokoll)](https://www.elektronik-kompendium.de/sites/net/1706181.htm)
- [Layer-2-VPN](https://www.elektronik-kompendium.de/sites/net/1710161.htm)

### Eigenes VPN aufbauen oder Outsourcing-Lösung?

Bei der Planung eines VPN kommt man nicht herum, heute schon an morgen zu denken. Doch langfristige Aussagen sind immer schwierig. Die Rahmenbedingungen sind ständigen Änderungen unterworfen. Zum Beispiel die Zahl der Benutzer, die benötigte Bandbreite, Qualitätsmerkmale, rechtliche Aspekte, neue Geschäftsfelder und Akquisitionen, an die man heute noch nicht denkt. Am Anfang groß zu denken, aber klein und bedarfsgerecht zu starten, ist deshalb eine gute Strategie.  
Grundsätzlich ist auf die Offenheit des Systems zu achten. Zum Beispiel auf die Einhaltung von Standards. Das erleichtert die Integration in existierende Netze. Der Sicherheitsstandard auf IP-Ebene heißt IPsec. Virtuelle, private Netze sind aber nicht auf IP beschränkt. Es gibt auch andere Lösungen.

Ein eigenes VPN aufzubauen bedeutet ein eigenes VPN-Gateway inklusive Access-Router zu betreiben. Hierbei entsteht ein relativ hoher Aufwand, weil man sich um alles selber kümmern muss.  
Die Management-Kosten werden in der Regel unterschätzt. Dabei geht es nicht nur um Geld. Viel vergeudete Zeit durch selbst verursachte Fehler, inkompatible Komponenten und fehlendes Know-how treiben den Frustfaktor nach oben. Obwohl man mit standardisierten Protokollen und Komponenten arbeitet, ist vieles so flexibel konfigurierbar, dass unter Umständen eine Zusammenarbeit unterschiedlich konfigurierter Geräte nicht zustande kommt. Zusatzkosten durch nachträgliches Eliminieren von Fehlerquelle sollte man nicht unterschätzen. So ist die Integration einer VPN-Technik häufig auch mit IP-Adressänderungen gekoppelt. Über ein externes VPN eines Dienstleisters spart man sich die Probleme häufig, weil der für die notwendige Adressumsetzung sorgen kann.

Eventuell ist die Rundumsorglos-Lösung eines Fernwartungsspezialisten für den Anfang die beste Lösung. Der Einstieg gelingt hier auf der Know-how-Seite relativ schmerzfrei. Hierbei muss man berücksichtigen, dass man sich von den Diensten eines Service-Providers je nach Outsourcing-Weite abhängig macht und wenig Einfluss hat. Es macht durchaus Sinn vor dem Outsourcing eine Exit-Strategie für den Betrieb eines eigenen Gateways in der Schublade zu haben.

### VPN und Firewall, eine unheimliche Begegnung!

VPN im Zusammenhang mit einer Firewall führt häufig zu ungeahnten Problemen. In der Regel sollte eine Firewall gekapselten Datenverkehr verhindern. Denn der gekapselte Datenverkehr könnte unberechtigte und unsichere Daten enthalten. Deshalb lässt man in der Regel eine Tür im Sicherheitskonzept geöffnet, wenn man ein VPN betreibt.

Beim Aufbau eines VPNs ist die Platzierung des VPN-Endpunktes, üblicherweise ein VPN-Router oder VPN-Gateway, eine wichtige Entscheidung. Es steht dabei die Frage im Raum, ob das VPN-Gateway vor oder hinter der Firewall sitzen soll.

![VPN-Gateway hinter der Firewall](https://www.elektronik-kompendium.de/sites/net/bilder/05120414.gif)

Eigentlich soll eine Firewall vor ungewollten Zugriffen aus dem Netz schützen. Wenn nun das VPN-Gateway hinter der Firewall sitzt, dann ist die Firewall nicht in der Lage in die verschlüsselten Pakete hineinzusehen. Die verschlüsselten IP-Pakete (z. B. mit IPsec und IKE) werden auf Port 500 an das VPN-Gateway durchgelassen. Ein VPN-Teilnehmer könnte auf diese Weise unkontrolliert das Netzwerk angreifen oder ungewollte Daten ins Netzwerk einschmuggeln.

![VPN-Gateway vor der Firewall](https://www.elektronik-kompendium.de/sites/net/bilder/05120415.gif)

Ein bessere Lösung ist, das VPN-Gateway vor die Firewall zu setzen und alle verschlüsselten Datenpakete zu entschlüsselt und erst danach die Prüfung auf ungewollte Verbindungen zu prüfen.

![VPN-Gateway zwischen Router und Firewall in der DMZ](https://www.elektronik-kompendium.de/sites/net/bilder/05120416.gif)

Die beste Lösung ist jedoch, das VPN-Gateway oder den VPN-Server in eine demilitarisierte Zone (DMZ), zwischen Netzzugangsrouter und Firewall, zu setzen. Auf diese Weise kann der entschlüsselte Datenverkehr in einer zweiten Filterstufe durch die Firewall nochmals überprüft werden.  
Wer Sicherheits- und Verbindungsprobleme vermeiden will, der wird in der Regel einen Router mit integrierter Firewall einsetzen, der gleichzeitig als Endpunkt einer VPN-Verbindung arbeitet.

### Problem: Höhere Paketlaufzeit

Bei einer VPN-Verbindung mit Tunneling kann es zu einer zusätzlichen zeitliche Verzögerung kommen, die eine längere Paketlaufzeit zur Folge hat (Latenz).

### Problem: Fragmentierte IP-Pakete

Gelegentlich kommt es vor, dass VPN-Verbindungen hergestellt werden können, aber keine Datenübertragung möglich ist. In der Regel liegt das daran, dass die Firewall auf der Gegenseite aus Sicherheitsgründen fragmentierte Datenpakete verwirft. Das ist dann der Fall, wenn IP-Pakete auf mehrere VPN-Pakete verteilt werden. In diesem Fall muss man in der betreffenden Firewall diese Funktion (drop fragmented packets) abschalten.