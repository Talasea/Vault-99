---
created: 2024-12-06T17:12
updated: 2024-12-09T12:31
---
Ihr werdet ein völlig neues AD definieren. Beim Thema seid ihr diesmal frei, lediglich die Struktur soll den Vorgaben entsprechen.

# Netzwerk
* Das Netzwerk wird wieder aus einen Domain Controller und einen Client bestehen. Konfiguriert hierfür einen neuen Switch in `HyperV`. Die beiden Geräte sollen ausschließlich über diesem Switch verbunden sein. Das Netzwerk ist `172.16.0.0/16`.

# Active Directory
## Organisationseinheiten
* Es sollen zwei OUs, nachfolgende OU1 und OU2 genannt, angelegt werden
* OU1 hat zusätzlich zwei unterOUs, unterOU1 und unterOU2
## Benutzer
* Fünf beliebige Benuzter sollen in OU2 angelegt werden
* Jeweils drei Benutzer in unterOU1 und unterOU2
* Einer Eurer Benutzer soll Mitglied der Domänen-Admin Gruppe sein
## Gruppen
(Verwendet das IDGLA Designkonzept für die Gruppenstruktur)
* Definiert drei globale Gruppen (diese Gruppen sollen keine besonderen Berechtigungen bekommen)
* Definiert mindestens zwei domänen lokale Gruppen
	* Den Gruppen sollen die Berechtigungen für Freigaben zugeteilt werden
	* Die globalen Gruppen sollen Mitglieder dieser Gruppen sein
## Freigaben
Alle Ordner für die Freigabe sollen **auf dem DC im Ordner `C:\Shares`** erstellt werden
* Ein Share um die Hintergründe lesend für alle Domänen-Benutzer zur Verfügung zu stellen
* Definiert mindestens zwei zusätzliche Freigabe mit Inhalt Eurer Wahl. Zugang zu diesen Freigaben soll ausschließlich über die domänen lokalen Gruppen geregelt werden
## GPOs
* Es soll eine lokale Gruppe auf dem Client mittels GPO eingerichtet werden
* Der Desktophintergrund soll basierend auf den OUs angelegt werden. Benutzer in OU1 sollen Hintergrund1 haben, Benutzer in OU2 sollen Hintergrund 2 haben. Für unterOU1 soll die Vererbung des Hintergrundes deaktiviert sein.
* Die Skriptausführung soll für alle Benutzer aus OU2 erlaubt sein
* Entgegengesetzt soll die Skriptausführung für alle Benutzer aus OU1 **verboten** sein
* Auf dem Client soll eine beliebige Anmeldenachricht konfiguriert werden, **auf dem DC eine andere**
* Das Verwenden von USB-Geräten soll aus Sicherheitsgründen an allen Geräten deaktiviert sein

