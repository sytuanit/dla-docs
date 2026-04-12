# Recettes

## 1. Objectif

Le module **Recettes** permet d’enregistrer des **recettes** (nom, ingrédients, préparation), des **types de protéines**, une **note par étoiles** et d’organiser les plats en **collections**. Les données sont partagées avec la **Planification des menus** pour chaque repas de la semaine.

## 2. Quand l’utiliser

- Carnet de recettes personnel.
- Regrouper les plats par thème via les **collections**.
- Préparer la **Planification des menus** — il faut au moins quelques plats enregistrés.

## 3. Écrans concernés

- **Fonctions** → **Cuisine et arts culinaires** → **Recettes**
- Onglets **Recettes** / **Collections**
- **Ajouter une recette** / **Modifier**
- **Détail de collection**

## 4. Utilisation principale

### 4.1 Liste et recherche

**Fonctions** → **Recettes** → **Rechercher des recettes...** ; onglet **Collections** avec recherche dédiée.

### 4.2 Nouvelle recette

**+** (FAB) → **Nom du plat** (obligatoire), **Types de protéines** (optionnel, virgules), **Note**, **Ingrédients** (au moins un nom), **Préparation**, **Collections** → **Enregistrer**.

### 4.3 Modifier / supprimer

Ouvrir un plat ; **Enregistrer**. **Supprimer** avec avertissement si le plat est dans un **menu hebdomadaire**.

### 4.4 Collections

**Collections** → **Créer une collection** ; ouvrir une collection → **Ajouter des recettes** ; **Renommer** / **Supprimer** (ne supprime pas les recettes).

## 5. Exemples & schémas

### 5.1 RECIPE-01

**Objectif** : enregistrer « Soupe tom yum » dans la collection « Thaï ».

```text
[ Recettes ]  [ Collections ]
[ Recherche...____________________________ ]

┌────────────────────────────────────────────┐
│ Soupe tom yum                      [ x ]  │
│ ★★★★☆  ·  Protéine : fruits de mer        │
│ 5 ingrédients  ·  Collection : Thaï       │
└────────────────────────────────────────────┘
                                             [ + ]
```

## 6. Logique

- **Au moins un ingrédient** requis.
- Suppression d’un plat utilisé dans le menu : confirmation ; retrait du plan.
- Plusieurs **collections** par plat possible.

## 7. Notes

- **Premium** possible sur **Fonctions**.
- Documentation utilisateur, sans chemins techniques.
