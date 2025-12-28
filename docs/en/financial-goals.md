# Financial Goals

## 1. Purpose

The **Financial Goals** module helps you:
- Set financial goals (e.g., buy house, buy car)
- Plan finances to achieve goals
- Evaluate financial assumptions
- Compare loan scenarios
- Track goal progress

## 2. When to Use

Use this module when you want to:
- Plan for a major financial goal
- Evaluate borrowing capacity to buy assets
- Compare financial options
- Track savings progress

## 3. Related Screens

- Create financial goal (3 steps)
- Goal details and plans
- View loan plan
- Evaluate assumptions
- Evaluate assumptions and loan

## 4. Main Usage

### 4.1 Create Financial Goal (3 Steps)

#### Step 1: Enter Financial Plan

1. Go to **Functions** → Select **Planning & Assumptions**
2. Tap the **➕ Add New** (FAB) button
3. View auto-filled information:
   - **Average Income**: Auto retrieved from active recurring income (can click to view breakdown)
   - **Fixed Expenses**: Auto retrieved from active recurring expenses + loan payments (can click to view breakdown)
   - **Current Balance**: Auto retrieved from current balance
4. Enter **Living Expenses**: Monthly living expenses (food, transportation, etc.)
5. View auto-calculated forecast:
   - After 12 months
   - After 24 months
   - After 36 months
   (if keeping current income and expense levels)
6. Tap **Continue**

#### Step 2: Enter Goal Information

1. Enter **Goal Name**: (e.g., "Buy House")
2. Enter **Amount Needed**: Total amount needed to achieve goal
3. View **Down Payment**: Auto-filled from current balance (can edit)
4. Tap **Continue**

#### Step 3: Check Goal Achievement Capability

1. View goal information: Name, Goal Value, Down Payment, Remaining Gap
2. View current finances: Average Income, Average Expenses, Average Savings
3. View conclusion:
   - "You will achieve the goal in ~X years" (if savings > 0)
   - "With current situation, you cannot achieve the goal without borrowing or improving finances" (if savings <= 0)
4. View next options:
   - **View Loan Option**: Evaluate borrowing capacity
   - **Create Income/Expense Assumption**: Simulate financial improvement
   - **Combine Assumption + Loan**: Optimal scenario
5. Tap **Save Goal** (can save now or create plan later)

### 4.2 View Goal List and Details

1. Go to **Functions** → Select **Planning & Assumptions**
2. View list of created goals:
   - Each goal displays: Name, Goal Value, Down Payment Made, Remaining Gap
3. (Optional) Use search bar to find goal by name
4. Tap on a goal to view details:
   - **Goal Information**: Name, Goal Value, Down Payment, Remaining Gap
   - **Financial Plan (baseline)**: Click to view dialog with average income, expenses, savings
   - **Saved Plans List**: Loan plans, assumptions, or combinations that have been created

### 4.3 Create Loan Plan for Goal

1. On goal details screen, tap **➕ Add New** button
2. App shows dialog to select plan type, select **"Loan"**
3. Enter loan information: Loan Amount, Interest Rate, Loan Term, Plan Name
4. View auto-calculated results: Monthly Payment, Total Amount to Pay, Time to Achieve Goal, Affordability
5. Tap **Save Plan**

### 4.4 Create Income/Expense Assumption

1. On goal details screen, tap **➕ Add New** button
2. App shows dialog to select plan type, select **"Assumption"**
3. Enter assumptions:
   - **Increase Income**: Additional amount (or leave blank if no increase)
   - **Decrease Expenses**: Reduced amount (or leave blank if no decrease)
   - Assumption name
4. View auto-calculated results: New Income, New Expenses, New Savings, New Time to Achieve Goal
5. Tap **Save Assumption**

### 4.5 Delete Financial Goal

1. Go to goal details screen
2. Tap **Delete** button (delete icon) at top right of goal card
3. App shows confirmation dialog
4. Tap **Delete** to confirm

**Note**: Deleting goal will delete all related plans and cannot be undone.

## 5. Examples & UI Illustrations

### 5.1 PLANNING-01: Create New Financial Goal (Buy House)

**Goal**: Create a financial goal to plan and simulate the ability to achieve that goal.

**Steps**:
1. Go to Functions screen, select "Planning & Assumptions"
2. Tap "➕ Add New" button
3. **Step 1**: Enter financial plan (view auto-filled info, enter living expenses, view forecast)
4. **Step 2**: Enter goal information (name, amount needed, down payment)
5. **Step 3**: Check goal achievement capability (view conclusion and options)
6. Tap "Save Goal"

**Result**: Goal saved, returns to goal list screen.

**UI Illustration - Step 1: Enter Financial Plan**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Create Goal (1/3)            │
├─────────────────────────────────────────┤
│  Financial Plan                          │
│                                         │
│  Average Income *                        │
│  [$1,200]                               │
│  (Default from recurring items)          │
│  [View Breakdown]                        │
│                                         │
│  Fixed Expenses *                        │
│  [$916]                                 │
│  (Default from recurring items)          │
│  [View Breakdown]                        │
│                                         │
│  Living Expenses *                       │
│  [$200]                                 │
│  (Includes food, transportation,...)     │
│                                         │
│  Current Balance *                       │
│  [$2,000]                               │
│  (Default from current balance)         │
│                                         │
│  Forecast                                │
│  ┌───────────────────────────────────┐ │
│  │ After 12 months: $2,960             │ │
│  │ After 24 months: $3,920             │ │
│  │ After 36 months: $4,880             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Continue] [Cancel]                     │
└─────────────────────────────────────────┘
```

**UI Illustration - Step 2: Enter Goal Information**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Create Goal (2/3)            │
├─────────────────────────────────────────┤
│  Enter Goal Information                 │
│                                         │
│  Goal Name *                            │
│  [Buy House]                            │
│  (Example: Buy House, Buy Car,...)     │
│                                         │
│  Amount Needed *                         │
│  [$80,000]                              │
│  (Total amount needed to achieve goal)   │
│                                         │
│  Down Payment                            │
│  [$2,000]                               │
│  (Default = Current Balance)            │
│                                         │
│  [Continue] [Back]                       │
└─────────────────────────────────────────┘
```

**UI Illustration - Step 3: Check Goal Achievement Capability**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Create Goal (3/3)            │
├─────────────────────────────────────────┤
│  Check Goal Achievement Capability      │
│                                         │
│  Goal Information                       │
│  ┌───────────────────────────────────┐ │
│  │ Goal: Buy House                     │ │
│  │ Goal Value: $80,000                 │ │
│  │ Down Payment: $2,000                │ │
│  │ Remaining Gap: $78,000              │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Your Current Finances                  │
│  ┌───────────────────────────────────┐ │
│  │ Average Income: $1,200              │ │
│  │ Average Expenses: $1,116             │ │
│  │ Average Savings: $84                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  If keeping current situation           │
│  Monthly savings: $84                   │
│  You will need approximately: ~77 years │
│                                         │
│  Conclusion                              │
│  With current situation, you cannot     │
│  achieve the goal without borrowing or  │
│  improving finances                     │
│                                         │
│  What would you like to do next?         │
│  ┌───────────────────────────────────┐ │
│  │ View Loan Option ›                 │ │
│  │ (If you want to see if loan helps...)│ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ Create Income/Expense Assumption ›│ │
│  │ (If you want to try improving...) │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Save Goal] [Back]                     │
└─────────────────────────────────────────┘
```

---

### 5.2 PLANNING-02: View Goal List and Details

**Goal**: View list of created goals and view details of each goal with saved plans.

**Steps**:
1. Go to Functions screen, select "Planning & Assumptions"
2. View list of created goals
3. (Optional) Use search bar to find goal by name
4. Tap on a goal to view details
5. View goal information, financial plan (baseline), and saved plans list

**Result**: Displays full goal information and saved plans.

**UI Illustration - Goal List**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Planning & Assumptions       │
├─────────────────────────────────────────┤
│  [🔍 Search by goal name]               │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Buy House                           │ │
│  │ 🎯 Goal Value: $80,000             │ │
│  │ 💰 Down Payment: $2,000             │ │
│  │ ⚠️ Remaining Gap: $78,000           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Buy Car                             │ │
│  │ 🎯 Goal Value: $20,000              │ │
│  │ 💰 Down Payment: $800               │ │
│  │ ⚠️ Remaining Gap: $19,200           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [➕ Add New]                           │
└─────────────────────────────────────────┘
```

**UI Illustration - Goal Details**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Goal: Buy House              │
├─────────────────────────────────────────┤
│  Goal Information                       │
│  ┌───────────────────────────────────┐ │
│  │ 🎯 Goal Value: $80,000              │ │
│  │ 💰 Down Payment: $2,000             │ │
│  │ ⚠️ Remaining Gap: $78,000           │ │
│  │                                    │ │
│  │ [🗑️ Delete]                         │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [📊 View Financial Plan (baseline)]     │
│                                         │
│  Saved Plans List                       │
│  ┌───────────────────────────────────┐ │
│  │ Loan 80% of house value            │ │
│  │ Loan: $60,000                      │ │
│  │ Interest Rate: 8%/year             │ │
│  │ Term: 20 years                     │ │
│  │ [View Details]                     │ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ Increase Income + Decrease Expenses│ │
│  │ New Income: $1,400                  │ │
│  │ New Expenses: $1,076                │ │
│  │ New Savings: $324                   │ │
│  │ [View Details]                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [➕ Add New]                           │
└─────────────────────────────────────────┘
```

---

### 5.3 PLANNING-03: Create Loan Plan for Goal

**Goal**: Create a loan plan to see if borrowing helps shorten time to achieve goal and affordability.

**Steps**:
1. On goal details screen, tap "➕ Add New" button
2. Select "Loan" in dialog
3. Enter loan information: Loan Amount, Interest Rate, Loan Term, Plan Name
4. View auto-calculated results
5. Tap "Save Plan"

**Result**: Loan plan saved and appears in plans list.

**UI Illustration**: Create loan plan screen (details in related screens).

---

### 5.4 PLANNING-04: Create Income/Expense Assumption to Improve Goal Achievement Capability

**Goal**: Create assumption about increasing income or decreasing expenses to see if this helps achieve goal faster.

**Steps**:
1. On goal details screen, tap "➕ Add New" button
2. Select "Assumption" in dialog
3. Enter assumptions: Increase Income (if any), Decrease Expenses (if any), Assumption Name
4. View auto-calculated results
5. Tap "Save Assumption"

**Result**: Assumption saved and appears in plans list.

**UI Illustration**: Create assumption screen (details in related screens).

---

### 5.5 PLANNING-05: Delete Financial Goal

**Goal**: Delete a financial goal when no longer needed.

**Steps**:
1. Go to goal details screen
2. Tap "Delete" button (delete icon)
3. Confirm deletion in dialog

**Result**: Goal and all related plans have been deleted.

**UI Illustration**: Confirm delete goal dialog.

## 6. Logic & Rules

### 6.1 Forecast Calculation

- Forecast based on:
  - Income - Fixed Expenses - Living Expenses = Savings/month
  - Current Balance + (Savings/month × Number of months)

### 6.2 Goals

- Remaining Gap = Amount Needed - Down Payment
- Estimated Time = Remaining Gap / Average Savings (months)
- If average savings <= 0: Cannot achieve goal without borrowing or improving finances

### 6.3 Loan Plans

- Calculation based on:
  - Loan amount
  - Interest rate
  - Term
  - Auto create payment schedule

### 6.4 Financial Assumptions

- Evaluate assumptions such as:
  - Increase/decrease income
  - Increase/decrease expenses
  - Change interest rate
- View impact on goal achievement capability

## 7. Important Notes

- **Premium Module Required**: This feature is only for Premium users
- **Forecast is for reference only**: Based on assumption of stable income and expenses
- **Can create multiple plans**: You can create multiple plans (loan, assumption, combination) to compare
- **Baseline is saved**: Initial financial plan (baseline) is saved when creating goal, used to compare with later plans
- **Auto Calculation**: Income and fixed expenses automatically retrieved from active recurring items, including bank loan payments
- **Delete Goal**: When deleting goal, all related plans are also deleted and cannot be restored

