# Revenus Supplémentaires

## 1. Objectif

Le module **Revenus Supplémentaires** vous aide à enregistrer les revenus non récurrents sans cycle fixe tels que :
- Ventes en ligne
- Freelance
- Bonus
- Cadeaux en espèces
- Autres revenus irréguliers

Contrairement aux **Revenus Récurrents**, les revenus supplémentaires n'ont pas de cycle automatique, vous devez les saisir manuellement à chaque fois.

## 2. Quand utiliser

Utilisez ce module si vous souhaitez :
- Enregistrer des revenus aléatoires non récurrents
- Suivre les revenus totaux sur une période
- Analyser les tendances des revenus supplémentaires
- Calculer dans le budget mensuel

## 3. Écrans associés

- Liste des revenus supplémentaires
- Ajouter un nouveau revenu
- Modifier un revenu

## 4. Utilisation principale

### 4.1 Ajouter un revenu supplémentaire

1. Allez à **Fonctions** → Sélectionnez **Revenus Supplémentaires**
2. Appuyez sur le bouton **➕** (FAB) en bas à droite
3. Remplissez les informations :
   - **Catégorie** : Sélectionnez une catégorie ou créez-en une nouvelle
   - **Montant** : Entrez le montant reçu
   - **Date** : Sélectionnez la date à laquelle l'argent a été reçu (par défaut aujourd'hui)
   - **Note** : Description détaillée (optionnel)
4. Appuyez sur **Enregistrer**

### 4.2 Afficher la liste des revenus

1. Allez à **Fonctions** → Sélectionnez **Revenus Supplémentaires**
2. La liste s'affiche selon votre configuration d'affichage (1, 2, 3 ou 4 colonnes)
3. Utilisez la **Recherche** pour filtrer par catégorie ou note
4. Sélectionnez le **Filtre temporel** : Aujourd'hui / Cette semaine / Ce mois / Mois dernier / Personnalisé

### 4.3 Modifier un revenu

1. Allez à la liste des revenus supplémentaires
2. Appuyez longuement sur l'élément à modifier
3. Sélectionnez **Modifier** dans le menu
4. Mettez à jour les informations
5. Appuyez sur **Enregistrer**

### 4.4 Supprimer un revenu

1. Allez à la liste des revenus supplémentaires
2. Appuyez longuement sur l'élément à supprimer
3. Sélectionnez **Supprimer** dans le menu
4. Confirmez la suppression

## 5. Illustrations UI (Wireframe)

### 5.1 Écran de liste

```text
┌─────────────────────────────────────────┐
│  ← Retour    Revenus Supplémentaires                 │
├─────────────────────────────────────────┤
│  [🔍 Rechercher...]                         │
│  [Ce mois ▼] [Cette semaine] [Aujourd'hui]     │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Ventes en ligne                        │ │
│  │ €18                                 │ │
│  │ 15/11/2024                          │ │
│  │                                    │ │
│  │ [Modifier] [Supprimer]                    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Freelance                           │ │
│  │ €36                                 │ │
│  │ 14/11/2024                          │ │
│  │                                    │ │
│  │ [Modifier] [Supprimer]                    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Total : €54                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Écran Ajouter/Modifier

```text
┌─────────────────────────────────────────┐
│  ← Retour    Ajouter un revenu supplémentaire             │
├─────────────────────────────────────────┤
│  Catégorie *                              │
│  [Ventes en ligne ▼]                        │
│                                         │
│  Montant *                                │
│  [€18]                                  │
│                                         │
│  Date *                                  │
│  [15/11/2024]                           │
│                                         │
│  Note                                    │
│  [Produit A vendu]                        │
│                                         │
│  [Enregistrer] [Annuler]                        │
└─────────────────────────────────────────┘
```

## 6. Logique et règles

### 6.1 Disposition d'affichage

- Vous pouvez configurer le nombre de colonnes : 1, 2, 3 ou 4 colonnes
- La disposition est enregistrée dans les paramètres et s'applique à toutes les listes de revenus supplémentaires

### 6.2 Filtre temporel

- **Aujourd'hui** : Affiche uniquement les revenus d'aujourd'hui
- **Cette semaine** : Du début de la semaine à aujourd'hui
- **Ce mois** : Du début du mois à aujourd'hui
- **Mois dernier** : Mois précédent complet
- **Personnalisé** : Sélectionnez une période personnalisée

### 6.3 Recherche

- Recherche dans **Nom de catégorie** et **Note**
- Insensible à la casse
- Recherche en temps réel pendant la saisie

### 6.4 Intégration au budget

- Les revenus supplémentaires sont calculés dans "Revenus Supplémentaires" dans le budget
- Vous aide à suivre le revenu mensuel total

## 7. Notes importantes

- **Pas de cycle** : Les revenus supplémentaires n'ont pas de cycle automatique, vous devez les saisir manuellement à chaque fois
- **Peut être supprimé** : Vous pouvez supprimer n'importe quel revenu
- **Intégration au budget** : Les revenus supplémentaires sont automatiquement calculés dans le budget du mois en cours

