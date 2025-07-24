<font color="#ff0000">Aufgabe(-n) Zur Einführung in Windows Core Server werden wir uns eingehender mit der PowerShell beschäŌigen. </font>



<font color="#ff0000">Aufgabe 1: Suche dir essenzielle PS-Befehle heraus, um Benutzer auf einen Windows Server administrieren zu können (anlegen, löschen, ändern). </font>

### **Benutzer anlegen**


`New-LocalUser -Name "Benutzername" -Password (ConvertTo-SecureString "Passwort123!" -AsPlainText -Force) -FullName "Max Mustermann" -Description "Neuer Benutzer"`

### **Benutzer einem lokalen Gruppe hinzufügen**

`Add-LocalGroupMember -Group "Administratoren" -Member "Benutzername"`

### **Benutzerpasswort ändern**

`Set-LocalUser -Name "Benutzername" -Password (ConvertTo-SecureString "NeuesPasswort123!" -AsPlainText -Force)`

### **Benutzer umbenennen**


`Rename-LocalUser -Name "AlterBenutzername" -NewName "NeuerBenutzername"`

### **Benutzer deaktivieren**


`Disable-LocalUser -Name "Benutzername"`

### **Benutzer aktivieren**


`Enable-LocalUser -Name "Benutzername"`

### **Benutzer löschen**


`Remove-LocalUser -Name "Benutzername"`

Falls der Server in einer **Active Directory (AD)**-Domäne läuft, sind die folgenden Befehle relevant (Active Directory-Modul erforderlich):

### **AD-Benutzer anlegen**


`New-ADUser -Name "Max Mustermann" -SamAccountName "mmustermann" -UserPrincipalName "mmustermann@domain.local" -Path "OU=Users,DC=domain,DC=local" -AccountPassword (ConvertTo-SecureString "Passwort123!" -AsPlainText -Force) -Enabled $true`

### **AD-Benutzer löschen**


`Remove-ADUser -Identity "mmustermann"`

### **AD-Benutzer deaktivieren**


`Disable-ADAccount -Identity "mmustermann"`

### **AD-Benutzer aktivieren**


`Enable-ADAccount -Identity "mmustermann"`

### **AD-Benutzer in Gruppe hinzufügen**


`Add-ADGroupMember -Identity "Gruppe" -Members "mmustermann"`




<font color="#ff0000">Aufgabe 2: Suche dir essenzielle PS-Befehle heraus, um Benutzergruppen auf einen Windows Server administrieren zu können (anlegen, löschen, ändern). </font>

## **Lokale Gruppenverwaltung (Windows Server ohne AD)**

### **Gruppe anlegen**



`New-LocalGroup -Name "GruppeName" -Description "Beschreibung der Gruppe"`

### **Gruppe umbenennen**



`Rename-LocalGroup -Name "AlterGruppenname" -NewName "NeuerGruppenname"`

### **Gruppe löschen**



`Remove-LocalGroup -Name "GruppeName"`

### **Benutzer einer Gruppe hinzufügen**



`Add-LocalGroupMember -Group "GruppeName" -Member "Benutzername"`

### **Benutzer aus einer Gruppe entfernen**



`Remove-LocalGroupMember -Group "GruppeName" -Member "Benutzername"`

### **Alle Mitglieder einer Gruppe anzeigen**



`Get-LocalGroupMember -Group "GruppeName"`



## **AD Gruppenverwaltung (Windows Server mit AD)**

### **AD-Gruppe anlegen**

`New-ADGroup -Name "GruppeName" -SamAccountName "GruppeName" -GroupCategory Security -GroupScope Global -Path "OU=Groups,DC=domain,DC=local"`

**GroupCategory:** `Security`  oder `Distribution` muss angegeben werden 
 **GroupScope:** `Global`, `DomainLocal` oder `Universal`

### **AD-Gruppe löschen**

`Remove-ADGroup -Identity "GruppeName"`

### **AD-Gruppe umbenennen**

`Rename-ADObject -Identity "CN=AlteGruppe,OU=Groups,DC=domain,DC=local" -NewName "NeueGruppe"`

### **Benutzer einer AD-Gruppe hinzufügen**


`Add-ADGroupMember -Identity "GruppeName" -Members "Benutzer1", "Benutzer2"`

### **Benutzer aus einer AD-Gruppe entfernen**

`Remove-ADGroupMember -Identity "GruppeName" -Members "Benutzer1" -Confirm:$false`

### **Mitglieder einer AD-Gruppe anzeigen**

`Get-ADGroupMember -Identity "GruppeName"`

### **Prüfen, ob ein Benutzer in einer Gruppe ist**

`Get-ADUser -Identity "Benutzername" -Property MemberOf`






<font color="#ff0000">Aufgabe 3: Erstelle mit Hilfe von PS-Befehlen eine Freigabe auf dem Server und konfiguriere den Client (ebenfalls mit Hilfe von PS_Befehlen) so, daß diese Freigabe als Laufwerk im Explorer sichtbar ist. (z.B. als Laufwerk „F“) </font>

### **Auf dem Server: Ordner freigeben**

Zuerst muss ein Ordner auf dem Server erstellt und freigegeben werden.

#### **Ordner erstellen**



`New-Item -Path "C:\Freigaben\DatenKlasse" -ItemType Directory`

Erstellt einen neuen Ordner auf dem Server unter `C:\Freigaben\DatenKlasse`.

#### **Freigabe einrichten**


`New-SmbShare -Name "DatenFreigabe" -Path "C:\Freigaben\DatenKlasse" -FullAccess "Jeder"`

Gibt den Ordner unter dem Namen **"DatenFreigabe"** im Netzwerk frei. Jeder kann darauf zugreifen.

Falls nur bestimmte Benutzer Zugriff haben sollen:

`New-SmbShare -Name "DatenFreigabe" -Path "C:\Freigaben\Daten" -FullAccess "Domänen-Benutzer"`

Erlaubt nur **Domänen-Benutzern** den Zugriff. Kann auf Jede Anglegte Benutzergruppe der AD angewendet werden 





### **Auf dem Client: Freigabe als Laufwerk verbinden**

Damit der freigegebene Ordner als **Laufwerk "F:"** im Explorer angezeigt wird:
#### **Netzwerkverbindung einrichten**

`New-PSDrive -Name "F" -PSProvider FileSystem -Root "\\KlasseTest\DatenFreigabe" -Persist`

 Verbindet die Freigabe `\\KlasseTest\DatenFreigabe` als Laufwerk **F:** im Explorer.  
Das Laufwerk bleibt auch nach einem Neustart ereichbar

`New-PSDrive -Name "F" -PSProvider FileSystem -Root "\\KlasseTest\DatenFreigabe" -Credential "KlasseTest\Chris" -Persist`



Falls das Laufwerk wieder entfernt werden soll:

`Remove-PSDrive -Name "F"`





<font color="#ff0000">Aufgabe 4: Benutze eine Remotedesktopverbindung, um dich vom Server auf den Client zu Verbinden und dich dort einzuloggen. Diese Art der Verbindung wird  von Administratoren benutzt und ist in der Praxis relevant, auch wenn es im Curriculum nicht explizit behandelt wurde. (Sollten diesbezüglich Probleme bzw. Fragen auŌreten wende dich biƩe an deinen TA oder Dozenten.)</font>



Vorbereitungen auf dem Client

Remote-Desktop aktivieren
![[Pasted image 20250205144202.png]]

Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0


Firewall für RDP freigeben
![[Pasted image 20250205144733.png]]
bei mir war es bereits eingestellt 

alternativ 
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"


Einen Benutzer für den Zugriff hinzufügen

Add-LocalGroupMember -Group "Remote Desktop Users" -Member "![[Pasted image 20250205145309.png]]







### *Verbindung vom Server zum Client herstellen*

Reicht mit Window + R 
mstsc einzugeben 

DESKTOP-10MR9FF

Das öffnet die **Remotedesktop-Verbindung** zu `Client-PC-Name` (ersetze das mit dem Computernamen oder der IP-Adresse).


![[Pasted image 20250205150543.png]]
![[Pasted image 20250205150701.png]]