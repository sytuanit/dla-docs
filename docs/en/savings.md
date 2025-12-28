# Savings

## 1. Purpose

The **Savings** module helps you manage bank savings accounts, track balances, interest rates, and terms. This module supports:
- Managing multiple savings accounts
- Tracking interest rates and terms
- Auto calculating interest at maturity
- Early withdrawal (if needed)
- Account rollover

## 2. When to Use

Use this module when you have:
- Bank savings accounts
- Need to track balances and interest rates
- Want reminders at maturity
- Need to manage multiple savings accounts

## 3. Related Screens

- Savings accounts list
- Add new account
- Edit account
- Account details
- Early withdrawal

## 4. Main Usage

### 4.1 Create New Savings Account

1. Go to **Functions** → Select **Bank Savings**
2. Tap the **+** (FAB) button at the bottom right
3. View "Current Balance" (can click to view details)
4. Select bank:
   - If exists: Select from dropdown
   - If not: Tap "+" button to create new bank
5. Enter deposit amount (must be ≤ Current Balance)
6. Enter term: 1-36 months
7. Enter interest rate: %/year (1-100%)
8. Select start date (default is today, can select from previous month to present)
9. View maturity date auto calculated (from start date + term)
10. Select plan at maturity:
    - Withdraw principal and interest (default)
    - Rollover PRINCIPAL (interest to account)
    - Rollover PRINCIPAL + INTEREST
11. (Optional) Enter note
12. (Optional) Select notification times (default: 10:00 and 19:00)
13. Tap **CREATE ACCOUNT**

### 4.2 View List and Account Details

1. Go to **Functions** → Select **Bank Savings**
2. View "Savings Accounts List" screen with default filter "Active"
3. View overview card:
   - Filter "Active": Current balance, Money in savings, Expected interest, This month's interest
   - Filter "Completed": Total withdrawn, Interest received
4. (Optional) Use search bar to find accounts by bank name or code
5. Switch filter between "Active" and "Completed"
6. Tap on a savings account to view details:
   - Account info: Bank, Term, Interest rate, Deposit amount, Estimated interest
   - Start date and maturity date
   - Status: Active
   - Plan at maturity
   - (If exists) Rollover history
   - "WITHDRAW" button (if active)

### 4.3 Withdraw Savings Account

1. Go to savings list, find account that has reached or passed maturity date
2. Tap **WITHDRAW** button on card (or go to details then tap "WITHDRAW")
3. View "WITHDRAW SAVINGS ACCOUNT" dialog with:
   - Account info: Bank, Deposit amount, Term, Interest rate
   - Withdrawal date (default = maturity date, can select different date)
   - Interest received (default = estimated interest, can edit)
   - Total received (auto calculated = principal + interest)
4. (Optional) Edit withdrawal date or interest received
5. Tap **CONFIRM**

### 4.4 Rollover Savings Account

1. Go to savings list, find account that has reached maturity date with plan "Rollover PRINCIPAL" or "Rollover PRINCIPAL + INTEREST"
2. Tap **ROLLOVER** button or "Rollover as planned"
3. View "ROLLOVER SAVINGS ACCOUNT" dialog with:
   - Account info: Bank, Principal amount, Term, Interest rate
   - Interest received (if rollover PRINCIPAL, interest goes to account)
4. (Optional) Edit new interest rate or new term (default = old term)
5. Tap **CONFIRM ROLLOVER**

### 4.5 Edit Savings Account

1. Go to active savings account details
2. Tap **Edit** button at top right
3. Edit information:
   - Bank (if needed)
   - Deposit amount (if increase, must be ≤ Current Balance)
   - Term, Interest rate
   - Start date (if needed)
   - Plan at maturity
   - Note, Notification times
4. View maturity date auto recalculated (if term/start date changes)
5. Tap **SAVE CHANGES**

### 4.6 Create New Bank

1. On "Add Savings Account" or "Edit Savings Account" screen
2. Tap on "Bank" field
3. Tap "+" button next to dropdown to create new bank
4. View "ADD NEW BANK" dialog
5. Enter bank name
6. Enter bank code (max 3-4 characters, auto uppercase)
7. Select icon color (from color picker or palette)
8. View icon preview
9. Tap **CREATE**

## 5. Examples & UI Illustrations

### SAVINGS-01: Create New Savings Account

**Goal**: Create a new savings account to track bank deposit, interest rate, and maturity date.

**Main Steps**:
1. Go to Functions → Bank Savings
2. Tap "+" (FAB) button
3. Select bank (or create new)
4. Enter deposit amount, term, interest rate
5. Select start date (default today)
6. Select plan at maturity
7. (Optional) Enter note and notification times
8. Tap "CREATE ACCOUNT"

**Wireframe - Add Savings Account Screen**:

```text
┌──────────────────────────────────────────────┐
│ <  Add Savings Account                       │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ Card ]                                      │
│                                               │
│ Current Balance                      [ > ]    │
│ $2,080                                        │
│                                               │
│ Bank *                                        │
│ [ Bank of America ▼ ]                 [ + ] │
│                                               │
│ Deposit Amount (USD) *                       │
│ [ $4,000 ]                                    │
│                                               │
│ Term *                                        │
│ [ 6 ] months                                  │
│                                               │
│ Interest Rate *                               │
│ [ 4.8 ] %/year                                │
│                                               │
│ Start Date *                                  │
│ [ 12/20/2025 ]                    [📅]        │
│                                               │
│ Maturity Date (readonly)                      │
│ [ 06/20/2026 ]                                 │
│                                               │
│ Plan at Maturity                              │
│ (●) Withdraw principal and interest          │
│ ( ) Rollover PRINCIPAL                        │
│ ( ) Rollover PRINCIPAL + INTEREST            │
│                                               │
│ Note (optional)                               │
│ [                                      ]      │
│                                               │
│ Notification Time 1                           │
│ [ 10:00 ]                          [🕐]       │
│                                               │
│ Notification Time 2                            │
│ [ 19:00 ]                          [🕐]       │
└──────────────────────────────────────────────┘

        [  CANCEL  ]       [  CREATE ACCOUNT  ]
```

---

### SAVINGS-02: Withdraw Savings Account

**Goal**: Withdraw savings account when it reaches maturity date to receive principal and interest.

**Main Steps**:
1. Go to savings list, find account that has reached or passed maturity date
2. Tap "WITHDRAW" button
3. View dialog with account info, withdrawal date, interest received
4. (Optional) Edit withdrawal date or interest received
5. Tap "CONFIRM"

**Wireframe - Withdraw Dialog**:

```text
┌─────────────────────────────────────────┐
│  WITHDRAW SAVINGS ACCOUNT                │
├─────────────────────────────────────────┤
│  [ICON BANK]  Bank of America            │
│                                         │
│  Term & Interest Rate: 6 months · 4.8%/year │
│  Deposit Amount: $4,000                 │
│                                         │
│  Withdrawal Date:                       │
│  [ 12 / 20 / 2025 ]  [📅]               │
│                                         │
│  Interest Received:                     │
│  [ $96 ]                                │
│                                         │
│  Total Received: $4,096                 │
│                                         │
│  [  CONFIRM  ]                          │
└─────────────────────────────────────────┘
```

---

### SAVINGS-03: View List and Account Details

**Goal**: View overview of active and completed savings accounts, as well as details of each account.

**Main Steps**:
1. Go to Functions → Bank Savings
2. View overview card by filter
3. Use search bar (optional)
4. Switch filter between "Active" and "Completed"
5. Tap on account to view details

**Wireframe - List Screen**:

```text
┌──────────────────────────────────────────────┐
│ <  Bank Savings Management                    │
│                  [ + [FAB] Add Account ]      │
└──────────────────────────────────────────────┘

[Chip] Filter
[ Active ]   [ Completed ]

┌──────────────────────────────────────────────┐
│  OVERVIEW CARD                                │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Current      │  │ Expected      │         │
│  │ Balance      │  │ Interest      │         │
│  │ $2,080       │  │ $219          │         │
│  └──────────────┘  └──────────────┘         │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Money in     │  │ This Month's │         │
│  │ Savings      │  │ Interest      │         │
│  │ $14,000      │  │ $76           │         │
│  └──────────────┘  └──────────────┘         │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  🔍 Search Bar                               │
│  [ 🔍 Search... ]                            │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ICON BANK] Bank of America      [Icon Delete] │
│                                              │
│ $4,000         |  6 months @ 4.8%           │
│                                              │
│ Estimated Interest: $96                     │
│ Maturity: 12/20/2025   (5 days remaining)  │
│                    🔔 Due Soon               │
│                                              │
│                    [ WITHDRAW ]             │
└──────────────────────────────────────────────┘
```

**Wireframe - Details Screen**:

```text
┌──────────────────────────────────────────────┐
│ [ICON BANK]  Bank of America          [ Edit ]│
│                                              │
│ Term & Interest Rate: 6 months · 4.8%/year  │
│ Deposit Amount: $4,000                       │
│ Estimated Interest: $96                     │
│                                              │
│ Start Date: 06/20/2025                       │
│ Maturity Date: (5 days remaining) 12/20/2025 │
│                                              │
│ Status: Active                               │
│                                              │
│ Plan at Maturity:                           │
│ (●) Withdraw principal and interest         │
│                                              │
│                    [  WITHDRAW  ]           │
└──────────────────────────────────────────────┘
```

---

### SAVINGS-04: Rollover Savings Account

**Goal**: Rollover savings account as planned when it reaches maturity date.

**Main Steps**:
1. Find account that has reached maturity date with plan "Rollover PRINCIPAL" or "Rollover PRINCIPAL + INTEREST"
2. Tap "ROLLOVER" button
3. View dialog with account info and interest received
4. (Optional) Edit new interest rate or new term
5. Tap "CONFIRM ROLLOVER"

**Result**: Old account is updated, new account is created with rootSavingId linked to old account. If rollover PRINCIPAL, interest is added to current balance. If rollover PRINCIPAL + INTEREST, both principal and interest are rolled over.

---

### SAVINGS-05: Create New Bank

**Goal**: Create a new bank to use when creating savings accounts.

**Main Steps**:
1. On "Add Savings Account" or "Edit Savings Account" screen
2. Tap "+" button next to "Bank" dropdown
3. Enter bank name, bank code
4. Select icon color
5. View icon preview
6. Tap "CREATE"

**Wireframe - Create Bank Dialog**:

```text
┌─────────────────────────────────────────┐
│  ADD NEW BANK                            │
├─────────────────────────────────────────┤
│  BANK NAME                               │
│  [ ABC Bank ]                            │
│                                         │
│  BANK CODE                               │
│  [ ABC ]                                 │
│                                         │
│  ICON COLOR                              │
│  [ 🎨 ]  #FF5722                         │
│                                         │
│  PREVIEW ICON                            │
│  ┌─────────┐                             │
│  │   ABC   │  (Background: #FF5722)      │
│  └─────────┘                             │
│                                         │
│  [  CANCEL  ]    [  CREATE  ]           │
└─────────────────────────────────────────┘
```

---

### SAVINGS-06: Edit Savings Account

**Goal**: Edit information of active savings account (bank, amount, term, interest rate, maturity plan).

**Main Steps**:
1. Go to active savings account details
2. Tap "Edit" button
3. Edit necessary information
4. View maturity date auto recalculated (if term/start date changes)
5. Tap "SAVE CHANGES"

**Result**: Account info is updated, estimated interest is recalculated based on new interest rate. If amount changes, current balance is adjusted accordingly.

## 6. Logic & Rules

### 6.1 Interest Calculation

- Interest is calculated by formula: `Amount × Interest Rate × (Term / 12)`
- Interest is calculated at maturity or when withdrawing early

### 6.2 Status

- **Active (ACTIVE)**: Savings account is active, hasn't reached maturity date or hasn't been processed
- **Completed (COMPLETED)**: Account has been withdrawn
- **Rolled Over (ROLLED_OVER)**: Account has been rolled over, new account created

### 6.3 Withdrawal and Rollover

- **Withdrawal**: When withdrawing, principal + interest is added to current balance, automatically creates "Extra Income" with category "Savings Interest"
- **Early Withdrawal**: Can withdraw before maturity date, interest received may be lower than estimated interest
- **Rollover PRINCIPAL**: Interest is added to current balance, principal is rolled over with new term
- **Rollover PRINCIPAL + INTEREST**: Both principal and interest are rolled over, current balance doesn't change
- **Rollover History**: Rollovers are saved and displayed in account details, linked via `rootSavingId`

### 6.4 Notifications

- App sends reminder notification when maturity date arrives
- Notification time can be configured for each account (`notificationTime1`, `notificationTime2`, default 10:00 and 19:00)

## 7. Important Notes

- **Premium Module Required**: This feature is only for Premium users
- **Interest Rate**: Enter interest rate per year (%/year), from 1 to 100%
- **Term**: Calculated in months, from 1 to 36 months
- **Maturity Date**: Auto calculated from start date + term
- **Deposit Amount**: Must be ≤ Current Balance, when creating account will automatically subtract from current balance
- **Start Date**: Can only select from beginning of previous month to present
- **Notifications**: Notifications are sent on maturity date at 2 times (default 10:00 and 19:00), can be customized for each account
- **Badge "Due Soon"**: Shown when ≤ 7 days until maturity date
- **Badge "Matured"**: Shown when maturity date has arrived
- **Delete Account**: When deleting active account, principal amount is added back to current balance. Deleting root account will delete entire rollover chain
- **Overview Card**: Changes by filter, displays aggregated information for active or completed accounts

