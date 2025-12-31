# Budget

## 1. Obiettivo

Il modulo **Budget** ti aiuta a pianificare e monitorare le spese mensili e assicura che non superi il budget stabilito. Questo modulo calcola automaticamente in base a:
- Le tue entrate ricorrenti
- Le tue spese ricorrenti
- Spese quotidiane effettive

## 2. Quando usare

Usa questo modulo se desideri:
- Pianificare le spese mensili
- Controllare che non superi il budget
- Monitorare il tasso di risparmio
- Vedere l'analisi delle spese per categoria
- Confrontare i budget tra i mesi

## 3. Schermate associate

- Creare un budget (prima volta o copiare dal mese precedente)
- Visualizzare il riepilogo del budget
- Cronologia del budget per mese
- Suggerimento di copia del mese precedente

## 4. Utilizzo principale

### 4.1 Creare un budget per la prima volta

1. Vai a **Funzioni** → Seleziona **Budget**
2. Se non esiste alcun budget, l'applicazione apre automaticamente la schermata **Crea Budget**
3. L'applicazione calcola e visualizza automaticamente:
   - **Entrate Ricorrenti**: Totale di tutte le entrate ricorrenti attive (sola lettura, mostra il dettaglio)
   - **Spese Ricorrenti**: Totale di tutte le spese ricorrenti attive (sola lettura, mostra il dettaglio)
   - **Budget Totale (prima del risparmio)**: Calcolato automaticamente = Entrate Ricorrenti - Spese Ricorrenti
4. Inserisci il **Tasso di Risparmio**: % di risparmio (0-100%, richiesto)
5. Visualizza l'**Importo di Risparmio** e il **Budget di Spese** calcolati automaticamente
6. Premi **Salva Budget**

### 4.2 Copiare il budget del mese precedente

1. Vai a **Funzioni** → Seleziona **Budget**
2. Se il mese corrente non ha un budget, ma il mese precedente ne ha uno, l'applicazione mostra la schermata **Suggerimento di Copia Budget**
3. Seleziona una delle opzioni:
   - **Copia tutto il budget del mese precedente**: L'applicazione copia automaticamente il tasso di risparmio, ricalcola le entrate/spese ricorrenti dai dati attuali e crea il budget immediatamente
   - **Copia e Modifica**: L'applicazione naviga alla schermata Crea Budget con il tasso di risparmio precompilato del mese precedente, puoi modificare prima di salvare
   - **Crea un Nuovo Budget**: Esegui il flusso di creazione del budget dall'inizio
4. Se "Copia e Modifica" è selezionato, modifica il tasso di risparmio se necessario
5. Premi **Salva Budget**

**Nota**: Durante la copia, le Entrate Ricorrenti e le Spese Ricorrenti vengono ricalcolate dai dati ricorrenti attuali (non copiate dal mese precedente), solo il tasso di risparmio viene copiato.

### 4.3 Visualizzare il riepilogo del budget

1. Vai a **Funzioni** → Seleziona **Budget**
2. Se il mese corrente ha un budget, l'applicazione apre la schermata **Riepilogo**
3. Visualizza le informazioni:
   - **Budget di Spese**: Limite di spesa stabilito
   - **Utilizzato**: Importo speso (incluso spese quotidiane e scostamenti entrate/spese)
   - **Rimanente**: Importo rimanente nel budget
   - **Tasso di Utilizzo**: % del budget utilizzato (con colori di avviso)
   - **Scostamenti Entrate e Spese dal Piano**: Deviazioni dal piano originale
   - **Spese Quotidiane per Categoria**: Analisi dettagliata delle spese per categoria

### 4.4 Modificare il budget del mese corrente

1. Nella schermata **Riepilogo Budget**, premi il pulsante **"Modifica Budget"**
2. L'applicazione mostra la schermata di modifica con:
   - **Entrate Ricorrenti** e **Spese Ricorrenti**: Valori vecchi conservati (sola lettura)
   - **Tasso di Risparmio**: Precompilato dal budget attuale (può essere modificato)
3. Modifica il tasso di risparmio se necessario
4. Visualizza l'importo di risparmio e il budget di spese aggiornati automaticamente
5. Premi **"Salva Budget"**

**Nota**: Durante la modifica, le Entrate Ricorrenti e le Spese Ricorrenti non vengono ricalcolate (l'istantanea vecchia viene conservata), solo il tasso di risparmio e il budget di spese vengono aggiornati.

## 5. Logica e regole

### 5.1 Calcolo automatico

- **Entrate Ricorrenti**: Totale di tutti i `recurring_income` attivi
- **Spese Ricorrenti**: Totale di tutte le `recurring_expense` attive
- **Spese Quotidiane**: Totale dei `daily_expense` del mese
- **Budget Totale**: Entrate Ricorrenti + Entrate Extra
- **Risparmio**: Budget Totale × Tasso di Risparmio

### 5.2 Integrazione con altri moduli

- Quando confermi un'entrata ricorrente → Aggiorna automaticamente il budget
- Quando confermi una spesa ricorrente → Aggiorna automaticamente il budget
- Le spese quotidiane vengono calcolate automaticamente nel budget

### 5.3 Avviso di superamento del budget

- L'applicazione mostra un avviso quando le spese superano il budget
- L'avviso viene mostrato nella schermata principale e nelle notifiche

## 6. Note importanti

- **Un budget per mese**: Devi creare un budget per ogni mese
- **Modificare il budget**: Puoi modificare il budget del mese corrente cambiando il tasso di risparmio. Le Entrate Ricorrenti e le Spese Ricorrenti rimangono invariate (istantanea), per garantire la precisione
- **Aggiornamento automatico**: Il budget si aggiorna automaticamente quando confermi entrate/spese
- **Copiare dal mese precedente**: La funzione di copia ti aiuta a risparmiare tempo durante la creazione del budget

