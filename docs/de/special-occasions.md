# Besondere Anlässe

## 1. Zweck

Das Modul **Besondere Anlässe** hilft Ihnen bei der Verwaltung besonderer Anlässe im Laufe des Jahres und der Vorbereitung darauf, einschließlich:
- Verwaltung besonderer Anlässe (Geburtstage, Feiertage, etc.)
- Erstellen von To-do-Listen (Vorbereitungsschritte)
- Anhängen von Checklisten an jeden Vorbereitungsschritt
- Erinnerungen vor Anlässen
- Verfolgung des Vorbereitungsfortschritts

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie möchten:
- Besondere Anlässe im Laufe des Jahres verwalten
- Für wichtige Anlässe vorbereiten
- To-do-Listen erstellen
- Erinnerungen vor Anlässen erhalten

## 3. Verwandte Bildschirme

- Liste besondere Anlässe
- Neuen besonderen Anlass hinzufügen
- Anlassdetails und Vorbereitungsschritte
- Vorbereitungsschritt hinzufügen
- Checkliste auswählen
- Neue Checkliste erstellen

## 4. Hauptverwendung

### 4.1 Besonderen Anlass hinzufügen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Besondere Anlässe**
2. Tippen Sie auf die **+** (FAB) Schaltfläche
3. Füllen Sie Informationen aus:
   - **Anlassname**: (z. B. "Mamas Geburtstag")
   - **Datum**: Wählen Sie Tag/Monat (DatePicker wählt nur Tag/Monat, kein Jahr)
   - **Mondkalender verwenden**: (Optional) Ankreuzen, wenn Sie Mondkalender verwenden möchten
     - Wenn angekreuzt: Geben Sie Mondtag und Monat ein, App berechnet automatisch nächstes Sonnendatum
   - **Wiederholen**: Jährlich / Nur dieses Jahr
   - **Benachrichtigung anzeigen um**: Wählen Sie Zeit (erforderlich, z. B. 07:00)
   - **Notiz**: Zusätzliche Informationen (optional)
4. (Optional) Vorbereitungsschritte hinzufügen (siehe 4.2)
5. Tippen Sie auf **Speichern**

### 4.2 Vorbereitungsschritt hinzufügen

1. Beim Hinzufügen neues Anlasses: Tippen Sie auf **+ Schritt hinzufügen** im Abschnitt "Vorbereitungsschritte"
2. Oder von Anlassdetails: Tippen Sie auf **+ Schritt hinzufügen**
3. Füllen Sie Informationen aus:
   - **Wann?**: "X Tage vorher" oder "Am Tag"
   - **Anzahl der Tage**: (wenn "X Tage vorher" ausgewählt) Geben Sie Anzahl der Tage vor Anlass ein
   - **Benachrichtigung anzeigen um**: Wählen Sie Zeit (erforderlich)
   - **Täglich wiederholen bis abgeschlossen**: (Optional) Ankreuzen, wenn Sie tägliche Erinnerungen möchten
   - **Inhalt**: Schrittname (erforderlich, z. B. "Geschenk kaufen")
   - **Notiz**: (Optional)
   - **Checkliste verwenden**: (Optional) Ankreuzen, um mit Einkaufscheckliste zu verknüpfen
4. Tippen Sie auf **Hinzufügen** (oder FAB "Anwenden")

### 4.3 Checkliste erstellen

1. Beim Hinzufügen Vorbereitungsschritt, kreuzen Sie **Checkliste verwenden** an
2. "Einkaufscheckliste auswählen" Bildschirm öffnet automatisch
3. Tippen Sie auf FAB **+**, um neue Checkliste zu erstellen
4. Geben Sie Checklistenname ein
5. Fügen Sie Elemente hinzu:
   - Geben Sie Elementname ein
   - Tippen Sie auf **+**, um neues Element hinzuzufügen
6. Tippen Sie auf **Speichern**
7. Neue Checkliste wird automatisch ausgewählt und kehrt zu "Vorbereitungsschritt hinzufügen" Bildschirm zurück

### 4.4 Schritt als abgeschlossen markieren

1. Gehen Sie zu besonderen Anlassdetails
2. Finden Sie Schritt zum Markieren
3. Tippen Sie auf Kontrollkästchen [ ], um zu [✓] zu ändern
4. Wenn Checkliste vorhanden, tippen Sie auf Checklistenname, um Elemente anzuzeigen und anzukreuzen/abzukreuzen

### 4.5 Fortschritt anzeigen

1. Gehen Sie zu besonderen Anlassdetails
2. Zeigen Sie Abschnitt "Übersicht" an:
   - Vorbereitungsschritte: Gesamtanzahl der Schritte
   - Abgeschlossen: Anzahl der angekreuzten Schritte / Gesamte Schritte
   - Status: Nicht gestartet / In Bearbeitung / Abgeschlossen

### 4.6 Besonderen Anlass bearbeiten

1. Gehen Sie zu besonderen Anlassdetails
2. Tippen Sie auf Hyperlink **Bearbeiten ›** im Header
3. Bearbeiten Sie Informationen: Name, Datum, Wiederholen, Erinnerungszeit, Notiz
4. Tippen Sie auf **Speichern**

### 4.7 Vorbereitungsschritt bearbeiten

1. Gehen Sie zu besonderen Anlassdetails
2. Tippen Sie auf Schritt zum Bearbeiten (klicken Sie auf gesamtes Element, außer Löschen-Symbol)
3. Bearbeiten Sie Informationen: Zeit, Inhalt, Checkliste
4. Tippen Sie auf **Anwenden** (oder FAB)

## 5. Beispiele & UI-Illustrationen

### OCCASION-01: Neuen besonderen Anlass erstellen (Geburtstag mit Vorbereitungsschritten)

**Ziel**: Neuen besonderen Anlass (Geburtstag) mit Vorbereitungsschritten erstellen, damit die App Sie automatisch erinnert, bevor der Anlass eintritt.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Besondere Anlässe → Tippen Sie auf "+" (FAB) Schaltfläche
2. Geben Sie Anlassname ein, wählen Sie Datum (01/05), wählen Sie Wiederholen "Jährlich", wählen Sie Erinnerungszeit (07:00)
3. Fügen Sie Vorbereitungsschritt 1 hinzu: "7 Tage vorher – 08:00" - "Geschenk kaufen"
4. Fügen Sie Vorbereitungsschritt 2 hinzu: "1 Tag vorher – 19:00" - "Kuchen bestellen"
5. Tippen Sie auf "Speichern"

**Wireframe - Besonderen Anlass hinzufügen Bildschirm**:

```text
┌──────────────────────────────────────────────┐
│ <  Besonderen Anlass hinzufügen                      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📝 Anlassinformationen                      │
│                                               │
│ Anlassname *                               │
│ [ An's Geburtstag                      ]       │
│                                               │
│ Datum                                          │
│ [ 01 / 05            ▼ ]                      │
│ (DatePicker wählt nur Tag/Monat)          │
│                                               │
│ [ ] Mondkalender verwenden                        │
│                                               │
│ Wiederholen                                        │
│ (•) Jährlich                                     │
│ ( ) Nur dieses Jahr                            │
│                                               │
│ Benachrichtigung anzeigen um *                        │
│ [ 07:00        ▼ ]                            │
│                                               │
│ Notiz (optional)                                │
│ [                                      ]      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📋 Vorbereitungsschritte          [ + Schritt hinzufügen ]│
│ ┌──────────────────────────────────────────┐ │
│ │  1. Geschenk kaufen                   [Icon Löschen] │ │
│ │     7 Tage vorher – 08:00                 │ │
│ │ ──────────────────────────────────────── │ │
│ │  2. Kuchen bestellen                   [Icon Löschen] │ │
│ │     1 Tag vorher – 19:00                 │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘

        [ Abbrechen ]                        [ Speichern ]
```

---

### OCCASION-02: Besonderen Anlass mit Mondkalender erstellen (Gedenktag mit Einkaufscheckliste)

**Ziel**: Besonderen Anlass mit Mondkalender erstellen (Gedenktag) mit Vorbereitungsschritten, die mit Einkaufscheckliste verknüpft sind, um Opfergabenkauf zu verfolgen.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Besondere Anlässe → Tippen Sie auf "+" (FAB) Schaltfläche
2. Geben Sie Anlassname "Mamas Gedenktag" ein, kreuzen Sie "Mondkalender verwenden" an
3. Geben Sie Monddatum ein: 15/11, App berechnet automatisch Sonnendatum: 15/12/2025
4. Fügen Sie 3 Vorbereitungsschritte hinzu, wobei Schritt 2 Checklistenlink "Opfergaben kaufen" hat
5. Tippen Sie auf "Speichern"

**Wireframe - Monddatum auswählen**:

```text
│ │ │ Monddatum                                   │ │ │
│ │ │ Tag (1-30)    Monat (1-12)                   │ │ │
│ │ │ [ 15 ]        [ 11 ]                         │ │ │
│ │ │                                               │ │ │
│ │ │ Sonnendatum (automatisch berechnet - nur Anzeige)  │ │ │
│ │ │ [ Text: 15/12/2025                 ]         │ │ │
│ │ │ (Dies ist das NÄCHSTE Sonnendatum in der Zukunft)│ │ │
```

---

### OCCASION-03: Liste und Details besonderer Anlässe anzeigen

**Ziel**: Übersicht besonderer Anlässe anzeigen, nach Zeit filtern und Details jedes Anlasses mit Vorbereitungsfortschritt anzeigen.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Besondere Anlässe
2. Zeigen Sie Liste mit Filter "Alle", "Bevorstehend", "Dieser Monat" an
3. Tippen Sie auf Anlasskarte, um Details anzuzeigen
4. Zeigen Sie Übersicht an: Anzahl der Schritte, Abgeschlossen, Status
5. Markieren Sie Schritt als abgeschlossen, indem Sie Kontrollkästchen ankreuzen

**Wireframe - Besondere Anlässe Liste Bildschirm**:

```text
┌────────────────────────────────────────────────────────────┐
│ 📅 Besondere Anlässe Liste                                  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ + Anlass hinzufügen ]                                     │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔍 Filter: [ Alle ]  [ Bevorstehend ]  [ Dieser Monat ]      │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Mamas Gedenktag    [In Bearbeitung] [Icon Löschen] │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 📅 15/12/2025 • 15/11 (Mond) • 10 Tage verbleibend  │ │ │
│ │ │                                                      │ │ │
│ │ │ ✅ Benötigte Vorbereitungsschritte:                        │ │ │
│ │ │   [✓] 3 Tage vorher – Opfergaben auflisten               │ │ │
│ │ │   [ ] 1 Tag vorher – Opfergaben einkaufen     │ │ │
│ │ │   [ ] Am Tag – Altar / Zeremonie vorbereiten        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

**Wireframe - Besonderer Anlass Details Bildschirm**:

```text
┌─────────────────────────────────────────────────────────┐
│ 📋 Besonderer Anlass Details                             │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Mamas Gedenktag                       [Bearbeiten ›]        │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 15/12/2025 (Sonne) • 15/11 (Mondkalender)      │ │ │
│ │ │ 10 Tage verbleibend • Wiederholen: Jährlich                │ │ │
│ │ │                                                      │ │ │
│ │ │ Notiz:                                             │ │ │
│ │ │ Kleine Mahlzeit, weiße Blumen, Gäste begrenzen.          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📊 Übersicht                                         │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Vorbereitungsschritte: 3                              │ │ │
│ │ │ Abgeschlossen: 1 / 3                                 │ │ │
│ │ │ Status: [In Bearbeitung]                            │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Vorbereitungsschritte                  [ + Schritt hinzufügen ]                  │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ [✓] Opfergaben auflisten                    [Icon Löschen]           │ │ │
│ │ │     3 Tage vorher – 08:00                        │ │ │
│ │ │     Abgeschlossen um 09:15 – 12/12/2025               │ │ │
│ │ │ ──────────────────────────────────────────────────── │ │ │
│ │ │                                                      │ │ │
│ │ │ [ ] Opfergaben einkaufen            [Icon Löschen]            │ │ │
│ │ │     1 Tag vorher – 19:00                      │ │ │
│ │ │     Täglich wiederholen bis abgeschlossen                  │ │ │
│ │ │     Einkaufscheckliste: Opfergaben kaufen ›           │ │ │
│ │ │     [✓] Abgeschlossen 3 / 8 Elemente                        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

---

### OCCASION-04: Vorbereitungsschritt mit Einkaufscheckliste hinzufügen

**Ziel**: Neuen Vorbereitungsschritt für besonderen Anlass hinzufügen und mit Einkaufscheckliste verknüpfen, um Einkauf zu verfolgen.

**Hauptschritte**:
1. Gehen Sie zu besonderen Anlassdetails → Tippen Sie auf "+ Schritt hinzufügen"
2. Wählen Sie "Wann?": "X Tage vorher", geben Sie Anzahl der Tage ein: 1
3. Wählen Sie Erinnerungszeit: 19:00
4. Aktivieren Sie "Täglich wiederholen bis abgeschlossen"
5. Geben Sie Inhalt ein: "Opfergaben einkaufen"
6. Kreuzen Sie "Checkliste verwenden" an → Wählen Sie Checkliste "Opfergaben kaufen"
7. Tippen Sie auf "Hinzufügen"

**Wireframe - Vorbereitungsschritt hinzufügen Bildschirm**:

```text
┌────────────────────────────────────────────────────────────┐
│ ➕ Vorbereitungsschritt hinzufügen                                     │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ⏰ Vorbereitungszeit                                    │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Wann? * (erforderlich)                                │ │ │
│ │ │ [ X Tage vorher         ▼ ]                       │ │ │
│ │ │                                                      │ │ │
│ │ │ Anzahl der Tage * (nur angezeigt, wenn "X Tage vorher") │ │ │
│ │ │ [  1  ]  Tage vorher                               │ │ │
│ │ │                                                      │ │ │
│ │ │ Benachrichtigung anzeigen um * (erforderlich)                  │ │ │
│ │ │ [ 19:00        ▼ ]                                 │ │ │
│ │ │                                                      │ │ │
│ │ │ [✓] Täglich wiederholen bis abgeschlossen                    │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Inhalt                                             │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Inhalt * (erforderlich)                              │ │ │
│ │ │ [ Opfergaben einkaufen               ]        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔗 Mit Einkaufscheckliste verknüpfen?                       │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ ☑ Checkliste verwenden                                    │ │ │
│ │ │ Einkaufscheckliste: Opfergaben kaufen ›    [Icon Tauschen]  │ │ │
│ │ │ (8 Elemente)                                          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ Abbrechen ]                        [ Hinzufügen ]             │ │
│ └────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

### OCCASION-05: Vorbereitungsschritt als abgeschlossen markieren und Checklistenfortschritt anzeigen

**Ziel**: Vorbereitungsschritte als abgeschlossen markieren und Einkaufschecklistenfortschritt verfolgen.

**Hauptschritte**:
1. Gehen Sie zu besonderen Anlassdetails
2. Zeigen Sie Schritt mit Checkliste an, der Fortschritt "Abgeschlossen 3 / 8 Elemente" zeigt
3. Tippen Sie auf Checklistenname, um Details anzuzeigen und Elemente anzukreuzen/abzukreuzen
4. Kreuzen Sie Schrittkontrollkästchen an, um als abgeschlossen zu markieren
5. Zeigen Sie "Übersicht" aktualisiert in Echtzeit an

---

### OCCASION-06: Besonderen Anlass und Vorbereitungsschritte bearbeiten

**Ziel**: Informationen besonderer Anlass und Vorbereitungsschritte nach Erstellung bearbeiten.

**Hauptschritte**:
1. Gehen Sie zu besonderen Anlassdetails → Tippen Sie auf "Bearbeiten ›"
2. Bearbeiten Sie Anlassname, Notiz
3. Tippen Sie auf "Speichern"
4. Tippen Sie auf Schritt zum Bearbeiten: Ändern Sie Zeit, Inhalt
5. Tippen Sie auf Löschen-Symbol, um Schritt zu löschen (hat Bestätigungsdialog)

## 6. Logik & Regeln

### 6.1 Mondkalender-Daten

- Sie können sowohl Sonnen- als auch Mondkalender-Daten eingeben
- App berechnet automatisch Sonnendatum entsprechend Monddatum
- Unterstützt jährliche Wiederholung nach Mondkalender

### 6.2 Wiederholen

- **Jährlich**: Anlass wiederholt sich jedes Jahr (nach Sonnen- oder Mondkalender)
  - Mit Sonnenkalender: Jedes Jahr berechnet nextOccurDate basierend auf (Tag/Monat) von solarDate
  - Mit Mondkalender: Jedes Jahr konvertiert von Monddatum zu entsprechendem Sonnendatum und aktualisiert nextOccurDate
- **Nur dieses Jahr**: Anlass nur gültig im aktuellen Jahr, wiederholt sich nicht nächstes Jahr

### 6.3 Vorbereitungsschritte

- **Wann?**: Hat 2 Optionen:
  - **X Tage vorher**: Erinnern X Tage vor Anlassdatum (muss Anzahl der Tage eingeben)
  - **Am Tag**: Erinnern am Anlassdatum (muss keine Anzahl der Tage eingeben)
- **Benachrichtigung anzeigen um**: Erinnerungszeit (erforderlich, Format HH:mm)
- **Täglich wiederholen bis abgeschlossen**: Wenn aktiviert, wird Benachrichtigung täglich wiederholt, bis Benutzer Schritt als abgeschlossen markiert
- **Checkliste verknüpfen**: Jeder Schritt kann eine Einkaufscheckliste anhängen, um Einkaufsfortschritt zu verfolgen

### 6.4 Checkliste

- Checkliste kann für mehrere Schritte wiederverwendet werden
- Verfolgen Sie Anzahl der abgeschlossenen Elemente / Gesamte Elemente (z. B. "Abgeschlossen 3 / 8 Elemente")
- Angezeigt in Schrittdetails mit Link "Checklistenname ›", um Details anzuzeigen
- Kann Elemente in Checkliste ankreuzen/abkreuzen, um Fortschritt zu aktualisieren
- Vorbereitungsschritt kann als abgeschlossen markiert werden, auch wenn Checkliste nicht vollständig abgeschlossen ist

### 6.5 Benachrichtigungen

- **Hauptanlass-Benachrichtigung**: Erstellt bei `nextOccurDate + reminder_time`
  - Mit JÄHRLICH Anlass: Benachrichtigung wird neu erstellt, wenn App startet (basierend auf neu berechnetem nextOccurDate)
  - Mit EINMAL Anlass: Benachrichtigung wird nur einmal für aktuelles nextOccurDate erstellt
- **Vorbereitungsschritt-Benachrichtigung**: Berechnen Sie Erinnerungsdatum basierend auf:
  - `nextOccurDate` des besonderen Anlasses
  - `reminderType` und `daysBefore` (falls vorhanden)
  - `reminderTime`
- **Wiederholungsbenachrichtigung**: Wenn `repeatDailyUntilComplete = true`:
  - Erstellen Sie täglich wiederholende Benachrichtigung
  - Verwenden Sie `notificationGroupKey`, um Wiederholungsbenachrichtigungen zu gruppieren
  - Automatisch abbrechen, wenn Benutzer Schritt als abgeschlossen markiert

## 7. Wichtige Hinweise

- **Mondkalender-Daten**: 
  - App konvertiert automatisch zu Sonnenkalender für Anzeige
  - Findet "NÄCHSTES Sonnendatum in der Zukunft" im Vergleich zu aktuellem Datum
  - Zukünftige Jahre: System berechnet immer entsprechendes Sonnendatum aus (Mondtag, Mondmonat) für jedes Jahr neu
  - Wenn dieses Jahr sowohl regulären als auch Schaltmonat desselben Monats hat: System kann 2 Erinnerungen erstellen, um zu vermeiden, dass etwas fehlt
- **Jährliche Wiederholung**: 
  - Anlass berechnet automatisch nextOccurDate nächstes Jahr neu
  - Mit Mondkalender: Jedes Jahr konvertiert von Monddatum zu entsprechendem Sonnendatum
- **Erinnerungszeit**: 
  - Muss einen Wert haben (kann nicht leer sein)
  - Muss korrektes Format HH:mm haben (00:00 - 23:59)
- **Checkliste**: 
  - Gelöschte Checkliste wird immer noch in Schritt angezeigt (kann aber nicht bearbeitet werden)
  - Kann Schritt als abgeschlossen markieren, auch wenn Checkliste nicht vollständig abgeschlossen ist
- **Benachrichtigungen**: 
  - Müssen Benachrichtigungen in Einstellungen aktivieren, um Erinnerungen zu erhalten
  - Wiederholungsbenachrichtigungen werden automatisch abgebrochen, wenn Schritt als abgeschlossen markiert wird
- **Anlassstatus**:
  - **Nicht gestartet**: Alle Schritte sind nicht abgeschlossen (grau)
  - **In Bearbeitung**: Mindestens 1 Schritt ist abgeschlossen, aber nicht alle (blau)
  - **Abgeschlossen**: Alle Schritte sind abgeschlossen (dunkelgrün)
  - Wenn Anlass keine Vorbereitungsschritte hat: Status wird nach Datum berechnet (Nicht gestartet / Laufend / Abgeschlossen)

