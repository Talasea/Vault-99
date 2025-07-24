---
created: 2025-01-17T10:33
updated: 2025-01-17T12:18
---
GitHub Seite des Codes: https://github.com/Orange-Cyberdefense/arsenal

Fix TIOCSTI issue for current session

```bash
sudo sysctl -w dev.tty.legacy_tiocsti=1
```

Alias anliegen für komfortable Benutzung (Pfade anpassen bei Bedarf)

```bash
 alias arsenal="source ~/arsenal/venv/bin/activate; ~/arsenal/run; deactivate"
```

# Installation

Herunterladen des Codeprojektes

```bash
git clone https://github.com/Orange-Cyberdefense/arsenal.git
```

Wechseln in den Ordner

```bash
cd arsenal
```

Erstellen eine virtuelle Python Umgebung

```bash
python3 -m venv venv # Das zweite venv ist hierbei der Name der virtuellen Umgebung
```

Virtuelle Python Umgebung **aktivieren**

```bash
source venv/bin/activate
```

Wir installieren die Abhängigkeiten für `arsenal`

```bash
pip3 install -r requirements.txt
```

Jetzt können wir `arsenal` starten

```bash
./run
```
