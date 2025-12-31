# Prestiti Bancari

## 1. Obiettivo

Il modulo **Prestiti Bancari** ti aiuta a gestire i prestiti bancari, inclusi:
- Monitorare l'importo del prestito, il tasso di interesse, la durata
- Gestire il calendario dei pagamenti
- Calcolare gli interessi per periodo (se applicabile)
- Gestire le penali per ritardo di pagamento
- Rimborso anticipato (se necessario)

## 2. Quando usare

Usa questo modulo quando hai:
- Prestiti bancari
- Bisogno di monitorare il calendario dei pagamenti
- Desideri calcolare interessi e penali
- Bisogno di promemoria quando il pagamento è in ritardo

## 3. Schermate associate

- Elenco dei prestiti
- Aggiungere un nuovo prestito (4 passaggi)
- Modificare un prestito
- Dettagli del prestito e calendario dei pagamenti
- Rimborso anticipato

## 4. Utilizzo principale

### 4.1 Aggiungere un nuovo prestito (4 passaggi)

#### Passaggio 1: Informazioni di base

1. Vai a **Funzioni** → Seleziona **Prestiti Bancari**
2. Premi il pulsante **+** (FAB)
3. Compila le informazioni:
   - **Banca**: Seleziona la banca o creane una nuova
   - **Nome del Prestito**: (es. "Prestito Ipotecario")
   - **Importo del Prestito**: Importo del capitale
   - **Data di Disbursamento**: Data in cui il denaro è stato ricevuto
   - **Durata**: Numero di anni
   - **Tipo di Interesse**: Tasso promozionale/variabile o Tasso fisso
4. Premi **Avanti**

#### Passaggio 2: Configurare il tasso di interesse

**Se selezioni "Tasso Promozionale/Variabile":**
- Attiva **Ha un Tasso Promozionale** (se applicabile)
- Inserisci **Mesi Promozionali** e **Tasso Promozionale**
- Aggiungi periodi di tasso variabile:
  - Seleziona l'anno e l'intervallo di mesi
  - Inserisci il tasso di interesse (%/anno)
  - Seleziona **Variabile** o **Fisso**

**Se selezioni "Tasso Fisso":**
- Inserisci **Tasso Fisso** (%/anno)

Premi **Avanti**

#### Passaggio 3: Configurare le penali

1. Attiva **Ha una Penale per Ritardo di Pagamento** (se applicabile)
2. Aggiungi periodi di penale:
   - Seleziona l'anno e l'intervallo di mesi
   - Inserisci **Tasso di Penale** (%/anno)
3. Premi **Avanti**

#### Passaggio 4: Confermare e salvare

1. Esamina le informazioni:
   - Importo totale da pagare
   - Calendario dei pagamenti previsto
2. Premi **Salva**

### 4.2 Visualizzare i dettagli del prestito

1. Vai all'elenco dei prestiti
2. Premi su un prestito
3. Vedi le informazioni:
   - Informazioni di base
   - Calendario dei pagamenti
   - Importo pagato / Rimanente
   - Tasso di interesse e penali

### 4.3 Marcare un periodo di pagamento come pagato

1. Vai ai dettagli del prestito
2. Trova il periodo di pagamento scaduto (badge "Non Pagato")
3. Premi **Marca come Pagato**
4. Compila le informazioni:
   - **Data di Pagamento Reale**: Data pagata (predefinito = oggi)
   - **Interessi Pagati Reali**: Interessi effettivamente pagati (predefinito = interessi pianificati)
   - **Nota**: (opzionale)
5. Vedi **Pagamento Totale Reale** calcolato automaticamente (capitale + interessi reali)
6. Premi **Conferma**

## 5. Logica e regole

### 5.1 Tasso Promozionale/Variabile

- Può avere un periodo promozionale (tasso di interesse più basso)
- Dopo il periodo promozionale, il tasso di interesse varia per periodo
- Ogni periodo può essere **Variabile** (basato sul mercato) o **Fisso**

### 5.2 Penali per Ritardo di Pagamento

- Le penali vengono calcolate per %/anno
- Possono essere configurate diversamente per ogni periodo
- Le penali si applicano solo quando il pagamento è in ritardo

### 5.3 Calendario dei Pagamenti

- L'applicazione crea automaticamente il calendario dei pagamenti basato su:
  - Importo del prestito
  - Tasso di interesse
  - Durata
- Ogni periodo di pagamento include: Capitale + Interessi

### 5.4 Rimborso Anticipato

- Calcola l'importo rimanente (capitale + interessi + penali se presenti)
- Dopo il rimborso, il prestito cambierà allo stato "Terminato"

### 5.5 Notifiche

- L'applicazione invia una notifica di promemoria quando il pagamento è in ritardo
- L'ora della notifica può essere configurata per ogni prestito (`notificationTime1`, `notificationTime2`, predefinito 10:00 e 19:00)

## 6. Note importanti

- **Tassi di Interesse Complessi**: Questo modulo supporta tassi di interesse che cambiano per periodo, richiede una configurazione attenta
- **Non può essere eliminato quando esiste il calendario dei pagamenti**: Se il calendario dei pagamenti esiste, puoi solo rimborsare, non eliminare
- **Rimborso Anticipato**: Può richiedere commissioni di penale aggiuntive, dipende dalla politica della banca
- **Calendario dei Pagamenti**: Il calendario dei pagamenti viene calcolato automaticamente, non può essere modificato direttamente

