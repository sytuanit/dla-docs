# Épargne

## 1. Objectif

Le module **Épargne** vous aide à gérer les comptes d'épargne, suivre les soldes, les taux d'intérêt et les échéances. Ce module prend en charge :
- Gestion de plusieurs comptes d'épargne
- Suivi des taux d'intérêt et des échéances
- Calcul automatique des intérêts à l'échéance
- Retrait anticipé (si nécessaire)
- Renouvellement de compte

## 2. Quand utiliser

Utilisez ce module lorsque vous avez :
- Comptes d'épargne bancaires
- Besoin de suivre les soldes et les taux d'intérêt
- Souhaitez des rappels à l'échéance
- Besoin de gérer plusieurs comptes d'épargne

## 3. Écrans associés

- Liste des comptes d'épargne
- Ajouter un nouveau compte
- Modifier un compte
- Détails du compte
- Retrait anticipé

## 4. Utilisation principale

### 4.1 Créer un nouveau compte d'épargne

1. Allez à **Fonctions** → Sélectionnez **Épargne bancaire**
2. Appuyez sur le bouton **+** (FAB) en bas à droite
3. Voyez "Solde Actuel" (vous pouvez cliquer pour voir les détails)
4. Sélectionnez la banque :
   - Si elle existe : Sélectionnez dans le menu déroulant
   - Sinon : Appuyez sur le bouton "+" pour créer une nouvelle banque
5. Entrez le montant du dépôt (doit être ≤ Solde Actuel)
6. Entrez la durée : 1-36 mois
7. Entrez le taux d'intérêt : %/an (1-100%)
8. Sélectionnez la date de début (par défaut aujourd'hui, peut sélectionner depuis le mois précédent jusqu'à aujourd'hui)
9. Voyez la date d'échéance calculée automatiquement (depuis la date de début + durée)
10. Sélectionnez le plan à l'échéance :
    - Retirer le capital et les intérêts (par défaut)
    - Renouveler le CAPITAL (intérêts au compte)
    - Renouveler CAPITAL + INTÉRÊTS
11. (Optionnel) Entrez une note
12. (Optionnel) Sélectionnez les heures de notification (par défaut : 10:00 et 19:00)
13. Appuyez sur **CRÉER LE COMPTE**

### 4.2 Voir la liste et les détails du compte

1. Allez à **Fonctions** → Sélectionnez **Épargne bancaire**
2. Voyez l'écran "Liste des Comptes d'Épargne" avec le filtre par défaut "Actif"
3. Voyez la carte de résumé :
   - Filtre "Actif" : Solde actuel, Argent en épargne, Intérêts attendus, Intérêts de ce mois
   - Filtre "Terminé" : Total retiré, Intérêts reçus
4. (Optionnel) Utilisez la barre de recherche pour trouver des comptes par nom ou code de banque
5. Changez le filtre entre "Actif" et "Terminé"
6. Appuyez sur un compte d'épargne pour voir les détails :
   - Informations du compte : Banque, Durée, Taux d'intérêt, Montant du dépôt, Intérêts estimés
   - Date de début et date d'échéance
   - Statut : Actif
   - Plan à l'échéance
   - (Si existe) Historique des renouvellements
   - Bouton "RETIRER" (si actif)

### 4.3 Retirer un compte d'épargne

1. Allez à la liste des comptes d'épargne, trouvez le compte qui a atteint ou dépassé la date d'échéance
2. Appuyez sur le bouton **RETIRER** sur la carte (ou allez aux détails puis appuyez sur "RETIRER")
3. Voyez le dialogue "RETIRER LE COMPTE D'ÉPARGNE" avec :
   - Informations du compte : Banque, Montant du dépôt, Durée, Taux d'intérêt
   - Date de retrait (par défaut = date d'échéance, peut sélectionner une date différente)
   - Intérêts reçus (par défaut = intérêts estimés, peut être modifié)
   - Total reçu (calculé automatiquement = capital + intérêts)
4. (Optionnel) Modifiez la date de retrait ou les intérêts reçus
5. Appuyez sur **CONFIRMER**

### 4.4 Renouveler un compte d'épargne

1. Allez à la liste des comptes d'épargne, trouvez le compte qui a atteint la date d'échéance avec le plan "Renouveler le CAPITAL" ou "Renouveler CAPITAL + INTÉRÊTS"
2. Appuyez sur le bouton **RENOUVELER** ou "Renouveler comme prévu"
3. Voyez le dialogue "RENOUVELER LE COMPTE D'ÉPARGNE" avec :
   - Informations du compte : Banque, Montant du capital, Durée, Taux d'intérêt
   - Intérêts reçus (si renouvellement du CAPITAL, les intérêts vont au compte)
4. (Optionnel) Modifiez le nouveau taux d'intérêt ou la nouvelle durée (par défaut = ancienne durée)
5. Appuyez sur **CONFIRMER LE RENOUVELLEMENT**

### 4.5 Modifier un compte d'épargne

1. Allez aux détails du compte d'épargne actif
2. Appuyez sur le bouton **Modifier** en haut à droite
3. Modifiez les informations :
   - Banque (si nécessaire)
   - Montant du dépôt (si augmentation, doit être ≤ Solde Actuel)
   - Durée, Taux d'intérêt
   - Date de début (si nécessaire)
   - Plan à l'échéance
   - Note, Heures de notification
4. Voyez la date d'échéance recalculée automatiquement (si la durée/date de début change)
5. Appuyez sur **ENREGISTRER LES MODIFICATIONS**

### 4.6 Créer une nouvelle banque

1. Sur l'écran "Ajouter un Compte d'Épargne" ou "Modifier un Compte d'Épargne"
2. Appuyez sur le champ "Banque"
3. Appuyez sur le bouton "+" à côté du menu déroulant pour créer une nouvelle banque
4. Voyez le dialogue "AJOUTER UNE NOUVELLE BANQUE"
5. Entrez le nom de la banque
6. Entrez le code de la banque (max. 3-4 caractères, automatiquement en majuscules)
7. Sélectionnez la couleur de l'icône (du sélecteur de couleur ou de la palette)
8. Voyez l'aperçu de l'icône
9. Appuyez sur **CRÉER**

## 5. Exemples & illustrations d'interface

### SAVINGS-01: Créer un nouveau compte d'épargne

**Objectif** : Créer un nouveau compte d'épargne pour suivre le dépôt bancaire, le taux d'intérêt et la date d'échéance.

**Étapes principales** :
1. Allez à Fonctions → Épargne bancaire
2. Appuyez sur le bouton "+" (FAB)
3. Sélectionnez la banque (ou créez-en une nouvelle)
4. Entrez le montant du dépôt, la durée, le taux d'intérêt
5. Sélectionnez la date de début (par défaut aujourd'hui)
6. Sélectionnez le plan à l'échéance
7. (Optionnel) Entrez une note et les heures de notification
8. Appuyez sur "CRÉER LE COMPTE"

**Wireframe - Écran Ajouter un Compte d'Épargne** :

```text
┌──────────────────────────────────────────────┐
│ <  Ajouter un Compte d'Épargne                       │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ Carte ]                                      │
│                                               │
│ Solde Actuel                      [ > ]    │
│ €1,872                                        │
│                                               │
│ Banque *                                        │
│ [ Banque Santander ▼ ]                 [ + ] │
│                                               │
│ Montant du Dépôt (EUR) *                       │
│ [ €3,600 ]                                    │
│                                               │
│ Durée *                                        │
│ [ 6 ] Mois                                  │
│                                               │
│ Taux d'Intérêt *                               │
│ [ 4.8 ] %/an                                │
│                                               │
│ Date de Début *                                  │
│ [ 20/12/2025 ]                    [📅]        │
│                                               │
│ Date d'Échéance (lecture seule)                      │
│ [ 20/06/2026 ]                                 │
│                                               │
│ Plan à l'Échéance                              │
│ (●) Retirer le capital et les intérêts          │
│ ( ) Renouveler le CAPITAL                        │
│ ( ) Renouveler CAPITAL + INTÉRÊTS            │
│                                               │
│ Note (optionnelle)                               │
│ [                                      ]      │
│                                               │
│ Heure de Notification 1                           │
│ [ 10:00 ]                          [🕐]       │
│                                               │
│ Heure de Notification 2                            │
│ [ 19:00 ]                          [🕐]       │
└──────────────────────────────────────────────┘

        [  ANNULER  ]       [  CRÉER LE COMPTE  ]
```

---

### SAVINGS-02: Retirer un compte d'épargne

**Objectif** : Retirer un compte d'épargne lorsqu'il atteint la date d'échéance pour recevoir le capital et les intérêts.

**Étapes principales** :
1. Allez à la liste des comptes d'épargne, trouvez le compte qui a atteint ou dépassé la date d'échéance
2. Appuyez sur le bouton "RETIRER"
3. Voyez le dialogue avec les informations du compte, la date de retrait, les intérêts reçus
4. (Optionnel) Modifiez la date de retrait ou les intérêts reçus
5. Appuyez sur "CONFIRMER"

**Wireframe - Dialogue Retirer** :

```text
┌─────────────────────────────────────────┐
│  RETIRER LE COMPTE D'ÉPARGNE                │
├─────────────────────────────────────────┤
│  [ICON BANK]  Banque Santander            │
│                                         │
│  Durée & Taux d'Intérêt : 6 mois · 4.8%/an │
│  Montant du Dépôt : €3,600                 │
│                                         │
│  Date de Retrait :                       │
│  [ 20 / 12 / 2025 ]  [📅]               │
│                                         │
│  Intérêts Reçus :                     │
│  [ €86 ]                                │
│                                         │
│  Total Reçu : €3,686                 │
│                                         │
│  [  CONFIRMER  ]                          │
└─────────────────────────────────────────┘
```

---

### SAVINGS-03: Voir la liste et les détails du compte

**Objectif** : Voir le résumé des comptes d'épargne actifs et terminés, ainsi que les détails de chaque compte.

**Étapes principales** :
1. Allez à Fonctions → Épargne bancaire
2. Voyez la carte de résumé par filtre
3. Utilisez la barre de recherche (optionnel)
4. Changez le filtre entre "Actif" et "Terminé"
5. Appuyez sur le compte pour voir les détails

**Wireframe - Écran de Liste** :

```text
┌──────────────────────────────────────────────┐
│ <  Gestion de l'Épargne Bancaire                    │
│                  [ + [FAB] Ajouter un Compte ]      │
└──────────────────────────────────────────────┘

[Chip] Filtre
[ Actif ]   [ Terminé ]

┌──────────────────────────────────────────────┐
│  CARTE DE RÉSUMÉ                                │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Solde      │  │ Intérêts      │         │
│  │ Actuel      │  │ Attendus      │         │
│  │ €1,872       │  │ €197          │         │
│  └──────────────┘  └──────────────┘         │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Argent en     │  │ Intérêts de ce │         │
│  │ Épargne      │  │ mois      │         │
│  │ €12,600      │  │ €68           │         │
│  └──────────────┘  └──────────────┘         │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  🔍 Barre de Recherche                               │
│  [ 🔍 Rechercher... ]                            │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ICON BANK] Banque Santander      [Icone Supprimer] │
│                                              │
│ €3,600         |  6 mois @ 4.8%           │
│                                              │
│ Intérêts Estimés : €86                     │
│ Échéance : 20/12/2025   (5 jours restants)  │
│                    🔔 Proche de l'échéance               │
│                                              │
│                    [ RETIRER ]             │
└──────────────────────────────────────────────┘
```

**Wireframe - Écran de Détails** :

```text
┌──────────────────────────────────────────────┐
│ [ICON BANK]  Banque Santander          [ Modifier ]│
│                                              │
│ Durée & Taux d'Intérêt : 6 mois · 4.8%/an  │
│ Montant du Dépôt : €3,600                       │
│ Intérêts Estimés : €86                     │
│                                              │
│ Date de Début : 20/06/2025                       │
│ Date d'Échéance : (5 jours restants) 20/12/2025 │
│                                              │
│ Statut : Actif                               │
│                                              │
│ Plan à l'Échéance :                           │
│ (●) Retirer le capital et les intérêts         │
│                                              │
│                    [  RETIRER  ]           │
└──────────────────────────────────────────────┘
```

---

### SAVINGS-04: Renouveler un compte d'épargne

**Objectif** : Renouveler un compte d'épargne comme prévu lorsqu'il atteint la date d'échéance.

**Étapes principales** :
1. Trouvez le compte qui a atteint la date d'échéance avec le plan "Renouveler le CAPITAL" ou "Renouveler CAPITAL + INTÉRÊTS"
2. Appuyez sur le bouton "RENOUVELER"
3. Voyez le dialogue avec les informations du compte et les intérêts reçus
4. (Optionnel) Modifiez le nouveau taux d'intérêt ou la nouvelle durée
5. Appuyez sur "CONFIRMER LE RENOUVELLEMENT"

**Résultat** : L'ancien compte est mis à jour, un nouveau compte est créé lié avec rootSavingId à l'ancien compte. Si renouvellement du CAPITAL, les intérêts sont ajoutés au solde actuel. Si renouvellement CAPITAL + INTÉRÊTS, le capital et les intérêts sont renouvelés.

---

### SAVINGS-05: Créer une nouvelle banque

**Objectif** : Créer une nouvelle banque pour l'utiliser lors de la création de comptes d'épargne.

**Étapes principales** :
1. Sur l'écran "Ajouter un Compte d'Épargne" ou "Modifier un Compte d'Épargne"
2. Appuyez sur le bouton "+" à côté du menu déroulant "Banque"
3. Entrez le nom de la banque, le code de la banque
4. Sélectionnez la couleur de l'icône
5. Voyez l'aperçu de l'icône
6. Appuyez sur "CRÉER"

**Wireframe - Dialogue Créer une Banque** :

```text
┌─────────────────────────────────────────┐
│  AJOUTER UNE NOUVELLE BANQUE                            │
├─────────────────────────────────────────┤
│  NOM DE LA BANQUE                               │
│  [ Banque ABC ]                            │
│                                         │
│  CODE DE LA BANQUE                               │
│  [ ABC ]                                 │
│                                         │
│  COULEUR DE L'ICÔNE                              │
│  [ 🎨 ]  #FF5722                         │
│                                         │
│  APERÇU DE L'ICÔNE                            │
│  ┌─────────┐                             │
│  │   ABC   │  (Fond : #FF5722)      │
│  └─────────┘                             │
│                                         │
│  [  ANNULER  ]    [  CRÉER  ]           │
└─────────────────────────────────────────┘
```

---

### SAVINGS-06: Modifier un compte d'épargne

**Objectif** : Modifier les informations d'un compte d'épargne actif (banque, montant, durée, taux d'intérêt, plan d'échéance).

**Étapes principales** :
1. Allez aux détails du compte d'épargne actif
2. Appuyez sur le bouton "Modifier"
3. Modifiez les informations nécessaires
4. Voyez la date d'échéance recalculée automatiquement (si la durée/date de début change)
5. Appuyez sur "ENREGISTRER LES MODIFICATIONS"

**Résultat** : Les informations du compte sont mises à jour, les intérêts estimés sont recalculés en fonction du nouveau taux d'intérêt. Si le montant change, le solde actuel est ajusté en conséquence.

## 6. Logique & règles

### 6.1 Calcul des intérêts

- Les intérêts sont calculés par la formule : `Montant × Taux d'Intérêt × (Durée / 12)`
- Les intérêts sont calculés à l'échéance ou lors du retrait anticipé

### 6.2 Statut

- **Actif (ACTIVE)** : Le compte d'épargne est actif, n'a pas atteint la date d'échéance ou n'a pas été traité
- **Terminé (COMPLETED)** : Le compte a été retiré
- **Renouvelé (ROLLED_OVER)** : Le compte a été renouvelé, un nouveau compte a été créé

### 6.3 Retrait et renouvellement

- **Retrait** : Lors du retrait, le capital + intérêts sont ajoutés au solde actuel, crée automatiquement "Revenu Extra" avec la catégorie "Intérêts d'Épargne"
- **Retrait Anticipé** : Peut retirer avant la date d'échéance, les intérêts reçus peuvent être inférieurs aux intérêts estimés
- **Renouveler le CAPITAL** : Les intérêts sont ajoutés au solde actuel, le capital est renouvelé avec une nouvelle durée
- **Renouveler CAPITAL + INTÉRÊTS** : Le capital et les intérêts sont renouvelés, le solde actuel ne change pas
- **Historique des Renouvellements** : Les renouvellements sont enregistrés et affichés dans les détails du compte, liés via `rootSavingId`

### 6.4 Notifications

- L'application envoie une notification de rappel lorsque la date d'échéance arrive
- L'heure de notification peut être configurée pour chaque compte (`notificationTime1`, `notificationTime2`, par défaut 10:00 et 19:00)

## 7. Notes importantes

- **Module Premium Requis** : Cette fonctionnalité est réservée aux utilisateurs Premium
- **Taux d'Intérêt** : Entrez le taux d'intérêt par an (%/an), de 1 à 100%
- **Durée** : Calculée en mois, de 1 à 36 mois
- **Date d'Échéance** : Calculée automatiquement depuis la date de début + durée
- **Montant du Dépôt** : Doit être ≤ Solde Actuel, lors de la création du compte, il est automatiquement soustrait du solde actuel
- **Date de Début** : Ne peut sélectionner que depuis le début du mois précédent jusqu'à aujourd'hui
- **Notifications** : Les notifications sont envoyées à la date d'échéance à 2 heures (par défaut 10:00 et 19:00), peuvent être personnalisées pour chaque compte
- **Badge "Proche de l'échéance"** : Affiché lorsque ≤ 7 jours jusqu'à la date d'échéance
- **Badge "Échu"** : Affiché lorsque la date d'échéance est arrivée
- **Supprimer un Compte** : Lors de la suppression d'un compte actif, le montant du capital est ajouté au solde actuel. Supprimer le compte racine supprime toute la chaîne de renouvellements
- **Carte de Résumé** : Change selon le filtre, affiche des informations agrégées pour les comptes actifs ou terminés

