# Todo List

## 1. Purpose

The **Todo List** module helps you manage recurring tasks and track completion progress, including:
- Time-based recurring tasks (daily/weekly/monthly/yearly)
- Metric-based recurring tasks (miles/hours/times...)
- Reminders when due
- Completion history tracking
- Expense recording (if applicable)

This module helps you never miss important tasks like car maintenance, filter replacements, periodic checks, etc.

## 2. When to Use

Use this module when you have:
- Tasks that repeat on a schedule (e.g., Replace water filter every 3 months)
- Tasks that repeat based on metrics (e.g., Change car oil every 3,000 miles)
- Need automatic reminders when due
- Want to track completion history
- Need to record associated expenses

## 3. Related Screens

- Todo list screen
- Select task type (Time-based / Metric-based)
- Add new todo
- Edit todo
- Confirm metric-based task
- Todo history
- Due tasks list (bell list)

## 4. Main Usage

### 4.1 Add Time-Based Todo

1. Go to **Functions** → Select **Todo List**
2. Tap the **+** (FAB) button at the bottom right
3. Select **Time-based Todo**
4. Fill in the information:
   - **Task Name**: (required, e.g., "Replace water filter")
   - **Recurrence Cycle**: Enter number and select unit (Day/Week/Month/Year)
   - **Next Due Date**: Select date (only allows selecting from tomorrow onwards)
   - **Reminder Time**: Select time (required, e.g., 08:00)
   - **This task incurs expenses**: (Optional) Check if there are expenses
     - If checked: Select **Category** (required)
   - **Note**: Additional information (optional)
5. Tap **Save**

### 4.2 Add Metric-Based Todo

1. Go to **Functions** → Select **Todo List**
2. Tap the **+** (FAB) button
3. Select **Metric-based Todo**
4. Fill in the information:
   - **Task Name**: (required, e.g., "Change car oil")
   - **Cycle**: Enter number (e.g., 3,000)
   - **Unit**: Enter unit (e.g., "Miles")
   - **Last Completed Metric Value**: Enter current value (e.g., 12,500)
   - **This task incurs expenses**: (Optional) Check if there are expenses
     - If checked: Select **Category** (required)
   - **Note**: Additional information (optional)
5. Tap **Save**

### 4.3 Confirm Metric-Based Task

1. Go to the todo list
2. Find the metric-based task (METRIC type) to confirm
3. Tap the **Confirm** button in the card (only shown when `isActive = true`)
4. Fill in the information:
   - **Current Metric Value**: Enter current value (required, must be ≥ last completed metric value)
   - **Note**: (Optional)
5. View **Delta** automatically calculated (current value - last completed value)
6. Tap **Confirmed**
7. (If task has expenses) Select **Add Expense** or **Cancel**

**Note**: Time-based tasks (CYCLE type) do not have a "Confirm" button in the card. Confirmation is only done in the "Due Tasks" (bell list) screen.

### 4.4 View List and Details

1. Go to **Functions** → Select **Todo List**
2. Use **Search bar** to search by task name
3. Use **Filter chips** to filter:
   - **All**: Show all tasks
   - **Time-based**: Show only CYCLE type tasks
   - **Metric-based**: Show only METRIC type tasks
4. Tap on a task card to view details and edit

### 4.5 Edit Todo

1. Go to the todo list
2. Tap on the task card to edit
3. Update information:
   - **Note**: If there is history, **Cycle** (CYCLE) or **Unit/Cycle** (METRIC) will be locked and cannot be edited
4. Tap **Save**

### 4.6 View History

1. Go to the todo list
2. Tap on the **View History ›** link of the task to view
3. Use **Filter chips** to filter by time:
   - **All**: Show all history
   - **This Month**: Show only history from the current month
   - **Last Month**: Show only history from the previous month
   - **Last 3 Months**: Show only history from the last 3 months

### 4.7 Deactivate/Activate Task

1. Go to the todo list
2. Find the task to deactivate/activate
3. Toggle the **Active** switch in the card footer
4. Deactivated tasks will show a **"Inactive"** badge (gray)

### 4.8 Delete Todo

1. Go to the todo list
2. Tap the **Delete** icon (🗑️) in the card header
3. Confirm deletion in the dialog
4. The task and all related history will be deleted

## 5. Examples & UI Illustrations

### TODO-01: Create Time-Based Todo (Replace Water Filter)

**Goal**: Create a time-based todo so the app automatically reminds you when it's due.

**Main Steps**:
1. Go to Functions → Todo List → Tap the "+" (FAB) button
2. Select "Time-based Todo"
3. Enter task name: "Replace water filter"
4. Enter cycle: "3" months
5. Select next due date: 03/01/2026
6. Select reminder time: 08:00
7. Check "This task incurs expenses", select category "Utilities"
8. Enter note: "Replace filter #1 and #2"
9. Tap "Save"

**Wireframe - Add Time-Based Todo Screen**:

```text
┌──────────────────────────────────────────────┐
│ <  Add Time-Based Todo                      │
├──────────────────────────────────────────────┤

Task Name
[ Replace water filter            ]

Recurrence Cycle
Every [ 3 ] [ Month ▼ ]
(Unit: Day / Week / Month / Year)

Next Due Date
[ 03 / 01 / 2026    ▼ ]
Hint: 
Due date for the first time.
Subsequent dates will be automatically calculated based on the cycle you entered.

Reminder Time
[ 08 : 00           ▼ ]

──────────────────────────────────────────────
[✓] This task incurs expenses

┌─────────────────────────────────────┐
│ Category *                           │
│ [Utilities ▼] [+ Create New]       │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Note (optional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Cancel ]                         [ Save ]
└──────────────────────────────────────────────┘
```

---

### TODO-02: Create Metric-Based Todo (Change Car Oil)

**Goal**: Create a metric-based todo to track car maintenance based on mileage.

**Main Steps**:
1. Go to Functions → Todo List → Tap the "+" (FAB) button
2. Select "Metric-based Todo"
3. Enter task name: "Change car oil"
4. Enter cycle: "3,000", unit: "Miles"
5. Enter last completed metric value: "12,500"
6. Check "This task incurs expenses", select category "Car Maintenance"
7. Enter note: "Change oil + oil filter"
8. Tap "Save"

**Wireframe - Add Metric-Based Todo Screen**:

```text
┌──────────────────────────────────────────────┐
│ <  Add Metric-Based Todo                    │
├──────────────────────────────────────────────┤

Task Name
[ Change car oil                        ]

Cycle
Every [ 3,000 ] Unit [ Miles ]
(Unit: Miles / Hours / Times / ...)

Last Completed Metric Value
[ 12,500 ]

──────────────────────────────────────────────
[✓] This task incurs expenses

┌─────────────────────────────────────┐
│ Category *                           │
│ [Car Maintenance ▼] [+ Create New] │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Note (optional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Cancel ]                         [ Save ]
└──────────────────────────────────────────────┘
```

---

### TODO-03: View List and Details

**Goal**: View an overview of todos, filter by type, search, and view details of each task.

**Main Steps**:
1. Go to Functions → Todo List
2. View list with search bar and filter chips
3. Use filters: "All", "Time-based", "Metric-based"
4. Use search bar to search by task name
5. Tap on a task card to view details

**Wireframe - Todo List Screen**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Back]  Todo List                        [🔔]        │
└─────────────────────────────────────────────────────────┘
│  🔍 Search...                                             │
│                                                          │
│  [All] [Time-based] [Metric-based]                     │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Card: Replace water filter                      │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Replace water filter    [Completed] [🗑️]   │ │    │
│  │ │                                              │ │    │
│  │ │ 📅 Cycle: Every 3 months                     │ │    │
│  │ │ ✅ Last completed: 12/01/2025                │ │    │
│  │ │ 📅 Next due date: 03/01/2026                 │ │    │
│  │ │ ⏳ 76 days remaining                          │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ View History ›                     [⚪ Active]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Card: Change car oil                            │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Change car oil                   [🗑️]      │ │    │
│  │ │                                              │ │    │
│  │ │ 📏 Track by: Miles                           │ │    │
│  │ │ ✅ Last confirmed: 12/02/2025                │ │    │
│  │ │ 🔢 Last metric value: 12,500 miles          │ │    │
│  │ │ 🎯 Next due: 14,500 miles                    │ │    │
│  │ │ ⏳ ~300 miles remaining                      │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ [✓ Confirm]                                  │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ View History ›                     [⚪ Active]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ FAB]                                                 │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-04: Confirm Metric-Based Task (Change Car Oil)

**Goal**: Confirm completion of a metric-based task by entering the current metric value.

**Main Steps**:
1. Go to the todo list
2. Find the "Change car oil" task (METRIC type)
3. Tap the "Confirm" button
4. Enter current metric value: "14,520"
5. View automatically calculated delta: "+2,020 miles"
6. Enter note: "Changed oil + oil filter"
7. Tap "Confirmed"

**Wireframe - Confirm Metric-Based Task Dialog**:

```text
┌──────────────────────────────────────────────┐
│  Confirm Metric-Based Task                   │
├──────────────────────────────────────────────┤

Task Name:
Change car oil   (readonly)

Track by:
Miles   (readonly)

Last Completed Metric Value:
12,500 Miles   (readonly)

──────────────────────────────────────────────
Current Metric Value
[ 14,520 ] Miles

Delta:
+2,020 Miles   (auto)

──────────────────────────────────────────────
Note
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
        [ Not Confirmed ]    [ Confirmed ]
└──────────────────────────────────────────────┘
```

---

### TODO-05: Edit Todo and View History

**Goal**: Edit todo information and view completion history.

**Main Steps**:
1. Go to the todo list
2. Tap on the "Replace water filter" task card
3. View warning: "⚠️ Cycle is locked because there is history" (if history exists)
4. Edit next due date, reminder time, note
5. Tap "Save"
6. Tap "View History ›" to view history with filters

**Wireframe - Todo History Screen**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Back]  Todo History - Replace water filter          │
└─────────────────────────────────────────────────────────┘
│  [All] [This Month] [Last Month] [Last 3 Months]        │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Replace water filter            [Completed]      │    │
│  │                                                  │    │
│  │ 📅 Cycle: Every 3 months                         │    │
│  │ ✅ Completed on: 12/01/2025 – 09:10             │    │
│  │ 📝 Note: Replace filter #1 and #2                │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Replace water filter            [Completed]      │    │
│  │                                                  │    │
│  │ 📅 Cycle: Every 3 months                         │    │
│  │ ✅ Completed on: 09/01/2025 – 08:45             │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-06: Deactivate and Delete Todo

**Goal**: Deactivate or delete a todo when it's no longer needed.

**Main Steps**:
1. Go to the todo list
2. Find the task to deactivate
3. Tap the "Active" switch to turn off
4. View "Inactive" badge appear
5. Tap the switch again to reactivate
6. Tap the Delete icon (🗑️) to delete the task
7. Confirm deletion in the dialog

---

### TODO-07: Confirm Metric-Based Task and Add Expense

**Goal**: Confirm a metric-based task and automatically add the related expense.

**Main Steps**:
1. Go to the todo list
2. Find the "Change car oil" task (METRIC type, hasCost = true)
3. Tap the "Confirm" button
4. Enter current metric value: "14,520"
5. Enter note: "Changed oil + oil filter"
6. Tap "Confirmed"
7. View "Incurred Expense?" dialog automatically open
8. Tap "Add Expense"
9. View "Add Expense" screen with note and category pre-filled
10. Enter amount: ₹4,150
11. Tap "Save"

**Wireframe - Incurred Expense Dialog**:

```text
┌──────────────────────────────────────────────┐
│  Incurred Expense?                           │
├──────────────────────────────────────────────┤
Do you want to add an expense for this
completion?

        [ Cancel ]         [ Add Expense ]
└──────────────────────────────────────────────┘
```

## 6. Logic & Rules

### 6.1 Todo Types

- **Time-based (CYCLE type)**:
  - Repeats on a schedule (Day/Week/Month/Year)
  - Has reminder notifications when due
  - Confirmation only done in the "Due Tasks" (bell list) screen
  - No "Confirm" button in the card

- **Metric-based (METRIC type)**:
  - Repeats based on metric milestones (Miles/Hours/Times/Other)
  - No notifications (MVP1)
  - Has "Confirm" button in the card (only shown when `isActive = true`)
  - Confirmation by entering current metric value

### 6.2 Todo Status

- **PENDING**: Upcoming (not yet due)
  - No badge shown: `nextDueDate - today > 7 days`
  - Show "Upcoming" badge (yellow): `0 < nextDueDate - today ≤ 7 days`
- **OVERDUE**: Overdue (red) - `nextDueDate < today` and not confirmed
- **NOT_COMPLETED**: Not done (orange) - Due but not confirmed
- **COMPLETED**: Completed (green) - Confirmed
- **CANCELLED**: Cancelled (gray) - This occurrence was cancelled
- **INACTIVE**: Inactive (gray) - `isActive = false`

### 6.3 Lock Cycle/Unit

- If there is history (history records):
  - **CYCLE type**: Cycle is locked, cannot be edited
  - **METRIC type**: Unit and cycle are locked, cannot be edited
- Show warning: "⚠️ Cycle is locked because there is history" or "⚠️ Unit is locked because there is history"

### 6.4 Confirm Metric-Based Task

- **Validation**:
  - Current metric value must be ≥ last completed metric value
  - If invalid: Show error "Current metric value must be ≥ last completed metric value"
- **Auto Update**:
  - `lastMetricValue` = current value
  - `nextMetricValue` = current value + cycle
  - `lastCompletedDate` = today
- **Expenses**:
  - If `hasCost = true`: Show "Incurred Expense?" dialog after successful confirmation
  - Navigate to "Add Expense" screen with `initialNote`, `initialCategoryId`, `todoHistoryId`

### 6.5 Notifications

- **CYCLE type**: 
  - Notifications are scheduled when creating/editing task
  - Notifications are cancelled when deactivating or deleting task
  - Notifications are rescheduled when reactivating (if `nextDueDate >= today`)
- **METRIC type**: No notifications (MVP1)

### 6.6 Calculate Next Due Date

- **CYCLE type**: 
  - Next due date automatically calculated based on cycle after confirmation
  - Example: Cycle 3 months, due date 03/01/2026 → After confirmation, next due date = 06/01/2026
- **METRIC type**: 
  - Next due = current value + cycle
  - Example: Current value 14,520 miles, cycle 3,000 miles → Next due = 17,520 miles

## 7. Important Notes

1. **Confirm Button**:
   - **Time-based tasks (CYCLE)**: No "Confirm" button in the card. Confirmation is only done in the "Due Tasks" (bell list) screen.
   - **Metric-based tasks (METRIC)**: Has "Confirm" button in the card (only shown when `isActive = true`).

2. **Bell Icon**: The bell icon in the header navigates to the "Due Tasks" (bell list) screen where users can confirm due tasks (only for CYCLE type).

3. **Lock Cycle/Unit**: If there is history, the cycle (CYCLE) or unit/cycle (METRIC) will be locked and cannot be edited to ensure data consistency.

4. **Metric Validation**: When confirming a metric-based task, the current metric value must be ≥ last completed metric value. If not, the app will show an error and prevent confirmation.

5. **Incurred Expenses**: If a task has expenses (`hasCost = true`), after successful confirmation, the app will ask if you want to add an expense. If you choose "Add Expense", the app will automatically pre-fill the note and category.

6. **Delete Task**: When deleting a task, all related history will also be deleted (cascade delete). Notifications will also be cancelled.

7. **Deactivate**: When deactivating a CYCLE type task, notifications will be cancelled. When reactivating, notifications will be rescheduled (if `nextDueDate >= today`).

8. **Premium Access**: This module requires Premium Access. If you don't have Premium, the app will show a dialog requesting an upgrade.

