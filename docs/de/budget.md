# Budget

## 1. Zweck

Das Modul **Budget** hilft Ihnen bei der Planung und Verfolgung monatlicher Ausgaben und stellt sicher, dass Sie Ihr gesetztes Budget nicht überschreiten. Dieses Modul berechnet automatisch basierend auf:
- Ihrem wiederkehrenden Einkommen
- Ihren wiederkehrenden Ausgaben
- Tatsächlichen täglichen Ausgaben

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie möchten:
- Monatliche Ausgaben planen
- Kontrollieren, Budget nicht zu überschreiten
- Sparrate verfolgen
- Ausgabenanalyse nach Kategorie anzeigen
- Budgets zwischen Monaten vergleichen

## 3. Verwandte Bildschirme

- Budget erstellen (erstes Mal oder von vorherigem Monat kopieren)
- Budget-Übersicht anzeigen
- Budget-Verlauf nach Monat
- Kopiervorschlag von vorherigem Monat

## 4. Hauptverwendung

### 4.1 Budget erstes Mal erstellen (Fall A)

1. Gehen Sie zu **Funktionen** → Wählen Sie **Budget**
2. Wenn kein Budget existiert, öffnet App automatisch **Budget erstellen** Bildschirm
3. App berechnet und zeigt automatisch an:
   - **Wiederkehrendes Einkommen**: Gesamt aus allen aktiven wiederkehrenden Einkommen (nur lesen, zeigt detaillierte Aufschlüsselung)
   - **Wiederkehrende Ausgaben**: Gesamt aus allen aktiven wiederkehrenden Ausgaben (nur lesen, zeigt detaillierte Aufschlüsselung)
   - **Gesamtbudget (vor Ersparnissen)**: Auto berechnet = Wiederkehrendes Einkommen - Wiederkehrende Ausgaben
4. Geben Sie **Sparrate** ein: % Ersparnisse (0-100%, erforderlich)
5. Zeigen Sie **Ersparnisbetrag** und **Ausgabenbudget** automatisch berechnet an
6. Tippen Sie auf **Budget speichern**

### 4.2 Budget von vorherigem Monat kopieren (Fall C)

1. Gehen Sie zu **Funktionen** → Wählen Sie **Budget**
2. Wenn aktueller Monat kein Budget hat, aber vorheriger Monat hat, zeigt App **Budget kopieren Vorschlag** Bildschirm
3. Wählen Sie eine der Optionen:
   - **Gesamtes Budget des vorherigen Monats kopieren**: App kopiert automatisch Sparrate, berechnet wiederkehrendes Einkommen/Ausgaben aus aktuellen Daten neu und erstellt Budget sofort
   - **Kopieren & Anpassen**: App navigiert zu Budget erstellen Bildschirm mit Sparrate vorausgefüllt vom vorherigen Monat, Sie können vor dem Speichern anpassen
   - **Neues Budget erstellen**: Budget erstellen Ablauf von Grund auf ausführen (Fall A)
4. Wenn "Kopieren & Anpassen" gewählt, Sparrate bei Bedarf anpassen
5. Tippen Sie auf **Budget speichern**

**Hinweis**: Beim Kopieren werden Wiederkehrendes Einkommen und Wiederkehrende Ausgaben aus aktuellen wiederkehrenden Daten neu berechnet (nicht vom vorherigen Monat kopiert), nur Sparrate wird kopiert.

### 4.3 Budget-Übersicht anzeigen (Fall B)

1. Gehen Sie zu **Funktionen** → Wählen Sie **Budget**
2. Wenn aktueller Monat Budget hat, öffnet App **Übersicht** Bildschirm
3. Informationen anzeigen:
   - **Ausgabenbudget**: Gesetztes Ausgabenlimit
   - **Verwendet**: Ausgegebener Betrag (einschließlich täglicher Ausgaben und Einkommens-/Ausgabenabweichungen)
   - **Verbleibend**: Verbleibender Betrag im Budget
   - **Nutzungsrate**: % verwendetes Budget (mit Warnfarben)
   - **Einkommens- & Ausgabenabweichungen vom Plan**: Abweichungen vom ursprünglichen Plan
   - **Tägliche Ausgaben nach Kategorie**: Detaillierte Ausgabenanalyse nach Kategorie

### 4.4 Budget des aktuellen Monats bearbeiten

1. Auf **Budget-Übersicht** Bildschirm, tippen Sie auf **"Budget bearbeiten"** Schaltfläche
2. App zeigt Bearbeitungsbildschirm mit:
   - **Wiederkehrendes Einkommen** und **Wiederkehrende Ausgaben**: Alte Werte behalten (nur lesen)
   - **Sparrate**: Vorausgefüllt aus aktuellem Budget (kann bearbeitet werden)
3. Sparrate bei Bedarf ändern
4. Zeigen Sie Ersparnisbetrag und Ausgabenbudget automatisch aktualisiert an
5. Tippen Sie auf **"Budget speichern"**

**Hinweis**: Beim Bearbeiten werden Wiederkehrendes Einkommen und Wiederkehrende Ausgaben nicht neu berechnet (alte Momentaufnahme behalten), nur Sparrate und Ausgabenbudget werden aktualisiert.

### 4.5 Budget-Verlauf anzeigen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Budget**
2. Wählen Sie **Verlauf** aus dem Menü
3. Zeigen Sie Liste der Budgets für vergangene Monate an
4. Tippen Sie auf einen Monat, um Details anzuzeigen

### 4.6 Ausgabendetails nach Kategorie anzeigen

1. Gehen Sie zum **Budget-Übersicht** Bildschirm
2. Scrollen Sie nach unten zu **Analyse nach Kategorie** Abschnitt
3. Tippen Sie auf eine Kategorie
4. Zeigen Sie Liste der Ausgaben in dieser Kategorie an

## 5. Beispiele & UI-Illustrationen

### 5.1 BUDGET-01: Budget erstes Mal für aktuellen Monat erstellen

**Ziel**: Budget erstes Mal erstellen, damit App automatisch monatliche Ausgaben basierend auf Einkommen und wiederkehrenden Ausgaben berechnet und verfolgt.

**Schritte**:
1. Gehen Sie zum Funktionsbildschirm, wählen Sie "Budgetverwaltung"
2. App erkennt automatisch kein Budget und zeigt "Budget erstellen" Bildschirm
3. Zeigen Sie automatisch berechnete Informationen an: Wiederkehrendes Einkommen, Wiederkehrende Ausgaben, Gesamtbudget (vor Ersparnissen)
4. Geben Sie Sparrate ein: 20
5. Zeigen Sie Ersparnisbetrag und Ausgabenbudget automatisch berechnet an
6. Tippen Sie auf "Budget speichern" Schaltfläche

**Ergebnis**: Budget für aktuellen Monat gespeichert, navigiert automatisch zu "Budget-Übersicht" Bildschirm.

**UI-Illustration**:

```text
[ Karte: Budget November 2025 erstellen ]
+------------------------------------------------+
||                                                |
|| Wiederkehrendes Einkommen                €1,080         |
||  • Mein Gehalt (Monatlich)         €1,080         |
||                                                |
|| Wiederkehrende Ausgaben              €824          |
||  • Strom (Monatlich)          €31        |
||  • Wasser (Monatlich)                €15        |
||  • Studiengebühren für BN (Monatlich)       €245       |
||  • Frühstück & Kaffee (Wöchentlich x 4) €32       |
||  • Wohnungsdarlehen (Monatlich)     €378      |
||                                                |
|| (Diese Daten werden automatisch abgerufen)        |
+------------------------------------------------+

[ Karte: Gesamtbudget (vor Ersparnissen) ]
 ------------------------------------------------
||   €1,080 (Wiederkehrendes Einkommen)                   |
|| - €824 (Wiederkehrende Ausgaben)                    |
||-----------------------------------------------|
|| = €256 EUR                                     |
 ------------------------------------------------

[ Karte: Sparrate ]
 ------------------------------------------------
|| Wie viel möchten Sie sparen?                 |
||                                                |
|| Sparrate (%)                               |
|| [  Eingabe (erforderlich): 20  ]                    |
||                                                |
|| → Entspricht: €51                              |
 ------------------------------------------------

[ Karte: Ausgabenbudget ]
 ------------------------------------------------
||    €256 (Gesamtbudget (vor Ersparnissen))       |
|| -  €51 (Ersparnisbetrag)                        |
||-----------------------------------------------|
|| = €204 EUR                                     |
||                                                |
|| (Enthält Essen, Transport, Kaffee, kleine Einkäufe...)
 ------------------------------------------------

[ Schaltfläche ]
 -------------------------------
||      Budget speichern              |
 -------------------------------
```

---

### 5.2 BUDGET-02: Budget-Übersicht des aktuellen Monats anzeigen

**Ziel**: Ausgabensituation im Vergleich zum gesetzten Budget anzeigen, einschließlich verwendeter Beträge, verbleibender Beträge und Analyse nach Kategorie.

**Schritte**:
1. Gehen Sie zum Funktionsbildschirm, wählen Sie "Budgetverwaltung"
2. App erkennt automatisch Budget existiert und zeigt "Budget-Übersicht" Bildschirm
3. Zeigen Sie Karte 1 - Monatliches Budget an: Ausgabenbudget, Verwendet, Verbleibend, Nutzungsrate
4. Zeigen Sie Karte 2 - Einkommens- & Ausgabenabweichungen vom Plan an
5. Zeigen Sie Karte 3 - Tägliche Ausgaben nach Kategorie an
6. (Optional) Klicken Sie auf "Ausgabenbudget ›", um detaillierten Dialog mit Budgetberechnung anzuzeigen

**Ergebnis**: Zeigt vollständige Budgetinformationen des aktuellen Monats mit Fortschrittsring/-balken und angemessenen Farben an.

**UI-Illustration**:

```text
[ Karte 1 – Budget November 2025 ]
┌──────────────────────────────────────────────┐
│ Budget November 2025                         │
│                                             │
│ Ausgabenbudget ›      €204                 │
│ Verwendet                  €32                   │
│  • Tägliche Ausgaben              €43          │   
│  • Einkommensabweichung      -€144              │
│  • Ausgabenabweichung       +€7               │
│ Verbleibend              €94                 │
│                                             │
│                    15.4%                    │
│   (Sie haben 15.4% des Ausgabenbudgets dieses Monats verwendet)
│   (Sie sind dabei, das Ausgabenbudget dieses Monats aufzubrauchen)
│                                             │
│                               [Verlauf anzeigen]│
└──────────────────────────────────────────────┘

[ Karte 2 – Einkommens- & Ausgabenabweichungen vom Plan ]
┌──────────────────────────────────────────────┐
│ Einkommens- & Ausgabenabweichungen vom Plan        │
│                                              │
│ Wiederkehrendes Einkommen                             │
│  • Mein Gehalt                 +€72           │
│    (€432 > €360)                             │
│                                              │
│ Wiederkehrende Ausgaben                           │
│  • Studiengebühren für BN              -€4          │
│    (€245 > €252)                             │
│                                              │
│ Gesamte Einkommensabweichung:        +€216          │
│ Gesamte Ausgabenabweichung:        -€7          │
└──────────────────────────────────────────────┘

[ Karte 3 – Tägliche Ausgaben nach Kategorie ]
┌──────────────────────────────────────────────┐
│ Tägliche Ausgaben nach Kategorie                   │
│ (Essen, Transport, Kaffee, kleine Einkäufe...)
│                                             │
│ Gesamte tägliche Ausgaben: €43                    │
│                                             │
│ Essen              €22    50% [█████---------]│
│ Transport     €11    25% [███-----------]│
│ Kaffee             €7     17% [██------------]│
│ Kleine Einkäufe     €4     8%  [█-------------]│
└──────────────────────────────────────────────┘
```

---

### 5.3 BUDGET-03: Budget des aktuellen Monats bearbeiten

**Ziel**: Sparrate anpassen, um Ausgabenbudget für aktuellen Monat zu ändern.

**Schritte**:
1. Auf "Budget-Übersicht" Bildschirm, tippen Sie auf "Budget bearbeiten" Schaltfläche
2. App zeigt Bearbeitungsbildschirm (ähnlich wie Budget erstellen Bildschirm)
3. Zeigen Sie aktuelle Informationen an: Wiederkehrendes Einkommen, Wiederkehrende Ausgaben (alte Werte behalten)
4. Ändern Sie Sparrate auf 25
5. Zeigen Sie Ersparnisbetrag und Ausgabenbudget automatisch aktualisiert an
6. Tippen Sie auf "Budget speichern" Schaltfläche

**Ergebnis**: Budget aktualisiert, kehrt zu "Budget-Übersicht" Bildschirm mit neuen Werten zurück.

**UI-Illustration**: Ähnlich wie BUDGET-01 (Budget erstellen Bildschirm), aber Wiederkehrendes Einkommen und Wiederkehrende Ausgaben Werte sind nur lesen und vom alten Budget behalten.

---

### 5.4 BUDGET-04: Budget von vorherigem Monat kopieren, wenn neuer Monat beginnt

**Ziel**: Budget des vorherigen Monats wiederverwenden, um Zeit beim Erstellen neues Budget zu sparen, mit Option zur Anpassung bei Bedarf.

**Schritte**:
1. Gehen Sie zum Funktionsbildschirm, wählen Sie "Budgetverwaltung"
2. App erkennt automatisch aktueller Monat hat kein Budget, aber vorheriger Monat hat, zeigt "Budget kopieren Vorschlag" Bildschirm
3. Wählen Sie "Kopieren & Anpassen"
4. App navigiert zu Budget erstellen Bildschirm mit Sparrate vorausgefüllt vom vorherigen Monat
5. (Optional) Sparrate bei Bedarf anpassen
6. Tippen Sie auf "Budget speichern" Schaltfläche

**Ergebnis**: Neues Budget für aktuellen Monat erstellt, navigiert automatisch zu "Budget-Übersicht" Bildschirm.

**UI-Illustration**:

```text
[ BILDSCHIRM ]  Budget Dezember 2025
┌──────────────────────────────────────────────┐
│ Dezember 2025 hat kein Budget                 │
│                                              │
│ Wie möchten Sie das Budget des neuen Monats erstellen?│
├──────────────────────────────────────────────┤
│                                              │
│ 📝 Kopieren & Anpassen ›                          │
│    Hinweis: Budget November 2025 kopieren und anpassen│
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│ ➕ Neues Budget erstellen ›                      │
│   Hinweis: Budget erstellen Ablauf erneut ausführen        │
│                                              │
└──────────────────────────────────────────────┘
```

Nach Auswahl von "Kopieren & Anpassen" wird der Budget erstellen Bildschirm ähnlich wie BUDGET-01 angezeigt, aber Sparrate ist vom vorherigen Monat vorausgefüllt.

## 6. Logik & Regeln

### 6.1 Fälle

- **Fall A**: Budget erstes Mal erstellen (kein Budget für irgendeinen Monat)
- **Fall B**: Aktueller Monat hat Budget → Übersicht anzeigen
- **Fall C**: Aktueller Monat hat keins, aber vorheriger Monat hat → Kopiervorschlag

### 6.2 Automatische Berechnung

- **Wiederkehrendes Einkommen**: Gesamt aus allen aktiven `recurring_income`
- **Wiederkehrende Ausgaben**: Gesamt aus allen aktiven `recurring_expense`
- **Tägliche Ausgaben**: Gesamt aus `daily_expense` im Monat
- **Gesamtbudget**: Wiederkehrendes Einkommen + Zusatzeinkommen
- **Ersparnisse**: Gesamtbudget × Sparrate

### 6.3 Integration mit anderen Modulen

- Beim Bestätigen wiederkehrendes Einkommen → Budget automatisch aktualisieren
- Beim Bestätigen wiederkehrende Ausgabe → Budget automatisch aktualisieren
- Tägliche Ausgaben werden automatisch in Budget berechnet

### 6.4 Budget überschritten Warnung

- App zeigt Warnung an, wenn Ausgaben Budget überschreiten
- Warnung wird auf Startbildschirm und in Benachrichtigungen angezeigt

### 6.5 Momentaufnahme

- Beim Erstellen des Budgets erstellt App Momentaufnahme von Einkommens-/Ausgabenelementen, um Zustand zu diesem Zeitpunkt zu speichern
- Momentaufnahme wird für Vergleich und Analyse verwendet

## 7. Wichtige Hinweise

- **Ein Budget pro Monat**: Sie müssen für jeden Monat Budget erstellen
- **Budget bearbeiten**: Sie können Budget des aktuellen Monats bearbeiten, indem Sie Sparrate ändern. Wiederkehrendes Einkommen und Wiederkehrende Ausgaben bleiben unverändert (Momentaufnahme), um Genauigkeit sicherzustellen
- **Automatische Aktualisierung**: Budget aktualisiert automatisch, wenn Sie Einkommen/Ausgaben bestätigen
- **Von vorherigem Monat kopieren**: Kopierfunktion hilft Ihnen, Zeit beim Erstellen des Budgets zu sparen

