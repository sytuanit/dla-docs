# Budget

## 1. Objectif

Le module **Budget** vous aide à planifier et suivre les dépenses mensuelles et s'assure que vous ne dépassez pas votre budget établi. Ce module calcule automatiquement en fonction de :
- Vos revenus récurrents
- Vos dépenses récurrentes
- Dépenses quotidiennes réelles

## 2. Quand utiliser

Utilisez ce module si vous souhaitez :
- Planifier les dépenses mensuelles
- Contrôler que vous ne dépassez pas le budget
- Suivre le taux d'épargne
- Voir l'analyse des dépenses par catégorie
- Comparer les budgets entre les mois

## 3. Écrans associés

- Créer un budget (première fois ou copier du mois précédent)
- Afficher le résumé du budget
- Historique du budget par mois
- Suggestion de copie du mois précédent

## 4. Utilisation principale

### 4.1 Créer un budget pour la première fois (Cas A)

1. Allez à **Fonctions** → Sélectionnez **Budget**
2. Si aucun budget n'existe, l'application ouvre automatiquement l'écran **Créer un Budget**
3. L'application calcule et affiche automatiquement :
   - **Revenus Récurrents** : Total de tous les revenus récurrents actifs (lecture seule, affiche le détail)
   - **Dépenses Récurrentes** : Total de toutes les dépenses récurrentes actives (lecture seule, affiche le détail)
   - **Budget Total (avant épargne)** : Calculé automatiquement = Revenus Récurrents - Dépenses Récurrentes
4. Entrez le **Taux d'Épargne** : % d'épargne (0-100%, requis)
5. Affichez le **Montant d'Épargne** et le **Budget de Dépenses** calculés automatiquement
6. Appuyez sur **Enregistrer le Budget**

### 4.2 Copier le budget du mois précédent (Cas C)

1. Allez à **Fonctions** → Sélectionnez **Budget**
2. Si le mois actuel n'a pas de budget, mais le mois précédent en a un, l'application affiche l'écran **Suggestion de Copier le Budget**
3. Sélectionnez une des options :
   - **Copier tout le budget du mois précédent** : L'application copie automatiquement le taux d'épargne, recalcule les revenus/dépenses récurrents à partir des données actuelles et crée le budget immédiatement
   - **Copier et Ajuster** : L'application navigue vers l'écran Créer un Budget avec le taux d'épargne pré-rempli du mois précédent, vous pouvez ajuster avant d'enregistrer
   - **Créer un Nouveau Budget** : Exécuter le flux de création de budget depuis le début (Cas A)
4. Si "Copier et Ajuster" est sélectionné, ajustez le taux d'épargne si nécessaire
5. Appuyez sur **Enregistrer le Budget**

**Note** : Lors de la copie, les Revenus Récurrents et les Dépenses Récurrentes sont recalculés à partir des données récurrentes actuelles (non copiées du mois précédent), seul le taux d'épargne est copié.

### 4.3 Afficher le résumé du budget (Cas B)

1. Allez à **Fonctions** → Sélectionnez **Budget**
2. Si le mois actuel a un budget, l'application ouvre l'écran **Résumé**
3. Affichez les informations :
   - **Budget de Dépenses** : Limite de dépenses établie
   - **Utilisé** : Montant dépensé (y compris les dépenses quotidiennes et les écarts de revenus/dépenses)
   - **Restant** : Montant restant dans le budget
   - **Taux d'Utilisation** : % du budget utilisé (avec couleurs d'avertissement)
   - **Écarts de Revenus et Dépenses du Plan** : Déviations par rapport au plan original
   - **Dépenses Quotidiennes par Catégorie** : Analyse détaillée des dépenses par catégorie

### 4.4 Modifier le budget du mois actuel

1. Sur l'écran **Résumé du Budget**, appuyez sur le bouton **"Modifier le Budget"**
2. L'application affiche l'écran de modification avec :
   - **Revenus Récurrents** et **Dépenses Récurrentes** : Anciennes valeurs conservées (lecture seule)
   - **Taux d'Épargne** : Pré-rempli à partir du budget actuel (peut être modifié)
3. Modifiez le taux d'épargne si nécessaire
4. Affichez le montant d'épargne et le budget de dépenses mis à jour automatiquement
5. Appuyez sur **"Enregistrer le Budget"**

**Note** : Lors de la modification, les Revenus Récurrents et les Dépenses Récurrentes ne sont pas recalculés (l'ancien instantané est conservé), seuls le taux d'épargne et le budget de dépenses sont mis à jour.

### 4.5 Afficher l'historique du budget

1. Allez à **Fonctions** → Sélectionnez **Budget**
2. Sélectionnez **Historique** dans le menu
3. Affichez la liste des budgets pour les mois passés
4. Appuyez sur un mois pour voir les détails

### 4.6 Afficher les détails des dépenses par catégorie

1. Allez à l'écran **Résumé du Budget**
2. Faites défiler vers le bas jusqu'à la section **Analyse par Catégorie**
3. Appuyez sur une catégorie
4. Affichez la liste des dépenses dans cette catégorie

## 5. Exemples et illustrations UI

### 5.1 BUDGET-01 : Créer un budget pour la première fois pour le mois actuel

**Objectif** : Créer un budget pour la première fois afin que l'application calcule et suive automatiquement les dépenses mensuelles en fonction des revenus et dépenses récurrents.

**Étapes** :
1. Allez à l'écran Fonctions, sélectionnez "Gestion du Budget"
2. L'application détecte automatiquement qu'il n'y a pas de budget et affiche l'écran "Créer un Budget"
3. Affichez les informations calculées automatiquement : Revenus Récurrents, Dépenses Récurrentes, Budget Total (avant épargne)
4. Entrez le taux d'épargne : 20
5. Affichez le montant d'épargne et le budget de dépenses calculés automatiquement
6. Appuyez sur le bouton "Enregistrer le Budget"

**Résultat** : Budget enregistré pour le mois actuel, navigue automatiquement vers l'écran "Résumé du Budget".

**Illustration UI** :

```text
[ Carte : Créer Budget Novembre 2025 ]
+------------------------------------------------+
||                                                |
|| Revenus Récurrents                €1,080         |
||  • Mon Salaire (Mensuel)         €1,080         |
||                                                |
|| Dépenses Récurrentes              €824          |
||  • Électricité (Mensuel)          €31        |
||  • Eau (Mensuel)                €15        |
||  • Frais de scolarité pour BN (Mensuel)       €245       |
||  • Petit-déjeuner et Café (Hebdomadaire x 4) €32       |
||  • Prêt Immobilier (Mensuel)     €378      |
||                                                |
|| (Ces données sont récupérées automatiquement)        |
+------------------------------------------------+

[ Carte : Budget Total (avant épargne) ]
 ------------------------------------------------
||   €1,080 (Revenus Récurrents)                   |
|| - €824 (Dépenses Récurrentes)                    |
||-----------------------------------------------|
|| = €256 EUR                                     |
 ------------------------------------------------

[ Carte : Taux d'Épargne ]
 ------------------------------------------------
|| Combien souhaitez-vous épargner ?                 |
||                                                |
|| Taux d'Épargne (%)                               |
|| [  Entrée (requis) : 20  ]                    |
||                                                |
|| → Équivaut à : €51                              |
 ------------------------------------------------

[ Carte : Budget de Dépenses ]
 ------------------------------------------------
||    €256 (Budget Total (avant épargne))       |
|| -  €51 (Montant d'Épargne)                        |
||-----------------------------------------------|
|| = €204 EUR                                     |
||                                                |
|| (Inclut nourriture, transport, café, petits achats...)
 ------------------------------------------------

[ Bouton ]
 -------------------------------
||      Enregistrer le Budget              |
 -------------------------------
```

---

### 5.2 BUDGET-02 : Afficher le résumé du budget du mois actuel

**Objectif** : Afficher la situation des dépenses par rapport au budget établi, y compris les montants utilisés, les montants restants et l'analyse par catégorie.

**Étapes** :
1. Allez à l'écran Fonctions, sélectionnez "Gestion du Budget"
2. L'application détecte automatiquement qu'un budget existe et affiche l'écran "Résumé du Budget"
3. Affichez la Carte 1 - Budget Mensuel : Budget de Dépenses, Utilisé, Restant, Taux d'Utilisation
4. Affichez la Carte 2 - Écarts de Revenus et Dépenses du Plan
5. Affichez la Carte 3 - Dépenses Quotidiennes par Catégorie
6. (Optionnel) Cliquez sur "Budget de Dépenses ›" pour afficher le dialogue détaillé avec le calcul du budget

**Résultat** : Affiche les informations complètes du budget du mois actuel avec barre/anneau de progression et couleurs appropriées.

**Illustration UI** :

```text
[ Carte 1 – Budget Novembre 2025 ]
┌──────────────────────────────────────────────┐
│ Budget Novembre 2025                         │
│                                             │
│ Budget de Dépenses ›      €204                 │
│ Utilisé                  €32                   │
│  • Dépenses Quotidiennes              €43          │   
│  • Écart de Revenus      -€144              │
│  • Écart de Dépenses       +€7               │
│ Restant              €94                 │
│                                             │
│                    15.4%                    │
│   (Vous avez utilisé 15.4% du budget de dépenses de ce mois)
│   (Vous êtes en train d'épuiser le budget de dépenses de ce mois)
│                                             │
│                               [Voir Historique]│
└──────────────────────────────────────────────┘

[ Carte 2 – Écarts de Revenus et Dépenses du Plan ]
┌──────────────────────────────────────────────┐
│ Écarts de Revenus et Dépenses du Plan        │
│                                              │
│ Revenus Récurrents                             │
│  • Mon Salaire                 +€72           │
│    (€432 > €360)                             │
│                                              │
│ Dépenses Récurrentes                           │
│  • Frais de scolarité pour BN              -€4          │
│    (€245 > €252)                             │
│                                              │
│ Écart Total de Revenus :        +€216          │
│ Écart Total de Dépenses :        -€7          │
└──────────────────────────────────────────────┘

[ Carte 3 – Dépenses Quotidiennes par Catégorie ]
┌──────────────────────────────────────────────┐
│ Dépenses Quotidiennes par Catégorie                   │
│ (Nourriture, Transport, Café, petits achats...)
│                                             │
│ Dépenses Quotidiennes Totales : €43                    │
│                                             │
│ Nourriture              €22    50% [█████---------]│
│ Transport     €11    25% [███-----------]│
│ Café             €7     17% [██------------]│
│ Petits Achats     €4     8%  [█-------------]│
└──────────────────────────────────────────────┘
```

---

### 5.3 BUDGET-03 : Modifier le budget du mois actuel

**Objectif** : Ajuster le taux d'épargne pour modifier le budget de dépenses du mois actuel.

**Étapes** :
1. Sur l'écran "Résumé du Budget", appuyez sur le bouton "Modifier le Budget"
2. L'application affiche l'écran de modification (similaire à l'écran Créer un Budget)
3. Affichez les informations actuelles : Revenus Récurrents, Dépenses Récurrentes (anciennes valeurs conservées)
4. Modifiez le taux d'épargne à 25
5. Affichez le montant d'épargne et le budget de dépenses mis à jour automatiquement
6. Appuyez sur le bouton "Enregistrer le Budget"

**Résultat** : Budget mis à jour, retourne à l'écran "Résumé du Budget" avec les nouvelles valeurs.

**Illustration UI** : Similaire à BUDGET-01 (écran Créer un Budget), mais les valeurs de Revenus Récurrents et Dépenses Récurrentes sont en lecture seule et conservées de l'ancien budget.

---

### 5.4 BUDGET-04 : Copier le budget du mois précédent lorsque le nouveau mois commence

**Objectif** : Réutiliser le budget du mois précédent pour gagner du temps lors de la création d'un nouveau budget, avec option d'ajustement si nécessaire.

**Étapes** :
1. Allez à l'écran Fonctions, sélectionnez "Gestion du Budget"
2. L'application détecte automatiquement que le mois actuel n'a pas de budget, mais le mois précédent en a un, affiche l'écran "Suggestion de Copier le Budget"
3. Sélectionnez "Copier et Ajuster"
4. L'application navigue vers l'écran Créer un Budget avec le taux d'épargne pré-rempli du mois précédent
5. (Optionnel) Ajustez le taux d'épargne si nécessaire
6. Appuyez sur le bouton "Enregistrer le Budget"

**Résultat** : Nouveau budget créé pour le mois actuel, navigue automatiquement vers l'écran "Résumé du Budget".

**Illustration UI** :

```text
[ ÉCRAN ]  Budget Décembre 2025
┌──────────────────────────────────────────────┐
│ Décembre 2025 n'a pas de budget                 │
│                                              │
│ Comment souhaitez-vous créer le budget du nouveau mois ?│
├──────────────────────────────────────────────┤
│                                              │
│ 📝 Copier et Ajuster ›                          │
│    Note : Copier et ajuster le budget Novembre 2025│
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│ ➕ Créer un Nouveau Budget ›                      │
│   Note : Exécuter le flux de création de budget à nouveau        │
│                                              │
└──────────────────────────────────────────────┘
```

Après avoir sélectionné "Copier et Ajuster", l'écran Créer un Budget s'affiche de manière similaire à BUDGET-01, mais le taux d'épargne est pré-rempli du mois précédent.

## 6. Logique et règles

### 6.1 Cas

- **Cas A** : Créer un budget pour la première fois (aucun budget pour aucun mois)
- **Cas B** : Le mois actuel a un budget → Afficher le résumé
- **Cas C** : Le mois actuel n'en a pas, mais le mois précédent en a un → Suggestion de copie

### 6.2 Calcul automatique

- **Revenus Récurrents** : Total de tous les `recurring_income` actifs
- **Dépenses Récurrentes** : Total de toutes les `recurring_expense` actives
- **Dépenses Quotidiennes** : Total des `daily_expense` du mois
- **Budget Total** : Revenus Récurrents + Revenus Supplémentaires
- **Épargne** : Budget Total × Taux d'Épargne

### 6.3 Intégration avec d'autres modules

- Lors de la confirmation d'un revenu récurrent → Mettre à jour le budget automatiquement
- Lors de la confirmation d'une dépense récurrente → Mettre à jour le budget automatiquement
- Les dépenses quotidiennes sont automatiquement calculées dans le budget

### 6.4 Avertissement de dépassement du budget

- L'application affiche un avertissement lorsque les dépenses dépassent le budget
- L'avertissement est affiché sur l'écran d'accueil et dans les notifications

### 6.5 Instantané

- Lors de la création du budget, l'application crée un instantané des éléments de revenus/dépenses pour enregistrer l'état à ce moment-là
- L'instantané est utilisé pour la comparaison et l'analyse

## 7. Notes importantes

- **Un budget par mois** : Vous devez créer un budget pour chaque mois
- **Modifier le budget** : Vous pouvez modifier le budget du mois actuel en changeant le taux d'épargne. Les Revenus Récurrents et les Dépenses Récurrentes restent inchangés (instantané), pour assurer la précision
- **Mise à jour automatique** : Le budget se met à jour automatiquement lorsque vous confirmez les revenus/dépenses
- **Copier du mois précédent** : La fonction de copie vous aide à gagner du temps lors de la création du budget

