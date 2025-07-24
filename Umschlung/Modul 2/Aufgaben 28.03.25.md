Lösung Christian und daniel

Aufgabe 1:

- Erstelle in im Home-Verzeichnis deines Benutzer das Verzeichnis 'Test1'

[[1b113b2d7685a151dd23823b1a5d9167_MD5.jpeg|Open: Pasted image 20250328115149.png]]
![[1b113b2d7685a151dd23823b1a5d9167_MD5.jpeg]]

- Wechsle in das neue Verzeichnis.
- [[88580c4d280dc59e46d763c227ca4117_MD5.jpeg|Open: Pasted image 20250328115222.png]]
![[88580c4d280dc59e46d763c227ca4117_MD5.jpeg]]

- Erstelle im neuen Verzeichnis ein Unerverzeichnis 'Test1'

[[c3c852b934b5eb3d0fc4372f981d2242_MD5.jpeg|Open: Pasted image 20250328115307.png]]
![[c3c852b934b5eb3d0fc4372f981d2242_MD5.jpeg]]

- In diesem Verz. wird nun eine Datei mit dem Namen "testdatei.txt"


[[f2897b3b2318f26c0ca25f07ab42f175_MD5.jpeg|Open: Pasted image 20250328115613.png]]
![[f2897b3b2318f26c0ca25f07ab42f175_MD5.jpeg]]
  und dem Inhalt "echo Es funktioniert." erstellt.

  

Aufgabe 2:

- Sorge dafür, dass diese Datei vom Benutzer ausführbar wird.

  -> Beim Aufruf der Datei soll also der Text des Echo Befehls ausgegeben werden.
[[5ae6cdb67bd9cc5ca27d0436c6aae704_MD5.jpeg|Open: Pasted image 20250328115953.png]]
![[5ae6cdb67bd9cc5ca27d0436c6aae704_MD5.jpeg]]

Aufgabe 3:

- Wechsle den Benutzer. Werde 'root'

  [[af9358b8c44cbfd74a919358302d303e_MD5.jpeg|Open: Pasted image 20250328120603.png]]
![[af9358b8c44cbfd74a919358302d303e_MD5.jpeg]]

Aufgabe 4:

- Lege als root eine neue Datei im Home-Verzeichnis deines 'normalen' Benutzers an.
[[86ff367a382a265aa07aacecc4457544_MD5.jpeg|Open: Pasted image 20250328121024.png]]
![[86ff367a382a265aa07aacecc4457544_MD5.jpeg]]
- Werde wieder zum normalen Benutzer (z.B. 'kali')
[[efa72389c2495111ae570093622a96ae_MD5.jpeg|Open: Pasted image 20250328121041.png]]
![[efa72389c2495111ae570093622a96ae_MD5.jpeg]]

- Versuche auf die Datei schreibend zuzugreifen. Füge z.B. einen Text hinzu.

[[178f7c873d38fcdf324a5445283583a6_MD5.jpeg|Open: Pasted image 20250328121432.png]]
![[178f7c873d38fcdf324a5445283583a6_MD5.jpeg]]

- Geht nicht? -> Dann sorge dafür,

  dass dein normaler Benutzer Schreibrechte auf die Datei bekommt.
ich habe den user in ene gruppe die rchte gegben um die datei  lesen schreiben und ausführen zu können 
  [[bfe46f3af52457a0896758aa5c558482_MD5.jpeg|Open: Pasted image 20250328122659.png]]
![[bfe46f3af52457a0896758aa5c558482_MD5.jpeg]]
[[a64dafb7aa07ac5f83ccb76769a7d164_MD5.jpeg|Open: Pasted image 20250328122720.png]]
![[a64dafb7aa07ac5f83ccb76769a7d164_MD5.jpeg]]
Aufgabe 5:

- Finde heraus mit welcher Shell dein User arbeitet.
- [[6fa01a7f17aa3529600792ad168da075_MD5.jpeg|Open: Pasted image 20250328122835.png]]
![[6fa01a7f17aa3529600792ad168da075_MD5.jpeg]]

- Erstelle eine Sicherheitskopie der Konfig-Datei für diese Shell
[[45ac22a7804754fe1a6316c252948f70_MD5.jpeg|Open: Pasted image 20250328124546.png]]
![[45ac22a7804754fe1a6316c252948f70_MD5.jpeg]]
[[b71e0244e71a634c830c0f5c617cec06_MD5.jpeg|Open: Pasted image 20250328124911.png]]
![[b71e0244e71a634c830c0f5c617cec06_MD5.jpeg]]
- Füge in die Konfig Datei einen weiteren Alias hinzu (freie Wahl)
 nano ~/.bashrc
- [[8ca70aa05eaaab17189b05cc699c932d_MD5.jpeg|Open: Pasted image 20250328125212.png]]



- Füge temporär einen Alias hinzu: Ein Alias deiner Wahl soll die Befehle zum 

  updaten des Systems ausführen.

[[4bf5d7ac7fb70eb65f1c78b617f435f2_MD5.jpeg|Open: Pasted image 20250328125644.png]]
![[4bf5d7ac7fb70eb65f1c78b617f435f2_MD5.jpeg]]

  

Aufgabe 6:

- Lösche (mit einem einzigen Befehl), die eben angelegte Verzeichnisstruktur.

  [[3a0bc59896077bf797eb68fd036a464a_MD5.jpeg|Open: Pasted image 20250328125805.png]]
![[3a0bc59896077bf797eb68fd036a464a_MD5.jpeg]]

Aufgabe 7:

- Lasse die die man-Page zum Befehl 'ifconfig' anzeigen und schreibe den Inhalt der Anzeige

  in die Datei 'ifconfig.txt' (Zum Nachschlagen :)

  [[871cb758fafba4cd24774428e1aba687_MD5.jpeg|Open: Pasted image 20250328125919.png]]
![[871cb758fafba4cd24774428e1aba687_MD5.jpeg]]

Aufgabe 8:

- Installiere das Programm 'htop'

sudo apt update
sudo apt install htop
  
[[923416d5295ade1f6ed5d3d6a80c4045_MD5.jpeg|Open: Pasted image 20250328125954.png]]
![[923416d5295ade1f6ed5d3d6a80c4045_MD5.jpeg]]
Aufgabe 9:

- Starte einen beliebigen Prozess und finde seine Nummer heraus
ps -ef
[[a0890e29fbeedc9a627862aee90dc35e_MD5.jpeg|Open: Pasted image 20250328130447.png]]
![[a0890e29fbeedc9a627862aee90dc35e_MD5.jpeg]]

- Beende diesen Prozess von der Shell (CLI) aus.
sudo kill -9 5555

[[3ed0012a2296ab92148d96611a64b377_MD5.jpeg|Open: Pasted image 20250328130607.png]]
![[3ed0012a2296ab92148d96611a64b377_MD5.jpeg]]


[[60511ffd76e1af3e20f3349eab9f09e4_MD5.jpeg|Open: Pasted image 20250328130632.png]]
![[60511ffd76e1af3e20f3349eab9f09e4_MD5.jpeg]]
  

Aufgabe 10:

- Nenne den Befehl, um nach der Datei 'sources.list' zu suchen.

sudo find / -name sources.list

  - Zeige, dass es funktioniert hat.
[[0493018f900997c9ad3438c2478f919a_MD5.jpeg|Open: Pasted image 20250328130954.png]]
![[0493018f900997c9ad3438c2478f919a_MD5.jpeg]]