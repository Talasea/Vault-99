# 

5-4-3 Regel Erklärung

Die 5-4-3-Regel, auch als Repeater-Regel bezeichnet, ist eine Faustregel in der Netzwerktechnik, die die maximale Ausdehnung eines Ethernet-Netzwerks mit gemeinsamem Zugriff (CSMA/CD) beschreibt. Die Regel gilt für Netzwerke mit einer Übertragungsgeschwindigkeit von 10 Mbit/s und ist notwendig, um Kollisionen auf dem Netzwerkmedium zu vermeiden.

Die 5-4-3-Regel besagt, dass:

1. Innerhalb einer Kollisionsdomäne (Collision Domain) maximal fünf Segmente (Link-Segmente oder Inter-Repeater-Leitungen) verbunden sein dürfen.
2. Maximal vier Repeaters (Koppelelemente) dürfen zwischen diesen Segmenten eingesetzt werden.
3. Nur drei dieser Segmente dürfen lokale Netze (Stationen) enthalten, die aktiv sind (d.h., Endgeräte, die Daten senden und empfangen).

Die Regel wurde entwickelt, um die Laufzeit eines Signals und damit die maximale Größe einer Kollisionsdomäne zu beschränken. Die Laufzeit eines Signals wird durch die Summierung der Laufzeiten je Segment und der Verzögerung der Koppelelemente ermittelt. Sie muss unterhalb des maximal erlaubten Round Trip Delays liegen.

Die 5-4-3-Regel gilt nur für Ethernet-Netzwerke mit gemeinsamem Zugriff (CSMA/CD) und nicht für Switch-Netzwerke oder Fast Ethernet/Gigabit-Ethernet-Netzwerke, die andere Kollisionsvermeidungsmechanismen verwenden.

In der Praxis bedeutet dies, dass bei der Erweiterung eines Ethernet-Netzwerks mit Repeatern die 5-4-3-Regel beachtet werden muss, um sicherzustellen, dass das Netzwerk stabil und fehlerfrei funktioniert.