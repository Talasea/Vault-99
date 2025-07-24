**Was ist Verkapselung?**

Verkapselung ist eines der vier Grundprinzipien der objektorientierten Programmierung (neben Abstraktion, Vererbung und Polymorphie). Sie bezieht sich auf die Bündelung von Daten (Attribute) und den Methoden (Funktionen), die auf diesen Daten operieren, innerhalb einer einzigen Einheit, einem sogenannten Objekt.

**Hauptziele der Verkapselung:**

- **Datenverbergung (Data Hiding):**
    - Verkapselung ermöglicht es, den direkten Zugriff auf die internen Daten eines Objekts zu beschränken.
    - Dies schützt die Daten vor unbeabsichtigten oder unerwünschten Änderungen von außen.
    - Der Zugriff auf die Daten erfolgt stattdessen über definierte Schnittstellen (Methoden).
- **Modularität:**
    - Durch die Bündelung von Daten und Methoden in Objekten wird der Code modularer und besser organisierbar.
    - Objekte können als unabhängige Einheiten betrachtet und wiederverwendet werden.
- **Wartbarkeit:**
    - Wenn die internen Daten eines Objekts geschützt sind, können Änderungen an der internen Implementierung vorgenommen werden, ohne dass andere Teile des Codes beeinträchtigt werden.
    - Dies erleichtert die Wartung und Weiterentwicklung des Codes.

**Wie funktioniert Verkapselung?**

- **Zugriffsmodifizierer:**
    - Programmiersprachen wie Java, C++ und Python bieten Zugriffsmodifizierer (z. B. "private", "protected", "public"), um den Zugriff auf Attribute und Methoden zu steuern.
    - "Private" Attribute und Methoden sind nur innerhalb der Klasse selbst zugänglich, während "public" Attribute und Methoden von überall aus zugänglich sind.
- **Getter und Setter:**
    - Um auf private Attribute zuzugreifen oder sie zu ändern, werden in der Regel "Getter"-Methoden (zum Lesen) und "Setter"-Methoden (zum Schreiben) verwendet.
    - Diese Methoden bieten eine kontrollierte Schnittstelle zum Zugriff auf die Daten.

**Beispiel:**

Stellen Sie sich ein Objekt "Auto" vor. Dieses Objekt könnte Attribute wie "Farbe", "Modell" und "Kilometerstand" sowie Methoden wie "Beschleunigen()" und "Bremsen()" haben. Die Verkapselung würde sicherstellen, dass der Kilometerstand nicht direkt von außen verändert werden kann, sondern nur durch die Methode "Beschleunigen()", die auch andere notwendige Prüfungen durchführen kann.

**Zusammenfassend:**

Verkapselung ist ein wichtiges Prinzip der OOP, das dazu beiträgt, den Code sicherer, modularer und wartbarer zu machen.



**Das OSI-Modell und Verkapselung:**

Das OSI-Modell ist ein konzeptionelles Rahmenwerk, das die Funktionen eines Telekommunikations- oder Computernetzwerks in sieben Schichten unterteilt. Jede Schicht hat spezifische Verantwortlichkeiten und kommuniziert mit den Schichten darüber und darunter. Verkapselung spielt in diesem Modell eine entscheidende Rolle, da sie die Art und Weise beeinflusst, wie Daten durch die verschiedenen Schichten übertragen werden.

**Wie Verkapselung im OSI-Modell funktioniert:**

- **Datenfluss und Schichten:**
    - Wenn Daten von einer Anwendung gesendet werden, beginnen sie ihren Weg durch die Schichten des OSI-Modells.
    - In jeder Schicht werden Header-Informationen hinzugefügt, die zur Steuerung der Datenübertragung auf dieser Schicht dienen. Dies ist ein wesentlicher Aspekt der Verkapselung.
- **Header-Hinzufügung:**
    - Jede Schicht "verkapselt" die Daten der darüberliegenden Schicht, indem sie ihren eigenen Header hinzufügt.
    - Dieser Header enthält spezifische Steuerungsinformationen, die für die Funktion dieser Schicht erforderlich sind.
    - Beispielsweise fügt die Netzwerkschicht (Layer 3) einen IP-Header hinzu, der die Quell- und Ziel-IP-Adressen enthält.
    - Die Sicherungsschicht (Layer 2) fügt einen Frame Header, mit den MAC Adressen der Geräte im Netzwerk hinzu.
- **Datenkapselung:**
    - Die Daten, zusammen mit den hinzugefügten Headern, werden dann an die nächste untere Schicht weitergegeben.
    - Dieser Prozess wird fortgesetzt, bis die Daten die physikalische Schicht (Layer 1) erreichen, wo sie in ein Signal umgewandelt und über das Übertragungsmedium gesendet werden.
- **Entkapselung:**
    - Auf der Empfängerseite wird der Prozess umgekehrt.
    - Jede Schicht entfernt ihren eigenen Header und gibt die Daten an die darüberliegende Schicht weiter.
    - Dieser Prozess wird fortgesetzt, bis die ursprünglichen Daten die Anwendungsschicht erreichen.
- **Zusammenhang mit OOP-Verkapselung:**
    - Auch wenn das OSI-Model keine Objecte und Klassen wie die OOP beschreibt, ist das grundlegende Konzept ähnlich. Informationen werden in eine Kapsel gepackt, um diese vor äußeren Einflüssen zu schützen, und die Daten nur mit hilfe bestimmter Steuer informationen genutzt werden können.

**Wichtige Punkte:**

- Verkapselung im OSI-Modell ermöglicht es, dass jede Schicht ihre Aufgaben unabhängig von den anderen Schichten erfüllen kann.
- Dies trägt zur Modularität und Flexibilität des Netzwerks bei.
- Es ermöglicht auch die Standardisierung von Netzwerkprotokollen, da jede Schicht definierte Schnittstellen hat.