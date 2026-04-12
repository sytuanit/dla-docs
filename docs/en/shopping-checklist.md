# Shopping (checklist)

## 1. Purpose

**Shopping (checklist)** helps you create **shopping lists** (list name, line items), **check off items** while shopping, **open quickly** on your phone, **edit** or **duplicate** an existing list, and **delete** when done. A checklist can be **linked to a preparation step** in **Special occasions** — then the app **blocks deletion** while it is in use.

## 2. When to use it

- Shopping at the supermarket or market with a clear list.
- Reusing lists for similar events (duplicate checklist).
- The list is linked to **Special occasions** — then it is part of your preparation workflow.

## 3. Related screens

- **Functions** → **Shopping (checklist)** — all your lists
- **Create / Edit checklist** — name, add/edit/delete items
- **Use checklist** — check items, quick add, reset
- **Special occasions** — pick a checklist when adding a preparation step (deletion rules below)

## 4. Main usage

### 4.1 Create a new list

1. Go to **Functions** → **Shopping (checklist)**.
2. Tap **+** (FAB).
3. Enter **list name** (e.g. “Weekly groceries”).
4. Add **items**; order/edit/delete per the create screen.
5. **Save** to return to the list.

### 4.2 Use a list while shopping

1. On the overview, **tap a list** to open **use checklist**.
2. Check each item when bought.
3. **Quick add** — optional field for last-minute items.
4. **Reset** — clears all “purchased” checks (confirmation dialog); reuse the same list next time.

### 4.3 Edit a list

1. On the card, tap **Edit ›** (or equivalent).
2. Change name or items → **Save**.

### 4.4 Duplicate

1. Use **Copy / create from existing** on the card — opens create with **prefilled** data.
2. Rename if needed → **Save**.

### 4.5 Delete a list

1. Tap **delete** on the card.
2. If the list is **used by Special occasions**, the app **refuses** and shows an error.
3. If not linked, confirm — list and items are deleted.

### 4.6 Search

1. Use **Search checklists...** at the top.
2. The list filters by name (normalized search per app rules).

## 5. Examples & UI sketches

### 5.1 SHOP-01: Grocery run

**Goal**: Create “New Year party” with a few items, then check them off in the store.

**Steps**:
1. Shopping (checklist) → **+** → name `New Year party`
2. Items: `Snacks`, `Drinks`, `Napkins`
3. Save → open list → check items as you buy

**UI sketch**:

```text
[ Search checklists..._____________________ ]

┌────────────────────────────────────────────┐
│ New Year party               Edit ›   [x] │
│ 3 items                                   │
│ ○ ○ ○  0/3 done                           │
└────────────────────────────────────────────┘

                                              [ + ]
```

### 5.2 SHOP-02: Use screen

```text
Shopping checklist: New Year party

[ Reset ]

☑ Snacks
☐ Drinks
☐ Napkins

[ Quick add item...____________________]
```

## 6. Logic & rules

- Each item is purchased or not; the overview may show **total items** and **completed count**.
- **Reset** sets all items back to unpurchased (with confirmation).
- **Special occasions link** — if a checklist is attached to a preparation step, **delete** stays blocked until you unlink it in Special occasions.
- **Duplicate** creates a new list from old data without removing the original.

## 7. Important notes

- **Premium**: **Shopping (checklist)** is under Kitchen & culinary; a Premium badge may appear on **Functions**.
- **Internet** is needed to open the web user guide (per app spec); the checklist itself works in the app once data is loaded.
