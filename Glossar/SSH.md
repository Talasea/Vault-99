
SSH (Secure Shell) ist ein Netzwerkprotokoll, das eine sichere Verbindung zwischen zwei Computern über ein unsicheres Netzwerk ermöglicht. Hier ist eine ausführliche Erklärung von SSH:

**Grundlagen:**

- **Zweck:**
    - SSH ermöglicht die sichere Fernverwaltung von Computern.
    - Es verschlüsselt die gesamte Kommunikation, um sensible Daten vor dem Abfangen zu schützen.
    - Es wird häufig verwendet, um auf Server zuzugreifen, Dateien zu übertragen und Befehle auszuführen.
- **Funktionsweise:**
    - SSH verwendet kryptografische Techniken, um eine sichere Verbindung aufzubauen.
    - Es verwendet Public-Key-Kryptographie zur Authentifizierung des Servers und des Clients.
    - Nach der Authentifizierung werden alle Daten, die zwischen den beiden Computern ausgetauscht werden, verschlüsselt.
- **Komponenten:**
    - **SSH-Client:** Das Programm, das die Verbindung zum entfernten Server initiiert.
    - **SSH-Server:** Das Programm auf dem entfernten Computer, das Verbindungen akzeptiert.

**Wichtige Aspekte:**

- **Verschlüsselung:**
    - SSH verwendet starke Verschlüsselungsalgorithmen, um die Daten zu schützen.
    - Dies verhindert, dass Angreifer die Kommunikation abhören oder manipulieren können.
- **Authentifizierung:**
    - SSH bietet verschiedene Authentifizierungsmethoden, darunter:
        - Passwortbasierte Authentifizierung: Benutzer geben ein Passwort ein, um sich anzumelden.
        - Schlüsselbasierte Authentifizierung: Benutzer verwenden ein Schlüsselpaar (öffentlicher und privater Schlüssel) zur Authentifizierung. Dies gilt als sicherer als die Passwortauthentifizierung.
- **Anwendungen:**
    - Fernverwaltung von Servern: SSH ist ein unverzichtbares Werkzeug für Systemadministratoren.
    - Sichere Dateiübertragung: SSH kann verwendet werden, um Dateien sicher zwischen Computern zu übertragen (z.B. mit `scp` oder `sftp`).
    - Tunneling: SSH kann verwendet werden, um verschlüsselte Tunnel durch unsichere Netzwerke zu erstellen.

**Schlüsselbasierte Authentifizierung:**

- Bei der schlüsselbasierten Authentifizierung wird ein Schlüsselpaar erzeugt:
    - **Öffentlicher Schlüssel:** Dieser kann frei weitergegeben werden und wird auf dem Server platziert.
    - **Privater Schlüssel:** Dieser muss geheim gehalten werden und wird auf dem Client-Computer gespeichert.
- Wenn der Client eine Verbindung zum Server herstellt, verwendet der Server den öffentlichen Schlüssel, um den Client zu authentifizieren.
- Da der private Schlüssel niemals über das Netzwerk übertragen wird, ist diese Methode sicherer als die passwortbasierte Authentifizierung.