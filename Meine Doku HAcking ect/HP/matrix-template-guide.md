# Matrix Template - Cyberpunk Design System

> **Template-Referenz für KI-Prompts und Entwicklungsprojekte**

## 🎯 Template-Übersicht

Das **Matrix Template** ist ein vollständiges, responsives Cyberpunk-Design-System mit Neon-Grün-Ästhetik, das sich ideal für Tech-, Security- und Gaming-Websites eignet.

### 📦 Template-Komponenten

```
matrix-template/
├── matrix-template.html     (Haupt-HTML-Struktur)
├── matrix-template.css      (Design-System + Matrix-Theme)
└── matrix-template.js       (Interaktivität + Navigation)
```

---

## 🎨 Design-System Kernmerkmale

### Farbpalette
```css
:root {
  /* Matrix Colors */
  --color-matrix-green: #39FF14;
  --color-matrix-dark-green: #00FF00;
  --color-matrix-bg: #000000;
  --color-matrix-bg-secondary: #0A0A0A;
  --color-matrix-bg-tertiary: #001100;
  --color-matrix-border: #003300;
  --color-matrix-glow: rgba(57, 255, 20, 0.3);
}
```

### Typografie
```css
/* Fonts */
--matrix-font-main: 'Share Tech Mono', monospace;
--matrix-font-title: 'Orbitron', sans-serif;

/* Font Sizes */
--font-size-xs: 11px;
--font-size-sm: 12px;
--font-size-base: 14px;
--font-size-lg: 16px;
--font-size-xl: 18px;
--font-size-2xl: 20px;
--font-size-3xl: 24px;
--font-size-4xl: 30px;
```

### Spacing-System
```css
/* Spacing Tokens */
--space-4: 4px;
--space-8: 8px;
--space-12: 12px;
--space-16: 16px;
--space-20: 20px;
--space-24: 24px;
--space-32: 32px;
```

---

## 🏗️ HTML-Struktur-Template

### Basis-Layout
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matrix Template - Cyberpunk Design</title>
    <link rel="stylesheet" href="matrix-template.css">
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono:wght@400&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Legal Warning (optional) -->
    <div class="legal-warning" id="legalWarning">
        <div class="container">
            ⚠️ <strong>WARNUNG:</strong> Nur für autorisierte Nutzung.
            <button class="legal-close" onclick="dismissLegalWarning()">✕</button>
        </div>
    </div>

    <div class="content-wrapper">
        <!-- Header -->
        <header class="header">
            <div class="container">
                <div class="header__content">
                    <h1 class="header__title">
                        <span class="matrix-effect">PROJEKT-NAME</span>
                        <span class="version">v1.0</span>
                    </h1>
                    <div class="header__controls">
                        <button class="btn btn--sm" id="searchBtn">
                            🔍 Search <span class="shortcut">Ctrl+K</span>
                        </button>
                        <button class="btn btn--sm btn--secondary" id="themeToggle">
                            🌙 Theme
                        </button>
                    </div>
                </div>
            </div>
        </header>

        <!-- Navigation -->
        <nav class="nav">
            <div class="container">
                <div class="tab-nav">
                    <button class="tab-link active" data-tab="home">🏠 Home</button>
                    <button class="tab-link" data-tab="features">⚡ Features</button>
                    <button class="tab-link" data-tab="docs">📚 Docs</button>
                    <!-- Weitere Tabs nach Bedarf -->
                </div>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="main">
            <div class="container">
                <!-- Tab Contents -->
                <section id="home" class="tab-content active">
                    <div class="card">
                        <div class="card__body">
                            <h2>Titel</h2>
                            <p>Beschreibung...</p>
                        </div>
                    </div>
                </section>
            </div>
        </main>
    </div>

    <script src="matrix-template.js"></script>
</body>
</html>
```

---

## 🧩 Wiederverwendbare Komponenten

### 1. Card-Komponente
```html
<div class="card">
    <div class="card__body">
        <h2>Titel</h2>
        <p>Inhalt...</p>
    </div>
</div>
```

### 2. Button-Varianten
```html
<button class="btn btn--primary">Primary</button>
<button class="btn btn--secondary">Secondary</button>
<button class="btn btn--sm">Small</button>
<button class="btn btn--outline">Outline</button>
```

### 3. Status-Indikatoren
```html
<div class="status status--success">✅ Erfolgreich!</div>
<div class="status status--warning">⚠️ Warnung!</div>
<div class="status status--error">❌ Fehler!</div>
<div class="status status--info">ℹ️ Information!</div>
```

### 4. Code-Block mit Copy-Button
```html
<div class="code-block">
    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
    <pre><code>// Dein Code hier
console.log('Hello Matrix!');</code></pre>
</div>
```

### 5. Grid-Layouts
```html
<!-- 3-Spalten Grid -->
<div class="architecture-grid">
    <div class="arch-component">
        <h4>Feature 1</h4>
        <p>Beschreibung...</p>
    </div>
    <div class="arch-component">
        <h4>Feature 2</h4>
        <p>Beschreibung...</p>
    </div>
    <div class="arch-component">
        <h4>Feature 3</h4>
        <p>Beschreibung...</p>
    </div>
</div>

<!-- Timeline-Layout -->
<div class="timeline">
    <div class="timeline-item">
        <div class="timeline-year">2024</div>
        <div class="timeline-content">
            <h4>Event-Titel</h4>
            <p>Beschreibung...</p>
        </div>
    </div>
</div>
```

---

## ⚙️ JavaScript Funktionalität

### Kern-Funktionen
```javascript
// Tab-Navigation
switchToTab(tabId)

// Theme-Toggle (Dark/Light)
toggleTheme()

// Search-Overlay
openSearch()
closeSearch()

// Code-Kopieren
copyCode(button)

// Legal Warning dismissal
dismissLegalWarning()
```

### Keyboard Shortcuts
- **Ctrl+K / ⌘+K**: Suche öffnen
- **Esc**: Suche schließen
- **Tab**: Navigation zwischen Elementen

---

## 🎯 Template-Anpassungen

### Farb-Themes ändern
```css
:root {
  /* Orange Matrix Theme */
  --color-matrix-green: #FF6B35;
  --color-matrix-dark-green: #FF8C42;
  
  /* Blue Cyber Theme */
  --color-matrix-green: #00BFFF;
  --color-matrix-dark-green: #1E90FF;
  
  /* Purple Neon Theme */
  --color-matrix-green: #9D00FF;
  --color-matrix-dark-green: #B533FF;
}
```

### Container-Breite anpassen
```css
.container {
  max-width: 1400px; /* Standard: 1200px */
}
```

### Neue Tab hinzufügen
1. **HTML**: Button in `.tab-nav` hinzufügen
2. **HTML**: `<section>` mit entsprechender ID erstellen
3. **JS**: Tab-ID zu TABS-Array hinzufügen (falls validation vorhanden)

---

## 🚀 Prompt-Template für KI

### Für neue Projekte verwenden:

```
Erstelle eine Website mit dem Matrix Template Design-System:

**Design-Vorgaben:**
- Verwende das Matrix-Cyberpunk-Theme mit Neon-Grün (#39FF14)
- Nutze 'Share Tech Mono' für Code/Mono-Text und 'Orbitron' für Titel
- Implementiere das Card-basierte Layout-System
- Baue Tab-Navigation mit folgenden Tabs: [TABS HIER EINFÜGEN]

**Technische Requirements:**
- Responsive Design mit Container-System
- Dark/Light Mode Toggle
- Search-Overlay mit Ctrl+K Shortcut
- Status-Komponenten für Feedback
- Code-Blöcke mit Copy-Funktionalität

**Content-Struktur:**
[HIER PROJEKT-SPEZIFISCHE ANFORDERUNGEN EINFÜGEN]

**Basis-Template:**
Verwende die HTML-Struktur und CSS-Klassen aus dem Matrix Template als Grundlage.
```

---

## 📋 Template-Checkliste

### ✅ Vor der Implementierung:
- [ ] Projekt-spezifische Farben definiert?
- [ ] Benötigte Tabs geplant?
- [ ] Content-Struktur erstellt?
- [ ] Responsive Breakpoints berücksichtigt?

### ✅ Nach der Implementierung:
- [ ] Alle Links funktional?
- [ ] Tab-Navigation arbeitet korrekt?
- [ ] Search-Funktionalität getestet?
- [ ] Theme-Toggle funktioniert?
- [ ] Mobile Ansicht überprüft?
- [ ] Accessibility Standards erfüllt?

---

## 🎨 CSS-Klassen Referenz

### Layout
- `.container` - Haupt-Container (max-width + padding)
- `.content-wrapper` - Wrapper für Legal-Banner-Offset
- `.header`, `.nav`, `.main`, `.footer` - Haupt-Sektionen

### Navigation
- `.tab-nav` - Tab-Container
- `.tab-link` - Tab-Buttons
- `.tab-content` - Tab-Inhalte (mit `.active` State)

### Komponenten
- `.card` + `.card__body` - Content-Container
- `.btn` + Modifier (`.btn--primary`, `.btn--sm`, etc.)
- `.status` + Modifier (`.status--success`, etc.)
- `.code-block` - Code-Container mit Copy-Button

### Grid-Layouts
- `.architecture-grid` - 3-Spalten responsive Grid
- `.requirements-grid` - 2-4 Spalten Grid
- `.timeline` - Vertikales Timeline-Layout
- `.ethical-guidelines` - Multi-column Guidelines

### Utilities
- `.matrix-effect` - Animierter Gradient-Text
- `.version` - Version-Badge Styling
- `.shortcut` - Keyboard-Shortcut Styling

---

## 🔧 Entwickler-Notizen

### Performance-Optimierungen
- CSS-Variablen für konsistente Theming
- Minimal JavaScript (Vanilla JS, ~20KB)
- Effiziente CSS-Selektoren
- Lazy-Loading für große Inhalte

### Browser-Kompatibilität
- Chrome/Edge: ✅ Vollständig
- Firefox: ✅ Vollständig
- Safari: ✅ Vollständig
- IE11: ❌ Nicht unterstützt (CSS Custom Properties)

### Accessibility Features
- ARIA-Labels für Screen Reader
- Keyboard-Navigation unterstützt
- Focus-Visible Styling
- High-Contrast Mode Support

---

## 📄 Lizenz & Credits

**Template:** Matrix Cyberpunk Design System  
**Erstellt:** 2025  
**Lizenz:** [HIER LIZENZ EINFÜGEN]  
**Dependencies:** Google Fonts (Share Tech Mono, Orbitron)

---

*Dieses Template wurde für maximale Wiederverwendbarkeit entwickelt. Passe Farben, Content und Layout nach den spezifischen Projektanforderungen an.*