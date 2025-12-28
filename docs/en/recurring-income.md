# Recurring Income

## 1. Purpose

The **Recurring Income** module helps you manage regular income sources such as:
- Monthly salary
- Rental income
- Pension
- Investment dividends
- Other recurring income

This module automatically creates **occurrences** based on the cycle you configure, and reminds you when it's time to receive payment.

## 2. When to Use

Use this module when you have:
- Fixed income on a schedule (weekly, bi-weekly, or monthly)
- Need to track and confirm when payment is received
- Want automatic calculation into monthly budget

## 3. Related Screens

- Recurring income list
- Add new recurring income
- Edit recurring income
- Occurrence history

## 4. Main Usage

### 4.1 Add New Recurring Income

1. Go to **Functions** → Select **Recurring Income**
2. Tap the **+** (FAB) button at the bottom right
3. Fill in the information:
   - **Category**: Select or create a new category
   - **Amount**: Enter income amount (can be left blank, enter when confirming)
   - **Cycle**: Select Weekly / Bi-weekly / Monthly
   - **Date**: Select date in the cycle (e.g., 15th of each month)
   - **Start Date**: (Only for bi-weekly cycle) Select start date
   - **Note**: Additional information (optional)
4. Tap **Save**

### 4.2 Confirm Payment Received

1. Go to the recurring income list
2. Find item with **"Pending Confirmation"** badge (yellow)
3. Tap on the item to open confirmation dialog
4. Fill in:
   - **Actual Amount**: (if different from expected)
   - **Note**: (optional)
5. Tap **Confirm**

### 4.3 Edit Recurring Income

1. Go to the recurring income list
2. Tap on the item to edit
3. Select **Edit** from menu
4. Update information
5. Tap **Save**

### 4.4 View History

1. Go to the recurring income list
2. Tap on an item
3. Select **History** to view all past occurrences

### 4.5 Deactivate/Activate Income

1. Go to the recurring income list
2. Find the item to deactivate/activate
3. Toggle the **Active** switch on the right side of the item

## 5. Examples & UI Illustrations

### 5.1 Example 1: Create Monthly Recurring Income (Salary)

**Scenario**: You want to track monthly salary so the app automatically reminds you when it's time to receive payment.

**Steps**:
1. Go to Functions screen, select "Recurring Income"
2. Tap the "➕ Add New" button at the bottom right
3. Select category "Salary" (or create new if not available)
4. Enter amount: $4,000
5. Select cycle "Monthly"
6. Select "Select day of month", enter 5
7. Note auto-filled "Monthly salary" (can be edited)
8. Tap "Save"

**Result**: App displays success message and returns to list. New item appears with full information, and app will automatically remind you on the 5th of each month.

**Add Recurring Income Screen**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Add Recurring Income          │
├─────────────────────────────────────────┤
│  Category *                              │
│  [Salary ▼] [+ Add New]                 │
│                                         │
│  Amount (USD) *                          │
│  [$4,000]                               │
│                                         │
│  Cycle *                                 │
│  ┌──────┐ ┌────────┐ ┌────────┐        │
│  │Week  │ │Bi-week │ │Month  │        │
│  └──────┘ └────────┘ └────────┘        │
│                                         │
│  Payment Date in Cycle                  │
│  ⚪ End of month                         │
│  ⚫ Select day of month                  │
│  ┌───────────────────────────────────┐ │
│  │ Day of month: [5]                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Note                                    │
│  ┌───────────────────────────────────┐ │
│  │ Monthly salary                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Cancel]                  [Save]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Example 2: Confirm Due Income and Update Actual Amount

**Scenario**: It's payday (5th), but the actual amount received is $4,200 (salary increase) instead of $4,000 as set.

**Steps**:
1. Open app or go to "Recurring Income" screen
2. App automatically detects due occurrence and shows confirmation dialog
3. Dialog displays default amount: $4,000
4. Update actual amount to $4,200
5. Enter note: "This month has bonus" (optional)
6. Tap "Confirm Received"

**Result**: App updates the confirmed occurrence with actual amount $4,200, automatically creates next occurrence, and updates current financial balance.

**Confirm Income Dialog**:

```text
┌─────────────────────────────────────────┐
│  Confirm Received                        │
├─────────────────────────────────────────┤
│  Salary                                  │
│  Monthly (5th)                          │
│  Due Date: Today                        │
│                                         │
│  Actual Amount *                         │
│  [$4,200]                               │
│                                         │
│  Note                                    │
│  [This month has bonus]                 │
│                                         │
│  [Cancel This]    [Confirm Received]   │
└─────────────────────────────────────────┘
```

---

### 5.3 Example 3: Cancel Income Occurrence When Payment Not Received

**Scenario**: It's rental payment day (1st), but tenant hasn't transferred money so payment wasn't received.

**Steps**:
1. Open app or go to "Recurring Income" screen
2. App shows confirmation dialog for due occurrence
3. Tap "Cancel This" button
4. Enter reason: "Tenant hasn't transferred money" (required)
5. Tap "Confirm Cancel"

**Result**: Cancelled occurrence changes to "Cancelled" status, shows cancellation reason, and app automatically creates next occurrence. Financial balance doesn't change because no payment was received.

**Cancel Income Occurrence Dialog**:

```text
┌─────────────────────────────────────────┐
│  Cancel This                              │
├─────────────────────────────────────────┤
│  Rental Income                            │
│  Monthly (1st)                           │
│  Due Date: Today                         │
│                                         │
│  Cancellation Reason *                    │
│  ┌───────────────────────────────────┐ │
│  │ Tenant hasn't transferred money    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Back]        [Confirm Cancel]         │
└─────────────────────────────────────────┘
```

---

## 6. Logic & Rules

### 6.1 Cycle and Date

- **Weekly**: Select day of week (1=Monday, 7=Sunday)
- **Bi-weekly**: Select day of week + specific start date
- **Monthly**: Select day of month (1-31)

### 6.2 Auto Create Occurrences

- App automatically creates **occurrence** when:
  - Adding new income
  - Reaching date in cycle
  - New month begins

### 6.3 Occurrence Status

- **PENDING**: Pending confirmation (shows yellow badge)
- **COMPLETED**: Confirmed (shows green badge)
- **CANCELLED**: Cancelled (shows red badge)

### 6.4 Budget Integration

- When confirming income, app automatically updates current month's budget (if exists)
- Income is calculated into "Recurring Income" in budget

### 6.5 Notifications

- App sends reminder notification when payment is due
- Notification time can be configured for each item (`notificationTime1`, `notificationTime2`, default 16:00 and 19:00)

## 7. Important Notes

- **Amount can be left blank**: If you don't know the exact amount, you can leave it blank and enter when confirming
- **Cannot delete when occurrence exists**: If there are occurrences, you can only deactivate (isActive = false), cannot delete
- **Late confirmation**: You can confirm past occurrences, app will automatically recalculate budget
- **Change cycle**: When editing cycle, future occurrences will be recalculated

