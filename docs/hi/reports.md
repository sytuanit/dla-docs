# Reports

## 1. Purpose

The **Reports** module provides detailed financial reports, helping you:
- View current month's financial overview
- Analyze income and expenses
- Track savings progress
- Forecast end-of-month spending
- View reports by type (Income, Expenses, Savings, Loans)

## 2. When to Use

Use this module when you want to:
- View financial overview
- Analyze spending trends
- Check savings goal progress
- Forecast budget overrun risk
- View detailed reports by type

## 3. Related Screens

- Overview report
- Income report
- Expense report
- Savings report
- Loan report

## 4. Main Usage

### 4.1 View Overview Report

1. Go to **Reports** tab in bottom navigation
2. View **Financial Health** section:
   - Savings goal and actual savings (with progress bar and achievement level)
   - Net Cashflow with detailed formula
   - Budget remaining (if budget has been created)
   - Spending pace compared to previous month (if data available)
   - Loan obligations this month (if any)
   - Top 5 spending categories by percentage
3. View **Future Trend Forecast** section (if budget > 0):
   - Expected remaining at end of month with detailed formula
   - Savings goal achievement probability
   - Upcoming loan payment (if any)
4. Tap on cards to scroll to corresponding detailed reports

### 4.2 View Income Report

1. From Reports screen, tap on menu item **💵 Income** in "Detailed Reports" section
2. View total actual income this month
3. View **Recurring Income** section: Total, received, not yet received, details for each item
4. View **Extra Income** section (if any): Total, details for each item, % increase/decrease
5. View **3-Month Income Trend** (if sufficient data available)
6. View **Monthly Income History**
7. View **Income Analysis (Insights)**: Percentage, stability level, trends

### 4.3 View Expense Report

1. From Reports screen, tap on menu item **🔥 Expenses** in "Detailed Reports" section
2. View total actual expenses this month with % increase/decrease compared to previous month
3. View **Recurring Expenses** section: Total, paid, not yet paid, details for each item
4. View **Daily Expenses by Category** section: Top categories with amounts and percentages
5. View **Spending Surge** section (if previous month data available)
6. View **3-Month Expense Trend** (if sufficient data available)
7. View **Monthly Expense History**

### 4.4 View Budget Report

1. From Reports screen, tap on menu item **📉 Budget** in "Detailed Reports" section (only shown when budget has been created)
2. View **Budget Overview This Month**: Monthly budget, spent (with breakdown), remaining, progress bar
3. Tap on "Monthly Budget" to view **Budget Detail Dialog** with calculation method
4. View **Variance from Plan** section: Income and expense items with variances, total variance
5. View **Expenses by Category** section: Total, each category with amount, percentage, progress bar
6. Tap on category to view list of expenses in that category

### 4.5 View Savings Report

1. From Reports screen, tap on menu item **💾 Savings** in "Detailed Reports" section (only shown when savings accounts exist)
2. View **Actual Savings This Month** with Net Cashflow formula
3. View **Savings Analysis** section: % of income, comparison with previous month, end-of-month forecast
4. View **Savings Account List** section: All active accounts, sorted by nearest maturity date
5. View **6-Month Savings Growth Chart** (if more than 1 month of data available)

### 4.6 View Loan Report

1. From Reports screen, tap on menu item **💸 Loans** in "Detailed Reports" section (only shown when loans exist)
2. View **Loan Overview**: Current debt balance, loan cost this month (with principal + interest breakdown)
3. View **Nearest Payment** section: Due date, status, days until next payment
4. View **Monthly Payment Schedule** section: Last 3 months with amounts and status
5. View **Loan Analysis (Insights)** section: Total paid, debt balance trend, interest rate, late payment risk
6. View **6-Month Debt Reduction Chart** (if more than 1 month of data available)

## 5. Examples & UI Illustrations

### 5.1 REPORT-01: View Financial Health Overview and Trend Forecast

**Goal**: View current month's financial overview, including savings progress, net cashflow, budget remaining, and end-of-month forecast.

**Steps**:
1. Go to **Reports** tab in bottom navigation
2. View **Financial Health** section:
   - Savings goal: ₹49,800 (20% of income)
   - Actual savings: ₹34,860
   - Progress bar: 70% - ACHIEVEMENT LEVEL: MEDIUM
   - Net Cashflow: +₹23,240 [POSITIVE] with detailed formula
   - Budget remaining: ₹51,460 [STABLE] (62% budget ≈ 60% time)
   - Spending pace: 12% higher than previous month
   - Loan obligations: ₹34,860 [PAID]
   - Top 5 categories: Food (32%), Shopping (25%), Entertainment (18%), Transportation (15%), Other (10%)
3. View **Future Trend Forecast** section:
   - Expected remaining at end of month: +₹19,090 [SURPLUS] with detailed formula
   - Goal achievement probability: 82% [NEAR ACHIEVE]
   - Upcoming loan payment: Day 25: ₹34,860 [SUFFICIENT FUNDS]

**Wireframe**:
```text
┌──────────────────────┐  ┌──────────────────────┐
│ 🎯 Savings Goal       │  │ 💾 Actual Savings    │
│ ₹49,800               │  │ ₹34,860              │
│ 20% of income        │  │                      │
└──────────────────────┘  └──────────────────────┘

[██████████████----------------------] 70%
ACHIEVEMENT LEVEL: MEDIUM

┌────────────────────────────────────────────────────────────┐
│ Net Cashflow = Actual Savings                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ +₹23,240                    [POSITIVE]                  │ │
│ └────────────────────────────────────────────────────────┘ │
│ Net Cashflow = Income (recurring + extra)                  │
│                – Expenses (recurring + daily + loan)       │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 📉 Budget Remaining                                         │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ₹51,460                      [STABLE]                    │ │
│ └────────────────────────────────────────────────────────┘ │
│ • 62% budget ≈ 60% time → Spending at appropriate pace   │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 💹 Expected Remaining at End of Month                      │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ Expected: +₹19,090             [SURPLUS]                 │ │
│ └────────────────────────────────────────────────────────┘ │
│ • Expected Spending = (Avg Daily Spending × Days Remaining)│
│                + (Pending Fixed Expenses)                  │
└────────────────────────────────────────────────────────────┘
```

### 5.2 REPORT-02: View Income Report

**Goal**: View detailed analysis of this month's income, including recurring income, extra income, trends and insights.

**Steps**:
1. From Reports screen, tap on menu item **💵 Income** in "Detailed Reports" section
2. View **Total Actual Income This Month**: ₹1,74,300
3. View **Recurring Income** section: Total ₹1,24,500 (Received: ₹1,07,900, Not yet received: ₹16,600), details for each item
4. View **Extra Income** section: Total ₹49,800 (Freelance: ₹24,900, Selling items: ₹8,300, Small bonus: ₹16,600), 5% increase from previous month
5. View **3-Month Income Trend** (sparkline chart)
6. View **Monthly Income History**: This month, previous month, 2 months ago
7. View **Income Analysis (Insights)**: Recurring income percentage, stability assessment, % increase/decrease

**Wireframe**: Refer to `wf-bao-cao-thu-nhap.md`

### 5.3 REPORT-03: View Expense Report

**Goal**: View detailed analysis of this month's expenses, including recurring expenses, daily expenses by category, trends and spending surge categories.

**Steps**:
1. From Reports screen, tap on menu item **🔥 Expenses** in "Detailed Reports" section
2. View **Total Actual Expenses This Month**: ₹1,51,060 (12% increase from previous month)
3. View **Recurring Expenses** section: Total ₹70,550 (Paid: ₹62,250, Not yet paid: ₹8,300), details for each item
4. View **Daily Expenses by Category** section: Food ₹53,950 (36%), Shopping ₹24,900 (16%), Transportation ₹17,430 (12%), Entertainment ₹11,620 (8%), Other ₹8,300 (5%)
5. View **Spending Surge** section: Food (+₹9,960, +22%), Shopping (+₹6,640, +35%)
6. View **3-Month Expense Trend** (sparkline chart)
7. View **Monthly Expense History**: This month, previous month, 2 months ago

**Wireframe**: Refer to `wf-bao-cao-chi-tieu.md`

### 5.4 REPORT-04: View Budget Report

**Goal**: View this month's budget overview, including budget spent, remaining, variance from plan, and expenses by category.

**Steps**:
1. From Reports screen, tap on menu item **📉 Budget** in "Detailed Reports" section
2. View **Budget Overview This Month**:
   - Monthly budget: ₹83,000 (tap to view calculation details)
   - Spent: ₹31,540 (Daily expenses: ₹20,750, Expense variance: +₹4,150, Income variance: -₹1,660)
   - Remaining: ₹51,460
   - Progress bar: 38.0% with dynamic hint text
3. Tap on "Monthly Budget" to view **Budget Detail Dialog** with formula: Budget = Income - Expenses
4. View **Variance from Plan** section: Each income/expense item with variance, total variance
5. View **Expenses by Category** section: Total, each category with amount, percentage, progress bar
6. Tap on category to view list of expenses in that category

**Wireframe**: Refer to `wf-bao-cao-ngan-sach.md`

### 5.5 REPORT-05: View Savings Report

**Goal**: View detailed analysis of this month's savings, including actual savings, savings analysis, savings account list, and trends.

**Steps**:
1. From Reports screen, tap on menu item **💾 Savings** in "Detailed Reports" section
2. View **Actual Savings This Month**: ₹34,860 with detailed Net Cashflow formula
3. View **Savings Analysis** section: Savings account for 20% of income, 12% increase from previous month, end-of-month forecast: ₹42,330 (≈85% of goal)
4. View **Savings Account List** section: 3 accounts (₹3,32,000, ₹41,500, ₹1,66,000), sorted by nearest maturity date
5. View **6-Month Savings Growth Chart** (line chart)

**Wireframe**: Refer to `wf-bao-cao-tiet-kiem.md`

### 5.6 REPORT-06: View Loan Report

**Goal**: View detailed analysis of loans, including current debt balance, loan cost this month, payment schedule, insights and trends.

**Steps**:
1. From Reports screen, tap on menu item **💸 Loans** in "Detailed Reports" section
2. View **Loan Overview**: Current debt balance ₹53,95,000, Loan cost this month ₹34,860 (Principal: ₹29,050 + Interest: ₹5,810)
3. View **Nearest Payment** section: Day 25 → PAID, Next payment in 14 days
4. View **Monthly Payment Schedule** section: Last 3 months with amounts and status
5. View **Loan Analysis (Insights)** section: Paid in last 3 months: ₹1,04,580, Debt balance trend decreasing steadily, Interest accounts for 17% of payment, Late payment risk: LOW
6. View **6-Month Debt Reduction Chart** (line chart)

**Wireframe**: Refer to `wf-bao-cao-khoan-vay.md`

### 5.7 REPORT-07: Analyze Expenses by Category from Overview Report

**Goal**: From overview report, tap on "Expenses by Category" section to view detailed expense report and deeper analysis.

**Steps**:
1. From Reports overview screen, scroll to **Expenses by Category** section
2. View top 5 categories with highest percentages
3. Tap on "Expenses by Category" card (with chevron-right icon)
4. App automatically scrolls to **Expense Report** section in the same screen
5. View full details: Total expenses, recurring expenses, daily expenses by category (more than top 5), spending surge, trends and history

**Wireframe**: Refer to `wf-bao-cao.md` - "Expenses by Category" section

### 5.8 REPORT-08: View Reports When Insufficient Data (First Month)

**Goal**: New app users view reports in the first month, when there is insufficient data for comparison and trend analysis.

**Steps**:
1. Go to **Reports** tab
2. View **Financial Health** section:
   - Savings goal and actual savings (if budget exists)
   - Net Cashflow with formula
   - Budget remaining (if exists)
   - **NOT** displayed: "Spending Pace" (no previous month data)
3. View **Future Trend Forecast** section (if budget > 0)
4. Tap on **Income Report**: Total income this month, recurring and extra income, **NOT** displayed "3-Month Trend", **ONLY** displayed "This Month" in history
5. Tap on **Expense Report**: Total expenses this month, recurring and daily expenses, **NOT** displayed "Spending Surge", "3-Month Trend", **ONLY** displayed "This Month" in history

**Wireframe**: Refer to `wf-bao-cao.md` - cards with conditional display

## 6. Logic & Rules

### 6.1 Net Cashflow Calculation

**Formula**:
```
Net Cashflow_month = 
  (Recurring income actually received in month + Extra income in month)
  - (Recurring expenses actually paid in month + Daily expenses in month + Actual loan payments in month)
```

**Details**:
- **Income**: SUM(recurring_income_occurrence.amount_snapshot) WHERE status = 'COMPLETED' AND due_date in month + SUM(extra_income.amount) WHERE occurred_at in month
- **Expenses**: SUM(recurring_expense_occurrence.amount_snapshot) WHERE status = 'COMPLETED' AND due_date in month + SUM(daily_expense.amount) WHERE occurred_at in month + SUM(bank_debt_payment.total_amount) WHERE due_date in month AND status != 'CANCELLED'
- **Actual Savings**: max(NetCashflow_month, 0) - If Net Cashflow positive: Savings = Net Cashflow, If Net Cashflow negative: Savings = 0 (overspending)

### 6.2 Savings Goal Achievement Level

**Formula**:
```
ratio = Saving_month / budget.savings_amount
progress% = round(ratio × 100)
```

**Thresholds**:
- **GOOD**: progress% ≥ 90
- **MEDIUM**: 70 ≤ progress% < 90
- **BAD**: progress% < 70

### 6.3 Budget Remaining

**Formula**:
- % Budget Remaining = (Budget Remaining / Total Budget) × 100
- % Time Remaining = (Days Remaining / Total Days in Month) × 100

**Conclusion**:
- If % budget ≈ % time: Spending pace is **REASONABLE**
- If % budget < % time: Spending **FASTER** than pace
- If % budget > % time: Spending **SLOWER** than pace

**Note**: This card only displays when budget has been created for this month.

### 6.4 End-of-Month Forecast

**Expected Spending**:
```
Expected_Spending = 
  (Avg_Daily_Spending × Days_Remaining_in_Month)
  + Total_Recurring_Expense_Pending_Remaining_Month
  + Total_Bank_Debt_Payment_Pending_in_Month
```

**Details**:
- Avg_Daily_Spending = (Total daily_expense.amount from start of month to today) / Days_Elapsed_in_Month
- Total_Recurring_Expense_Pending = SUM(recurring_expense_occurrence.amount_snapshot) WHERE status = 'PENDING' AND due_date between tomorrow and end of month
- Total_Bank_Debt_Payment_Pending = SUM(bank_debt_payment.total_amount) WHERE due_date between tomorrow and end of month AND status = 'PENDING'

**Expected Remaining at End of Month**:
```
Expected_Remaining_End_of_Month = NetCashflow_month - Expected_Spending
```

**Savings Goal Achievement Probability**:
```
ratio = Expected_Remaining_End_of_Month / budget.savings_amount
progress% = round(ratio × 100)
```

**Labels**:
- ≥ 90% → **WILL ACHIEVE**
- 70–89% → **NEAR ACHIEVE**
- < 70% → **DIFFICULT TO ACHIEVE**

**Note**: Forecast only displays when budget > 0.

### 6.5 Actual Data vs Plan

- **All report data uses ACTUAL data**:
  - Income: COMPLETED occurrences + extra_income
  - Expenses: COMPLETED occurrences + daily_expense
  - Loan payments: bank_debt_payment with due_date in month (regardless of whether paid or not)
- **Does NOT use plan data** (PENDING occurrences not yet due)

## 7. Important Notes

- **Current Month Data Only**: Reports only display current month's data
- **Display Conditions**:
  - "Budget Remaining" card only displays when budget has been created for this month
  - "Spending Pace" card only displays when previous month data is available for comparison
  - "Loan Obligations" card only displays when loans exist
  - "Budget" menu item only displays when budget has been created
  - "Savings" menu item only displays when savings accounts exist
  - "Loans" menu item only displays when loans exist
  - "Future Trend Forecast" section only displays when budget > 0
- **Forecast is for Reference Only**: Based on current trends and PENDING items
- **First Month**: Some cards/sections do not display due to lack of comparison data (e.g., "Spending Pace", "3-Month Trend", "Spending Surge")
- **Cards are Tappable**: Tapping a card scrolls to corresponding detailed report in the same screen

