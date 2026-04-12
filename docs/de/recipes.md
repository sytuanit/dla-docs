# Rezepte

## 1. Zweck

Im Modul **Rezepte** speichern Sie **Kochrezepte** (Gerichtname, Zutaten, Zubereitung), optional **Proteintypen**, **Sternebewertungen** und ordnen Gerichte in **Sammlungen**. Diese Daten werden für die **Speiseplanung** genutzt, wenn Sie Gerichte den Mahlzeiten der Woche zuweisen.

## 2. Wann nutzen?

- Persönliches Rezeptbuch zum Nachschlagen beim Kochen.
- Gerichte nach Thema gruppieren (z. B. Wochenende, Kinder) über **Sammlungen**.
- Sie möchten den **Speiseplan** nutzen — es werden zuerst Rezepte benötigt.

## 3. Zugehörige Bildschirme

- **Funktionen** → **Küche & Kulinarik** → **Rezepte**
- Register **Rezepte** / **Sammlungen**
- **Rezept hinzufügen** / **Rezept bearbeiten**
- **Sammlungsdetail** (Gerichte in der Sammlung, Rezepte hinzufügen)

## 4. Hauptbedienung

### 4.1 Liste und Suche

1. **Funktionen** → **Rezepte**.
2. Im Tab **Rezepte** **Rezepte suchen...** nutzen.
3. Tab **Sammlungen** mit eigener Suche.

### 4.2 Neues Rezept

1. **+** (FAB) tippen.
2. **Gerichtname** (Pflicht), optional **Proteintypen** (kommagetrennt), **Bewertung**, **Zutaten** (mind. eine Zeile), **Zubereitung**, **Sammlungen**.
3. **Speichern**.

### 4.3 Bearbeiten / Löschen

Rezept antippen; **Speichern**. **Löschen** mit Warnung, falls im **Speiseplan** verwendet.

### 4.4 Sammlungen

**Sammlungen** → **Neue Sammlung**; Sammlung öffnen → Rezepte hinzufügen; **Umbenennen** / **Löschen** (löscht keine Rezepte).

## 5. Beispiele & UI-Skizzen

### 5.1 RECIPE-01

**Ziel**: „Tom Yum“ speichern und der Sammlung „Thai“ zuordnen.

**Schritte**: Funktionen → Rezepte → **+** → ausfüllen → Sammlung **Thai** → Speichern.

```text
[ Rezepte ]  [ Sammlungen ]
[ Suche...________________________________ ]

┌──────────────────────────────────────────┐
│ Tom Yum                            [ x ] │
│ ★★★★☆  ·  Protein: Meeresfrüchte         │
│ 5 Zutaten  ·  Sammlung: Thai            │
└──────────────────────────────────────────┘
                                           [ + ]
```

### 5.2 RECIPE-02: Suche nach „Suppe“

```text
[ Suche...  suppe_______________________ ]
```

## 6. Logik & Regeln

- **Mindestens eine Zutat** erforderlich.
- Löschen eines im Speiseplan genutzten Gerichts mit Warnung.
- **Sammlungen** sind Gruppen; ein Gericht kann in mehreren sein.

## 7. Wichtige Hinweise

- **Premium**: Badge möglich unter **Funktionen**.
- Endbenutzer-Dokumentation ohne technische Pfade.
