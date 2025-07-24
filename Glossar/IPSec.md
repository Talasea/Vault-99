

IPsec, abgekürzt für Internet Protocol Security, ist eine Sammlung von Protokollen, die eine sichere Kommunikation über das Internet gewährleisten.
Es wurde von der Internet Engineering Task Force entwickelt, um die Vertraulichkeit, Integrität und Authentizität von Daten beim Zugriff auf öffentliche Netzwerke zu gewährleisten.
IPsec erweitert das Internet-Protokoll um Verschlüsselungs- und Authentifizierungsmechanismen, um Daten sicher über öffentliche und unsichere Netze zu transportieren.
Es verwendet asymmetrische und symmetrische Verschlüsselung, um Geschwindigkeit und Sicherheit bei der Datenübertragung zu gewährleisten.
IPsec unterstützt verschiedene Verschlüsselungsarten, wie AES, Blowfish, Triple DES, ChaCha und DES-CBC.2 Es besteht aus Protokollen wie Authentication Header (AH) und Encapsulating Security Payload (ESP), die für die Authentifizierung, Integrität und Vertraulichkeit der IP-Pakete sorgen.



## Was ist IPSec?

IPSec ist ein Satz von Kommunikationsregeln oder Protokollen, um eine sichere Verbindung über ein Netzwerk herzustellen. Internet Protocol (IP) ist der allgemeine Standard, der festlegt, wie Daten im Internet übermittelt werden. IPSec fügt daran Verschlüsselung und Berechtigungen hinzu, um die Protokolle noch sicherer zu machen. So werden, zum Beispiel, Daten an der Quelle zerteilt und am Ziel wieder zusammengesetzt. Es bestätigt auch die Quelle der Daten. 

## Warum ist IPSec wichtig?

Die Internet Engineering Task Force entwickelte IPSec in den 1990er Jahren, um die Vertraulichkeit, Integrität und Authentizität von Daten beim Zugriff auf öffentliche Netzwerke zu gewährleisten. So stellen Benutzer beispielsweise über ein [Virtual Private Network (VPN)](https://aws.amazon.com/what-is/vpn/) mit IPSec eine Verbindung zum Internet her, um remote auf Unternehmensdateien zuzugreifen. Das IPSec-Protokoll verschlüsselt vertrauliche Informationen, um eine unerwünschte Überwachung zu verhindern. Der Server kann auch überprüfen, ob die empfangenen Datenpakete autorisiert sind.

## Was sind die Einsatzmöglichkeiten von IPSec?

IPsec kann verwendet werden, um Folgendes zu tun:

- Gewährleistung der Routersicherheit beim Senden von Daten über das öffentliche Internet.
- Verschlüsseln von Anwendungsdaten.
- Schnelles Bestätigen von Daten, wenn die Daten von einem bekannten Absender stammen.
- Schützen von Netzwerkdaten durch die Einrichtung von verschlüsselten Verbindungen, sogenannte IPsec-Tunnel, die alle zwischen zwei Endpunkten gesendeten Daten verschlüsseln.

Organisationen verwenden IPSec, um sich vor Replay-Angriffen zu schützen. Ein Replay-Angriff oder Man-in-the-Middle-Angriff besteht darin, eine laufende Übertragung abzufangen und zu verändern, indem Daten an einen zwischengeschalteten Computer weitergeleitet werden. Das IPSec-Protokoll weist jedem Datenpaket eine fortlaufende Nummer zu und führt Prüfungen durch, um Anzeichen für doppelte Pakete zu erkennen. 

## Was ist IPSec-Verschlüsselung?

Die IPSec-Verschlüsselung ist eine Softwarefunktion, die Daten verschlüsselt, um deren Inhalt vor Unbefugten zu schützen. Daten werden durch einen Verschlüsselungsschlüssel verschlüsselt, und ein Entschlüsselungsschlüssel wird benötigt, um die Informationen zu entschlüsseln. IPSec unterstützt verschiedene Arten von Verschlüsselungen, einschließlich AES, Blowfish, Triple DES, ChaCha und DES-CBC. 

IPSec verwendet asymmetrische und symmetrische Verschlüsselung, um Geschwindigkeit und Sicherheit bei der Datenübertragung zu gewährleisten. Bei der asymmetrischen Verschlüsselung wird der Verschlüsselungsschlüssel öffentlich gemacht, während der Entschlüsselungsschlüssel geheim gehalten wird. Die symmetrische Verschlüsselung verwendet denselben öffentlichen Schlüssel zum Verschlüsseln und Entschlüsseln von Daten. IPSec stellt eine sichere Verbindung mit asymmetrischer Verschlüsselung her und wechselt zur symmetrischen Verschlüsselung, um die Datenübertragung zu beschleunigen.

## Wie funktioniert IPSec?

Computer tauschen Daten mit dem IPSec-Protokoll über die folgenden Schritte aus. 

1. Der Absendercomputer bestimmt, ob die Datenübertragung einen IPSec-Schutz erfordert, indem er diese anhand seiner Sicherheitsrichtlinie überprüft. Wenn dies der Fall ist, initiiert der Computer eine sichere IPSec-Übertragung mit dem Empfängercomputer.
2. Beide Computer handeln die Anforderungen aus, um eine sichere Verbindung herzustellen. Dazu gehört die gegenseitige Vereinbarung der Parameter für Verschlüsselung, Authentifizierung und andere Sicherheitsassoziations (SA)-Parameter. 
3. Der Computer sendet und empfängt verschlüsselte Daten und bestätigt so, dass sie aus vertrauenswürdigen Quellen stammen. Es führt Überprüfungen durch, um sicherzustellen, dass der zugrunde liegende Inhalt zuverlässig ist. 
4. Sobald die Übertragung abgeschlossen ist oder die Sitzung abgelaufen ist, beendet der Computer die IPSec-Verbindung. 

## Was sind die IPSec-Protokolle?

IPSec-Protokolle versenden Datenpakete auf sichere Weise. Ein Datenpaket ist eine spezifische Struktur, die Informationen für die Netzwerkübertragung formatiert und aufbereitet. Es besteht aus einem Header, Nutzdaten und einem Trailer.

- Ein Header ist ein vorangehender Abschnitt, der Anweisungsinformationen enthält, um das Datenpaket an das richtige Ziel zu leiten. 
- Nutzdaten ist ein Begriff, der die eigentlichen Informationen beschreibt, die in einem Datenpaket enthalten sind.
- Der Trailer besteht aus zusätzlichen Daten, die an das Ende der Nutzdaten angehängt werden, um das Ende des Datenpakets anzuzeigen. 

 Nachfolgend sind einige IPSec-Protokolle aufgeführt.

### **Authentication Header (AH)**

Das Authentication Header (AH)-Protokoll fügt einen Header hinzu, der Absender-Authentifizierungsdaten enthält und den Paketinhalt vor Änderungen durch Unbefugte schützt. Es warnt den Empfänger vor möglichen Manipulationen des ursprünglichen Datenpakets. Beim Empfang des Datenpakets vergleicht der Computer die kryptographische Hash-Berechnung aus den Nutzdaten mit dem Header, um sicherzustellen, dass beide Werte übereinstimmen. Ein kryptografischer Hash ist eine mathematische Funktion, die Daten zu einem eindeutigen Wert zusammenfasst. 

### **Encapsulating Security Payload (ESP)**

Je nach ausgewähltem IPSec-Modus führt das Encapsulating Security Payload (ESP)-Protokoll eine Verschlüsselung des gesamten IP-Pakets oder nur der Nutzlast durch. ESP fügt dem Datenpaket beim Verschlüsseln einen Header und einen Trailer hinzu. 

### **Internet Key Exchange (IKE)**

Internet Key Exchange (IKE) ist ein Protokoll, das eine sichere Verbindung zwischen zwei Geräten im Internet herstellt. Beide Geräte richten eine Sicherheitsassoziation (SA) ein, bei der Verschlüsselungsschlüssel und Algorithmen ausgehandelt werden, um nachfolgende Datenpakete zu übertragen und zu empfangen. 

## Was sind IPSec-Modi?

IPSec arbeitet in zwei verschiedenen Modi mit unterschiedlichen Sicherheitsstufen. 

**Tunnel**

Der IPSec-Tunnelmodus eignet sich für die Übertragung von Daten in öffentlichen Netzwerken, da er den Datenschutz vor Unbefugten erhöht. Der Computer verschlüsselt alle Daten, einschließlich der Nutzdaten und des Headers, und fügt einen neuen Header an die Daten an. 

**Transport**

Der IPSec-Transportmodus verschlüsselt nur die Nutzdaten des Datenpakets und belässt den IP-Header in seiner ursprünglichen Form. Der unverschlüsselte Paket-Header ermöglicht es Routern, die Zieladresse jedes Datenpakets zu identifizieren. Daher wird der IPSec-Transport in einem engen und vertrauenswürdigen Netzwerk verwendet, z. B. zum Sichern einer direkten Verbindung zwischen zwei Computern. 

## Was ist IPSec-VPN?

Ein VPN oder virtuelles privates Netzwerk ist eine Netzwerksoftware, mit der Benutzer anonym und sicher im Internet surfen können. Ein IPSec-VPN ist eine VPN-Software, die das IPSec-Protokoll verwendet, um verschlüsselte Tunnel im Internet zu erstellen. Es bietet eine End-to-End-Verschlüsselung, d. h. die Daten werden auf dem Computer verschlüsselt und auf dem Empfangsserver wieder entschlüsselt. 

### **SSL-VPN** 

SSL steht für Secure Socket Layer. Es handelt sich um ein Sicherheitsprotokoll, das den Web-Datenverkehr schützt. Ein SSL-VPN ist ein browserbasierter Service zur Netzwerksicherheit, der das integrierte SSL-Protokoll verwendet, um die Netzwerkkommunikation zu verschlüsseln und zu schützen. 

### **Was ist der Unterschied zwischen IPSec-VPN und SSL-VPN?**

Beide Sicherheitsprotokolle arbeiten auf verschiedenen Schichten des Open Systems Interconnection (OSI)-Modells. Das OSI-Modell definiert die Schichtenarchitektur des Datenaustauschs zwischen Computern in einem Netzwerk. 

IPSec-Protokolle gelten für die Netzwerk- und Transportschichten in der Mitte des OSI-Modells. In der Zwischenzeit verschlüsselt SSL Daten auf der obersten Anwendungsschicht. Sie können über einen Webbrowser eine Verbindung zu einem SSL-VPN herstellen, müssen jedoch separate Software installieren, um IPSec-VPNs zu nutzen.

## Wie unterstützt AWS IPSec-Verbindungen?

[AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/) ist ein vollständig verwalteter Service, der mithilfe von IPSec-Tunneln eine sichere Verbindung zwischen Ihrem Rechenzentrum oder Ihrer Zweigstelle und Ihren AWS-Ressourcen herstellt. Wenn Sie Site-to-Site VPN verwenden, können Sie sich sowohl mit Ihren [Amazon Virtual Private Clouds (VPC)](https://aws.amazon.com/vpc/) als auch mit [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) verbinden. Es werden zwei Tunnel pro Verbindung für eine erhöhte Redundanz verwendet. AWS Site-to-Site VPN bietet viele Vorteile wie:

- Einblick in den Zustand des lokalen und Remote-Netzwerks mit Leistungsüberwachung.
- Sichere und einfache Migration von lokalen Anwendungen in die AWS-Cloud.
- Verbesserte Leistung von Anwendungen bei Integration mit [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/?blogs-global-accelerator.sort-by=item.additionalFields.createdDate&blogs-global-accelerator.sort-order=desc&aws-global-accelerator-wn.sort-by=item.additionalFields.postDateTime&aws-global-accelerator-wn.sort-order=desc).

Beginnen Sie mit AWS VPN, indem Sie sich noch heute [für ein AWS-Konto registrieren](https://portal.aws.amazon.com/gp/aws/developer/registration/index).