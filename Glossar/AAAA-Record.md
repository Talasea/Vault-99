# AAAA-Record

## 1. Kerndefinition

Ein **AAAA-Record** (auch Quad-A-Record genannt) ist ein Eintragstyp im Domain Name System (DNS), der einen Host- oder Domainnamen auf eine **IPv6-Adresse** abbildet. Er ist das direkte Gegenstück zum A-Record, der für IPv4-Adressen zuständig ist, und spielt eine entscheidende Rolle bei der Einführung und Nutzung des modernen Internet-Protokolls IPv6.

## 2. Detaillierte Erläuterung / Funktionsweise

Die Funktionsweise des AAAA-Records ist analog zum A-Record, jedoch für den wesentlich größeren Adressraum von IPv6 ausgelegt.

### 2.1 Schlüsselkomponenten

Ein AAAA-Record enthält:

- **Hostname:** Der aufzulösende Name (z. B. `www`, `ftp`).
    
- **TTL (Time To Live):** Die Cache-Dauer des Eintrags in Sekunden.
    
- **Typ:** `AAAA`
    
- **Wert:** Die 128-Bit-IPv6-Adresse (z. B. `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
    

Der Name "AAAA" leitet sich humorvoll davon ab, dass eine 128-Bit-IPv6-Adresse viermal so lang ist wie eine 32-Bit-IPv4-Adresse, und "AAAA" ist viermal "A".

### 2.2 Prozess und Zweck

In einem modernen, "dual-stack" fähigen Netzwerk (das sowohl IPv4 als auch IPv6 unterstützt) läuft der Prozess wie folgt ab:

1. Ein Client möchte die Domain `www.beispiel.com` erreichen.
    
2. Er fragt beim DNS-Server sowohl den A-Record (für IPv4) als auch den AAAA-Record an.
    
3. Der DNS-Server liefert beide Adressen, sofern sie existieren.
    
4. Moderne Betriebssysteme **bevorzugen in der Regel die IPv6-Verbindung**. Der Client versucht also zuerst, über die via AAAA-Record erhaltene IPv6-Adresse eine Verbindung aufzubauen. Schlägt dies fehl, greift er auf die IPv4-Adresse aus dem A-Record zurück (Fallback).
    

## 3. Einordnung in den Gesamtkontext

Der AAAA-Record ist ein unverzichtbarer Bestandteil der **IPv6-Infrastruktur** und der globalen Strategie zur Ablösung des knappen IPv4-Adressraums.

- **Dual-Stack:** In der Übergangsphase betreiben die meisten Server und Netzwerke IPv4 und IPv6 parallel. Daher sind für die meisten Domains sowohl A- als auch AAAA-Records konfiguriert, um die Erreichbarkeit für alle Nutzer zu gewährleisten.
    
- **IPv6-only-Netzwerke:** In reinen IPv6-Netzwerken (z. B. in einigen modernen Mobilfunknetzen) ist der AAAA-Record die einzige Möglichkeit zur Namensauflösung. Fehlt er, ist eine Webseite oder ein Dienst nicht erreichbar.
    

## 4. Sicherheitsaspekte

Die Sicherheitsrisiken sind identisch mit denen von A-Records, insbesondere **DNS-Spoofing** und **Cache Poisoning**. Ein Angreifer könnte einen gefälschten AAAA-Record einschleusen, um den Verkehr auf einen von ihm kontrollierten IPv6-Server umzuleiten. Der Schutz durch **DNSSEC** ist daher für AAAA-Records genauso wichtig wie für A-Records. Fehlkonfigurationen (z. B. ein AAAA-Record, der auf einen nicht erreichbaren Server verweist) können zudem zu langen Ladezeiten oder Verbindungsabbrüchen führen, da Clients erst den Timeout der IPv6-Verbindung abwarten müssen, bevor sie auf IPv4 zurückgreifen.

## 5. Praxisbeispiel / Analogie

Wenn der A-Record einer Adresse im **alten Stadtplan (IPv4)** entspricht, ist der AAAA-Record die Adresse in einem **neuen, globalen GPS-Koordinatensystem (IPv6)**. Dieses neue System ist viel detaillierter und hat unendlich viele Adressen zur Verfügung. Ein modernes Navigationsgerät (Client) wird immer versuchen, die präzisere GPS-Koordinate zu verwenden, wenn es die Wahl hat. Nur wenn das nicht möglich ist, greift es auf den alten Stadtplan zurück.

## 6. Fazit / Bedeutung für IT-Profis

Angesichts der Erschöpfung des IPv4-Adressraums ist der AAAA-Record kein Nischen-Thema mehr, sondern ein zentraler Bestandteil einer zukunftssicheren IT-Infrastruktur. Für Administratoren ist die korrekte Konfiguration von AAAA-Records unerlässlich, um die globale Erreichbarkeit ihrer Dienste sicherzustellen und die volle Leistungsfähigkeit moderner Netzwerke zu nutzen.