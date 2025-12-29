# Tägliche Ausgaben

## 1. Zweck

Das Modul **Tägliche Ausgaben** hilft Ihnen bei der Erfassung regelmäßiger, nicht fester Ausgaben wie:
- Essen & Restaurants
- Einkaufen
- Transport
- Unterhaltung
- Andere flexible Ausgaben

Im Gegensatz zu **Wiederkehrenden Ausgaben** variieren tägliche Ausgaben oft in Betrag und Häufigkeit, ohne festen Zyklus.

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie möchten:
- Zufällige, nicht wiederkehrende Ausgaben erfassen
- Tägliche Ausgaben verfolgen, um Budget zu kontrollieren
- Ausgabentrends nach Kategorie analysieren
- Gesamtausgaben in einem Zeitraum anzeigen

## 3. Verwandte Bildschirme

- Liste tägliche Ausgaben
- Neue Ausgabe hinzufügen
- Ausgabe bearbeiten

## 4. Hauptverwendung

### 4.1 Tägliche Ausgabe hinzufügen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Tägliche Ausgaben**
2. Tippen Sie auf die **+** (FAB) Schaltfläche unten rechts
3. Füllen Sie Informationen aus:
   - **Kategorie**: Wählen Sie Kategorie (oder verwenden Sie Standardkategorie, falls konfiguriert)
   - **Betrag**: Geben Sie ausgegebenen Betrag ein
   - **Datum**: Wählen Sie Ausgabedatum (Standard ist heute)
   - **Notiz**: Detaillierte Beschreibung (optional)
4. Tippen Sie auf **Speichern**

### 4.2 Ausgabenliste anzeigen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Tägliche Ausgaben**
2. Liste wird gemäß Ihrer konfigurierten Anordnung angezeigt (2, 3 oder 4 Spalten)
3. Verwenden Sie **Suche**, um nach Kategorie oder Notiz zu filtern
4. Wählen Sie **Zeitfilter**: Heute / Diese Woche / Dieser Monat / Letzter Monat / Benutzerdefiniert

### 4.3 Ausgabe bearbeiten

1. Gehen Sie zur Liste tägliche Ausgaben
2. Lang drücken auf Element zum Bearbeiten
3. Wählen Sie **Bearbeiten** aus dem Menü
4. Aktualisieren Sie Informationen
5. Tippen Sie auf **Speichern**

### 4.4 Ausgabe löschen

1. Gehen Sie zur Liste tägliche Ausgaben
2. Lang drücken auf Element zum Löschen
3. Wählen Sie **Löschen** aus dem Menü
4. Löschung bestätigen

### 4.5 Standardkategorie festlegen

1. Gehen Sie zu **Einstellungen** → **Kategorien** → **Kategorien tägliche Ausgaben**
2. Tippen Sie auf Kategorie, die Sie als Standard festlegen möchten
3. Wählen Sie **Als Standard festlegen**
4. Beim Hinzufügen neuer Ausgabe wird diese Kategorie automatisch ausgewählt

## 5. UI-Illustrationen (Wireframe)

### 5.1 Listenscreen

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Tägliche Ausgaben               │
├─────────────────────────────────────────┤
│  [🔍 Suchen...]                         │
│  [Heute ▼] [Diese Woche] [Dieser Monat]    │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Essen│ │Einka│ │ Taxi │            │
│  │ aus  │ │ufen │ │      │            │
│  │      │ │      │ │      │            │
│  │ €1.80│ │ €7.20│ │ €0.90│            │
│  │      │ │      │ │      │            │
│  │ 15/11│ │ 15/11│ │ 14/11│            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Kaff│ │ Ande│ │      │            │
│  │ ee  │ │ res │ │      │            │
│  │      │ │      │ │      │            │
│  │ €0.90│ │ €3.60│ │      │            │
│  │      │ │      │ │      │            │
│  │ 13/11│ │ 12/11│ │      │            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  Gesamt: €14.40                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Hinzufügen/Bearbeiten Screen

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Tägliche Ausgabe hinzufügen            │
├─────────────────────────────────────────┤
│  Kategorie *                              │
│  [Essen aus ▼]                            │
│                                         │
│  Betrag *                                │
│  [€1.80]                                   │
│                                         │
│  Datum *                                  │
│  [15/11/2024]                           │
│                                         │
│  Notiz                                    │
│  [Mittagessen mit Freund]                     │
│                                         │
│  [Speichern] [Abbrechen]                        │
└─────────────────────────────────────────┘
```

### 5.3 Menü (Lang drücken)

```text
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐ │
│  │ Essen aus                            │ │
│  │ €1.80                                  │ │
│  │ 15/11/2024                          │
│  │                                     │
│  │ [Bearbeiten] [Löschen]                    │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logik & Regeln

### 6.1 Anzeigeanordnung

- Sie können Anzahl der Spalten konfigurieren: 2, 3 oder 4 Spalten
- Anordnung wird in Einstellungen gespeichert und gilt für alle Ausgabenlisten

### 6.2 Zeitfilter

- **Heute**: Zeigt nur Ausgaben von heute
- **Diese Woche**: Vom Wochenanfang bis heute
- **Dieser Monat**: Vom Monatsanfang bis heute
- **Letzter Monat**: Gesamter vorheriger Monat
- **Benutzerdefiniert**: Benutzerdefinierten Zeitraum auswählen

### 6.3 Suche

- Suche in **Kategoriename** und **Notiz**
- Groß-/Kleinschreibung nicht beachtend
- Echtzeit-Suche während der Eingabe

### 6.4 Standardkategorie

- Wenn Sie eine Standardkategorie festgelegt haben, wird beim Öffnen des Hinzufügen-Bildschirms diese Kategorie automatisch ausgewählt
- Notiz kann auch basierend auf Kategorie automatisch ausgefüllt werden (falls konfiguriert)

### 6.5 Gesamtausgaben

- Gesamtausgaben werden basierend auf dem aktuell ausgewählten Zeitfilter berechnet
- Wird am Ende der Liste angezeigt

## 7. Wichtige Hinweise

- **Kein Zyklus**: Tägliche Ausgaben haben keinen automatischen Zyklus, Sie müssen jedes Mal manuell eingeben
- **Kann gelöscht werden**: Sie können jede Ausgabe löschen (im Gegensatz zu wiederkehrenden Ausgaben)
- **Keine Budget-Integration**: Tägliche Ausgaben werden nicht automatisch in Budget berechnet (Sie müssen selbst verfolgen)
- **Benutzerdefinierte Kategorien**: Sie können neue Kategorien in Einstellungen erstellen

