
# Sicherheitsschlüssel für die Multifaktor-Authentifizierung: Hardware-Token im Überblick

USB-Sicherheitsschlüssel sind eine sinnvolle Ergänzung zur Kennworteingabe bei Online-Services. Die Zwei-Faktor-Authentifizierung sichert Ihre Online-Konten ab und nimmt Cyberkriminellen den Wind aus den Segeln.

![Seitenansicht Hände auf Laptop-Tastatur](https://www.onlinesicherheit.gv.at/dam/jcr:109550e3-8a31-48a1-ab7b-ff2f267797ed/Sicherheitsschluessel_460x323.png)

Krypto-Schlüssel. Foto: Adobe Stock

Eine etablierte Methode für die passwortfreie Anmeldung bei Online-Services ist die Nutzung eines digitalen Sicherheitsschlüssels (Krypto-Schlüssel, Hardware-Token, Security-Token, Token-Generator, USB-Token, Authenticator). Dabei handelt es sich meist um einen kleinen Apparat in Form eines Schlüsselanhängers oder USB-Sticks. Je nach zugrundeliegender Technologie generiert dieser entweder einen auf dem Display angezeigten Einmalcode zur Eingabe oder er wird als Zwei-Faktor-Hardware (FIDO) an den Computer angeschlossen, um sich im Rahmen einer [Mehrfaktor-Authentifizierung](https://www.onlinesicherheit.gv.at/Themen/Praevention/Konten-und-Passwoerter/Mehrfaktor-Authentifizierung.html "Öffnet in einem neuen Fenster") bei Online-Services anzumelden.

In Kombination mit dem üblichen Login-Verfahren, einer PIN-Eingabe oder einer [biometrischen Authentifizierung](https://www.onlinesicherheit.gv.at/Services/News/Biometrische-Authentifizierung.html "Öffnet in einem neuen Fenster") bieten Sicherheitsschlüssel einen effektiven Schutz für Online-Zugänge. Wird neben der Passwort-Eingabe (Faktor Wissen) ein USB-Sicherheitsschlüssel (Faktor Besitz) verwendet, liegt eine [Zwei-Faktor-Authentifizierung](https://www.onlinesicherheit.gv.at/Services/Technologie-Schwerpunkte/Sichere-Passwoerter/Zwei-Faktor-Authentifizierung.html "Öffnet in einem neuen Fenster") vor.

##  Hinweis

Welche Methoden bei einer Mehrfaktor-Authentifizierung zum Einsatz kommen können, erfahren Sie im Beitrag „[Mehrfaktor-Authentifizierung: Überblick über die verschiedenen Technologien](https://www.onlinesicherheit.gv.at/Services/News/Mehrfaktor-Authentifizierung-Ueberblick.html "Öffnet in einem neuen Fenster")“.

## **Sicherheitsschlüssel oder Token? Was ist ein Token?**

Der Begriff „Token“ hat je nach Einsatzgebiet (Authentifizierungen, Kryptowährung, Netzwerk-Technologie) unterschiedliche Bedeutungen. Im Kontext von Authentifizierungssystemen bezeichnet Token meist einen einmaligen und häufig zeitlich limitierten Nachweis für eine Zugriffsberechtigung. Dabei fungiert ein Token als Code, der die Identität der Inhaberin oder des Inhabers verifiziert. Häufig werden zum Generieren von Token kleine Hardware-Komponenten in Form eines Schlüsselanhängers verwendet. Alternativ ist die Bezeichnung "Sicherheitsschlüssel" möglich. 

##  Hinweis

Eine allgemeine Einführung in das Thema Kryptowährung sowie die zugrundeliegende Blockchain-Technologie finden Sie im Beitrag „[Kryptowährung: Nutzen und Risiken des digitalen Geldes](https://www.onlinesicherheit.gv.at/Services/News/Kryptowaehrung_digitales-Geld.html "Öffnet in einem neuen Fenster")“.

## **Wie funktioniert ein Hardware-Token?**

Die Handhabung eines Sicherheitsschlüssels unterscheidet sich je nach Modell und dem verwendeten kryptografischen Verfahren:

So kann das Hardware-Token nach Betätigung einer Taste ein Einmalpasswort (Time-based One-Time Password; TOTP) generieren. Dieses wird auf einem kleinen Display angezeigt und muss beim jeweiligen Online-Service angegeben werden. Beim Systemverwalter des Online-Services arbeitet derselbe Algorithmus wie auf dem Sicherheitsschlüssel, weshalb für ein definiertes Zeitintervall auf beiden Seiten ein identischer Code vorliegt. Die Userin oder der User gibt die Kennung ein und wird nach einem erfolgreichen Abgleich authentifiziert.

Alternativ wird ein Token (zum Beispiel FIDO) als Zwei-Faktor-Hardware via USB an das IT-Gerät angeschlossen, um sich zu authentifizieren. Ebenso sind der Anschluss des Tokens an den Computer sowie die Datenübertragung anstelle von USB auch kontaktlos über die Bluetooth-Schnittstelle (etwa über Bluetooth Low Energy) oder via NFC durchführbar. Dabei kommt eine asymmetrische Verschlüsselung im Public-Key-Verfahren (Public-Key-Infrastruktur; PKI) zum Einsatz, bei dem keine sensiblen Daten ausgetauscht werden. Stattdessen wird mithilfe eines speziellen Algorithmus ein Schlüsselpaar erzeugt: Nachrichten, die mit dem öffentlichen Schlüssel verschlüsselt wurden, können nur mit dem privaten Schlüssel entschlüsselt werden. Umgekehrt kann nur eine mit dem privaten Schlüssel signierte Nachricht mit dem dazugehörigen öffentlichen Schlüssel verifiziert werden. Im Beispiel von FIDO verbleibt der private Schlüssel auf dem Hardware-Token der Userin oder des Users, während der öffentliche Key beim jeweiligen Online-Dienst vorliegt und die Authentifizierung ermöglicht.

##  Hinweis

Der Authenticator, der das Einmalpasswort generiert, operiert im Idealfall unabhängig von dem Gerät, mit dem Sie sich anmelden wollen. TOTP-Generatoren gibt es als Software- oder Hardware-Lösungen. Neben Open-Source-Apps wie FreeOTP bieten auch große Unternehmen wie Google entsprechende Funktionen an, wie zum Beispiel den [Google Authenticator](https://www.onlinesicherheit.gv.at/Services/News/Google-Authenticator-einrichten.html "Öffnet in einem neuen Fenster").

## **Sicherheitsschlüssel: Einsatzgebiete und Nutzen**

Anwendung finden Security-Token als Komponente der Multifaktor-Authentifizierung häufig in Umgebungen mit hohen Sicherheitsstandards, zum Beispiel im Unternehmensumfeld. Prinzipiell erfüllen Software-Token, die etwa über eine App am Smartphone ausgespielt werden, dieselbe Aufgabe wie Hardware-Token. Ein weitaus höheres Sicherheitsniveau liegt jedoch vor, wenn der Sicherheitsschlüssel physisch von IT-Systemen getrennt ist, die mit dem Internet verbunden sind.

Krypto-Schlüssel sind eine effektive Maßnahme gegen klassische Angriffsvektoren wie Man-in-the-Middle-Attacken und [Phishing](https://www.onlinesicherheit.gv.at/Services/Cybermonitor/Phishing.html "Öffnet in einem neuen Fenster"). Selbst wenn die Login-Daten von Cyberkriminellen gestohlen werden, kann eine Anmeldung nur über den Sicherheitsschlüssel erfolgen. Zahlreiche Online-Services bieten eine zusätzliche Absicherung mittels Sicherheitsschlüssel für die Zwei-Faktor-Authentifizierung an. Dazu zählen beispielsweise:  

- Microsoft (Windows)
- Google
- Krypto-Handelsbörsen
- Social Media (Facebook, Instagram, Twitter, YouTube)
- Internet-Browser
- Password-Manager
- Online-Händler (eBay, Amazon)

## **FIDO Sicherheitsschlüssel: Universal Second Factor (U2F) und FIDO2**

FIDO Universal Second Factor (FIDO U2F), FIDO Universal Authentication Framework (FIDO UAF) und FIDO2 sind von der FIDO-Allianz und dem W3C (World Wide Web Consortium; Standardisierungsgremium für das Internet) entwickelte, nichtkommerzielle Standards, welche die passwortfreie Identifikation einer Userin oder eines Users ermöglichen. Für gewöhnlich wird der FIDO-Krypto-Schlüssel jedoch neben der Passwort-Eingabe als zweiter Sicherheitsfaktor herangezogen.  

##  Tipp

Hardware-Token sind eine praktische und sichere Alternative oder Ergänzung zur herkömmlichen Kennwort-Eingabe. Welche weiteren Möglichkeiten es hierbei gibt, lesen Sie im Beitrag „[Authentifizierung ohne Passwort: Kennwortlose Login-Methoden im Überblick](https://www.onlinesicherheit.gv.at/Services/News/Authentifizierung-ohne-Passwort.html "Öffnet in einem neuen Fenster")“.

## **Wie funktioniert der Sicherheitsschlüssel FIDO2?**

Mit FIDO2 können Sie sich unkompliziert gegenüber Webdiensten authentifizieren, wenn der Sicherheitsschlüssel zuvor mit dem Account gekoppelt wurde. Dabei kann FIDO2 prinzipiell auch ohne Hardware-Komponente genutzt werden, da ein entsprechender Sicherheitschip bereits in vielen Smartphones (Secure Element) und neueren PC-Systemen (Trusted Platform Module; TPM) integriert ist. Der Sicherheitsschlüssel unterstützt neben USB auch kontaktlose Übertragungsprotokolle wie NFC (Near Field Communication) und BLE (Bluetooth Low Energy). Alternativ können Sie spezielle USB-Sticks verschiedener Anbieter (SoloKeys, YubiKey, Nitrokey) verwenden.

Für eine Anmeldung mittels FIDO2 werden zwei Komponenten benötigt: Zunächst muss der Browser per JavaScript eine Anmeldung via FIDO2-Hardware ermöglichen. Dieser Vorgang wird über die vom W3C verwaltete Schnittstelle WebAuthn (Web Authentication) geregelt. Die zweite Komponente ist der USB-Stick beziehungsweise der im PC, Notebook oder Smartphone eingebaute Sicherheitschip. Das zugrundeliegende Sicherheitsprotokoll heißt „Client to Authenticator Protocol“ (CTAP).

Schematisch erfolgt eine FIDO2-Anmeldung in folgenden Schritten:

- Die Userin oder der User registriert sich bei einem Online-Dienst. FIDO2 erzeugt dabei ein Schlüsselpaar – bestehend aus einem privaten Schlüssel (Private Key) und einem öffentlichen Schlüssel (Public Key).
- Der private Schlüssel ist auf dem Hardware-Token gespeichert und ausschließlich der Nutzerin beziehungsweise dem Nutzer bekannt. Der Public Key hingegen wird in der Datenbank des Online-Dienstes hinterlegt.
- Die Überprüfung der Identität erfolgt mittels Challenge-Response-Verfahren: Der Server schickt einen Zeichen-Code, der im Sicherheitschip mithilfe des privaten Schlüssels signiert und zurückgeschickt wird. Der Internet-Browser vermittelt dabei zwischen Systemserver und Sicherheitschip beziehungsweise FIDO2. Der Server überprüft, ob die Userin oder der User den dazugehörigen privaten Schlüssel für die übermittelte Signatur besitzt.
- Zukünftige Anmeldungen erfolgen über den Nachweis des privaten Schlüssels durch Aktivierung des Hardware-Tokens. Userinnen und User melden sich bei einem Online-Dienst an, indem sie ihre Anmeldedaten eingeben und den Sicherheitsschlüssel an das Gerät anschließen.

##  Hinweis

Biometrische Daten kommen häufig bei Mehrfaktor-Authentifizierungen zum Einsatz. Erfahren Sie mehr über die biometrische Authentifizierung und Sicherheitsaspekte in den Beiträgen „[Biometrische Gesichtserkennung: Funktionsweise und Sicherheit](https://www.onlinesicherheit.gv.at/Services/News/Biometrische-Gesichtserkennung.html "Öffnet in einem neuen Fenster")“ und „[Fingerabdruck-Sensor: Wenn der Finger zum Schlüssel wird](https://www.onlinesicherheit.gv.at/Services/News/Fingerabdruck-Sensor.html "Öffnet in einem neuen Fenster")“.