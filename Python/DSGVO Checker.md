#!/usr/bin/env python3
"""
DSGVO-Checker: Ein Tool zur Überprüfung der DSGVO-Konformität von Programmierprojekten
"""

import os
import re
import sys
import json
import argparse
from typing import Dict, List, Tuple, Any, Set

class DSGVOChecker:
    """DSGVO-Konformitätsprüfer für Programmierprojekte"""
    
    def __init__(self):
        # Definition der problematischen Muster
        self.patterns = {
            "persönliche_daten": [
                r"(?:name|vorname|nachname|email|e-mail|telefon|handy|geburtsdatum|adresse|plz|postleitzahl)",
                r"(?:personalausweis|steuer(?:nummer|id)|sozialversicherung)",
                r"(?:iban|bic|kreditkarte|konto(?:nummer|daten))",
            ],
            "ohne_einwilligung": [
                r"(?:automatic_tracking|auto_track|autotrack)",
                r"(?:silent_login|auto_login|remember_user)",
                r"(?:default_opt_in|opt_out)"
            ],
            "unverschlüsselt": [
                r"(?:http[^s]|plaintext|unencrypted|cleartext)",
                r"(?:md5\(|sha1\()"
            ],
            "externe_dienste": [
                r"(?:google\s*analytics|gtag|ga\(|fbq\(|facebook\s*pixel)",
                r"(?:amazon\s*analytics|hotjar|segment|mixpanel|matomo)",
                r"(?:cdn\.example\.com|api\.external-service\.com)"
            ],
            "cookies": [
                r"(?:document\.cookie|set-cookie|setcookie)",
                r"(?:localStorage\.|sessionStorage\.)",
                r"(?:first_party_cookies|third_party_cookies)"
            ]
        }
        
        # DSGVO-Anforderungen und Empfehlungen
        self.recommendations = {
            "persönliche_daten": [
                "Sammle nur notwendige personenbezogene Daten (Datensparsamkeit)",
                "Implementiere eine klare Datenschutzerklärung",
                "Stelle sicher, dass Nutzer der Datenverarbeitung zustimmen können",
                "Implementiere Funktionen zum Exportieren und Löschen von Nutzerdaten"
            ],
            "ohne_einwilligung": [
                "Implementiere ein explizites Einwilligungs-System vor dem Sammeln von Daten",
                "Nutze 'Opt-in' statt 'Opt-out' als Standard",
                "Biete detaillierte Informationen darüber, welche Daten warum gesammelt werden"
            ],
            "unverschlüsselt": [
                "Verwende HTTPS für alle Verbindungen",
                "Implementiere moderne Verschlüsselung für sensible Daten (z.B. bcrypt für Passwörter)",
                "Vermeide veraltete Verschlüsselungsmethoden wie MD5 oder SHA1"
            ],
            "externe_dienste": [
                "Stelle sicher, dass alle externen Dienste DSGVO-konform sind",
                "Implementiere einen Cookie-Banner mit detaillierten Informationen",
                "Lade externe Dienste erst nach Einwilligung des Nutzers"
            ],
            "cookies": [
                "Unterscheide zwischen notwendigen und optionalen Cookies",
                "Gib dem Nutzer die Möglichkeit, einzelne Cookie-Typen abzulehnen",
                "Setze angemessene Ablauffristen für Cookies"
            ]
        }

    def check_file(self, file_path: str) -> Dict[str, List[Tuple[int, str]]]:
        """Überprüft eine einzelne Datei auf DSGVO-Probleme"""
        results = {category: [] for category in self.patterns}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    for category, patterns in self.patterns.items():
                        for pattern in patterns:
                            matches = re.finditer(pattern, line.lower())
                            for match in matches:
                                results[category].append((line_num, line.strip()))
        except Exception as e:
            print(f"Fehler beim Lesen der Datei {file_path}: {e}")
        
        return results

    def check_directory(self, directory: str, file_extensions: Set[str]) -> Dict[str, Dict[str, List[Tuple[int, str]]]]:
        """Überprüft ein Verzeichnis rekursiv auf DSGVO-Probleme"""
        results = {}
        
        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in file_extensions):
                    file_path = os.path.join(root, file)
                    file_results = self.check_file(file_path)
                    
                    # Nur Dateien mit Ergebnissen aufnehmen
                    if any(findings for findings in file_results.values()):
                        results[file_path] = file_results
        
        return results

    def check_codepen_html(self, html_content: str) -> Dict[str, List[Tuple[int, str]]]:
        """Überprüft CodePen HTML-Inhalt auf DSGVO-Probleme"""
        results = {category: [] for category in self.patterns}
        
        lines = html_content.split('\n')
        for line_num, line in enumerate(lines, 1):
            for category, patterns in self.patterns.items():
                for pattern in patterns:
                    matches = re.finditer(pattern, line.lower())
                    for match in matches:
                        results[category].append((line_num, line.strip()))
        
        return results

    def generate_report(self, results: Dict[str, Dict[str, List[Tuple[int, str]]]], detailed: bool = False) -> str:
        """Generiert einen Bericht basierend auf den Prüfergebnissen"""
        report = []
        report.append("=" * 80)
        report.append("DSGVO-CHECKER BERICHT")
        report.append("=" * 80)
        
        if not results:
            report.append("Keine potenziellen DSGVO-Probleme gefunden.")
            return "\n".join(report)
        
        total_issues = sum(
            len(issues)
            for file_results in results.values()
            for category_issues in file_results.values()
            for issues in [category_issues]
        )
        
        report.append(f"Gefundene potenzielle Probleme: {total_issues}")
        report.append("")
        
        # Zusammenfassung der Kategorien
        category_counts = {category: 0 for category in self.patterns}
        for file_results in results.values():
            for category, issues in file_results.items():
                category_counts[category] += len(issues)
        
        report.append("ZUSAMMENFASSUNG DER PROBLEME:")
        report.append("-" * 40)
        for category, count in category_counts.items():
            if count > 0:
                report.append(f"{category.replace('_', ' ').capitalize()}: {count} Vorkommen")
        
        report.append("")
        report.append("DETAILLIERTE ERGEBNISSE:")
        report.append("=" * 80)
        
        # Detaillierte Ergebnisse nach Dateien
        for file_path, file_results in results.items():
            has_issues = any(len(issues) > 0 for issues in file_results.values())
            if has_issues:
                report.append(f"\nDatei: {file_path}")
                report.append("-" * 80)
                
                for category, issues in file_results.items():
                    if issues:
                        report.append(f"\n  Kategorie: {category.replace('_', ' ').capitalize()}")
                        
                        if detailed:
                            for line_num, line in issues:
                                report.append(f"    Zeile {line_num}: {line}")
                        else:
                            report.append(f"    {len(issues)} Vorkommen gefunden")
                        
                        # Empfehlungen hinzufügen
                        report.append("\n    Empfehlungen:")
                        for rec in self.recommendations[category]:
                            report.append(f"      - {rec}")
        
        report.append("\n" + "=" * 80)
        report.append("ALLGEMEINE DSGVO-EMPFEHLUNGEN:")
        report.append("-" * 80)
        report.append("1. Führe eine Datenschutz-Folgenabschätzung für dein Projekt durch")
        report.append("2. Dokumentiere alle Datenverarbeitungsprozesse")
        report.append("3. Implementiere technische und organisatorische Maßnahmen zum Datenschutz")
        report.append("4. Stelle sicher, dass Nutzer ihre Rechte ausüben können (Auskunft, Löschung, etc.)")
        report.append("5. Achte auf angemessene Aufbewahrungsfristen für personenbezogene Daten")
        
        return "\n".join(report)

def parse_arguments():
    """Verarbeitet Kommandozeilenargumente"""
    parser = argparse.ArgumentParser(description='DSGVO-Checker für Programmierprojekte')
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help='Zu überprüfende Datei')
    group.add_argument('-d', '--directory', help='Zu überprüfendes Verzeichnis')
    group.add_argument('-c', '--codepen', help='CodePen HTML zum Überprüfen')
    
    parser.add_argument('-e', '--extensions', default='.js,.html,.css,.py,.php,.jsx,.ts,.tsx',
                        help='Komma-getrennte Liste von Dateierweiterungen (Standard: .js,.html,.css,.py,.php,.jsx,.ts,.tsx)')
    parser.add_argument('--detailed', action='store_true', help='Detaillierte Ausgabe mit Codezeilen')
    parser.add_argument('-o', '--output', help='Ausgabedatei für den Bericht (Standard: Konsolenausgabe)')
    
    return parser.parse_args()

def main():
    """Hauptfunktion des DSGVO-Checkers"""
    args = parse_arguments()
    checker = DSGVOChecker()
    results = {}
    
    # Dateitypen für die Überprüfung
    file_extensions = set(args.extensions.split(','))
    
    if args.file:
        if os.path.isfile(args.file):
            file_results = checker.check_file(args.file)
            if any(findings for findings in file_results.values()):
                results[args.file] = file_results
        else:
            print(f"Fehler: Die Datei '{args.file}' existiert nicht.")
            sys.exit(1)
    
    elif args.directory:
        if os.path.isdir(args.directory):
            results = checker.check_directory(args.directory, file_extensions)
        else:
            print(f"Fehler: Das Verzeichnis '{args.directory}' existiert nicht.")
            sys.exit(1)
    
    elif args.codepen:
        # Entweder eine CodePen HTML-Datei oder ein HTML-String
        if os.path.isfile(args.codepen):
            try:
                with open(args.codepen, 'r', encoding='utf-8') as file:
                    html_content = file.read()
            except Exception as e:
                print(f"Fehler beim Lesen der CodePen-Datei: {e}")
                sys.exit(1)
        else:
            html_content = args.codepen
        
        codepen_results = checker.check_codepen_html(html_content)
        if any(findings for findings in codepen_results.values()):
            results["CodePen HTML"] = codepen_results
    
    # Report generieren
    report = checker.generate_report(results, args.detailed)
    
    # Ausgabe des Reports
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(report)
            print(f"Bericht wurde in '{args.output}' gespeichert.")
        except Exception as e:
            print(f"Fehler beim Schreiben der Ausgabedatei: {e}")
            print(report)
    else:
        print(report)

if __name__ == "__main__":
    main()