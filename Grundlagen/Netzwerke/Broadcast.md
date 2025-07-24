

Ein Broadcast in einem Netzwerk ist eine Nachricht, die von einem Punkt aus an alle Teilnehmer eines Nachrichtennetzes übertragen wird. Diese Nachrichten werden als Datenpakete an alle Geräte innerhalb eines bestimmten Netzwerksegments gesendet, ohne dass die Empfänger explizit angegeben werden müssen. Im Kontext von IP-Netzwerken wird die Broadcast-Adresse genutzt, um Datenpakete an alle Geräte innerhalb eines Subnetzes zu senden. Die Broadcast-Adresse ist immer die letzte IP-Adresse des Subnetzes und wird in jedem Netzwerk nur einmal vergeben. Beispielsweise in einem IPv4-Netz mit der IP-Adresse 192.168.0.0 und der Subnetzmaske 255.255.255.0 (/24) wäre die Broadcast-Adresse 192.168.0.255.

Ein Broadcast-Paket erreicht alle Teilnehmer eines lokalen Netzes, ohne dass sie explizit als Empfänger angegeben sind. Dies ermöglicht es, Informationen breit zu streuen und mehrfache Übertragungen zu vermeiden. Jedoch kann ein zu großes Broadcast-Gebiet das Netzwerk belasten und die Übertragungsgeschwindigkeit verschlechtern. Um diese Probleme zu minimieren, werden große Netzwerke oft in kleinere Broadcast-Domänen unterteilt, die durch VLANs oder Routern auf Schicht 3 getrennt werden.

