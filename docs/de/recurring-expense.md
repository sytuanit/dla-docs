# Wiederkehrende Ausgaben

## 1. Zweck

Das Modul **Wiederkehrende Ausgaben** hilft Ihnen bei der Verwaltung periodischer Ausgaben mit festen Zyklen wie:
- Strom-, Wasser-, Gasrechnungen
- Internet, Kabelfernsehen
- Versicherung
- Studiengebühren
- Miete
- Andere wiederkehrende Ausgaben

Dieses Modul erstellt automatisch **Vorkommen** basierend auf dem von Ihnen konfigurierten Zyklus und erinnert Sie, wenn die Zahlung fällig ist.

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie haben:
- Feste Ausgaben nach Zeitplan (wöchentlich, alle zwei Wochen oder monatlich)
- Müssen verfolgen und bestätigen, wann die Zahlung geleistet wurde
- Möchten automatische Berechnung in monatliches Budget

## 3. Verwandte Bildschirme

- Liste wiederkehrende Ausgaben
- Neue wiederkehrende Ausgabe hinzufügen
- Wiederkehrende Ausgabe bearbeiten
- Vorkommensverlauf

## 4. Hauptverwendung

### 4.1 Neue wiederkehrende Ausgabe hinzufügen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Wiederkehrende Ausgaben**
2. Tippen Sie auf die **+** (FAB) Schaltfläche unten rechts
3. Füllen Sie die Informationen aus:
   - **Kategorie**: Wählen Sie eine Kategorie aus oder erstellen Sie eine neue
   - **Betrag**: Geben Sie den Ausgabenbetrag ein (kann leer gelassen werden, beim Bestätigen eingeben)
   - **Zyklus**: Wählen Sie Wöchentlich / Alle zwei Wochen / Monatlich
   - **Datum**: Wählen Sie das Datum im Zyklus (z. B. 15. jedes Monats)
   - **Startdatum**: (Nur für Zwei-Wochen-Zyklus) Wählen Sie Startdatum
   - **Notiz**: Zusätzliche Informationen (optional)
4. Tippen Sie auf **Speichern**

### 4.2 Zahlung bestätigen

1. Gehen Sie zur Liste wiederkehrende Ausgaben
2. Finden Sie Element mit **"Ausstehende Bestätigung"** Badge (gelb)
3. Tippen Sie auf das Element, um Bestätigungsdialog zu öffnen
4. Füllen Sie aus:
   - **Tatsächlicher Betrag**: (falls anders als erwartet)
   - **Notiz**: (optional)
5. Tippen Sie auf **Bestätigen**

### 4.3 Wiederkehrende Ausgabe bearbeiten

1. Gehen Sie zur Liste wiederkehrende Ausgaben
2. Tippen Sie auf das zu bearbeitende Element
3. Wählen Sie **Bearbeiten** aus dem Menü
4. Aktualisieren Sie die Informationen
5. Tippen Sie auf **Speichern**

### 4.4 Verlauf anzeigen

1. Gehen Sie zur Liste wiederkehrende Ausgaben
2. Tippen Sie auf ein Element
3. Wählen Sie **Verlauf**, um alle vergangenen Vorkommen anzuzeigen

### 4.5 Ausgabe deaktivieren/aktivieren

1. Gehen Sie zur Liste wiederkehrende Ausgaben
2. Finden Sie das zu deaktivierende/aktivierende Element
3. Schalten Sie den **Aktiv**-Schalter auf der rechten Seite des Elements um

## 5. Beispiele & UI-Illustrationen

### 5.1 Beispiel 1: Monatliche wiederkehrende Ausgabe erstellen (Stromrechnung)

**Szenario**: Sie möchten die monatliche Stromrechnung verfolgen, damit die App Sie automatisch erinnert, wenn die Zahlung fällig ist.

**Schritte**:
1. Gehen Sie zum Funktionsbildschirm, wählen Sie "Wiederkehrende Ausgaben"
2. Tippen Sie auf die "➕ Neu hinzufügen" Schaltfläche unten rechts
3. Wählen Sie Kategorie "Versorgungsunternehmen" (oder erstellen Sie neu, falls nicht verfügbar)
4. Geben Sie Betrag ein: €18
5. Wählen Sie Zyklus "Monatlich"
6. Wählen Sie "Tag des Monats auswählen", geben Sie 15 ein
7. Notiz automatisch ausgefüllt "Monatliche Stromrechnung" (kann bearbeitet werden)
8. Tippen Sie auf "Speichern"

**Ergebnis**: App zeigt Erfolgsmeldung an und kehrt zur Liste zurück. Neues Element erscheint mit vollständigen Informationen, und die App erinnert Sie automatisch am 15. jedes Monats.

**Bildschirm "Wiederkehrende Ausgabe hinzufügen"**:

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Wiederkehrende Ausgabe hinzufügen        │
├─────────────────────────────────────────┤
│  Kategorie *                              │
│  [Versorgungsunternehmen ▼] [+ Neu hinzufügen]             │
│                                         │
│  Betrag (EUR) *                          │
│  [€18]                                  │
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
│  │ Tag des Monats: [15]                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notiz                                    │
│  ┌───────────────────────────────────┐ │
│  │ Monatliche Stromrechnung           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Abbrechen]                  [Speichern]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Beispiel 2: Fällige Ausgabe bestätigen und tatsächlichen Betrag aktualisieren

**Szenario**: Es ist Wasserrechnungszahlungstag (10.), aber der tatsächlich zu zahlende Betrag ist €6.30 (verringert) statt €7.20 wie eingestellt.

**Schritte**:
1. Öffnen Sie die App oder gehen Sie zum "Wiederkehrende Ausgaben" Bildschirm
2. App erkennt automatisch fälliges Vorkommen und zeigt Bestätigungsdialog
3. Dialog zeigt Standardbetrag: €7.20
4. Aktualisieren Sie tatsächlichen Betrag auf €6.30
5. Geben Sie Notiz ein: "Dieser Monat Wasser gespart" (optional)
6. Tippen Sie auf "Bezahlt bestätigen"

**Ergebnis**: App aktualisiert das bestätigte Vorkommen mit tatsächlichem Betrag €6.30, erstellt automatisch nächstes Vorkommen und aktualisiert aktuelles Finanzguthaben (subtrahiert €6.30).

**Bestätigungsdialog Ausgabe**:

```text
┌─────────────────────────────────────────┐
│  Bezahlt bestätigen                           │
├─────────────────────────────────────────┤
│  Wasserrechnung                              │
│  Monatlich (10.)                         │
│  Fälligkeitsdatum: Heute                        │
│                                         │
│  Tatsächlicher Betrag *                         │
│  [€6.30]                                   │
│                                         │
│  Notiz                                    │
│  [Dieser Monat Wasser gespart]               │
│                                         │
│  [Dieses abbrechen]    [Bezahlt bestätigen]        │
└─────────────────────────────────────────┘
```

---

### 5.3 Beispiel 3: Wiederkehrende Ausgabe deaktivieren, wenn nicht mehr anwendbar

**Szenario**: Sie mieten vorübergehend 2 Monate lang keine Wohnung, daher möchten Sie die "Miete" Ausgabe deaktivieren, anstatt sie vollständig zu löschen.

**Schritte**:
1. Gehen Sie zum "Wiederkehrende Ausgaben" Bildschirm
2. Finden Sie "Miete" Element in der Liste
3. Tippen Sie auf den "Aktiv" Schalter auf der rechten Seite des Elements
4. App zeigt Bestätigungsdialog: "Sind Sie sicher, dass Sie diese Ausgabe deaktivieren möchten?"
5. Tippen Sie auf "Deaktivieren" Schaltfläche, um zu bestätigen

**Ergebnis**: "Miete" Karte ändert sich zu "Inaktiv" Status (grau), Schalter ändert sich zu "Inaktiv". App erstellt keine neuen Vorkommen mehr für diese Ausgabe. Sie können durch Tippen auf den Schalter "Inaktiv" → "Aktiv" reaktivieren.

**Liste mit Schalter**:

```text
┌─────────────────────────────────────────┐
│  ← Zurück    Wiederkehrende Ausgaben           │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Miete              [⚪ Inaktiv]   │ │
│  │ €1,080                            │
│  │ Monatlich - 1.                     │
│  │ (Deaktiviert)                     │
│  │                                    │
│  │ [Bearbeiten] [Verlauf] [Löschen]         │
│  └───────────────────────────────────┘ │
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
  - Neue Ausgabe hinzufügen
  - Datum im Zyklus erreichen
  - Neuer Monat beginnt

### 6.3 Vorkommensstatus

- **AUSSTEHEND**: Ausstehende Bestätigung (zeigt gelbes Badge)
- **ABGESCHLOSSEN**: Bestätigt (zeigt grünes Badge)
- **ABGEBROCHEN**: Abgebrochen (zeigt rotes Badge)

### 6.4 Budget-Integration

- Beim Bestätigen der Ausgabe aktualisiert die App automatisch das Budget des aktuellen Monats (falls vorhanden)
- Ausgabe wird in "Wiederkehrende Ausgaben" im Budget berechnet

### 6.5 Benachrichtigungen

- App sendet Erinnerungsbenachrichtigung, wenn Zahlung fällig ist
- Benachrichtigungszeit kann für jedes Element konfiguriert werden (`notificationTime1`, `notificationTime2`, Standard 16:00 und 19:00)

## 7. Wichtige Hinweise

- **Betrag kann leer gelassen werden**: Wenn Sie den genauen Betrag nicht kennen, können Sie ihn leer lassen und beim Bestätigen eingeben
- **Kann nicht gelöscht werden, wenn Vorkommen existiert**: Wenn es Vorkommen gibt, können Sie nur deaktivieren (isActive = false), nicht löschen
- **Verspätete Bestätigung**: Sie können vergangene Vorkommen bestätigen, App berechnet Budget automatisch neu
- **Zyklus ändern**: Beim Bearbeiten des Zyklus werden zukünftige Vorkommen neu berechnet

