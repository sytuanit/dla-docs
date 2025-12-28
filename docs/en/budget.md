# Budget

## 1. Purpose

The **Budget** module helps you plan and track monthly spending, ensuring you don't exceed your set budget. This module automatically calculates based on:
- Your recurring income
- Your recurring expenses
- Actual daily expenses

## 2. When to Use

Use this module when you want to:
- Plan monthly spending
- Control not to exceed budget
- Track savings rate
- View spending analysis by category
- Compare budgets between months

## 3. Related Screens

- Create budget (first time or copy from previous month)
- View budget overview
- Budget history by month
- Copy suggestion from previous month

## 4. Main Usage

### 4.1 Create Budget First Time (Case A)

1. Go to **Functions** → Select **Budget**
2. If no budget exists, app will automatically open **Create Budget** screen
3. App automatically calculates and displays:
   - **Recurring Income**: Total from all active recurring income (readonly, shows detailed breakdown)
   - **Recurring Expenses**: Total from all active recurring expenses (readonly, shows detailed breakdown)
   - **Total Budget (before savings)**: Auto calculated = Recurring Income - Recurring Expenses
4. Enter **Savings Rate**: % savings (0-100%, required)
5. View **Savings Amount** and **Spending Budget** auto calculated
6. Tap **Save Budget**

### 4.2 Copy Budget from Previous Month (Case C)

1. Go to **Functions** → Select **Budget**
2. If current month has no budget but previous month has, app will show **Copy Budget Suggestion** screen
3. Choose one of the options:
   - **Copy entire previous month's budget**: App automatically copies savings rate, recalculates recurring income/expenses from current data, and creates budget immediately
   - **Copy & Adjust**: App navigates to create budget screen with savings rate pre-filled from previous month, you can adjust before saving
   - **Create New Budget**: Run create budget flow from scratch (Case A)
4. If choosing "Copy & Adjust", adjust savings rate if needed
5. Tap **Save Budget**

**Note**: When copying, Recurring Income and Recurring Expenses are recalculated from current recurring data (not copied from previous month), only savings rate is copied.

### 4.3 View Budget Overview (Case B)

1. Go to **Functions** → Select **Budget**
2. If current month has budget, app will open **Overview** screen
3. View information:
   - **Spending Budget**: Spending limit set
   - **Used**: Amount spent (including daily expenses and income/expense variances)
   - **Remaining**: Remaining amount in budget
   - **Usage Rate**: % budget used (with warning colors)
   - **Income & Expense Variances from Plan**: Variances from original plan
   - **Daily Expenses by Category**: Detailed spending analysis by category

### 4.4 Edit Current Month's Budget

1. On **Budget Overview** screen, tap **"Edit Budget"** button
2. App shows edit screen with:
   - **Recurring Income** and **Recurring Expenses**: Keep old values (readonly)
   - **Savings Rate**: Pre-filled from current budget (can be edited)
3. Change savings rate if needed
4. View savings amount and spending budget auto update
5. Tap **"Save Budget"**

**Note**: When editing, Recurring Income and Recurring Expenses are not recalculated (keep old snapshot), only savings rate and spending budget are updated.

### 4.5 View Budget History

1. Go to **Functions** → Select **Budget**
2. Select **History** from menu
3. View list of budgets for past months
4. Tap on a month to view details

### 4.6 View Expense Details by Category

1. Go to **Budget Overview** screen
2. Scroll down to **Analysis by Category** section
3. Tap on a category
4. View list of expenses in that category

## 5. Examples & UI Illustrations

### 5.1 BUDGET-01: Create Budget First Time for Current Month

**Goal**: Create budget first time so app automatically calculates and tracks monthly spending based on income and recurring expenses.

**Steps**:
1. Go to Functions screen, select "Budget Management"
2. App automatically detects no budget and shows "Create Budget" screen
3. View auto calculated info: Recurring Income, Recurring Expenses, Total Budget (before savings)
4. Enter savings rate: 20
5. View savings amount and spending budget auto calculated
6. Tap "Save Budget" button

**Result**: Budget saved for current month, automatically navigates to "Budget Overview" screen.

**UI Illustration**:

```text
[ Card: Create Budget November 2025 ]
+------------------------------------------------+
||                                                |
|| Recurring Income                $1,200         |
||  • My Salary (Monthly)         $1,200         |
||                                                |
|| Recurring Expenses              $916          |
||  • Electricity (Monthly)          $34        |
||  • Water (Monthly)                $17        |
||  • Tuition for BN (Monthly)       $272       |
||  • Breakfast & Coffee (Weekly x 4) $36       |
||  • Home Loan Payment (Monthly)     $420      |
||                                                |
|| (This data is automatically retrieved)        |
+------------------------------------------------+

[ Card: Total Budget (before savings) ]
 ------------------------------------------------
||   $1,200 (Recurring Income)                   |
|| - $916 (Recurring Expenses)                    |
||-----------------------------------------------|
|| = $284 USD                                     |
 ------------------------------------------------

[ Card: Savings Rate ]
 ------------------------------------------------
|| How much do you want to save?                 |
||                                                |
|| Savings Rate (%)                               |
|| [  Input (mandatory): 20  ]                    |
||                                                |
|| → Equivalent: $57                              |
 ------------------------------------------------

[ Card: Spending Budget ]
 ------------------------------------------------
||    $284 (Total Budget (before savings))       |
|| -  $57 (Savings Amount)                        |
||-----------------------------------------------|
|| = $227 USD                                     |
||                                                |
|| (Includes food, transportation, coffee, small shopping...)
 ------------------------------------------------

[ Button ]
 -------------------------------
||      Save Budget              |
 -------------------------------
```

---

### 5.2 BUDGET-02: View Current Month's Budget Overview

**Goal**: View spending situation compared to set budget, including amounts used, remaining, and analysis by category.

**Steps**:
1. Go to Functions screen, select "Budget Management"
2. App automatically detects budget exists and shows "Budget Overview" screen
3. View Card 1 - Monthly Budget: Spending Budget, Used, Remaining, Usage Rate
4. View Card 2 - Income & Expense Variances from Plan
5. View Card 3 - Daily Expenses by Category
6. (Optional) Click on "Spending Budget ›" to view detailed dialog explaining budget calculation

**Result**: Displays full current month's budget information with progress ring/bar and appropriate colors.

**UI Illustration**:

```text
[ Card 1 – Budget November 2025 ]
┌──────────────────────────────────────────────┐
│ Budget November 2025                         │
│                                             │
│ Spending Budget ›      $227                 │
│ Used                  $35                   │
│  • Daily expenses              $48          │   
│  • Income variance      -$160              │
│  • Expense variance       +$8               │
│ Remaining              $104                 │
│                                             │
│                    15.4%                    │
│   (You have used 15.4% of this month's spending budget)
│   (You are about to use up this month's spending budget)
│                                             │
│                               [View History]│
└──────────────────────────────────────────────┘

[ Card 2 – Income & Expense Variances from Plan ]
┌──────────────────────────────────────────────┐
│ Income & Expense Variances from Plan        │
│                                              │
│ Recurring Income                             │
│  • My Salary                 +$80           │
│    ($480 > $400)                             │
│                                              │
│ Recurring Expenses                           │
│  • Tuition for BN              -$4          │
│    ($284 > $280)                             │
│                                              │
│ Total Income Variance:        +$240          │
│ Total Expense Variance:        -$8          │
└──────────────────────────────────────────────┘

[ Card 3 – Daily Expenses by Category ]
┌──────────────────────────────────────────────┐
│ Daily Expenses by Category                   │
│ (Food, transportation, coffee, small shopping...)
│                                             │
│ Total Daily Expenses: $48                    │
│                                             │
│ Food              $24    50% [█████---------]│
│ Transportation     $12    25% [███-----------]│
│ Coffee             $8     17% [██------------]│
│ Small Shopping     $4     8%  [█-------------]│
└──────────────────────────────────────────────┘
```

---

### 5.3 BUDGET-03: Edit Current Month's Budget

**Goal**: Adjust savings rate to change spending budget for current month.

**Steps**:
1. On "Budget Overview" screen, tap "Edit Budget" button
2. App shows edit screen (similar to create budget screen)
3. View current info: Recurring Income, Recurring Expenses (keep old values)
4. Change savings rate to 25
5. View savings amount and spending budget auto update
6. Tap "Save Budget" button

**Result**: Budget updated, returns to "Budget Overview" screen with new values.

**UI Illustration**: Similar to BUDGET-01 (create budget screen), but Recurring Income and Recurring Expenses values are readonly and kept from old budget.

---

### 5.4 BUDGET-04: Copy Budget from Previous Month When Starting New Month

**Goal**: Reuse previous month's budget to save time creating new budget, with option to adjust if needed.

**Steps**:
1. Go to Functions screen, select "Budget Management"
2. App automatically detects current month has no budget but previous month has, shows "Copy Budget Suggestion" screen
3. Select "Copy & Adjust"
4. App navigates to create budget screen with savings rate pre-filled from previous month
5. (Optional) Adjust savings rate if needed
6. Tap "Save Budget" button

**Result**: New budget created for current month, automatically navigates to "Budget Overview" screen.

**UI Illustration**:

```text
[ SCREEN ]  Budget December 2025
┌──────────────────────────────────────────────┐
│ December 2025 has no budget                 │
│                                              │
│ How do you want to create the new month's budget?│
├──────────────────────────────────────────────┤
│                                              │
│ 📝 Copy & Adjust ›                          │
│    Hint: Copy November 2025 budget and adjust│
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│ ➕ Create New Budget ›                      │
│   Hint: Run Create Budget flow again        │
│                                              │
└──────────────────────────────────────────────┘
```

After selecting "Copy & Adjust", the create budget screen will display similar to BUDGET-01, but savings rate is pre-filled from previous month.

## 6. Logic & Rules

### 6.1 Cases

- **Case A**: Create budget first time (no budget for any month)
- **Case B**: Current month has budget → View overview
- **Case C**: Current month has none, but previous month has → Copy suggestion

### 6.2 Auto Calculation

- **Recurring Income**: Total from all active `recurring_income`
- **Recurring Expenses**: Total from all active `recurring_expense`
- **Daily Expenses**: Total from `daily_expense` in the month
- **Total Budget**: Recurring Income + Extra Income
- **Savings**: Total Budget × Savings Rate

### 6.3 Integration with Other Modules

- When confirming recurring income → Automatically update budget
- When confirming recurring expense → Automatically update budget
- Daily expenses are automatically calculated into budget

### 6.4 Budget Exceeded Warning

- App will show warning when spending exceeds budget
- Warning displayed on Home screen and in notifications

### 6.5 Snapshot

- When creating budget, app creates snapshot of income/expense items to save state at that time
- Snapshot is used for comparison and analysis

## 7. Important Notes

- **One budget per month**: You need to create budget for each month
- **Edit budget**: You can edit current month's budget by changing savings rate. Recurring Income and Recurring Expenses will remain unchanged (snapshot) to ensure accuracy
- **Auto update**: Budget automatically updates when you confirm income/expenses
- **Copy from previous month**: Copy feature helps you save time creating budget

