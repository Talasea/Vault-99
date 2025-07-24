
Active Directory (AD) ist ein Verzeichnisdienst von Microsoft, der erstmals mit Windows 2000 eingeführt wurde. Es ermöglicht die zentrale Verwaltung von Netzwerkinformationen und -ressourcen in Windows-basierten Netzwerken. Hier sind einige wichtige Aspekte:

- **Entwickler**: Microsoft
- **Erscheinungsjahr**: 1999
- **Betriebssystem**: Windows

Active Directory speichert Informationen zu Benutzern, Computern, Anwendungen, Druckern und freigegebenen Ordnern. Diese Informationen sind in einer hierarchischen Struktur organisiert, was es ermöglicht, Netzwerkinformationen nach der realen Struktur eines Unternehmens oder seiner räumlichen Verteilung zu gliedern.

Der Dienst besteht aus verschiedenen Komponenten, darunter Active Directory Domain Services (AD DS), die die grundlegenden Verzeichnisfunktionen bereitstellen, und Active Directory Lightweight Directory Services (AD LDS), die eine reduzierte Version des AD DS sind und speziell für Anwendungen entwickelt wurden, die LDAP-konforme Informationen benötigen.

Zur Sicherheit bietet Active Directory Funktionen wie Anmeldeauthentifizierung und Zugriffssteuerung, die es Benutzern ermöglichen, sich einmal anzumelden und auf Ressourcen im gesamten Netzwerk zuzugreifen. Es verwendet Protokolle wie LDAP, Kerberos und SMB.

Am 5. Januar 2025 wurde eine Schwachstelle in Active Directory gemeldet, die ungepatchte Windows Server zu einem Absturz bringen kann. Microsoft hat diese Schwachstelle im Dezember 2024 gepatcht, aber ungepatchte Systeme bleiben anfällig.


https://learn.microsoft.com/de-de/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview