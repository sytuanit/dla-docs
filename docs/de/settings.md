# Einstellungen

## 1. Zweck

Das Modul **Einstellungen** ermöglicht es Ihnen, die App nach Ihren persönlichen Bedürfnissen zu konfigurieren, einschließlich:
- Sprache und Währung
- Benachrichtigungen
- Kategorien
- Sicherung und Wiederherstellung von Daten
- Sicherheit (Passwort, Face ID)

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie möchten:
- Sprache oder Währung ändern
- Benachrichtigungen aktivieren/deaktivieren
- Kategorien verwalten (hinzufügen, bearbeiten, löschen, als Standard festlegen)
- Daten sichern oder wiederherstellen
- Passwort ändern oder Face ID aktivieren

## 3. Verwandte Bildschirme

- Haupt-Einstellungsbildschirm
- Grundeinstellungen
- Sprache auswählen
- Währung auswählen
- Kategorien verwalten
- Daten sichern
- Daten wiederherstellen
- Passwort ändern
- Face ID / Fingerabdruck aktivieren

## 4. Hauptverwendung

### 4.1 Sprache ändern

1. Gehen Sie zu **Einstellungen** → **Anzeige & Sprache** → **Sprache**
2. Wählen Sie gewünschte Sprache
3. App lädt automatisch mit neuer Sprache neu

### 4.2 Währung ändern

1. Gehen Sie zu **Einstellungen** → **Anzeige & Sprache** → **Währung**
2. Wählen Sie Währungstyp
3. Alle Beträge werden in der neuen Einheit angezeigt

### 4.3 Benachrichtigungen aktivieren/deaktivieren

1. Gehen Sie zu **Einstellungen** → **Benachrichtigungen**
2. Schalten Sie **Benachrichtigungen** Schalter um
3. Wenn aktiviert, erhalten Sie Erinnerungen über:
   - Fälliges wiederkehrendes Einkommen
   - Fällige wiederkehrende Ausgaben
   - Fällige Sparkonten
   - Bevorstehende besondere Anlässe

### 4.4 Kategorien verwalten

1. Gehen Sie zu **Einstellungen** → **Kategorien**
2. Wählen Sie Kategorietyp zum Verwalten:
   - Wiederkehrendes Einkommen
   - Zusatzeinkommen
   - Wiederkehrende Ausgaben
   - Tägliche Ausgaben
3. Kategorien hinzufügen/bearbeiten/löschen
4. Standardkategorie festlegen (für tägliche Ausgaben)

### 4.5 Daten sichern

1. Gehen Sie zu **Einstellungen** → **Sicherung & Daten** → **Sicherung**
2. Wählen Sie Speicherort (Dateisystem)
3. Tippen Sie auf **Sichern**
4. Sicherungsdatei wird erstellt

### 4.6 Daten wiederherstellen

1. Gehen Sie zu **Einstellungen** → **Sicherung & Daten** → **Wiederherstellen**
2. Wählen Sie Sicherungsdatei aus
3. Wiederherstellung bestätigen
4. **Hinweis**: Wiederherstellung überschreibt aktuelle Daten

## 5. UI-Illustrationen (Wireframe)

### 5.1 Haupt-Einstellungsbildschirm

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Einstellungen                    │
├─────────────────────────────────────────┤
│  Anzeige & Sprache                     │
│  ┌───────────────────────────────────┐ │
│  │ Sprache                           │ │
│  │ Deutsch                      →     │ │
│  │                                    │ │
│  │ Währung                           │ │
│  │ EUR (€)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Benachrichtigungen                          │
│  ┌───────────────────────────────────┐ │
│  │ Benachrichtigungen                [AN]  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Sicherung & Daten                          │
│  ┌───────────────────────────────────┐ │
│  │ Sicherung                        →    │ │
│  │                                    │ │
│  │ Wiederherstellen                       →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Kategorien                             │
│  ┌───────────────────────────────────┐ │
│  │ Kategorien verwalten              →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Sicherheit                               │
│  ┌───────────────────────────────────┐ │
│  │ Passwort                        →    │ │
│  │                                    │ │
│  │ Face ID / Fingerabdruck          →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logik & Regeln

### 6.1 Sprache

- Unterstützt: Deutsch, English, Tiếng Việt, 日本語
- Änderung der Sprache lädt gesamte App neu
- Systemkategorien werden automatisch in neue Sprache übersetzt

### 6.2 Währung

- Jede Sprache hat Standardwährung (z. B. EUR für Deutsch)
- Sie können andere Währung auswählen
- Alle Beträge werden gemäß ausgewählter Währung formatiert

### 6.3 Benachrichtigungen

- Benachrichtigungen funktionieren nur, wenn App Berechtigung hat
- Benachrichtigungszeit hängt von jeder Funktion ab und kann konfiguriert werden:
  - Wiederkehrendes Einkommen/Ausgaben: `notificationTime1`, `notificationTime2` (Standard 16:00 & 19:00)
  - Sparkonten & Kredite: `notificationTime1`, `notificationTime2` (Standard 10:00 & 19:00)
  - Besondere Anlässe & Vorbereitungsschritte: gemäß `reminderTime`, den Sie eingeben
  - Kann Benachrichtigungen für jeden Typ separat deaktivieren (in Zukunft)

### 6.4 Kategorien

- Systemkategorien können nicht gelöscht werden, nur deaktiviert
- Benutzerkategorien können gelöscht werden (wenn nicht in Verwendung)
- Jeder Kategorietyp ist unabhängig (wiederkehrendes Einkommen, tägliche Ausgaben, etc.)

## 7. Wichtige Hinweise

- **Regelmäßig sichern**: Sollten Daten periodisch sichern, um Datenverlust zu vermeiden
- **Wiederherstellung überschreibt**: Wiederherstellung ersetzt alle aktuellen Daten
- **Passwort**: Wenn Sie Passwort vergessen, können Sie zurücksetzen (löscht Daten)

