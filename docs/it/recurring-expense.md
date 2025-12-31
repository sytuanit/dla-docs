# Spese Ricorrenti

## 1. Obiettivo

Il modulo **Spese Ricorrenti** ti aiuta a gestire le spese periodiche con cicli fissi come:
- Bollette di elettricità, acqua, gas
- Internet, TV via cavo
- Assicurazione
- Tasse scolastiche
- Affitto
- Altre spese ricorrenti

Questo modulo crea automaticamente **occorrenze** basate sul ciclo che configuri e ti ricorda quando il pagamento è dovuto.

## 2. Quando usare

Usa questo modulo se hai:
- Spese fisse secondo un programma (settimanale, bisettimanale o mensile)
- Bisogno di monitorare e confermare quando il pagamento è stato effettuato
- Desideri un calcolo automatico nel budget mensile

## 3. Schermate associate

- Elenco delle spese ricorrenti
- Aggiungere una nuova spesa ricorrente
- Modificare una spesa ricorrente
- Cronologia delle occorrenze

## 4. Utilizzo principale

### 4.1 Aggiungere una nuova spesa ricorrente

1. Vai a **Funzioni** → Seleziona **Spese Ricorrenti**
2. Premi il pulsante **➕** (FAB) in basso a destra
3. Compila le informazioni:
   - **Categoria**: Seleziona una categoria o creane una nuova
   - **Importo**: Inserisci l'importo della spesa (può essere lasciato vuoto, da inserire alla conferma)
   - **Ciclo**: Seleziona Settimanale / Bisettimanale / Mensile
   - **Data**: Seleziona la data nel ciclo (es. il 15 di ogni mese)
   - **Data di inizio**: (Solo per il ciclo bisettimanale) Seleziona la data di inizio
   - **Nota**: Informazioni aggiuntive (opzionale)
4. Premi **Salva**

### 4.2 Confermare il pagamento

1. Vai all'elenco delle spese ricorrenti
2. Trova l'elemento con il badge **"Conferma in attesa"** (giallo)
3. Premi sull'elemento per aprire il dialogo di conferma
4. Compila:
   - **Importo reale**: (se diverso da quello previsto)
   - **Nota**: (opzionale)
5. Premi **Conferma**

### 4.3 Modificare una spesa ricorrente

1. Vai all'elenco delle spese ricorrenti
2. Premi sull'elemento da modificare
3. Seleziona **Modifica** nel menu
4. Aggiorna le informazioni
5. Premi **Salva**

### 4.4 Visualizzare la cronologia

1. Vai all'elenco delle spese ricorrenti
2. Premi su un elemento
3. Seleziona **Cronologia** per visualizzare tutte le occorrenze passate

### 4.5 Disattivare/attivare una spesa

1. Vai all'elenco delle spese ricorrenti
2. Trova l'elemento da disattivare/attivare
3. Attiva/disattiva l'interruttore **Attivo** sul lato destro dell'elemento

## 5. Logica e regole

### 5.1 Ciclo e data

- **Settimanale**: Seleziona il giorno della settimana (1=Lunedì, 7=Domenica)
- **Bisettimanale**: Seleziona il giorno della settimana + data di inizio specifica
- **Mensile**: Seleziona il giorno del mese (1-31)

### 5.2 Creazione automatica delle occorrenze

- L'applicazione crea automaticamente **occorrenze** quando:
  - Aggiungi una nuova spesa
  - La data nel ciclo viene raggiunta
  - Inizia un nuovo mese

### 5.3 Stato delle occorrenze

- **IN ATTESA**: Conferma in attesa (mostra un badge giallo)
- **COMPLETATA**: Confermata (mostra un badge verde)
- **ANNULLATA**: Annullata (mostra un badge rosso)

### 5.4 Integrazione con il budget

- Quando confermi la spesa, l'applicazione aggiorna automaticamente il budget del mese corrente (se esiste)
- La spesa viene calcolata in "Spese Ricorrenti" nel budget

### 5.5 Notifiche

- L'applicazione invia una notifica di promemoria quando il pagamento è dovuto
- L'ora della notifica può essere configurata per ogni elemento (`notificationTime1`, `notificationTime2`, predefinito 16:00 e 19:00)

## 6. Note importanti

- **L'importo può essere lasciato vuoto**: Se non conosci l'importo esatto, puoi lasciarlo vuoto e inserirlo alla conferma
- **Non può essere eliminato se esistono occorrenze**: Se ci sono occorrenze, puoi solo disattivare (isActive = false), non eliminare
- **Conferma tardiva**: Puoi confermare occorrenze passate, l'applicazione ricalcola automaticamente il budget
- **Cambiare il ciclo**: Quando modifichi il ciclo, le occorrenze future vengono ricalcolate

