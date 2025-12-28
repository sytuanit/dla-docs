# Daily Expenses

## 1. Purpose

The **Daily Expenses** module helps you record regular, non-fixed expenses such as:
- Food & Dining
- Shopping
- Transportation
- Entertainment
- Other flexible expenses

Unlike **Recurring Expenses**, daily expenses often vary in amount and frequency, with no fixed cycle.

## 2. When to Use

Use this module when you want to:
- Record random, non-recurring expenses
- Track daily spending to control budget
- Analyze spending trends by category
- View total spending in a time period

## 3. Related Screens

- Daily expenses list
- Add new expense
- Edit expense

## 4. Main Usage

### 4.1 Add Daily Expense

1. Go to **Functions** → Select **Daily Expenses**
2. Tap the **+** (FAB) button at the bottom right
3. Fill in information:
   - **Category**: Select category (or use default category if configured)
   - **Amount**: Enter amount spent
   - **Date**: Select expense date (default is today)
   - **Note**: Detailed description (optional)
4. Tap **Save**

### 4.2 View Expense List

1. Go to **Functions** → Select **Daily Expenses**
2. List displays according to your configured layout (2, 3, or 4 columns)
3. Use **Search** to filter by category or note
4. Select **Time Filter**: Today / This Week / This Month / Last Month / Custom

### 4.3 Edit Expense

1. Go to daily expenses list
2. Long press on item to edit
3. Select **Edit** from menu
4. Update information
5. Tap **Save**

### 4.4 Delete Expense

1. Go to daily expenses list
2. Long press on item to delete
3. Select **Delete** from menu
4. Confirm deletion

### 4.5 Set Default Category

1. Go to **Settings** → **Categories** → **Daily Expense Categories**
2. Tap on category you want to set as default
3. Select **Set as Default**
4. When adding new expense, this category will be automatically selected

## 5. UI Illustrations (Wireframe)

### 5.1 List Screen

```text
┌─────────────────────────────────────────┐
│  ← Back    Daily Expenses               │
├─────────────────────────────────────────┤
│  [🔍 Search...]                         │
│  [Today ▼] [This Week] [This Month]    │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Food │ │ Shop │ │ Taxi │            │
│  │ Out  │ │ ping │ │      │            │
│  │      │ │      │ │      │            │
│  │ $2   │ │ $8   │ │ $1   │            │
│  │      │ │      │ │      │            │
│  │ 11/15│ │ 11/15│ │ 11/14│            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Cof  │ │ Other│ │      │            │
│  │ fee  │ │      │ │      │            │
│  │      │ │      │ │      │            │
│  │ $1   │ │ $4   │ │      │            │
│  │      │ │      │ │      │            │
│  │ 11/13│ │ 11/12│ │      │            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  Total: $16                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Add/Edit Screen

```text
┌─────────────────────────────────────────┐
│  ← Back    Add Daily Expense            │
├─────────────────────────────────────────┤
│  Category *                              │
│  [Food Out ▼]                            │
│                                         │
│  Amount *                                │
│  [$2]                                   │
│                                         │
│  Date *                                  │
│  [11/15/2024]                           │
│                                         │
│  Note                                    │
│  [Lunch with friend]                     │
│                                         │
│  [Save] [Cancel]                        │
└─────────────────────────────────────────┘
```

### 5.3 Menu (Long Press)

```text
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐ │
│  │ Food Out                            │ │
│  │ $2                                  │ │
│  │ 11/15/2024                          │ │
│  │                                     │ │
│  │ [Edit] [Delete]                    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logic & Rules

### 6.1 Display Layout

- You can configure number of columns: 2, 3, or 4 columns
- Layout is saved in settings and applies to all expense lists

### 6.2 Time Filter

- **Today**: Only shows expenses from today
- **This Week**: From start of week to today
- **This Month**: From start of month to today
- **Last Month**: Entire previous month
- **Custom**: Select custom time range

### 6.3 Search

- Search in **category name** and **note**
- Case insensitive
- Real-time search as you type

### 6.4 Default Category

- If you have set a default category, when opening add screen, that category will be automatically selected
- Note can also be auto-filled based on category (if configured)

### 6.5 Total Expenses

- Total expenses calculated based on currently selected time filter
- Displayed at bottom of list

## 7. Important Notes

- **No Cycle**: Daily expenses have no automatic cycle, you must enter manually each time
- **Can Delete**: You can delete any expense (unlike recurring expenses)
- **No Budget Integration**: Daily expenses are not automatically calculated into budget (you must track yourself)
- **Custom Categories**: You can create new categories in Settings

