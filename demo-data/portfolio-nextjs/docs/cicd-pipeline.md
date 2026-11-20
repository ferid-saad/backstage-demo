# Pipeline CI/CD Jenkins

## Présentation

Le pipeline CI/CD automatise la construction, la validation, la publication et le déploiement de Portfolio Next.js.

- Serveur Jenkins : http://192.168.50.88:8080
- Job : portfolio-nextjs-ci
- Dépôt source : https://github.com/ferid-saad/portfolio-nextjs
- Branche : main

## Étapes du pipeline

### 1. Checkout

Jenkins récupère le code source depuis le dépôt GitHub.

### 2. Installation des dépendances

Les dépendances Node.js sont installées avec npm ci.

Cette commande utilise le fichier package-lock.json pour assurer une installation reproductible.

### 3. Build Next.js

Jenkins lance la compilation de l'application avec npm run build.

Cette étape permet de détecter les erreurs de compilation.

### 4. Construction de l'image Docker

Docker construit une image de l'application à partir du Dockerfile.

Image utilisée :

feridsaad/portfolio-nextjs

### 5. Vérification de l'image

Le pipeline vérifie que l'image Docker a été correctement construite.

### 6. Smoke test

Un test de fonctionnement vérifie que l'application peut démarrer correctement avant sa publication.

### 7. Publication sur Docker Hub

Jenkins publie l'image dans le registre Docker Hub.

Le numéro du build Jenkins est utilisé comme tag de l'image.

Exemple :

feridsaad/portfolio-nextjs:11

### 8. Vérifications avant déploiement

Le pipeline vérifie les conditions nécessaires avant de déployer la nouvelle version.

### 9. Déploiement

Jenkins déploie l'image sur le serveur Ubuntu dans le conteneur :

portfolio-nextjs-prod

Le port 3001 du serveur est associé au port 3000 du conteneur.

### 10. Vérification finale

Le pipeline vérifie que l'application est accessible après le déploiement.

## Suivi des exécutions

Les builds et leurs résultats sont consultables depuis Jenkins et depuis l'onglet Jenkins du composant Backstage.

[Consulter le job Jenkins](http://192.168.50.88:8080/job/portfolio-nextjs-ci/)

## Résultat attendu

Une nouvelle version de l'application est construite, publiée sur Docker Hub et déployée sur Ubuntu après validation des étapes du pipeline.
