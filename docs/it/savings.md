# Risparmio

## 1. Obiettivo

Il modulo **Risparmio** ti aiuta a gestire i conti di risparmio, monitorare i saldi, i tassi di interesse e le scadenze. Questo modulo supporta:
- Gestione di più conti di risparmio
- Monitoraggio dei tassi di interesse e delle scadenze
- Calcolo automatico degli interessi alla scadenza
- Prelievo anticipato (se necessario)
- Rinnovo del conto

## 2. Quando usare

Usa questo modulo quando hai:
- Conti di risparmio bancari
- Bisogno di monitorare saldi e tassi di interesse
- Desideri promemoria alla scadenza
- Bisogno di gestire più conti di risparmio

## 3. Schermate associate

- Elenco dei conti di risparmio
- Aggiungere un nuovo conto
- Modificare un conto
- Dettagli del conto
- Prelievo anticipato

## 4. Utilizzo principale

### 4.1 Creare un nuovo conto di risparmio

1. Vai a **Funzioni** → Seleziona **Risparmio Bancario**
2. Premi il pulsante **+** (FAB) in basso a destra
3. Vedi "Saldo Attuale" (puoi cliccare per vedere i dettagli)
4. Seleziona la banca:
   - Se esiste: Seleziona dal menu a discesa
   - Altrimenti: Premi il pulsante "+" per creare una nuova banca
5. Inserisci l'importo del deposito (deve essere ≤ Saldo Attuale)
6. Inserisci la durata: 1-36 mesi
7. Inserisci il tasso di interesse: %/anno (1-100%)
8. Seleziona la data di inizio (predefinito oggi, puoi selezionare dal mese precedente fino a oggi)
9. Vedi la data di scadenza calcolata automaticamente (dalla data di inizio + durata)
10. Seleziona il piano alla scadenza:
    - Preleva capitale e interessi (predefinito)
    - Rinnova il CAPITALE (interessi al conto)
    - Rinnova CAPITALE + INTERESSI
11. (Opzionale) Inserisci una nota
12. (Opzionale) Seleziona le ore di notifica (predefinito: 10:00 e 19:00)
13. Premi **CREA IL CONTO**

### 4.2 Visualizzare l'elenco e i dettagli del conto

1. Vai a **Funzioni** → Seleziona **Risparmio Bancario**
2. Vedi la schermata "Elenco Conti di Risparmio" con il filtro predefinito "Attivo"
3. Vedi la carta di riepilogo:
   - Filtro "Attivo": Saldo attuale, Denaro in risparmio, Interessi attesi, Interessi di questo mese
   - Filtro "Terminato": Totale prelevato, Interessi ricevuti
4. (Opzionale) Usa la barra di ricerca per trovare conti per nome o codice banca
5. Cambia il filtro tra "Attivo" e "Terminato"
6. Premi su un conto di risparmio per vedere i dettagli:
   - Informazioni del conto: Banca, Durata, Tasso di interesse, Importo del deposito, Interessi stimati
   - Data di inizio e data di scadenza
   - Stato: Attivo
   - Piano alla scadenza
   - (Se esiste) Cronologia dei rinnovi
   - Pulsante "PRELEVA" (se attivo)

### 4.3 Prelevare un conto di risparmio

1. Vai all'elenco dei conti di risparmio, trova il conto che ha raggiunto o superato la data di scadenza
2. Premi il pulsante **PRELEVA** sulla carta (o vai ai dettagli e premi "PRELEVA")
3. Vedi il dialogo "PRELEVA IL CONTO DI RISPARMIO" con:
   - Informazioni del conto: Banca, Importo del deposito, Durata, Tasso di interesse
   - Data di prelievo (predefinito = data di scadenza, puoi selezionare una data diversa)
   - Interessi ricevuti (predefinito = interessi stimati, può essere modificato)
   - Totale ricevuto (calcolato automaticamente = capitale + interessi)
4. (Opzionale) Modifica la data di prelievo o gli interessi ricevuti
5. Premi **CONFERMA**

## 5. Logica e regole

### 5.1 Calcolo degli interessi

- Gli interessi vengono calcolati con la formula: `Importo × Tasso di Interesse × (Durata / 12)`
- Gli interessi vengono calcolati alla scadenza o al prelievo anticipato

### 5.2 Stato

- **Attivo (ACTIVE)**: Il conto di risparmio è attivo, non ha raggiunto la data di scadenza o non è stato elaborato
- **Terminato (COMPLETED)**: Il conto è stato prelevato
- **Rinnovato (ROLLED_OVER)**: Il conto è stato rinnovato, un nuovo conto è stato creato

### 5.3 Prelievo e rinnovo

- **Prelievo**: Quando prelevi, il capitale + interessi vengono aggiunti al saldo attuale, crea automaticamente "Entrata Extra" con la categoria "Interessi di Risparmio"
- **Prelievo Anticipato**: Puoi prelevare prima della data di scadenza, gli interessi ricevuti possono essere inferiori agli interessi stimati
- **Rinnova il CAPITALE**: Gli interessi vengono aggiunti al saldo attuale, il capitale viene rinnovato con una nuova durata
- **Rinnova CAPITALE + INTERESSI**: Il capitale e gli interessi vengono rinnovati, il saldo attuale non cambia

### 5.4 Notifiche

- L'applicazione invia una notifica di promemoria quando arriva la data di scadenza
- L'ora della notifica può essere configurata per ogni conto (`notificationTime1`, `notificationTime2`, predefinito 10:00 e 19:00)

## 6. Note importanti

- **Modulo Premium Richiesto**: Questa funzionalità è riservata agli utenti Premium
- **Tasso di Interesse**: Inserisci il tasso di interesse per anno (%/anno), da 1 a 100%
- **Durata**: Calcolata in mesi, da 1 a 36 mesi
- **Data di Scadenza**: Calcolata automaticamente dalla data di inizio + durata
- **Importo del Deposito**: Deve essere ≤ Saldo Attuale, quando crei il conto, viene automaticamente sottratto dal saldo attuale
- **Data di Inizio**: Puoi selezionare solo dall'inizio del mese precedente fino a oggi
- **Notifiche**: Le notifiche vengono inviate alla data di scadenza alle 2 ore (predefinito 10:00 e 19:00), possono essere personalizzate per ogni conto
- **Badge "Vicino alla scadenza"**: Mostrato quando ≤ 7 giorni fino alla data di scadenza
- **Badge "Scaduto"**: Mostrato quando la data di scadenza è arrivata

