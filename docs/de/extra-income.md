# Zusatzeinkommen

## 1. Zweck

Das Modul **Zusatzeinkommen** hilft Ihnen bei der Erfassung nicht wiederkehrenden Einkommens ohne festen Zyklus wie:
- Online-Verkäufe
- Freelance
- Boni
- Bargeldgeschenke
- Anderes unregelmäßiges Einkommen

Im Gegensatz zu **Wiederkehrendem Einkommen** hat Zusatzeinkommen keinen automatischen Zyklus, Sie müssen jedes Mal manuell eingeben.

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie möchten:
- Zufälliges, nicht wiederkehrendes Einkommen erfassen
- Gesamteinkommen in einem Zeitraum verfolgen
- Zusatzeinkommen-Trends analysieren
- In monatliches Budget berechnen

## 3. Verwandte Bildschirme

- Liste Zusatzeinkommen
- Neues Einkommen hinzufügen
- Einkommen bearbeiten

## 4. Hauptverwendung

### 4.1 Zusatzeinkommen hinzufügen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Zusatzeinkommen**
2. Tippen Sie auf die **+** (FAB) Schaltfläche unten rechts
3. Füllen Sie Informationen aus:
   - **Kategorie**: Wählen Sie Kategorie aus oder erstellen Sie neue
   - **Betrag**: Geben Sie erhaltenen Betrag ein
   - **Datum**: Wählen Sie Datum, an dem Geld erhalten wurde (Standard ist heute)
   - **Notiz**: Detaillierte Beschreibung (optional)
4. Tippen Sie auf **Speichern**

### 4.2 Einkommensliste anzeigen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Zusatzeinkommen**
2. Liste wird gemäß Ihrer konfigurierten Anordnung angezeigt (1, 2, 3 oder 4 Spalten)
3. Verwenden Sie **Suche**, um nach Kategorie oder Notiz zu filtern
4. Wählen Sie **Zeitfilter**: Heute / Diese Woche / Dieser Monat / Letzter Monat / Benutzerdefiniert

### 4.3 Einkommen bearbeiten

1. Gehen Sie zur Liste Zusatzeinkommen
2. Lang drücken auf Element zum Bearbeiten
3. Wählen Sie **Bearbeiten** aus dem Menü
4. Aktualisieren Sie Informationen
5. Tippen Sie auf **Speichern**

### 4.4 Einkommen löschen

1. Gehen Sie zur Liste Zusatzeinkommen
2. Lang drücken auf Element zum Löschen
3. Wählen Sie **Löschen** aus dem Menü
4. Löschung bestätigen

## 5. UI-Illustrationen (Wireframe)

### 5.1 Listenscreen

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Zusatzeinkommen                 │
├─────────────────────────────────────────┤
│  [🔍 Suchen...]                         │
│  [Dieser Monat ▼] [Diese Woche] [Heute]     │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Online-Verkäufe                        │ │
│  │ €18                                 │ │
│  │ 15/11/2024                          │ │
│  │                                    │ │
│  │ [Bearbeiten] [Löschen]                    │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Freelance                           │ │
│  │ €36                                 │ │
│  │ 14/11/2024                          │ │
│  │                                    │ │
│  │ [Bearbeiten] [Löschen]                    │
│  └───────────────────────────────────┘ │
│                                         │
│  Gesamt: €54                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Hinzufügen/Bearbeiten Screen

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Zusatzeinkommen hinzufügen             │
├─────────────────────────────────────────┤
│  Kategorie *                              │
│  [Online-Verkäufe ▼]                        │
│                                         │
│  Betrag *                                │
│  [€18]                                  │
│                                         │
│  Datum *                                  │
│  [15/11/2024]                           │
│                                         │
│  Notiz                                    │
│  [Produkt A verkauft]                        │
│                                         │
│  [Speichern] [Abbrechen]                        │
└─────────────────────────────────────────┘
```

## 6. Logik & Regeln

### 6.1 Anzeigeanordnung

- Sie können Anzahl der Spalten konfigurieren: 1, 2, 3 oder 4 Spalten
- Anordnung wird in Einstellungen gespeichert und gilt für alle Zusatzeinkommen-Listen

### 6.2 Zeitfilter

- **Heute**: Zeigt nur Einkommen von heute
- **Diese Woche**: Vom Wochenanfang bis heute
- **Dieser Monat**: Vom Monatsanfang bis heute
- **Letzter Monat**: Gesamter vorheriger Monat
- **Benutzerdefiniert**: Benutzerdefinierten Zeitraum auswählen

### 6.3 Suche

- Suche in **Kategoriename** und **Notiz**
- Groß-/Kleinschreibung nicht beachtend
- Echtzeit-Suche während der Eingabe

### 6.4 Budget-Integration

- Zusatzeinkommen wird in "Zusatzeinkommen" im Budget berechnet
- Hilft Ihnen, gesamtes monatliches Einkommen zu verfolgen

## 7. Wichtige Hinweise

- **Kein Zyklus**: Zusatzeinkommen hat keinen automatischen Zyklus, Sie müssen jedes Mal manuell eingeben
- **Kann gelöscht werden**: Sie können jedes Einkommen löschen
- **Budget-Integration**: Zusatzeinkommen wird automatisch in Budget des aktuellen Monats berechnet

