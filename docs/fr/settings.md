# Paramètres

## 1. Objectif

Le module **Paramètres** vous permet de configurer l'application selon vos besoins personnels, notamment :
- Langue et devise
- Notifications
- Catégories
- Sauvegarde et restauration des données
- Sécurité (mot de passe, Face ID)

## 2. Quand utiliser

Utilisez ce module si vous souhaitez :
- Changer la langue ou la devise
- Activer/désactiver les notifications
- Gérer les catégories (ajouter, modifier, supprimer, définir comme par défaut)
- Sauvegarder ou restaurer les données
- Changer le mot de passe ou activer Face ID

## 3. Écrans associés

- Écran principal des paramètres
- Paramètres de base
- Sélectionner la langue
- Sélectionner la devise
- Gérer les catégories
- Sauvegarder les données
- Restaurer les données
- Changer le mot de passe
- Activer Face ID / Empreinte digitale

## 4. Utilisation principale

### 4.1 Changer la langue

1. Allez à **Paramètres** → **Affichage et Langue** → **Langue**
2. Sélectionnez la langue souhaitée
3. L'application se recharge automatiquement avec la nouvelle langue

### 4.2 Changer la devise

1. Allez à **Paramètres** → **Affichage et Langue** → **Devise**
2. Sélectionnez le type de devise
3. Tous les montants sont affichés dans la nouvelle unité

### 4.3 Activer/désactiver les notifications

1. Allez à **Paramètres** → **Notifications**
2. Basculez l'interrupteur **Notifications**
3. Si activé, vous recevrez des rappels concernant :
   - Revenus récurrents dus
   - Dépenses récurrentes dues
   - Comptes d'épargne dus
   - Occasions spéciales à venir

### 4.4 Gérer les catégories

1. Allez à **Paramètres** → **Catégories**
2. Sélectionnez le type de catégorie à gérer :
   - Revenus récurrents
   - Revenus supplémentaires
   - Dépenses récurrentes
   - Dépenses quotidiennes
3. Ajouter/modifier/supprimer des catégories
4. Définir une catégorie par défaut (pour les dépenses quotidiennes)

### 4.5 Sauvegarder les données

1. Allez à **Paramètres** → **Sauvegarde et Données** → **Sauvegarde**
2. Sélectionnez l'emplacement de stockage (système de fichiers)
3. Appuyez sur **Sauvegarder**
4. Le fichier de sauvegarde est créé

### 4.6 Restaurer les données

1. Allez à **Paramètres** → **Sauvegarde et Données** → **Restauration**
2. Sélectionnez le fichier de sauvegarde
3. Confirmez la restauration
4. **Note** : La restauration remplace les données actuelles

## 5. Illustrations UI (Wireframe)

### 5.1 Écran principal des paramètres

```text
┌─────────────────────────────────────────┐
│  ← Retour    Paramètres                    │
├─────────────────────────────────────────┤
│  Affichage et Langue                     │
│  ┌───────────────────────────────────┐ │
│  │ Langue                           │ │
│  │ Français                      →     │ │
│  │                                    │ │
│  │ Devise                           │ │
│  │ EUR (€)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notifications                          │
│  ┌───────────────────────────────────┐ │
│  │ Notifications                [ON]  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Sauvegarde et Données                          │
│  ┌───────────────────────────────────┐ │
│  │ Sauvegarde                        →    │ │
│  │                                    │ │
│  │ Restauration                       →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Catégories                             │
│  ┌───────────────────────────────────┐ │
│  │ Gérer les catégories              →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Sécurité                               │
│  ┌───────────────────────────────────┐ │
│  │ Mot de passe                        →    │ │
│  │                                    │ │
│  │ Face ID / Empreinte digitale          →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logique et règles

### 6.1 Langue

- Supporte : Français, English, Tiếng Việt, 日本語
- Le changement de langue recharge toute l'application
- Les catégories système sont automatiquement traduites dans la nouvelle langue

### 6.2 Devise

- Chaque langue a une devise par défaut (ex. EUR pour le français)
- Vous pouvez sélectionner une autre devise
- Tous les montants sont formatés selon la devise sélectionnée

### 6.3 Notifications

- Les notifications fonctionnent uniquement si l'application a la permission
- L'heure de notification dépend de chaque fonction et peut être configurée :
  - Revenus/Dépenses récurrents : `notificationTime1`, `notificationTime2` (par défaut 16:00 et 19:00)
  - Comptes d'épargne et prêts : `notificationTime1`, `notificationTime2` (par défaut 10:00 et 19:00)
  - Occasions spéciales et étapes de préparation : selon `reminderTime` que vous entrez
  - Peut désactiver les notifications pour chaque type séparément (à l'avenir)

### 6.4 Catégories

- Les catégories système ne peuvent pas être supprimées, seulement désactivées
- Les catégories utilisateur peuvent être supprimées (si elles ne sont pas utilisées)
- Chaque type de catégorie est indépendant (revenus récurrents, dépenses quotidiennes, etc.)

## 7. Notes importantes

- **Sauvegarder régulièrement** : Vous devriez sauvegarder les données périodiquement pour éviter la perte de données
- **La restauration remplace** : La restauration remplace toutes les données actuelles
- **Mot de passe** : Si vous oubliez le mot de passe, vous pouvez le réinitialiser (supprime les données)

