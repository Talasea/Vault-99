- **Kerndefinition:** Ein **Supply-Chain-Angriff** ist eine Art von Cyberangriff, bei dem ein Angreifer ein Unternehmen nicht direkt, sondern indirekt über einen seiner Zulieferer oder Partner in der Lieferkette kompromittiert. Der Angreifer infiltriert ein schwächer gesichertes Glied der Kette, um dessen vertrauenswürdige Beziehung zum eigentlichen Ziel für einen Angriff auszunutzen.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Der Angreifer identifiziert einen Zulieferer des Zielunternehmens, der Software, Hardware oder Dienstleistungen bereitstellt. Er kompromittiert diesen Zulieferer und manipuliert dessen Produkte. Beispielsweise wird bösartiger Code in ein legitimes Software-Update eingeschleust. Das Zielunternehmen installiert dieses vertrauenswürdige Update und infiziert sich so unwissentlich selbst.
        
    - **Zweck:** Das Ziel ist es, die oft starken Verteidigungsmaßnahmen des eigentlichen Ziels zu umgehen, indem man durch eine "vertrauenswürdige Vordertür" eindringt.
        
- **Einordnung in den Gesamtkontext:** Lieferkettenangriffe sind eine hochentwickelte und gefährliche Form von **Advanced Persistent Threats (APTs)**. Sie sind schwer zu erkennen, da die Kompromittierung über einen legitimen Kanal erfolgt. Berühmte Beispiele, die die enorme Reichweite und den Schaden solcher Angriffe verdeutlichen, sind der **SolarWinds/Sunburst-Angriff** und der **NotPetya**-Vorfall.
    
- **Sicherheitsaspekte:** Dies ist ein reines Cybersicherheitsthema und eine der größten Herausforderungen für moderne Unternehmen. Es verdeutlicht, dass die eigene Sicherheit untrennbar mit der Sicherheit der gesamten Lieferkette verbunden ist. Abwehrmaßnahmen umfassen:
    
    - **Third-Party Risk Management:** Strenge Überprüfung der Sicherheitspraktiken von Lieferanten.
        
    - **Software-Integritätsprüfung:** Überprüfung von Hashes und digitalen Signaturen von Software-Updates.
        
    - **Prinzip der geringsten Rechte:** Sicherstellen, dass Software nur die absolut notwendigen Berechtigungen hat.
        
- **Praxisbeispiel / Analogie:** Stellen Sie sich eine mittelalterliche Festung vor, die uneinnehmbar scheint. Anstatt die Mauern direkt anzugreifen, besticht ein Feind den Bauern, der täglich Lebensmittel in die Festung liefert. Der Feind versteckt seine Soldaten in den Lebensmittelkarren. Da die Wachen dem Bauern vertrauen, kontrollieren sie die Lieferung nur oberflächlich und lassen die Soldaten unwissentlich in die Festung.
    
- **Fazit / Bedeutung für IT-Profis:** Für CISOs und Sicherheitsteams bedeutet die Bedrohung durch Lieferkettenangriffe eine fundamentale Erweiterung des Sicherheitsdenkens. Es reicht nicht mehr aus, nur die eigenen Systeme zu schützen. Ein proaktives Management der Risiken, die von Drittanbietern ausgehen, und die Implementierung einer "Zero Trust"-Architektur, bei der auch internem Verkehr nicht standardmäßig vertraut wird, sind unerlässlich.