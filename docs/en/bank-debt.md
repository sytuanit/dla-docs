# Bank Loans

## 1. Purpose

The **Bank Loans** module helps you manage bank loans, including:
- Track loan amount, interest rate, term
- Manage payment schedule
- Calculate interest by period (if applicable)
- Manage late payment penalties
- Early settlement (if needed)

## 2. When to Use

Use this module when you have:
- Bank loans
- Need to track payment schedule
- Want to calculate interest and penalties
- Need reminders when payment is due

## 3. Related Screens

- Loan list
- Add new loan (4 steps)
- Edit loan
- Loan details and payment schedule
- Early settlement

## 4. Main Usage

### 4.1 Add New Loan (4 Steps)

#### Step 1: Basic Information

1. Go to **Functions** → Select **Bank Loans**
2. Tap the **+** (FAB) button
3. Fill in information:
   - **Bank**: Select or create new bank
   - **Loan Name**: (e.g., "Home Loan")
   - **Loan Amount**: Principal amount
   - **Disbursement Date**: Date money was received
   - **Term**: Number of years
   - **Interest Type**: Promotional/floating rate or Fixed rate
4. Tap **Next**

#### Step 2: Configure Interest Rate

**If selecting "Promotional/Floating Rate":**
- Enable **Has Promotional Rate** (if applicable)
- Enter **Promotional Months** and **Promotional Rate**
- Add floating rate periods:
  - Select year and month range
  - Enter interest rate (%/year)
  - Select **Floating** or **Fixed**

**If selecting "Fixed Rate":**
- Enter **Fixed Rate** (%/year)

Tap **Next**

#### Step 3: Configure Penalties

1. Enable **Has Late Payment Penalty** (if applicable)
2. Add penalty periods:
   - Select year and month range
   - Enter **Penalty Rate** (%/year)
3. Tap **Next**

#### Step 4: Confirm and Save

1. Review information:
   - Total amount to pay
   - Expected payment schedule
2. Tap **Save**

### 4.2 View Loan Details

1. Go to loan list
2. Tap on a loan
3. View information:
   - Basic information
   - Payment schedule
   - Amount paid / Remaining
   - Interest rate and penalties

### 4.3 Mark Payment Period as Paid

1. Go to loan details
2. Find payment period due (badge "Not Paid")
3. Tap **Mark as Paid**
4. Fill in information:
   - **Actual Payment Date**: Date paid (default = today)
   - **Actual Interest Paid**: Actual interest paid (default = planned interest)
   - **Note**: (optional)
5. View **Total Actual Payment** automatically calculated (principal + actual interest)
6. Tap **Confirm**

### 4.4 Update Current Interest Rate

1. Go to loan details (only shown if currently in floating rate period)
2. Tap **Update Current Interest Rate**
3. Fill in information:
   - **New Interest Rate**: New interest rate (%/year)
   - **Effective Date**: Date to start applying new rate (default = start of current period)
   - **Note**: (optional)
4. Tap **Save**
5. Unpaid periods from current period onwards will be updated with new interest rate

### 4.5 Early Settlement

1. Go to loan details
2. Tap **Calculate Settlement Amount**
3. **Step 1 - Enter Prepayment Information:**
   - Select method: **Partial Payment** or **Full Settlement**
   - Select prepayment date (default = today)
   - Enter prepayment amount (if partial)
   - View **Early Payment Penalty** automatically calculated
4. Tap **Next**
5. **Step 2 - Compare Options:**
   - View comparison between "No Prepayment" and "Prepayment"
   - View results: Interest savings, time reduction
6. Tap **Confirm Prepayment**

### 4.6 Edit Loan

1. Go to loan details
2. Tap **Edit** (only edit name, note, bank)
3. Edit editable information:
   - **Loan Name**: Can edit
   - **Bank**: Can change
   - **Note**: Can edit
   - **Loan Amount, Disbursement Date, Term, Interest Rate**: Can only edit if no payments made yet
4. Tap **Save**

## 5. Examples & UI Illustrations

### LOAN-01: Create New Loan (Home Loan with Promotional Interest Rate)

**Goal**: Create a new loan to track a home loan, promotional interest rate, and monthly payment schedule.

**Steps**:
1. Go to **Functions** → Select **Bank Loans**
2. Tap the **+** (FAB) button to add new loan
3. **Step 1 - Basic Information:**
   - Select bank: Bank of America
   - Enter name: "Home Loan - Downtown Apartment"
   - Enter loan amount: $200,000
   - Select disbursement date: 04/01/2023
   - Enter term: 10 years (auto-calculated = 120 periods)
   - Select notification times: 10:00 and 19:00
   - Select interest type: "Declining Balance"
   - Tap **Next**
4. **Step 2 - Configure Interest Rate:**
   - Enable "Has Promotional Interest Period"
   - Enter: First 6 months @ 6.0%/year
   - Add subsequent periods:
     - Year 1 (months 7-12): 9.0%/year, floating
     - Year 2 (months 13-24): 9.5%/year, floating
     - Year 3 onwards: 10.0%/year, floating
   - Tap **Next**
5. **Step 3 - Configure Early Payment Penalty:**
   - Enable "Apply Early Payment Penalty"
   - Enter penalties: Years 1-3: 2.0%, Years 4-5: 1.5%, Year 6+: 1.0%
   - Tap **Next**
6. **Step 4 - Confirm:**
   - Review summary information
   - Tap **Create Loan**

**Result**: Loan created successfully, 120-period payment schedule created automatically, notifications scheduled.

**Wireframe - Step 1: Basic Information**

```text
┌─────────────────────────────────────────┐
│ <  Add Loan                              │
├─────────────────────────────────────────┤
│ Loan Name *                              │
│ [Home Loan - Downtown Apartment]        │
│                                          │
│ Bank *                                    │
│ [Bank of America ▼] [+ Create New]       │
│                                          │
│ Loan Amount *                            │
│ [$200,000]                               │
│                                          │
│ Disbursement Date *                      │
│ [04/01/2023] [📅]                        │
│                                          │
│ Loan Term (years) *                       │
│ [10] years                               │
│ Hint: App auto-calculates = 120 periods  │
│                                          │
│ Notification Time 1 *                    │
│ [10:00] [🕐]                             │
│                                          │
│ Notification Time 2 *                    │
│ [19:00] [🕐]                             │
│                                          │
│ Interest Type *                          │
│ ● Declining Balance                      │
│ ○ Fixed Rate for Entire Term             │
│                                          │
│ [NEXT] [CANCEL]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-02: View Loan List and Details

**Goal**: View overview of loans, filter by status, search, and view details of each loan.

**Steps**:
1. Go to **Functions** → Select **Bank Loans**
2. View list screen with filters "Active" (default) and "Completed"
3. Switch between filters to see different overviews
4. Use search bar: Enter "Downtown"
5. Tap on loan to view details
6. View payment schedule with paid periods, current period, and future periods
7. Use search bar in payment schedule: Enter "9/2024"

**Result**: List displays correctly by filter, loan details show full information and payment schedule.

**Wireframe - Loan List**

```text
┌─────────────────────────────────────────┐
│ <  Bank Loan Management                 │
├─────────────────────────────────────────┤
│ [Active] [Completed]                    │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ Current Balance: $164,500          │  │
│ │ Total Original Loan: $200,000      │  │
│ │ Interest Paid: $1,720              │  │
│ │ Active: 1 loan                     │  │
│ └─────────────────────────────────────┘  │
│                                          │
│ [🔍 Search (loan name, bank)]            │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ [ICON] Bank of America  [Active]    │  │
│ │ Home Loan - Downtown Apartment      │  │
│ │ Balance: $164,500                   │  │
│ │ Original: $200,000                 │  │
│ │ Progress: 8 / 120 periods          │  │
│ │ End Date: 04/01/2033               │  │
│ └─────────────────────────────────────┘  │
│                                          │
│                                    [+]   │
└─────────────────────────────────────────┘
```

**Wireframe - Loan Details**

```text
┌─────────────────────────────────────────┐
│ <  Loan Details                         │
├─────────────────────────────────────────┤
│ [ICON] Bank of America          [Edit]  │
│ Home Loan - Downtown Apartment           │
│ [Active]                                 │
│                                          │
│ Original Loan: $200,000                 │
│ Current Balance: $164,500               │
│ Periods Paid: 8 / 120                    │
│ Interest Paid: $1,720                    │
│ Current Interest Rate: 9.0%/year        │
│                                          │
│ [Update Interest] [Calculate Settlement]│
│                                          │
│ Payment Schedule                         │
│ [🔍 Search period (e.g., "5/2025")]     │
│                                          │
│ Period 1 – 05/2023 [Paid]                │
│ Total: $2.15k • Principal: $1k • Interest: $1.15k│
│                                          │
│ Period 9 – 01/2024 [Not Paid]            │
│ Principal: $1,000                        │
│ Interest: $1,150                        │
│ Total: $2,150                            │
│ Due Date: 01/15/2024                     │
│ [Mark as Paid]                           │
│                                          │
│ Period 10 – 02/2024 [Not Due]            │
│ Total: $2.15k • Principal: $1k • Interest: $1.15k│
└─────────────────────────────────────────┘
```

---

### LOAN-03: Mark Payment Period as Paid (Record Payment)

**Goal**: Mark a payment period as "Paid" after making payment to the bank.

**Steps**:
1. Go to loan details
2. Find current period (Period 9) with badge "Not Paid"
3. Tap **Mark as Paid**
4. Fill in information:
   - Actual payment date: 01/15/2024 (default = today)
   - Actual interest paid: $1,150 (default = planned interest)
   - Note: (optional)
5. View total actual payment automatically calculated
6. Tap **Confirm**

**Result**: Period 9 updated to "Paid", balance decreases, paid periods increase, current balance decreases.

**Wireframe - Mark as Paid Dialog**

```text
┌─────────────────────────────────────────┐
│ Mark as Paid                             │
├─────────────────────────────────────────┤
│ Period 9 – 01/2024          [Not Paid]   │
│                                          │
│ Due Date (planned): 01/15/2024          │
│ Principal (fixed): $1,000                │
│                                          │
│ Actual Payment Date *                    │
│ [01/15/2024] [📅]                        │
│                                          │
│ Actual Interest Paid *                   │
│ [$1,150]                                 │
│ Hint: Planned interest: $1,150           │
│                                          │
│ Total Actual Payment =                   │
│   $1,000 (Principal)                    │
│ + $1,150 (Actual Interest)              │
│ ────────────────────────────────        │
│ = $2,150                                 │
│                                          │
│ Note (optional)                          │
│ [Paid $50 less, got interest reduction...]│
│                                          │
│ [CANCEL] [CONFIRM]                       │
└─────────────────────────────────────────┘
```

---

### LOAN-04: Update Current Interest Rate (When Bank Adjusts Floating Rate)

**Goal**: Update new interest rate when bank announces floating rate adjustment.

**Steps**:
1. Go to loan details
2. View "Current Interest Rate: 9.0%/year"
3. Tap **Update Current Interest Rate** (only shown if currently in floating rate period)
4. Fill in information:
   - New interest rate: 10.5%/year
   - Effective date: 01/15/2024 (default = start of current period)
   - Note: "Bank adjusted interest rate per new decision"
5. Tap **Save**

**Result**: Current interest rate updated, unpaid periods from current period onwards updated with new interest rate.

**Wireframe - Update Interest Rate Dialog**

```text
┌─────────────────────────────────────────┐
│ Update Current Interest Rate             │
├─────────────────────────────────────────┤
│ [ICON] Bank of America                   │
│ Loan Name: Home Loan - Downtown Apartment│
│ Current Period: Period 9 – 01/2024       │
│ Status: [Active]                         │
│ Period: Floating (after promotional)     │
│                                          │
│ Current Interest Rate (applying):       │
│ [9.0] %/year (readonly)                  │
│                                          │
│ New Interest Rate (%/year) *              │
│ [10.5] %/year                            │
│                                          │
│ Effective Date *                         │
│ [01/15/2024] [📅]                        │
│                                          │
│ Note (optional)                          │
│ [Bank adjusted interest rate...]         │
│                                          │
│ • New interest rate will be applied to   │
│   periods from Current Period onwards.   │
│ • Previously paid periods are unchanged. │
│                                          │
│ [CANCEL] [SAVE]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-05: Early Settlement (Partial Payment to Reduce Interest)

**Goal**: Settle part of the loan early to reduce total interest payable and shorten loan term.

**Steps**:
1. Go to loan details
2. Tap **Calculate Settlement Amount**
3. **Step 1 - Enter Prepayment Information:**
   - Select method: "Partial Payment"
   - Select prepayment date: 01/15/2024
   - Enter prepayment amount: $80,000
   - View penalty automatically calculated: $1,600 (2.0%)
   - Tap **Next**
4. **Step 2 - Compare Options:**
   - View comparison between "No Prepayment" and "Prepayment $80,000"
   - View results: Save $30,000 interest, reduce 40 periods
   - Tap **Confirm Prepayment**

**Result**: Balance decreases, payment schedule recalculated, number of periods decreases, end date earlier.

**Wireframe - Step 1: Enter Prepayment Information**

```text
┌─────────────────────────────────────────┐
│ <  Early Settlement                      │
├─────────────────────────────────────────┤
│ [ICON] Bank of America                   │
│ Loan Name: Home Loan - Downtown Apartment│
│ Current Balance: $200,000                │
│ Current Period: Period 9 – 01/2024       │
│                                          │
│ How do you want to settle?              │
│ ● Partial Payment                        │
│ ○ Full Settlement                        │
│                                          │
│ Prepayment Date *                        │
│ [01/15/2024] [📅]                        │
│                                          │
│ Prepayment Amount *                      │
│ [$80,000]                                │
│                                          │
│ Penalty Rate Applied: 2.0%                │
│ Penalty: $1,600                          │
│                                          │
│ [NEXT]                                   │
└─────────────────────────────────────────┘
```

**Wireframe - Step 2: Compare Options**

```text
┌─────────────────────────────────────────┐
│ <  Compare Options                       │
├─────────────────────────────────────────┤
│ OPTION A: No Prepayment                 │
│ ────────────────────────────────────────│
│ Total Interest Paid to Date:            │
│   $52,000                               │
│ Total Interest Remaining: $52,000       │
│ Periods Remaining: 112 periods          │
│ End Date: 04/01/2033                    │
│                                          │
│ OPTION B: Prepayment $80,000            │
│ ────────────────────────────────────────│
│ Early Payment Penalty: $1,600           │
│ Total Interest Paid to Date:            │
│   $53,600                               │
│ Total Interest Remaining: $22,000       │
│ Periods Remaining: 72 periods           │
│ End Date: 04/01/2029                    │
│                                          │
│ COMPARISON RESULT:                       │
│ • Interest Savings: $30,000             │
│ • Time Reduction: 40 periods (~3.5 years)│
│                                          │
│ [CONFIRM PREPAYMENT]                     │
└─────────────────────────────────────────┘
```

---

### LOAN-06: Edit Loan (Edit Basic Information)

**Goal**: Edit basic information of loan (name, bank, note) after starting payments.

**Steps**:
1. Go to loan details
2. Tap **Edit** (only edit name, note, bank)
3. Edit:
   - Loan Name: "Home Loan - Downtown Apartment - Unit A1-1201"
   - (Optional) Change bank: Chase Bank
   - Note: "Transferred to new bank"
4. View disabled fields: Loan Amount, Disbursement Date, Term, Interest Rate
5. Tap **Save**

**Result**: Basic information updated, other information unchanged.

**Note**: If loan has no payments made yet, can edit all information (amount, term, interest configuration).

## 6. Logic & Rules

### 6.1 Promotional/Floating Rate

- Can have promotional period (lower interest rate)
- After promotional period, interest rate floats by period
- Each period can be **Floating** (market-based) or **Fixed**

### 6.2 Late Payment Penalties

- Penalties calculated by %/year
- Can configure differently for each period
- Penalties only apply when payment is late

### 6.3 Payment Schedule

- App automatically creates payment schedule based on:
  - Loan amount
  - Interest rate
  - Term
- Each payment period includes: Principal + Interest

### 6.4 Early Settlement

- Calculate remaining amount (principal + interest + penalties if any)
- After settlement, loan will change to "Completed" status

### 6.5 Notifications

- App sends reminder notification when payment is due
- Notification time can be configured for each loan (`notificationTime1`, `notificationTime2`, default 10:00 and 19:00)

## 7. Important Notes

- **Complex Interest Rates**: This module supports interest rates that change by period, requires careful configuration
- **Cannot delete when payment schedule exists**: If payment schedule exists, you can only settle, cannot delete
- **Early Settlement**: May require additional penalty fees, depends on bank policy
- **Payment Schedule**: Payment schedule is calculated automatically, you cannot edit directly

