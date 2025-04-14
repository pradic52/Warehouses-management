# README

Ce document explique comment structurer et configurer dynamiquement vos applications et middlewares dans le projet.

---

## 1. Introduction

Ce projet permet de :

- Centraliser la configuration des apps et des middlewares.
- Ajouter ou retirer une app tiers facilement en créant ou supprimant un seul import.
- Garantir une cohérence des noms de variables pour l’automatisation via la fonction `find_value()`.

---

## 2. Ajout d’une app tierce

Pour intégrer une app tierce :

1. **Créer un fichier de configuration**
   - Emplacement suggéré : `config/apps/<nom_app>_config.py`
   - Définir toutes les variables spécifiques à cette app (apps, middlewares, context processors, etc.).

2. **Importer la configuration**
   - Dans le fichier `appinstall.py`, ajoutez :
     ```python
     from config.apps.<nom_app>_config import *
     ```

3. **Nommer vos variables**
   - Suivez les conventions décrites ci-dessous pour que `find_value()` les détecte automatiquement.

---

## 3. Définition des listes d’apps

Chaque app installable doit déclarer une variable de type `list` dont le nom se termine par `_APP_LIST`.

### Exemple :
```python
# Dans config/apps/monapp_config.py
MONAPP_APP_LIST = [
    'django.contrib.admin',
    'rest_framework',
    'monapp',
]
```

> **Astuce** : utilisez des noms explicites (`NOMDEAPP_APP_LIST`) pour éviter les collisions.

---

## 4. Définition des middlewares

Pour chaque ensemble de middlewares, créez une variable `list` se terminant par `_MIDDLEWARE`.

### Exemple :
```python
# Dans config/apps/monapp_config.py
MONAPP_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'monapp.middleware.CustomHeaderMiddleware',
]
```

---

## 5. Intégration dans `appinstall.py`

Utilisez la fonction `find_value()` pour agréger toutes les listes déclarées :

```python
from .utils import find_value

# Importez ici tous vos fichiers de config d'apps
from config.apps.monapp_config import *
# from config.apps.autreapp_config import *

# Récupération automatique des apps et middlewares
INSTALLED_APPS = find_value('_APP_LIST', mode='endswith', variables=globals())
MIDDLEWARE = find_value('_MIDDLEWARE', mode='endswith', variables=globals())
MIDDLEWARE = find_value('_CONTEXT_PROCESSOR', mode='endswith', variables=globals())
```

- `mode='endswith'` permet de filtrer toutes les variables dont le nom se termine par le motif.
- `variables=globals()` passe le namespace courant à la fonction.

---

## 6. Personnalisation et maintenance

- **Ajouter une app** :
  1. Créer son fichier `<nom_app>_config.py`.
  2. Définir `_APP_LIST`, `_CONTEXT_PROCESSOR` et/ou `_MIDDLEWARE`.
  3. Importer dans `appinstall.py`.

- **Retirer une app** :
  1. Supprimer l’import de son fichier de config dans `appinstall.py`.
  2. Aucun autre changement n’est nécessaire.

- **Conventions de nommage** :
  - Tous les noms finissant par `_APP_LIST` ou `_MIDDLEWARE` seront détectés.
  - Assurez-vous d’utiliser des noms uniques et explicites pour chaque app.

---

## 7. FAQ

- **Q** : Que se passe-t-il si deux apps ont la même variable `_APP_LIST` ?
  - **R** : Les listes seront concaténées, dans l’ordre des imports.

- **Q** : Puis-je utiliser un autre mapping que `globals()` ?
  - **R** : Oui, il suffit de passer votre propre `dict` à `variables` dans `find_value()`.

---

*Fin du README*

