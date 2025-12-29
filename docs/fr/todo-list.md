# Liste de tâches

## 1. Objectif

Le module **Liste de tâches** vous aide à gérer les tâches récurrentes et à suivre les progrès de réalisation, notamment :
- Tâches récurrentes basées sur le temps (quotidiennes/hebdomadaires/mensuelles/annuelles)
- Tâches récurrentes basées sur des métriques (miles/heures/fois...)
- Rappels à l'échéance
- Suivi de l'historique de réalisation
- Enregistrement des dépenses (le cas échéant)

Ce module vous aide à ne jamais manquer des tâches importantes comme l'entretien de la voiture, le remplacement des filtres, les contrôles périodiques, etc.

## 2. Quand utiliser

Utilisez ce module lorsque vous avez :
- Des tâches qui se répètent selon un calendrier (par exemple, remplacer le filtre à eau tous les 3 mois)
- Des tâches qui se répètent en fonction de métriques (par exemple, changer l'huile de la voiture tous les 3 000 miles)
- Besoin de rappels automatiques à l'échéance
- Souhaitez suivre l'historique de réalisation
- Besoin d'enregistrer les dépenses associées

## 3. Écrans associés

- Écran de liste de tâches
- Sélectionner le type de tâche (Basée sur le temps / Basée sur des métriques)
- Ajouter une nouvelle tâche
- Modifier une tâche
- Confirmer une tâche basée sur des métriques
- Historique des tâches
- Liste des tâches à faire (liste de cloche)

## 4. Utilisation principale

### 4.1 Ajouter une tâche basée sur le temps

1. Allez à **Fonctions** → Sélectionnez **Liste de tâches**
2. Appuyez sur le bouton **+** (FAB) en bas à droite
3. Sélectionnez **Tâche basée sur le temps**
4. Remplissez les informations :
   - **Nom de la tâche** : (obligatoire, par exemple "Remplacer le filtre à eau")
   - **Cycle de récurrence** : Entrez un nombre et sélectionnez l'unité (Jour/Semaine/Mois/Année)
   - **Prochaine date d'échéance** : Sélectionnez une date (permet uniquement de sélectionner à partir de demain)
   - **Heure de rappel** : Sélectionnez une heure (obligatoire, par exemple 08:00)
   - **Cette tâche entraîne des dépenses** : (Optionnel) Cochez si des dépenses sont impliquées
     - Si coché : Sélectionnez **Catégorie** (obligatoire)
   - **Note** : Informations supplémentaires (optionnel)
5. Appuyez sur **Enregistrer**

### 4.2 Ajouter une tâche basée sur des métriques

1. Allez à **Fonctions** → Sélectionnez **Liste de tâches**
2. Appuyez sur le bouton **+** (FAB)
3. Sélectionnez **Tâche basée sur des métriques**
4. Remplissez les informations :
   - **Nom de la tâche** : (obligatoire, par exemple "Changer l'huile de la voiture")
   - **Cycle** : Entrez un nombre (par exemple 3,000)
   - **Unité** : Entrez l'unité (par exemple "Miles")
   - **Dernière valeur métrique réalisée** : Entrez la valeur actuelle (par exemple 12,500)
   - **Cette tâche entraîne des dépenses** : (Optionnel) Cochez si des dépenses sont impliquées
     - Si coché : Sélectionnez **Catégorie** (obligatoire)
   - **Note** : Informations supplémentaires (optionnel)
5. Appuyez sur **Enregistrer**

### 4.3 Confirmer une tâche basée sur des métriques

1. Allez à la liste de tâches
2. Trouvez la tâche basée sur des métriques (type METRIC) à confirmer
3. Appuyez sur le bouton **Confirmer** dans la carte (affiché uniquement lorsque `isActive = true`)
4. Remplissez les informations :
   - **Valeur métrique actuelle** : Entrez la valeur actuelle (obligatoire, doit être ≥ dernière valeur métrique réalisée)
   - **Note** : (Optionnel)
5. Affichez le **Delta** calculé automatiquement (valeur actuelle - dernière valeur réalisée)
6. Appuyez sur **Confirmé**
7. (Si la tâche a des dépenses) Sélectionnez **Ajouter une dépense** ou **Annuler**

**Note** : Les tâches basées sur le temps (type CYCLE) n'ont pas de bouton "Confirmer" dans la carte. La confirmation se fait uniquement dans l'écran "Tâches à faire" (liste de cloche).

### 4.4 Afficher la liste et les détails

1. Allez à **Fonctions** → Sélectionnez **Liste de tâches**
2. Utilisez la **Barre de recherche** pour rechercher par nom de tâche
3. Utilisez les **Puces de filtre** pour filtrer :
   - **Tout** : Afficher toutes les tâches
   - **Basée sur le temps** : Afficher uniquement les tâches de type CYCLE
   - **Basée sur des métriques** : Afficher uniquement les tâches de type METRIC
4. Appuyez sur une carte de tâche pour afficher les détails et modifier

### 4.5 Modifier une tâche

1. Allez à la liste de tâches
2. Appuyez sur la carte de tâche pour modifier
3. Mettez à jour les informations :
   - **Note** : S'il y a un historique, **Cycle** (CYCLE) ou **Unité/Cycle** (METRIC) sera verrouillé et ne pourra pas être modifié
4. Appuyez sur **Enregistrer**

### 4.6 Afficher l'historique

1. Allez à la liste de tâches
2. Appuyez sur le lien **Afficher l'historique ›** de la tâche à afficher
3. Utilisez les **Puces de filtre** pour filtrer par temps :
   - **Tout** : Afficher tout l'historique
   - **Ce mois** : Afficher uniquement l'historique du mois en cours
   - **Mois dernier** : Afficher uniquement l'historique du mois précédent
   - **3 derniers mois** : Afficher uniquement l'historique des 3 derniers mois

### 4.7 Désactiver/Activer une tâche

1. Allez à la liste de tâches
2. Trouvez la tâche à désactiver/activer
3. Basculez l'interrupteur **Actif** dans le pied de page de la carte
4. Les tâches désactivées afficheront un badge **"Inactif"** (gris)

### 4.8 Supprimer une tâche

1. Allez à la liste de tâches
2. Appuyez sur l'icône **Supprimer** (🗑️) dans l'en-tête de la carte
3. Confirmez la suppression dans la boîte de dialogue
4. La tâche et tout l'historique associé seront supprimés

## 5. Exemples et illustrations de l'interface utilisateur

### TODO-01 : Créer une tâche basée sur le temps (Remplacer le filtre à eau)

**Objectif** : Créer une tâche basée sur le temps pour que l'application vous rappelle automatiquement à l'échéance.

**Étapes principales** :
1. Allez à Fonctions → Liste de tâches → Appuyez sur le bouton "+" (FAB)
2. Sélectionnez "Tâche basée sur le temps"
3. Entrez le nom de la tâche : "Remplacer le filtre à eau"
4. Entrez le cycle : "3" mois
5. Sélectionnez la prochaine date d'échéance : 03/01/2026
6. Sélectionnez l'heure de rappel : 08:00
7. Cochez "Cette tâche entraîne des dépenses", sélectionnez la catégorie "Services publics"
8. Entrez la note : "Remplacer le filtre #1 et #2"
9. Appuyez sur "Enregistrer"

**Schéma filaire - Écran Ajouter une tâche basée sur le temps** :

```text
┌──────────────────────────────────────────────┐
│ <  Ajouter une tâche basée sur le temps     │
├──────────────────────────────────────────────┤

Nom de la tâche
[ Remplacer le filtre à eau            ]

Cycle de récurrence
Tous les [ 3 ] [ Mois ▼ ]
(Unité : Jour / Semaine / Mois / Année)

Prochaine date d'échéance
[ 03 / 01 / 2026    ▼ ]
Indication : 
Date d'échéance pour la première fois.
Les dates suivantes seront automatiquement calculées en fonction du cycle que vous avez entré.

Heure de rappel
[ 08 : 00           ▼ ]

──────────────────────────────────────────────
[✓] Cette tâche entraîne des dépenses

┌─────────────────────────────────────┐
│ Catégorie *                          │
│ [Services publics ▼] [+ Créer nouveau]│
└─────────────────────────────────────┘

──────────────────────────────────────────────
Note (optionnel)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Annuler ]                         [ Enregistrer ]
└──────────────────────────────────────────────┘
```

---

### TODO-02 : Créer une tâche basée sur des métriques (Changer l'huile de la voiture)

**Objectif** : Créer une tâche basée sur des métriques pour suivre l'entretien de la voiture en fonction du kilométrage.

**Étapes principales** :
1. Allez à Fonctions → Liste de tâches → Appuyez sur le bouton "+" (FAB)
2. Sélectionnez "Tâche basée sur des métriques"
3. Entrez le nom de la tâche : "Changer l'huile de la voiture"
4. Entrez le cycle : "3,000", unité : "Miles"
5. Entrez la dernière valeur métrique réalisée : "12,500"
6. Cochez "Cette tâche entraîne des dépenses", sélectionnez la catégorie "Entretien voiture"
7. Entrez la note : "Changer l'huile + filtre à huile"
8. Appuyez sur "Enregistrer"

**Schéma filaire - Écran Ajouter une tâche basée sur des métriques** :

```text
┌──────────────────────────────────────────────┐
│ <  Ajouter une tâche basée sur des métriques │
├──────────────────────────────────────────────┤

Nom de la tâche
[ Changer l'huile de la voiture            ]

Cycle
Tous les [ 3,000 ] Unité [ Miles ]
(Unité : Miles / Heures / Fois / ...)

Dernière valeur métrique réalisée
[ 12,500 ]

──────────────────────────────────────────────
[✓] Cette tâche entraîne des dépenses

┌─────────────────────────────────────┐
│ Catégorie *                          │
│ [Entretien voiture ▼] [+ Créer nouveau]│
└─────────────────────────────────────┘

──────────────────────────────────────────────
Note (optionnel)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Annuler ]                         [ Enregistrer ]
└──────────────────────────────────────────────┘
```

---

### TODO-03 : Afficher la liste et les détails

**Objectif** : Afficher un aperçu des tâches, filtrer par type, rechercher et afficher les détails de chaque tâche.

**Étapes principales** :
1. Allez à Fonctions → Liste de tâches
2. Affichez la liste avec la barre de recherche et les puces de filtre
3. Utilisez les filtres : "Tout", "Basée sur le temps", "Basée sur des métriques"
4. Utilisez la barre de recherche pour rechercher par nom de tâche
5. Appuyez sur une carte de tâche pour afficher les détails

**Schéma filaire - Écran Liste de tâches** :

```text
┌─────────────────────────────────────────────────────────┐
│  [← Retour]  Liste de tâches                  [🔔]        │
└─────────────────────────────────────────────────────────┘
│  🔍 Rechercher...                                        │
│                                                          │
│  [Tout] [Basée sur le temps] [Basée sur des métriques] │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Carte : Remplacer le filtre à eau                │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Remplacer le filtre à eau    [Terminé] [🗑️] │ │    │
│  │ │                                              │ │    │
│  │ │ 📅 Cycle : Tous les 3 mois                   │ │    │
│  │ │ ✅ Dernière réalisation : 12/01/2025         │ │    │
│  │ │ 📅 Prochaine date d'échéance : 03/01/2026    │ │    │
│  │ │ ⏳ 76 jours restants                          │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Afficher l'historique ›           [⚪ Actif] │ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Carte : Changer l'huile de la voiture           │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Changer l'huile de la voiture   [🗑️]       │ │    │
│  │ │                                              │ │    │
│  │ │ 📏 Suivi par : Miles                         │ │    │
│  │ │ ✅ Dernière confirmation : 12/02/2025       │ │    │
│  │ │ 🔢 Dernière valeur métrique : 12,500 miles  │ │    │
│  │ │ 🎯 Prochaine échéance : 14,500 miles         │ │    │
│  │ │ ⏳ ~300 miles restants                       │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ [✓ Confirmer]                                │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Afficher l'historique ›           [⚪ Actif] │ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ FAB]                                                 │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-04 : Confirmer une tâche basée sur des métriques (Changer l'huile de la voiture)

**Objectif** : Confirmer la réalisation d'une tâche basée sur des métriques en entrant la valeur métrique actuelle.

**Étapes principales** :
1. Allez à la liste de tâches
2. Trouvez la tâche "Changer l'huile de la voiture" (type METRIC)
3. Appuyez sur le bouton "Confirmer"
4. Entrez la valeur métrique actuelle : "14,520"
5. Affichez le delta calculé automatiquement : "+2,020 miles"
6. Entrez la note : "Huile changée + filtre à huile"
7. Appuyez sur "Confirmé"

**Schéma filaire - Boîte de dialogue Confirmer une tâche basée sur des métriques** :

```text
┌──────────────────────────────────────────────┐
│  Confirmer une tâche basée sur des métriques │
├──────────────────────────────────────────────┤

Nom de la tâche :
Changer l'huile de la voiture   (lecture seule)

Suivi par :
Miles   (lecture seule)

Dernière valeur métrique réalisée :
12,500 Miles   (lecture seule)

──────────────────────────────────────────────
Valeur métrique actuelle
[ 14,520 ] Miles

Delta :
+2,020 Miles   (automatique)

──────────────────────────────────────────────
Note
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
        [ Non confirmé ]    [ Confirmé ]
└──────────────────────────────────────────────┘
```

---

### TODO-05 : Modifier une tâche et afficher l'historique

**Objectif** : Modifier les informations d'une tâche et afficher l'historique de réalisation.

**Étapes principales** :
1. Allez à la liste de tâches
2. Appuyez sur la carte de tâche "Remplacer le filtre à eau"
3. Affichez l'avertissement : "⚠️ Le cycle est verrouillé car il y a un historique" (s'il y a un historique)
4. Modifiez la prochaine date d'échéance, l'heure de rappel, la note
5. Appuyez sur "Enregistrer"
6. Appuyez sur "Afficher l'historique ›" pour afficher l'historique avec les filtres

**Schéma filaire - Écran Historique des tâches** :

```text
┌─────────────────────────────────────────────────────────┐
│  [← Retour]  Historique des tâches - Remplacer le filtre à eau│
└─────────────────────────────────────────────────────────┘
│  [Tout] [Ce mois] [Mois dernier] [3 derniers mois]      │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Remplacer le filtre à eau        [Terminé]      │    │
│  │                                                  │    │
│  │ 📅 Cycle : Tous les 3 mois                       │    │
│  │ ✅ Réalisé le : 12/01/2025 – 09:10             │    │
│  │ 📝 Note : Remplacer le filtre #1 et #2           │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Remplacer le filtre à eau        [Terminé]      │    │
│  │                                                  │    │
│  │ 📅 Cycle : Tous les 3 mois                       │    │
│  │ ✅ Réalisé le : 09/01/2025 – 08:45             │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-06 : Désactiver et supprimer une tâche

**Objectif** : Désactiver ou supprimer une tâche lorsqu'elle n'est plus nécessaire.

**Étapes principales** :
1. Allez à la liste de tâches
2. Trouvez la tâche à désactiver
3. Appuyez sur l'interrupteur "Actif" pour l'éteindre
4. Affichez le badge "Inactif" apparaître
5. Appuyez à nouveau sur l'interrupteur pour réactiver
6. Appuyez sur l'icône Supprimer (🗑️) pour supprimer la tâche
7. Confirmez la suppression dans la boîte de dialogue

---

### TODO-07 : Confirmer une tâche basée sur des métriques et ajouter une dépense

**Objectif** : Confirmer une tâche basée sur des métriques et ajouter automatiquement la dépense associée.

**Étapes principales** :
1. Allez à la liste de tâches
2. Trouvez la tâche "Changer l'huile de la voiture" (type METRIC, hasCost = true)
3. Appuyez sur le bouton "Confirmer"
4. Entrez la valeur métrique actuelle : "14,520"
5. Entrez la note : "Huile changée + filtre à huile"
6. Appuyez sur "Confirmé"
7. Affichez la boîte de dialogue "Dépense engagée ?" s'ouvrir automatiquement
8. Appuyez sur "Ajouter une dépense"
9. Affichez l'écran "Ajouter une dépense" avec la note et la catégorie pré-remplies
10. Entrez le montant : 45 EUR
11. Appuyez sur "Enregistrer"

**Schéma filaire - Boîte de dialogue Dépense engagée** :

```text
┌──────────────────────────────────────────────┐
│  Dépense engagée ?                           │
├──────────────────────────────────────────────┤
Voulez-vous ajouter une dépense pour cette
réalisation ?

        [ Annuler ]         [ Ajouter une dépense ]
└──────────────────────────────────────────────┘
```

## 6. Logique et règles

### 6.1 Types de tâches

- **Basée sur le temps (type CYCLE)** :
  - Se répète selon un calendrier (Jour/Semaine/Mois/Année)
  - A des notifications de rappel à l'échéance
  - La confirmation se fait uniquement dans l'écran "Tâches à faire" (liste de cloche)
  - Pas de bouton "Confirmer" dans la carte

- **Basée sur des métriques (type METRIC)** :
  - Se répète en fonction de jalons métriques (Miles/Heures/Fois/Autre)
  - Pas de notifications (MVP1)
  - A un bouton "Confirmer" dans la carte (affiché uniquement lorsque `isActive = true`)
  - Confirmation en entrant la valeur métrique actuelle

### 6.2 Statut des tâches

- **EN ATTENTE** : À venir (pas encore due)
  - Pas de badge affiché : `nextDueDate - today > 7 jours`
  - Afficher le badge "À venir" (jaune) : `0 < nextDueDate - today ≤ 7 jours`
- **EN RETARD** : En retard (rouge) - `nextDueDate < today` et non confirmé
- **NON RÉALISÉE** : Non faite (orange) - Due mais non confirmée
- **TERMINÉE** : Terminée (vert) - Confirmée
- **ANNULÉE** : Annulée (gris) - Cette occurrence a été annulée
- **INACTIVE** : Inactive (gris) - `isActive = false`

### 6.3 Verrouiller Cycle/Unité

- S'il y a un historique (enregistrements d'historique) :
  - **Type CYCLE** : Le cycle est verrouillé, ne peut pas être modifié
  - **Type METRIC** : L'unité et le cycle sont verrouillés, ne peuvent pas être modifiés
- Afficher l'avertissement : "⚠️ Le cycle est verrouillé car il y a un historique" ou "⚠️ L'unité est verrouillée car il y a un historique"

### 6.4 Confirmer une tâche basée sur des métriques

- **Validation** :
  - La valeur métrique actuelle doit être ≥ dernière valeur métrique réalisée
  - Si invalide : Afficher l'erreur "La valeur métrique actuelle doit être ≥ dernière valeur métrique réalisée"
- **Mise à jour automatique** :
  - `lastMetricValue` = valeur actuelle
  - `nextMetricValue` = valeur actuelle + cycle
  - `lastCompletedDate` = aujourd'hui
- **Dépenses** :
  - Si `hasCost = true` : Afficher la boîte de dialogue "Dépense engagée ?" après confirmation réussie
  - Naviguer vers l'écran "Ajouter une dépense" avec `initialNote`, `initialCategoryId`, `todoHistoryId`

### 6.5 Notifications

- **Type CYCLE** :
  - Les notifications sont programmées lors de la création/modification de la tâche
  - Les notifications sont annulées lors de la désactivation ou de la suppression de la tâche
  - Les notifications sont reprogrammées lors de la réactivation (si `nextDueDate >= today`)
- **Type METRIC** : Pas de notifications (MVP1)

### 6.6 Calculer la prochaine date d'échéance

- **Type CYCLE** :
  - La prochaine date d'échéance est automatiquement calculée en fonction du cycle après confirmation
  - Exemple : Cycle 3 mois, date d'échéance 03/01/2026 → Après confirmation, prochaine date d'échéance = 06/01/2026
- **Type METRIC** :
  - Prochaine échéance = valeur actuelle + cycle
  - Exemple : Valeur actuelle 14,520 miles, cycle 3,000 miles → Prochaine échéance = 17,520 miles

## 7. Notes importantes

1. **Bouton Confirmer** :
   - **Tâches basées sur le temps (CYCLE)** : Pas de bouton "Confirmer" dans la carte. La confirmation se fait uniquement dans l'écran "Tâches à faire" (liste de cloche).
   - **Tâches basées sur des métriques (METRIC)** : A un bouton "Confirmer" dans la carte (affiché uniquement lorsque `isActive = true`).

2. **Icône de cloche** : L'icône de cloche dans l'en-tête navigue vers l'écran "Tâches à faire" (liste de cloche) où les utilisateurs peuvent confirmer les tâches à faire (uniquement pour le type CYCLE).

3. **Verrouiller Cycle/Unité** : S'il y a un historique, le cycle (CYCLE) ou l'unité/cycle (METRIC) sera verrouillé et ne pourra pas être modifié pour assurer la cohérence des données.

4. **Validation métrique** : Lors de la confirmation d'une tâche basée sur des métriques, la valeur métrique actuelle doit être ≥ dernière valeur métrique réalisée. Sinon, l'application affichera une erreur et empêchera la confirmation.

5. **Dépenses engagées** : Si une tâche a des dépenses (`hasCost = true`), après confirmation réussie, l'application demandera si vous souhaitez ajouter une dépense. Si vous choisissez "Ajouter une dépense", l'application remplira automatiquement la note et la catégorie.

6. **Supprimer une tâche** : Lors de la suppression d'une tâche, tout l'historique associé sera également supprimé (suppression en cascade). Les notifications seront également annulées.

7. **Désactiver** : Lors de la désactivation d'une tâche de type CYCLE, les notifications seront annulées. Lors de la réactivation, les notifications seront reprogrammées (si `nextDueDate >= today`).

8. **Accès Premium** : Ce module nécessite un accès Premium. Si vous n'avez pas Premium, l'application affichera une boîte de dialogue demandant une mise à niveau.

