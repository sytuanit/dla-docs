# Revenus Récurrents

## 1. Objectif

Le module **Revenus Récurrents** vous aide à gérer les sources de revenus régulières telles que :
- Salaire mensuel
- Revenus de location
- Pension
- Dividendes d'investissement
- Autres revenus récurrents

Ce module crée automatiquement des **occurrences** basées sur le cycle que vous configurez et vous rappelle quand il est temps de recevoir le paiement.

## 2. Quand utiliser

Utilisez ce module si vous avez :
- Revenus fixes selon un horaire (hebdomadaire, bihebdomadaire ou mensuel)
- Besoin de suivre et confirmer quand le paiement a été reçu
- Souhaitez un calcul automatique dans le budget mensuel

## 3. Écrans associés

- Liste des revenus récurrents
- Ajouter un nouveau revenu récurrent
- Modifier un revenu récurrent
- Historique des occurrences

## 4. Utilisation principale

### 4.1 Ajouter un nouveau revenu récurrent

1. Allez à **Fonctions** → Sélectionnez **Revenus Récurrents**
2. Appuyez sur le bouton **➕** (FAB) en bas à droite
3. Remplissez les informations :
   - **Catégorie** : Sélectionnez une catégorie ou créez-en une nouvelle
   - **Montant** : Entrez le montant du revenu (peut être laissé vide, à saisir lors de la confirmation)
   - **Cycle** : Sélectionnez Hebdomadaire / Bihebdomadaire / Mensuel
   - **Date** : Sélectionnez la date dans le cycle (ex. le 15 de chaque mois)
   - **Date de début** : (Uniquement pour le cycle bihebdomadaire) Sélectionnez la date de début
   - **Note** : Informations supplémentaires (optionnel)
4. Appuyez sur **Enregistrer**

### 4.2 Confirmer la réception du paiement

1. Allez à la liste des revenus récurrents
2. Trouvez l'élément avec le badge **"Confirmation en attente"** (jaune)
3. Appuyez sur l'élément pour ouvrir le dialogue de confirmation
4. Remplissez :
   - **Montant réel** : (si différent de celui attendu)
   - **Note** : (optionnel)
5. Appuyez sur **Confirmer**

### 4.3 Modifier un revenu récurrent

1. Allez à la liste des revenus récurrents
2. Appuyez sur l'élément à modifier
3. Sélectionnez **Modifier** dans le menu
4. Mettez à jour les informations
5. Appuyez sur **Enregistrer**

### 4.4 Afficher l'historique

1. Allez à la liste des revenus récurrents
2. Appuyez sur un élément
3. Sélectionnez **Historique** pour afficher toutes les occurrences passées

### 4.5 Désactiver/activer un revenu

1. Allez à la liste des revenus récurrents
2. Trouvez l'élément à désactiver/activer
3. Basculez l'interrupteur **Actif** sur le côté droit de l'élément

## 5. Exemples et illustrations UI

### 5.1 Exemple 1 : Créer un revenu récurrent mensuel (Salaire)

**Scénario** : Vous souhaitez suivre votre salaire mensuel pour que l'application vous rappelle automatiquement quand il est temps de recevoir le paiement.

**Étapes** :
1. Allez à l'écran Fonctions, sélectionnez "Revenus Récurrents"
2. Appuyez sur le bouton "➕ Nouveau" en bas à droite
3. Sélectionnez la catégorie "Salaire" (ou créez-en une nouvelle si elle n'est pas disponible)
4. Entrez le montant : €3,600
5. Sélectionnez le cycle "Mensuel"
6. Sélectionnez "Sélectionner le jour du mois", entrez 5
7. Note automatiquement remplie "Salaire mensuel" (peut être modifiée)
8. Appuyez sur "Enregistrer"

**Résultat** : L'application affiche un message de succès et revient à la liste. Le nouvel élément apparaît avec toutes les informations, et l'application vous rappellera automatiquement le 5 de chaque mois.

**Écran "Ajouter un revenu récurrent"** :

```text
┌─────────────────────────────────────────┐
│  ← Retour    Ajouter un revenu récurrent │
├─────────────────────────────────────────┤
│  Catégorie *                              │
│  [Salaire ▼] [+ Nouveau]                 │
│                                         │
│  Montant (EUR) *                          │
│  [€3,600]                               │
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
│  │ Jour du mois : [5]                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Note                                    │
│  ┌───────────────────────────────────┐ │
│  │ Salaire mensuel                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Annuler]                  [Enregistrer]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Exemple 2 : Confirmer un revenu dû et mettre à jour le montant réel

**Scénario** : C'est le jour de paie (5), mais le montant réellement reçu est €3,780 (augmentation de salaire) au lieu de €3,600 comme configuré.

**Étapes** :
1. Ouvrez l'application ou allez à l'écran "Revenus Récurrents"
2. L'application détecte automatiquement l'occurrence due et affiche le dialogue de confirmation
3. Le dialogue affiche le montant par défaut : €3,600
4. Mettez à jour le montant réel à €3,780
5. Entrez une note : "Ce mois a un bonus" (optionnel)
6. Appuyez sur "Confirmer la réception"

**Résultat** : L'application met à jour l'occurrence confirmée avec le montant réel €3,780, crée automatiquement la prochaine occurrence et met à jour le solde financier actuel.

**Dialogue de confirmation du revenu** :

```text
┌─────────────────────────────────────────┐
│  Confirmer la réception                        │
├─────────────────────────────────────────┤
│  Salaire                                  │
│  Mensuel (5.)                          │
│  Date d'échéance : Aujourd'hui                        │
│                                         │
│  Montant réel *                         │
│  [€3,780]                               │
│                                         │
│  Note                                    │
│  [Ce mois a un bonus]                 │
│                                         │
│  [Annuler]    [Confirmer la réception]   │
└─────────────────────────────────────────┘
```

---

### 5.3 Exemple 3 : Annuler une occurrence de revenu si le paiement n'a pas été reçu

**Scénario** : C'est le jour de paiement du loyer (1), mais le locataire n'a pas transféré d'argent, donc le paiement n'a pas été reçu.

**Étapes** :
1. Ouvrez l'application ou allez à l'écran "Revenus Récurrents"
2. L'application affiche le dialogue de confirmation pour l'occurrence due
3. Appuyez sur le bouton "Annuler"
4. Entrez la raison : "Le locataire n'a pas transféré d'argent" (requis)
5. Appuyez sur "Confirmer l'annulation"

**Résultat** : L'occurrence annulée passe au statut "Annulé", affiche la raison de l'annulation, et l'application crée automatiquement la prochaine occurrence. Le solde financier ne change pas car aucun paiement n'a été reçu.

**Dialogue "Annuler l'occurrence de revenu"** :

```text
┌─────────────────────────────────────────┐
│  Annuler                              │
├─────────────────────────────────────────┤
│  Revenus de location                            │
│  Mensuel (1.)                           │
│  Date d'échéance : Aujourd'hui                         │
│                                         │
│  Raison de l'annulation *                    │
│  ┌───────────────────────────────────┐ │
│  │ Le locataire n'a pas transféré d'argent    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Retour]        [Confirmer l'annulation]         │
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
  - Vous ajoutez un nouveau revenu
  - La date dans le cycle est atteinte
  - Un nouveau mois commence

### 6.3 Statut des occurrences

- **EN ATTENTE** : Confirmation en attente (affiche un badge jaune)
- **TERMINÉ** : Confirmé (affiche un badge vert)
- **ANNULÉ** : Annulé (affiche un badge rouge)

### 6.4 Intégration au budget

- Lors de la confirmation du revenu, l'application met automatiquement à jour le budget du mois en cours (s'il existe)
- Le revenu est calculé dans "Revenus Récurrents" dans le budget

### 6.5 Notifications

- L'application envoie une notification de rappel quand le paiement est dû
- L'heure de notification peut être configurée pour chaque élément (`notificationTime1`, `notificationTime2`, par défaut 16:00 et 19:00)

## 7. Notes importantes

- **Le montant peut être laissé vide** : Si vous ne connaissez pas le montant exact, vous pouvez le laisser vide et l'entrer lors de la confirmation
- **Ne peut pas être supprimé si des occurrences existent** : S'il y a des occurrences, vous ne pouvez que désactiver (isActive = false), pas supprimer
- **Confirmation tardive** : Vous pouvez confirmer des occurrences passées, l'application recalcule automatiquement le budget
- **Changer le cycle** : Lors de la modification du cycle, les occurrences futures sont recalculées

