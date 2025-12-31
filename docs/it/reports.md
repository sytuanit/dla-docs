# Rapporti

## 1. Obiettivo

Il modulo **Rapporti** fornisce rapporti finanziari dettagliati e ti aiuta a:
- Visualizzare il riepilogo finanziario del mese corrente
- Analizzare entrate e spese
- Monitorare i progressi del risparmio
- Prevedere le spese di fine mese
- Visualizzare rapporti per tipo (Entrate, Spese, Risparmio, Prestiti)

## 2. Quando usare

Usa questo modulo quando desideri:
- Visualizzare il riepilogo finanziario
- Analizzare le tendenze delle spese
- Verificare i progressi dell'obiettivo di risparmio
- Prevedere il rischio di superamento del budget
- Visualizzare rapporti dettagliati per tipo

## 3. Schermate associate

- Rapporto di riepilogo
- Rapporto delle entrate
- Rapporto delle spese
- Rapporto del risparmio
- Rapporto dei prestiti

## 4. Utilizzo principale

### 4.1 Visualizzare il rapporto di riepilogo

1. Vai alla scheda **Rapporti** nella navigazione inferiore
2. Visualizza la sezione **Salute finanziaria**:
   - Obiettivo di risparmio e risparmio reale (con barra di progresso e livello di raggiungimento)
   - Flusso di cassa netto con formula dettagliata
   - Budget rimanente (se il budget è stato creato)
   - Ritmo delle spese rispetto al mese precedente (se i dati sono disponibili)
   - Obblighi di prestito questo mese (se presenti)
   - Top 5 delle categorie di spese per percentuale
3. Visualizza la sezione **Previsione di tendenza futura** (se budget > 0):
   - Rimanente previsto alla fine del mese con formula dettagliata
   - Probabilità di raggiungimento dell'obiettivo di risparmio
   - Pagamento del prestito in arrivo (se presente)
4. Premi sulle carte per scorrere verso i rapporti dettagliati corrispondenti

### 4.2 Visualizzare il rapporto delle entrate

1. Dalla schermata Rapporti, premi l'elemento del menu **💵 Entrate** nella sezione "Rapporti dettagliati"
2. Visualizza il totale delle entrate reali questo mese
3. Visualizza la sezione **Entrate ricorrenti**: Totale, ricevute, non ancora ricevute, dettagli per ogni elemento
4. Visualizza la sezione **Entrate extra** (se presenti): Totale, dettagli per ogni elemento, % di aumento/diminuzione
5. Visualizza la **Tendenza delle entrate su 3 mesi** (se sono disponibili dati sufficienti)
6. Visualizza l'**Cronologia mensile delle entrate**
7. Visualizza l'**Analisi delle entrate (Insights)**: Percentuale, livello di stabilità, tendenze

### 4.3 Visualizzare il rapporto delle spese

1. Dalla schermata Rapporti, premi l'elemento del menu **🔥 Spese** nella sezione "Rapporti dettagliati"
2. Visualizza il totale delle spese reali questo mese con % di aumento/diminuzione rispetto al mese precedente
3. Visualizza la sezione **Spese ricorrenti**: Totale, pagate, non ancora pagate, dettagli per ogni elemento
4. Visualizza la sezione **Spese quotidiane per categoria**: Categorie principali con importi e percentuali
5. Visualizza la sezione **Impennata delle spese** (se i dati del mese precedente sono disponibili)
6. Visualizza la **Tendenza delle spese su 3 mesi** (se sono disponibili dati sufficienti)
7. Visualizza l'**Cronologia mensile delle spese**

## 5. Logica e regole

### 5.1 Calcolo del flusso di cassa netto

**Formula**:
```
Flusso di cassa netto_mese = 
  (Entrate ricorrenti effettivamente ricevute nel mese + Entrate extra nel mese)
  - (Spese ricorrenti effettivamente pagate nel mese + Spese quotidiane nel mese + Pagamenti di prestito reali nel mese)
```

**Dettagli**:
- **Entrate**: SUM(recurring_income_occurrence.amount_snapshot) WHERE status = 'COMPLETED' AND due_date in month + SUM(extra_income.amount) WHERE occurred_at in month
- **Spese**: SUM(recurring_expense_occurrence.amount_snapshot) WHERE status = 'COMPLETED' AND due_date in month + SUM(daily_expense.amount) WHERE occurred_at in month + SUM(bank_debt_payment.total_amount) WHERE due_date in month AND status != 'CANCELLED'
- **Risparmio reale**: max(NetCashflow_month, 0) - Se il flusso di cassa netto è positivo: Risparmio = Flusso di cassa netto, Se il flusso di cassa netto è negativo: Risparmio = 0 (superamento)

### 5.2 Livello di raggiungimento dell'obiettivo di risparmio

**Formula**:
```
ratio = Risparmio_mese / budget.savings_amount
progression% = round(ratio × 100)
```

**Soglie**:
- **BUONO**: progression% ≥ 90
- **MEDIO**: 70 ≤ progression% < 90
- **CATTIVO**: progression% < 70

### 5.3 Budget rimanente

**Formula**:
- % Budget rimanente = (Budget rimanente / Budget totale) × 100
- % Tempo rimanente = (Giorni rimanenti / Totale giorni nel mese) × 100

**Conclusione**:
- Se % budget ≈ % tempo: Il ritmo delle spese è **RAGIONEVOLE**
- Se % budget < % tempo: Spese **PIÙ VELOCI** del ritmo
- Se % budget > % tempo: Spese **PIÙ LENTE** del ritmo

**Nota**: Questa carta viene visualizzata solo quando il budget è stato creato per questo mese.

### 5.4 Previsione di fine mese

**Spese previste**:
```
Spese_previste = 
  (Spese_quotidiane_medie × Giorni_rimanenti_nel_mese)
  + Totale_Spese_ricorrenti_in_attesa_rimanenti_mese
  + Totale_Pagamento_Prestito_Bancario_in_attesa_nel_mese
```

**Rimanente previsto alla fine del mese**:
```
Rimanente_previsto_fine_mese = NetCashflow_month - Spese_previste
```

**Probabilità di raggiungimento dell'obiettivo di risparmio**:
```
ratio = Rimanente_previsto_fine_mese / budget.savings_amount
progression% = round(ratio × 100)
```

**Etichette**:
- ≥ 90% → **RAGGIUNGERÀ**
- 70–89% → **VICINO A RAGGIUNGERE**
- < 70% → **DIFFICILE DA RAGGIUNGERE**

**Nota**: La previsione viene visualizzata solo quando budget > 0.

## 6. Note importanti

- **Dati del mese corrente solo**: I rapporti mostrano solo i dati del mese corrente
- **Condizioni di visualizzazione**:
  - La carta "Budget rimanente" viene visualizzata solo quando il budget è stato creato per questo mese
  - La carta "Ritmo delle spese" viene visualizzata solo quando i dati del mese precedente sono disponibili per il confronto
  - La carta "Obblighi di prestito" viene visualizzata solo quando esistono prestiti
  - L'elemento del menu "Budget" viene visualizzato solo quando il budget è stato creato
  - L'elemento del menu "Risparmio" viene visualizzato solo quando esistono conti di risparmio
  - L'elemento del menu "Prestiti" viene visualizzato solo quando esistono prestiti
  - La sezione "Previsione di tendenza futura" viene visualizzata solo quando budget > 0
- **La previsione è solo a scopo indicativo**: Basata sulle tendenze attuali e sugli elementi PENDING
- **Primo mese**: Alcune carte/sezioni non vengono visualizzate a causa della mancanza di dati di confronto (es. "Ritmo delle spese", "Tendenza su 3 mesi", "Impennata delle spese")
- **Le carte sono cliccabili**: Premere su una carta scorre verso il rapporto dettagliato corrispondente nella stessa schermata

