![[Pasted image 20250124122603.png]]
Ein Domain Controller (DC) ist ein Server, der für die zentrale Authentifizierung von Computern und Benutzern in einem Netzwerk verantwortlich ist. Er verwaltet die Benutzerkonten, Passwörter und Gruppenzugehörigkeiten und stellt sicher, dass diese Informationen für alle Computer in der Domain konsistent sind. Der Domain Controller ist ein wesentlicher Bestandteil von Windows-Netzwerken und wurde ursprünglich von IBM in den 1970er Jahren eingeführt und später von Microsoft in Windows NT übernommen. Er ermöglicht es, Benutzerrechte und -zugriffe zentral zu verwalten und sicherzustellen, dass Änderungen für alle Computer in der Domain wirksam werden.



Primary
Ein Primärer Domänencontroller (Primary Domain Controller, PDC) ist ein Server, der in einem Netzwerk für die Verwaltung und Authentifizierung von Benutzern und Computern zuständig ist. Er fungiert als zentrale Instanz für die Verwaltung von Benutzerkonten und Sicherheitsrichtlinien. In früheren Windows-Systemen, wie NT 4.0, konnten Änderungen nur auf dem PDC vorgenommen werden, während Backup-Domänencontroller (BDC) nur Sicherheitskopien dieser Daten hielten und regelmäßig aktualisiert wurden.

Seit Windows 2000 hat sich die Architektur geändert, sodass alle Domänencontroller (DC) eine beschreibbare Kopie der Active-Directory-Datenbank haben, was eine bessere Verfügbarkeit und Replikation ermöglicht. In aktuellen Windows-Umgebungen ist der Begriff PDC nicht mehr so relevant, da alle DCs gleichberechtigt sind und Änderungen in regelmäßigen Abständen repliziert werden.

Es ist üblich, mehrere DCs in einer Domäne zu betreiben, um Ausfallzeiten zu minimieren und die Verfügbarkeit zu erhöhen. Ein PDC in modernen Umgebungen ist eher ein historischer Begriff und wird nicht mehr verwendet, um die Rolle eines DCs zu beschreiben.

secondery

Ein sekundärer Domänencontroller (DC) ist ein Server, der in einem Active Directory (AD) Netzwerk verwendet wird, um die Verfügbarkeit und Zuverlässigkeit des Netzwerks zu gewährleisten. Er übernimmt die Aufgaben des primären Domänencontrollers (PDC), falls dieser ausfällt, und hilft dabei, Lasten zu verteilen und die Leistung zu verbessern.

Hier sind einige wichtige Punkte zur Erklärung des sekundären Domänencontrollers:

- **Redundanz**: Ein sekundärer Domänencontroller bietet eine Sicherung für den primären Domänencontroller. Wenn der primäre DC ausfällt, übernimmt der sekundäre DC die Rolle, um sicherzustellen, dass das Netzwerk weiterhin funktioniert.
- **Lastverteilung**: Bei großen Netzwerken mit vielen Benutzern hilft ein sekundärer DC, die Last von Authentifizierungs- und Autorisierungsanfragen zu verteilen, was die Leistung verbessert und die Wahrscheinlichkeit reduziert, dass der primäre DC überlastet wird.
- **Sicherheit**: Ein sekundärer DC an einem entfernten Standort erhöht die Sicherheit, indem er eine Abkopie der Daten bereitstellt, die zum Wiederherstellen des Netzwerks im Falle eines Sicherheitsvorfalls verwendet werden kann.
- **Fehlerbehebung**: Durch die regelmäßige Replikation von Verzeichnisinformationen zwischen Domänencontrollern wird sichergestellt, dass Änderungen in einem Teil des Netzwerks in Echtzeit in das gesamte Netzwerk übertragen werden. Dies verhindert Probleme wie veraltete Benutzerkontoinformationen oder inkonsistente Gruppenrichtlinien.

Um einen sekundären Domänencontroller hinzuzufügen, müssen Sie einige Vorbereitungsarbeiten durchführen, wie zum Beispiel die Festlegung des Computernamens, die Konfiguration der IP-Einstellungen und die Überprüfung der Zeitzone. Anschließend können Sie den Server als Domänencontroller hochgradigen und die notwendigen Features hinzufügen.