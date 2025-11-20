# Architecture

Ce projet contient deux apps Django indépendantes, chacune exposant sa propre API REST :

```
project/
├── config/
│   └── ...
├── notes/
│   ├── models.py
│   ├── api/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── tests/
│   └── ...
├── todos/
│   ├── models.py
│   ├── api/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── tests/
│   └── ...
└── ...
```
> Chaque app est entièrement responsable de ses modèles, de sa couche API et de son routage.


## Modèle de données

### Relation Notes → Todos

Spécifications fonctionnelles :
- “Une todo **peut** référencer une note”
- “Une note **peut** comporter plusieurs todos”

Implémentation :
- Une **Todo** possède une ForeignKey vers une **Note**, ce qui permet de la lier à une note existante.
- Une **Note** peut être associée à plusieurs todos via le `related_name="todos"`, mais n’a pas besoin de connaître les todos pour fonctionner.
- La ForeignKey est **nullable**, donc une todo peut exister sans note.

Ainsi :
- Une Todo peut référencer une ou aucune Note.
- Une Note peut être associée à plusieurs ou aucune Todo.




## Couche REST

Les deux apps utilisent :

- `ModelViewSet` pour un CRUD complet avec un minimum de code
- `DefaultRouter` pour des URLs REST conventionnelles
- `ModelSerializer` pour une sérialisation cohérente et prévisible

Approche choisie pour son efficacité, sa lisibilité et sa conformité aux conventions DRF.



## Authentification

JWT est intégré via `rest_framework_simplejwt`.

Avec :

```py
#settings.py

DEFAULT_AUTHENTICATION_CLASSES = [
    "rest_framework_simplejwt.authentication.JWTAuthentication"
]
DEFAULT_PERMISSION_CLASSES = ["rest_framework.permissions.IsAuthenticated"]
```
> Tous les endpoints nécessitent un token JWT valide.
