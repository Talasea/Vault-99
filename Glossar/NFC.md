
NFC steht für Near-Field Communication. Es handelt sich um eine Technologie, die eine drahtlose Kommunikation über kurze Distanzen ermöglicht, typischerweise bis zu einigen Zentimetern. NFC basiert auf dem Prinzip der induktiven Kopplung zwischen zwei Geräten, von denen eines aktiv ein elektromagnetisches Feld erzeugt und das andere passiv darauf reagiert oder ebenfalls aktiv sendet.

**Grundlagen der NFC-Technologie:**

- **Kurze Reichweite:** Die limitierte Reichweite ist ein bewusstes Designmerkmal, das die Sicherheit erhöht und unbeabsichtigte Verbindungen reduziert.
- **Frequenz:** NFC operiert im lizenzfreien ISM-Band bei einer Frequenz von 13,56 MHz.
- **Datenübertragungsraten:** Die Datenübertragungsraten sind im Vergleich zu anderen drahtlosen Technologien wie Bluetooth oder WLAN relativ gering (typischerweise bis zu 424 kbit/s), aber für die meisten NFC-Anwendungen ausreichend.
- **Zwei Betriebsmodi:**
    - **Aktiver Modus:** Beide an der Kommunikation beteiligten Geräte erzeugen ihr eigenes elektromagnetisches Feld und wechseln sich beim Senden und Empfangen von Daten ab.
    - **Passiver Modus:** Ein Gerät (das Lesegerät) erzeugt ein elektromagnetisches Feld, und das andere Gerät (das NFC-Tag) nutzt dieses Feld, um sich mit Energie zu versorgen und seine Daten zurückzusenden.

**Der NFC-Tag:**

Ein NFC-Tag ist ein kleiner, in der Regel passiver Transponder, der einen Mikrochip mit Speicher und eine Antenne enthält. Er benötigt keine eigene Stromquelle und wird durch das elektromagnetische Feld eines NFC-fähigen Lesegeräts aktiviert.

- **Aufbau:** Ein NFC-Tag besteht typischerweise aus einem integrierten Schaltkreis (IC) und einer Antenne, die auf einem Substrat (z. B. Papier, Kunststoff) aufgebracht sind. Das Ganze kann in verschiedenen Formen und Größen vorliegen, von kleinen Aufklebern bis hin zu integrierten Komponenten in Geräten.
- **Funktionsweise:** Wenn ein NFC-Lesegerät in die Nähe eines passiven NFC-Tags kommt, induziert das vom Lesegerät erzeugte elektromagnetische Feld einen Strom in der Antenne des Tags. Dieser Strom versorgt den Chip des Tags mit Energie, wodurch dieser seine gespeicherten Daten auslesen und über die Antenne zurück an das Lesegerät senden kann.
- **Datenspeicherung:** NFC-Tags können unterschiedliche Mengen an Daten speichern, von wenigen Bytes bis zu mehreren Kilobytes. Die Art der speicherbaren Daten hängt vom Typ des NFC-Tags ab. Häufig gespeicherte Informationen sind eindeutige Identifikationsnummern (UIDs), Weblinks (URLs), Textinformationen, Kontaktdaten oder Befehle zur Ausführung von Aktionen auf einem NFC-fähigen Gerät.
- **Verschiedene Tag-Typen:** Es gibt verschiedene NFC-Tag-Typen (z. B. Typ 1 bis Typ 5), die sich in ihrer Speicherkapazität, Datenübertragungsrate und Kompatibilität mit verschiedenen Standards unterscheiden.

**Anwendungen von NFC und NFC-Tags:**

NFC-Technologie und NFC-Tags werden in einer Vielzahl von Anwendungen eingesetzt, darunter:

- **Kontaktloses Bezahlen:** Ermöglicht sichere und schnelle Transaktionen an Kassen durch einfaches Antippen eines NFC-fähigen Geräts (z. B. Smartphone, Smartwatch) an ein Bezahlterminal.
- **Zutrittskontrolle:** NFC-Tags können in Ausweisen oder Schlüsselkarten integriert werden, um den Zutritt zu Gebäuden oder gesicherten Bereichen zu ermöglichen.
- **Öffentlicher Nahverkehr:** Fahrkarten und Tickets können auf NFC-fähigen Geräten oder Karten gespeichert und an Fahrkartenlesern validiert werden.
- **Datenaustausch:** Schnelles und unkompliziertes Teilen von kleinen Datenmengen zwischen zwei NFC-fähigen Geräten (z. B. Kontaktdaten, Fotos, Weblinks).
- **Gerätekopplung:** Vereinfachte Verbindung von Bluetooth- oder WLAN-Geräten durch einfaches Antippen.
- **Informationsabruf:** NFC-Tags können in Plakaten, Produkten oder an Orten platziert werden, um Nutzern durch Antippen mit einem NFC-fähigen Smartphone zusätzliche Informationen (z. B. Produktinformationen, Wegbeschreibungen) bereitzustellen.
- **Authentifizierung:** NFC kann zur Zwei-Faktor-Authentifizierung eingesetzt werden, indem ein physischer NFC-Tag als zusätzlicher Sicherheitsfaktor dient.
- **Asset Tracking:** NFC-Tags können an Geräten oder Inventar angebracht werden, um deren Standort und Status zu verfolgen.

**Sicherheitsaspekte von NFC:**

Obwohl die kurze Reichweite von NFC inhärent einige Sicherheitsvorteile bietet (z. B. Schutz vor Fernangriffen), gibt es auch potenzielle Sicherheitsrisiken:

- **Eavesdropping (Abhören):** Obwohl die Reichweite gering ist, ist es theoretisch möglich, die Kommunikation zwischen einem NFC-Gerät und einem Tag mit spezialisierter Ausrüstung abzufangen.
- **Data Corruption:** Störungen oder Manipulationen während der Datenübertragung könnten zu Datenverlust oder -beschädigung führen.
- **Relay Attacks:** Ein Angreifer könnte das Signal zwischen einem NFC-Gerät und einem Tag in Echtzeit weiterleiten, um eine Transaktion oder einen Zugriff aus der Ferne zu ermöglichen.
- **Tag Cloning:** Die Daten eines NFC-Tags könnten auf einen anderen Tag kopiert werden.
- **Man-in-the-Middle-Angriffe:** In Szenarien, in denen zwei aktive NFC-Geräte kommunizieren, könnte ein Angreifer versuchen, die Kommunikation abzufangen und zu manipulieren.

**Sicherheitsmaßnahmen für NFC:**

- **Verschlüsselung:** Die in NFC-Protokollen integrierten Verschlüsselungsmechanismen schützen die übertragenen Daten.
- **Sichere Elemente:** In vielen Anwendungen (z. B. kontaktloses Bezahlen) werden sensible Daten in sicheren Hardware-Elementen (Secure Elements) auf den Geräten gespeichert, die vor unbefugtem Zugriff geschützt sind.
- **Distanzbeschränkung:** Die Notwendigkeit der physischen Nähe für die Kommunikation reduziert das Risiko von Fernangriffen.
- **Transaktionsbestätigungen:** Bei finanziellen Transaktionen werden oft zusätzliche Sicherheitsmaßnahmen wie PIN-Eingaben oder biometrische Authentifizierung eingesetzt.

Zusammenfassend ist NFC eine praktische und vielseitige Technologie für die drahtlose Kommunikation über kurze Distanzen. NFC-Tags dienen als kostengünstige und energieeffiziente Datenträger, die in einer breiten Palette von Anwendungen zur Identifizierung, Authentifizierung und zum Datenaustausch eingesetzt werden. Obwohl inhärente Sicherheitsmerkmale vorhanden sind, ist es wichtig, die potenziellen Risiken zu verstehen und geeignete Sicherheitsmaßnahmen zu implementieren, um einen sicheren Einsatz der NFC-Technologie zu gewährleisten.