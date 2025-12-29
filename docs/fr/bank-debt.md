# Prêts Bancaires

## 1. Objectif

Le module **Prêts Bancaires** vous aide à gérer les prêts bancaires, y compris :
- Suivre le montant du prêt, le taux d'intérêt, la durée
- Gérer le calendrier des paiements
- Calculer les intérêts par période (si applicable)
- Gérer les pénalités de retard de paiement
- Règlement anticipé (si nécessaire)

## 2. Quand utiliser

Utilisez ce module lorsque vous avez :
- Prêts bancaires
- Besoin de suivre le calendrier des paiements
- Souhaitez calculer les intérêts et les pénalités
- Besoin de rappels lorsque le paiement est en retard

## 3. Écrans associés

- Liste des prêts
- Ajouter un nouveau prêt (4 étapes)
- Modifier un prêt
- Détails du prêt et calendrier des paiements
- Règlement anticipé

## 4. Utilisation principale

### 4.1 Ajouter un nouveau prêt (4 étapes)

#### Étape 1 : Informations de base

1. Allez à **Fonctions** → Sélectionnez **Prêts Bancaires**
2. Appuyez sur le bouton **+** (FAB)
3. Complétez les informations :
   - **Banque** : Sélectionnez la banque ou créez-en une nouvelle
   - **Nom du Prêt** : (ex. "Prêt Hypothécaire")
   - **Montant du Prêt** : Montant du capital
   - **Date de Décaissement** : Date à laquelle l'argent a été reçu
   - **Durée** : Nombre d'années
   - **Type d'Intérêt** : Taux promotionnel/variable ou Taux fixe
4. Appuyez sur **Suivant**

#### Étape 2 : Configurer le taux d'intérêt

**Si vous sélectionnez "Taux Promotionnel/Variable" :**
- Activez **A un Taux Promotionnel** (si applicable)
- Entrez **Mois Promotionnels** et **Taux Promotionnel**
- Ajoutez des périodes de taux variable :
  - Sélectionnez l'année et la plage de mois
  - Entrez le taux d'intérêt (%/an)
  - Sélectionnez **Variable** ou **Fixe**

**Si vous sélectionnez "Taux Fixe" :**
- Entrez **Taux Fixe** (%/an)

Appuyez sur **Suivant**

#### Étape 3 : Configurer les pénalités

1. Activez **A une Pénalité de Retard de Paiement** (si applicable)
2. Ajoutez des périodes de pénalité :
   - Sélectionnez l'année et la plage de mois
   - Entrez **Taux de Pénalité** (%/an)
3. Appuyez sur **Suivant**

#### Étape 4 : Confirmer et enregistrer

1. Examinez les informations :
   - Montant total à payer
   - Calendrier des paiements attendu
2. Appuyez sur **Enregistrer**

### 4.2 Voir les détails du prêt

1. Allez à la liste des prêts
2. Appuyez sur un prêt
3. Voyez les informations :
   - Informations de base
   - Calendrier des paiements
   - Montant payé / Restant
   - Taux d'intérêt et pénalités

### 4.3 Marquer une période de paiement comme payée

1. Allez aux détails du prêt
2. Trouvez la période de paiement échue (badge "Non Payé")
3. Appuyez sur **Marquer comme Payé**
4. Complétez les informations :
   - **Date de Paiement Réel** : Date payée (par défaut = aujourd'hui)
   - **Intérêts Payés Réels** : Intérêts réellement payés (par défaut = intérêts planifiés)
   - **Note** : (optionnelle)
5. Voyez **Paiement Total Réel** calculé automatiquement (capital + intérêts réels)
6. Appuyez sur **Confirmer**

### 4.4 Mettre à jour le taux d'intérêt actuel

1. Allez aux détails du prêt (s'affiche uniquement si actuellement en période de taux variable)
2. Appuyez sur **Mettre à Jour le Taux d'Intérêt Actuel**
3. Complétez les informations :
   - **Nouveau Taux d'Intérêt** : Nouveau taux d'intérêt (%/an)
   - **Date Effective** : Date pour commencer à appliquer le nouveau taux (par défaut = début de la période actuelle)
   - **Note** : (optionnelle)
4. Appuyez sur **Enregistrer**
5. Les périodes non payées depuis la période actuelle sont mises à jour avec le nouveau taux d'intérêt

### 4.5 Règlement anticipé

1. Allez aux détails du prêt
2. Appuyez sur **Calculer le Montant du Règlement**
3. **Étape 1 - Entrer les informations de prépaiement :**
   - Sélectionnez la méthode : **Paiement Partiel** ou **Règlement Complet**
   - Sélectionnez la date de prépaiement (par défaut = aujourd'hui)
   - Entrez le montant de prépaiement (si partiel)
   - Voyez **Pénalité de Paiement Anticipé** calculée automatiquement
4. Appuyez sur **Suivant**
5. **Étape 2 - Comparer les options :**
   - Voyez la comparaison entre "Sans Prépaiment" et "Prépaiement"
   - Voyez les résultats : Économie d'intérêts, réduction de temps
6. Appuyez sur **Confirmer le Prépaiment**

### 4.6 Modifier un prêt

1. Allez aux détails du prêt
2. Appuyez sur **Modifier** (ne peut modifier que le nom, la note, la banque)
3. Modifiez les informations modifiables :
   - **Nom du Prêt** : Peut être modifié
   - **Banque** : Peut être changée
   - **Note** : Peut être modifiée
   - **Montant du Prêt, Date de Décaissement, Durée, Taux d'Intérêt** : Ne peuvent être modifiés que si aucun paiement n'a encore été effectué
4. Appuyez sur **Enregistrer**

## 5. Exemples & illustrations d'interface

### LOAN-01: Créer un nouveau prêt (Prêt Hypothécaire avec Taux d'Intérêt Promotionnel)

**Objectif** : Créer un nouveau prêt pour suivre un prêt hypothécaire, un taux d'intérêt promotionnel et un calendrier de paiements mensuels.

**Étapes** :
1. Allez à **Fonctions** → Sélectionnez **Prêts Bancaires**
2. Appuyez sur le bouton **+** (FAB) pour ajouter un nouveau prêt
3. **Étape 1 - Informations de base :**
   - Sélectionnez la banque : Banque Santander
   - Entrez le nom : "Prêt Hypothécaire - Appartement Centre"
   - Entrez le montant du prêt : €180,000
   - Sélectionnez la date de décaissement : 01/04/2023
   - Entrez la durée : 10 ans (calculé automatiquement = 120 périodes)
   - Sélectionnez les heures de notification : 10:00 et 19:00
   - Sélectionnez le type d'intérêt : "Solde Dégressif"
   - Appuyez sur **Suivant**
4. **Étape 2 - Configurer le taux d'intérêt :**
   - Activez "A une Période d'Intérêt Promotionnel"
   - Entrez : Premiers 6 mois @ 6.0%/an
   - Ajoutez des périodes subséquentes :
     - Année 1 (mois 7-12) : 9.0%/an, variable
     - Année 2 (mois 13-24) : 9.5%/an, variable
     - Année 3 et suivantes : 10.0%/an, variable
   - Appuyez sur **Suivant**
5. **Étape 3 - Configurer la pénalité de paiement anticipé :**
   - Activez "Appliquer Pénalité de Paiement Anticipé"
   - Entrez les pénalités : Années 1-3 : 2.0%, Années 4-5 : 1.5%, Année 6+ : 1.0%
   - Appuyez sur **Suivant**
6. **Étape 4 - Confirmer :**
   - Examinez les informations résumées
   - Appuyez sur **Créer le Prêt**

**Résultat** : Prêt créé avec succès, calendrier de paiements de 120 périodes créé automatiquement, notifications programmées.

**Wireframe - Étape 1 : Informations de base**

```text
┌─────────────────────────────────────────┐
│ <  Ajouter un Prêt                              │
├─────────────────────────────────────────┤
│ Nom du Prêt *                              │
│ [Prêt Hypothécaire - Appartement Centre]        │
│                                          │
│ Banque *                                    │
│ [Banque Santander ▼] [+ Créer Nouveau]       │
│                                          │
│ Montant du Prêt *                            │
│ [€180,000]                               │
│                                          │
│ Date de Décaissement *                      │
│ [01/04/2023] [📅]                        │
│                                          │
│ Durée du Prêt (années) *                       │
│ [10] années                               │
│ Note : L'application calcule automatiquement = 120 périodes  │
│                                          │
│ Heure de Notification 1 *                    │
│ [10:00] [🕐]                             │
│                                          │
│ Heure de Notification 2 *                    │
│ [19:00] [🕐]                             │
│                                          │
│ Type d'Intérêt *                          │
│ ● Solde Dégressif                      │
│ ○ Taux Fixe pour Toute la Durée             │
│                                          │
│ [SUIVANT] [ANNULER]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-02: Voir la liste et les détails des prêts

**Objectif** : Voir le résumé des prêts, filtrer par statut, rechercher et voir les détails de chaque prêt.

**Étapes** :
1. Allez à **Fonctions** → Sélectionnez **Prêts Bancaires**
2. Voyez l'écran de liste avec les filtres "Actif" (par défaut) et "Terminé"
3. Changez entre les filtres pour voir différents résumés
4. Utilisez la barre de recherche : Entrez "Centre"
5. Appuyez sur le prêt pour voir les détails
6. Voyez le calendrier des paiements avec les périodes payées, la période actuelle et les périodes futures
7. Utilisez la barre de recherche dans le calendrier des paiements : Entrez "9/2024"

**Résultat** : La liste s'affiche correctement par filtre, les détails du prêt affichent des informations complètes et le calendrier des paiements.

**Wireframe - Liste des Prêts**

```text
┌─────────────────────────────────────────┐
│ <  Gestion des Prêts Bancaires                 │
├─────────────────────────────────────────┤
│ [Actif] [Terminé]                    │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ Solde Actuel : €148,050          │  │
│ │ Prêt Original Total : €180,000      │  │
│ │ Intérêts Payés : €1,548              │  │
│ │ Actif : 1 prêt                     │  │
│ └─────────────────────────────────────┘  │
│                                          │
│ [🔍 Rechercher (nom du prêt, banque)]            │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ [ICON] Banque Santander  [Actif]    │  │
│ │ Prêt Hypothécaire - Appartement Centre      │  │
│ │ Solde : €148,050                   │  │
│ │ Original : €180,000                 │  │
│ │ Progrès : 8 / 120 périodes          │  │
│ │ Date Finale : 01/04/2033               │  │
│ └─────────────────────────────────────┘  │
│                                          │
│                                    [+]   │
└─────────────────────────────────────────┘
```

**Wireframe - Détails du Prêt**

```text
┌─────────────────────────────────────────┐
│ <  Détails du Prêt                         │
├─────────────────────────────────────────┤
│ [ICON] Banque Santander          [Modifier]  │
│ Prêt Hypothécaire - Appartement Centre           │
│ [Actif]                                 │
│                                          │
│ Prêt Original : €180,000                 │
│ Solde Actuel : €148,050               │
│ Périodes Payées : 8 / 120                    │
│ Intérêts Payés : €1,548                    │
│ Taux d'Intérêt Actuel : 9.0%/an        │
│                                          │
│ [Mettre à Jour Intérêt] [Calculer Règlement]│
│                                          │
│ Calendrier des Paiements                         │
│ [🔍 Rechercher période (ex. "5/2025")]     │
│                                          │
│ Période 1 – 05/2023 [Payé]                │
│ Total : €1.94k • Capital : €900 • Intérêts : €1.04k│
│                                          │
│ Période 9 – 01/2024 [Non Payé]            │
│ Capital : €900                        │
│ Intérêts : €1,035                        │
│ Total : €1,935                            │
│ Date d'Échéance : 15/01/2024                     │
│ [Marquer comme Payé]                           │
│                                          │
│ Période 10 – 02/2024 [Non Échu]            │
│ Total : €1.94k • Capital : €900 • Intérêts : €1.04k│
└─────────────────────────────────────────┘
```

---

### LOAN-03: Marquer une période de paiement comme payée (Enregistrer un paiement)

**Objectif** : Marquer une période de paiement comme "Payée" après avoir effectué le paiement à la banque.

**Étapes** :
1. Allez aux détails du prêt
2. Trouvez la période actuelle (Période 9) avec le badge "Non Payé"
3. Appuyez sur **Marquer comme Payé**
4. Complétez les informations :
   - Date de paiement réel : 15/01/2024 (par défaut = aujourd'hui)
   - Intérêts payés réels : €1,035 (par défaut = intérêts planifiés)
   - Note : (optionnelle)
5. Voyez le paiement total réel calculé automatiquement
6. Appuyez sur **Confirmer**

**Résultat** : Période 9 mise à jour à "Payée", le solde diminue, les périodes payées augmentent, le solde actuel diminue.

**Wireframe - Dialogue Marquer comme Payé**

```text
┌─────────────────────────────────────────┐
│ Marquer comme Payé                             │
├─────────────────────────────────────────┤
│ Période 9 – 01/2024          [Non Payé]   │
│                                          │
│ Date d'Échéance (planifiée) : 15/01/2024          │
│ Capital (fixe) : €900                │
│                                          │
│ Date de Paiement Réel *                    │
│ [15/01/2024] [📅]                        │
│                                          │
│ Intérêts Payés Réels *                   │
│ [€1,035]                                 │
│ Note : Intérêts planifiés : €1,035           │
│                                          │
│ Paiement Total Réel =                   │
│   €900 (Capital)                    │
│ + €1,035 (Intérêts Réels)              │
│ ────────────────────────────────        │
│ = €1,935                                 │
│                                          │
│ Note (optionnelle)                          │
│ [Payé €50 de moins, a reçu réduction d'intérêts...]│
│                                          │
│ [ANNULER] [CONFIRMER]                       │
└─────────────────────────────────────────┘
```

---

### LOAN-04: Mettre à jour le taux d'intérêt actuel (Lorsque la banque ajuste le taux variable)

**Objectif** : Mettre à jour le nouveau taux d'intérêt lorsque la banque annonce un ajustement du taux variable.

**Étapes** :
1. Allez aux détails du prêt
2. Voyez "Taux d'Intérêt Actuel : 9.0%/an"
3. Appuyez sur **Mettre à Jour le Taux d'Intérêt Actuel** (s'affiche uniquement si actuellement en période de taux variable)
4. Complétez les informations :
   - Nouveau taux d'intérêt : 10.5%/an
   - Date effective : 15/01/2024 (par défaut = début de la période actuelle)
   - Note : "Banque a ajusté le taux d'intérêt selon nouvelle décision"
5. Appuyez sur **Enregistrer**

**Résultat** : Taux d'intérêt actuel mis à jour, les périodes non payées depuis la période actuelle sont mises à jour avec le nouveau taux d'intérêt.

**Wireframe - Dialogue Mettre à Jour le Taux d'Intérêt**

```text
┌─────────────────────────────────────────┐
│ Mettre à Jour le Taux d'Intérêt Actuel             │
├─────────────────────────────────────────┤
│ [ICON] Banque Santander                   │
│ Nom du Prêt : Prêt Hypothécaire - Appartement Centre│
│ Période Actuelle : Période 9 – 01/2024       │
│ Statut : [Actif]                         │
│ Période : Variable (après promotionnel)     │
│                                          │
│ Taux d'Intérêt Actuel (appliquant) :       │
│ [9.0] %/an (lecture seule)                  │
│                                          │
│ Nouveau Taux d'Intérêt (%/an) *              │
│ [10.5] %/an                            │
│                                          │
│ Date Effective *                         │
│ [15/01/2024] [📅]                        │
│                                          │
│ Note (optionnelle)                          │
│ [Banque a ajusté le taux d'intérêt...]         │
│                                          │
│ • Le nouveau taux d'intérêt s'appliquera aux périodes depuis    │
│   la Période Actuelle et suivantes.   │
│ • Les périodes précédemment payées restent inchangées. │
│                                          │
│ [ANNULER] [ENREGISTRER]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-05: Règlement anticipé (Paiement partiel pour réduire les intérêts)

**Objectif** : Règler une partie du prêt anticipativement pour réduire les intérêts totaux à payer et raccourcir la durée du prêt.

**Étapes** :
1. Allez aux détails du prêt
2. Appuyez sur **Calculer le Montant du Règlement**
3. **Étape 1 - Entrer les informations de prépaiement :**
   - Sélectionnez la méthode : "Paiement Partiel"
   - Sélectionnez la date de prépaiement : 15/01/2024
   - Entrez le montant de prépaiement : €72,000
   - Voyez la pénalité calculée automatiquement : €1,440 (2.0%)
   - Appuyez sur **Suivant**
4. **Étape 2 - Comparer les options :**
   - Voyez la comparaison entre "Sans Prépaiment" et "Prépaiement €72,000"
   - Voyez les résultats : Économiser €27,000 en intérêts, réduire 40 périodes
   - Appuyez sur **Confirmer le Prépaiment**

**Résultat** : Le solde diminue, le calendrier des paiements est recalculé, le nombre de périodes diminue, la date finale est antérieure.

**Wireframe - Étape 1 : Entrer les informations de prépaiement**

```text
┌─────────────────────────────────────────┐
│ <  Règlement Anticipé                      │
├─────────────────────────────────────────┤
│ [ICON] Banque Santander                   │
│ Nom du Prêt : Prêt Hypothécaire - Appartement Centre│
│ Solde Actuel : €180,000                │
│ Période Actuelle : Période 9 – 01/2024       │
│                                          │
│ Comment souhaitez-vous régler ?              │
│ ● Paiement Partiel                        │
│ ○ Règlement Complet                        │
│                                          │
│ Date de Prépaiment *                        │
│ [15/01/2024] [📅]                        │
│                                          │
│ Montant de Prépaiment *                      │
│ [€72,000]                                │
│                                          │
│ Taux de Pénalité Appliquée : 2.0%                │
│ Pénalité : €1,440                          │
│                                          │
│ [SUIVANT]                                   │
└─────────────────────────────────────────┘
```

**Wireframe - Étape 2 : Comparer les options**

```text
┌─────────────────────────────────────────┐
│ <  Comparer les Options                       │
├─────────────────────────────────────────┤
│ OPTION A : Sans Prépaiment                 │
│ ────────────────────────────────────────│
│ Intérêts Totaux Payés jusqu'à aujourd'hui :            │
│   €46,800                               │
│ Intérêts Totaux Restants : €46,800       │
│ Périodes Restantes : 112 périodes          │
│ Date Finale : 01/04/2033                    │
│                                          │
│ OPTION B : Prépaiment €72,000            │
│ ────────────────────────────────────────│
│ Pénalité de Paiement Anticipé : €1,440           │
│ Intérêts Totaux Payés jusqu'à aujourd'hui :            │
│   €48,240                               │
│ Intérêts Totaux Restants : €19,800       │
│ Périodes Restantes : 72 périodes           │
│ Date Finale : 01/04/2029                    │
│                                          │
│ RÉSULTAT DE COMPARAISON :                       │
│ • Économie d'Intérêts : €27,000             │
│ • Réduction de Temps : 40 périodes (~3.5 ans)│
│                                          │
│ [CONFIRMER LE PRÉPAIEMENT]                     │
└─────────────────────────────────────────┘
```

---

### LOAN-06: Modifier un prêt (Modifier les informations de base)

**Objectif** : Modifier les informations de base du prêt (nom, banque, note) après avoir commencé les paiements.

**Étapes** :
1. Allez aux détails du prêt
2. Appuyez sur **Modifier** (ne peut modifier que le nom, la note, la banque)
3. Modifiez :
   - Nom du Prêt : "Prêt Hypothécaire - Appartement Centre - Unité A1-1201"
   - (Optionnel) Changer la banque : Banque BBVA
   - Note : "Transféré à une nouvelle banque"
4. Voyez les champs désactivés : Montant du Prêt, Date de Décaissement, Durée, Taux d'Intérêt
5. Appuyez sur **Enregistrer**

**Résultat** : Informations de base mises à jour, autres informations inchangées.

**Note** : Si le prêt n'a pas encore effectué de paiements, toutes les informations peuvent être modifiées (montant, durée, configuration d'intérêt).

## 6. Logique & règles

### 6.1 Taux Promotionnel/Variable

- Peut avoir une période promotionnelle (taux d'intérêt plus bas)
- Après la période promotionnelle, le taux d'intérêt varie par période
- Chaque période peut être **Variable** (basée sur le marché) ou **Fixe**

### 6.2 Pénalités de Retard de Paiement

- Les pénalités sont calculées par %/an
- Peut être configuré différemment pour chaque période
- Les pénalités ne s'appliquent que lorsque le paiement est en retard

### 6.3 Calendrier des Paiements

- L'application crée automatiquement le calendrier des paiements basé sur :
  - Montant du prêt
  - Taux d'intérêt
  - Durée
- Chaque période de paiement comprend : Capital + Intérêts

### 6.4 Règlement Anticipé

- Calculer le montant restant (capital + intérêts + pénalités si présentes)
- Après le règlement, le prêt changera au statut "Terminé"

### 6.5 Notifications

- L'application envoie une notification de rappel lorsque le paiement est en retard
- L'heure de notification peut être configurée pour chaque prêt (`notificationTime1`, `notificationTime2`, par défaut 10:00 et 19:00)

## 7. Notes importantes

- **Taux d'Intérêt Complexes** : Ce module prend en charge les taux d'intérêt qui changent par période, nécessite une configuration minutieuse
- **Ne peut pas supprimer lorsque le calendrier des paiements existe** : Si le calendrier des paiements existe, ne peut que régler, pas supprimer
- **Règlement Anticipé** : Peut nécessiter des frais de pénalité supplémentaires, dépend de la politique de la banque
- **Calendrier des Paiements** : Le calendrier des paiements est calculé automatiquement, ne peut pas éditer directement

