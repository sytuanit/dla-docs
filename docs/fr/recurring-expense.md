# Dépenses Récurrentes

## 1. Objectif

Le module **Dépenses Récurrentes** vous aide à gérer les dépenses périodiques avec des cycles fixes telles que :
- Factures d'électricité, d'eau, de gaz
- Internet, télévision par câble
- Assurance
- Frais de scolarité
- Loyer
- Autres dépenses récurrentes

Ce module crée automatiquement des **occurrences** basées sur le cycle que vous configurez et vous rappelle quand le paiement est dû.

## 2. Quand utiliser

Utilisez ce module si vous avez :
- Dépenses fixes selon un horaire (hebdomadaire, bihebdomadaire ou mensuel)
- Besoin de suivre et confirmer quand le paiement a été effectué
- Souhaitez un calcul automatique dans le budget mensuel

## 3. Écrans associés

- Liste des dépenses récurrentes
- Ajouter une nouvelle dépense récurrente
- Modifier une dépense récurrente
- Historique des occurrences

## 4. Utilisation principale

### 4.1 Ajouter une nouvelle dépense récurrente

1. Allez à **Fonctions** → Sélectionnez **Dépenses Récurrentes**
2. Appuyez sur le bouton **➕** (FAB) en bas à droite
3. Remplissez les informations :
   - **Catégorie** : Sélectionnez une catégorie ou créez-en une nouvelle
   - **Montant** : Entrez le montant de la dépense (peut être laissé vide, à saisir lors de la confirmation)
   - **Cycle** : Sélectionnez Hebdomadaire / Bihebdomadaire / Mensuel
   - **Date** : Sélectionnez la date dans le cycle (ex. le 15 de chaque mois)
   - **Date de début** : (Uniquement pour le cycle bihebdomadaire) Sélectionnez la date de début
   - **Note** : Informations supplémentaires (optionnel)
4. Appuyez sur **Enregistrer**

### 4.2 Confirmer le paiement

1. Allez à la liste des dépenses récurrentes
2. Trouvez l'élément avec le badge **"Confirmation en attente"** (jaune)
3. Appuyez sur l'élément pour ouvrir le dialogue de confirmation
4. Remplissez :
   - **Montant réel** : (si différent de celui attendu)
   - **Note** : (optionnel)
5. Appuyez sur **Confirmer**

### 4.3 Modifier une dépense récurrente

1. Allez à la liste des dépenses récurrentes
2. Appuyez sur l'élément à modifier
3. Sélectionnez **Modifier** dans le menu
4. Mettez à jour les informations
5. Appuyez sur **Enregistrer**

### 4.4 Afficher l'historique

1. Allez à la liste des dépenses récurrentes
2. Appuyez sur un élément
3. Sélectionnez **Historique** pour afficher toutes les occurrences passées

### 4.5 Désactiver/activer une dépense

1. Allez à la liste des dépenses récurrentes
2. Trouvez l'élément à désactiver/activer
3. Basculez l'interrupteur **Actif** sur le côté droit de l'élément

## 5. Exemples et illustrations UI

### 5.1 Exemple 1 : Créer une dépense récurrente mensuelle (Facture d'électricité)

**Scénario** : Vous souhaitez suivre votre facture d'électricité mensuelle pour que l'application vous rappelle automatiquement quand le paiement est dû.

**Étapes** :
1. Allez à l'écran Fonctions, sélectionnez "Dépenses Récurrentes"
2. Appuyez sur le bouton "➕ Nouveau" en bas à droite
3. Sélectionnez la catégorie "Services publics" (ou créez-en une nouvelle si elle n'est pas disponible)
4. Entrez le montant : €18
5. Sélectionnez le cycle "Mensuel"
6. Sélectionnez "Sélectionner le jour du mois", entrez 15
7. Note automatiquement remplie "Facture d'électricité mensuelle" (peut être modifiée)
8. Appuyez sur "Enregistrer"

**Résultat** : L'application affiche un message de succès et revient à la liste. Le nouvel élément apparaît avec toutes les informations, et l'application vous rappellera automatiquement le 15 de chaque mois.

**Écran "Ajouter une dépense récurrente"** :

```text
┌─────────────────────────────────────────┐
│  ← Retour    Ajouter une dépense récurrente        │
├─────────────────────────────────────────┤
│  Catégorie *                              │
│  [Services publics ▼] [+ Nouveau]             │
│                                         │
│  Montant (EUR) *                          │
│  [€18]                                  │
│                                         │
│  Cycle *                                 │
│  ┌──────┐ ┌────────┐ ┌────────┐        │
│  │Semaine│ │Bihebdo│ │Mois  │        │
│  └──────┘ └────────┘ └────────┘        │
│                                         │
│  Date de paiement dans le cycle                  │
│  ⚪ Fin du mois                         │
│  ⚫ Sélectionner le jour du mois                  │
│  ┌───────────────────────────────────┐ │
│  │ Jour du mois : [15]                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Note                                    │
│  ┌───────────────────────────────────┐ │
│  │ Facture d'électricité mensuelle           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Annuler]                  [Enregistrer]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Exemple 2 : Confirmer une dépense due et mettre à jour le montant réel

**Scénario** : C'est le jour de paiement de la facture d'eau (10), mais le montant réellement payé est €6.30 (réduit) au lieu de €7.20 comme configuré.

**Étapes** :
1. Ouvrez l'application ou allez à l'écran "Dépenses Récurrentes"
2. L'application détecte automatiquement l'occurrence due et affiche le dialogue de confirmation
3. Le dialogue affiche le montant par défaut : €7.20
4. Mettez à jour le montant réel à €6.30
5. Entrez une note : "Ce mois économie d'eau" (optionnel)
6. Appuyez sur "Confirmer le paiement"

**Résultat** : L'application met à jour l'occurrence confirmée avec le montant réel €6.30, crée automatiquement la prochaine occurrence et met à jour le solde financier actuel (soustrait €6.30).

**Dialogue de confirmation de la dépense** :

```text
┌─────────────────────────────────────────┐
│  Confirmer le paiement                           │
├─────────────────────────────────────────┤
│  Facture d'eau                              │
│  Mensuel (10.)                         │
│  Date d'échéance : Aujourd'hui                        │
│                                         │
│  Montant réel *                         │
│  [€6.30]                                   │
│                                         │
│  Note                                    │
│  [Ce mois économie d'eau]               │
│                                         │
│  [Annuler]    [Confirmer le paiement]        │
└─────────────────────────────────────────┘
```

---

### 5.3 Exemple 3 : Désactiver une dépense récurrente si elle n'est plus applicable

**Scénario** : Vous ne louez temporairement pas d'appartement pendant 2 mois, donc vous souhaitez désactiver la dépense "Loyer" au lieu de la supprimer complètement.

**Étapes** :
1. Allez à l'écran "Dépenses Récurrentes"
2. Trouvez l'élément "Loyer" dans la liste
3. Appuyez sur l'interrupteur "Actif" sur le côté droit de l'élément
4. L'application affiche un dialogue de confirmation : "Êtes-vous sûr de vouloir désactiver cette dépense ?"
5. Appuyez sur le bouton "Désactiver" pour confirmer

**Résultat** : La carte "Loyer" passe au statut "Inactif" (gris), l'interrupteur passe à "Inactif". L'application ne crée plus de nouvelles occurrences pour cette dépense. Vous pouvez réactiver en appuyant sur l'interrupteur "Inactif" → "Actif".

**Liste avec interrupteur** :

```text
┌─────────────────────────────────────────┐
│  ← Retour    Dépenses Récurrentes           │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Loyer              [⚪ Inactif]   │ │
│  │ €1,080                            │ │
│  │ Mensuel - 1.                     │ │
│  │ (Désactivé)                     │ │
│  │                                    │ │
│  │ [Modifier] [Historique] [Supprimer]         │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

---

## 6. Logique et règles

### 6.1 Cycle et date

- **Hebdomadaire** : Sélectionnez le jour de la semaine (1=Lundi, 7=Dimanche)
- **Bihebdomadaire** : Sélectionnez le jour de la semaine + date de début spécifique
- **Mensuel** : Sélectionnez le jour du mois (1-31)

### 6.2 Création automatique d'occurrences

- L'application crée automatiquement des **occurrences** quand :
  - Vous ajoutez une nouvelle dépense
  - La date dans le cycle est atteinte
  - Un nouveau mois commence

### 6.3 Statut des occurrences

- **EN ATTENTE** : Confirmation en attente (affiche un badge jaune)
- **TERMINÉ** : Confirmé (affiche un badge vert)
- **ANNULÉ** : Annulé (affiche un badge rouge)

### 6.4 Intégration au budget

- Lors de la confirmation de la dépense, l'application met automatiquement à jour le budget du mois en cours (s'il existe)
- La dépense est calculée dans "Dépenses Récurrentes" dans le budget

### 6.5 Notifications

- L'application envoie une notification de rappel quand le paiement est dû
- L'heure de notification peut être configurée pour chaque élément (`notificationTime1`, `notificationTime2`, par défaut 16:00 et 19:00)

## 7. Notes importantes

- **Le montant peut être laissé vide** : Si vous ne connaissez pas le montant exact, vous pouvez le laisser vide et l'entrer lors de la confirmation
- **Ne peut pas être supprimé si des occurrences existent** : S'il y a des occurrences, vous ne pouvez que désactiver (isActive = false), pas supprimer
- **Confirmation tardive** : Vous pouvez confirmer des occurrences passées, l'application recalcule automatiquement le budget
- **Changer le cycle** : Lors de la modification du cycle, les occurrences futures sont recalculées

