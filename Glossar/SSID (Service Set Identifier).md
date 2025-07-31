- **Kerndefinition:** Der **SSID (Service Set Identifier)** ist der für Menschen lesbare Name eines drahtlosen lokalen Netzwerks (WLAN). Es ist die Zeichenkette (bis zu 32 Zeichen), die in der Liste der verfügbaren Wi-Fi-Netzwerke auf einem Computer, Smartphone oder einem anderen drahtlosen Gerät angezeigt wird.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Access Points senden die SSID in regelmäßigen Abständen in speziellen Paketen, den sogenannten **Beacon Frames**, aus. Dadurch können Geräte in der Umgebung das Netzwerk entdecken und sich damit verbinden.
        
    - **ESSID:** In größeren Netzwerken können mehrere Access Points dieselbe SSID verwenden, um ein einziges, nahtloses Netzwerk zu bilden. Dies wird als **Extended Service Set (ESS)** bezeichnet, und die gemeinsam genutzte SSID wird dann technisch korrekt als ESSID bezeichnet. Dies ermöglicht es den Clients, sich frei zwischen den Access Points zu bewegen (Roaming), ohne die Verbindung zu verlieren.
        
    - **BSSID:** Die SSID sollte nicht mit der **BSSID** verwechselt werden, bei der es sich um die eindeutige MAC-Adresse des Funkmoduls eines einzelnen Access Points handelt.
        
- **Einordnung in den Gesamtkontext:** Die SSID ist ein fundamentaler Parameter des **IEEE 802.11**-Standards, der die Grundlage für WLAN bildet. Sie ist der primäre Identifikator, den Endbenutzer verwenden, um ein bestimmtes Netzwerk auszuwählen.
    
- **Sicherheitsaspekte:**
    
    - **Versteckte SSIDs:** Das Deaktivieren der SSID-Aussendung in den Beacon Frames ("Hiding the SSID") gilt heute als veraltete und ineffektive Sicherheitsmaßnahme. Die SSID wird weiterhin in anderen Paketen unverschlüsselt übertragen und kann von Angreifern mit einfachen Tools innerhalb von Sekunden aufgespürt werden.
        
    - **Evil Twin Angriffe:** Ein erhebliches Risiko besteht darin, dass Angreifer einen eigenen Access Point mit einer vertrauenswürdig klingenden oder identischen SSID (z. B. "Telekom_FON" oder der Name des Firmen-WLANs) aufsetzen. Verbindet sich ein Benutzer mit diesem "bösen Zwilling", kann der Angreifer den gesamten Datenverkehr mitlesen.
        
- **Praxisbeispiel / Analogie:** Die SSID ist wie der Name, der an der Klingel eines Hauses steht. Er sagt Ihnen, wer in diesem Haus wohnt (z. B. "Familie Müller WLAN"). Der Schlüssel, den Sie zum Eintreten benötigen, ist das Wi-Fi-Passwort (der Pre-Shared Key bei WPA2/3).
    
- **Fazit / Bedeutung für IT-Profis:** Für Netzwerkadministratoren ist die Wahl einer klaren und eindeutigen SSID Teil der grundlegenden Netzwerkkonfiguration. Viel wichtiger ist jedoch die Aufklärung der Benutzer über die damit verbundenen Risiken, insbesondere über die Gefahr von Evil-Twin-Angriffen. Anstatt auf das Verstecken von SSIDs zu vertrauen, müssen robuste Sicherheitsmechanismen wie WPA3 und gegebenenfalls 802.1X/EAP zur Authentifizierung eingesetzt werden.