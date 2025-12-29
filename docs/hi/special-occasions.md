# Special Occasions

## 1. Purpose

The **Special Occasions** module helps you manage special occasions throughout the year and prepare for them, including:
- Managing special occasions (birthdays, holidays, etc.)
- Creating to-do lists (preparation steps)
- Attaching checklists to each preparation step
- Reminders before occasions
- Tracking preparation progress

## 2. When to Use

Use this module when you want to:
- Manage special occasions throughout the year
- Prepare for important occasions
- Create to-do lists
- Receive reminders before occasions

## 3. Related Screens

- Special occasions list
- Add new special occasion
- Occasion details and preparation steps
- Add preparation step
- Select checklist
- Create new checklist

## 4. Main Usage

### 4.1 Add Special Occasion

1. Go to **Functions** → Select **Special Occasions**
2. Tap the **+** (FAB) button
3. Fill in information:
   - **Occasion Name**: (e.g., "Mom's Birthday")
   - **Date**: Select day/month (DatePicker only selects day/month, no year)
   - **Use Lunar Calendar**: (Optional) Tick if you want to use lunar calendar
     - If ticked: Enter lunar day and month, app auto calculates nearest solar date
   - **Repeat**: Yearly / This Year Only
   - **Show Notification At**: Select time (required, e.g., 07:00)
   - **Note**: Additional information (optional)
4. (Optional) Add preparation steps (see 4.2)
5. Tap **Save**

### 4.2 Add Preparation Step

1. When adding new occasion: Tap **+ Add Step** in "Preparation Steps" section
2. Or from occasion details: Tap **+ Add Step**
3. Fill in information:
   - **When?**: "X days before" or "On the day"
   - **Number of Days**: (if selecting "X days before") Enter number of days before occasion
   - **Show Notification At**: Select time (required)
   - **Repeat Daily Until Completed**: (Optional) Tick if you want daily reminders
   - **Content**: Step name (required, e.g., "Buy Gift")
   - **Note**: (Optional)
   - **Use Checklist**: (Optional) Tick to link with shopping checklist
4. Tap **Add** (or FAB "Apply")

### 4.3 Create Checklist

1. When adding preparation step, tick **Use Checklist**
2. "Select Shopping Checklist" screen automatically opens
3. Tap FAB **+** to create new checklist
4. Enter checklist name
5. Add items:
   - Enter item name
   - Tap **+** to add new item
6. Tap **Save**
7. New checklist is automatically selected and returns to "Add Preparation Step" screen

### 4.4 Mark Step as Complete

1. Go to special occasion details
2. Find step to mark
3. Tap checkbox [ ] to change to [✓]
4. If has checklist, tap checklist name to view and tick/untick items

### 4.5 View Progress

1. Go to special occasion details
2. View "Overview" section:
   - Preparation Steps: Total number of steps
   - Completed: Number of steps ticked / Total steps
   - Status: Not Started / In Progress / Completed

### 4.6 Edit Special Occasion

1. Go to special occasion details
2. Tap hyperlink **Edit ›** in header
3. Edit information: Name, date, repeat, reminder time, note
4. Tap **Save**

### 4.7 Edit Preparation Step

1. Go to special occasion details
2. Tap on step to edit (click on entire item, except Delete icon)
3. Edit information: Time, content, checklist
4. Tap **Apply** (or FAB)

## 5. Examples & UI Illustrations

### OCCASION-01: Create New Special Occasion (Birthday with Preparation Steps)

**Goal**: Create a new special occasion (birthday) with preparation steps so the app automatically reminds you before the occasion occurs.

**Main Steps**:
1. Go to Functions → Special Occasions → Tap "+" (FAB) button
2. Enter occasion name, select date (01/05), select repeat "Yearly", select reminder time (07:00)
3. Add preparation step 1: "7 days before – 08:00" - "Buy Gift"
4. Add preparation step 2: "1 day before – 19:00" - "Order Cake"
5. Tap "Save"

**Wireframe - Add Special Occasion Screen**:

```text
┌──────────────────────────────────────────────┐
│ <  Add Special Occasion                      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📝 Occasion Information                      │
│                                               │
│ Occasion Name *                               │
│ [ An's Birthday                      ]       │
│                                               │
│ Date                                          │
│ [ 01 / 05            ▼ ]                      │
│ (DatePicker only selects day/month)          │
│                                               │
│ [ ] Use Lunar Calendar                        │
│                                               │
│ Repeat                                        │
│ (•) Yearly                                     │
│ ( ) This Year Only                            │
│                                               │
│ Show Notification At *                        │
│ [ 07:00        ▼ ]                            │
│                                               │
│ Note (optional)                                │
│ [                                      ]      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📋 Preparation Steps          [ + Add Step ]│
│ ┌──────────────────────────────────────────┐ │
│ │  1. Buy Gift                   [Icon Delete] │ │
│ │     7 days before – 08:00                 │ │
│ │ ──────────────────────────────────────── │ │
│ │  2. Order Cake                   [Icon Delete] │ │
│ │     1 day before – 19:00                 │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘

        [ Cancel ]                        [ Save ]
```

---

### OCCASION-02: Create Special Occasion Using Lunar Calendar (Memorial Day with Shopping Checklist)

**Goal**: Create a special occasion using lunar calendar (Memorial Day) with preparation steps linked to shopping checklist to track offerings purchase.

**Main Steps**:
1. Go to Functions → Special Occasions → Tap "+" (FAB) button
2. Enter occasion name "Mom's Memorial Day", tick "Use Lunar Calendar"
3. Enter lunar date: 15/11, app auto calculates solar date: 12/15/2025
4. Add 3 preparation steps, where step 2 has checklist link "buy offerings"
5. Tap "Save"

**Wireframe - Select Lunar Date**:

```text
│ │ │ Lunar Date                                   │ │ │
│ │ │ Day (1-30)    Month (1-12)                   │ │ │
│ │ │ [ 15 ]        [ 11 ]                         │ │ │
│ │ │                                               │ │ │
│ │ │ Solar Date (auto calculated - display only)  │ │ │
│ │ │ [ Text: 12/15/2025                 ]         │ │ │
│ │ │ (This is the NEAREST solar date in the future)│ │ │
```

---

### OCCASION-03: View List and Details of Special Occasions

**Goal**: View overview of special occasions, filter by time, and view details of each occasion with preparation progress.

**Main Steps**:
1. Go to Functions → Special Occasions
2. View list with filter "All", "Upcoming", "This Month"
3. Tap on occasion card to view details
4. View overview: Number of steps, Completed, Status
5. Mark step as complete by ticking checkbox

**Wireframe - Special Occasions List Screen**:

```text
┌────────────────────────────────────────────────────────────┐
│ 📅 Special Occasions List                                  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ + Add Occasion ]                                     │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔍 Filter: [ All ]  [ Upcoming ]  [ This Month ]      │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Mom's Memorial Day    [In Progress] [Icon Delete] │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 📅 12/15/2025 • 15/11 (Lunar) • 10 days remaining  │ │ │
│ │ │                                                      │ │ │
│ │ │ ✅ Preparation Steps Needed:                        │ │ │
│ │ │   [✓] 3 days before – List offerings               │ │ │
│ │ │   [ ] 1 day before – Go shopping for offerings     │ │ │
│ │ │   [ ] On the day – Prepare altar / ceremony        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

**Wireframe - Special Occasion Details Screen**:

```text
┌─────────────────────────────────────────────────────────┐
│ 📋 Special Occasion Details                             │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Mom's Memorial Day                       [Edit ›]        │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 12/15/2025 (Solar) • 15/11 (Lunar Calendar)      │ │ │
│ │ │ 10 days remaining • Repeat: Yearly                │ │ │
│ │ │                                                      │ │ │
│ │ │ Note:                                             │ │ │
│ │ │ Small meal, white flowers, limit guests.          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📊 Overview                                         │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Preparation Steps: 3                              │ │ │
│ │ │ Completed: 1 / 3                                 │ │ │
│ │ │ Status: [In Progress]                            │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Preparation Steps                  [ + Add Step ]                  │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ [✓] List offerings                    [Icon Delete]           │ │ │
│ │ │     3 days before – 08:00                        │ │ │
│ │ │     Completed at 09:15 – 12/12/2025               │ │ │
│ │ │ ──────────────────────────────────────────────────── │ │ │
│ │ │                                                      │ │ │
│ │ │ [ ] Go shopping for offerings            [Icon Delete]            │ │ │
│ │ │     1 day before – 19:00                      │ │ │
│ │ │     Repeat daily until completed                  │ │ │
│ │ │     Shopping Checklist: buy offerings ›           │ │ │
│ │ │     [✓] Completed 3 / 8 items                        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

---

### OCCASION-04: Add Preparation Step with Shopping Checklist

**Goal**: Add new preparation step for special occasion and link with shopping checklist to track shopping.

**Main Steps**:
1. Go to special occasion details → Tap "+ Add Step"
2. Select "When?": "X days before", enter number of days: 1
3. Select reminder time: 19:00
4. Enable "Repeat Daily Until Completed"
5. Enter content: "Go shopping for offerings"
6. Tick "Use Checklist" → Select checklist "buy offerings"
7. Tap "Add"

**Wireframe - Add Preparation Step Screen**:

```text
┌────────────────────────────────────────────────────────────┐
│ ➕ Add Preparation Step                                     │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ⏰ Preparation Time                                    │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ When? * (required)                                │ │ │
│ │ │ [ X days before         ▼ ]                       │ │ │
│ │ │                                                      │ │ │
│ │ │ Number of Days * (only shown when "X days before") │ │ │
│ │ │ [  1  ]  days before                               │ │ │
│ │ │                                                      │ │ │
│ │ │ Show Notification At * (required)                  │ │ │
│ │ │ [ 19:00        ▼ ]                                 │ │ │
│ │ │                                                      │ │ │
│ │ │ [✓] Repeat daily until completed                    │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Content                                             │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Content * (required)                              │ │ │
│ │ │ [ Go shopping for offerings               ]        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔗 Link with Shopping Checklist?                       │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ ☑ Use Checklist                                    │ │ │
│ │ │ Shopping Checklist: buy offerings ›    [Icon Swap]  │ │ │
│ │ │ (8 items)                                          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ Cancel ]                        [ Add ]             │ │
│ └────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

### OCCASION-05: Mark Preparation Step as Complete and View Checklist Progress

**Goal**: Mark preparation steps as complete and track shopping checklist progress.

**Main Steps**:
1. Go to special occasion details
2. View step with checklist showing progress "Completed 3 / 8 items"
3. Tap checklist name to view details and tick/untick items
4. Tick step checkbox to mark as complete
5. View "Overview" updates in real-time

---

### OCCASION-06: Edit Special Occasion and Preparation Steps

**Goal**: Edit special occasion information and preparation steps after creation.

**Main Steps**:
1. Go to special occasion details → Tap "Edit ›"
2. Edit occasion name, note
3. Tap "Save"
4. Tap on step to edit: Change time, content
5. Tap Delete icon to delete step (has confirm dialog)

## 6. Logic & Rules

### 6.1 Lunar Calendar Dates

- You can enter both solar and lunar calendar dates
- App automatically calculates solar date corresponding to lunar date
- Supports yearly repeat by lunar calendar

### 6.2 Repeat

- **Yearly**: Occasion repeats every year (by solar or lunar calendar)
  - With solar calendar: Each year calculates nextOccurDate based on (day/month) of solarDate
  - With lunar calendar: Each year converts from lunar date to corresponding solar date and updates nextOccurDate
- **This Year Only**: Occasion only valid in current year, doesn't repeat next year

### 6.3 Preparation Steps

- **When?**: Has 2 options:
  - **X days before**: Remind X days before occasion date (must enter number of days)
  - **On the day**: Remind on the occasion date (no need to enter number of days)
- **Show Notification At**: Reminder time (required, format HH:mm)
- **Repeat Daily Until Completed**: If enabled, notification will repeat daily until user marks step as complete
- **Link Checklist**: Each step can attach a shopping checklist to track shopping progress

### 6.4 Checklist

- Checklist can be reused for multiple steps
- Track number of completed items / Total items (e.g., "Completed 3 / 8 items")
- Displayed in step details with link "checklist name ›" to view details
- Can tick/untick items in checklist to update progress
- Preparation step can be marked complete even if checklist is not fully completed

### 6.5 Notifications

- **Main Occasion Notification**: Created at `nextOccurDate + reminder_time`
  - With YEARLY occasion: notification will be rebuilt when app starts (based on newly calculated nextOccurDate)
  - With ONCE occasion: notification only created once for current nextOccurDate
- **Preparation Step Notification**: Calculate reminder date based on:
  - `nextOccurDate` of special occasion
  - `reminderType` and `daysBefore` (if any)
  - `reminderTime`
- **Repeat Notification**: If `repeatDailyUntilComplete = true`:
  - Create daily repeating notification
  - Use `notificationGroupKey` to group repeat notifications
  - Automatically cancel when user marks step as complete

## 7. Important Notes

- **Lunar Calendar Dates**: 
  - App automatically converts to solar calendar for display
  - Finds "NEAREST solar date in the future" compared to current date
  - Future years: System always recalculates corresponding solar date from (lunar_day, lunar_month) for each year
  - If that year has both regular and leap month of the same month: System may create 2 reminders to avoid missing
- **Yearly Repeat**: 
  - Occasion will automatically recalculate nextOccurDate next year
  - With lunar calendar: Each year converts from lunar date to corresponding solar date
- **Reminder Time**: 
  - Must have a value (cannot be empty)
  - Must be correct format HH:mm (00:00 - 23:59)
- **Checklist**: 
  - Deleted checklist still displays in step (but cannot be edited)
  - Can mark step as complete even if checklist is not fully completed
- **Notifications**: 
  - Need to enable notifications in Settings to receive reminders
  - Repeat notifications will automatically cancel when marking step as complete
- **Occasion Status**:
  - **Not Started**: All steps are not completed (gray)
  - **In Progress**: At least 1 step is completed but not all (blue)
  - **Completed**: All steps are completed (dark green)
  - If occasion has no preparation steps: Status calculated by date (Not Started / Ongoing / Completed)

