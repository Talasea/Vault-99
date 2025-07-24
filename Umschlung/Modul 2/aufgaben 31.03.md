**To Do:**

  

1. Aufgaben von Freitag beenden

2. Aufgaben von heute bearbeiten

3. Wer fertig ist bekommt gerne Zusatzaufgaben

  

# ------------------

  

Aufgaben von heute:

  

Aufgabe 1:

- Erstelle in deiner VM-Umgebung eine neue, virtuelle Festplatte und

  weise sie deiner VM zu.[[db13826439b2d1c031afc423cfc6633e_MD5.jpeg|Open: Pasted image 20250331105832.png]]
![[db13826439b2d1c031afc423cfc6633e_MD5.jpeg]]

- Binde diese neue HD ins das Linux-Dateisystem ein.

[[52297d538d7163aa063ade048b45f50d_MD5.jpeg|Open: Pasted image 20250331110321.png]]
![[52297d538d7163aa063ade048b45f50d_MD5.jpeg]]

[[452111af003755f2855056385e4dfc8f_MD5.jpeg|Open: Pasted image 20250331114521.png]]
![[452111af003755f2855056385e4dfc8f_MD5.jpeg]]


- Teste den mount-Befehl mit diversen Optionen (z.B. Read Only)
[[7a0a5aaff5fd920f8617b9a5ced62ae9_MD5.jpeg|Open: Pasted image 20250331130144.png]]
![[7a0a5aaff5fd920f8617b9a5ced62ae9_MD5.jpeg]]
  - Wer kann, wenn der Mountpoint auf ro gesetzt ist, auf den Datenträger schreiben?

Wenn ein Mountpoint mit der Option `ro` (read-only) gesetzt wurde, kann **niemand** direkt über diesen Mountpoint auf den Datenträger schreiben, **nicht einmal der Root-Benutzer**.

[[a00bb3d31d0b07f2bb82cae1e816a6f3_MD5.jpeg|Open: Pasted image 20250331130223.png]]
![[a00bb3d31d0b07f2bb82cae1e816a6f3_MD5.jpeg]]

Diese Option verhindert die Interpretation von Gerätedateien (z.B. `/dev/sda`) auf dem eingehängten Dateisystem.
[[475185497db238b194adb0a8edf09770_MD5.jpeg|Open: Pasted image 20250331130607.png]]
![[475185497db238b194adb0a8edf09770_MD5.jpeg]]



- Binde eine ISO-Datei ins dein Linux System ein.

[[6957d1889a19e8015f5b2411991bcf95_MD5.jpeg|Open: Pasted image 20250331131405.png]]
![[6957d1889a19e8015f5b2411991bcf95_MD5.jpeg]]
- Erkläre (in eigenen Worten): Was macht der 'mount'-Befehl ?

  - Was ist ein Mountpont?

  - ...
Antwort: 

Der `mount`-Befehl macht den Inhalt eines Speichergeräts über einen bestimmten Ordner in deinem Dateisystem zugänglich. Ein **Mountpoint** ist der Ordner, an dem dieses Speichergerät "eingehängt" wird, und wo du auf dessen Inhalt zugreifen kannst. Ohne den `mount`-Befehl und einen Mountpoint wären die Daten auf separaten Speichergeräten isoliert und du könntest nicht einfach darauf zugreifen, als wären sie Teil deiner normalen Ordnerstruktur.

Der `mount`-Befehl hat verschiedene Optionen, die wie zusätzliche Anweisungen funktionieren:

- **-o ro (Read Only - Nur Lesen)**: Du kannst nur lesen, aber nicht schreiben.
    
- **-o rw (Read Write - Lesen und Schreiben)**: Du kannst lesen und schreiben.
    
- **-o noexec (No Execute - Nicht Ausführbar)**: Programme können nicht ausgeführt werden.
    
- **-o nosuid (No Set User ID - Keine Benutzer-ID setzen)**: Programme laufen mit den Rechten des Starters.
    
- **-o nodev (No Device - Keine Geräte)**: Direkter Zugriff auf Hardware wird blockiert.
    
- **-o loop (Loopback)**: Für virtuelle Speichergeräte wie ISO-Dateien.
    
- **-t <Dateisystemtyp> (Type - Typ des Dateisystems)**: Gibt den Dateisystemtyp an.

Syntax : mount [Optionen] <Gerät> <Mountpunkt>`
    
    - **Gerät**: Das Gerät, das Sie einhängen möchten (z.B. /dev/sda1, /dev/cdrom).
        
    - **Mount_punkt**: Das Verzeichnis, in das das Gerät eingehängt werden soll (z.B. /mnt/usb).


Aufgabe 2:

- Prüfe ob der Apache-Webserver auf deinem System installiert ist.
[[60c02069f1ad3c0cf60b22eee3309811_MD5 1.jpeg]]

[[60c02069f1ad3c0cf60b22eee3309811_MD5 1.jpeg|Open: Screenshot 2025-03-31 132137.png]]
![[60c02069f1ad3c0cf60b22eee3309811_MD5 1.jpeg]]

- Falls nicht -> installiere ihn.

- Sorge dafür, dass der Webserver mit jedem Systemstart hochfährt.

[[1cd2dfea634cac84b3fe6a05605e7262_MD5 1.jpeg]]


[[1cd2dfea634cac84b3fe6a05605e7262_MD5 1.jpeg]]

[[4c925fe8e963ad45b729d965ad38d601_MD5.jpeg|Open: Pasted image 20250331132826.png]]
![[Pasted image 20250331132839.png]]![[4c925fe8e963ad45b729d965ad38d601_MD5.jpeg]]

