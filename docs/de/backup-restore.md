# Sicherung & Wiederherstellung

## 1. Zweck

Das Modul **Sicherung & Wiederherstellung** hilft Ihnen:
- Alle App-Daten in Datei zu sichern
- Daten aus Sicherungsdatei wiederherzustellen
- Daten vor Verlust durch Gerätefehler oder App-Neuinstallation zu schützen

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie möchten:
- Daten vor App-Neuinstallation sichern
- Daten auf neues Gerät übertragen
- Daten nach Datenverlust wiederherstellen
- Periodische Sicherungen erstellen

## 3. Verwandte Bildschirme

- Sicherungsbildschirm
- Wiederherstellungsbildschirm

## 4. Hauptverwendung

### 4.1 Daten sichern

1. Gehen Sie zu **Einstellungen** → **Sicherung & Daten** → **Sicherung**
2. Informationen anzeigen:
   - Anzahl der zu sichernden Datensätze
   - Erwartete Dateigröße
3. Tippen Sie auf **Sichern**
4. Wählen Sie Speicherort (Dateisystem)
5. Sicherungsdatei wird mit Namen erstellt: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Speichern Sie diese Datei an sicherem Ort (Cloud, Computer, etc.)

### 4.2 Daten wiederherstellen

1. Gehen Sie zu **Einstellungen** → **Sicherung & Daten** → **Wiederherstellen**
2. Wählen Sie Sicherungsdatei aus Dateisystem
3. Dateiinformationen anzeigen:
   - Sicherungserstellungsdatum
   - Anzahl der Datensätze
   - Dateigröße
4. **Warnung**: Wiederherstellung überschreibt alle aktuellen Daten
5. Tippen Sie auf **Wiederherstellen**
6. Wiederherstellung bestätigen
7. Warten Sie, bis Wiederherstellungsprozess abgeschlossen ist
8. App lädt automatisch neu

## 5. UI-Illustrationen (Wireframe)

### 5.1 Sicherungsbildschirm

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Daten sichern                   │
├─────────────────────────────────────────┤
│  Sicherungsinformationen                      │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Anzahl der Datensätze                  │ │
│  │ 1.234 Datensätze                      │ │
│  │                                    │ │
│  │ Erwartete Größe                      │ │
│  │ ~2,5 MB                            │ │
│  │                                    │ │
│  │ Zu sichernde Daten:              │ │
│  │ • Wiederkehrendes Einkommen                 │ │
│  │ • Wiederkehrende Ausgaben               │ │
│  │ • Tägliche Ausgaben                   │ │
│  │ • Budget                           │ │
│  │ • Ersparnisse                          │ │
│  │ • Kredite                            │ │
│  │ • Besondere Anlässe                │ │
│  │ • Kategorien                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Sichern]                               │
└─────────────────────────────────────────┘
```

### 5.2 Wiederherstellungsbildschirm

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Daten wiederherstellen                 │
├─────────────────────────────────────────┤
│  Sicherungsdatei auswählen                      │
│                                         │
│  [Datei auswählen...]                       │
│                                         │
│  Dateiinformationen                       │
│  ┌───────────────────────────────────┐ │
│  │ Datei: dla-backup-2024-11-15.json │ │
│  │                                    │ │
│  │ Erstellt: 15/11/2024 10:30         │ │
│  │                                    │ │
│  │ Anzahl der Datensätze: 1.234         │ │
│  │                                    │ │
│  │ Größe: 2,5 MB                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Warnung                             │
│  Wiederherstellung überschreibt alle aktuellen     │
│  Daten. Sind Sie sicher?                    │
│                                         │
│  [Wiederherstellen] [Abbrechen]                     │
└─────────────────────────────────────────┘
```

## 6. Logik & Regeln

### 6.1 Sicherungsdateiformat

- Sicherungsdatei ist JSON-Format
- Dateiname: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Enthält alle Daten: Benutzer, Kategorien, Transaktionen, Budgets, etc.

### 6.2 Gesicherte Daten

- Alle Tabellen in Datenbank
- Enthält sowohl Systemdaten als auch Benutzerdaten
- Enthält nicht: App-Einstellungen, Präferenzen (Sprache, Währung)

### 6.3 Wiederherstellung

- Wiederherstellung löscht alle aktuellen Daten
- Dann importiert Daten aus Sicherungsdatei
- App lädt automatisch neu nach Abschluss der Wiederherstellung

### 6.4 Validierung

- App prüft Dateiformat vor Wiederherstellung
- Prüft Versionskompatibilität (falls vorhanden)
- Zeigt Fehler an, wenn Datei ungültig ist

## 7. Wichtige Hinweise

- **Regelmäßig sichern**: Sollten periodisch sichern (wöchentlich oder monatlich)
- **An mehreren Orten speichern**: Speichern Sie Sicherungsdatei an mehreren Orten (Cloud, Computer, USB)
- **Wiederherstellung verliert aktuelle Daten**: Stellen Sie sicher, dass Sie aktuelle Daten gesichert haben, bevor Sie wiederherstellen
- **Kann nicht rückgängig gemacht werden**: Nach Wiederherstellung kann nicht rückgängig gemacht werden

