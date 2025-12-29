# Aufgabenliste

## 1. Zweck

Das Modul **Aufgabenliste** hilft Ihnen bei der Verwaltung wiederkehrender Aufgaben und der Verfolgung des Abschlussfortschritts, einschließlich:
- Zeitbasierte wiederkehrende Aufgaben (täglich/wöchentlich/monatlich/jährlich)
- Metrikbasierte wiederkehrende Aufgaben (Meilen/Stunden/Mal...)
- Erinnerungen, wenn fällig
- Abschlussverlauf verfolgen
- Ausgaben erfassen (falls zutreffend)

Dieses Modul hilft Ihnen, wichtige Aufgaben wie Autowartung, Filterwechsel, periodische Kontrollen usw. nie zu verpassen.

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie haben:
- Aufgaben, die nach Zeitplan wiederkehren (z. B. Wasserfilter alle 3 Monate wechseln)
- Aufgaben, die basierend auf Metriken wiederkehren (z. B. Motoröl alle 3.000 Meilen wechseln)
- Müssen automatische Erinnerungen, wenn fällig
- Möchten Abschlussverlauf verfolgen
- Müssen zugehörige Ausgaben erfassen

## 3. Verwandte Bildschirme

- Aufgabenliste Bildschirm
- Aufgabentyp auswählen (Zeitbasiert / Metrikbasiert)
- Neue Aufgabe hinzufügen
- Aufgabe bearbeiten
- Metrikbasierte Aufgabe bestätigen
- Aufgabenverlauf
- Fällige Aufgaben Liste (Glockenliste)

## 4. Hauptverwendung

### 4.1 Zeitbasierte Aufgabe hinzufügen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Aufgabenliste**
2. Tippen Sie auf die **+** (FAB) Schaltfläche unten rechts
3. Wählen Sie **Zeitbasierte Aufgabe**
4. Füllen Sie Informationen aus:
   - **Aufgabenname**: (erforderlich, z. B. "Wasserfilter wechseln")
   - **Wiederholungszyklus**: Geben Sie Zahl ein und wählen Sie Einheit (Tag/Woche/Monat/Jahr)
   - **Nächstes Fälligkeitsdatum**: Wählen Sie Datum (nur ab morgen auswählen erlaubt)
   - **Erinnerungszeit**: Wählen Sie Zeit (erforderlich, z. B. 08:00)
   - **Diese Aufgabe verursacht Ausgaben**: (Optional) Ankreuzen, wenn es Ausgaben gibt
     - Wenn angekreuzt: Wählen Sie **Kategorie** (erforderlich)
   - **Notiz**: Zusätzliche Informationen (optional)
5. Tippen Sie auf **Speichern**

### 4.2 Metrikbasierte Aufgabe hinzufügen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Aufgabenliste**
2. Tippen Sie auf die **+** (FAB) Schaltfläche
3. Wählen Sie **Metrikbasierte Aufgabe**
4. Füllen Sie Informationen aus:
   - **Aufgabenname**: (erforderlich, z. B. "Motoröl wechseln")
   - **Zyklus**: Geben Sie Zahl ein (z. B. 3.000)
   - **Einheit**: Geben Sie Einheit ein (z. B. "Meilen")
   - **Letzter abgeschlossener Metrikwert**: Geben Sie aktuellen Wert ein (z. B. 12.500)
   - **Diese Aufgabe verursacht Ausgaben**: (Optional) Ankreuzen, wenn es Ausgaben gibt
     - Wenn angekreuzt: Wählen Sie **Kategorie** (erforderlich)
   - **Notiz**: Zusätzliche Informationen (optional)
5. Tippen Sie auf **Speichern**

### 4.3 Metrikbasierte Aufgabe bestätigen

1. Gehen Sie zur Aufgabenliste
2. Finden Sie metrikbasierte Aufgabe (METRIC Typ) zum Bestätigen
3. Tippen Sie auf **Bestätigen** Schaltfläche in der Karte (nur angezeigt, wenn `isActive = true`)
4. Füllen Sie Informationen aus:
   - **Aktueller Metrikwert**: Geben Sie aktuellen Wert ein (erforderlich, muss ≥ letzter abgeschlossener Metrikwert sein)
   - **Notiz**: (Optional)
5. Zeigen Sie **Delta** automatisch berechnet an (aktueller Wert - letzter abgeschlossener Wert)
6. Tippen Sie auf **Bestätigt**
7. (Wenn Aufgabe Ausgaben hat) Wählen Sie **Ausgabe hinzufügen** oder **Abbrechen**

**Hinweis**: Zeitbasierte Aufgaben (CYCLE Typ) haben keine "Bestätigen" Schaltfläche in der Karte. Bestätigung wird nur im "Fällige Aufgaben" (Glockenliste) Bildschirm durchgeführt.

### 4.4 Liste und Details anzeigen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Aufgabenliste**
2. Verwenden Sie **Suchleiste**, um nach Aufgabenname zu suchen
3. Verwenden Sie **Filter-Chips**, um zu filtern:
   - **Alle**: Zeigt alle Aufgaben an
   - **Zeitbasiert**: Zeigt nur CYCLE Typ Aufgaben an
   - **Metrikbasiert**: Zeigt nur METRIC Typ Aufgaben an
4. Tippen Sie auf Aufgabenkarte, um Details anzuzeigen und zu bearbeiten

### 4.5 Aufgabe bearbeiten

1. Gehen Sie zur Aufgabenliste
2. Tippen Sie auf Aufgabenkarte zum Bearbeiten
3. Aktualisieren Sie Informationen:
   - **Notiz**: Wenn es Verlauf gibt, wird **Zyklus** (CYCLE) oder **Einheit/Zyklus** (METRIC) gesperrt und kann nicht bearbeitet werden
4. Tippen Sie auf **Speichern**

### 4.6 Verlauf anzeigen

1. Gehen Sie zur Aufgabenliste
2. Tippen Sie auf **Verlauf anzeigen ›** Link der Aufgabe zum Anzeigen
3. Verwenden Sie **Filter-Chips**, um nach Zeit zu filtern:
   - **Alle**: Zeigt gesamten Verlauf an
   - **Dieser Monat**: Zeigt nur Verlauf vom aktuellen Monat an
   - **Letzter Monat**: Zeigt nur Verlauf vom vorherigen Monat an
   - **Letzte 3 Monate**: Zeigt nur Verlauf von den letzten 3 Monaten an

### 4.7 Aufgabe deaktivieren/aktivieren

1. Gehen Sie zur Aufgabenliste
2. Finden Sie Aufgabe zum Deaktivieren/Aktivieren
3. Schalten Sie **Aktiv** Schalter in der Kartenfußzeile um
4. Deaktivierte Aufgaben zeigen **"Inaktiv"** Badge (grau) an

### 4.8 Aufgabe löschen

1. Gehen Sie zur Aufgabenliste
2. Tippen Sie auf **Löschen** Symbol (🗑️) im Kartenheader
3. Löschung im Dialog bestätigen
4. Die Aufgabe und der gesamte zugehörige Verlauf werden gelöscht

## 5. Beispiele & UI-Illustrationen

### TODO-01: Zeitbasierte Aufgabe erstellen (Wasserfilter wechseln)

**Ziel**: Zeitbasierte Aufgabe erstellen, damit die App Sie automatisch erinnert, wenn sie fällig ist.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Aufgabenliste → Tippen Sie auf "+" (FAB) Schaltfläche
2. Wählen Sie "Zeitbasierte Aufgabe"
3. Geben Sie Aufgabenname ein: "Wasserfilter wechseln"
4. Geben Sie Zyklus ein: "3" Monate
5. Wählen Sie nächstes Fälligkeitsdatum: 01/03/2026
6. Wählen Sie Erinnerungszeit: 08:00
7. Kreuzen Sie "Diese Aufgabe verursacht Ausgaben" an, wählen Sie Kategorie "Versorgungsunternehmen"
8. Geben Sie Notiz ein: "Filter #1 und #2 wechseln"
9. Tippen Sie auf "Speichern"

**Wireframe - Zeitbasierte Aufgabe hinzufügen Bildschirm**:

```text
┌──────────────────────────────────────────────┐
│ <  Zeitbasierte Aufgabe hinzufügen                      │
├──────────────────────────────────────────────┤

Aufgabenname
[ Wasserfilter wechseln            ]

Wiederholungszyklus
Alle [ 3 ] [ Monat ▼ ]
(Einheit: Tag / Woche / Monat / Jahr)

Nächstes Fälligkeitsdatum
[ 01 / 03 / 2026    ▼ ]
Hinweis: 
Fälligkeitsdatum für das erste Mal.
Nachfolgende Daten werden automatisch basierend auf dem von Ihnen eingegebenen Zyklus berechnet.

Erinnerungszeit
[ 08 : 00           ▼ ]

──────────────────────────────────────────────
[✓] Diese Aufgabe verursacht Ausgaben

┌─────────────────────────────────────┐
│ Kategorie *                           │
│ [Versorgungsunternehmen ▼] [+ Neu erstellen]       │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Notiz (optional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Abbrechen ]                         [ Speichern ]
└──────────────────────────────────────────────┘
```

---

### TODO-02: Metrikbasierte Aufgabe erstellen (Motoröl wechseln)

**Ziel**: Metrikbasierte Aufgabe erstellen, um Autowartung basierend auf Kilometerstand zu verfolgen.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Aufgabenliste → Tippen Sie auf "+" (FAB) Schaltfläche
2. Wählen Sie "Metrikbasierte Aufgabe"
3. Geben Sie Aufgabenname ein: "Motoröl wechseln"
4. Geben Sie Zyklus ein: "3.000", Einheit: "Meilen"
5. Geben Sie letzter abgeschlossener Metrikwert ein: "12.500"
6. Kreuzen Sie "Diese Aufgabe verursacht Ausgaben" an, wählen Sie Kategorie "Autowartung"
7. Geben Sie Notiz ein: "Öl + Ölfilter wechseln"
8. Tippen Sie auf "Speichern"

**Wireframe - Metrikbasierte Aufgabe hinzufügen Bildschirm**:

```text
┌──────────────────────────────────────────────┐
│ <  Metrikbasierte Aufgabe hinzufügen                    │
├──────────────────────────────────────────────┤

Aufgabenname
[ Motoröl wechseln                        ]

Zyklus
Alle [ 3.000 ] Einheit [ Meilen ]
(Einheit: Meilen / Stunden / Mal / ...)

Letzter abgeschlossener Metrikwert
[ 12.500 ]

──────────────────────────────────────────────
[✓] Diese Aufgabe verursacht Ausgaben

┌─────────────────────────────────────┐
│ Kategorie *                           │
│ [Autowartung ▼] [+ Neu erstellen] │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Notiz (optional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Abbrechen ]                         [ Speichern ]
└──────────────────────────────────────────────┘
```

---

### TODO-03: Liste und Details anzeigen

**Ziel**: Übersicht der Aufgaben anzeigen, nach Typ filtern, suchen und Details jeder Aufgabe anzeigen.

**Hauptschritte**:
1. Gehen Sie zu Funktionen → Aufgabenliste
2. Zeigen Sie Liste mit Suchleiste und Filter-Chips an
3. Verwenden Sie Filter: "Alle", "Zeitbasiert", "Metrikbasiert"
4. Verwenden Sie Suchleiste, um nach Aufgabenname zu suchen
5. Tippen Sie auf Aufgabenkarte, um Details anzuzeigen

**Wireframe - Aufgabenliste Bildschirm**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Zurück]  Aufgabenliste                        [🔔]        │
└─────────────────────────────────────────────────────────┘
│  🔍 Suchen...                                             │
│                                                          │
│  [Alle] [Zeitbasiert] [Metrikbasiert]                     │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Karte: Wasserfilter wechseln                      │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Wasserfilter wechseln    [Abgeschlossen] [🗑️]   │ │    │
│  │ │                                              │ │    │
│  │ │ 📅 Zyklus: Alle 3 Monate                     │ │    │
│  │ │ ✅ Zuletzt abgeschlossen: 01/12/2025                │ │    │
│  │ │ 📅 Nächstes Fälligkeitsdatum: 01/03/2026                 │ │    │
│  │ │ ⏳ 76 Tage verbleibend                          │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Verlauf anzeigen ›                     [⚪ Aktiv]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Karte: Motoröl wechseln                            │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Motoröl wechseln                   [🗑️]      │ │    │
│  │ │                                              │ │    │
│  │ │ 📏 Verfolgen nach: Meilen                           │ │    │
│  │ │ ✅ Zuletzt bestätigt: 02/12/2025                │ │    │
│  │ │ 🔢 Letzter Metrikwert: 12.500 Meilen          │ │    │
│  │ │ 🎯 Nächstes fällig: 15.500 Meilen                    │ │    │
│  │ │ ⏳ ~300 Meilen verbleibend                      │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ [✓ Bestätigen]                                  │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Verlauf anzeigen ›                     [⚪ Aktiv]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ FAB]                                                 │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-04: Metrikbasierte Aufgabe bestätigen (Motoröl wechseln)

**Ziel**: Abschluss einer metrikbasierten Aufgabe bestätigen, indem aktueller Metrikwert eingegeben wird.

**Hauptschritte**:
1. Gehen Sie zur Aufgabenliste
2. Finden Sie "Motoröl wechseln" Aufgabe (METRIC Typ)
3. Tippen Sie auf "Bestätigen" Schaltfläche
4. Geben Sie aktuellen Metrikwert ein: "14.520"
5. Zeigen Sie automatisch berechnetes Delta an: "+2.020 Meilen"
6. Geben Sie Notiz ein: "Öl + Ölfilter gewechselt"
7. Tippen Sie auf "Bestätigt"

**Wireframe - Metrikbasierte Aufgabe bestätigen Dialog**:

```text
┌──────────────────────────────────────────────┐
│  Metrikbasierte Aufgabe bestätigen                   │
├──────────────────────────────────────────────┤

Aufgabenname:
Motoröl wechseln   (nur lesen)

Verfolgen nach:
Meilen   (nur lesen)

Letzter abgeschlossener Metrikwert:
12.500 Meilen   (nur lesen)

──────────────────────────────────────────────
Aktueller Metrikwert
[ 14.520 ] Meilen

Delta:
+2.020 Meilen   (automatisch)

──────────────────────────────────────────────
Notiz
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
        [ Nicht bestätigt ]    [ Bestätigt ]
└──────────────────────────────────────────────┘
```

---

### TODO-05: Aufgabe bearbeiten und Verlauf anzeigen

**Ziel**: Aufgabeninformationen bearbeiten und Abschlussverlauf anzeigen.

**Hauptschritte**:
1. Gehen Sie zur Aufgabenliste
2. Tippen Sie auf "Wasserfilter wechseln" Aufgabenkarte
3. Zeigen Sie Warnung an: "⚠️ Zyklus ist gesperrt, weil es Verlauf gibt" (wenn Verlauf existiert)
4. Bearbeiten Sie nächstes Fälligkeitsdatum, Erinnerungszeit, Notiz
5. Tippen Sie auf "Speichern"
6. Tippen Sie auf "Verlauf anzeigen ›", um Verlauf mit Filtern anzuzeigen

**Wireframe - Aufgabenverlauf Bildschirm**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Zurück]  Aufgabenverlauf - Wasserfilter wechseln          │
└─────────────────────────────────────────────────────────┘
│  [Alle] [Dieser Monat] [Letzter Monat] [Letzte 3 Monate]        │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Wasserfilter wechseln            [Abgeschlossen]      │    │
│  │                                                  │    │
│  │ 📅 Zyklus: Alle 3 Monate                         │    │
│  │ ✅ Abgeschlossen am: 01/12/2025 – 09:10             │    │
│  │ 📝 Notiz: Filter #1 und #2 wechseln                │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Wasserfilter wechseln            [Abgeschlossen]      │    │
│  │                                                  │    │
│  │ 📅 Zyklus: Alle 3 Monate                         │    │
│  │ ✅ Abgeschlossen am: 01/09/2025 – 08:45             │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-06: Aufgabe deaktivieren und löschen

**Ziel**: Aufgabe deaktivieren oder löschen, wenn nicht mehr benötigt.

**Hauptschritte**:
1. Gehen Sie zur Aufgabenliste
2. Finden Sie Aufgabe zum Deaktivieren
3. Tippen Sie auf "Aktiv" Schalter, um auszuschalten
4. Zeigen Sie "Inaktiv" Badge erscheinen an
5. Tippen Sie erneut auf Schalter, um zu reaktivieren
6. Tippen Sie auf Löschen Symbol (🗑️), um Aufgabe zu löschen
7. Löschung im Dialog bestätigen

---

### TODO-07: Metrikbasierte Aufgabe bestätigen und Ausgabe hinzufügen

**Ziel**: Metrikbasierte Aufgabe bestätigen und automatisch zugehörige Ausgabe hinzufügen.

**Hauptschritte**:
1. Gehen Sie zur Aufgabenliste
2. Finden Sie "Motoröl wechseln" Aufgabe (METRIC Typ, hasCost = true)
3. Tippen Sie auf "Bestätigen" Schaltfläche
4. Geben Sie aktuellen Metrikwert ein: "14.520"
5. Geben Sie Notiz ein: "Öl + Ölfilter gewechselt"
6. Tippen Sie auf "Bestätigt"
7. Zeigen Sie "Verursachte Ausgabe?" Dialog automatisch öffnen an
8. Tippen Sie auf "Ausgabe hinzufügen"
9. Zeigen Sie "Ausgabe hinzufügen" Bildschirm mit Notiz und Kategorie vorausgefüllt an
10. Geben Sie Betrag ein: €45
11. Tippen Sie auf "Speichern"

**Wireframe - Verursachte Ausgabe Dialog**:

```text
┌──────────────────────────────────────────────┐
│  Verursachte Ausgabe?                           │
├──────────────────────────────────────────────┤
Möchten Sie eine Ausgabe für diesen
Abschluss hinzufügen?

        [ Abbrechen ]         [ Ausgabe hinzufügen ]
└──────────────────────────────────────────────┘
```

## 6. Logik & Regeln

### 6.1 Aufgabentypen

- **Zeitbasiert (CYCLE Typ)**:
  - Wiederholt sich nach Zeitplan (Tag/Woche/Monat/Jahr)
  - Hat Erinnerungsbenachrichtigungen, wenn fällig
  - Bestätigung wird nur im "Fällige Aufgaben" (Glockenliste) Bildschirm durchgeführt
  - Keine "Bestätigen" Schaltfläche in der Karte

- **Metrikbasiert (METRIC Typ)**:
  - Wiederholt sich basierend auf Metrik-Meilensteinen (Meilen/Stunden/Mal/Andere)
  - Keine Benachrichtigungen (MVP1)
  - Hat "Bestätigen" Schaltfläche in der Karte (nur angezeigt, wenn `isActive = true`)
  - Bestätigung durch Eingabe aktuellen Metrikwerts

### 6.2 Aufgabenstatus

- **AUSSTEHEND**: Bevorstehend (noch nicht fällig)
  - Kein Badge angezeigt: `nextDueDate - heute > 7 Tage`
  - Zeigt "Bevorstehend" Badge (gelb): `0 < nextDueDate - heute ≤ 7 Tage`
- **ÜBERFÄLLIG**: Überfällig (rot) - `nextDueDate < heute` und nicht bestätigt
- **NICHT ABGESCHLOSSEN**: Nicht erledigt (orange) - Fällig, aber nicht bestätigt
- **ABGESCHLOSSEN**: Abgeschlossen (grün) - Bestätigt
- **ABGEBROCHEN**: Abgebrochen (grau) - Dieses Vorkommen wurde abgebrochen
- **INAKTIV**: Inaktiv (grau) - `isActive = false`

### 6.3 Zyklus/Einheit sperren

- Wenn es Verlauf gibt (Verlaufsdatensätze):
  - **CYCLE Typ**: Zyklus ist gesperrt, kann nicht bearbeitet werden
  - **METRIC Typ**: Einheit und Zyklus sind gesperrt, können nicht bearbeitet werden
- Zeigt Warnung an: "⚠️ Zyklus ist gesperrt, weil es Verlauf gibt" oder "⚠️ Einheit ist gesperrt, weil es Verlauf gibt"

### 6.4 Metrikbasierte Aufgabe bestätigen

- **Validierung**:
  - Aktueller Metrikwert muss ≥ letzter abgeschlossener Metrikwert sein
  - Wenn ungültig: Zeigt Fehler "Aktueller Metrikwert muss ≥ letzter abgeschlossener Metrikwert sein"
- **Automatische Aktualisierung**:
  - `lastMetricValue` = aktueller Wert
  - `nextMetricValue` = aktueller Wert + Zyklus
  - `lastCompletedDate` = heute
- **Ausgaben**:
  - Wenn `hasCost = true`: Zeigt "Verursachte Ausgabe?" Dialog nach erfolgreicher Bestätigung an
  - Navigiert zu "Ausgabe hinzufügen" Bildschirm mit `initialNote`, `initialCategoryId`, `todoHistoryId`

### 6.5 Benachrichtigungen

- **CYCLE Typ**: 
  - Benachrichtigungen werden geplant, wenn Aufgabe erstellt/bearbeitet wird
  - Benachrichtigungen werden abgebrochen, wenn Aufgabe deaktiviert oder gelöscht wird
  - Benachrichtigungen werden neu geplant, wenn reaktiviert (wenn `nextDueDate >= heute`)
- **METRIC Typ**: Keine Benachrichtigungen (MVP1)

### 6.6 Nächstes Fälligkeitsdatum berechnen

- **CYCLE Typ**: 
  - Nächstes Fälligkeitsdatum automatisch basierend auf Zyklus nach Bestätigung berechnet
  - Beispiel: Zyklus 3 Monate, Fälligkeitsdatum 01/03/2026 → Nach Bestätigung, nächstes Fälligkeitsdatum = 01/06/2026
- **METRIC Typ**: 
  - Nächstes fällig = aktueller Wert + Zyklus
  - Beispiel: Aktueller Wert 14.520 Meilen, Zyklus 3.000 Meilen → Nächstes fällig = 17.520 Meilen

## 7. Wichtige Hinweise

1. **Bestätigen Schaltfläche**:
   - **Zeitbasierte Aufgaben (CYCLE)**: Keine "Bestätigen" Schaltfläche in der Karte. Bestätigung wird nur im "Fällige Aufgaben" (Glockenliste) Bildschirm durchgeführt.
   - **Metrikbasierte Aufgaben (METRIC)**: Hat "Bestätigen" Schaltfläche in der Karte (nur angezeigt, wenn `isActive = true`).

2. **Glocken-Symbol**: Das Glocken-Symbol im Header navigiert zum "Fällige Aufgaben" (Glockenliste) Bildschirm, wo Benutzer fällige Aufgaben bestätigen können (nur für CYCLE Typ).

3. **Zyklus/Einheit sperren**: Wenn es Verlauf gibt, wird der Zyklus (CYCLE) oder die Einheit/Zyklus (METRIC) gesperrt und kann nicht bearbeitet werden, um Datenkonsistenz sicherzustellen.

4. **Metrik-Validierung**: Beim Bestätigen einer metrikbasierten Aufgabe muss der aktuelle Metrikwert ≥ letzter abgeschlossener Metrikwert sein. Wenn nicht, zeigt die App einen Fehler an und verhindert Bestätigung.

5. **Verursachte Ausgaben**: Wenn eine Aufgabe Ausgaben hat (`hasCost = true`), fragt die App nach erfolgreicher Bestätigung, ob Sie eine Ausgabe hinzufügen möchten. Wenn Sie "Ausgabe hinzufügen" wählen, füllt die App automatisch Notiz und Kategorie voraus.

6. **Aufgabe löschen**: Beim Löschen einer Aufgabe wird auch der gesamte zugehörige Verlauf gelöscht (Kaskadenlöschung). Benachrichtigungen werden ebenfalls abgebrochen.

7. **Deaktivieren**: Beim Deaktivieren einer CYCLE Typ Aufgabe werden Benachrichtigungen abgebrochen. Beim Reaktivieren werden Benachrichtigungen neu geplant (wenn `nextDueDate >= heute`).

8. **Premium-Zugang**: Dieses Modul erfordert Premium-Zugang. Wenn Sie kein Premium haben, zeigt die App einen Dialog an, der ein Upgrade anfordert.

