# Lista delle Attività

## 1. Obiettivo

Il modulo **Lista delle Attività** ti aiuta a gestire attività ricorrenti e monitorare i progressi di completamento, inclusi:
- Attività ricorrenti basate sul tempo (quotidiane/settimanali/mensili/annuali)
- Attività ricorrenti basate su metriche (miglia/ore/volte...)
- Promemoria alla scadenza
- Monitoraggio della cronologia di completamento
- Registrazione delle spese (se applicabile)

Questo modulo ti aiuta a non perdere mai attività importanti come la manutenzione dell'auto, la sostituzione dei filtri, i controlli periodici, ecc.

## 2. Quando usare

Usa questo modulo quando hai:
- Attività che si ripetono secondo un calendario (ad esempio, sostituire il filtro dell'acqua ogni 3 mesi)
- Attività che si ripetono in base a metriche (ad esempio, cambiare l'olio dell'auto ogni 3.000 miglia)
- Bisogno di promemoria automatici alla scadenza
- Desideri monitorare la cronologia di completamento
- Bisogno di registrare le spese associate

## 3. Schermate associate

- Schermata elenco attività
- Selezionare il tipo di attività (Basata sul tempo / Basata su metriche)
- Aggiungere una nuova attività
- Modificare un'attività
- Confermare un'attività basata su metriche
- Cronologia delle attività
- Lista delle attività da fare (lista campanello)

## 4. Utilizzo principale

### 4.1 Aggiungere un'attività basata sul tempo

1. Vai a **Funzioni** → Seleziona **Lista delle Attività**
2. Premi il pulsante **+** (FAB) in basso a destra
3. Seleziona **Attività basata sul tempo**
4. Compila le informazioni:
   - **Nome dell'attività**: (obbligatorio, ad esempio "Sostituire il filtro dell'acqua")
   - **Ciclo di ricorrenza**: Inserisci un numero e seleziona l'unità (Giorno/Settimana/Mese/Anno)
   - **Prossima data di scadenza**: Seleziona una data (consente solo di selezionare da domani)
   - **Ora del promemoria**: Seleziona un'ora (obbligatorio, ad esempio 08:00)
   - **Questa attività comporta spese**: (Opzionale) Seleziona se sono coinvolte spese
     - Se selezionato: Seleziona **Categoria** (obbligatorio)
   - **Nota**: Informazioni aggiuntive (opzionale)
5. Premi **Salva**

### 4.2 Aggiungere un'attività basata su metriche

1. Vai a **Funzioni** → Seleziona **Lista delle Attività**
2. Premi il pulsante **+** (FAB)
3. Seleziona **Attività basata su metriche**
4. Compila le informazioni:
   - **Nome dell'attività**: (obbligatorio, ad esempio "Cambiare l'olio dell'auto")
   - **Ciclo**: Inserisci un numero (ad esempio 3,000)
   - **Unità**: Inserisci l'unità (ad esempio "Miglia")
   - **Ultimo valore metrico completato**: Inserisci il valore attuale (ad esempio 12,500)
   - **Questa attività comporta spese**: (Opzionale) Seleziona se sono coinvolte spese
     - Se selezionato: Seleziona **Categoria** (obbligatorio)
   - **Nota**: Informazioni aggiuntive (opzionale)
5. Premi **Salva**

### 4.3 Confermare un'attività basata su metriche

1. Vai all'elenco delle attività
2. Trova l'attività basata su metriche (tipo METRIC) da confermare
3. Premi il pulsante **Conferma** nella carta (mostrato solo quando `isActive = true`)
4. Compila le informazioni:
   - **Valore metrico attuale**: Inserisci il valore attuale (obbligatorio, deve essere ≥ ultimo valore metrico completato)
   - **Nota**: (Opzionale)
5. Visualizza il **Delta** calcolato automaticamente (valore attuale - ultimo valore completato)
6. Premi **Confermato**
7. (Se l'attività ha spese) Seleziona **Aggiungi una spesa** o **Annulla**

**Nota**: Le attività basate sul tempo (tipo CYCLE) non hanno un pulsante "Conferma" nella carta. La conferma avviene solo nella schermata "Attività da fare" (lista campanello).

## 5. Logica e regole

### 5.1 Tipi di attività

- **Basata sul tempo (tipo CYCLE)**:
  - Si ripete secondo un calendario (Giorno/Settimana/Mese/Anno)
  - Ha notifiche di promemoria alla scadenza
  - La conferma avviene solo nella schermata "Attività da fare" (lista campanello)
  - Nessun pulsante "Conferma" nella carta

- **Basata su metriche (tipo METRIC)**:
  - Si ripete in base a traguardi metrici (Miglia/Ore/Volte/Altro)
  - Nessuna notifica (MVP1)
  - Ha un pulsante "Conferma" nella carta (mostrato solo quando `isActive = true`)
  - Conferma inserendo il valore metrico attuale

### 5.2 Stato delle attività

- **IN ATTESA**: In arrivo (non ancora scaduta)
  - Nessun badge mostrato: `nextDueDate - today > 7 giorni`
  - Mostra badge "In arrivo" (giallo): `0 < nextDueDate - today ≤ 7 giorni`
- **IN RITARDO**: In ritardo (rosso) - `nextDueDate < today` e non confermato
- **NON COMPLETATA**: Non fatta (arancione) - Scaduta ma non confermata
- **COMPLETATA**: Completata (verde) - Confermata
- **ANNULLATA**: Annullata (grigio) - Questa occorrenza è stata annullata
- **INATTIVA**: Inattiva (grigio) - `isActive = false`

### 5.3 Bloccare Ciclo/Unità

- Se c'è una cronologia (record di cronologia):
  - **Tipo CYCLE**: Il ciclo è bloccato, non può essere modificato
  - **Tipo METRIC**: L'unità e il ciclo sono bloccati, non possono essere modificati
- Mostra avviso: "⚠️ Il ciclo è bloccato perché c'è una cronologia" o "⚠️ L'unità è bloccata perché c'è una cronologia"

### 5.4 Confermare un'attività basata su metriche

- **Validazione**:
  - Il valore metrico attuale deve essere ≥ ultimo valore metrico completato
  - Se non valido: Mostra errore "Il valore metrico attuale deve essere ≥ ultimo valore metrico completato"
- **Aggiornamento automatico**:
  - `lastMetricValue` = valore attuale
  - `nextMetricValue` = valore attuale + ciclo
  - `lastCompletedDate` = oggi
- **Spese**:
  - Se `hasCost = true`: Mostra il dialogo "Spesa sostenuta?" dopo conferma riuscita
  - Naviga alla schermata "Aggiungi una spesa" con `initialNote`, `initialCategoryId`, `todoHistoryId`

### 5.5 Notifiche

- **Tipo CYCLE**:
  - Le notifiche sono programmate quando crei/modifichi l'attività
  - Le notifiche vengono annullate quando disattivi o elimini l'attività
  - Le notifiche vengono riprogrammate quando riattivi (se `nextDueDate >= today`)
- **Tipo METRIC**: Nessuna notifica (MVP1)

## 6. Note importanti

1. **Pulsante Conferma**:
   - **Attività basate sul tempo (CYCLE)**: Nessun pulsante "Conferma" nella carta. La conferma avviene solo nella schermata "Attività da fare" (lista campanello).
   - **Attività basate su metriche (METRIC)**: Ha un pulsante "Conferma" nella carta (mostrato solo quando `isActive = true`).

2. **Icona campanello**: L'icona campanello nell'intestazione naviga alla schermata "Attività da fare" (lista campanello) dove gli utenti possono confermare le attività da fare (solo per il tipo CYCLE).

3. **Bloccare Ciclo/Unità**: Se c'è una cronologia, il ciclo (CYCLE) o l'unità/ciclo (METRIC) sarà bloccato e non può essere modificato per garantire la coerenza dei dati.

4. **Validazione metrica**: Quando confermi un'attività basata su metriche, il valore metrico attuale deve essere ≥ ultimo valore metrico completato. Altrimenti, l'applicazione mostrerà un errore e impedirà la conferma.

5. **Spese sostenute**: Se un'attività ha spese (`hasCost = true`), dopo conferma riuscita, l'applicazione chiederà se desideri aggiungere una spesa. Se scegli "Aggiungi una spesa", l'applicazione compilerà automaticamente la nota e la categoria.

6. **Eliminare un'attività**: Quando elimini un'attività, anche tutta la cronologia associata verrà eliminata (eliminazione a cascata). Le notifiche verranno anche annullate.

7. **Disattivare**: Quando disattivi un'attività di tipo CYCLE, le notifiche verranno annullate. Quando riattivi, le notifiche verranno riprogrammate (se `nextDueDate >= today`).

8. **Accesso Premium**: Questo modulo richiede accesso Premium. Se non hai Premium, l'applicazione mostrerà un dialogo che richiede un aggiornamento.

