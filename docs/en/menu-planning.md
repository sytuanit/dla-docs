# Menu planning

## 1. Purpose

**Menu planning** (weekly meal planning) lets you place **saved dishes** from **Recipes** into **Breakfast / Lunch / Dinner** for each day (Monday–Sunday), mark **no-cooking days**, view a **weekly summary** (protein, repeated dishes), and **copy** from an existing week to save time.

## 2. When to use it

- You want a full week of meals before shopping.
- You want to agree “what’s for dinner” with your household.
- You already have **at least one recipe** in **Recipes** (required to create a new weekly plan).

## 3. Related screens

- **Functions** → **Menu planning** — list of **weekly meal plans** (status: upcoming / current / past)
- **Create weekly meal plan** — pick week start date (7 days Mon–Sun), optional copy from another week
- **Meal plan detail** — grid by day and meal; add dishes, outside meals, no-cooking days; weekly summary; previous week

## 4. Main usage

### 4.1 Create a new weekly plan

1. Go to **Functions** → **Menu planning**.
2. Tap **Create weekly meal plan** (or the empty-state button).
3. Choose **Week start date** (the week spans 7 consecutive days Mon–Sun as defined in the app).
4. (Optional) Enable **Copy from an existing plan** and pick a source week — meals are copied (you can edit after).
5. If the new week **overlaps dates** with an existing plan, the app shows an error — pick another range or delete/edit the old plan.
6. Confirm — opens **meal plan detail**.

**Note**: If you have **no recipes** yet, the app blocks creating a plan and asks you to add recipes first.

### 4.2 Add dishes to each meal

1. In **meal plan detail**, tap **Breakfast / Lunch / Dinner** for a day.
2. **Pick a recipe** opens — search **Recipes** and tap to select.
3. (Optional) **Add outside meal** (free text, e.g. pho, burgers) when not cooking at home.
4. Repeat for other slots.

### 4.3 No-cooking day

1. Use **No cooking this day** for that date.
2. (Optional) **Reason** — the app warns that all dishes on that day will be removed from the plan.
3. You can **Turn cooking back on** to clear the day-off state.

### 4.4 Weekly summary and previous week

1. **Weekly summary** — statistics such as protein types, dishes cooked often vs once (per on-screen labels).
2. **Previous week** — opens summary or reference for the adjacent week (per app flow).

### 4.5 Delete a meal plan

1. From the plan list, delete (icon/menu) for one week.
2. Confirm — that week is removed.

**Limit**: With **12 meal plans** stored, creating another may show a limit dialog (the oldest week may be removed — see the in-app message).

## 5. Examples & UI sketches

### 5.1 MEAL-01: Create a week and add lunch

**Goal**: Plan the current week with at least Tuesday lunch filled.

**Steps**:
1. Menu planning → **Create weekly meal plan** → pick a valid start date
2. **Lunch** on **Tuesday** → **Add dish** → pick “Tom yum soup”
3. **Save** / back per app flow

**UI sketch**:

```text
[ Weekly plan: 01/03 – 01/09 ]     [🟢 Current]

        Mon     Tue     Wed   ...
Breakfast [+]     [+]     [+]
Lunch     [+]   [Tom yum] [+]
Dinner    [+]     [+]     [+]
```

### 5.2 MEAL-02: Eating out

**Goal**: Saturday — no home cooking; record as day off or outside meal.

**Steps**: On **Saturday** → **No cooking this day** (reason: “Party”) **or** add **Outside meal** to a slot.

## 6. Logic & rules

- **One week = 7 days** with start/end dates; status **upcoming / current / past** is based on today’s date.
- **No overlapping date ranges** with another saved plan.
- **In-app dishes** always come from **Recipes**; **outside meals** are free text with an “outside” style label.
- **12-plan limit** — at the cap, the app may offer to remove the oldest week to create a new one (see dialog).

## 7. Important notes

- **Premium**: **Menu planning** is under Kitchen & culinary; a Premium badge may appear on **Functions**.
- You need **recipes** in **Recipes** before creating a new weekly plan.
- If something is unclear on your app build, rely on on-screen buttons and messages.
