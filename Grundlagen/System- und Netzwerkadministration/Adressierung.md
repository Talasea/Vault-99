# 

Adressierung Netzwerk Erklärung

Die Adressierung in Netzwerken ist ein wesentlicher Bestandteil der Kommunikation im Internet und in lokalen Netzwerken. Sie ermöglicht es, Datenpakete effizient an die richtigen Empfänger zu senden und zu empfangen. Hier sind die grundlegenden Konzepte:

- **IP-Adresse**: Eine IP-Adresse ist eine eindeutige Nummer, die einem Gerät im Netzwerk zugewiesen wird. Sie besteht aus 32 Bit bei IPv4 (z.B. 192.168.123.137) oder 128 Bit bei IPv6 (z.B. 2001:0db8:85a3:0000:0000:8a2e:0370:7334). Die IP-Adresse besteht aus zwei Teilen: dem Netzwerkanteil und dem Hostanteil.
    
- **Netzwerkanteil und Hostanteil**: Bei IPv4 wird die IP-Adresse in zwei Teile unterteilt. Der Netzwerkanteil identifiziert das Netzwerk, während der Hostanteil den spezifischen Host innerhalb des Netzwerks identifiziert. Beispielsweise bei der IP-Adresse 192.168.123.137: Der Netzwerkanteil könnte 192.168.123 sein und der Hostanteil 137.
    
- **Netzmaske**: Eine Netzmaske (Subnetzmaske) definiert, welcher Teil der IP-Adresse zum Netzwerkanteil und welcher zum Hostanteil gehört. Beispielsweise bei der IP-Adresse 192.168.123.137 mit der Netzmaske 255.255.255.0: Der Netzwerkanteil ist 192.168.123 und der Hostanteil ist 137.
    
- **Subnetze**: Um große Netzwerke effizient zu verwalten, werden sie in kleinere Teile, sogenannte Subnetze, unterteilt. Dies ermöglicht es, Datenpakete nur an die relevanten Teilnehmer zu senden.