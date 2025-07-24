
**CVE (Common Vulnerabilities and Exposures)**

**Was ist CVE?**

CVE steht für **Common Vulnerabilities and Exposures** (Gemeinsame Schwachstellen und Gefährdungen). Es handelt sich um ein **standardisiertes System zur Identifizierung, Benennung und Katalogisierung öffentlich bekannter Sicherheitslücken** in Software und Firmware. Man kann sich CVE wie ein Wörterbuch oder eine Enzyklopädie für Sicherheitslücken vorstellen.

**Zweck von CVE:**

Der Hauptzweck von CVE ist es, eine **eindeutige und konsistente Methode zur Beschreibung von Sicherheitslücken** bereitzustellen. Dies ermöglicht:

- **Klare Kommunikation:** Sicherheitsforscher, Softwarehersteller, Anbieter von Sicherheitstools und Endnutzer können über dieselbe Schwachstelle sprechen und sich darauf beziehen, ohne Verwirrung durch unterschiedliche Bezeichnungen.
- **Verbesserte Suche und Nachverfolgung:** CVE-IDs ermöglichen es, Informationen über spezifische Schwachstellen in verschiedenen Quellen (Sicherheitsbulletins, Datenbanken, Tools usw.) zu finden und zu verfolgen.
- **Effektives Vulnerability Management:** Unternehmen können CVE-IDs nutzen, um ihre Systeme auf bekannte Schwachstellen zu überprüfen und ihre Prioritäten bei der Behebung zu setzen.
- **Automatisierung:** Sicherheitstools und -prozesse können CVE-IDs verwenden, um Schwachstellen automatisch zu erkennen, zu melden und zu beheben.

**Verwaltung von CVE:**

CVE wird von der **MITRE Corporation** verwaltet und betrieben, mit finanzieller Unterstützung durch die **Cybersecurity and Infrastructure Security Agency (CISA)** des US-amerikanischen Heimatschutzministeriums. MITRE ist eine gemeinnützige Organisation, die sich mit Forschung und Entwicklung im öffentlichen Interesse beschäftigt.

**CVE-Identifikator (CVE-ID):**

Jeder bekannten Schwachstelle wird eine **eindeutige CVE-Identifikationsnummer (CVE-ID)** zugewiesen. Diese ID hat typischerweise das Format:

**CVE-YYYY-NNNNN**

- **CVE:** Präfix, das "Common Vulnerabilities and Exposures" kennzeichnet.
- **YYYY:** Das vierstellige Jahr, in dem die CVE-ID veröffentlicht wurde.
- **NNNNN:** Eine eindeutige, fortlaufende Ziffernfolge (mindestens vier Ziffern, kann bei Bedarf erweitert werden).

**Beispiel einer CVE-ID:** CVE-2023-12345

**Wie werden CVE-IDs vergeben?**

Der Prozess der CVE-ID-Vergabe beinhaltet typischerweise:

1. **Entdeckung einer Schwachstelle:** Sicherheitsforscher, Softwareanbieter oder andere finden eine Sicherheitslücke in einem Produkt.
2. **Meldung (Disclosure):** Die Entdecker melden die Schwachstelle in der Regel dem betroffenen Softwareanbieter und/oder einer CVE Numbering Authority (CNA).
3. **CVE-ID-Anfrage:** Der Anbieter oder die CNA beantragt eine CVE-ID bei der MITRE Corporation.
4. **CVE-ID-Zuweisung:** MITRE prüft den Antrag und weist, falls die Schwachstelle validiert wird, eine eindeutige CVE-ID zu.
5. **Veröffentlichung der CVE-Informationen:** Die Details der Schwachstelle werden in der CVE-Liste veröffentlicht, oft zusammen mit Informationen zur Behebung (Patches).

**Wo finde ich CVE-Informationen?**

Die offizielle Quelle für CVE-Informationen ist die **CVE List** auf der MITRE-Webseite: [https://cve.mitre.org/](https://www.google.com/url?sa=E&source=gmail&q=https://cve.mitre.org/)

Es gibt auch viele andere Ressourcen, die CVE-Informationen aggregieren und bereitstellen, darunter:

- **Nationale Schwachstellendatenbank (NVD) des NIST:** [https://nvd.nist.gov/](https://www.google.com/url?sa=E&source=gmail&q=https://nvd.nist.gov/) (NVD ist eine erweiterte Datenbank, die CVE-Informationen mit CVSS-Bewertungen und weiteren Details anreichert.)
- **Sicherheitsbulletins von Softwareanbietern:** (z.B. Microsoft Security Bulletins, Adobe Security Bulletins, etc.)
- **Kommerzielle und Open-Source-Vulnerability-Scanner:** Diese Tools verwenden CVE-IDs, um Systeme auf bekannte Schwachstellen zu überprüfen.

**CVSS (Common Vulnerability Scoring System)**

**Was ist CVSS?**

CVSS steht für **Common Vulnerability Scoring System** (Gemeinsames Bewertungssystem für Schwachstellen). Es ist ein **offener Industriestandard zur Bewertung des Schweregrads von Sicherheitslücken**. CVSS bietet eine standardisierte und numerische Bewertung, die den Schweregrad einer Schwachstelle widerspiegelt und hilft, Prioritäten für die Behebung zu setzen.

**Zweck von CVSS:**

Der Hauptzweck von CVSS ist es, eine **objektive und messbare Methode zur Quantifizierung des Schweregrads** einer Sicherheitslücke zu bieten. Dies ermöglicht:

- **Priorisierung von Behebungsmaßnahmen:** Sicherheitsteams können CVSS-Scores nutzen, um zu entscheiden, welche Schwachstellen zuerst behoben werden müssen. Höhere Scores bedeuten in der Regel eine höhere Priorität.
- **Vergleich von Schwachstellen:** CVSS ermöglicht es, den Schweregrad verschiedener Schwachstellen zu vergleichen, auch wenn sie unterschiedliche Systeme oder Produkte betreffen.
- **Risikobewertung:** CVSS-Scores sind ein wichtiger Bestandteil von Risikobewertungen, um das Gesamtrisiko einer IT-Umgebung zu beurteilen.
- **Kommunikation des Schweregrads:** CVSS-Scores werden oft in Sicherheitsbulletins, Vulnerability Reports und anderen Kommunikationen verwendet, um den Schweregrad einer Schwachstelle klar und präzise zu vermitteln.

**Verwaltung von CVSS:**

CVSS wird von **FIRST.org** (Forum of Incident Response and Security Teams) entwickelt und gepflegt. FIRST.org ist eine internationale Organisation, die Incident-Response-Teams aus der ganzen Welt zusammenbringt.

**CVSS Metrikgruppen:**

CVSS verwendet drei Metrikgruppen, um den Schweregrad einer Schwachstelle zu bewerten:

1. **Basis-Metriken (Base Metrics):** Diese Metriken beschreiben die intrinsischen Eigenschaften der Schwachstelle, die über alle Installationen hinweg konstant sind. Sie umfassen:
    
    - **Exploitability Metrics (Ausnutzbarkeits-Metriken):** Beschreiben, wie einfach es ist, die Schwachstelle auszunutzen.
        
        - **Attack Vector (Angriffsvektor):** Wie kann die Schwachstelle erreicht werden (Netzwerk, Lokal, Physikalisch, Adjacent Network)?
        - **Attack Complexity (Angriffskomplexität):** Wie komplex ist es, einen Angriff auszuführen (Niedrig, Hoch)?
        - **Privileges Required (Erforderliche Privilegien):** Welche Berechtigungen benötigt der Angreifer, um die Schwachstelle auszunutzen (Keine, Niedrig, Hoch)?
        - **User Interaction (Benutzerinteraktion):** Ist eine Benutzerinteraktion erforderlich, um die Schwachstelle auszunutzen (Keine, Erforderlich)?
        - **Scope (Wirkungsbereich):** Ändert sich der Wirkungsbereich der Sicherheitsauswirkung über die kompromittierte Komponente hinaus (Unverändert, Geändert)?
    - **Impact Metrics (Auswirkungs-Metriken):** Beschreiben die direkten Folgen einer erfolgreichen Ausnutzung.
        
        - **Confidentiality Impact (Auswirkung auf die Vertraulichkeit):** Verlust der Vertraulichkeit von Daten (Keine, Niedrig, Hoch)?
        - **Integrity Impact (Auswirkung auf die Integrität):** Verlust der Integrität von Daten (Keine, Niedrig, Hoch)?
        - **Availability Impact (Auswirkung auf die Verfügbarkeit):** Verlust der Verfügbarkeit von Ressourcen (Keine, Niedrig, Hoch)?
2. **Temporale Metriken (Temporal Metrics):** Diese Metriken beschreiben die zeitlichen Aspekte der Schwachstelle, die sich im Laufe der Zeit ändern können. Sie umfassen:
    
    - **Exploit Code Maturity (Reife des Exploit-Codes):** Wie ausgereift ist der Exploit-Code (Nicht definiert, Proof-of-Concept, Funktionaler Exploit, Hoch)?
    - **Remediation Level (Abhilfestufe):** Welche Art von Abhilfe ist verfügbar (Nicht definiert, Offizieller Patch, Temporäre Abhilfe, Workaround, Nicht verfügbar)?
    - **Report Confidence (Vertrauenswürdigkeit des Berichts):** Wie vertrauenswürdig ist der Bericht über die Schwachstelle (Nicht definiert, Unbestätigt, Vernünftig, Bestätigt)?
3. **Umgebungsmetriken (Environmental Metrics):** Diese Metriken beschreiben die Merkmale der Umgebung, in der die betroffene Software eingesetzt wird. Sie ermöglichen es, den CVSS-Score an die spezifische Situation eines Unternehmens anzupassen. Sie umfassen:
    
    - **Confidentiality Requirement (Anforderung an die Vertraulichkeit):** Wie wichtig ist die Vertraulichkeit der betroffenen Daten (Nicht definiert, Niedrig, Mittel, Hoch)?
    - **Integrity Requirement (Anforderung an die Integrität):** Wie wichtig ist die Integrität der betroffenen Daten (Nicht definiert, Niedrig, Mittel, Hoch)?
    - **Availability Requirement (Anforderung an die Verfügbarkeit):** Wie wichtig ist die Verfügbarkeit der betroffenen Systeme (Nicht definiert, Niedrig, Mittel, Hoch)?
    - **Modified Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality Impact, Integrity Impact, Availability Impact:** Diese Metriken ermöglichen es, die Basis-Metriken basierend auf der spezifischen Umgebung anzupassen.

**CVSS Score und Severity Rating:**

Basierend auf den ausgewählten Metrikwerten berechnet CVSS einen numerischen **Score** zwischen **0.0 und 10.0**. Dieser Score wird dann in ein **Severity Rating** (Schweregradbewertung) übersetzt:

- **0.0:** None (Keine)
- **0.1 - 3.9:** Low (Niedrig)
- **4.0 - 6.9:** Medium (Mittel)
- **7.0 - 8.9:** High (Hoch)
- **9.0 - 10.0:** Critical (Kritisch)

**Wie werden CVSS-Scores berechnet?**

Die Berechnung des CVSS-Scores ist komplex und basiert auf Formeln, die die Gewichtung der verschiedenen Metriken berücksichtigen. Es gibt online CVSS-Rechner, die verwendet werden können, um den Score basierend auf den ausgewählten Metrikwerten zu berechnen (z.B. auf der NVD-Webseite oder über Online-CVSS-Rechner).

**Beispiel eines CVSS-Vektors (CVSS Vector String):**

Der CVSS-Vektor ist eine Textzeichenfolge, die die Werte der ausgewählten Metriken in einer standardisierten Form darstellt. Dies ermöglicht es, die genaue Berechnung des CVSS-Scores zu reproduzieren.

**Beispiel eines CVSS v3.1 Vektors:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

Dieser Vektor beschreibt eine Schwachstelle mit folgenden Eigenschaften:

- **AV:N (Attack Vector: Network):** Angriffsvektor ist das Netzwerk.
- **AC:L (Attack Complexity: Low):** Angriffskomplexität ist niedrig.
- **PR:N (Privileges Required: None):** Keine Privilegien erforderlich.
- **UI:N (User Interaction: None):** Keine Benutzerinteraktion erforderlich.
- **S:U (Scope: Unchanged):** Wirkungsbereich ist unverändert.
- **C:H (Confidentiality Impact: High):** Hohe Auswirkung auf die Vertraulichkeit.
- **I:H (Integrity Impact: High):** Hohe Auswirkung auf die Integrität.
- **A:H (Availability Impact: High):** Hohe Auswirkung auf die Verfügbarkeit.

Dieser Vektor würde zu einem **CVSS Base Score von 9.8 (Critical)** führen.

**Wo finde ich CVSS-Scores?**

- **Nationale Schwachstellendatenbank (NVD) des NIST:** Die NVD ist die umfangreichste Quelle für CVSS-Scores, da sie CVE-Informationen mit CVSS-Bewertungen anreichert.
- **Sicherheitsbulletins von Softwareanbietern:** Viele Anbieter geben in 1 ihren Bulletins CVSS-Scores für die behandelten Schwachstellen an.  
    
    [
    
    1. www.openlogic.com
    
    ](https://www.openlogic.com/blog/understanding-cves-cvss-scores)
    
    [
    
    www.openlogic.com
    
    ](https://www.openlogic.com/blog/understanding-cves-cvss-scores)
    
- **Vulnerability-Scanner und Sicherheits-Tools:** Viele Tools berechnen oder zeigen CVSS-Scores für erkannte Schwachstellen an.

**Zusammenhang zwischen CVE und CVSS**

CVE und CVSS sind eng miteinander verbunden und ergänzen sich:

- **CVE identifiziert die Schwachstelle:** CVE liefert eine eindeutige ID und Beschreibung der Sicherheitslücke.
- **CVSS bewertet den Schweregrad:** CVSS quantifiziert den Schweregrad der durch die CVE identifizierten Schwachstelle.

In der Praxis werden CVE-IDs oft mit CVSS-Scores zusammen verwendet. Wenn eine neue Schwachstelle entdeckt und eine CVE-ID zugewiesen wird, wird in vielen Fällen auch eine CVSS-Bewertung durchgeführt und veröffentlicht, um den Schweregrad der Schwachstelle zu verdeutlichen.

**Beispielhafte Anwendung:**

Stellen Sie sich vor, ein Sicherheitsteam verwendet einen Vulnerability-Scanner und dieser meldet eine Schwachstelle mit der CVE-ID **CVE-2023-12345** und einem **CVSS v3.1 Base Score von 8.5 (High)** mit dem Vektor `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H`.

- **CVE-2023-12345:** Identifiziert die spezifische Schwachstelle eindeutig. Das Sicherheitsteam kann diese CVE-ID verwenden, um detaillierte Informationen über die Schwachstelle zu finden.
- **CVSS Base Score 8.5 (High):** Zeigt an, dass es sich um eine hochriskante Schwachstelle handelt, die priorisiert behoben werden sollte.
- **CVSS Vektor:** Liefert detaillierte Informationen darüber, wie die Bewertung zustande gekommen ist. Das Team kann die Metrikwerte analysieren, um den Kontext des Scores besser zu verstehen (z.B. dass die Angriffskomplexität hoch ist, aber die Auswirkungen auf die Vertraulichkeit, Integrität und Verfügbarkeit ebenfalls hoch sind).

**Zusammenfassend:**

- **CVE** ist das System zur **Identifizierung und Benennung** von Schwachstellen. Es ist das "Namensschild" für jede bekannte Sicherheitslücke.
- **CVSS** ist das System zur **Bewertung des Schweregrads** von Schwachstellen. Es ist die "Risikobewertung", die angibt, wie gefährlich eine Schwachstelle ist.

Gemeinsam bilden CVE und CVSS ein wichtiges Fundament für das Vulnerability Management, die Risikobewertung und die Kommunikation von Sicherheitsinformationen in der IT-Welt. Sie ermöglichen es Sicherheitsteams, effizienter und effektiver auf Sicherheitsbedrohungen zu reagieren.













## Was ist CVE?

05.11.2018 Aktualisiert am 05.12.2024  Von [Dipl.-Ing. (FH) Stefan Luber](https://www.security-insider.de/autor/stefan-luber/1590387/)  3 min Lesedauer  


Bei den Common Vulnerabilities and Exposures (CVE) handelt es sich um eine standardisierte Liste über Schwachstellen und Sicherheitsrisiken von Computersystemen. Dank der eindeutigen Benennung wird der Datenaustausch vereinfacht. Laufende Nummern identifizieren die verschiedenen Einträge eindeutig.

![[f7d43faa83ab1be3abf11e85dbe314a8_MD5.jpg]]sind eine standardisierte Liste von IT-Schwachstellen und Sicherheitslücken.(Bild:  gemeinfrei / Pixabay)")

Die Common Vulnerabilities and Exposures (CVE) sind eine standardisierte Liste von IT-Schwachstellen und Sicherheitslücken.

(Bild: gemeinfrei / Pixabay)

Die Abkürzung [CVE](https://www.security-insider.de/was-ist-cve-a-771921/) steht für Common Vulnerabilities and Exposures. Dabei handelt es sich um einen Standard, der Schwachstellen und Sicherheitsrisiken von Computersystemen eindeutig benennt und in einem allgemein zugänglichen Verzeichnis auflistet. Ziel ist es, den Datenaustausch über Schwachstellen beispielsweise zwischen verschiedenen Herstellern zu vereinfachen und eine eindeutige Identifikation zu ermöglichen. [IPS](https://www.security-insider.de/was-ist-ein-intrusion-prevention-system-ips-a-612859/)- oder [IDS](https://www.security-insider.de/was-ist-ein-intrusion-detection-system-ids-a-612870/)-Systeme können das [CVE-Verzeichnis](https://cve.mitre.org/) in ihrem Vulnerability-Management verwenden.

### Wer gibt CVE heraus?

Grundsätzlich unterscheidet das Verzeichnis zwischen Sicherheitslücken, Schwachstellen und Exposures. Während Sicherheitslücken durch einen Fehler im Code verursacht werden und direkten Zugriff auf ein System ermöglichen, gestattet ein Exposure indirekten Zugang und beispielsweise das Kopieren von Kundendaten oder das unbefugte Erlangen weiterer Rechte. Die CVEs pflegt das sogenannte CVE Editorial Board. Mitglieder sind Vertreter von Sicherheitsorganisationen, akademische Institutionen, Hersteller und Sicherheitsexperten. Moderator im Editorial Board ist die gemeinnützige MITRE Corporation, die von der US-amerikanischen Regierung unterstützt wird. Die MITRE verwaltet auch die Website. Seit 1999 werden CVE-Nummern vergeben.

[

![[942ef2e9ef834777c6850dbb8b74d7c8_MD5.jpg]]")

Common Vulnerabilities and Exposures (CVE)

CVE & Co. für Einsteiger





### Wo findet man den aktuellsten CVE?

Den aktuellen CVE einer bekannten [Schwachstelle](https://www.security-insider.de/was-ist-eine-sicherheitsluecke-a-648842/) findet man im [CVE-Verzeichnis von MITRE](https://cve.mitre.org/cve/search_cve_list.html). DOrt kann man nach direkt nach dem CVE-Namen suchen, sofern dessen ID bekannt ist. Außerdem kann man nach einem oder mehreren Stichworten suchen. Um die Ergebnisse zu optimieren, hat MITRE eine [Liste mit Such-Tipps für CVEs veröffentlicht](https://www.cve.org/ResourcesSupport/FAQs#pc_cve_list_basicssearch_cve).

Für die Suche nach einer aktuellen CVE ist wichtig zu wissen, dass CVE-Namen, auch CVE-IDs oder nur CVEs genannt, nach einer genau definierten Syntax aufgebaut sind. Jeder Name enthält die folgenden Angaben:

- eine eindeutige Identifikationsnummer beispielsweise CVE-1999-0050

- den Status „Entry“ oder „Candidate“

- eine kurze Beschreibung der Sicherheitslücke oder des Exposures

- passende Referenzen

Die Fortlaufenden Identifikationsnummern waren zu Beginn vierstellig mit führenden Nullen. Mittlerweile erlaubt das Format beliebig viele Stellen (mindestens jedoch vier).

CVEs unterscheiden die zwei Stati „Entry“ und „Candidate“ (Eintrag oder Kandidat). Der Entry-Status sagt aus, dass die ID von der Common Vulnerabilities and Exposures Liste akzeptiert ist. Ein Eintrag mit dem Status Candidate steht unter Beobachtung und ist noch nicht offiziell in die Liste aufgenommen. Es wird noch geprüft, ob eine Aufnahme in die Liste erfolgt.

[

![[1f104177e836ea05253c9e4c4269a723_MD5.jpg]]

Common Vulnerabilities and Exposures

Die CVE-Auflistung bekannter Sicherheitslücken



](https://www.security-insider.de/die-cve-auflistung-bekannter-sicherheitsluecken-a-746043/?cflt=rdt)

### Ziele der Common Vulnerabilities and Exposures

Hauptziel der Common Vulnerabilities and Exposures ist es, bekannte Schwachstellen oder Expositionen eindeutig zu benennen, um Administratoren oder Herstellern einen schnellen Zugriff auf Informationen über Bedrohungen zu ermöglichen. Dank der eindeutigen Nummern kann auf weitere CVE-kompatible Informationsquellen schnell zugegriffen werden. Common Vulnerabilities and Exposures erleichtern die Suche in anderen Datenbanken und gestatten einen Austausch von Daten zwischen Herstellern mit ihren verschiedenen Sicherheitstools.

### Bedeutung der CVE-Kompatibilität

Datenbanken, Security-Tools oder Webseiten können CVE-kompatibel sein. Die Kompatibilität sagt aus, dass CVE-IDs korrekt und gemäß der Syntax verwendet werden, um sie mit anderen Informationen zu verknüpfen. So ist sichergestellt, dass sich die kompatiblen Services und Anwendungen untereinander austauschen können. Die vier Mindestanforderungen für die Kompatibilität sind:

- Schwachstellen und zugehörige Informationen sind unter der CVE-ID auffindbar,

- die angebotenen Informationen verwenden CVE-Namen,

- die Dokumentation enthält Beschreibungen zur Kompatibilität und Informationen, wie die bereitgestellten Informationen für andere Dienste oder Produkte nutzbar sind,

- der Eigentümer eines Repositories hat eine exakte Zuordnung zu spezifischen CVE-Versionen sichergestellt.















## Überblick

CVE, kurz für Common Vulnerabilities and Exposures (Häufige Schwachstellen und Risiken), ist eine Liste mit öffentlichen Sicherheitsschwachstellen in Computersystemen. Mit CVE ist eine bestimmte Schwachstelle gemeint, der eine CVE-Nummer zugewiesen ist.

In Sicherheitshinweisen von Anbietern und Forschenden wird fast immer mindestens 1 CVE-Nummer erwähnt. Mithilfe von CVEs können IT-Fachleute solche Schwachstellen leichter priorisieren und beheben, um Computersysteme so sicher wie möglich zu machen.



## Wie funktioniert das CVE-System?

Das von der US-Regierung finanzierte Forschungs- und Entwicklungsunternehmen MITRE Corporation entwickelte 1999 [das CVE-System](https://www.cve.org/), das einen einheitlichen Standard zum Melden und Nachverfolgen von Sicherheitsfehlern in Software darstellt.

CVE-Einträge sind sehr kurz. Sie enthalten keinerlei technische Daten oder Infos zu Risiken, Auswirkungen und Fixes. Diese Details werden in anderen Datenbanken angezeigt, u. a. in der [U.S. National Vulnerability Database (NVD)](https://nvd.nist.gov/), der [CERT/CC Vulnerability Notes Database](https://www.kb.cert.org/vuls/) und in verschiedenen von Anbietern und anderen Organisationen gepflegten Listen.

In diesen verschiedenen Systemen bieten CVE-Nummern den Nutzenden eine zuverlässige Möglichkeit, eindeutige Schwachstellen zu erkennen und die Entwicklung von Sicherheitstools und -lösungen zu koordinieren. Die MITRE Corporation verwaltet die CVE-Liste, aber eine Schwachstelle, die zu einem CVE-Eintrag wird, wird oft von Organisationen und Mitgliedern der Open Source Community gemeldet.

### CVE-Nummern

CVE-Nummern werden von einer [CVE Numbering Authority (CNA)](https://www.cve.org/ProgramOrganization/CNAs) zugewiesen. Es gibt [etwa 100 CNAs](https://cve.mitre.org/cve/request_id.html), darunter Sicherheitsfirmen, Forschungseinrichtungen und wichtige IT-Anbieter wie Red Hat, [IBM](https://www.redhat.com/de/partners/ibm-alliance), [Cisco](https://www.redhat.com/de/partners/cisco-systems), [Oracle](https://partner-finder.oracle.com/catalog/Partner/SC2PP-REDHAT#profile-solutions) und [Microsoft](https://www.redhat.com/de/partners/microsoft). Außerdem können CVE-Nummern direkt von MITRE ausgegeben werden.

Den CNAs werden CVE-Nummernblöcke zugewiesen, die von den CNAs in Reserve gehalten werden, um sie dann bei Bedarf neu entdeckten Schwachstellen zuzuordnen. Jedes Jahr werden Tausende von [CVE-Nummern](https://www.cvedetails.com/browse-by-date.php) vergeben. Ein einzelnes komplexes Produkt wie ein Betriebssystem kann Hunderte von CVE-Nummern enthalten. In 2 Phasen ist ein Betriebssystem besonders anfällig für Schwachstellen: in der End-of-Maintenance-Phase, in der keine Bug Fixes und Sicherheitspatches mehr ausgegeben werden, und der End-of-Life-Phase, in der es keinen Support durch den Erstanbieter mehr gibt. Als CentOS Linux 7 am 1. Juli 2024 die End-of-Life-Phase erreichte, wurde beispielsweise innerhalb eines Tages eine neue CVE bekannt gegeben. Dies zeigt, wie wichtig die Migration zu einem stabilen Betriebssystem ist, das regelmäßige Sicherheitspatches und -updates erhält.

[Migration von CentOS Linux zu Red Hat Enterprise Linux](https://www.redhat.com/de/technologies/linux-platforms/enterprise-linux/centos-migration)

Schwachstellen können von Anbietern, Forschenden oder auch von fachkundigen Nutzenden entdeckt und gemeldet werden. Viele Anbieter vergeben sogenannte [Bug-Prämien](https://en.wikipedia.org/wiki/Bug_bounty_program), um die Offenlegung von Schwachstellen zu fördern. Wenn Sie also eine Schwachstelle in [Open Source-Software](https://www.redhat.com/de/topics/open-source/what-is-open-source-software) finden, sollten Sie diese [der jeweiligen Community melden](https://opensource.com/article/19/3/bug-reporting).

Auf diese Weise finden Infos zu Schwachstellen stets ihren Weg zu einer CNA. Die CNA weist der Information dann eine CVE-Nummer zu. Danach wird der neue CVE-Eintrag auf der [CVE-Website](https://www.cve.org/) veröffentlicht.

Eine CNA weist die CVE-Nummer oft schon zu, bevor der Sicherheitshinweis öffentlich gemacht wird. Anbieter halten Sicherheitsschwachstellen häufig geheim, bis sie entsprechende Fixes entwickelt und getestet haben, um Angriffe zur Ausbeutung nicht gepatchter Schwachstellen zu verhindern.

Sobald CVE-Einträge veröffentlicht wurden, werden ihnen CVE-Nummern (im Format CVE-2019-1234567) sowie eine kurze Beschreibung der Sicherheitsschwachstelle mit Referenzen hinzugefügt, die Links zu Schwachstellenmeldungen und Empfehlungen enthalten können.

## Red Hat Ressourcen



## Welche Kriterien muss eine CVE erfüllen?

Gemäß den [operativen CNA-Regeln](https://www.cve.org/ResourcesSupport/AllResources/CNARules) werden CVE-Nummern Schwachstellen zugewiesen, die folgende Kriterien erfüllen:

- **Sie sind unabhängig behebbar:**  
    Die Schwachstelle kann unabhängig von anderen Bugs behoben werden.
- **Sie wurden vom betroffenen Anbieter bestätigt oder dokumentiert:**  
    Der Software- oder Hardwareanbieter bestätigt, dass die Schwachstelle existiert und die Sicherheit beeinträchtigt. Alternativ muss die meldende Person eine Schwachstellenmeldung geteilt haben, die die negativen Auswirkungen der Schwachstelle demonstriert, _und_ bestätigt haben, dass sie die Sicherheitsrichtlinien des betroffenen Systems verletzt.
- **Sie wirkt sich nur auf 1 Codebase aus:**  
    Wenn eine Schwachstelle sich auf mehr als 1 Produkt auswirkt, wird jedem Produkt eine separate CVE-Nummer zugewiesen. Bei geteilten Libraries, Protokollen oder Standards erhält die Schwachstelle nur dann eine gemeinsame CVE-Nummer, wenn die Verwendung des geteilten Codes in allen Fällen dieselbe Schwachstelle verursacht. Ansonsten erhält jede betroffene Codebase oder jedes Produkt eine separate CVE-Nummer.



## Was ist das Common Vulnerability Scoring System (CVSS)?

Der Schweregrad einer Schwachstelle lässt sich auf vielerlei Weise bestimmen. Eine Möglichkeit ist das [Common Vulnerability Scoring System (CVSS)](https://www.first.org/cvss/), das aus mehreren offenen Standards besteht, mit denen eine Zahl zur Festlegung eines Schweregrads zugewiesen wird. CVSS-Scores werden von der NVD, CERT und anderen verwendet, um die Auswirkungen von Schwachstellen zu beurteilen. Die Punkteskala reicht von 0,0 bis 10,0, wobei der Schweregrad mit der Zahl zunimmt. Viele Sicherheitsanbieter haben außerdem ihr eigenes Punktesystem entwickelt.

### 3 wichtige Schlussfolgerungen

**Prüfen Sie Ihre Bereitstellungen:** Nur, weil ein CVE-Eintrag existiert, heißt das noch lange nicht, dass das damit verbundene Risiko auf Ihre spezifische Umgebung oder Bereitstellung zutrifft. Lesen Sie daher die jeweilige CVE, um sicherzustellen, ob sie (vollständig oder teilweise) für das Betriebssystem sowie die Anwendungen, Module und Konfigurationen Ihrer Umgebung relevant ist.

**Praktizieren Sie Schwachstellenmanagement:** [Schwachstellenmanagement](https://www.redhat.com/de/topics/security/what-is-vulnerability-management) umfasst wiederholbare Prozesse zur Identifizierung, Klassifizierung, Priorisierung, Behebung und Minderung von Schwachstellen. Es bedeutet, dass Sie wissen müssen, wie sich ein bestimmtes Risiko auf Ihre Organisation auswirkt, damit Sie ungeklärte Schwachstellen entsprechend priorisieren und beheben können.

**Zeigen Sie Kommunikationsbereitschaft:**CVEs haben Auswirkungen auf die Systeme Ihrer Organisation, und zwar einerseits wegen der Schwachstellen selbst und andererseits wegen der Ausfallzeiten, die für ihre Behebung anfallen. Kommunizieren und koordinieren Sie dies mit Ihren internen Kunden, und teilen Sie Ihrer Organisation die Schwachstellen samt den zentralen Risikomanagementprozessen mit.

### Wie Red Hat mit CVEs arbeitet

Red Hat leistet sehr viele Beiträge zu [Open Source](https://www.redhat.com/de/topics/open-source/what-is-open-source)-Software und engagiert sich daher fortlaufend in der Sicherheits-Community. Red Hat ist selbst eine CNA und verwendet zur Überwachung von Sicherheitsschwachstellen CVE-Nummern. Red Hat Product Security unterhält eine offene und regelmäßig aktualisierte Datenbank mit Sicherheitsupdates, die Sie nach CVE-Nummer anzeigen können.

[Zur Red Hat CVE-Datenbank](https://access.redhat.com/security/security-updates/#/cve)

## Was ist die Red Hat Security Data API?

Red Hat Product Security bietet Zugriff auf Sicherheitsrohdaten im [Red Hat Customer Portal](https://www.redhat.com/security/data/metrics/) und in einem maschinenlesbaren Format mit der Security Data API (Application Programming Interface).

Zusätzlich zu den Sicherheitsberichten und Metriken, die Red Hat erstellt, können Kunden diese Rohdaten verwenden, um ihre eigenen Metriken für ihre besonderen Situationen zu erstellen.

Die von der Security Data API bereitgestellten Daten umfassen OVAL-Definitionen (Open Vulnerability and Assessment Language), CVRF-Dokumente (Common Vulnerability Reporting Framework) und CVE-Daten. Die Daten sind im XML- oder JSON-Format verfügbar.