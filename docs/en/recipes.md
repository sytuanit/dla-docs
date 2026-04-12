# Recipes

## 1. Purpose

The **Recipes** module lets you store **cooking recipes** (dish name, ingredients, instructions), optional **protein types**, **star ratings**, and organize dishes into **collections**. This data is shared with **Menu planning** when you assign dishes to each meal in the week.

## 2. When to use it

- You want a personal recipe notebook for quick lookup while cooking.
- You want to group dishes by theme (e.g. weekend meals, kid-friendly) using **collections**.
- You plan to use **Menu planning** — you need at least a few saved dishes to assign to meals.

## 3. Related screens

- **Functions** → **Kitchen & culinary** → **Recipes** (dish list)
- **Recipes** tab / **Collections** tab on the same list screen
- **Add recipe** / **Edit recipe** (detail form)
- **Collection detail** (dishes in the collection, add dishes to collection)

## 4. Main usage

### 4.1 Open the list and search

1. Go to **Functions** → **Recipes** (under Kitchen & culinary).
2. On the **Recipes** tab, use **Search recipes...** to filter by name (updates as you type).
3. Switch to the **Collections** tab to see your collections; there is a separate search for collections.

### 4.2 Add a new recipe

1. Tap the **+** (FAB) at the bottom.
2. Enter **Dish name** (required).
3. (Optional) **Protein types** — multiple values separated by commas (e.g. Beef, Seafood).
4. **Rating** — tap stars to rate the dish.
5. **Ingredients** — add at least one row: ingredient name (required), quantity (optional). You can add more rows.
6. **Instructions** — cooking steps (optional but recommended).
7. **Collections** — link the dish to one or more existing collections (optional).
8. Tap **Save**.

### 4.3 Edit / delete a recipe

1. On the list, tap a recipe to open edit.
2. Change fields as when creating, then **Save** / **Update** (per app labels).
3. **Delete**: use the delete control on the screen (the app warns if the dish is used in a **meal plan** — confirming removes it from those slots).

### 4.4 Collections

1. **Collections** tab → **Create collection**, enter a name → confirm.
2. Tap a collection to see dishes inside; you can **Add recipes to collection** (pick from dishes not yet in that collection).
3. **Rename** / **Delete collection** from the row; deleting a collection **does not** delete recipes, only unlinks them.

## 5. Examples & UI sketches

### 5.1 RECIPE-01: Create a dish and assign a collection

**Goal**: Save “Tom yum soup” for later use in the meal plan and filter by collection “Thai”.

**Steps**:
1. Functions → **Recipes** → **+**
2. Name: `Tom yum soup`, protein: `Seafood`, add ingredients, etc.
3. Add **Instructions**
4. Choose collection **Thai** (or create it first) → **Save**

**Result**: The dish appears on the **Recipes** tab; the **Thai** collection shows the correct dish count.

**UI sketch**:

```text
[ Tab: Recipes ]  [ Tab: Collections ]

[ Search recipes...___________________________ ]

┌────────────────────────────────────────────┐
│ Tom yum soup                        [ x ] │
│ ★★★★☆   ·   Protein: Seafood              │
│ 5 ingredients  ·  Collection: Thai        │
└────────────────────────────────────────────┘

                                              [ + ]
```

### 5.2 RECIPE-02: Search when the list is long

**Goal**: Quickly filter dishes whose names contain “soup”.

**Steps**: Type `soup` in the search field — the list shows only matching dishes.

**UI sketch**:

```text
[ Search recipes...  soup____________________ ]

┌────────────────────────────────────────────┐
│ Tom yum soup                        [ x ] │
└────────────────────────────────────────────┘
```

## 6. Logic & rules

- **At least one ingredient** — the app blocks save until there is a valid ingredient row.
- **Dish in meal plan** — deleting a dish used in the plan shows a warning; confirming removes it from those meal slots.
- **Collections** are labels; one dish can belong to multiple collections.
- **Star rating** is stored per dish; you can change it from the list (tap stars).

## 7. Important notes

- **Premium**: **Recipes** (Kitchen & culinary) may show a Premium badge on **Functions** — an eligible subscription may be required.
- This guide is for end users; it does not describe file paths or database structure.
