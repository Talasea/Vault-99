
Eine MAC-Adresse (Media Access Control-Adresse) ist eine eindeutige Identifikationsnummer, die jedem Netzwerkadapter in einem Rechnernetz zugewiesen wird. Sie dient als physische Adresse und ermöglicht die eindeutige Identifikation eines Geräts in einem Netzwerk.

- **Aufbau einer MAC-Adresse**: Eine MAC-Adresse besteht aus 6 Byte (48 Bit) und ist in einer bestimmten Reihenfolge aufgebaut. Die ersten zwei Bits geben Auskunft über die Adressart, zum Beispiel ob es sich um eine Einzel- oder Gruppenadresse handelt.
- **Funktion einer MAC-Adresse**: Die MAC-Adresse ermöglicht die eindeutige Identifikation eines Geräts in einem Netzwerk und ermöglicht die Zuordnung von Datenpaketen zu dem entsprechenden Gerät.
- **Darstellungsformen von MAC-Adressen**: MAC-Adressen können in verschiedenen Darstellungsformen angezeigt werden, zum Beispiel in der kanonischen Form (z.B. 12-34-56-00-00-80) oder als Bitfolge (z.B. 01001000 00101100 01101010 00000000 00000000 00000001).
- **Herstellererkennung**: Jede MAC-Adresse enthält eine Herstellererkennung, die es ermöglicht, den Hersteller des Netzwerkadapters zu identifizieren.
- **Einzigartigkeit**: MAC-Adressen sind weltweit einzigartig und ermöglichen die eindeutige Identifikation eines Geräts in einem Netzwerk.



Detail erklärung 

https://www.dr-datenschutz.de/mac-adressen-aufbau-funktion-und-gefahren-im-netzwerk/



**Aufbau einer MAC-Adresse:**

- Eine MAC-Adresse besteht aus 48 Bits, was 6 Bytes entspricht.
- Sie wird in der Regel in hexadezimaler Form dargestellt, um sie für Menschen lesbarer zu machen.
- Die hexadezimale Darstellung bedeutet, dass jede Ziffer oder jeder Buchstabe eine Kombination von 4 Bits repräsentiert.

**Darstellungsformate:**

- Die gebräuchlichste Form ist die Darstellung in sechs durch Doppelpunkte oder Bindestriche getrennte hexadezimale Oktette.
    - Beispiel: `00:1A:2B:3C:4D:5E` oder `00-1A-2B-3C-4D-5E`
- Manchmal wird auch eine Darstellung in dreier Gruppen durch Punkte getrennt benutzt.
    - Beispiel: `001A.2B3C.4D5E`

**Bedeutung der Bestandteile:**

- Die ersten 24 Bits (die ersten drei Oktette) werden als OUI (Organizationally Unique Identifier) bezeichnet. Dieser Teil identifiziert den Hersteller des Netzwerkadapters.
- Die letzten 24 Bits werden vom Hersteller vergeben und stellen die eindeutige Seriennummer des Netzwerkadapters dar.

**Wichtige Punkte:**

- MAC-Adressen sind hardwareseitig festgelegt und in den Netzwerkadapter eingebettet.
- Sie dienen der Identifizierung von Geräten im lokalen Netzwerk (LAN).
- Im Gegensatz zu IP-Adressen, die logische Adressen sind und sich ändern können, sind MAC-Adressen physische Adressen, die in der Regel unveränderlich sind.
- Die MAC-Adresse arbeitet auf schicht 2 des OSI Modells, und wird deshalb für die direkte kommunikation im Lokalen netzwerk verwendet.