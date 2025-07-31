- **Kerndefinition:** **Pseudonymität** ist ein Datenschutzkonzept, bei dem personenbezogene Daten so verarbeitet werden, dass sie ohne Hinzuziehung zusätzlicher Informationen nicht mehr einer spezifischen betroffenen Person zugeordnet werden können. Im Gegensatz zur Anonymität ist die Re-Identifizierung der Person jedoch weiterhin möglich, wenn man über den "Schlüssel" (die zusätzlichen Informationen) verfügt.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Ein gängiges technisches Verfahren zur Pseudonymisierung ist das Ersetzen von direkten Identifikatoren (wie Name oder E-Mail-Adresse) durch einen künstlichen Bezeichner, ein sogenanntes Pseudonym (z. B. eine zufällige ID wie "User-4XF87"). Die Zuordnungstabelle, die das Pseudonym mit dem echten Namen verknüpft, muss getrennt von den pseudonymisierten Daten und sicher aufbewahrt werden.
        
    - **Zweck:** Das Ziel ist es, die Risiken für die betroffenen Personen bei der Datenverarbeitung zu verringern. Es ermöglicht die Analyse von Daten (z. B. für statistische Zwecke oder Forschung), ohne die Identität der Personen direkt preiszugeben.
        
- **Einordnung in den Gesamtkontext:** Pseudonymität ist ein Mittelweg zwischen der Verarbeitung von Klardaten und der vollständigen **Anonymisierung**.
    
    - **Anonymisierung:** Die Daten werden so verändert, dass eine Re-Identifizierung der Person unmöglich oder nur mit unverhältnismäßig hohem Aufwand möglich ist. Anonymisierte Daten fallen nicht mehr unter die DSGVO.
        
    - **Pseudonymisierung:** Die Daten gelten weiterhin als personenbezogene Daten im Sinne der DSGVO, da die Möglichkeit der Re-Identifizierung besteht. Die Pseudonymisierung wird jedoch in der DSGVO explizit als eine empfohlene technische und organisatorische Maßnahme (TOM) zum Schutz der Daten genannt.
        
- **Sicherheitsaspekte:** Die Sicherheit des gesamten Prozesses hängt von der strikten Trennung der pseudonymisierten Daten und der Zuordnungsinformationen ab. Wenn ein Angreifer Zugriff auf beide Datensätze erlangt, ist die Pseudonymisierung aufgehoben. Die Stärke der Pseudonymisierung hängt auch von der Art der verbleibenden Daten ab. Wenn aus den pseudonymisierten Daten (z. B. seltene Merkmalskombinationen) indirekt auf eine Person geschlossen werden kann, ist der Schutz gering.
    
- **Praxisbeispiel / Analogie:** Pseudonymität ist wie ein Autor, der unter einem Künstlernamen (Pseudonym) schreibt. Die Öffentlichkeit kennt nur den Künstlernamen und kann die Bücher nicht direkt mit der Privatperson des Autors in Verbindung bringen. Der Verlag (der die Zuordnungsinformationen besitzt) kennt jedoch die wahre Identität des Autors, zum Beispiel um ihm seine Tantiemen auszuzahlen.
    
- **Fazit / Bedeutung für IT-Profis:** Für Datenschutzbeauftragte, Softwareentwickler und Datenanalysten ist die Pseudonymisierung eine zentrale Technik, um die Anforderungen der DSGVO zu erfüllen und gleichzeitig einen Nutzen aus Daten zu ziehen. IT-Profis müssen die geeigneten technischen Verfahren auswählen und implementieren und vor allem die organisatorischen Maßnahmen zur sicheren Aufbewahrung der "Schlüsselinformationen" gewährleisten.