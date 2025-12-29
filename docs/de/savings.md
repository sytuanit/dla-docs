# Ersparnisse

## 1. Zweck

Das Modul **Ersparnisse** hilft Ihnen bei der Verwaltung von Sparkonten, Verfolgung von Guthaben, Zinssätzen und Laufzeiten. Dieses Modul unterstützt:
- Verwaltung mehrerer Sparkonten
- Verfolgung von Zinssätzen und Laufzeiten
- Automatische Berechnung der Zinsen bei Fälligkeit
- Vorzeitige Abhebung (falls erforderlich)
- Kontoumschlag

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie haben:
- Sparkonten
- Müssen Guthaben und Zinssätze verfolgen
- Möchten Erinnerungen bei Fälligkeit
- Müssen mehrere Sparkonten verwalten

## 3. Verwandte Bildschirme

- Liste Sparkonten
- Neues Konto hinzufügen
- Konto bearbeiten
- Kontodetails
- Vorzeitige Abhebung

## 4. Hauptverwendung

### 4.1 Neues Sparkonto erstellen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Bankersparnisse**
2. Tippen Sie auf die **+** (FAB) Schaltfläche unten rechts
3. Zeigen Sie "Aktuelles Guthaben" an (kann klicken, um Details anzuzeigen)
4. Wählen Sie Bank:
   - Wenn vorhanden: Aus Dropdown auswählen
   - Wenn nicht: Tippen Sie auf "+" Schaltfläche, um neue Bank zu erstellen
5. Geben Sie Einzahlungsbetrag ein (muss ≤ Aktuelles Guthaben sein)
6. Geben Sie Laufzeit ein: 1-36 Monate
7. Geben Sie Zinssatz ein: %/Jahr (1-100%)
8. Wählen Sie Startdatum (Standard ist heute, kann vom vorherigen Monat bis heute auswählen)
9. Zeigen Sie Fälligkeitsdatum automatisch berechnet an (vom Startdatum + Laufzeit)
10. Wählen Sie Plan bei Fälligkeit:
    - Kapital und Zinsen abheben (Standard)
    - KAPITAL umschlagen (Zinsen auf Konto)
    - KAPITAL + ZINSEN umschlagen
11. (Optional) Geben Sie Notiz ein
12. (Optional) Wählen Sie Benachrichtigungszeiten (Standard: 10:00 und 19:00)
13. Tippen Sie auf **KONTO ERSTELLEN**

### 4.2 Liste und Kontodetails anzeigen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Bankersparnisse**
2. Zeigen Sie "Sparkonten Liste" Bildschirm mit Standardfilter "Aktiv" an
3. Zeigen Sie Übersichtskarte an:
   - Filter "Aktiv": Aktuelles Guthaben, Geld in Ersparnissen, Erwartete Zinsen, Zinsen dieses Monats
   - Filter "Abgeschlossen": Gesamt abgehoben, Zinsen erhalten
4. (Optional) Verwenden Sie Suchleiste, um Konten nach Bankname oder Code zu finden
5. Wechseln Sie Filter zwischen "Aktiv" und "Abgeschlossen"
6. Tippen Sie auf ein Sparkonto, um Details anzuzeigen:
   - Kontoinformationen: Bank, Laufzeit, Zinssatz, Einzahlungsbetrag, Geschätzte Zinsen
   - Startdatum und Fälligkeitsdatum
   - Status: Aktiv
   - Plan bei Fälligkeit
   - (Falls vorhanden) Umschlagverlauf
   - "ABHEBEN" Schaltfläche (wenn aktiv)

### 4.3 Sparkonto abheben

1. Gehen Sie zur Sparkontenliste, finden Sie Konto, das Fälligkeitsdatum erreicht oder überschritten hat
2. Tippen Sie auf **ABHEBEN** Schaltfläche auf Karte (oder gehen Sie zu Details, dann tippen Sie auf "ABHEBEN")
3. Zeigen Sie "SPARKONTO ABHEBEN" Dialog mit:
   - Kontoinformationen: Bank, Einzahlungsbetrag, Laufzeit, Zinssatz
   - Abhebungsdatum (Standard = Fälligkeitsdatum, kann anderes Datum auswählen)
   - Zinsen erhalten (Standard = geschätzte Zinsen, kann bearbeitet werden)
   - Gesamt erhalten (automatisch berechnet = Kapital + Zinsen)
4. (Optional) Bearbeiten Sie Abhebungsdatum oder erhaltene Zinsen
5. Tippen Sie auf **BESTÄTIGEN**

### 4.4 Sparkonto umschlagen

1. Gehen Sie zur Sparkontenliste, finden Sie Konto, das Fälligkeitsdatum mit Plan "KAPITAL umschlagen" oder "KAPITAL + ZINSEN umschlagen" erreicht hat
2. Tippen Sie auf **UMSCHLAGEN** Schaltfläche oder "Wie geplant umschlagen"
3. Zeigen Sie "SPARKONTO UMSCHLAGEN" Dialog mit:
   - Kontoinformationen: Bank, Kapitalbetrag, Laufzeit, Zinssatz
   - Zinsen erhalten (wenn KAPITAL umschlagen, Zinsen gehen auf Konto)
4. (Optional) Bearbeiten Sie neuen Zinssatz oder neue Laufzeit (Standard = alte Laufzeit)
5. Tippen Sie auf **UMSCHLAGEN BESTÄTIGEN**

### 4.5 Sparkonto bearbeiten

1. Gehen Sie zu aktiven Sparkontodetails
2. Tippen Sie auf **Bearbeiten** Schaltfläche oben rechts
3. Bearbeiten Sie Informationen:
   - Bank (falls erforderlich)
   - Einzahlungsbetrag (wenn erhöhen, muss ≤ Aktuelles Guthaben sein)
   - Laufzeit, Zinssatz
   - Startdatum (falls erforderlich)
   - Plan bei Fälligkeit
   - Notiz, Benachrichtigungszeiten
4. Zeigen Sie Fälligkeitsdatum automatisch neu berechnet an (wenn Laufzeit/Startdatum sich ändert)
5. Tippen Sie auf **ÄNDERUNGEN SPEICHERN**

### 4.6 Neue Bank erstellen

1. Auf "Sparkonto hinzufügen" oder "Sparkonto bearbeiten" Bildschirm
2. Tippen Sie auf "Bank" Feld
3. Tippen Sie auf "+" Schaltfläche neben Dropdown, um neue Bank zu erstellen
4. Zeigen Sie "NEUE BANK HINZUFÜGEN" Dialog an
5. Geben Sie Bankname ein
6. Geben Sie Bankcode ein (max. 3-4 Zeichen, automatisch Großbuchstaben)
7. Wählen Sie Symbolfarbe (aus Farbwähler oder Palette)
8. Zeigen Sie Symbolvorschau an
9. Tippen Sie auf **ERSTELLEN**

## 5. Beispiele & UI-Illustrationen

### SAVINGS-01: Neues Sparkonto erstellen

**Ziel**: Neues Sparkonto erstellen, um Bankeinlage, Zinssatz und Fälligkeitsdatum zu verfolgen.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Bankersparnisse
2. Tippen Sie auf "+" (FAB) Schaltfläche
3. Wählen Sie Bank (oder erstellen Sie neu)
4. Geben Sie Einzahlungsbetrag, Laufzeit, Zinssatz ein
5. Wählen Sie Startdatum (Standard heute)
6. Wählen Sie Plan bei Fälligkeit
7. (Optional) Geben Sie Notiz und Benachrichtigungszeiten ein
8. Tippen Sie auf "KONTO ERSTELLEN"

**Wireframe - Sparkonto hinzufügen Bildschirm**:

```text
┌──────────────────────────────────────────────┐
│ <  Sparkonto hinzufügen                       │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ Karte ]                                      │
│                                               │
│ Aktuelles Guthaben                      [ > ]    │
│ €1,872                                        │
│                                               │
│ Bank *                                        │
│ [ Deutsche Bank ▼ ]                 [ + ] │
│                                               │
│ Einzahlungsbetrag (EUR) *                       │
│ [ €3,600 ]                                    │
│                                               │
│ Laufzeit *                                        │
│ [ 6 ] Monate                                  │
│                                               │
│ Zinssatz *                               │
│ [ 4.8 ] %/Jahr                                │
│                                               │
│ Startdatum *                                  │
│ [ 20/12/2025 ]                    [📅]        │
│                                               │
│ Fälligkeitsdatum (nur lesen)                      │
│ [ 20/06/2026 ]                                 │
│                                               │
│ Plan bei Fälligkeit                              │
│ (●) Kapital und Zinsen abheben          │
│ ( ) KAPITAL umschlagen                        │
│ ( ) KAPITAL + ZINSEN umschlagen            │
│                                               │
│ Notiz (optional)                               │
│ [                                      ]      │
│                                               │
│ Benachrichtigungszeit 1                           │
│ [ 10:00 ]                          [🕐]       │
│                                               │
│ Benachrichtigungszeit 2                            │
│ [ 19:00 ]                          [🕐]       │
└──────────────────────────────────────────────┘

        [  ABBRECHEN  ]       [  KONTO ERSTELLEN  ]
```

---

### SAVINGS-02: Sparkonto abheben

**Ziel**: Sparkonto abheben, wenn es Fälligkeitsdatum erreicht, um Kapital und Zinsen zu erhalten.

**Hauptschritte**:
1. Gehen Sie zur Sparkontenliste, finden Sie Konto, das Fälligkeitsdatum erreicht oder überschritten hat
2. Tippen Sie auf "ABHEBEN" Schaltfläche
3. Zeigen Sie Dialog mit Kontoinformationen, Abhebungsdatum, erhaltene Zinsen an
4. (Optional) Bearbeiten Sie Abhebungsdatum oder erhaltene Zinsen
5. Tippen Sie auf "BESTÄTIGEN"

**Wireframe - Abheben Dialog**:

```text
┌─────────────────────────────────────────┐
│  SPARKONTO ABHEBEN                │
├─────────────────────────────────────────┤
│  [ICON BANK]  Deutsche Bank            │
│                                         │
│  Laufzeit & Zinssatz: 6 Monate · 4.8%/Jahr │
│  Einzahlungsbetrag: €3,600                 │
│                                         │
│  Abhebungsdatum:                       │
│  [ 20 / 12 / 2025 ]  [📅]               │
│                                         │
│  Zinsen erhalten:                     │
│  [ €86 ]                                │
│                                         │
│  Gesamt erhalten: €3,686                 │
│                                         │
│  [  BESTÄTIGEN  ]                          │
└─────────────────────────────────────────┘
```

---

### SAVINGS-03: Liste und Kontodetails anzeigen

**Ziel**: Übersicht aktiver und abgeschlossener Sparkonten sowie Details jedes Kontos anzeigen.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Bankersparnisse
2. Zeigen Sie Übersichtskarte nach Filter an
3. Verwenden Sie Suchleiste (optional)
4. Wechseln Sie Filter zwischen "Aktiv" und "Abgeschlossen"
5. Tippen Sie auf Konto, um Details anzuzeigen

**Wireframe - Listenscreen**:

```text
┌──────────────────────────────────────────────┐
│ <  Bankersparnisse Verwaltung                    │
│                  [ + [FAB] Konto hinzufügen ]      │
└──────────────────────────────────────────────┘

[Chip] Filter
[ Aktiv ]   [ Abgeschlossen ]

┌──────────────────────────────────────────────┐
│  ÜBERSICHTSKARTE                                │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Aktuelles      │  │ Erwartete      │         │
│  │ Guthaben      │  │ Zinsen      │         │
│  │ €1,872       │  │ €197          │         │
│  └──────────────┘  └──────────────┘         │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Geld in     │  │ Zinsen dieses │         │
│  │ Ersparnissen      │  │ Monats      │         │
│  │ €12,600      │  │ €68           │         │
│  └──────────────┘  └──────────────┘         │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  🔍 Suchleiste                               │
│  [ 🔍 Suchen... ]                            │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ICON BANK] Deutsche Bank      [Icon Löschen] │
│                                              │
│ €3,600         |  6 Monate @ 4.8%           │
│                                              │
│ Geschätzte Zinsen: €86                     │
│ Fälligkeit: 20/12/2025   (5 Tage verbleibend)  │
│                    🔔 Bald fällig               │
│                                              │
│                    [ ABHEBEN ]             │
└──────────────────────────────────────────────┘
```

**Wireframe - Details Bildschirm**:

```text
┌──────────────────────────────────────────────┐
│ [ICON BANK]  Deutsche Bank          [ Bearbeiten ]│
│                                              │
│ Laufzeit & Zinssatz: 6 Monate · 4.8%/Jahr  │
│ Einzahlungsbetrag: €3,600                       │
│ Geschätzte Zinsen: €86                     │
│                                              │
│ Startdatum: 20/06/2025                       │
│ Fälligkeitsdatum: (5 Tage verbleibend) 20/12/2025 │
│                                              │
│ Status: Aktiv                               │
│                                              │
│ Plan bei Fälligkeit:                           │
│ (●) Kapital und Zinsen abheben         │
│                                              │
│                    [  ABHEBEN  ]           │
└──────────────────────────────────────────────┘
```

---

### SAVINGS-04: Sparkonto umschlagen

**Ziel**: Sparkonto wie geplant umschlagen, wenn es Fälligkeitsdatum erreicht.

**Hauptschritte**:
1. Finden Sie Konto, das Fälligkeitsdatum mit Plan "KAPITAL umschlagen" oder "KAPITAL + ZINSEN umschlagen" erreicht hat
2. Tippen Sie auf "UMSCHLAGEN" Schaltfläche
3. Zeigen Sie Dialog mit Kontoinformationen und erhaltene Zinsen an
4. (Optional) Bearbeiten Sie neuen Zinssatz oder neue Laufzeit
5. Tippen Sie auf "UMSCHLAGEN BESTÄTIGEN"

**Ergebnis**: Altes Konto wird aktualisiert, neues Konto wird mit rootSavingId verknüpft mit altem Konto erstellt. Wenn KAPITAL umschlagen, werden Zinsen zum aktuellen Guthaben hinzugefügt. Wenn KAPITAL + ZINSEN umschlagen, werden sowohl Kapital als auch Zinsen umgeschlagen.

---

### SAVINGS-05: Neue Bank erstellen

**Ziel**: Neue Bank erstellen, um beim Erstellen von Sparkonten zu verwenden.

**Hauptschritte**:
1. Auf "Sparkonto hinzufügen" oder "Sparkonto bearbeiten" Bildschirm
2. Tippen Sie auf "+" Schaltfläche neben "Bank" Dropdown
3. Geben Sie Bankname, Bankcode ein
4. Wählen Sie Symbolfarbe
5. Zeigen Sie Symbolvorschau an
6. Tippen Sie auf "ERSTELLEN"

**Wireframe - Bank erstellen Dialog**:

```text
┌─────────────────────────────────────────┐
│  NEUE BANK HINZUFÜGEN                            │
├─────────────────────────────────────────┤
│  BANKNAME                               │
│  [ ABC Bank ]                            │
│                                         │
│  BANKCODE                               │
│  [ ABC ]                                 │
│                                         │
│  SYMBOLFARBE                              │
│  [ 🎨 ]  #FF5722                         │
│                                         │
│  SYMBOLVORSCHAU                            │
│  ┌─────────┐                             │
│  │   ABC   │  (Hintergrund: #FF5722)      │
│  └─────────┘                             │
│                                         │
│  [  ABBRECHEN  ]    [  ERSTELLEN  ]           │
└─────────────────────────────────────────┘
```

---

### SAVINGS-06: Sparkonto bearbeiten

**Ziel**: Informationen aktives Sparkonto bearbeiten (Bank, Betrag, Laufzeit, Zinssatz, Fälligkeitsplan).

**Hauptschritte**:
1. Gehen Sie zu aktiven Sparkontodetails
2. Tippen Sie auf "Bearbeiten" Schaltfläche
3. Bearbeiten Sie notwendige Informationen
4. Zeigen Sie Fälligkeitsdatum automatisch neu berechnet an (wenn Laufzeit/Startdatum sich ändert)
5. Tippen Sie auf "ÄNDERUNGEN SPEICHERN"

**Ergebnis**: Kontoinformationen werden aktualisiert, geschätzte Zinsen werden basierend auf neuem Zinssatz neu berechnet. Wenn Betrag sich ändert, wird aktuelles Guthaben entsprechend angepasst.

## 6. Logik & Regeln

### 6.1 Zinsberechnung

- Zinsen werden nach Formel berechnet: `Betrag × Zinssatz × (Laufzeit / 12)`
- Zinsen werden bei Fälligkeit oder bei vorzeitiger Abhebung berechnet

### 6.2 Status

- **Aktiv (ACTIVE)**: Sparkonto ist aktiv, hat Fälligkeitsdatum nicht erreicht oder wurde nicht bearbeitet
- **Abgeschlossen (COMPLETED)**: Konto wurde abgehoben
- **Umschlagen (ROLLED_OVER)**: Konto wurde umgeschlagen, neues Konto erstellt

### 6.3 Abhebung und Umschlag

- **Abhebung**: Beim Abheben wird Kapital + Zinsen zum aktuellen Guthaben hinzugefügt, erstellt automatisch "Zusatzeinkommen" mit Kategorie "Ersparniszinsen"
- **Vorzeitige Abhebung**: Kann vor Fälligkeitsdatum abheben, erhaltene Zinsen können niedriger sein als geschätzte Zinsen
- **KAPITAL umschlagen**: Zinsen werden zum aktuellen Guthaben hinzugefügt, Kapital wird mit neuer Laufzeit umgeschlagen
- **KAPITAL + ZINSEN umschlagen**: Sowohl Kapital als auch Zinsen werden umgeschlagen, aktuelles Guthaben ändert sich nicht
- **Umschlagverlauf**: Umschläge werden gespeichert und in Kontodetails angezeigt, verknüpft über `rootSavingId`

### 6.4 Benachrichtigungen

- App sendet Erinnerungsbenachrichtigung, wenn Fälligkeitsdatum ankommt
- Benachrichtigungszeit kann für jedes Konto konfiguriert werden (`notificationTime1`, `notificationTime2`, Standard 10:00 und 19:00)

## 7. Wichtige Hinweise

- **Premium-Modul erforderlich**: Diese Funktion ist nur für Premium-Benutzer
- **Zinssatz**: Geben Sie Zinssatz pro Jahr ein (%/Jahr), von 1 bis 100%
- **Laufzeit**: Berechnet in Monaten, von 1 bis 36 Monaten
- **Fälligkeitsdatum**: Automatisch berechnet vom Startdatum + Laufzeit
- **Einzahlungsbetrag**: Muss ≤ Aktuelles Guthaben sein, beim Erstellen des Kontos wird automatisch vom aktuellen Guthaben abgezogen
- **Startdatum**: Kann nur vom Anfang des vorherigen Monats bis heute auswählen
- **Benachrichtigungen**: Benachrichtigungen werden am Fälligkeitsdatum zu 2 Zeiten gesendet (Standard 10:00 und 19:00), können für jedes Konto angepasst werden
- **Badge "Bald fällig"**: Wird angezeigt, wenn ≤ 7 Tage bis Fälligkeitsdatum
- **Badge "Fällig"**: Wird angezeigt, wenn Fälligkeitsdatum angekommen ist
- **Konto löschen**: Beim Löschen aktives Konto wird Kapitalbetrag zum aktuellen Guthaben hinzugefügt. Löschen Stammkonto löscht gesamte Umschlagkette
- **Übersichtskarte**: Ändert sich nach Filter, zeigt aggregierte Informationen für aktive oder abgeschlossene Konten an

