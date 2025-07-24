Aufgabe(-n) Aufgabe 1: Installiere den Windows Core Server 2022. 

siehe doku mittschrift 6.02
.
Aufgabe 2: Nehme mit „SConfig“ die grundlegende, erforderliche Konfiguration vor (Zeitzone, …). 

siehe doku mittschrift 6.02


Aufgabe 3: Überprüfe ob dein Server und ein Client miteinander kommunizieren können. 

![[Pasted image 20250206145308.png]]


Aufgabe 4: Richte auf dem Server ein funktonierendes AD ein. Hinweis: Die Installation der Rollen kann teilweise über das Menü in SConfig vorgenommen werden. 



Install-WindowsFeature AD-Domain-Services -IncludeManagementTools  
Install-WindowsFeature DNS -IncludeManagementTools

Install-ADDSForest `  
-DomainName "KlasseCore.de"  
-DomainNetbiosName "KlasseCore"  
-InstallDns:$true  
-SafeModeAdministratorPassword (ConvertTo-SecureString -String "SicheresPasswort123!" -AsPlainText -Force)  
-Force:$true



Aufgabe 5: Erstelle drei Benutzer im AD. (Achte jetzt schon auf die richƟgen Gruppenzugehörigkeiten.)

![[Pasted image 20250206141937.png]]


![[Pasted image 20250206142007.png]]
![[Pasted image 20250206142231.png]]

Aufgabe 6: Erstelle die Benutzergruppe „Entwicklung“ und füge zwei der drei User hinzu.

![[Pasted image 20250206142234.png]]



Aufgabe 7: Erstelle auf dem Coreserver eine Freigabe, auf die nur die Entwicklungsabteilung zugreifen kann. (Checke mit den User, welcher nicht zu den Entwicklern gehört, ob deine Freigabe richƟg eingerichtet wurde.)


New-Item -Path C:\FreigabeEntwicklung -ItemType Directory

New-SmbShare -Name "FreigabeEntwicklung" -Path "C:\FreigabeEntwicklung" -FullAccess "Entwicklung"

icacls C:\FreigabeEntwicklung /inheritance:r /grant:r "Entwicklung:(OI)(CI)M"



![[Pasted image 20250206143725.png]]