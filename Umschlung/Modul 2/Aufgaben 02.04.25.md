#### Aufgabe 1:

- Erkläre den 'tcpdump' Befehl.  

Antwort

Der tcdump Befehl ist ein Kommandozeilen befehl (tool) zur Netzwerkanalyse, das Netzwerkpakete auf einem Interface erfasst und anzeigen kann . Es ist ähnliche wie Wireshark nur ohne Gui  also ne alternative zu TShark.

Es dient um Netzwerkpakete live aufzuzeichnen und zu analysieren. Du kannst damit sehen, welche Daten über dein Netzwerk fließen, und den Datenverkehr nach bestimmten Kriterien filtern (z.B. nach IP-Adresse oder Port).



- Fertige ein Capture aller vorkommenden HTTP und DNS-Anfragen an und schreibe das Resultat in eine Datei.

  
[[ea78127dbf4e06545a7a75618484e41d_MD5.jpeg|Open: Pasted image 20250402143055.png]]
![[ea78127dbf4e06545a7a75618484e41d_MD5.jpeg]]

[[3e45df2a8be08f048d2e94beacb6ff6b_MD5.jpeg|Open: Pasted image 20250402143909.png]]
![[3e45df2a8be08f048d2e94beacb6ff6b_MD5.jpeg]]



Aufhabe 2:  
Lass dir, unter Verwendung des grep-Befehls, alle HTTP-Anfragen aus der vorhin angelegten Datei anzeigen. (Screenshot nicht vergessen :)  

[[9c7a7965644d9a75422154f58dbe3243_MD5.jpeg|Open: Pasted image 20250402145741.png]]
![[9c7a7965644d9a75422154f58dbe3243_MD5.jpeg]]
  
Aufgabe 3:  
Erstelle ein Skript, welches beim Aufruf dein System auf den neuesten Stand bringt.




#!/bin/bash

# Einstellungen
LOGDATEINAME_ANFANG="protokoll_"
PROTOKOLL_ORDNER="./protokolle"
MAXIMALE_ANZAHL_LOGDATEIEN=20
ANZAHL_AELTESTE_LOESCHEN=10

# Stelle sicher, dass der Protokoll-Ordner existiert
mkdir -p "$PROTOKOLL_ORDNER"

# Erstelle einen Zeitstempel für den aktuellen Protokolleintrag
ZEITSTEMPEL=$(date +%Y%m%d_%H%M%S)
PROTOKOLL_DATEI="$PROTOKOLL_ORDNER/${LOGDATEINAME_ANFANG}${ZEITSTEMPEL}.txt"

# Funktion zum Aufzeichnen von Nachrichten im Protokoll
schreibe_protokoll () {
  echo "$(date +%Y-%m-%d_%H:%M:%S) - $1" >> "$PROTOKOLL_DATEI"
}

# Ersten Zeitstempel setzen
schreibe_protokoll "# Startzeitpunkt: $(date)"

# Protokolliere den Update-Vorgang
schreibe_protokoll ">>> Protokoll für < Update > :"
sudo apt update >> "$PROTOKOLL_DATEI" 2>&1

# Protokolliere den Upgrade-Vorgang und erfasse das ergebniss
schreibe_protokoll ">>> Protokoll für < Upgrade > :"
upgrade_ausgabe=$(sudo apt upgrade --simulate)
echo "$upgrade_ausgabe" >> "$PROTOKOLL_DATEI" 2>&1

# Zähle die Anzahl der Einträge in der Datei 'updates.txt'
schreibe_protokoll "Anzahl der Einträge in der Datei 'updates.txt':"
if [ -f "updates.txt" ]; then
  anzahl=$(wc -l < updates.txt)
  schreibe_protokoll "  $anzahl"
else
  schreibe_protokoll "  Datei 'updates.txt' nicht gefunden."
fi

schreibe_protokoll "(Parrot Parrot) - [~]"
schreibe_protokoll "\$"

# Überprüfe die Anzahl der Protokolldateien und lösche die ältesten 10 wen 20 erreicht sind 
anzahl_protokolle=$(find "$PROTOKOLL_ORDNER" -type f -name "${LOGDATEINAME_ANFANG}*.txt" | wc -l)

if [ "$anzahl_protokolle" -gt "$MAXIMALE_ANZAHL_LOGDATEIEN" ]; then
  echo "Anzahl der Protokolldateien ($anzahl_protokolle) übersteigt das Limit ($MAXIMALE_ANZAHL_LOGDATEIEN). Lösche die ältesten $ANZAHL_AELTESTE_LOESCHEN Dateien."
  find "$PROTOKOLL_ORDNER" -type f -name "${LOGDATEINAME_ANFANG}*.txt" -printf '%T@ %p\n' | sort -n | head -n "$ANZAHL_AELTESTE_LOESCHEN" | cut -d' ' -f2- | xargs rm -f
fi

# Auswertung des Upgrades
aktualisierte_pakete=$(echo "$upgrade_ausgabe" | grep -oP "^Die folgenden Pakete werden(.*)aktualisiert:" | sed 's/Die folgenden Pakete werden//' | sed 's/aktualisiert://' | tr ',' '\n' | sed 's/^[[:space:]]*//g' | sed '/^$/d')

if [ -n "$aktualisierte_pakete" ]; then
  echo -e "\nFolgende Pakete würden aktualisiert werden:\n$aktualisierte_pakete"
  schreibe_protokoll "Folgende Pakete würden aktualisiert werden:\n$aktualisierte_pakete"
else
  echo -e "\nEs würden keine Pakete aktualisiert ."
  schreibe_protokoll "Es würden keine Pakete aktualisiert ."
fi





[[b3d4b79966e8316d65429cfe18821ecf_MD5.jpeg|Open: Pasted image 20250402160403.png]]
![[b3d4b79966e8316d65429cfe18821ecf_MD5.jpeg]]