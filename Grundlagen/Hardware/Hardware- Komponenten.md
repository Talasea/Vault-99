
## Prozessor

Der **Prozessor** (auch **CPU**, also **Central Processing Unit**) genannt, ist das **Gehirn** des Computers.

Hier werden die **Befehle
interpretiert** und **ausgeführt**. Außerdem werden hier **Abläufe koordiniert**.

Wie du merkst, funktioniert ohne den Prozessor nichts.

Außerdem bestimmt die **Taktfrequenz** deines Prozessors, wie lang die **Rechenzeit** ist, also wie schnell oder langsam dein Computer ist. Sie wird in **Mega- oder Gigaherz** angegeben.



![[cpu-tower_3849739.png]]
## Speicher

Damit der Prozessor mit **Daten arbeiten** kann, benötigt er einen **Speicher**. Dabei unterscheidet man zwischen **Hauptspeicher** und **Sekundärspeicher**.

### Hauptspeicher

Der **Hauptspeicher** (auch **RAM**, also **Random Access Memory**) **verwaltet die Daten**, mit denen der Rechner **gerade** arbeitet.

Dieser Hauptspeicher wird unterteilt in mehrere **Speicher-Ebenen**. Für diese Ebenen gilt folgendes Prinzip: Je **kleiner** der Speicher ist, desto **schneller** kann auf die Daten zugegriffen werden. Aber dafür können dort natürlich weniger Daten gespeichert werden.

Im Umkehrschluss gilt also: Je **größer** der Speicher ist, also je mehr Daten gespeichert werden können, desto **langsamer** ist der Zugriff auf die Daten.

Die **Geschwindigkeit** deines Rechners hängt also auch von der **Größe** des Arbeitsspeichers ab.![[icons8-ram-64.png]]

## Motherboard

Der Prozessor, der Hauptspeicher, diverse Steckplätze und das Bussystem sind auf dem **Motherboard** (auch **Mainboard** oder **Hauptplatine**) platziert. Dadurch haben alle Elemente einen **festen Platz** und können über Verbindungen miteinander **kommunizieren**.

Dabei sind jedoch auch viele Komponenten, wie die Sound- und Netzwerkkarten oder die Standardanschlüsse bereits **fest** auf dem Motherboard integriert und können so nicht mehr ausgetauscht werden, wie es bei den anderen Komponenten der Fall ist.

Der Arbeitsspeicher liegt zur besseren Übersicht auf der Seite, denn normal steckt er in einem der dafür vorgesehenen Steckplätze.![[hauptplatine.png]]




### Gpu 

Die GPU (Graphics Processing Unit) ist ein spezieller Prozessor, der sich auf die Berechnung von Grafiken und visuellen Daten spezialisiert hat. Sie ist ein wichtiger Bestandteil einer Grafikkarte und übernimmt die Verarbeitung von Grafikaufgaben, wie zum Beispiel:

- Bildbearbeitung und -rendering
- 2D- und 3D-Grafiken
- Video- und Audio-Dekodierung
- Physik-Simulationen (z.B. in Spielen)

Die GPU ist im Gegensatz zur CPU (Central Processing Unit) speziell auf die parallele Verarbeitung von Grafik-Daten ausgelegt. Sie verfügt über viele Rechenkerne, die gemeinsam arbeiten, um komplexe Grafikoperationen auszuführen. Dies ermöglicht es, dass Grafikkarten viel schneller und effizienter als CPUs Grafikaufgaben bearbeiten können.

## Komponenten einer GPU

Eine moderne GPU besteht aus verschiedenen Komponenten, wie:

- **GPU-Prozessor** (Graphics Processing Unit): Der eigentliche Grafikprozessor, der die Grafikberechnungen durchführt.
- **Grafikspeicher** (Video Memory): Ein separates Speicherbereich, in dem die verarbeiteten Grafik-Daten abgelegt werden.
- **RAMDAC** (Random Access Memory Digital-to-Analog Converter): Ein Konverter, der die digitalen Grafik-Daten in analoge Signale umwandelt, um sie auf den Monitor zu übertragen.
- **Anschlüsse** (Interfaces): Schnittstellen, über die die GPU mit externen Geräten wie Monitoren oder Grafiktabletts verbunden werden kann.

## Funktionen einer GPU

Eine GPU kann folgende Funktionen ausführen:

- **3D-Grafikrendering**: Die Verarbeitung von 3D-Modellen und die Erstellung von Bildern auf Basis von 3D-Daten.
- **Video-Dekodierung**: Die Entschlüsselung und Wiedergabe von komprimierten Videodateien.
- **Physik-Simulationen**: Die Simulation von physikalischen Effekten wie Licht, Schatten, Bewegung und Kollisionen in Spielen und Anwendungen.
- **GPGPU** (General-Purpose Computing on Graphics Processing Units): Die Verwendung von GPUs als allgemeine Rechenmodule für nicht-grafikbezogene Aufgaben, wie z.B. Datenanalyse oder Kryptographie               .![[gpu.png]]


# Festplatte / Harddisk

Festplatten sind Massenspeicher, die auf einem magnetischen Datenträger beruhen, auf dem die Daten fest gespeichert werden und auch ohne Energieversorgung gespeichert bleiben. Festplatten werden typischerweise in einen Computer eingebaut. Auf Festplatten werden alle Daten und Anwendungen eines Computers gespeichert.

**![Harddisk / Festplatte mit Schutzdeckel](https://www.elektronik-kompendium.de/sites/com/fotos/06102911.jpg)Fesplatte**

**![Harddisk / Festplatte ohne Schutzdeckel](https://www.elektronik-kompendium.de/sites/com/fotos/06102912.jpg)Festplatte (geöffnet)**

Der Begriff Festplatte (engl. Harddisk bzw. Hard Density Disc, HDD) kommt durch die Unterscheidung zur inzwischen veraltete Diskette (engl. Floppydisk, FDD), die als wechselbarer Datenträger lange Zeit vor der Festplatte verwendet wurde. Die Festplatte ist durch ihre Art, fest in das Gehäuse eines Computers eingebaut zu sein, benannt worden.  
Festplatten ersetzen den Festwertspeicher ROM und die Diskette. Festplatten können viel mehr Daten speichern als Disketten. Im Gegensatz zum ROM kann man Daten von einer Festplatte nicht nur lesen, sondern auch darauf schreiben und jederzeit ändern.  
1954 wurden Festplatten erstmals industriell eingesetzt. Seit dem hat sich sehr viel getan. Vor allem die Speicherdichte führte zu der uns heute bekannten Speicherkapazität. Im Prinzip funktioniert die heutige Festplatte genauso wie die ersten Modelle.



#### Soundkarte
## Prinzipielle Funktionsweise einer Soundkarte

[![](http://audio-lexikon.com/wp-content/uploads/2014/11/funktionsweise-soundkarte.png)](http://audio-lexikon.com/wp-content/uploads/2014/11/funktionsweise-soundkarte.png)

**Abbildung 2**: Prinzipielle Funktionsweise einer Soundkarte eine Manipulation der Samples kann intern per DSP oder extern in der CPU des Computers erfolgen.

Abbildung 2 zeigt die rudimentäre Funktionsweise einer Soundkarte, egal welcher Bauart. Über den Input (Mic- /Line-Eingang) gelangt ein analoges Audiosignal, eine Wechselspannung, in die Soundkarte. Handelt es sich um ein Mikrofonsignal muss dieses noch per _Preamp_ verstärkt werden. Ein Line-Signal (z.B. aus dem Keyboard) ist bereits laut genug und würde bei Verstärkung _Clippen_. Anschließend wird die Spannung per [AD-Wandlung](http://audio-lexikon.com/analog-digital/ad-und-da-wandler/ "A/D und D/A Wandler") in ein binäres Signal umgewandelt. Jene Samples können nun _intern_ in der Soundkarte mittels ihres **D**igitalen **S**ignal **P**rozessors bearbeitet werden (Es könnte hier zum Beispiel ein Hall beigefügt werden). Soll die Bearbeitung mittels des CPU erfolgen, so werden die Samples an diesen mit einer bestimmten _Sample Buffer Size_ (SBS)per Datenbus (z.B. PCI) weitergereicht. Bei guten Soundkarten lässt sich die Sample Buffer Size einstellen, hierbei muss ein Kompromiss aus zwei verschiedenen Fakten gefunden werden:

1. Wird die SBS zu groß gewählt kommt es zu Latenzen, da Änderungen am Audiomaterial erst später in den nächsten Buffer kommen (bei kleiner Buffersize ist quasi die Frequenz der Bearbeitung höher).
2. Wird die SBS zu klein gewählt kommt es zwar zu geringen Latenzen, es kann jedoch sein, dass der Computer mit dem Schreiben (bei der Audiowiedergabe) bzw. mit dem Lesen (bei der Audioaufnahme) der Samples nicht hinterherkommt — es entstehen plötzliche Momente der Stille welche sich auf Grund von drastischen Audiosprüngen als Plops oder Knackser bemerkbar machen.

Über den Kontrollbus einer Soundkarte lässt sich zum Einen ein interner Mixer direkt ansteuern (falls dieser vorhanden ist), zum anderen lassen sich per MIDI Schnittstelle Befehle an eine **D**igital **A**udio **W**orkstation geben.

Die Samplingrate einer Soundkarte gibt an, wie oft die AD-Wandler ein analoges Signal pro Sekunde abtasten können. Eine hohe Samplingrate macht unter Umständen bei der Audiobearbeitung Sinn, siehe hierfür unseren Artikel [A/D-Wandler und D/A-Wandler](http://audio-lexikon.com/analog-digital/ad-und-da-wandler/ "A/D und D/A Wandler").

Die Bauart einer Soundkarte beschreibt, ob es sich um eine interne oder externe Soundkarte handelt. Im folgenden wird zunächst die externe und dann die interne Soundkarte berschrieben.

## Externe Soundkarten

Externe Soundkarten erfreuen sich besonderer Beliebtheit, da sie a) auch einem Notebook jegliche Audiofunktionalität verleihen können ohne auf dessen bescheidene Platzverhältnisse(Stichwort PCMCIA) beschränkt zu sein und b) das Problem interner Soundkarten von elektromagnetischen Feldern umgeben zu sein(Stichwort Brummen) durch örtliche Verlagerung lösen.

### Aufbau

Die prinzipielle Funktionsweisen interner und externer Soundkarten unterscheiden sich nicht, externe Soundkarten werden jedoch per FireWire oder USB am PC / Notebook angeschlossen. Hierdurch können auch Notebooks ohne PCMCIA mit den Funktionen einer guten Audiokarte ausgestattet werden.

#### Eingänge und Ausgänge

Meist beinhaltet eine externe Soundkarte folgende Eingänge:

- Mic-In (durch einen Preamp ist es so möglich, einen geringen Pegel auf Line-Niveau zu verstärken) — meist als XLR-Eingang
- Line-In: Hier kann z.B. ein Keyboard angeschlossen werden, welches über einen Pegel verfügt der nichtmehr verstärkt werden muss (Line-Pegel) — meist als Klinken-Eingang
- Instrumenten-In: Hier kann z.B. das Klinke-Kabel einer Gitarre angeschlossen werden. Wie beim Mikrofon ist der Pegel hier noch sehr niedrig, er muss verstärkt werden.
- Digitale/Optischer Eingänge:  Per S/PDIF (**S**ony/**P**hilips **D**igital **I**nterface) können Daten auch digital bzw. optisch übertragen werden: So kommt es zu keinerlei Signalveränderung durch AD- bzw. DA-Wandlung und Preamps.

Zum anderen gibt es [symmetrische](http://audio-lexikon.com/anschlusstechnik/symmetrische-und-unsymmetrische-signalfuehrung/ "Symmetrische und unsymmetrische Signalführung") Monitorausgänge, welche eine Brummfreie Audiowiedergabe garantieren. Auch S/PDIF gibt es als Ausgangsvariante, hierdurch können an andere digitale Geräte Samples ohne Qualitätsverlust weitergegeben werden. In teuren Soundkarten gibt es meist mehrere Ausgänge um verschiedene Abhörmonitore anschließen zu können, um so einen möglichst neutralen Mix vollführen zu können.

#### Netzwekkarte


Netzwerkkarte erklärt

Eine Netzwerkkarte, auch als Network Interface Card (NIC) oder Network Adapter bezeichnet, ist eine elektronische Schaltung in einem Computer, die die Verbindung zwischen dem Computer und einem Netzwerk ermöglicht. Sie ermöglicht den Austausch von Daten zwischen Geräten über ein Netzwerk, wie zum Beispiel einem lokalen Netzwerk (LAN) oder dem Internet.

## Aufgaben einer Netzwerkkarte

Eine Netzwerkkarte übernimmt folgende Aufgaben:

1. **Datenübertragung**: Sie wandelt digitale Signale vom Computer in ein formatumgewandeltes Signal um, das über Netzwerkschnittstellen, wie kabelgebundene oder drahtlose Netzwerke, gesendet werden kann.
2. **Adressierung**: Sie verantwortet die Adressierung von Datenpaketen durch die Verwendung von MAC-Adressen (Media Access Control), die eindeutig für jede Netzwerkkarte sind.
3. **Netzwerkkommunikation**: Sie verwaltet die Netzwerkkommunikation, um einen reibungslosen Datenaustausch sicherzustellen.

## Arten von Netzwerkkarten

Es gibt verschiedene Arten von Netzwerkkarten, wie:

1. **Ethernet-Karten**: für kabelgebundene Verbindungen über Ethernet-Kabel
2. **WLAN-Karten** (Wireless Local Area Network): für drahtlose Verbindungen über Wi-Fi
3. **PCI-Netzwerkkarten**: als separate Erweiterungskarten für ältere Computer
4. **USB-Netzwerkkarten**: als externe Geräte über USB-Anschlüsse

## Integration in den Computer

Netzwerkkarten sind in der Regel als feste Komponenten auf dem Motherboard integriert oder können als separate Erweiterungskarten installiert werden. Moderne Computer und mobile Geräte haben oft bereits integrierte Netzwerkkarten.

## Fazit

Eine Netzwerkkarte ist eine wichtige Hardware-Komponente, die die Verbindung zwischen einem Computer und einem Netzwerk ermöglicht und den Datenaustausch zwischen Geräten sicherstellt. Sie ist für die Funktionsfähigkeit von Netzwerken und dem Zugriff auf das Internet und andere Netzwerkressourcen unerlässlich.


## Busse
https://studyflix.de/informatik/bus-system-6108

Die **Busse** stellen die **Verbindungselemente** zwischen Prozessor, Hauptspeicher und den Ein- und Ausgabegeräten dar.

Sie dienen dabei der **Kommunikation**, also der **gemeinsamen Datenübertragung**, zwischen den Komponenten.

Wenn jetzt beispielsweise zwei Komponenten miteinander kommunizieren, dann dürfen in der Zeit **keine** anderen Komponenten Daten über diesen Bus schicken, da sie sonst **stören** würden.

Die Komponenten wissen durch ein bestimmtes **Signal-** oder **Zeit-Schema**, wann sie "sprechen" dürfen, damit solche Störungen vermieden werden.


# 

##### Acu erklärt

Die Abkürzung ACU steht für “Access Control Unit”, was eine Einheit zur Steuerung und Überwachung des Zugriffs auf Ressourcen, wie z.B. Räume, Geräte oder Daten, darstellt. ACUs werden in verschiedenen Bereichen eingesetzt, wie zum Beispiel:

- IT-Sicherheit: ACUs können verwendet werden, um den Zugriff auf Netzwerke, Server oder Anwendungen zu regulieren und zu überwachen.
- Gebäudetechnik: ACUs können in Gebäuden eingesetzt werden, um den Zugriff auf Räume, wie z.B. Lagerräume oder Serverräume, zu steuern und zu überwachen.
- Industrielle Automatisierung: ACUs können in industriellen Anwendungen eingesetzt werden, um den Zugriff auf Maschinen, Anlagen oder Prozesse zu regulieren und zu überwachen.

Insgesamt dienen ACUs dazu, den Zugriff auf kritische Ressourcen zu kontrollieren und zu überwachen, um die Sicherheit und Integrität von Systemen und Anwendungen zu gewährleisten.




Wo sitzt was im Pc : https://www.wintotal.de/mainboard-anschluesse/ 

