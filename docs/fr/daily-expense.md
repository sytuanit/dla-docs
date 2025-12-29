# Dépenses Quotidiennes

## 1. Objectif

Le module **Dépenses Quotidiennes** vous aide à enregistrer les dépenses régulières non fixes telles que :
- Nourriture et restaurants
- Achats
- Transport
- Divertissement
- Autres dépenses flexibles

Contrairement aux **Dépenses Récurrentes**, les dépenses quotidiennes varient souvent en montant et en fréquence, sans cycle fixe.

## 2. Quand utiliser

Utilisez ce module si vous souhaitez :
- Enregistrer des dépenses aléatoires non récurrentes
- Suivre les dépenses quotidiennes pour contrôler le budget
- Analyser les tendances de dépenses par catégorie
- Afficher les dépenses totales sur une période

## 3. Écrans associés

- Liste des dépenses quotidiennes
- Ajouter une nouvelle dépense
- Modifier une dépense

## 4. Utilisation principale

### 4.1 Ajouter une dépense quotidienne

1. Allez à **Fonctions** → Sélectionnez **Dépenses Quotidiennes**
2. Appuyez sur le bouton **➕** (FAB) en bas à droite
3. Remplissez les informations :
   - **Catégorie** : Sélectionnez une catégorie (ou utilisez la catégorie par défaut, si configurée)
   - **Montant** : Entrez le montant dépensé
   - **Date** : Sélectionnez la date de la dépense (par défaut aujourd'hui)
   - **Note** : Description détaillée (optionnel)
4. Appuyez sur **Enregistrer**

### 4.2 Afficher la liste des dépenses

1. Allez à **Fonctions** → Sélectionnez **Dépenses Quotidiennes**
2. La liste s'affiche selon votre configuration d'affichage (2, 3 ou 4 colonnes)
3. Utilisez la **Recherche** pour filtrer par catégorie ou note
4. Sélectionnez le **Filtre temporel** : Aujourd'hui / Cette semaine / Ce mois / Mois dernier / Personnalisé

### 4.3 Modifier une dépense

1. Allez à la liste des dépenses quotidiennes
2. Appuyez longuement sur l'élément à modifier
3. Sélectionnez **Modifier** dans le menu
4. Mettez à jour les informations
5. Appuyez sur **Enregistrer**

### 4.4 Supprimer une dépense

1. Allez à la liste des dépenses quotidiennes
2. Appuyez longuement sur l'élément à supprimer
3. Sélectionnez **Supprimer** dans le menu
4. Confirmez la suppression

### 4.5 Définir une catégorie par défaut

1. Allez à **Paramètres** → **Catégories** → **Catégories des dépenses quotidiennes**
2. Appuyez sur la catégorie que vous souhaitez définir comme par défaut
3. Sélectionnez **Définir comme par défaut**
4. Lors de l'ajout d'une nouvelle dépense, cette catégorie sera automatiquement sélectionnée

## 5. Illustrations UI (Wireframe)

### 5.1 Écran de liste

```text
┌─────────────────────────────────────────┐
│  ← Retour    Dépenses Quotidiennes               │
├─────────────────────────────────────────┤
│  [🔍 Rechercher...]                         │
│  [Aujourd'hui ▼] [Cette semaine] [Ce mois]    │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Nourriture│ │Achats│ │ Taxi │            │
│  │ sortie  │ │      │ │      │            │
│  │      │ │      │ │      │            │
│  │ €1.80│ │ €7.20│ │ €0.90│            │
│  │      │ │      │ │      │            │
│  │ 15/11│ │ 15/11│ │ 14/11│            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Café│ │ Autres│ │      │            │
│  │     │ │      │ │      │            │
│  │      │ │      │ │      │            │
│  │ €0.90│ │ €3.60│ │      │            │
│  │      │ │      │ │      │            │
│  │ 13/11│ │ 12/11│ │      │            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  Total : €14.40                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Écran Ajouter/Modifier

```text
┌─────────────────────────────────────────┐
│  ← Retour    Ajouter une dépense quotidienne            │
├─────────────────────────────────────────┤
│  Catégorie *                              │
│  [Nourriture sortie ▼]                            │
│                                         │
│  Montant *                                │
│  [€1.80]                                   │
│                                         │
│  Date *                                  │
│  [15/11/2024]                           │
│                                         │
│  Note                                    │
│  [Déjeuner avec un ami]                     │
│                                         │
│  [Enregistrer] [Annuler]                        │
└─────────────────────────────────────────┘
```

### 5.3 Menu (Appui long)

```text
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐ │
│  │ Nourriture sortie                            │ │
│  │ €1.80                                  │ │
│  │ 15/11/2024                          │
│  │                                     │ │
│  │ [Modifier] [Supprimer]                    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logique et règles

### 6.1 Disposition d'affichage

- Vous pouvez configurer le nombre de colonnes : 2, 3 ou 4 colonnes
- La disposition est enregistrée dans les paramètres et s'applique à toutes les listes de dépenses

### 6.2 Filtre temporel

- **Aujourd'hui** : Affiche uniquement les dépenses d'aujourd'hui
- **Cette semaine** : Du début de la semaine à aujourd'hui
- **Ce mois** : Du début du mois à aujourd'hui
- **Mois dernier** : Mois précédent complet
- **Personnalisé** : Sélectionnez une période personnalisée

### 6.3 Recherche

- Recherche dans **Nom de catégorie** et **Note**
- Insensible à la casse
- Recherche en temps réel pendant la saisie

### 6.4 Catégorie par défaut

- Si vous avez défini une catégorie par défaut, elle sera automatiquement sélectionnée lors de l'ouverture de l'écran d'ajout
- La note peut également être remplie automatiquement en fonction de la catégorie (si configurée)

### 6.5 Dépenses totales

- Les dépenses totales sont calculées en fonction du filtre temporel actuellement sélectionné
- Affichées à la fin de la liste

## 7. Notes importantes

- **Pas de cycle** : Les dépenses quotidiennes n'ont pas de cycle automatique, vous devez les saisir manuellement à chaque fois
- **Peut être supprimé** : Vous pouvez supprimer n'importe quelle dépense (contrairement aux dépenses récurrentes)
- **Pas d'intégration au budget** : Les dépenses quotidiennes ne sont pas automatiquement calculées dans le budget (vous devez les suivre vous-même)
- **Catégories personnalisées** : Vous pouvez créer de nouvelles catégories dans les paramètres

