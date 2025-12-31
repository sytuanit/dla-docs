# Backup e Ripristino

## 1. Scopo

Il modulo **Backup e Ripristino** ti aiuta a:
- Eseguire il backup di tutti i dati dell'app su file
- Ripristinare i dati da un file di backup
- Proteggere i dati dalla perdita dovuta a errori del dispositivo o reinstallazione dell'app

## 2. Quando Utilizzare

Usa questo modulo quando vuoi:
- Eseguire il backup dei dati prima di reinstallare l'app
- Trasferire i dati su un nuovo dispositivo
- Ripristinare i dati dopo una perdita di dati
- Creare backup periodici

## 3. Schermate Correlate

- Schermata Backup
- Schermata Ripristino

## 4. Utilizzo Principale

### 4.1 Backup Dati

1. Vai a **Impostazioni** → **Backup e Dati** → **Backup**
2. Visualizza le informazioni:
   - Numero di record da salvare
   - Dimensione file prevista
3. Tocca **Backup**
4. Seleziona la posizione di salvataggio (File system)
5. Il file di backup verrà creato con il nome: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Salva questo file in un posto sicuro (cloud, computer, ecc.)

### 4.2 Ripristino Dati

1. Vai a **Impostazioni** → **Backup e Dati** → **Ripristino**
2. Seleziona il file di backup dal file system
3. Visualizza le informazioni del file:
   - Data di creazione del backup
   - Numero di record
   - Dimensione del file
4. **Avviso**: Il ripristino sovrascriverà tutti i dati attuali
5. Tocca **Ripristino**
6. Conferma il ripristino
7. Attendi il completamento del processo di ripristino
8. L'app si ricaricherà automaticamente

## 5. Illustrazioni UI (Wireframe)

### 5.1 Schermata Backup

```text
┌─────────────────────────────────────────┐
│  ← Indietro    Backup Dati              │
├─────────────────────────────────────────┤
│  Informazioni Backup                     │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Numero di Record                   │ │
│  │ 1.234 record                       │ │
│  │                                    │ │
│  │ Dimensione Prevista                │ │
│  │ ~2,5 MB                            │ │
│  │                                    │ │
│  │ Dati da salvare:                  │ │
│  │ • Reddito Ricorrente               │ │
│  │ • Spese Ricorrenti                 │ │
│  │ • Spese Giornaliere                │ │
│  │ • Budget                           │ │
│  │ • Risparmi                         │ │
│  │ • Prestiti                         │ │
│  │ • Occasioni Speciali               │ │
│  │ • Categorie                        │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Backup]                               │
└─────────────────────────────────────────┘
```

### 5.2 Schermata Ripristino

```text
┌─────────────────────────────────────────┐
│  ← Indietro    Ripristino Dati          │
├─────────────────────────────────────────┤
│  Seleziona File di Backup                │
│                                         │
│  [Seleziona File...]                   │
│                                         │
│  Informazioni File                      │
│  ┌───────────────────────────────────┐ │
│  │ File: dla-backup-2024-11-15.json │ │
│  │                                    │ │
│  │ Creato: 15/11/2024 10:30          │ │
│  │                                    │ │
│  │ Numero di Record: 1.234           │ │
│  │                                    │ │
│  │ Dimensione: 2,5 MB                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Avviso                              │
│  Il ripristino sovrascriverà tutti i    │
│  dati attuali. Sei sicuro?              │
│                                         │
│  [Ripristino] [Annulla]                 │
└─────────────────────────────────────────┘
```

## 6. Logica e Regole

### 6.1 Formato File Backup

- Il file di backup è in formato JSON
- Nome file: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Contiene tutti i dati: utenti, categorie, transazioni, budget, ecc.

### 6.2 Dati Salvati

- Tutte le tabelle nel database
- Include sia dati di sistema che dati utente
- Non include: impostazioni app, preferenze (lingua, valuta)

### 6.3 Ripristino

- Il ripristino eliminerà tutti i dati attuali
- Quindi importa i dati dal file di backup
- L'app si ricaricherà automaticamente dopo il completamento del ripristino

### 6.4 Validazione

- L'app controlla il formato del file prima del ripristino
- Controlla la compatibilità della versione (se presente)
- Mostra un errore se il file non è valido

## 7. Note Importanti

- **Backup Regolare**: Dovresti eseguire il backup periodicamente (settimanale o mensile)
- **Salva in Più Posti**: Salva il file di backup in più posti (cloud, computer, USB)
- **Il Ripristino Perderà i Dati Attuali**: Assicurati di aver eseguito il backup dei dati attuali prima del ripristino
- **Non Può Essere Annullato**: Dopo il ripristino, non può essere annullato

