# Spese Quotidiane

## 1. Obiettivo

Il modulo **Spese Quotidiane** ti aiuta a registrare le spese regolari non fisse come:
- Cibo e ristoranti
- Shopping
- Trasporti
- Intrattenimento
- Altre spese flessibili

A differenza delle **Spese Ricorrenti**, le spese quotidiane spesso variano in importo e frequenza, senza un ciclo fisso.

## 2. Quando usare

Usa questo modulo se desideri:
- Registrare spese casuali non ricorrenti
- Monitorare le spese quotidiane per controllare il budget
- Analizzare le tendenze delle spese per categoria
- Visualizzare le spese totali in un periodo

## 3. Schermate associate

- Elenco delle spese quotidiane
- Aggiungere una nuova spesa
- Modificare una spesa

## 4. Utilizzo principale

### 4.1 Aggiungere una spesa quotidiana

1. Vai a **Funzioni** → Seleziona **Spese Quotidiane**
2. Premi il pulsante **➕** (FAB) in basso a destra
3. Compila le informazioni:
   - **Categoria**: Seleziona una categoria (o usa la categoria predefinita, se configurata)
   - **Importo**: Inserisci l'importo speso
   - **Data**: Seleziona la data della spesa (predefinito oggi)
   - **Nota**: Descrizione dettagliata (opzionale)
4. Premi **Salva**

### 4.2 Visualizzare l'elenco delle spese

1. Vai a **Funzioni** → Seleziona **Spese Quotidiane**
2. L'elenco viene visualizzato secondo la configurazione di visualizzazione (2, 3 o 4 colonne)
3. Usa la **Ricerca** per filtrare per categoria o nota
4. Seleziona il **Filtro temporale**: Oggi / Questa settimana / Questo mese / Mese scorso / Personalizzato

### 4.3 Modificare una spesa

1. Vai all'elenco delle spese quotidiane
2. Premi a lungo sull'elemento da modificare
3. Seleziona **Modifica** nel menu
4. Aggiorna le informazioni
5. Premi **Salva**

### 4.4 Eliminare una spesa

1. Vai all'elenco delle spese quotidiane
2. Premi a lungo sull'elemento da eliminare
3. Seleziona **Elimina** nel menu
4. Conferma l'eliminazione

### 4.5 Impostare una categoria predefinita

1. Vai a **Impostazioni** → **Categorie** → **Categorie spese quotidiane**
2. Premi sulla categoria che desideri impostare come predefinita
3. Seleziona **Imposta come predefinita**
4. Quando aggiungi una nuova spesa, questa categoria sarà automaticamente selezionata

## 5. Illustrazioni UI (Wireframe)

### 5.1 Schermata elenco

```text
┌─────────────────────────────────────────┐
│  ← Indietro    Spese Quotidiane               │
├─────────────────────────────────────────┤
│  [🔍 Cerca...]                         │
│  [Oggi ▼] [Questa settimana] [Questo mese]    │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Cibo│ │Shopping│ │ Taxi │            │
│  │ uscita  │ │      │ │      │            │
│  │      │ │      │ │      │            │
│  │ €1.80│ │ €7.20│ │ €0.90│            │
│  │      │ │      │ │      │            │
│  │ 15/11│ │ 15/11│ │ 14/11│            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Caffè│ │ Altro│ │      │            │
│  │     │ │      │ │      │            │
│  │      │ │      │ │      │            │
│  │ €0.90│ │ €3.60│ │      │            │
│  │      │ │      │ │      │            │
│  │ 13/11│ │ 12/11│ │      │            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  Totale : €14.40                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Schermata Aggiungi/Modifica

```text
┌─────────────────────────────────────────┐
│  ← Indietro    Aggiungi una spesa quotidiana            │
├─────────────────────────────────────────┤
│  Categoria *                              │
│  [Cibo uscita ▼]                            │
│                                         │
│  Importo *                                │
│  [€1.80]                                   │
│                                         │
│  Data *                                  │
│  [15/11/2024]                           │
│                                         │
│  Nota                                    │
│  [Pranzo con un amico]                     │
│                                         │
│  [Salva] [Annulla]                        │
└─────────────────────────────────────────┘
```

## 6. Logica e regole

### 6.1 Layout di visualizzazione

- Puoi configurare il numero di colonne: 2, 3 o 4 colonne
- Il layout viene salvato nelle impostazioni e si applica a tutti gli elenchi di spese

### 6.2 Filtro temporale

- **Oggi**: Mostra solo le spese di oggi
- **Questa settimana**: Dall'inizio della settimana a oggi
- **Questo mese**: Dall'inizio del mese a oggi
- **Mese scorso**: Mese precedente completo
- **Personalizzato**: Seleziona un periodo personalizzato

### 6.3 Ricerca

- Cerca in **Nome categoria** e **Nota**
- Insensibile alle maiuscole/minuscole
- Ricerca in tempo reale durante la digitazione

### 6.4 Categoria predefinita

- Se hai impostato una categoria predefinita, sarà automaticamente selezionata all'apertura della schermata di aggiunta
- La nota può anche essere compilata automaticamente in base alla categoria (se configurata)

### 6.5 Spese totali

- Le spese totali vengono calcolate in base al filtro temporale attualmente selezionato
- Visualizzate alla fine dell'elenco

## 7. Note importanti

- **Nessun ciclo**: Le spese quotidiane non hanno un ciclo automatico, devi inserirle manualmente ogni volta
- **Possono essere eliminate**: Puoi eliminare qualsiasi spesa (a differenza delle spese ricorrenti)
- **Nessuna integrazione con il budget**: Le spese quotidiane non vengono calcolate automaticamente nel budget (devi monitorarle tu stesso)
- **Categorie personalizzate**: Puoi creare nuove categorie nelle impostazioni

