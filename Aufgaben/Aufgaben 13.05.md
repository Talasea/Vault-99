DS -> Datensatz

DB -> Datenbank

  

  

# ##############################################################################################

  

Aufgabe 1: 'Adressverwaltung'

  

   1 - Die Adressverwaltung soll folgende Daten organisieren:

       - Name, Vorname, Straße, Hausnummer, PLZ, Ort, Email, Telefon1, Telefon2, Gebutrtsdatum

       - nicht verwendete Daten sollen in der DB eindeutig gekennzeichnet sein, z.B. durch '<na>'

   2 - Es soll möglich sein alle (komplette DB) bzw. einzelne Daten (also Personen) anzuzeigen

   3 - Es soll möglich sein neue DS anzulegen

   4 - Möglichkeit DS zu ändern (falls mal Jemand heiratet oder umzieht ...)

   5 - Möglichkeit DS zu löschen

   6 - Suche nach einem Kriterium (z.B. Nachname oder PLZ)

   7 - Zusatz:

       Implementiere eine Backupfunktion. (Verwende u.a. das Modul 'datetime'

       Das Backup soll je halbe Stunde in das Unterverzeichnis './Backup' geschrieben werden.

  

Hinweis: Die DB soll als CSV-Datei bereit gestellt werden.

  

# ##############################################################################################

  

Aufgabe 2: 'Brute Force'

  

  Erstellen eines Programms, um das Passwort einer verschlüsselten Datei herauszufinden.

  

  1 - Verwendung einer vorhandenen Datenbankdatei (z.B. rockyou.txt')

  2 - Implementierung eines Algorithmus zur Umgehung von Maßnahmen gegen Brute Force.

  3 - Es soll getrackt werden, welche Einträge bereits abgearbeitet wurden.

  4 - Ergebnisse sollen gesichert werden.

  5 - Bei Erfolg soll das gefundene Passwort im Klartext ausgegeben werden.

  6 - Am Anfang soll angegeben werden welcher Hash-Algorithmus benutzt wird.


security-toolkit/
├── pyproject.toml
├── requirements.txt
├── src/
│   └── security_toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── os_detection.py
│       │   ├── logging_utils.py
│       │   └── sandbox_detection.py
│       ├── password_cracking/
│       │   ├── __init__.py
│       │   ├── brute_force.py
│       │   ├── dictionary_attack.py
│       │   ├── rainbow_tables.py
│       │   ├── markov_chains.py
│       │   └── hybrid_attack.py
│       ├── network/
│       │   ├── __init__.py
│       │   ├── mac_changer.py
│       │   └── ip_randomizer.py
│       ├── optimization/
│       │   ├── __init__.py
│       │   ├── multiprocessing_utils.py
│       │   ├── gpu_support.py
│       │   └── memory_mapping.py
│       ├── security/
│       │   ├── __init__.py
│       │   ├── stealth_mode.py
│       │   ├── random_delays.py
│       │   └── auto_deactivation.py
│       └── target_handlers/
│           ├── __init__.py
│           ├── console_handler.py
│           ├── web_handler.py
│           └── gui_handler.py
├── tests/
│   ├── __init__.py
│   ├── test_password_cracking.py
│   └── test_network.py
└── docs/
    ├── api_reference.md
    ├── security_guidelines.md
    └── troubleshooting.md
