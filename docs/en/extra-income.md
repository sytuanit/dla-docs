# Extra Income

## 1. Purpose

The **Extra Income** module helps you record non-recurring income with no fixed cycle such as:
- Online Sales
- Freelance
- Bonuses
- Cash Gifts
- Other irregular income

Unlike **Recurring Income**, extra income has no automatic cycle, you must enter manually each time.

## 2. When to Use

Use this module when you want to:
- Record random, non-recurring income
- Track total income in a time period
- Analyze extra income trends
- Calculate into monthly budget

## 3. Related Screens

- Extra income list
- Add new income
- Edit income

## 4. Main Usage

### 4.1 Add Extra Income

1. Go to **Functions** → Select **Extra Income**
2. Tap the **+** (FAB) button at the bottom right
3. Fill in information:
   - **Category**: Select or create new category
   - **Amount**: Enter amount received
   - **Date**: Select date money was received (default is today)
   - **Note**: Detailed description (optional)
4. Tap **Save**

### 4.2 View Income List

1. Go to **Functions** → Select **Extra Income**
2. List displays according to your configured layout (1, 2, 3, or 4 columns)
3. Use **Search** to filter by category or note
4. Select **Time Filter**: Today / This Week / This Month / Last Month / Custom

### 4.3 Edit Income

1. Go to extra income list
2. Long press on item to edit
3. Select **Edit** from menu
4. Update information
5. Tap **Save**

### 4.4 Delete Income

1. Go to extra income list
2. Long press on item to delete
3. Select **Delete** from menu
4. Confirm deletion

## 5. UI Illustrations (Wireframe)

### 5.1 List Screen

```text
┌─────────────────────────────────────────┐
│  ← Back    Extra Income                 │
├─────────────────────────────────────────┤
│  [🔍 Search...]                         │
│  [This Month ▼] [This Week] [Today]     │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Online Sales                        │ │
│  │ $20                                 │ │
│  │ 11/15/2024                          │ │
│  │                                    │ │
│  │ [Edit] [Delete]                    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Freelance                           │ │
│  │ $40                                 │ │
│  │ 11/14/2024                          │ │
│  │                                    │ │
│  │ [Edit] [Delete]                    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Total: $60                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Add/Edit Screen

```text
┌─────────────────────────────────────────┐
│  ← Back    Add Extra Income             │
├─────────────────────────────────────────┤
│  Category *                              │
│  [Online Sales ▼]                        │
│                                         │
│  Amount *                                │
│  [$20]                                  │
│                                         │
│  Date *                                  │
│  [11/15/2024]                           │
│                                         │
│  Note                                    │
│  [Sold Product A]                        │
│                                         │
│  [Save] [Cancel]                        │
└─────────────────────────────────────────┘
```

## 6. Logic & Rules

### 6.1 Display Layout

- You can configure number of columns: 1, 2, 3, or 4 columns
- Layout is saved in settings and applies to all extra income lists

### 6.2 Time Filter

- **Today**: Only shows income from today
- **This Week**: From start of week to today
- **This Month**: From start of month to today
- **Last Month**: Entire previous month
- **Custom**: Select custom time range

### 6.3 Search

- Search in **category name** and **note**
- Case insensitive
- Real-time search as you type

### 6.4 Budget Integration

- Extra income is calculated into "Extra Income" in budget
- Helps you track total monthly income

## 7. Important Notes

- **No Cycle**: Extra income has no automatic cycle, you must enter manually each time
- **Can Delete**: You can delete any income
- **Budget Integration**: Extra income is automatically calculated into current month's budget

