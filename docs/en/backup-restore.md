# Backup & Restore

## 1. Purpose

The **Backup & Restore** module helps you:
- Backup all app data to file
- Restore data from backup file
- Protect data from loss due to device errors or app reinstallation

## 2. When to Use

Use this module when you want to:
- Backup data before reinstalling app
- Transfer data to new device
- Restore data after data loss
- Create periodic backups

## 3. Related Screens

- Backup screen
- Restore screen

## 4. Main Usage

### 4.1 Backup Data

1. Go to **Settings** → **Backup & Data** → **Backup**
2. View information:
   - Number of records to be backed up
   - Expected file size
3. Tap **Backup**
4. Select save location (File system)
5. Backup file will be created with name: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Save this file in a safe place (cloud, computer, etc.)

### 4.2 Restore Data

1. Go to **Settings** → **Backup & Data** → **Restore**
2. Select backup file from file system
3. View file information:
   - Backup creation date
   - Number of records
   - File size
4. **Warning**: Restore will overwrite all current data
5. Tap **Restore**
6. Confirm restore
7. Wait for restore process to complete
8. App will automatically reload

## 5. UI Illustrations (Wireframe)

### 5.1 Backup Screen

```text
┌─────────────────────────────────────────┐
│  ← Back    Backup Data                   │
├─────────────────────────────────────────┤
│  Backup Information                      │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Number of Records                  │ │
│  │ 1,234 records                      │ │
│  │                                    │ │
│  │ Expected Size                      │ │
│  │ ~2.5 MB                            │ │
│  │                                    │ │
│  │ Data to be backed up:              │ │
│  │ • Recurring Income                 │ │
│  │ • Recurring Expenses               │ │
│  │ • Daily Expenses                   │ │
│  │ • Budget                           │ │
│  │ • Savings                          │ │
│  │ • Loans                            │ │
│  │ • Special Occasions                │ │
│  │ • Categories                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Backup]                               │
└─────────────────────────────────────────┘
```

### 5.2 Restore Screen

```text
┌─────────────────────────────────────────┐
│  ← Back    Restore Data                 │
├─────────────────────────────────────────┤
│  Select Backup File                      │
│                                         │
│  [Select File...]                       │
│                                         │
│  File Information                       │
│  ┌───────────────────────────────────┐ │
│  │ File: dla-backup-2024-11-15.json │ │
│  │                                    │ │
│  │ Created: 11/15/2024 10:30         │ │
│  │                                    │ │
│  │ Number of Records: 1,234         │ │
│  │                                    │ │
│  │ Size: 2.5 MB                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Warning                             │
│  Restore will overwrite all current     │
│  data. Are you sure?                    │
│                                         │
│  [Restore] [Cancel]                     │
└─────────────────────────────────────────┘
```

## 6. Logic & Rules

### 6.1 Backup File Format

- Backup file is JSON format
- File name: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Contains all data: users, categories, transactions, budgets, etc.

### 6.2 Data Backed Up

- All tables in database
- Includes both system data and user data
- Does not include: app settings, preferences (language, currency)

### 6.3 Restore

- Restore will delete all current data
- Then import data from backup file
- App will automatically reload after restore completes

### 6.4 Validation

- App checks file format before restoring
- Checks version compatibility (if any)
- Displays error if file is invalid

## 7. Important Notes

- **Backup Regularly**: Should backup periodically (weekly or monthly)
- **Save in Multiple Places**: Save backup file in multiple places (cloud, computer, USB)
- **Restore Will Lose Current Data**: Ensure you have backed up current data before restoring
- **Cannot Undo**: After restore, cannot undo

