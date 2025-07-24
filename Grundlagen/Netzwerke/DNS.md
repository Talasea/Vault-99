
Das Domain Name System (DNS) ist ein weltweit verteiltes System, das Domainnamen in IP-Adressen umwandelt, damit Computer und andere Geräte im Internet miteinander kommunizieren können. Es fungiert wie ein Telefonbuch des Internets, das menschenfreundliche Domainnamen in maschinenlesbare IP-Adressen umsetzt.

- **Funktion**: Das DNS ermöglicht es Nutzern, Websites über einfache Domainnamen wie `www.example.com` zu erreichen, anstatt sich IP-Adressen wie `193.19.92.139` zu merken.
- **Hierarchie**: Das DNS ist hierarchisch aufgebaut und besteht aus einer Reihe von DNS-Servern, die in einer Kette arbeiten, um eine Anfrage zu bearbeiten und eine IP-Adresse zu liefern.
- **Cache**: Lokale DNS-Server speichern oft benutzte IP-Adressen im Cache, um die Antwortzeit zu verkürzen.
- **Verschlüsselung**: Ursprünglich wurde DNS ohne Verschlüsselung übertragen, was es anfällig für Angriffe machte. Heutzutage gibt es verschlüsselte Protokolle wie DNSSEC und DNS über TLS, um diese Schwachstellen zu beheben.
- **DNS-Records**: Es gibt verschiedene Arten von DNS-Einträgen, wie A-Records, MX-Records und TXT-Records, die spezifische Informationen über eine Domain bereitstellen.
- **A-Record**: Ein A-Record weist eine Domain auf eine IP-Adresse hin, z.B. `@` (Domain ohne Subdomain) auf `193.19.92.139`.
- **MX-Record**: Ein MX-Record gibt an, welche Server für den E-Mail-Verkehr zuständig sind, z.B. `@` auf `mail.beispiel.tld` mit Priorität `10`.
- **TXT-Record**: Ein TXT-Record kann verschiedene Informationen enthalten, wie z.B. eine Google-Site-Verifizierung.
- **AAAA-Record**: Ein AAAA-Record weist eine Domain auf eine IPv6-Adresse hin, z.B. `@` auf `fd1e:9fad:b2c1:6771::1`.
- **CNAME-Record**: Ein CNAME-Record weist eine Domain auf eine andere Domain hin, z.B. `www` auf `beispiel2.tld`.

Das DNS ist ein wesentlicher Bestandteil des Internets und ermöglicht es uns, Websites und Dienste einfach und intuitiv zu erreichen.