# Portfolio Next.js

Bienvenue dans la documentation technique du projet **Portfolio Next.js**.

Ce projet démontre la mise en place d'une chaîne DevOps complète, depuis le dépôt du code source jusqu'au déploiement d'une application web sur un serveur Ubuntu.

## Informations générales

| Élément | Valeur |
|---|---|
| Application | Portfolio Next.js |
| Framework | Next.js |
| Langage | TypeScript |
| Code source | [GitHub](https://github.com/ferid-saad/portfolio-nextjs) |
| CI/CD | Jenkins |
| Conteneurisation | Docker |
| Registre d'images | Docker Hub |
| Plateforme développeur | Backstage |

## Accès à l'application

- **Application déployée :** [Portfolio Next.js](http://192.168.50.88:3001)
- **Dépôt GitHub :** [ferid-saad/portfolio-nextjs](https://github.com/ferid-saad/portfolio-nextjs)
- **Jenkins :** [portfolio-nextjs-ci](http://192.168.50.88:8080/job/portfolio-nextjs-ci/)

## Objectifs du projet

- Automatiser la construction de l'application.
- Vérifier le fonctionnement de l'application avant publication.
- Construire une image Docker.
- Publier l'image sur Docker Hub.
- Déployer automatiquement l'application sur Ubuntu.
- Centraliser les informations techniques dans Backstage.

## Chaîne CI/CD

Le pipeline Jenkins réalise les principales opérations suivantes :

1. Récupération du code depuis GitHub.
2. Installation des dépendances avec npm.
3. Construction de l'application Next.js.
4. Construction et vérification de l'image Docker.
5. Tests de fonctionnement.
6. Publication de l'image sur Docker Hub.
7. Vérifications avant déploiement.
8. Déploiement du conteneur sur Ubuntu.
9. Vérification de l'application déployée.

## Déploiement

L'application est exécutée dans un conteneur Docker nommé :

`portfolio-nextjs-prod`

La correspondance des ports est :

- Port Ubuntu : `3001`
- Port du conteneur : `3000`

L'image Docker est publiée dans le dépôt :

`feridsaad/portfolio-nextjs`

## Intégration Backstage

Backstage centralise les informations du composant :

- Présentation et propriétaire.
- Dépôt GitHub.
- Accès à l'application déployée.
- Historique et statut des builds Jenkins.
- Documentation technique avec TechDocs.

## Documentation complémentaire

- [Architecture technique](architecture.md)
- [Pipeline CI/CD](cicd-pipeline.md)
- [Procédure de déploiement](deployment.md)
