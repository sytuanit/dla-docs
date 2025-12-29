# Occasions Spéciales

## 1. Objectif

Le module **Occasions Spéciales** vous aide à :
- Gérer les occasions spéciales pendant l'année (anniversaires, fêtes, etc.)
- Créer des listes de tâches (étapes de préparation)
- Attacher des listes de courses à chaque étape de préparation
- Rappels avant les occasions
- Suivi de la progression de la préparation

## 2. Quand utiliser

Utilisez ce module lorsque vous souhaitez :
- Gérer les occasions spéciales pendant l'année
- Vous préparer pour des occasions importantes
- Créer des listes de tâches
- Recevoir des rappels avant les occasions

## 3. Écrans associés

- Liste des occasions spéciales
- Ajouter une nouvelle occasion spéciale
- Détails de l'occasion et étapes de préparation
- Ajouter une étape de préparation
- Sélectionner une liste de courses
- Créer une nouvelle liste de courses

## 4. Utilisation principale

### 4.1 Ajouter une occasion spéciale

1. Allez à **Fonctions** → Sélectionnez **Occasions Spéciales**
2. Appuyez sur le bouton **➕** (FAB)
3. Complétez les informations :
   - **Nom de l'Occasion** : (ex. "Anniversaire de Maman")
   - **Date** : Sélectionnez jour/mois (DatePicker ne sélectionne que jour/mois, pas l'année)
   - **Utiliser calendrier lunaire** : (Optionnel) Cochez si vous souhaitez utiliser le calendrier lunaire
     - Si coché : Entrez le jour et le mois lunaire, l'app calcule automatiquement la prochaine date solaire
   - **Répéter** : Annuellement / Seulement cette année
   - **Afficher notification à** : Sélectionnez l'heure (requis, ex. 07:00)
   - **Note** : Informations supplémentaires (optionnelles)
4. (Optionnel) Ajoutez des étapes de préparation (voir 4.2)
5. Appuyez sur **Enregistrer**

### 4.2 Ajouter une étape de préparation

1. Lors de l'ajout d'une nouvelle occasion : Appuyez sur **+ Ajouter Étape** dans la section "Étapes de Préparation"
2. Ou depuis les détails de l'occasion : Appuyez sur **+ Ajouter Étape**
3. Complétez les informations :
   - **Quand ?** : "X jours avant" ou "Le jour"
   - **Nombre de jours** : (si "X jours avant" est sélectionné) Entrez le nombre de jours avant l'occasion
   - **Afficher notification à** : Sélectionnez l'heure (requis)
   - **Répéter quotidiennement jusqu'à complétion** : (Optionnel) Cochez si vous souhaitez des rappels quotidiens
   - **Contenu** : Nom de l'étape (requis, ex. "Acheter un cadeau")
   - **Note** : (Optionnelle)
   - **Utiliser liste de courses** : (Optionnel) Cochez pour lier avec une liste de courses
4. Appuyez sur **Ajouter** (ou FAB "Appliquer")

### 4.3 Créer une liste de courses

1. Lors de l'ajout d'une étape de préparation, cochez **Utiliser liste de courses**
2. L'écran "Sélectionner une liste de courses" s'ouvre automatiquement
3. Appuyez sur le FAB **➕** pour créer une nouvelle liste de courses
4. Entrez le nom de la liste de courses
5. Ajoutez des éléments :
   - Entrez le nom de l'élément
   - Appuyez sur **➕** pour ajouter un nouvel élément
6. Appuyez sur **Enregistrer**
7. La nouvelle liste de courses est automatiquement sélectionnée et vous retournez à l'écran "Ajouter une étape de préparation"

### 4.4 Marquer une étape comme complétée

1. Allez aux détails de l'occasion spéciale
2. Trouvez l'étape à marquer
3. Appuyez sur la case [ ] pour passer à [✓]
4. S'il y a une liste de courses, appuyez sur le nom de la liste de courses pour afficher les éléments et cocher/décocher

### 4.5 Voir la progression

1. Allez aux détails de l'occasion spéciale
2. Affichez la section "Résumé" :
   - Étapes de préparation : Nombre total d'étapes
   - Complétées : Nombre d'étapes marquées / Total d'étapes
   - Statut : Non commencé / En cours / Complété

### 4.6 Modifier une occasion spéciale

1. Allez aux détails de l'occasion spéciale
2. Appuyez sur le lien hypertexte **Modifier ›** dans l'en-tête
3. Modifiez les informations : Nom, Date, Répéter, Heure de rappel, Note
4. Appuyez sur **Enregistrer**

### 4.7 Modifier une étape de préparation

1. Allez aux détails de l'occasion spéciale
2. Appuyez sur l'étape pour modifier (cliquez sur tout l'élément, sauf l'icône Supprimer)
3. Modifiez les informations : Temps, Contenu, Liste de courses
4. Appuyez sur **Appliquer** (ou FAB)

## 5. Exemples & illustrations d'interface

### 5.1 OCCASION-01: Créer une nouvelle occasion spéciale (Anniversaire avec étapes de préparation)

**Objectif** : Créer une nouvelle occasion spéciale (anniversaire) avec des étapes de préparation pour que l'app vous rappelle automatiquement avant que l'occasion ne se produise.

**Étapes principales** :
1. Allez à Fonctions → Occasions Spéciales → Appuyez sur le bouton "➕" (FAB)
2. Entrez le nom de l'occasion, sélectionnez la date (01/05), sélectionnez Répéter "Annuellement", sélectionnez l'heure de rappel (07:00)
3. Ajoutez l'étape de préparation 1 : "7 jours avant – 08:00" - "Acheter un cadeau"
4. Ajoutez l'étape de préparation 2 : "1 jour avant – 19:00" - "Commander un gâteau"
5. Appuyez sur "Enregistrer"

**Illustration d'interface - Écran Ajouter une Occasion Spéciale** :

```text
┌──────────────────────────────────────────────┐
│ <  Ajouter une Occasion Spéciale                      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📝 Informations de l'Occasion                      │
│                                               │
│ Nom de l'Occasion *                       │
│ [ Anniversaire d'An                      ]       │
│                                               │
│ Date                                          │
│ [ 01 / 05            ▼ ]                      │
│ (DatePicker ne sélectionne que jour/mois)          │
│                                               │
│ [ ] Utiliser calendrier lunaire                        │
│                                               │
│ Répéter                                        │
│ (•) Annuellement                                     │
│ ( ) Seulement cette année                            │
│                                               │
│ Afficher notification à *                        │
│ [ 07:00        ▼ ]                            │
│                                               │
│ Note (optionnelle)                                │
│ [                                      ]      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📋 Étapes de Préparation          [ + Ajouter Étape ]│
│ ┌──────────────────────────────────────────┐ │
│ │  1. Acheter un cadeau                   [Icône Supprimer] │ │
│ │     7 jours avant – 08:00                 │ │
│ │ ──────────────────────────────────────── │ │
│ │  2. Commander un gâteau                   [Icône Supprimer] │ │
│ │     1 jour avant – 19:00                 │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘

        [ Annuler ]                        [ Enregistrer ]
```

---

### 5.2 OCCASION-02: Créer une occasion spéciale avec calendrier lunaire (Jour de Commémoration avec liste de courses)

**Objectif** : Créer une occasion spéciale avec calendrier lunaire (jour de commémoration) avec des étapes de préparation liées à une liste de courses pour suivre l'achat d'offrandes.

**Étapes principales** :
1. Allez à Fonctions → Occasions Spéciales → Appuyez sur le bouton "➕" (FAB)
2. Entrez le nom de l'occasion "Jour de Commémoration de Maman", cochez "Utiliser calendrier lunaire"
3. Entrez la date lunaire : 15/11, l'app calcule automatiquement la date solaire : 15/12/2025
4. Ajoutez 3 étapes de préparation, où l'étape 2 a un lien de liste de courses "Acheter des offrandes"
5. Appuyez sur "Enregistrer"

**Illustration d'interface - Sélectionner date lunaire** :

```text
│ │ │ Date lunaire                                   │ │ │
│ │ │ Jour (1-30)    Mois (1-12)                   │ │ │
│ │ │ [ 15 ]        [ 11 ]                         │ │ │
│ │ │                                               │ │ │
│ │ │ Date solaire (calculée automatiquement - visualisation seule)  │ │ │
│ │ │ [ Texte : 15/12/2025                 ]         │ │ │
│ │ │ (C'est la PROCHAINE date solaire dans le futur)│ │ │
```

---

### 5.3 OCCASION-03: Voir la liste et les détails des occasions spéciales

**Objectif** : Voir le résumé des occasions spéciales, filtrer par temps et voir les détails de chaque occasion avec la progression de la préparation.

**Étapes principales** :
1. Allez à Fonctions → Occasions Spéciales
2. Affichez la liste avec les filtres "Toutes", "Prochaines", "Ce mois"
3. Appuyez sur la carte de l'occasion pour voir les détails
4. Affichez le résumé : Nombre d'étapes, Complétées, Statut
5. Marquez l'étape comme complétée en cochant la case

**Illustration d'interface - Écran Liste des Occasions Spéciales** :

```text
┌────────────────────────────────────────────────────────────┐
│ 📅 Liste des Occasions Spéciales                                  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ + Ajouter Occasion ]                                     │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔍 Filtre : [ Toutes ]  [ Prochaines ]  [ Ce mois ]      │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Jour de Commémoration de Maman    [En cours] [Icône Supprimer] │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 📅 15/12/2025 • 15/11 (Lunaire) • 10 jours restants  │ │ │
│ │ │                                                      │ │ │
│ │ │ ✅ Étapes de préparation requises :                        │ │ │
│ │ │   [✓] 3 jours avant – Lister offrandes               │ │ │
│ │ │   [ ] 1 jour avant – Acheter offrandes     │ │ │
│ │ │   [ ] Le jour – Préparer autel / cérémonie        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

**Illustration d'interface - Écran Détails de l'Occasion Spéciale** :

```text
┌─────────────────────────────────────────────────────────┐
│ 📋 Détails de l'Occasion Spéciale                             │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Jour de Commémoration de Maman                       [Modifier ›]        │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 15/12/2025 (Solaire) • 15/11 (Calendrier lunaire)      │ │ │
│ │ │ 10 jours restants • Répéter : Annuellement                │ │ │
│ │ │                                                      │ │ │
│ │ │ Note :                                             │ │ │
│ │ │ Petit repas, fleurs blanches, limiter les invités.          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📊 Résumé                                         │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Étapes de préparation : 3                              │ │ │
│ │ │ Complétées : 1 / 3                                 │ │ │
│ │ │ Statut : [En cours]                            │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Étapes de Préparation                  [ + Ajouter Étape ]                  │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ [✓] Lister offrandes                    [Icône Supprimer]           │ │ │
│ │ │     3 jours avant – 08:00                        │ │ │
│ │ │     Complété à 09:15 – 12/12/2025               │ │ │
│ │ │ ──────────────────────────────────────────────────── │ │ │
│ │ │                                                      │ │ │
│ │ │ [ ] Acheter offrandes            [Icône Supprimer]            │ │ │
│ │ │     1 jour avant – 19:00                      │ │ │
│ │ │     Répéter quotidiennement jusqu'à complétion                  │ │ │
│ │ │     Lista de courses : Acheter offrandes ›           │ │ │
│ │ │     [✓] Complété 3 / 8 éléments                        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

---

### 5.4 OCCASION-04: Ajouter une étape de préparation avec liste de courses

**Objectif** : Ajouter une nouvelle étape de préparation pour une occasion spéciale et la lier avec une liste de courses pour suivre les achats.

**Étapes principales** :
1. Allez aux détails de l'occasion spéciale → Appuyez sur "+ Ajouter Étape"
2. Sélectionnez "Quand ?" : "X jours avant", entrez le nombre de jours : 1
3. Sélectionnez l'heure de rappel : 19:00
4. Activez "Répéter quotidiennement jusqu'à complétion"
5. Entrez le contenu : "Acheter des offrandes"
6. Cochez "Utiliser liste de courses" → Sélectionnez la liste de courses "Acheter des offrandes"
7. Appuyez sur "Ajouter"

**Illustration d'interface - Écran Ajouter une Étape de Préparation** :

```text
┌────────────────────────────────────────────────────────────┐
│ ➕ Ajouter une Étape de Préparation                                     │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ⏰ Temps de Préparation                                    │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Quand ? * (requis)                                │ │ │
│ │ │ [ X jours avant         ▼ ]                       │ │ │
│ │ │                                                      │ │ │
│ │ │ Nombre de jours * (s'affiche uniquement si "X jours avant") │ │ │
│ │ │ [  1  ]  jours avant                               │ │ │
│ │ │                                                      │ │ │
│ │ │ Afficher notification à * (requis)                  │ │ │
│ │ │ [ 19:00        ▼ ]                                 │ │ │
│ │ │                                                      │ │ │
│ │ │ [✓] Répéter quotidiennement jusqu'à complétion                    │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Contenu                                             │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Contenu * (requis)                              │ │ │
│ │ │ [ Acheter des offrandes               ]        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔗 Lier avec une liste de courses ?                       │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ ☑ Utiliser liste de courses                                    │ │ │
│ │ │ Liste de courses : Acheter offrandes ›    [Icône Changer]  │ │ │
│ │ │ (8 éléments)                                          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ Annuler ]                        [ Ajouter ]             │ │
│ └────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

### 5.5 OCCASION-05: Marquer une étape de préparation comme complétée et afficher la progression de la liste de courses

**Objectif** : Marquer les étapes de préparation comme complétées et suivre la progression de la liste de courses.

**Étapes principales** :
1. Allez aux détails de l'occasion spéciale
2. Affichez l'étape avec la liste de courses qui montre la progression "Complété 3 / 8 éléments"
3. Appuyez sur le nom de la liste de courses pour voir les détails et cocher/décocher les éléments
4. Cochez la case de l'étape pour marquer comme complétée
5. Affichez le "Résumé" mis à jour en temps réel

---

### 5.6 OCCASION-06: Modifier une occasion spéciale et des étapes de préparation

**Objectif** : Modifier les informations de l'occasion spéciale et des étapes de préparation après les avoir créées.

**Étapes principales** :
1. Allez aux détails de l'occasion spéciale → Appuyez sur "Modifier ›"
2. Modifiez le nom de l'occasion, la note
3. Appuyez sur "Enregistrer"
4. Appuyez sur l'étape pour modifier : Changez le temps, le contenu
5. Appuyez sur l'icône Supprimer pour supprimer l'étape (a un dialogue de confirmation)

## 6. Logique & règles

### 6.1 Données du calendrier lunaire

- Vous pouvez entrer à la fois des dates solaires et lunaires
- L'app calcule automatiquement la date solaire correspondante à la date lunaire
- Prend en charge la répétition annuelle selon le calendrier lunaire

### 6.2 Répéter

- **Annuellement** : L'occasion se répète chaque année (selon le calendrier solaire ou lunaire)
  - Avec calendrier solaire : Chaque année calcule nextOccurDate basé sur (jour/mois) de solarDate
  - Avec calendrier lunaire : Chaque année convertit de la date lunaire à la date solaire correspondante et met à jour nextOccurDate
- **Seulement cette année** : L'occasion n'est valable que pour l'année en cours, ne se répète pas l'année prochaine

### 6.3 Étapes de préparation

- **Quand ?** : A 2 options :
  - **X jours avant** : Rappeler X jours avant la date de l'occasion (doit entrer le nombre de jours)
  - **Le jour** : Rappeler à la date de l'occasion (n'a pas besoin d'entrer le nombre de jours)
- **Afficher notification à** : Heure de rappel (requis, format HH:mm)
- **Répéter quotidiennement jusqu'à complétion** : Si activé, la notification se répète quotidiennement jusqu'à ce que l'utilisateur marque l'étape comme complétée
- **Lier liste de courses** : Chaque étape peut attacher une liste de courses pour suivre la progression des achats

### 6.4 Liste de courses

- La liste de courses peut être réutilisée pour plusieurs étapes
- Suit le nombre d'éléments complétés / Total d'éléments (ex. "Complété 3 / 8 éléments")
- Affichée dans les détails de l'étape avec le lien "Nom de la liste de courses ›" pour voir les détails
- Vous pouvez cocher/décocher les éléments dans la liste de courses pour mettre à jour la progression
- L'étape de préparation peut être marquée comme complétée même si la liste de courses n'est pas complètement complétée

### 6.5 Notifications

- **Notification de l'occasion principale** : Créée à `nextOccurDate + reminder_time`
  - Avec occasion ANNUALE : La notification est recréée lorsque l'app démarre (basée sur nextOccurDate nouvellement calculé)
  - Avec occasion UNE FOIS : La notification est créée une seule fois pour le nextOccurDate actuel
- **Notification d'étape de préparation** : Calculez la date de rappel basée sur :
  - `nextOccurDate` de l'occasion spéciale
  - `reminderType` et `daysBefore` (s'il existe)
  - `reminderTime`
- **Notification de répétition** : Si `repeatDailyUntilComplete = true` :
  - Créez une notification de répétition quotidienne
  - Utilisez `notificationGroupKey` pour regrouper les notifications de répétition
  - Annulée automatiquement lorsque l'utilisateur marque l'étape comme complétée

## 7. Notes importantes

- **Données du calendrier lunaire** : 
  - L'app convertit automatiquement au calendrier solaire pour l'affichage
  - Trouve la "PROCHAINE date solaire dans le futur" par rapport à la date actuelle
  - Années futures : Le système calcule toujours la date solaire correspondante depuis (jour lunaire, mois lunaire) pour chaque année à nouveau
  - Si cette année a à la fois le mois régulier et le mois intercalaire du même mois : Le système peut créer 2 rappels pour éviter de manquer quelque chose
- **Répétition annuelle** : 
  - L'occasion recalcule automatiquement nextOccurDate l'année prochaine
  - Avec calendrier lunaire : Chaque année convertit de la date lunaire à la date solaire correspondante
- **Heure de rappel** : 
  - Doit avoir une valeur (ne peut pas être vide)
  - Doit avoir un format correct HH:mm (00:00 - 23:59)
- **Liste de courses** : 
  - La liste de courses supprimée est toujours affichée dans l'étape (mais ne peut pas être modifiée)
  - Vous pouvez marquer l'étape comme complétée même si la liste de courses n'est pas complètement complétée
- **Notifications** : 
  - Vous devez activer les notifications dans Paramètres pour recevoir les rappels
  - Les notifications de répétition sont annulées automatiquement lorsque l'étape est marquée comme complétée
- **Statut de l'occasion** :
  - **Non commencé** : Toutes les étapes ne sont pas complétées (gris)
  - **En cours** : Au moins 1 étape est complétée, mais pas toutes (bleu)
  - **Complété** : Toutes les étapes sont complétées (vert foncé)
  - Si l'occasion n'a pas d'étapes de préparation : Le statut est calculé selon la date (Non commencé / En cours / Complété)

