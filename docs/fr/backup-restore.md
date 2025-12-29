# Sauvegarde et Restauration

## 1. Objectif

Le module **Sauvegarde et Restauration** vous aide à :
- Sauvegarder toutes les données de l'application dans un fichier
- Restaurer les données à partir d'un fichier de sauvegarde
- Protéger les données contre la perte due à une défaillance de l'appareil ou à une réinstallation de l'application

## 2. Quand utiliser

Utilisez ce module si vous souhaitez :
- Sauvegarder les données avant une réinstallation de l'application
- Transférer les données vers un nouvel appareil
- Restaurer les données après une perte de données
- Créer des sauvegardes périodiques

## 3. Écrans associés

- Écran de sauvegarde
- Écran de restauration

## 4. Utilisation principale

### 4.1 Sauvegarder les données

1. Allez à **Paramètres** → **Sauvegarde et Données** → **Sauvegarde**
2. Affichez les informations :
   - Nombre d'enregistrements à sauvegarder
   - Taille de fichier attendue
3. Appuyez sur **Sauvegarder**
4. Sélectionnez l'emplacement de stockage (système de fichiers)
5. Le fichier de sauvegarde est créé avec le nom : `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Enregistrez ce fichier dans un endroit sûr (Cloud, ordinateur, etc.)

### 4.2 Restaurer les données

1. Allez à **Paramètres** → **Sauvegarde et Données** → **Restauration**
2. Sélectionnez le fichier de sauvegarde dans le système de fichiers
3. Affichez les informations du fichier :
   - Date de création de la sauvegarde
   - Nombre d'enregistrements
   - Taille du fichier
4. **Avertissement** : La restauration remplace toutes les données actuelles
5. Appuyez sur **Restaurer**
6. Confirmez la restauration
7. Attendez que le processus de restauration soit terminé
8. L'application se recharge automatiquement

## 5. Illustrations UI (Wireframe)

### 5.1 Écran de sauvegarde

```text
┌─────────────────────────────────────────┐
│  ← Retour    Sauvegarder les données                   │
├─────────────────────────────────────────┤
│  Informations de sauvegarde                      │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Nombre d'enregistrements                  │ │
│  │ 1.234 enregistrements                      │ │
│  │                                    │ │
│  │ Taille attendue                      │ │
│  │ ~2,5 MB                            │ │
│  │                                    │ │
│  │ Données à sauvegarder :              │ │
│  │ • Revenus récurrents                 │ │
│  │ • Dépenses récurrentes               │ │
│  │ • Dépenses quotidiennes                   │ │
│  │ • Budget                           │ │
│  │ • Épargnes                          │ │
│  │ • Prêts                            │ │
│  │ • Occasions spéciales                │ │
│  │ • Catégories                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Sauvegarder]                               │
└─────────────────────────────────────────┘
```

### 5.2 Écran de restauration

```text
┌─────────────────────────────────────────┐
│  ← Retour    Restaurer les données                 │
├─────────────────────────────────────────┤
│  Sélectionner le fichier de sauvegarde                      │
│                                         │
│  [Sélectionner un fichier...]                       │
│                                         │
│  Informations du fichier                       │
│  ┌───────────────────────────────────┐ │
│  │ Fichier : dla-backup-2024-11-15.json │ │
│  │                                    │ │
│  │ Créé : 15/11/2024 10:30         │ │
│  │                                    │ │
│  │ Nombre d'enregistrements : 1.234         │ │
│  │                                    │ │
│  │ Taille : 2,5 MB                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Avertissement                             │
│  La restauration remplace toutes les données actuelles     │
│  actuelles. Êtes-vous sûr ?                    │
│                                         │
│  [Restaurer] [Annuler]                     │
└─────────────────────────────────────────┘
```

## 6. Logique et règles

### 6.1 Format du fichier de sauvegarde

- Le fichier de sauvegarde est au format JSON
- Nom du fichier : `dla-backup-YYYY-MM-DD-HHmmss.json`
- Contient toutes les données : Utilisateur, Catégories, Transactions, Budgets, etc.

### 6.2 Données sauvegardées

- Toutes les tables de la base de données
- Contient à la fois les données système et les données utilisateur
- Ne contient pas : Paramètres de l'application, Préférences (langue, devise)

### 6.3 Restauration

- La restauration supprime toutes les données actuelles
- Puis importe les données du fichier de sauvegarde
- L'application se recharge automatiquement après la fin de la restauration

### 6.4 Validation

- L'application vérifie le format du fichier avant la restauration
- Vérifie la compatibilité des versions (si disponible)
- Affiche une erreur si le fichier est invalide

## 7. Notes importantes

- **Sauvegarder régulièrement** : Vous devriez sauvegarder périodiquement (hebdomadairement ou mensuellement)
- **Stocker à plusieurs endroits** : Enregistrez le fichier de sauvegarde à plusieurs endroits (Cloud, ordinateur, USB)
- **La restauration perd les données actuelles** : Assurez-vous d'avoir sauvegardé les données actuelles avant de restaurer
- **Ne peut pas être annulé** : Après la restauration, cela ne peut pas être annulé

