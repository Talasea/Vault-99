
Das Domain Name System (DNS) ist ein Telefonbuch für das Internet, das menschenfreundliche Domainnamen wie “kinsta.com” in computerfreundliche IP-Adressen wie “216.3.128.12” umwandelt. Es ermöglicht es Webbrowsern, auf Websites zuzugreifen, ohne dass Benutzer sich die IP-Adressen merken müssen.

## Funktionsweise

1. Ein Benutzer gibt eine Domainadresse wie “www.seo-kueche.de” in einen Webbrowser ein.
2. Der Browser sendet eine Anfrage an den lokalen DNS-Server (Resolver), um die IP-Adresse zu ermitteln.
3. Der lokale DNS-Server kontaktiert schrittweise in der Hierarchie übergeordnete DNS-Server, bis er die richtige Antwort, nämlich die IP-Adresse, gefunden hat.
4. Wenn keine IP-Adresse auffindbar ist, wird eine Fehlermeldung ausgegeben.
5. Der DNS-Server gibt die IP-Adresse an den Browser zurück, der dann die Verbindung zum Server herstellt.

## DNS-Hierarchie

1. **Root-Server**: Die höchste Ebene der DNS-Hierarchie, die für die Top-Level-Domains (TLD) wie “.de” oder “.com” zuständig ist.
2. **Autoritative DNS-Server**: Diese Server sind für bestimmte Zonen (Domainnamen) zuständig und verwalten die Zonendaten.
3. **Non-Authoritative DNS-Server**: Diese Server holen die erforderlichen Domaininformationen bei autoritativen DNS-Servern ein und speichern sie im Cache.

## Ziele

1. Einfache Zuordnung von Domainnamen zu IP-Adressen
2. Verbesserte Skalierbarkeit und Verfügbarkeit von Websites
3. Reduzierung von Fehlern bei der Namensauflösung

## Bedrohungen

1. DNS-Sicherheitslücken: Unverschlüsselte DNS-Anfragen können von Cyberkriminellen missbraucht werden.
2. DNS-Attacken: Manipulation von DNS-Einträgen kann zu Überwachung oder Zensur führen.
3. Ausfall von DNS-Servern: Kann zu einer Unterbrechung der Verbindung zu Websites führen.

## Insgesamt

Das Domain Name System ist ein wichtiger Bestandteil des Internets, der es ermöglicht, auf Websites zuzugreifen, ohne dass Benutzer sich IP-Adressen merken müssen. Es ist jedoch wichtig, dass DNS-Sicherheitslücken geschlossen werden und dass autoritative DNS-Server regelmäßig aktualisiert werden, um sicherzustellen, dass die Zuordnung von Domainnamen zu IP-Adressen stabil und sicher bleibt.


### DNS Server

Ein DNS-Server (Domain Name System) ist ein Server, der die Zuweisung zwischen menschenlesbaren Domain-Namen und numerischen IP-Adressen verwalten und umsetzen kann. Dieser Prozess wird als Namensauflösung bezeichnet. Der DNS-Server fungiert als “Telefonbuch” für das Internet, indem er die Domain-Namen in IP-Adressen übersetzt, die von Computern zur Kommunikation verwendet werden.

## Arbeitsschritte eines DNS-Servers

1. **Abfrage**: Ein Client (z.B. ein Webbrowser) sendet eine Anfrage an den DNS-Server, um den Domain-Namen in eine IP-Adresse zu übersetzen (Forward-Lookup).
2. **Suche**: Der DNS-Server durchsucht seine Datenbank nach der angefragten Domain-Namen und gibt die zugehörige IP-Adresse zurück.
3. **Caching**: Der DNS-Server speichert die Antwort in seinem Cache, um zukünftige Anfragen schneller beantworten zu können.
4. **Delegation**: Wenn der DNS-Server keine direkte Antwort auf die Anfrage hat, delegiert er die Suche an einen anderen DNS-Server (rekursiver Resolver).

## Typen von DNS-Servern

1. **Autoritative Nameserver**: Verantwortlich für eine bestimmte Zone (Domain) und speichert die zugehörigen DNS-Einträge.
2. **Recursive Resolver**: Sucht nach DNS-Einträgen in anderen Servern und gibt die Antwort zurück.
3. **Caching-Nameserver**: Speichert DNS-Einträge in einem Cache und gibt sie zurück, wenn sie gefragt werden.

## Funktionen von DNS-Servers

1. **Namensauflösung**: Übersetzt Domain-Namen in IP-Adressen.
2. **Reverse-DNS**: Übersetzt IP-Adressen in Domain-Namen (Reverse-Lookup).
3. **Load Balancing**: Verteilt Last auf mehrere Server durch die Zuweisung von verschiedenen IP-Adressen zu einem Domain-Namen.

## Schutzmaßnahmen für DNS-Servers

1. **Verschlüsselung**: Verwendung von TLS (Transport Layer Security) oder DNS-over-HTTPS (DoH) für sichere Übertragung von DNS-Anfragen.
2. **Firewall-Einstellungen**: Einstellungen, um unerwünschte Verbindungen zu blockieren.
3. **Regular Maintenance**: Regelmäßige Überprüfung und Aktualisierung von DNS-Einträgen.

Insgesamt ist ein DNS-Server ein wichtiger Bestandteil des Internets, da er es ermöglicht, Domain-Namen zu verwenden, anstatt IP-Adressen, um auf Websites und Dienste zuzugreifen.