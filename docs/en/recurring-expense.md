# Recurring Expenses

## 1. Purpose

The **Recurring Expenses** module helps you manage periodic expenses with fixed cycles such as:
- Electricity, water, gas bills
- Internet, cable TV
- Insurance
- Tuition
- Rent
- Other recurring expenses

This module automatically creates **occurrences** based on the cycle you configure, and reminds you when payment is due.

## 2. When to Use

Use this module when you have:
- Fixed expenses on a schedule (weekly, bi-weekly, or monthly)
- Need to track and confirm when payment is made
- Want automatic calculation into monthly budget

## 3. Related Screens

- Recurring expenses list
- Add new recurring expense
- Edit recurring expense
- Occurrence history

## 4. Main Usage

### 4.1 Add New Recurring Expense

1. Go to **Functions** → Select **Recurring Expenses**
2. Tap the **+** (FAB) button at the bottom right
3. Fill in the information:
   - **Category**: Select or create a new category
   - **Amount**: Enter expense amount (can be left blank, enter when confirming)
   - **Cycle**: Select Weekly / Bi-weekly / Monthly
   - **Date**: Select date in the cycle (e.g., 15th of each month)
   - **Start Date**: (Only for bi-weekly cycle) Select start date
   - **Note**: Additional information (optional)
4. Tap **Save**

### 4.2 Confirm Payment Made

1. Go to the recurring expenses list
2. Find item with **"Pending Confirmation"** badge (yellow)
3. Tap on the item to open confirmation dialog
4. Fill in:
   - **Actual Amount**: (if different from expected)
   - **Note**: (optional)
5. Tap **Confirm**

### 4.3 Edit Recurring Expense

1. Go to the recurring expenses list
2. Tap on the item to edit
3. Select **Edit** from menu
4. Update information
5. Tap **Save**

### 4.4 View History

1. Go to the recurring expenses list
2. Tap on an item
3. Select **History** to view all past occurrences

### 4.5 Deactivate/Activate Expense

1. Go to the recurring expenses list
2. Find the item to deactivate/activate
3. Toggle the **Active** switch on the right side of the item

## 5. Examples & UI Illustrations

### 5.1 Example 1: Create Monthly Recurring Expense (Electricity Bill)

**Scenario**: You want to track monthly electricity bill so the app automatically reminds you when payment is due.

**Steps**:
1. Go to Functions screen, select "Recurring Expenses"
2. Tap the "➕ Add New" button at the bottom right
3. Select category "Utilities" (or create new if not available)
4. Enter amount: $20
5. Select cycle "Monthly"
6. Select "Select day of month", enter 15
7. Note auto-filled "Monthly electricity bill" (can be edited)
8. Tap "Save"

**Result**: App displays success message and returns to list. New item appears with full information, and app will automatically remind you on the 15th of each month.

**Add Recurring Expense Screen**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Add Recurring Expense        │
├─────────────────────────────────────────┤
│  Category *                              │
│  [Utilities ▼] [+ Add New]             │
│                                         │
│  Amount (USD) *                          │
│  [$20]                                  │
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
│  │ Day of month: [15]                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Note                                    │
│  ┌───────────────────────────────────┐ │
│  │ Monthly electricity bill           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Cancel]                  [Save]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Example 2: Confirm Due Expense and Update Actual Amount

**Scenario**: It's water bill payment day (10th), but the actual amount to pay is $7 (decreased) instead of $8 as set.

**Steps**:
1. Open app or go to "Recurring Expenses" screen
2. App automatically detects due occurrence and shows confirmation dialog
3. Dialog displays default amount: $8
4. Update actual amount to $7
5. Enter note: "This month saved water" (optional)
6. Tap "Confirm Paid"

**Result**: App updates the confirmed occurrence with actual amount $7, automatically creates next occurrence, and updates current financial balance (subtract $7).

**Confirm Expense Dialog**:

```text
┌─────────────────────────────────────────┐
│  Confirm Paid                           │
├─────────────────────────────────────────┤
│  Water Bill                              │
│  Monthly (10th)                         │
│  Due Date: Today                        │
│                                         │
│  Actual Amount *                         │
│  [$7]                                   │
│                                         │
│  Note                                    │
│  [This month saved water]               │
│                                         │
│  [Cancel This]    [Confirm Paid]        │
└─────────────────────────────────────────┘
```

---

### 5.3 Example 3: Deactivate Recurring Expense When No Longer Applicable

**Scenario**: You temporarily don't rent a place for 2 months, so you want to deactivate the "Rent" expense instead of deleting it completely.

**Steps**:
1. Go to "Recurring Expenses" screen
2. Find "Rent" item in the list
3. Tap the "Active" switch on the right side of the item
4. App shows confirmation dialog: "Are you sure you want to deactivate this expense?"
5. Tap "Deactivate" button to confirm

**Result**: "Rent" card changes to "Inactive" status (gray), switch changes to "Inactive". App no longer creates new occurrences for this expense. You can reactivate by tapping the switch "Inactive" → "Active".

**List Screen with Switch**:

```text
┌─────────────────────────────────────────┐
│  ← Back    Recurring Expenses           │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Rent              [⚪ Inactive]   │ │
│  │ $1,200                            │ │
│  │ Monthly - 1st                     │ │
│  │ (Deactivated)                     │ │
│  │                                    │ │
│  │ [Edit] [History] [Delete]         │ │
│  └───────────────────────────────────┘ │
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
  - Adding new expense
  - Reaching date in cycle
  - New month begins

### 6.3 Occurrence Status

- **PENDING**: Pending confirmation (shows yellow badge)
- **COMPLETED**: Confirmed (shows green badge)
- **CANCELLED**: Cancelled (shows red badge)

### 6.4 Budget Integration

- When confirming expense, app automatically updates current month's budget (if exists)
- Expense is calculated into "Recurring Expenses" in budget

### 6.5 Notifications

- App sends reminder notification when payment is due
- Notification time can be configured for each item (`notificationTime1`, `notificationTime2`, default 16:00 and 19:00)

## 7. Important Notes

- **Amount can be left blank**: If you don't know the exact amount, you can leave it blank and enter when confirming
- **Cannot delete when occurrence exists**: If there are occurrences, you can only deactivate (isActive = false), cannot delete
- **Late confirmation**: You can confirm past occurrences, app will automatically recalculate budget
- **Change cycle**: When editing cycle, future occurrences will be recalculated

