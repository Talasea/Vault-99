
Ein Active Directory Forest (AD Forest) ist die höchste Organisationsebene in einer Active Directory-Konfiguration. Es umfasst eine oder mehrere Domänen und bildet die Grundlage für die Verwaltung von Benutzern, Computern und Gruppenrichtlinien. Jeder Forest teilt sich eine einzige Datenbank, eine globale Adressliste (Global Address List, GAL) und eine Sicherheitsgrenze. Standardmäßig kann ein Benutzer oder Administrator in einem Forest nicht auf einen anderen Forest zugreifen.

Innerhalb eines Forests können mehrere Domänen existieren, die durch sogenannte Vertrauensstellungen (Trusts) miteinander verbunden sind. Diese Vertrauensstellungen ermöglichen es Benutzern, auf Ressourcen in anderen Domänen zuzugreifen. Es gibt verschiedene Modelle für Forests, wie das Organisatorische Gesamtstrukturmodell, das Ressourcen-Gesamtstrukturmodell und das Modell mit eingeschränktem Zugriff.

Die Entscheidung, ob ein Unternehmen ein Single Forest oder ein Multi Forest Modell einsetzt, hängt von den spezifischen Anforderungen ab. Ein Single Forest ist die bevorzugte Wahl für die meisten Unternehmen, solange keine administrative Trennung oder ein separates Schema erforderlich ist. Ein Multi Forest Modell kann jedoch sinnvoll sein, wenn es zu einer administrativen Trennung oder einem separaten Schema kommt.

Die Erstellung eines Forests beginnt mit der Installation von Windows Server und der Bereitstellung der Active Directory Domain Services-Rolle und der DNS-Serverrolle. Nach dem Aufbau des Forests können Domänen hinzugefügt und Vertrauensstellungen zwischen diesen eingerichtet werden.

![[Pasted image 20250124123249.png]]