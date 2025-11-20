# Decisions

## Séparation et efficacité des apps

Chaque app (`Notes` et `Todos`) est conçue comme un domaine autonome :
- **Isolation des responsabilités** : `Notes` gère uniquement les notes, `Todos` gère uniquement les tâches.
- **API propre à chaque app** : chaque app expose ses endpoints via son propre ViewSet et Router.
- **Indépendance fonctionnelle** : aucune logique métier de `Todos` n’est directement intégrée dans `Notes` et vice-versa.

**Couplage minimal** : la seule dépendance est la ForeignKey dans `Todo` vers `Note`, nécessaire pour répondre à la spécification.

>Pour comparaison, j’ai exploré une solution de **découplage complet** via un mécanisme de liens génériques, présenté dans ce dépôt :
https://github.com/manuo1/django-fully-decoupled-apps-sample.
>
>Dans cette architecture :
>- `Todo` et `Note` n’ont **aucune ForeignKey directe**.
>- Les liens sont gérés par un modèle `Link` générique, permettant à n’importe quelle app d’être supprimée sans casser ni modifier les autres.
>
>**Inconvénients du découplage complet par rapport à la solution choisie ici** :
>- Les requêtes pour récupérer les objets liés sont **moins performantes** que des FKs classiques.
>- Il faut **plus de code** pour gérer les liens et rendre l’accès ergonomique.
>- Moins de **contraintes au niveau base de données**, donc plus de garde-fous nécessaires.
>- Complexité générale accrue pour un projet simple comme ce test.


La solution choisie ici offre un **compromis efficace** : séparation claire, app indépendantes, mais avec un couplage minimal simple et performant.



## Gestion des interdépendances

Les interdépendances entre `Todos` et `Notes` sont limitées au strict nécessaire pour répondre au cahier des charges.
- La seule dépendance est la ForeignKey dans `Todo` vers `Note`.
- Cette relation est **unidirectionnelle** : `Todo` connaît sa `Note`, mais `Note` n’a pas besoin de connaître toutes les todos pour fonctionner.
- La ForeignKey est **nullable**, ce qui signifie qu’une todo peut exister sans être liée à une note.
- L’accès aux todos depuis une note est possible via le `related_name="todos"`, mais cela reste **passif** et n’impose aucune logique métier complexe.

Cette approche permet :
- De maintenir les apps **indépendantes** : modification dans `Notes` ou `Todos` n’impacte pas l’autre app en dehors de la relation FK.
- De réduire le risque de couplage fort ou de dépendances circulaires.
- De conserver un **code simple et lisible** tout en respectant la spécification : une todo peut référencer ou non une note, et une note peut avoir plusieurs ou aucune todo.




## Pourquoi telle structure ?

La structure choisie repose sur deux apps distinctes (`Todos` et `Notes`), chacune avec :
- ses modèles,
- ses serializers,
- ses ViewSets et routes propres.

Les raisons principales de ce choix sont :
- **Séparation claire des responsabilités** : chaque app gère uniquement son domaine, ce qui facilite la lecture et la maintenance.
- **Modularité** : il est possible de modifier, remplacer ou supprimer une app sans impacter l’autre (hors FK existante).
- **Alignement avec les bonnes pratiques Django/DRF** : apps séparées + ViewSets/routers pour un REST complet et cohérent.
- **Facilité des tests** : chaque app peut être testée indépendamment avec pytest.
- **Simplicité pour un projet time-boxé** : cette structure répond aux besoins du test sans sur-ingénierie.

Cette architecture offre un bon compromis entre **clarté**, **maintenabilité** et **rapidité de développement**, tout en restant flexible si d’autres apps ou relations étaient ajoutées par la suite.

## Pourquoi tel pattern ?

Pour cette API REST, les patterns choisis ont été :
- **ModelViewSet + DefaultRouter** : permet de générer rapidement tous les endpoints CRUD pour chaque ressource, tout en respectant les conventions REST de Django REST Framework.
- **ModelSerializer** : simplifie la sérialisation/désérialisation des modèles, réduit le code boilerplate et garantit la cohérence des champs.
- **Apps séparées** : correspond au pattern de séparation par domaine, favorise la modularité et la maintenance.
- **ForeignKey unidirectionnelle** : simplifie la relation entre `Todo` et `Note` tout en minimisant le couplage.


## Trade-offs
Pour ce projet, plusieurs compromis ont été nécessaires :

- **Simplicité vs flexibilité** :
  La relation `Todo → Note` est une ForeignKey simple, ce qui limite le couplage et la complexité, mais empêche des scénarios très dynamiques de type “une todo peut être liée à plusieurs notes ou à d’autres entités” sans modifier le modèle.

- **Performance vs découplage complet** :
  J’ai choisi un couplage minimal (FK) plutôt qu’une architecture totalement découplée via un modèle générique (`Link`).
  Avantage : performant et simple à utiliser.
  Inconvénient : moins modulable si le projet devait évoluer vers une architecture très flexible.

- **Fonctionnalité vs temps limité** :
  Les endpoints sont CRUD “simples” sans logique métier avancée ni règles de validation complexes.
  Cela répond au test et permet de rester dans un temps de développement réduit, mais pour un projet réel, il faudrait ajouter plus de règles métier, validations et tests.

- **Décisions techniques vs productivité** :
  Utilisation de ModelViewSet + DefaultRouter et ModelSerializer pour gagner du temps et rester lisible.
  Alternative plus “fine” : APIView ou GenericAPIView, plus flexible mais plus verbeux pour un test court.


