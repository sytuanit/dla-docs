# Wiederkehrendes Einkommen

## 1. Zweck

Das Modul **Wiederkehrendes Einkommen** hilft Ihnen bei der Verwaltung regelmäßiger Einkommensquellen wie:
- Monatliches Gehalt
- Mieteinnahmen
- Rente
- Investitionsdividenden
- Anderes wiederkehrendes Einkommen

Dieses Modul erstellt automatisch **Vorkommen** basierend auf dem von Ihnen konfigurierten Zyklus und erinnert Sie, wenn es Zeit ist, die Zahlung zu erhalten.

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie haben:
- Festes Einkommen nach Zeitplan (wöchentlich, alle zwei Wochen oder monatlich)
- Müssen verfolgen und bestätigen, wann die Zahlung erhalten wurde
- Möchten automatische Berechnung in monatliches Budget

## 3. Verwandte Bildschirme

- Liste wiederkehrendes Einkommen
- Neues wiederkehrendes Einkommen hinzufügen
- Wiederkehrendes Einkommen bearbeiten
- Vorkommensverlauf

## 4. Hauptverwendung

### 4.1 Neues wiederkehrendes Einkommen hinzufügen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Wiederkehrendes Einkommen**
2. Tippen Sie auf die **+** (FAB) Schaltfläche unten rechts
3. Füllen Sie die Informationen aus:
   - **Kategorie**: Wählen Sie eine Kategorie aus oder erstellen Sie eine neue
   - **Betrag**: Geben Sie den Einkommensbetrag ein (kann leer gelassen werden, beim Bestätigen eingeben)
   - **Zyklus**: Wählen Sie Wöchentlich / Alle zwei Wochen / Monatlich
   - **Datum**: Wählen Sie das Datum im Zyklus (z. B. 15. jedes Monats)
   - **Startdatum**: (Nur für Zwei-Wochen-Zyklus) Wählen Sie Startdatum
   - **Notiz**: Zusätzliche Informationen (optional)
4. Tippen Sie auf **Speichern**

### 4.2 Zahlungseingang bestätigen

1. Gehen Sie zur Liste wiederkehrendes Einkommen
2. Finden Sie Element mit **"Ausstehende Bestätigung"** Badge (gelb)
3. Tippen Sie auf das Element, um Bestätigungsdialog zu öffnen
4. Füllen Sie aus:
   - **Tatsächlicher Betrag**: (falls anders als erwartet)
   - **Notiz**: (optional)
5. Tippen Sie auf **Bestätigen**

### 4.3 Wiederkehrendes Einkommen bearbeiten

1. Gehen Sie zur Liste wiederkehrendes Einkommen
2. Tippen Sie auf das zu bearbeitende Element
3. Wählen Sie **Bearbeiten** aus dem Menü
4. Aktualisieren Sie die Informationen
5. Tippen Sie auf **Speichern**

### 4.4 Verlauf anzeigen

1. Gehen Sie zur Liste wiederkehrendes Einkommen
2. Tippen Sie auf ein Element
3. Wählen Sie **Verlauf**, um alle vergangenen Vorkommen anzuzeigen

### 4.5 Einkommen deaktivieren/aktivieren

1. Gehen Sie zur Liste wiederkehrendes Einkommen
2. Finden Sie das zu deaktivierende/aktivierende Element
3. Schalten Sie den **Aktiv**-Schalter auf der rechten Seite des Elements um

## 5. Beispiele & UI-Illustrationen

### 5.1 Beispiel 1: Monatliches wiederkehrendes Einkommen erstellen (Gehalt)

**Szenario**: Sie möchten das monatliche Gehalt verfolgen, damit die App Sie automatisch erinnert, wenn es Zeit ist, die Zahlung zu erhalten.

**Schritte**:
1. Gehen Sie zum Funktionsbildschirm, wählen Sie "Wiederkehrendes Einkommen"
2. Tippen Sie auf die "➕ Neu hinzufügen" Schaltfläche unten rechts
3. Wählen Sie Kategorie "Gehalt" (oder erstellen Sie neu, falls nicht verfügbar)
4. Geben Sie Betrag ein: €3,600
5. Wählen Sie Zyklus "Monatlich"
6. Wählen Sie "Tag des Monats auswählen", geben Sie 5 ein
7. Notiz automatisch ausgefüllt "Monatliches Gehalt" (kann bearbeitet werden)
8. Tippen Sie auf "Speichern"

**Ergebnis**: App zeigt Erfolgsmeldung an und kehrt zur Liste zurück. Neues Element erscheint mit vollständigen Informationen, und die App erinnert Sie automatisch am 5. jedes Monats.

**Bildschirm "Wiederkehrendes Einkommen hinzufügen"**:

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Wiederkehrendes Einkommen hinzufügen │
├─────────────────────────────────────────┤
│  Kategorie *                              │
│  [Gehalt ▼] [+ Neu hinzufügen]                 │
│                                         │
│  Betrag (EUR) *                          │
│  [€3,600]                               │
│                                         │
│  Zyklus *                                 │
│  ┌──────┐ ┌────────┐ ┌────────┐        │
│  │Woche │ │Zwei-Wo│ │Monat  │        │
│  └──────┘ └────────┘ └────────┘        │
│                                         │
│  Zahlungsdatum im Zyklus                  │
│  ⚪ Monatsende                         │
│  ⚫ Tag des Monats auswählen                  │
│  ┌───────────────────────────────────┐ │
│  │ Tag des Monats: [5]                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notiz                                    │
│  ┌───────────────────────────────────┐ │
│  │ Monatliches Gehalt                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Abbrechen]                  [Speichern]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Beispiel 2: Fälliges Einkommen bestätigen und tatsächlichen Betrag aktualisieren

**Szenario**: Es ist Zahltag (5.), aber der tatsächlich erhaltene Betrag ist €3,780 (Gehaltserhöhung) statt €3,600 wie eingestellt.

**Schritte**:
1. Öffnen Sie die App oder gehen Sie zum "Wiederkehrendes Einkommen" Bildschirm
2. App erkennt automatisch fälliges Vorkommen und zeigt Bestätigungsdialog
3. Dialog zeigt Standardbetrag: €3,600
4. Aktualisieren Sie tatsächlichen Betrag auf €3,780
5. Geben Sie Notiz ein: "Dieser Monat hat Bonus" (optional)
6. Tippen Sie auf "Erhalten bestätigen"

**Ergebnis**: App aktualisiert das bestätigte Vorkommen mit tatsächlichem Betrag €3,780, erstellt automatisch nächstes Vorkommen und aktualisiert aktuelles Finanzguthaben.

**Bestätigungsdialog Einkommen**:

```text
┌─────────────────────────────────────────┐
│  Erhalten bestätigen                        │
├─────────────────────────────────────────┤
│  Gehalt                                  │
│  Monatlich (5.)                          │
│  Fälligkeitsdatum: Heute                        │
│                                         │
│  Tatsächlicher Betrag *                         │
│  [€3,780]                               │
│                                         │
│  Notiz                                    │
│  [Dieser Monat hat Bonus]                 │
│                                         │
│  [Dieses abbrechen]    [Erhalten bestätigen]   │
└─────────────────────────────────────────┘
```

---

### 5.3 Beispiel 3: Einkommensvorkommen abbrechen, wenn Zahlung nicht erhalten wurde

**Szenario**: Es ist Mietzahlungstag (1.), aber der Mieter hat kein Geld überwiesen, daher wurde die Zahlung nicht erhalten.

**Schritte**:
1. Öffnen Sie die App oder gehen Sie zum "Wiederkehrendes Einkommen" Bildschirm
2. App zeigt Bestätigungsdialog für fälliges Vorkommen
3. Tippen Sie auf "Dieses abbrechen" Schaltfläche
4. Geben Sie Grund ein: "Mieter hat kein Geld überwiesen" (erforderlich)
5. Tippen Sie auf "Abbrechen bestätigen"

**Ergebnis**: Abgebrochenes Vorkommen ändert sich zu "Abgebrochen" Status, zeigt Kündigungsgrund, und App erstellt automatisch nächstes Vorkommen. Finanzguthaben ändert sich nicht, da keine Zahlung erhalten wurde.

**Dialog "Einkommensvorkommen abbrechen"**:

```text
┌─────────────────────────────────────────┐
│  Dieses abbrechen                              │
├─────────────────────────────────────────┤
│  Mieteinnahmen                            │
│  Monatlich (1.)                           │
│  Fälligkeitsdatum: Heute                         │
│                                         │
│  Kündigungsgrund *                    │
│  ┌───────────────────────────────────┐ │
│  │ Mieter hat kein Geld überwiesen    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Zurück]        [Abbrechen bestätigen]         │
└─────────────────────────────────────────┘
```

---

## 6. Logik & Regeln

### 6.1 Zyklus und Datum

- **Wöchentlich**: Tag der Woche auswählen (1=Montag, 7=Sonntag)
- **Alle zwei Wochen**: Tag der Woche + spezifisches Startdatum auswählen
- **Monatlich**: Tag des Monats auswählen (1-31)

### 6.2 Automatische Erstellung von Vorkommen

- App erstellt automatisch **Vorkommen**, wenn:
  - Neues Einkommen hinzufügen
  - Datum im Zyklus erreichen
  - Neuer Monat beginnt

### 6.3 Vorkommensstatus

- **AUSSTEHEND**: Ausstehende Bestätigung (zeigt gelbes Badge)
- **ABGESCHLOSSEN**: Bestätigt (zeigt grünes Badge)
- **ABGEBROCHEN**: Abgebrochen (zeigt rotes Badge)

### 6.4 Budget-Integration

- Beim Bestätigen des Einkommens aktualisiert die App automatisch das Budget des aktuellen Monats (falls vorhanden)
- Einkommen wird in "Wiederkehrendes Einkommen" im Budget berechnet

### 6.5 Benachrichtigungen

- App sendet Erinnerungsbenachrichtigung, wenn Zahlung fällig ist
- Benachrichtigungszeit kann für jedes Element konfiguriert werden (`notificationTime1`, `notificationTime2`, Standard 16:00 und 19:00)

## 7. Wichtige Hinweise

- **Betrag kann leer gelassen werden**: Wenn Sie den genauen Betrag nicht kennen, können Sie ihn leer lassen und beim Bestätigen eingeben
- **Kann nicht gelöscht werden, wenn Vorkommen existiert**: Wenn es Vorkommen gibt, können Sie nur deaktivieren (isActive = false), nicht löschen
- **Verspätete Bestätigung**: Sie können vergangene Vorkommen bestätigen, App berechnet Budget automatisch neu
- **Zyklus ändern**: Beim Bearbeiten des Zyklus werden zukünftige Vorkommen neu berechnet

