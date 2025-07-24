

MAC-Spoofing bezeichnet das Verschleiern der eigenen Media-Access-Control-Adresse (MAC-Adresse), die eine eindeutige Hardware-Adresse ist, die jedem Netzwerkgerät zugewiesen wird.234 Dies kann durch eine softwareseitige Maskierung erreicht werden, ohne dass die eigentliche MAC-Adresse der Hardware geändert wird.234 Nutzer können ihre MAC-Adresse ändern, um Privatsphäre zu schützen oder Netzwerkbeschränkungen zu umgehen.234

Einige Gründe, warum Nutzer ihre MAC-Adresse maskieren möchten, sind der Schutz der Privatsphäre, insbesondere in öffentlichen WLAN-Netzen, und das Umgehen von Zugangsbeschränkungen und Sicherheitsmechanismen.23 Hacker können ihre Identität verbergen oder die Identität eines anderen Netzwerkgeräts imitieren, um Zugriff auf Netzwerke zu erhalten oder Datenverkehr zu manipulieren.3

Um eine MAC-Adresse zu maskieren, können Nutzer die Netzwerkeinstellungen ihres Betriebssystems ändern. Beispielsweise unter Windows kann man die MAC-Adresse in den Netzwerkeinstellungen ändern, indem man die Netzwerkkarte auswählt und die Netzwerkadresse manuell einträgt.34 Einige Netzwerkkartentreiber bieten auch die Möglichkeit, die MAC-Adresse direkt zu ändern.4

Es ist wichtig zu beachten, dass MAC-Spoofing auch als Angriffsvektor genutzt werden kann, um Netzwerke zu gefährden. Netzwerkadministratoren können daher Maßnahmen ergreifen, um MAC-Spoofing zu verhindern, wie z.B. das Verwenden von Port-Security auf Switches, das Monitoring von MAC-Adressen oder die Implementierung von Media Access Control Security (MACSec).





# MAC Spoofing: Wie funktioniert der Angriff

1. Oktober 20226. Oktober 2022

Die MAC-Adresse soll ein eindeutiges, hardwarebezogenes Identifikationsmerkmal sein, welche durch den Hersteller zugewiesen wird. Das bezieht alle Netzwerkadapter mit ein und gilt als physische Adresse oder Geräteadresse in einem Rechnernetz. MAC steht hierbei für Media Access Control, also Geräte identifizieren sich anhand der MAC-Adresse in einem Netzwerk und steuern den Zugriff auf dieses. Eine MAC-Adresse besteht aus sechs Bytes, also 48 Bit. Die ersten drei Bytes sind herstellerspezifisch, die letzten drei Bytes sind dann zufällig gewählte Zeichen in hexadezimaler Darstellung.

Öffnet man unter Windows die CMD und gibt den Befehl **_ipconfig /all_** ein, so werden alle Netzwerkadapter aufgelistet, mit IP-Adresse und auch der MAC-Adresse (Physische Adresse) aufgelistet.

```
ipconfig /all

Ethernet-Adapter Ethernet:

   Medienstatus. . . . . . . . . . . : Medium getrennt
   Verbindungsspezifisches DNS-Suffix:
   Beschreibung. . . . . . . . . . . : Intel(R) I210 Gigabit Network Connection
   Physische Adresse . . . . . . . . : 3C-52-82-5F-67-9B
   DHCP aktiviert. . . . . . . . . . : Ja
   Autokonfiguration aktiviert . . . : Ja
```

Bei Linux und Unix erhält man eine ähnliche Ausgabe über die Kommandos _**ip -a**_ oder _**ifconfig**_.

## Vorteile von MAC Spoofing

Das Spoofing der MAC-Adresse bedeutet nicht immer nur, das jemand Böses im Schilde führt, sondern es dient auch als Mittel zum Schutz der Privatsspähre im Internet. Dies ist an sich kein illegaler Schritt. Nicht jeder möchte diese Transparenz im Netz. Dafür kann man, je nach Betriebssystem eine App oder ein Programm installieren, oder eben direkt in den Einstellungen eine zufällige MAC-Adresse zuweisen.

## MAC Spoofing als Angriffsvektor

Primär soll es aber in dem Artikel darum gehen, wie ein Angreifer durch MAC Spoofing Schaden anrichten kann. Damit man sich und das eigene Netzwerk schützen kann, muss man natürlich den Angriff dahinter verstehen. Ein Angreifer im Netzwerk, ob kabelgebunden oder WLAN ist hierbei irrelevant, kann mittels Tools wie Wireshark MAC-Adressen im Netzwerk _„sniffen“_. Weist sich der Angreifer beispielsweise die MAC-Adresse vom Empfänger zu, so ist es ihm möglich sich als dieser auszugeben und hat die Möglichkeit den Datenverkehr mitzuschneiden und zu manipulieren. Bei diesem Szenario wird auch der CAM Table (Content Addressable Memory) des Switches überschrieben. In dieser Tabelle werden MAC-Adressen und der physischen Port des Switches, über den der Teilnehmer angebunden ist, festgehalten.

Nachfolgende Skizze soll das Ganze verdeutlichen:

![MAC Spoofing](https://byte-sized.de/wp-content/uploads/2022/10/mac-spoofing.png)

Mac Spoofing Attacke

Im ersten Schritt kommuniziert PC A mit PC B. Die CAM-Tabelle ist gesetzt, so wie die Hosts auch angebunden sind. Der Hacker snifft die MAC-Adresse von PC A und weist seinem Netzwerkadapter diese zu. Jetzt sendet der Hacker, also PC C, Datenpakete an PC B mit der Quell-Adresse von PC A. Hierbei geht der Switch davon aus, dass PC A an Port 3 angebunden ist, obwohl es eigentlich der Hacker ist, der sich als PC A ausgibt. Somit wird der CAM-Table-Eintrag von PC A von Port 1 auf Port 3, also den Hacker geändert. Solange der echte PC A keine erneuten Daten an B sendet, hat der Hacker (PC C) weiterhin Zugriff auf den Datenverkehr, der ursprünglich für PC A vorgesehen war.

## Schutzmaßnahmen gegen MAC Spoofing

### Port Security

Eine schnelle Variante Access-Ports, also Ports, an denen Endgeräte am Switch angeschlossen sind, zu schützen, wäre die Konfiguration von Port Security. Bei Port Security werden MAC-Adressen in der Port-Konfiguration hinterlegt, sodass nur zugelassene MACs über diesen Port kommunizieren dürfen. Darüber habe ich bereits einen Artikel geschrieben, der [hier](https://byte-sized.de/netzwerk/wie-konfiguriert-man-port-security/) zu finden ist. Nachfolgend aber dennoch ein Beispiel dazu:

```
Switch(config)#int gi1/0/1
Switch(config-if)#switchport mode access
Switch(config-if)#switchport port-security
Switch(config-if)#switchport port-security violation shutdown
Switch(config-if)#switchport port-security maximum 1
Switch(config-if)#switchport port-security mac-address sticky
```

#### Erklärung

- Das Interface 1/0/1 in dem obigen Beispiel ist als Access-Port konfiguriert
- Port-Security ist aktiviert
- Bei Verletzung der Port Security wird das Interface abgeschaltet
- Es kann nur eine MAC-Adresse hinterlegt werden (der Wert kann, sollte aber nicht höher gesetzt werden)
- Mit dem letzten Befehl wird die MAC-Adresse dynamisch eingetragen. Sofern ein Gerät bereits angeschlossen ist, wird die zugehörige MAC direkt eingetragen und hinterlegt. Wenn man die Zeit hat oder das Risiko nicht eingehen möchte, dass vielleicht schon ein ungewollter Teilnehmer am Switch hängt, dann sucht man die zugehörige MAC vom Endgerät raus und trägt sie hinter **_„sticky“_** ein. Damit ist die Eintragung statisch erfolgt.

```
Switch(config-if)#switchport port-security mac-address sticky aaaa.bbbb.cccc
```

### Netzwerk-Monitoring

In der Regel sollte es in jedem Netzwerk eine Form von Monitoring geben. Hier hat man die Möglichkeit, sobald zwei Geräte die selbe MAC-Adresse aufweisen, einen Alarm auszulösen. Das ist in dem Sinne kein aktiver Schutz, aber man erhält Kenntnis über das MAC Spoofing und kann weitere Maßnahmen einleiten.

Beispiele für Monitoring-Software wären [Nagios](https://www.nagios.com/) oder [Zabbix](https://www.zabbix.com/).

### Reverse ARP

Ein RARP Server (Reverse Address Resolution Protocol) überprüft, ob innerhalb des Netzwerkes eine MAC mit mehreren IP-Adressen hinterlegt ist. Somit kann MAC Spoofing erkannt werden, also auch wie beim Monitoring – es ist schon geschehen, aber man bekommt es wenigstens mit.

### Implementierung von MACSec

MACSec steht (Media Access Control Security). Hierbei handelt sich um einen in der [IEEE-Norm 802.1AE](https://1.ieee802.org/security/802-1ae/) spezifizierten Sicherheitsstandard. Hierbei wird auf Layer 2 des OSI-Schichtenmodells die Vertraulichkeit und Integrität der Ethernet-Verbindungen gewährleistet. Die Funktionsweise ist an sich recht simpel: Es wird erst eine verschlüsselte Verbindung aufgebaut, sofern ein Schlüsselaustausch zwischen den zwei Schnittstellen ausgetauscht und verifiziert werden konnte. Diese Schutzmaßnahme verhindert Man-in-the-middle-Attacken (MITM), DDoS-Angriffe, Playback-Angriffe, und viele mehr.

## Abschluss

Das sollte ein kurzen Einblick darüber geben, was MAC Spoofing überhaupt ist und wie man sich erfolgreich dagegen schützen kann. Natürlich gibt es noch weitere Schutzmaßnahmen, aber das würde vermutlich den Rahmen des Artikels sprengen und eher einer Facharbeit ähneln. Es sollten zwar viele der oben genannten Schutzmaßnahmen in modernen Netzwerken implementiert sein, aber die Realität sieht leider meist ganz anders aus. IT-Sicherheit kostet dem Unternehmen Geld, Cyber-Angriffe aber auch, wenn sie nicht sogar den Bankrott bedeuten.