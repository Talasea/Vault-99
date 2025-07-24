
Aufgabe 1:

Alte Aufgaben fertig stellen.

  

Aufgabe 2:

Eine weitere Festplatte über Samba zur Verfügung stellen

(Hyper-V -> Platte erstellen ...)

  

# ===========================================================

  

- Samba auf SMB1 konfigurieren -> Mit Windows testen

  - Geht nicht ?

    -> Mit Wireshark den Traffic analysieren !

  

- Da SSH unverschlüsselt eingerichtet wurde:

  -> Traffic ansehen ...

Aufgabe2 lösung: 
[[9dbd947817bf944f702de6809683a184_MD5.jpeg|Open: Pasted image 20250404120718.png]]
![[9dbd947817bf944f702de6809683a184_MD5.jpeg]]
festplatte formatiert

[[3d1b73bde4a802dd79676a8c291c3438_MD5.jpeg|Open: Pasted image 20250404120736.png]]
![[3d1b73bde4a802dd79676a8c291c3438_MD5.jpeg]]

festplatte gemountet

[[cb6c2f64c9b27d0115a61b8a3ad31f75_MD5.jpeg|Open: Pasted image 20250404120654.png]]
![[cb6c2f64c9b27d0115a61b8a3ad31f75_MD5.jpeg]]
festplatte so gemuntet das sie auch bei einem neustart wieder eingebunden wird 



[[b9fd435150d6266d973e60264ca25ad5_MD5.jpeg|Open: Pasted image 20250404121209.png]]
![[b9fd435150d6266d973e60264ca25ad5_MD5.jpeg]]

einträge im samba server angepasst und hinzugefügt 

[[f985e5cbd5740adf335cbaff04132682_MD5.jpeg|Open: Pasted image 20250404121313.png]]
![[f985e5cbd5740adf335cbaff04132682_MD5.jpeg]]


dienst neugestartet 

[[add960daba8bcfd700a3b5a39e9d734b_MD5.jpeg|Open: Pasted image 20250404121448.png]]

![[add960daba8bcfd700a3b5a39e9d734b_MD5.jpeg]]
in windows auf die platte zugegriffen und ordner erstellt zum testen 

-------
----




Aufgabe

- Samba auf SMB1 konfigurieren -> Mit Windows testen

  - Geht nicht ?

    -> Mit Wireshark den Traffic analysieren !

       - Suche die Pakete, welche auf das Problem hindeuten

         und fertige einen Screenshot davon an.

  

- Da SSH unverschlüsselt eingerichtet wurde:

  -> Suche mit Wireshark den Moment des Einloggens.

     - Ist der Username und das Passwort sichtbar?

     - Füge einen Screenshot an.

[[45b469a3e11df8ed97fda2e86833e70d_MD5.jpeg|Open: Pasted image 20250404142830.png]]
![[45b469a3e11df8ed97fda2e86833e70d_MD5.jpeg]]