1. **Registry-Hives**  
    Die Hives enthalten lokale Kontoinformationen, Passworthashes und Konfigurationsdaten:
    
    - C:\Windows\System32\config\SAM
        
    - C:\Windows\System32\config\SECURITY
        
    - C:\Windows\System32\config\SYSTEM
        
    - C:\Windows\System32\config\SOFTWARE
        
2. **Event Logs**  
    Über Event Logs lassen sich Anmeldeversuche, Auditing-Events und Systemfehler rückwirkend analysieren. Pfad:
    
    - C:\Windows\System32\winevt\Logs*.evtx
        
3. **Active Directory-Datenbank (Domain-Controller)**  
    Falls Sie Zugriff auf einen Domain-Controller haben:
    
    - %SystemRoot%\NTDS\ntds.dit
        
    - NTDS-Protokolldateien im selben Verzeichnis
        
4. **LSASS-Memory und Credential Speicherauszüge**  
    Extrahieren Sie mit Tools wie `procdump` oder `comsvcs.dll` einen Speicherabbild von lsass.exe, um gespeicherte Anmeldeinformationen zu extrahieren.
    
5. **Gruppenrichtlinien und Scheduled Tasks**
    
    - C:\Windows\System32\GroupPolicy\Machine\Registry.pol
        
    - C:\Windows\System32\Tasks*
        
6. **Netzlaufwerke und Freigaben**  
    Prüfen Sie offene oder beschreibbare Freigaben:
    
    - Befehl `net share`
        
    - UNC-Pfade auf entfernte Hosts
        
7. **Konfigurationsdateien und PEM-Zertifikate**
    
    - IIS: C:\Windows\System32\inetsrv\config\applicationHost.config
        
    - Zertifikat-Stores und private Keys: C:\ProgramData\Microsoft\Crypto\RSA\MachineKeys
        
8. **Benutzerprofile und Autostart**  
    – C:\Users<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup  
    – C:\Users<User>\NTUSER.DAT
    
9. **Dienst- und Treiberkonfigurationen**  
    – C:\Windows\System32\drivers*.sys  
    – Diensteinträge via `sc query`