# Architecture technique

## Vue d'ensemble

Le projet Portfolio Next.js utilise une architecture DevOps intégrant GitHub, Jenkins, Docker Hub, Ubuntu et Backstage.

## Composants de l'architecture

### 1. GitHub

Le dépôt GitHub héberge le code source de l'application.

- Dépôt : https://github.com/ferid-saad/portfolio-nextjs
- Branche principale : main

### 2. Jenkins

Jenkins automatise le processus CI/CD.

- Serveur : http://192.168.50.88:8080
- Job : portfolio-nextjs-ci

Il récupère le code, construit l'application, exécute les vérifications et déclenche le déploiement.

### 3. Docker

Docker permet de construire une image reproductible de l'application Next.js.

- Image : feridsaad/portfolio-nextjs
- Conteneur de production : portfolio-nextjs-prod

### 4. Docker Hub

Docker Hub héberge les images publiées par Jenkins.

Le tag de l'image correspond au numéro du build Jenkins.

Exemple : feridsaad/portfolio-nextjs:11

### 5. Serveur Ubuntu

La machine Ubuntu héberge le conteneur de production.

- Adresse IP : 192.168.50.88
- Port exposé : 3001
- Port interne : 3000

### 6. Backstage

Backstage constitue le portail développeur centralisé.

Il fournit :

- Le catalogue des composants.
- Les liens vers GitHub et l'application.
- L'intégration Jenkins.
- La documentation TechDocs.

## Flux de fonctionnement

1. Le développeur publie son code sur GitHub.
2. Jenkins récupère le dépôt.
3. Jenkins construit et vérifie l'application.
4. Docker construit l'image.
5. Jenkins publie l'image sur Docker Hub.
6. Le serveur Ubuntu récupère l'image.
7. Le conteneur de production est démarré et vérifié.
8. Backstage centralise les informations du composant et du pipeline.

## Accès

- [Application](http://192.168.50.88:3001)
- [GitHub](https://github.com/ferid-saad/portfolio-nextjs)
- [Jenkins](http://192.168.50.88:8080/job/portfolio-nextjs-ci/)
