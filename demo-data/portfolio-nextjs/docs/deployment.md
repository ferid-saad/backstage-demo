# Procédure de déploiement

## Présentation

L'application Portfolio Next.js est déployée sur une machine virtuelle Ubuntu à l'aide de Docker et Jenkins.

## Informations sur le déploiement

| Élément | Valeur |
|---|---|
| Serveur Ubuntu | 192.168.50.88 |
| Conteneur | portfolio-nextjs-prod |
| Image Docker | feridsaad/portfolio-nextjs |
| Port du serveur | 3001 |
| Port du conteneur | 3000 |
| Pipeline Jenkins | portfolio-nextjs-ci |

## Prérequis

- Serveur Ubuntu opérationnel.
- Docker installé sur Ubuntu.
- Jenkins accessible.
- Accès au dépôt Docker Hub.
- Pipeline Jenkins configuré.

## Déploiement automatisé

Le déploiement est déclenché par le pipeline Jenkins.

Les principales opérations sont :

1. Vérifier les conditions avant déploiement.
2. Récupérer l'image Docker publiée.
3. Déployer le conteneur portfolio-nextjs-prod.
4. Exposer l'application sur le port 3001.
5. Vérifier que l'application répond correctement.

## Vérification sur Ubuntu

Se connecter au serveur Ubuntu puis vérifier le conteneur.

## Vérification de l'application

Depuis un navigateur, ouvrir :

http://192.168.50.88:3001

L'application doit afficher le portfolio Next.js.

## Retour à une version précédente

Les images publiées sur Docker Hub sont identifiées par leur numéro de build Jenkins.

Exemple : feridsaad/portfolio-nextjs:11

## Suivi et supervision

- Jenkins permet de consulter les exécutions du pipeline.
- Docker permet de vérifier l'état du conteneur.
- Backstage centralise les informations du composant.

## Liens utiles

- [Application déployée](http://192.168.50.88:3001)
- [Jenkins](http://192.168.50.88:8080/job/portfolio-nextjs-ci/)
- [Dépôt GitHub](https://github.com/ferid-saad/portfolio-nextjs)
- [Docker Hub](https://hub.docker.com/r/feridsaad/portfolio-nextjs)
