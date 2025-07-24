

Aufgabe 1:
Es soll ein Powershellscript erstellt werden, welches einen neuen Benutzer zur Gruppe der regulären Benutzer hinzufügt.
Der Aufruf erfolgt von der Kommandozeile und es werden vier Argumente mit übermittelt: 
Der Nutzername, das Passwort, der Vorname und der Nachname. Beispielhalber Aufruf: 


Falls dein Script nicht aufruĩar ist: Die ExecuƟon Policy überprüfen! 

Antwort 

![[Pasted image 20250204143322.png]]

Set
![[Pasted image 20250204144348.png]]


Aufgabe 2: Überprüfe mit dem Befehl Get-LocalGroupMember 
-Group "Benutzer", ob der Benutzer erfolgreich erstellt wurde. (Screenshot anfügen.)
Beispiel: 

![[Pasted image 20250204144652.png]]


![[Pasted image 20250204145523.png]]




Aufgabe 3: (OpƟonal / Für alle die schneller ferƟg sind bzw. Vorkenntnisse haben) ImplemenƟere eine Fehlerbehandlung, z.B. für den Fall, dass nicht alle Argumente beim Aufruf übergeben wurden


param(
    [Parameter(Position=0, Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string]$username,

    [Parameter(Position=1, Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string]$password,

    [Parameter(Position=2, Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string]$firstName,

    [Parameter(Position=3, Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string]$lastName
)

begin {
    # Administrator check
    if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Error "Das Skript muss als Administrator ausgeführt werden!"
        exit 1
    }
}

process {
    try {
        # Überprüfung auf existierenden Benutzer
        if (Get-LocalUser -Name $username -ErrorAction SilentlyContinue) {
            throw "Benutzer '$username' existiert bereits"
        }

        # Passwort konvertieren
        $securePassword = ConvertTo-SecureString $password -AsPlainText -Force -ErrorAction Stop

        # Benutzer erstellen
        $newUserParams = @{
            Name        = $username
            Password    = $securePassword
            FullName    = "$firstName $lastName"
            Description = "Regulärer Benutzer"
            ErrorAction = 'Stop'
        }
        New-LocalUser @newUserParams

        # Zur Gruppe hinzufügen
        Add-LocalGroupMember -Group "Users" -Member $username -ErrorAction Stop

        Write-Host "Benutzer $username wurde erfolgreich erstellt und zur Gruppe 'Users' hinzugefügt"
        exit 0
    }
    catch [Microsoft.PowerShell.Commands.UserExistsException] {
        Write-Error "Fehler: Benutzer '$username' existiert bereits"
        exit 2
    }
    catch [Microsoft.PowerShell.Commands.InvalidPasswordException] {
        Write-Error "Fehler: Ungültiges Passwortformat"
        exit 3
    }
    catch [System.Security.Authentication.AuthenticationException] {
        Write-Error "Fehler: Passwort entspricht nicht den Komplexitätsanforderungen"
        exit 4
    }
    catch {
        Write-Error "Fehler: $($_.Exception.Message)"
        exit 5
    }
}