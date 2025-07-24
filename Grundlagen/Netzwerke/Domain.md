
Eine Domain ist der eindeutige Name einer Website und dient als Adresse im Internet. Sie besteht aus mehreren Teilen, darunter Subdomain, Second-Level-Domain und Top-Level-Domain (TLD). Die Domain ist ein wesentlicher Bestandteil einer URL und erleichtert den Menschen die Erreichbarkeit einer Website, da sie die IP-Adresse des Servers übersetzt. Die TLD kann je nach Geschäftsbereich oder geografischer Position gewählt werden, zum Beispiel “.de” für Deutschland oder “.com” für internationale Unternehmen.

https://de.wix.com/blog/beitrag/was-ist-eine-domain?experiment_id=%5E%5E03ec69d6-bef3-442b-a45b-f2d6a462c0c3%5E



Eine Domain besteht aus mehreren Ebenen, die durch Punkte voneinander getrennt sind. Die genaue Aufteilung einer Domain ist wie folgt:

- **Root-Label**: Dies ist der leere Knotenname am höchsten Punkt des Domain-Namensbaums. Er wird in der Regel nicht explizit angegeben, sondern impliziert durch den letzten Punkt in der Domain-Adresse.
- **Top-Level-Domain (TLD)**: Diese ist die erste Ebene rechts von der Root-Label. Beispiele sind .com, .org, .de oder .uk. Sie gibt an, zu welchem Bereich oder Land die Domain gehört.
- **Second-Level-Domain (SLD)**: Diese Ebene steht direkt unter der TLD und ist der frei wählbare Teil der Domain, der oft den Namen eines Unternehmens oder einer Organisation darstellt.
- **Third-Level-Domain (Subdomain)**: Diese Ebene kann optional hinzugefügt werden und wird oft verwendet, um spezifische Teile einer Website zu adressieren, wie zum Beispiel www oder blog.

Ein vollständiger Domainname, der auch als Fully Qualified Domain Name (FQDN) bezeichnet wird, enthält alle diese Ebenen und endet mit einem Punkt, der das Root-Label repräsentiert. Beispiel: www.example.com.

Die Gesamtlänge eines FQDN darf nicht mehr als 255 Zeichen betragen, wobei jeder einzelne Label (von Root-Label bis SLD) maximal 63 Zeichen lang sein darf.


![[Pasted image 20250122103934.png]]




FQDN

Der Fully Qualified Domain Name (FQDN) ist der vollständige und eindeutige Name einer Internetpräsenz. Er setzt sich aus mehreren Ebenen zusammen, die durch Punkte getrennt sind. Die Ebenen sind von rechts nach links zu lesen, wobei die höchste Hierarchieebene das Root-Label ist, das durch einen Punkt dargestellt wird. Dieses Label ist leer und wird vom Browser automatisch hinzugefügt.

Ein FQDN besteht aus dem Hostname, der Domain und der Top-Level-Domain (TLD). Ein Beispiel für einen FQDN ist `www.morpheus42.com`. Hier ist `www` der Hostname, `morpheus42` die Domain und `.com` die TLD.

Der FQDN ist wichtig für die Namensauflösung im Domain Name System (DNS). Wenn du eine Adresse wie `www.morpheus42.com` in die Adresszeile deines Browsers eingibst, sendet dieser die Anfrage an einen DNS-Server, der die IP-Adresse des Ziels zurückgibt. Diese IP-Adresse wird dann verwendet, um die Internetressource aufzurufen.

Um den FQDN eines Rechners herauszufinden, gibt es verschiedene Methoden abhängig vom Betriebssystem:

- Unter Windows kannst du den FQDN mit dem Befehl `ipconfig /all` im Eingabeaufforderungsfenster finden.
- Unter macOS und Linux kannst du den Befehl `hostname -f` im Terminal ausführen.

Der FQDN ist auch wichtig bei der Erstellung von SSL-Zertifikaten, da er als gemeinsamer Name und in den alternativen DNS-Namen des Zertifikats auftaucht.