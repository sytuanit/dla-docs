# Impostazioni

## 1. Obiettivo

Il modulo **Impostazioni** ti consente di configurare l'applicazione secondo le tue esigenze personali, tra cui:
- Lingua e valuta
- Notifiche
- Categorie
- Backup e ripristino dei dati
- Sicurezza (password, Face ID)

## 2. Quando usare

Usa questo modulo se desideri:
- Cambiare la lingua o la valuta
- Attivare/disattivare le notifiche
- Gestire le categorie (aggiungere, modificare, eliminare, impostare come predefinita)
- Eseguire il backup o il ripristino dei dati
- Cambiare la password o attivare Face ID

## 3. Schermate associate

- Schermata principale delle impostazioni
- Impostazioni di base
- Selezionare la lingua
- Selezionare la valuta
- Gestire le categorie
- Eseguire il backup dei dati
- Ripristinare i dati
- Cambiare la password
- Attivare Face ID / Impronta digitale

## 4. Utilizzo principale

### 4.1 Cambiare la lingua

1. Vai a **Impostazioni** → **Visualizzazione e Lingua** → **Lingua**
2. Seleziona la lingua desiderata
3. L'applicazione si ricarica automaticamente con la nuova lingua

### 4.2 Cambiare la valuta

1. Vai a **Impostazioni** → **Visualizzazione e Lingua** → **Valuta**
2. Seleziona il tipo di valuta
3. Tutti gli importi vengono visualizzati nella nuova unità

### 4.3 Attivare/disattivare le notifiche

1. Vai a **Impostazioni** → **Notifiche**
2. Attiva/disattiva l'interruttore **Notifiche**
3. Se attivato, riceverai promemoria per:
   - Entrate ricorrenti in scadenza
   - Spese ricorrenti in scadenza
   - Conti di risparmio in scadenza
   - Occasioni speciali in arrivo

### 4.4 Gestire le categorie

1. Vai a **Impostazioni** → **Categorie**
2. Seleziona il tipo di categoria da gestire:
   - Entrate ricorrenti
   - Entrate extra
   - Spese ricorrenti
   - Spese quotidiane
3. Aggiungi/modifica/elimina categorie
4. Imposta una categoria come predefinita (per le spese quotidiane)

### 4.5 Eseguire il backup dei dati

1. Vai a **Impostazioni** → **Backup e Dati** → **Backup**
2. Seleziona la posizione di archiviazione (file system)
3. Premi **Backup**
4. Il file di backup viene creato

### 4.6 Ripristinare i dati

1. Vai a **Impostazioni** → **Backup e Dati** → **Ripristino**
2. Seleziona il file di backup
3. Conferma il ripristino
4. **Nota**: Il ripristino sostituisce i dati attuali

## 5. Illustrazioni UI (Wireframe)

### 5.1 Schermata principale delle impostazioni

```text
┌─────────────────────────────────────────┐
│  ← Indietro    Impostazioni                    │
├─────────────────────────────────────────┤
│  Visualizzazione e Lingua                     │
│  ┌───────────────────────────────────┐ │
│  │ Lingua                           │ │
│  │ Italiano                      →     │ │
│  │                                    │ │
│  │ Valuta                           │ │
│  │ EUR (€)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notifiche                          │
│  ┌───────────────────────────────────┐ │
│  │ Notifiche                [ON]  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Backup e Dati                          │
│  ┌───────────────────────────────────┐ │
│  │ Backup                        →    │ │
│  │                                    │ │
│  │ Ripristino                       →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Categorie                             │
│  ┌───────────────────────────────────┐ │
│  │ Gestisci categorie              →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Sicurezza                               │
│  ┌───────────────────────────────────┐ │
│  │ Password                        →    │ │
│  │                                    │ │
│  │ Face ID / Impronta digitale          →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logica e regole

### 6.1 Lingua

- Supporta: Italiano, English, Tiếng Việt, 日本語
- Il cambio di lingua ricarica tutta l'applicazione
- Le categorie di sistema vengono tradotte automaticamente nella nuova lingua

### 6.2 Valuta

- Ogni lingua ha una valuta predefinita (es. EUR per l'italiano)
- Puoi selezionare un'altra valuta
- Tutti gli importi vengono formattati secondo la valuta selezionata

### 6.3 Notifiche

- Le notifiche funzionano solo se l'applicazione ha il permesso
- L'ora della notifica dipende da ogni funzione e può essere configurata:
  - Entrate/Spese ricorrenti: `notificationTime1`, `notificationTime2` (predefinito 16:00 e 19:00)
  - Conti di risparmio e prestiti: `notificationTime1`, `notificationTime2` (predefinito 10:00 e 19:00)
  - Occasioni speciali e fasi di preparazione: secondo `reminderTime` che inserisci
  - Puoi disattivare le notifiche per ogni tipo separatamente (in futuro)

### 6.4 Categorie

- Le categorie di sistema non possono essere eliminate, solo disattivate
- Le categorie utente possono essere eliminate (se non sono utilizzate)
- Ogni tipo di categoria è indipendente (entrate ricorrenti, spese quotidiane, ecc.)

## 7. Note importanti

- **Esegui backup regolarmente**: Dovresti eseguire il backup dei dati periodicamente per evitare la perdita di dati
- **Il ripristino sostituisce**: Il ripristino sostituisce tutti i dati attuali
- **Password**: Se dimentichi la password, puoi reimpostarla (elimina i dati)

