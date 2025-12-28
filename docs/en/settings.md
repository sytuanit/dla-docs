# Settings

## 1. Purpose

The **Settings** module allows you to configure the app according to your personal needs, including:
- Language and currency
- Notifications
- Categories
- Backup and restore data
- Security (password, Face ID)

## 2. When to Use

Use this module when you want to:
- Change language or currency
- Enable/disable notifications
- Manage categories (add, edit, delete, set default)
- Backup or restore data
- Change password or enable Face ID

## 3. Related Screens

- Main settings screen
- Basic settings
- Select language
- Select currency
- Manage categories
- Backup data
- Restore data
- Change password
- Enable Face ID / Fingerprint

## 4. Main Usage

### 4.1 Change Language

1. Go to **Settings** → **Display & Language** → **Language**
2. Select desired language
3. App will automatically reload with new language

### 4.2 Change Currency

1. Go to **Settings** → **Display & Language** → **Currency**
2. Select currency type
3. All amounts will be displayed in the new unit

### 4.3 Enable/Disable Notifications

1. Go to **Settings** → **Notifications**
2. Toggle **Notifications** switch
3. If enabled, you will receive reminders about:
   - Recurring income due
   - Recurring expenses due
   - Savings accounts maturing
   - Special occasions coming up

### 4.4 Manage Categories

1. Go to **Settings** → **Categories**
2. Select category type to manage:
   - Recurring Income
   - Extra Income
   - Recurring Expenses
   - Daily Expenses
3. Add/Edit/Delete categories
4. Set default category (for daily expenses)

### 4.5 Backup Data

1. Go to **Settings** → **Backup & Data** → **Backup**
2. Select save location (File system)
3. Tap **Backup**
4. Backup file will be created

### 4.6 Restore Data

1. Go to **Settings** → **Backup & Data** → **Restore**
2. Select backup file
3. Confirm restore
4. **Note**: Restore will overwrite current data

## 5. UI Illustrations (Wireframe)

### 5.1 Main Settings Screen

```text
┌─────────────────────────────────────────┐
│  ← Back    Settings                    │
├─────────────────────────────────────────┤
│  Display & Language                     │
│  ┌───────────────────────────────────┐ │
│  │ Language                           │ │
│  │ English                      →     │ │
│  │                                    │ │
│  │ Currency                           │ │
│  │ USD ($)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notifications                          │
│  ┌───────────────────────────────────┐ │
│  │ Notifications                [ON]  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Backup & Data                          │
│  ┌───────────────────────────────────┐ │
│  │ Backup                        →    │ │
│  │                                    │ │
│  │ Restore                       →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Categories                             │
│  ┌───────────────────────────────────┐ │
│  │ Manage Categories              →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Security                               │
│  ┌───────────────────────────────────┐ │
│  │ Password                        →    │ │
│  │                                    │ │
│  │ Face ID / Fingerprint          →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logic & Rules

### 6.1 Language

- Supported: English, Tiếng Việt, 日本語
- Changing language will reload entire app
- System categories will automatically translate to new language

### 6.2 Currency

- Each language has default currency (e.g., USD for English)
- You can select different currency
- All amounts will be formatted according to selected currency

### 6.3 Notifications

- Notifications only work when app has permission
- Notification time depends on each function and can be configured:
  - Recurring Income/Expenses: `notificationTime1`, `notificationTime2` (default 16:00 & 19:00)
  - Savings Accounts & Loans: `notificationTime1`, `notificationTime2` (default 10:00 & 19:00)
  - Special Occasions & Preparation Steps: according to `reminderTime` you enter
  - Can disable notifications for each type separately (in the future)

### 6.4 Categories

- System categories cannot be deleted, only disabled
- User categories can be deleted (if not in use)
- Each category type is independent (recurring income, daily expenses, etc.)

## 7. Important Notes

- **Backup Regularly**: Should backup data periodically to avoid data loss
- **Restore Will Overwrite**: Restore will replace all current data
- **Password**: If you forget password, you can reset (will delete data)

