---
created: 2024-11-11T10:53
updated: 2024-11-11T10:54
---
Wir möchten das Konzept von gestern wieder aufgreifen und mit unserem neu gewonnenen Verständnis für Protokolle untersuchen.
Ihr könnt zum einen die Reverse Shell von gestern verwenden oder aber auch folgende `PowerShell` Kommandos verwenden um eine simple TCP Nachricht an Kali zu schicken:

```powershell
# Verbindung zu Kali aufbauen
$client = New-Object System.Net.Sockets.TcpClient("Kali_IP_Address", 4444)

# Die Verbindung für das Senden von Nachrichten verwenden
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)

# Eine Nachricht senden
$writer.WriteLine("Hello from Windows!")
$writer.Flush()
```

```powershell
# Die Verbindung muss wieder sauber getrennt werden
$writer.Close()
$client.Close()
```

1. Analysiert den Nachrichtenaustausch mit `Wireshark`. In welchem Schritt wird der TCP-Handshake durchgeführt?
2. Was genau ist die Funktion des TCP-Handshakes?
3. Warum fehlen beim Ethernet Packet die Präambel und die Checksumme?

1. `netcat` auf Windows Server bekommen
2. Einmal mit Windows als Server die Kommunikation aufbauen, einmal mit Kali als Server

Kommandos: 
    Server: nc -lvnp 8000
    Client: nc <ip> <port>
