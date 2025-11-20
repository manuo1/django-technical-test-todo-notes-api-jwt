On cherche à mieux comprendre comment tu abordes un projet Django avec des problématiques d'architecture réelles. Pas de piège, pas de questions théoriques : juste du code et une discussion sur tes choix.

## Le projet

On te propose de créer une instance Django avec deux apps exposées uniquement en REST :

### App 1 : Todolist
Une app de gestion de tâches classique. Une todo a au minimum un titre, un statut, et peut référencer une note.

### App 2 : Notes
Une app de prise de notes. Une note peut contenir du texte et peut être liée à plusieurs todos.

### La particularité
Les deux apps communiquent :
- Une todo peut référencer une note
- Une note peut comporter plusieurs todos

## Ce qu'on attend

**Stack :**
- Django + Django REST Framework
- Base de données au choix (SQLite suffit)
- Authentification optionnelle (si tu veux, mais pas obligatoire)

**Livrables :**
- Code source (repo Git ou archive)
- Un README avec les instructions pour lancer le projet
- Les endpoints doivent être fonctionnels (on testera avec Postman/cURL)

**Durée suggérée :** 2-3h max. On ne cherche pas une app production-ready, mais une base solide qui montre comment tu structures ton code.

## Ce qui nous intéresse particulièrement

- Comment assures-tu la meilleure séparation et efficacité entre ces deux apps ?
- Comment gères-tu leurs interdépendances ?
- Pourquoi telle structure ?
- Pourquoi tel pattern ?
- Quels trade-offs as-tu faits ?

C'est un exercice de discussion autant que de code. On veut comprendre ta façon de penser et de résoudre des problèmes réels.

## Questions ?

Si un point n'est pas clair, prends la décision qui te semble la plus cohérente et documente-la. C'est aussi ce qu'on évalue.

Bon code !
