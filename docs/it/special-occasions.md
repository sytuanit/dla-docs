# Occasioni Speciali

## 1. Obiettivo

Il modulo **Occasioni Speciali** ti aiuta a:
- Gestire le occasioni speciali durante l'anno (compleanni, feste, ecc.)
- Creare liste di attività (fasi di preparazione)
- Allegare liste della spesa a ogni fase di preparazione
- Promemoria prima delle occasioni
- Monitoraggio dei progressi della preparazione

## 2. Quando usare

Usa questo modulo quando desideri:
- Gestire le occasioni speciali durante l'anno
- Prepararti per occasioni importanti
- Creare liste di attività
- Ricevere promemoria prima delle occasioni

## 3. Schermate associate

- Elenco delle occasioni speciali
- Aggiungere una nuova occasione speciale
- Dettagli dell'occasione e fasi di preparazione
- Aggiungere una fase di preparazione
- Selezionare una lista della spesa
- Creare una nuova lista della spesa

## 4. Utilizzo principale

### 4.1 Aggiungere un'occasione speciale

1. Vai a **Funzioni** → Seleziona **Occasioni Speciali**
2. Premi il pulsante **➕** (FAB)
3. Compila le informazioni:
   - **Nome dell'Occasione**: (es. "Compleanno di Mamma")
   - **Data**: Seleziona giorno/mese (DatePicker seleziona solo giorno/mese, non l'anno)
   - **Usa calendario lunare**: (Opzionale) Seleziona se desideri usare il calendario lunare
     - Se selezionato: Inserisci il giorno e il mese lunare, l'app calcola automaticamente la prossima data solare
   - **Ripeti**: Annualmente / Solo quest'anno
   - **Mostra notifica alle**: Seleziona l'ora (richiesto, es. 07:00)
   - **Nota**: Informazioni aggiuntive (opzionali)
4. (Opzionale) Aggiungi fasi di preparazione (vedi 4.2)
5. Premi **Salva**

### 4.2 Aggiungere una fase di preparazione

1. Quando aggiungi una nuova occasione: Premi **+ Aggiungi Fase** nella sezione "Fasi di Preparazione"
2. Oppure dai dettagli dell'occasione: Premi **+ Aggiungi Fase**
3. Compila le informazioni:
   - **Quando?**: "X giorni prima" o "Il giorno"
   - **Numero di giorni**: (se "X giorni prima" è selezionato) Inserisci il numero di giorni prima dell'occasione
   - **Mostra notifica alle**: Seleziona l'ora (richiesto)
   - **Ripeti quotidianamente fino al completamento**: (Opzionale) Seleziona se desideri promemoria quotidiani
   - **Contenuto**: Nome della fase (richiesto, es. "Comprare un regalo")
   - **Nota**: (Opzionale)
   - **Usa lista della spesa**: (Opzionale) Seleziona per collegare con una lista della spesa
4. Premi **Aggiungi** (o FAB "Applica")

### 4.3 Marcare una fase come completata

1. Vai ai dettagli dell'occasione speciale
2. Trova la fase da marcare
3. Premi sulla casella [ ] per passare a [✓]
4. Se c'è una lista della spesa, premi sul nome della lista della spesa per visualizzare gli elementi e selezionare/deselezionare

### 4.4 Visualizzare i progressi

1. Vai ai dettagli dell'occasione speciale
2. Visualizza la sezione "Riepilogo":
   - Fasi di preparazione: Numero totale di fasi
   - Completate: Numero di fasi marcate / Totale fasi
   - Stato: Non iniziato / In corso / Completato

## 5. Logica e regole

### 5.1 Dati del calendario lunare

- Puoi inserire sia date solari che lunari
- L'app calcola automaticamente la data solare corrispondente alla data lunare
- Supporta la ripetizione annuale secondo il calendario lunare

### 5.2 Ripetere

- **Annualmente**: L'occasione si ripete ogni anno (secondo il calendario solare o lunare)
  - Con calendario solare: Ogni anno calcola nextOccurDate basato su (giorno/mese) di solarDate
  - Con calendario lunare: Ogni anno converte dalla data lunare alla data solare corrispondente e aggiorna nextOccurDate
- **Solo quest'anno**: L'occasione è valida solo per l'anno corrente, non si ripete l'anno prossimo

### 5.3 Fasi di preparazione

- **Quando?**: Ha 2 opzioni:
  - **X giorni prima**: Ricorda X giorni prima della data dell'occasione (devi inserire il numero di giorni)
  - **Il giorno**: Ricorda alla data dell'occasione (non devi inserire il numero di giorni)
- **Mostra notifica alle**: Ora del promemoria (richiesto, formato HH:mm)
- **Ripeti quotidianamente fino al completamento**: Se attivato, la notifica si ripete quotidianamente fino a quando l'utente marca la fase come completata
- **Collega lista della spesa**: Ogni fase può allegare una lista della spesa per monitorare i progressi degli acquisti

### 5.4 Notifiche

- **Notifica dell'occasione principale**: Creata a `nextOccurDate + reminder_time`
  - Con occasione ANNUALE: La notifica viene ricreata quando l'app si avvia (basata su nextOccurDate appena calcolato)
  - Con occasione UNA VOLTA: La notifica viene creata una sola volta per il nextOccurDate attuale
- **Notifica della fase di preparazione**: Calcola la data del promemoria basata su:
  - `nextOccurDate` dell'occasione speciale
  - `reminderType` e `daysBefore` (se esiste)
  - `reminderTime`
- **Notifica di ripetizione**: Se `repeatDailyUntilComplete = true`:
  - Crea una notifica di ripetizione quotidiana
  - Usa `notificationGroupKey` per raggruppare le notifiche di ripetizione
  - Annullata automaticamente quando l'utente marca la fase come completata

## 6. Note importanti

- **Dati del calendario lunare**: 
  - L'app converte automaticamente al calendario solare per la visualizzazione
  - Trova la "PROSSIMA data solare nel futuro" rispetto alla data attuale
  - Anni futuri: Il sistema calcola sempre la data solare corrispondente da (giorno lunare, mese lunare) per ogni anno di nuovo
- **Ripetizione annuale**: 
  - L'occasione ricalcola automaticamente nextOccurDate l'anno prossimo
  - Con calendario lunare: Ogni anno converte dalla data lunare alla data solare corrispondente
- **Ora del promemoria**: 
  - Deve avere un valore (non può essere vuoto)
  - Deve avere un formato corretto HH:mm (00:00 - 23:59)
- **Lista della spesa**: 
  - La lista della spesa eliminata viene sempre visualizzata nella fase (ma non può essere modificata)
  - Puoi marcare la fase come completata anche se la lista della spesa non è completamente completata
- **Notifiche**: 
  - Devi attivare le notifiche nelle Impostazioni per ricevere i promemoria
  - Le notifiche di ripetizione vengono annullate automaticamente quando la fase è marcata come completata
- **Stato dell'occasione**:
  - **Non iniziato**: Tutte le fasi non sono completate (grigio)
  - **In corso**: Almeno 1 fase è completata, ma non tutte (blu)
  - **Completato**: Tutte le fasi sono completate (verde scuro)
  - Se l'occasione non ha fasi di preparazione: Lo stato viene calcolato secondo la data (Non iniziato / In corso / Completato)

