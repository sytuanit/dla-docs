# Bankkredite

## 1. Zweck

Das Modul **Bankkredite** hilft Ihnen bei der Verwaltung von Bankkrediten, einschließlich:
- Kreditbetrag, Zinssatz, Laufzeit verfolgen
- Zahlungsplan verwalten
- Zinsen nach Periode berechnen (falls zutreffend)
- Verspätungsgebühren verwalten
- Vorzeitige Ablösung (falls erforderlich)

## 2. Wann zu verwenden

Verwenden Sie dieses Modul, wenn Sie haben:
- Bankkredite
- Müssen Zahlungsplan verfolgen
- Möchten Zinsen und Gebühren berechnen
- Müssen Erinnerungen, wenn Zahlung fällig ist

## 3. Verwandte Bildschirme

- Kreditliste
- Neuen Kredit hinzufügen (4 Schritte)
- Kredit bearbeiten
- Kreditdetails und Zahlungsplan
- Vorzeitige Ablösung

## 4. Hauptverwendung

### 4.1 Neuen Kredit hinzufügen (4 Schritte)

#### Schritt 1: Grundinformationen

1. Gehen Sie zu **Funktionen** → Wählen Sie **Bankkredite**
2. Tippen Sie auf die **+** (FAB) Schaltfläche
3. Füllen Sie Informationen aus:
   - **Bank**: Wählen Sie Bank aus oder erstellen Sie neue
   - **Kreditname**: (z. B. "Wohnungsdarlehen")
   - **Kreditbetrag**: Kapitalbetrag
   - **Auszahlungsdatum**: Datum, an dem Geld erhalten wurde
   - **Laufzeit**: Anzahl der Jahre
   - **Zinstyp**: Werbezins/Schwankender Zinssatz oder Fester Zinssatz
4. Tippen Sie auf **Weiter**

#### Schritt 2: Zinssatz konfigurieren

**Wenn "Werbezins/Schwankender Zinssatz" ausgewählt:**
- Aktivieren Sie **Hat Werbezins** (falls zutreffend)
- Geben Sie **Werbemonate** und **Werbezins** ein
- Fügen Sie Perioden mit schwankendem Zinssatz hinzu:
  - Wählen Sie Jahr und Monatsbereich
  - Geben Sie Zinssatz ein (%/Jahr)
  - Wählen Sie **Schwankend** oder **Fest**

**Wenn "Fester Zinssatz" ausgewählt:**
- Geben Sie **Fester Zinssatz** ein (%/Jahr)

Tippen Sie auf **Weiter**

#### Schritt 3: Gebühren konfigurieren

1. Aktivieren Sie **Hat Verspätungsgebühr** (falls zutreffend)
2. Fügen Sie Gebührenperioden hinzu:
   - Wählen Sie Jahr und Monatsbereich
   - Geben Sie **Gebührensatz** ein (%/Jahr)
3. Tippen Sie auf **Weiter**

#### Schritt 4: Bestätigen und speichern

1. Informationen überprüfen:
   - Gesamtbetrag zu zahlen
   - Erwarteter Zahlungsplan
2. Tippen Sie auf **Speichern**

### 4.2 Kreditdetails anzeigen

1. Gehen Sie zur Kreditliste
2. Tippen Sie auf einen Kredit
3. Zeigen Sie Informationen an:
   - Grundinformationen
   - Zahlungsplan
   - Gezahlter Betrag / Verbleibend
   - Zinssatz und Gebühren

### 4.3 Zahlungsperiode als bezahlt markieren

1. Gehen Sie zu Kreditdetails
2. Finden Sie fällige Zahlungsperiode (Badge "Nicht bezahlt")
3. Tippen Sie auf **Als bezahlt markieren**
4. Füllen Sie Informationen aus:
   - **Tatsächliches Zahlungsdatum**: Datum bezahlt (Standard = heute)
   - **Tatsächlich gezahlte Zinsen**: Tatsächlich gezahlte Zinsen (Standard = geplante Zinsen)
   - **Notiz**: (optional)
5. Zeigen Sie **Gesamte tatsächliche Zahlung** automatisch berechnet an (Kapital + tatsächliche Zinsen)
6. Tippen Sie auf **Bestätigen**

### 4.4 Aktuellen Zinssatz aktualisieren

1. Gehen Sie zu Kreditdetails (nur angezeigt, wenn aktuell in Periode mit schwankendem Zinssatz)
2. Tippen Sie auf **Aktuellen Zinssatz aktualisieren**
3. Füllen Sie Informationen aus:
   - **Neuer Zinssatz**: Neuer Zinssatz (%/Jahr)
   - **Gültigkeitsdatum**: Datum, ab dem neuer Zinssatz angewendet wird (Standard = Anfang der aktuellen Periode)
   - **Notiz**: (optional)
4. Tippen Sie auf **Speichern**
5. Nicht bezahlte Perioden ab aktueller Periode werden mit neuem Zinssatz aktualisiert

### 4.5 Vorzeitige Ablösung

1. Gehen Sie zu Kreditdetails
2. Tippen Sie auf **Ablösungsbetrag berechnen**
3. **Schritt 1 - Vorauszahlungsinformationen eingeben:**
   - Wählen Sie Methode: **Teilzahlung** oder **Vollständige Ablösung**
   - Wählen Sie Vorauszahlungsdatum (Standard = heute)
   - Geben Sie Vorauszahlungsbetrag ein (bei Teilzahlung)
   - Zeigen Sie **Vorauszahlungsgebühr** automatisch berechnet an
4. Tippen Sie auf **Weiter**
5. **Schritt 2 - Optionen vergleichen:**
   - Zeigen Sie Vergleich zwischen "Keine Vorauszahlung" und "Vorauszahlung" an
   - Zeigen Sie Ergebnisse an: Zinsersparnis, Zeitreduzierung
6. Tippen Sie auf **Vorauszahlung bestätigen**

### 4.6 Kredit bearbeiten

1. Gehen Sie zu Kreditdetails
2. Tippen Sie auf **Bearbeiten** (nur Name, Notiz, Bank bearbeiten)
3. Bearbeiten Sie bearbeitbare Informationen:
   - **Kreditname**: Kann bearbeitet werden
   - **Bank**: Kann geändert werden
   - **Notiz**: Kann bearbeitet werden
   - **Kreditbetrag, Auszahlungsdatum, Laufzeit, Zinssatz**: Kann nur bearbeitet werden, wenn noch keine Zahlungen geleistet wurden
4. Tippen Sie auf **Speichern**

## 5. Beispiele & UI-Illustrationen

### LOAN-01: Neuen Kredit erstellen (Wohnungsdarlehen mit Werbezins)

**Ziel**: Neuen Kredit erstellen, um Wohnungsdarlehen, Werbezins und monatlichen Zahlungsplan zu verfolgen.

**Schritte**:
1. Gehen Sie zu **Funktionen** → Wählen Sie **Bankkredite**
2. Tippen Sie auf die **+** (FAB) Schaltfläche, um neuen Kredit hinzuzufügen
3. **Schritt 1 - Grundinformationen:**
   - Wählen Sie Bank: Deutsche Bank
   - Geben Sie Name ein: "Wohnungsdarlehen - Innenstadtwohnung"
   - Geben Sie Kreditbetrag ein: €180,000
   - Wählen Sie Auszahlungsdatum: 01/04/2023
   - Geben Sie Laufzeit ein: 10 Jahre (automatisch berechnet = 120 Perioden)
   - Wählen Sie Benachrichtigungszeiten: 10:00 und 19:00
   - Wählen Sie Zinstyp: "Tilgungssaldo"
   - Tippen Sie auf **Weiter**
4. **Schritt 2 - Zinssatz konfigurieren:**
   - Aktivieren Sie "Hat Werbezinsperiode"
   - Geben Sie ein: Erste 6 Monate @ 6.0%/Jahr
   - Fügen Sie nachfolgende Perioden hinzu:
     - Jahr 1 (Monate 7-12): 9.0%/Jahr, schwankend
     - Jahr 2 (Monate 13-24): 9.5%/Jahr, schwankend
     - Jahr 3 und weiter: 10.0%/Jahr, schwankend
   - Tippen Sie auf **Weiter**
5. **Schritt 3 - Vorauszahlungsgebühr konfigurieren:**
   - Aktivieren Sie "Vorauszahlungsgebühr anwenden"
   - Geben Sie Gebühren ein: Jahre 1-3: 2.0%, Jahre 4-5: 1.5%, Jahr 6+: 1.0%
   - Tippen Sie auf **Weiter**
6. **Schritt 4 - Bestätigen:**
   - Zusammenfassung überprüfen
   - Tippen Sie auf **Kredit erstellen**

**Ergebnis**: Kredit erfolgreich erstellt, 120-Perioden-Zahlungsplan automatisch erstellt, Benachrichtigungen geplant.

**Wireframe - Schritt 1: Grundinformationen**

```text
┌─────────────────────────────────────────┐
│ <  Kredit hinzufügen                              │
├─────────────────────────────────────────┤
│ Kreditname *                              │
│ [Wohnungsdarlehen - Innenstadtwohnung]        │
│                                          │
│ Bank *                                    │
│ [Deutsche Bank ▼] [+ Neu erstellen]       │
│                                          │
│ Kreditbetrag *                            │
│ [€180,000]                               │
│                                          │
│ Auszahlungsdatum *                      │
│ [01/04/2023] [📅]                        │
│                                          │
│ Kreditlaufzeit (Jahre) *                       │
│ [10] Jahre                               │
│ Hinweis: App berechnet automatisch = 120 Perioden  │
│                                          │
│ Benachrichtigungszeit 1 *                    │
│ [10:00] [🕐]                             │
│                                          │
│ Benachrichtigungszeit 2 *                    │
│ [19:00] [🕐]                             │
│                                          │
│ Zinstyp *                          │
│ ● Tilgungssaldo                      │
│ ○ Fester Zinssatz für gesamte Laufzeit             │
│                                          │
│ [WEITER] [ABBRECHEN]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-02: Kreditliste und Details anzeigen

**Ziel**: Übersicht der Kredite anzeigen, nach Status filtern, suchen und Details jedes Kredits anzeigen.

**Schritte**:
1. Gehen Sie zu **Funktionen** → Wählen Sie **Bankkredite**
2. Zeigen Sie Listenscreen mit Filtern "Aktiv" (Standard) und "Abgeschlossen" an
3. Wechseln Sie zwischen Filtern, um verschiedene Übersichten zu sehen
4. Verwenden Sie Suchleiste: Geben Sie "Innenstadt" ein
5. Tippen Sie auf Kredit, um Details anzuzeigen
6. Zeigen Sie Zahlungsplan mit bezahlten Perioden, aktueller Periode und zukünftigen Perioden an
7. Verwenden Sie Suchleiste im Zahlungsplan: Geben Sie "9/2024" ein

**Ergebnis**: Liste wird korrekt nach Filter angezeigt, Kreditdetails zeigen vollständige Informationen und Zahlungsplan.

**Wireframe - Kreditliste**

```text
┌─────────────────────────────────────────┐
│ <  Bankkreditverwaltung                 │
├─────────────────────────────────────────┤
│ [Aktiv] [Abgeschlossen]                    │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ Aktuelles Guthaben: €148,050          │  │
│ │ Gesamt ursprünglicher Kredit: €180,000      │  │
│ │ Gezahlte Zinsen: €1,548              │  │
│ │ Aktiv: 1 Kredit                     │  │
│ └─────────────────────────────────────┘  │
│                                          │
│ [🔍 Suchen (Kreditname, Bank)]            │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ [ICON] Deutsche Bank  [Aktiv]    │  │
│ │ Wohnungsdarlehen - Innenstadtwohnung      │  │
│ │ Guthaben: €148,050                   │  │
│ │ Ursprünglich: €180,000                 │  │
│ │ Fortschritt: 8 / 120 Perioden          │  │
│ │ Enddatum: 01/04/2033               │  │
│ └─────────────────────────────────────┘  │
│                                          │
│                                    [+]   │
└─────────────────────────────────────────┘
```

**Wireframe - Kreditdetails**

```text
┌─────────────────────────────────────────┐
│ <  Kreditdetails                         │
├─────────────────────────────────────────┤
│ [ICON] Deutsche Bank          [Bearbeiten]  │
│ Wohnungsdarlehen - Innenstadtwohnung           │
│ [Aktiv]                                 │
│                                          │
│ Ursprünglicher Kredit: €180,000                 │
│ Aktuelles Guthaben: €148,050               │
│ Bezahlte Perioden: 8 / 120                    │
│ Gezahlte Zinsen: €1,548                    │
│ Aktueller Zinssatz: 9.0%/Jahr        │
│                                          │
│ [Zinsen aktualisieren] [Ablösung berechnen]│
│                                          │
│ Zahlungsplan                         │
│ [🔍 Periode suchen (z. B. "5/2025")]     │
│                                          │
│ Periode 1 – 05/2023 [Bezahlt]                │
│ Gesamt: €1.94k • Kapital: €900 • Zinsen: €1.04k│
│                                          │
│ Periode 9 – 01/2024 [Nicht bezahlt]            │
│ Kapital: €900                        │
│ Zinsen: €1,035                        │
│ Gesamt: €1,935                            │
│ Fälligkeitsdatum: 15/01/2024                     │
│ [Als bezahlt markieren]                           │
│                                          │
│ Periode 10 – 02/2024 [Nicht fällig]            │
│ Gesamt: €1.94k • Kapital: €900 • Zinsen: €1.04k│
└─────────────────────────────────────────┘
```

---

### LOAN-03: Zahlungsperiode als bezahlt markieren (Zahlung erfassen)

**Ziel**: Zahlungsperiode als "Bezahlt" markieren, nachdem Zahlung an Bank geleistet wurde.

**Schritte**:
1. Gehen Sie zu Kreditdetails
2. Finden Sie aktuelle Periode (Periode 9) mit Badge "Nicht bezahlt"
3. Tippen Sie auf **Als bezahlt markieren**
4. Füllen Sie Informationen aus:
   - Tatsächliches Zahlungsdatum: 15/01/2024 (Standard = heute)
   - Tatsächlich gezahlte Zinsen: €1,035 (Standard = geplante Zinsen)
   - Notiz: (optional)
5. Zeigen Sie gesamte tatsächliche Zahlung automatisch berechnet an
6. Tippen Sie auf **Bestätigen**

**Ergebnis**: Periode 9 aktualisiert zu "Bezahlt", Guthaben verringert sich, bezahlte Perioden erhöhen sich, aktuelles Guthaben verringert sich.

**Wireframe - Als bezahlt markieren Dialog**

```text
┌─────────────────────────────────────────┐
│ Als bezahlt markieren                             │
├─────────────────────────────────────────┤
│ Periode 9 – 01/2024          [Nicht bezahlt]   │
│                                          │
│ Fälligkeitsdatum (geplant): 15/01/2024          │
│ Kapital (fest): €900                │
│                                          │
│ Tatsächliches Zahlungsdatum *                    │
│ [15/01/2024] [📅]                        │
│                                          │
│ Tatsächlich gezahlte Zinsen *                   │
│ [€1,035]                                 │
│ Hinweis: Geplante Zinsen: €1,035           │
│                                          │
│ Gesamte tatsächliche Zahlung =                   │
│   €900 (Kapital)                    │
│ + €1,035 (Tatsächliche Zinsen)              │
│ ────────────────────────────────        │
│ = €1,935                                 │
│                                          │
│ Notiz (optional)                          │
│ [€50 weniger bezahlt, Zinsreduzierung erhalten...]│
│                                          │
│ [ABBRECHEN] [BESTÄTIGEN]                       │
└─────────────────────────────────────────┘
```

---

### LOAN-04: Aktuellen Zinssatz aktualisieren (Wenn Bank schwankenden Zinssatz anpasst)

**Ziel**: Neuen Zinssatz aktualisieren, wenn Bank Anpassung des schwankenden Zinssatzes ankündigt.

**Schritte**:
1. Gehen Sie zu Kreditdetails
2. Zeigen Sie "Aktueller Zinssatz: 9.0%/Jahr" an
3. Tippen Sie auf **Aktuellen Zinssatz aktualisieren** (nur angezeigt, wenn aktuell in Periode mit schwankendem Zinssatz)
4. Füllen Sie Informationen aus:
   - Neuer Zinssatz: 10.5%/Jahr
   - Gültigkeitsdatum: 15/01/2024 (Standard = Anfang der aktuellen Periode)
   - Notiz: "Bank hat Zinssatz nach neuer Entscheidung angepasst"
5. Tippen Sie auf **Speichern**

**Ergebnis**: Aktueller Zinssatz aktualisiert, nicht bezahlte Perioden ab aktueller Periode werden mit neuem Zinssatz aktualisiert.

**Wireframe - Zinssatz aktualisieren Dialog**

```text
┌─────────────────────────────────────────┐
│ Aktuellen Zinssatz aktualisieren             │
├─────────────────────────────────────────┤
│ [ICON] Deutsche Bank                   │
│ Kreditname: Wohnungsdarlehen - Innenstadtwohnung│
│ Aktuelle Periode: Periode 9 – 01/2024       │
│ Status: [Aktiv]                         │
│ Periode: Schwankend (nach Werbeperiode)     │
│                                          │
│ Aktueller Zinssatz (anwendend):       │
│ [9.0] %/Jahr (nur lesen)                  │
│                                          │
│ Neuer Zinssatz (%/Jahr) *              │
│ [10.5] %/Jahr                            │
│                                          │
│ Gültigkeitsdatum *                         │
│ [15/01/2024] [📅]                        │
│                                          │
│ Notiz (optional)                          │
│ [Bank hat Zinssatz angepasst...]         │
│                                          │
│ • Neuer Zinssatz wird auf Perioden ab    │
│   aktueller Periode angewendet.   │
│ • Zuvor bezahlte Perioden bleiben unverändert. │
│                                          │
│ [ABBRECHEN] [SPEICHERN]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-05: Vorzeitige Ablösung (Teilzahlung zur Zinsreduzierung)

**Ziel**: Teil des Kredits vorzeitig ablösen, um gesamte zu zahlende Zinsen zu reduzieren und Kreditlaufzeit zu verkürzen.

**Schritte**:
1. Gehen Sie zu Kreditdetails
2. Tippen Sie auf **Ablösungsbetrag berechnen**
3. **Schritt 1 - Vorauszahlungsinformationen eingeben:**
   - Wählen Sie Methode: "Teilzahlung"
   - Wählen Sie Vorauszahlungsdatum: 15/01/2024
   - Geben Sie Vorauszahlungsbetrag ein: €72,000
   - Zeigen Sie Gebühr automatisch berechnet an: €1,440 (2.0%)
   - Tippen Sie auf **Weiter**
4. **Schritt 2 - Optionen vergleichen:**
   - Zeigen Sie Vergleich zwischen "Keine Vorauszahlung" und "Vorauszahlung €72,000" an
   - Zeigen Sie Ergebnisse an: €27,000 Zinsen sparen, 40 Perioden reduzieren
   - Tippen Sie auf **Vorauszahlung bestätigen**

**Ergebnis**: Guthaben verringert sich, Zahlungsplan neu berechnet, Anzahl der Perioden verringert sich, Enddatum früher.

**Wireframe - Schritt 1: Vorauszahlungsinformationen eingeben**

```text
┌─────────────────────────────────────────┐
│ <  Vorzeitige Ablösung                      │
├─────────────────────────────────────────┤
│ [ICON] Deutsche Bank                   │
│ Kreditname: Wohnungsdarlehen - Innenstadtwohnung│
│ Aktuelles Guthaben: €180,000                │
│ Aktuelle Periode: Periode 9 – 01/2024       │
│                                          │
│ Wie möchten Sie ablösen?              │
│ ● Teilzahlung                        │
│ ○ Vollständige Ablösung                        │
│                                          │
│ Vorauszahlungsdatum *                        │
│ [15/01/2024] [📅]                        │
│                                          │
│ Vorauszahlungsbetrag *                      │
│ [€72,000]                                │
│                                          │
│ Angewandter Gebührensatz: 2.0%                │
│ Gebühr: €1,440                          │
│                                          │
│ [WEITER]                                   │
└─────────────────────────────────────────┘
```

**Wireframe - Schritt 2: Optionen vergleichen**

```text
┌─────────────────────────────────────────┐
│ <  Optionen vergleichen                       │
├─────────────────────────────────────────┤
│ OPTION A: Keine Vorauszahlung                 │
│ ────────────────────────────────────────│
│ Gesamte Zinsen bezahlt bis heute:            │
│   €46,800                               │
│ Gesamte verbleibende Zinsen: €46,800       │
│ Verbleibende Perioden: 112 Perioden          │
│ Enddatum: 01/04/2033                    │
│                                          │
│ OPTION B: Vorauszahlung €72,000            │
│ ────────────────────────────────────────│
│ Vorauszahlungsgebühr: €1,440           │
│ Gesamte Zinsen bezahlt bis heute:            │
│   €48,240                               │
│ Gesamte verbleibende Zinsen: €19,800       │
│ Verbleibende Perioden: 72 Perioden           │
│ Enddatum: 01/04/2029                    │
│                                          │
│ VERGLEICHSERGEBNIS:                       │
│ • Zinsersparnis: €27,000             │
│ • Zeitreduzierung: 40 Perioden (~3.5 Jahre)│
│                                          │
│ [VORAUSZAHLUNG BESTÄTIGEN]                     │
└─────────────────────────────────────────┘
```

---

### LOAN-06: Kredit bearbeiten (Grundinformationen bearbeiten)

**Ziel**: Grundinformationen des Kredits (Name, Bank, Notiz) nach Beginn der Zahlungen bearbeiten.

**Schritte**:
1. Gehen Sie zu Kreditdetails
2. Tippen Sie auf **Bearbeiten** (nur Name, Notiz, Bank bearbeiten)
3. Bearbeiten Sie:
   - Kreditname: "Wohnungsdarlehen - Innenstadtwohnung - Einheit A1-1201"
   - (Optional) Bank ändern: Commerzbank
   - Notiz: "An neue Bank übertragen"
4. Zeigen Sie deaktivierte Felder an: Kreditbetrag, Auszahlungsdatum, Laufzeit, Zinssatz
5. Tippen Sie auf **Speichern**

**Ergebnis**: Grundinformationen aktualisiert, andere Informationen unverändert.

**Hinweis**: Wenn Kredit noch keine Zahlungen geleistet hat, können alle Informationen bearbeitet werden (Betrag, Laufzeit, Zinskonfiguration).

## 6. Logik & Regeln

### 6.1 Werbezins/Schwankender Zinssatz

- Kann Werbeperiode haben (niedrigerer Zinssatz)
- Nach Werbeperiode schwankt Zinssatz nach Periode
- Jede Periode kann **Schwankend** (marktbasiert) oder **Fest** sein

### 6.2 Verspätungsgebühren

- Gebühren werden nach %/Jahr berechnet
- Kann für jede Periode unterschiedlich konfiguriert werden
- Gebühren gelten nur, wenn Zahlung verspätet ist

### 6.3 Zahlungsplan

- App erstellt automatisch Zahlungsplan basierend auf:
  - Kreditbetrag
  - Zinssatz
  - Laufzeit
- Jede Zahlungsperiode umfasst: Kapital + Zinsen

### 6.4 Vorzeitige Ablösung

- Verbleibenden Betrag berechnen (Kapital + Zinsen + Gebühren falls vorhanden)
- Nach Ablösung ändert sich Kredit zu "Abgeschlossen" Status

### 6.5 Benachrichtigungen

- App sendet Erinnerungsbenachrichtigung, wenn Zahlung fällig ist
- Benachrichtigungszeit kann für jeden Kredit konfiguriert werden (`notificationTime1`, `notificationTime2`, Standard 10:00 und 19:00)

## 7. Wichtige Hinweise

- **Komplexe Zinssätze**: Dieses Modul unterstützt Zinssätze, die sich nach Periode ändern, erfordert sorgfältige Konfiguration
- **Kann nicht löschen, wenn Zahlungsplan existiert**: Wenn Zahlungsplan existiert, können Sie nur ablösen, nicht löschen
- **Vorzeitige Ablösung**: Kann zusätzliche Gebühren erfordern, hängt von Bankrichtlinie ab
- **Zahlungsplan**: Zahlungsplan wird automatisch berechnet, Sie können nicht direkt bearbeiten

