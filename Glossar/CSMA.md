**CSMA/CD: Carrier Sense Multiple Access with Collision Detection**

CSMA/CD ist ein **Medienzugriffsverfahren**, das hauptsächlich in **verbindungsorientierten Netzwerken** (wie z.B. dem ursprünglichen **Ethernet** in Bus- oder Hub-Topologien) eingesetzt wurde, in denen sich mehrere Geräte ein gemeinsames Übertragungsmedium teilen. Es ist eine Methode, um zu regeln, wie diese Geräte auf das gemeinsame Medium zugreifen, um **Datenkollisionen zu vermeiden oder zu behandeln**, falls sie auftreten.

**Grundprinzip: "Höre zuerst, sprich dann, und erkenne, wenn es kracht!"**

CSMA/CD basiert auf drei Hauptkomponenten:

1. **Carrier Sense (CS) - Trägerprüfung (Abhören des Mediums):**
    
    - Bevor ein Gerät (z.B. ein Computer) Daten über das Netzwerkmedium senden möchte, **"hört" es zuerst auf das Medium**. Es überprüft, ob das Medium **frei** (inaktiv, keine Signale vorhanden) oder **belegt** (aktiv, ein anderes Gerät sendet gerade) ist.
    - **Analogie:** Stellen Sie sich vor, Sie möchten in einem Gespräch etwas sagen. Bevor Sie anfangen zu sprechen, hören Sie zuerst, ob gerade jemand anderes spricht.
    
    [![Bildmotiv: Person listening to a network cable  Carrier Sense](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGT3z_zmX323EhQDdteOChhYFJFNnacF3OzRRi9gtU0zUMbhi5tIFPL8oA6Wpp)Wird in einem neuen Fenster geöffnet](https://www.ciena.com/insights/blog/2024/4-key-steps-for-a-successful-network-equipment-deployment)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcR49dEg_Kw0RegUvmgwGSIlBQykeQHqzbUIH5axJcrrIXO6XVd3XFkr6hCudSm3hK3unYj0m0X4z2GvdsZ2kPO3BMqV92Ssbg)www.ciena.com](https://www.ciena.com/insights/blog/2024/4-key-steps-for-a-successful-network-equipment-deployment)
    
    Person listening to a network cable Carrier Sense
    
2. **Multiple Access (MA) - Mehrfachzugriff:**
    
    - **Mehrere Geräte teilen sich das gleiche Übertragungsmedium**. Es gibt keine zentrale Steuerung, die den Zugriff regelt (im Gegensatz zu Token-basierten Verfahren). Jedes Gerät hat die Möglichkeit, zu senden, sobald das Medium als frei erkannt wird.
    - **Analogie:** Es ist wie eine offene Gesprächsrunde, in der viele Menschen gleichzeitig sprechen könnten, wenn sie möchten.
    
    [![Bildmotiv: Multiple computers connected to a shared network cable  Multiple Access](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT3Og94JGnkACNCanXJo3zdM8IJFTVOwNeM-KLoA7M9sWM-FiWatimHBjDlGNya)Wird in einem neuen Fenster geöffnet](https://superuser.com/questions/1714834/best-way-to-share-wireless-connection-to-multiple-wired-machines)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcRjwenL3qwZRj6UKm-ix1TPs8PcGp4KSfaHtn7TcxsgbjMhCz5bEOMycznekNkLSseRQE8t1N4QFuVB4l5pEKQZRNJsVNZZkw)superuser.com](https://superuser.com/questions/1714834/best-way-to-share-wireless-connection-to-multiple-wired-machines)
    
    Multiple computers connected to a shared network cable Multiple Access
    
3. **Collision Detection (CD) - Kollisionserkennung:**
    
    - **Kollisionen können auftreten**, wenn zwei oder mehr Geräte gleichzeitig feststellen, dass das Medium frei ist und gleichzeitig mit der Übertragung beginnen. In diesem Fall **überlappen sich ihre Signale auf dem Medium**, was zu einer **Datenkollision** und **Signalverzerrung** führt.
    - CSMA/CD-Geräte sind in der Lage, diese **Kollisionen zu erkennen**. Sie überwachen das Medium **während der eigenen Übertragung**. Wenn ein Gerät eine Signalverzerrung (die typisch für eine Kollision ist) wahrnimmt, bedeutet dies, dass eine Kollision aufgetreten ist.
    - **Analogie:** Wenn zwei Personen in der Gesprächsrunde gleichzeitig anfangen zu sprechen, überlappen sich ihre Stimmen und man versteht nichts mehr richtig - das ist wie eine Kollision. Man erkennt, dass etwas schiefgelaufen ist, weil man die überlappenden Stimmen hört.
    
    [![Bildmotiv: Two signals colliding on a network cable  Collision Detection](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTeZDhWvKnc2SH38LAmYJXdcJQ87L-JZ2Kw7U29PuPgiRAWbnRPZOT60RC6PB9)Wird in einem neuen Fenster geöffnet](https://networkengineering.stackexchange.com/questions/57521/how-exactly-does-an-ethernet-collision-happen-in-the-cable-since-nodes-use-diff)[![](https://encrypted-tbn3.gstatic.com/favicon-tbn?q=tbn:ANd9GcT9DrOpJejR07ptnBaKkO0uSosua7D529uxTvBGK67klXhHo3R4dRdcp_rnRfTdhEq1T2XFhVb3dmWK5fvSuV-w_s8Cipvw6T2chW_75b6AfGrswyLPAaIusoS1hHqP)networkengineering.stackexchange.com](https://networkengineering.stackexchange.com/questions/57521/how-exactly-does-an-ethernet-collision-happen-in-the-cable-since-nodes-use-diff)
    
    Two signals colliding on a network cable Collision Detection
    

**Ablauf bei einer Datenübertragung mit CSMA/CD:**

1. **Sendeabsicht:** Gerät A möchte Daten an Gerät B senden.
    
2. **Carrier Sense (Abhören):** Gerät A "hört" auf das Netzwerkmedium.
    
3. **Medium frei?:**
    
    - **Ja, Medium ist frei:** Gerät A beginnt mit der Datenübertragung.
    - **Nein, Medium ist belegt:** Gerät A wartet, bis das Medium frei wird (keine Signale mehr vorhanden sind) und wiederholt dann Schritt 2.
4. **Übertragung:** Gerät A sendet die Daten.
    
5. **Collision Detection (Kollisionsüberwachung) während der Übertragung:** Gerät A überwacht das Medium _während_ es sendet.
    
6. **Kollision aufgetreten?:**
    
    - **Nein, keine Kollision:** Die Übertragung ist erfolgreich. Gerät A hat seine Daten gesendet.
    - **Ja, Kollision erkannt:**
        - **Jamming-Signal senden:** Gerät A **bricht die aktuelle Übertragung sofort ab** und sendet ein **"Jamming-Signal"**. Dieses spezielle Signal wird gesendet, um _alle_ anderen Geräte im Netzwerk **schnellstmöglich über die Kollision zu informieren**.
        - **Wartezeit (Backoff):** Gerät A und _alle_ anderen Geräte, die in der Kollision involviert waren, **warten eine zufällige Zeitspanne** (Backoff-Algorithmus) ab.
        - **Neuer Versuch:** Nach Ablauf der Wartezeit beginnen die Geräte **erneut bei Schritt 1**, um die Daten erneut zu senden.
    
    [![Bildmotiv: Flowchart explaining CSMA/CD process  Start, Carrier Sense, Medium Free?, Transmit, Collision Detection, Collision?, Jamming Signal, Backoff, Retry](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSNZDgswx3QYjP8ogkKb6-PWwozGfcm7h-fE3z5TH3zD01gp8_I0fEO1dbza4b8)Wird in einem neuen Fenster geöffnet](https://www.geeksforgeeks.org/carrier-sense-multiple-access-csma/)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcRhozPFEmg8f-ipzeQviUztsisaCXzxmMiAMrRliVhPQtJyEMMq_0b1osZy_EdZwXvGx2s17j-bfdCt94tYx_ITDG-xKXoZ_BxsQE05uyyO)www.geeksforgeeks.org](https://www.geeksforgeeks.org/carrier-sense-multiple-access-csma/)
    
    Flowchart explaining CSMA/CD process Start, Carrier Sense, Medium Free?, Transmit, Collision Detection, Collision?, Jamming Signal, Backoff, Retry
    

**Der Backoff-Algorithmus (Binary Exponential Backoff):**

Um zu verhindern, dass Geräte nach einer Kollision direkt wieder gleichzeitig senden und erneut kollidieren, wird ein **Backoff-Algorithmus** verwendet. Der gängigste Algorithmus ist der **Binary Exponential Backoff**.

- **Zufällige Wartezeit:** Nach der _i_-ten Kollision wählt das Gerät eine zufällige Wartezeit aus einem **exponentiell wachsenden Zeitfenster**.
- **Exponentielles Zeitfenster:** Das Zeitfenster für die zufällige Wartezeit verdoppelt sich mit jeder Kollision (bis zu einem gewissen Maximum).
- **Beispiel:**
    - Nach der 1. Kollision: Wartezeit aus {0, 1} * Zeitschlitz (z.B. 512 Bitzeiten in Ethernet).
    - Nach der 2. Kollision: Wartezeit aus {0, 1, 2, 3} * Zeitschlitz.
    - Nach der 3. Kollision: Wartezeit aus {0, 1, 2, 3, 4, 5, 6, 7} * Zeitschlitz.
    - ... usw. bis zu einem maximalen Zeitfenster.

**Zweck des Backoff-Algorithmus:**

- **Entzerrung der Sendeversuche:** Die zufällige Wartezeit reduziert die Wahrscheinlichkeit, dass die gleichen Geräte nach einer Kollision direkt wieder gleichzeitig senden und erneut kollidieren.
- **Stabilität des Netzwerks:** Durch das exponentiell wachsende Zeitfenster wird bei hoher Netzwerklast und vielen Kollisionen die Wahrscheinlichkeit für weitere Kollisionen reduziert und die Stabilität des Netzwerks erhalten.

**Vorteile von CSMA/CD:**

- **Einfachheit:** Relativ einfache Implementierung im Vergleich zu komplexeren Zugriffsmethoden.
- **Dezentrale Steuerung:** Keine zentrale Instanz zur Zugriffssteuerung erforderlich, was das Netzwerk robuster und weniger anfällig für einzelne Fehlerquellen macht.
- **Gut bei geringer Last:** Bei geringer Netzwerklast und wenigen Kollisionen ist CSMA/CD effizient, da Geräte sofort senden können, wenn das Medium frei ist.

**Nachteile von CSMA/CD:**

- **Ineffizienz bei hoher Last:** Bei hoher Netzwerklast steigt die Wahrscheinlichkeit für Kollisionen erheblich. Kollisionen verschwenden Bandbreite, da Daten erneut gesendet werden müssen. Die Effizienz des Netzwerks sinkt unter hoher Last.
- **Nicht deterministisch:** Der Zugriff auf das Medium ist nicht deterministisch. Es gibt keine Garantie, wann ein Gerät senden kann, da es von der aktuellen Netzwerklast und dem Zufall der Backoff-Zeiten abhängt.
- **Beschränkung der Netzwerkausdehnung:** Die maximale Netzwerkausdehnung (Kabellänge) ist durch die Zeit begrenzt, die benötigt wird, um eine Kollision zu erkennen (Kollisionsdomäne). In großen Netzwerken könnte es passieren, dass eine Kollision zu spät erkannt wird, was zu weiteren Problemen führt.
- **Halbduplex-Betrieb:** In der ursprünglichen CSMA/CD-Implementierung war nur **Halbduplex-Betrieb** möglich, d.h., ein Gerät kann entweder senden oder empfangen, aber nicht beides gleichzeitig. Dies limitiert die Bandbreitennutzung.

**Heutige Relevanz von CSMA/CD:**

In modernen Ethernet-Netzwerken, die **Switches** verwenden, spielt CSMA/CD **keine Rolle mehr in der gleichen Weise**.

- **Switched Ethernet (Vollduplex):** Switches verwenden **Punkt-zu-Punkt-Verbindungen** zwischen Ports. Jeder Port an einem Switch ist eine eigene Kollisionsdomäne. Geräte, die an Switch-Ports angeschlossen sind, arbeiten typischerweise im **Vollduplex-Modus**. In Vollduplex-Verbindungen können Geräte gleichzeitig senden und empfangen, und **Kollisionen treten nicht auf**.
- **Keine Kollisionsdomäne:** Durch die Verwendung von Switches und Vollduplex-Betrieb wird das Netzwerk in viele kleine Kollisionsdomänen aufgeteilt oder Kollisionsdomänen komplett eliminiert.

**Dennoch:**

- **Historische Bedeutung:** CSMA/CD ist von großer historischer Bedeutung, da es das **ursprüngliche Medienzugriffsverfahren für Ethernet** war und maßgeblich zum Erfolg von Ethernet beigetragen hat.
- **Grundlegendes Konzept:** Das Konzept des "Abhörens vor dem Sprechen" und der Kollisionserkennung ist ein **grundlegendes Prinzip in der Netzwerktechnik** und findet sich in abgewandelter Form auch in anderen Protokollen wieder.
- **Lehrreich:** Das Verständnis von CSMA/CD hilft, die **Herausforderungen des Medienzugriffs in geteilten Medien zu verstehen** und die Notwendigkeit für modernere Lösungen wie Switched Ethernet zu würdigen.

**Zusammenfassend lässt sich sagen, dass CSMA/CD ein cleveres und einfaches Verfahren war, um den Medienzugriff in frühen Ethernet-Netzwerken zu regeln. Obwohl es in modernen Switched-Ethernet-Netzwerken nicht mehr direkt verwendet wird, ist es ein wichtiges Konzept in der Geschichte der Netzwerktechnik und hilft, die Evolution der Netzwerktechnologien zu verstehen.**