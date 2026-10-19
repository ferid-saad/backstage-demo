# Guide de Démonstration en Direct : Spotify Backstage (3 à 5 minutes)

Ce document détaille le déroulé minute par minute de la démonstration pratique de **Spotify Backstage** pour votre TP. Il vous indique exactement **quoi cliquer**, **quoi montrer** et **quoi dire** devant votre jury ou vos enseignants.

---

## ⏱️ Chronométrage de la Démonstration (Total : ~4 minutes)

| Temps | Étape / Module | Objectif de Démonstration |
| :--- | :--- | :--- |
| **00:00 - 01:00** | **Software Catalog** | Montrer la fin des silos, la cartographie des microservices et l'ownership. |
| **01:00 - 02:30** | **Scaffolder (Golden Path)** | Créer un nouveau microservice en libre-service sans ticket d'infrastructure. |
| **02:30 - 03:30** | **TechDocs & Contrats d'API** | Démontrer la centralisation de la documentation technique et des contrats OpenAPI. |
| **03:30 - 04:00** | **GitOps & catalog-info.yaml** | Expliquer la puissance de la configuration déclarative stockée dans Git. |

---

## 🎬 Déroulé Pas-à-Pas (Scénario "Live Demo")

### 🚀 Lancement préalable
Avant de commencer votre présentation :
1. Double-cliquez sur `start_demo.bat` (ou lancez `python start_demo.py` dans le dossier `backstage-demo`).
2. Votre navigateur s'ouvre sur `http://localhost:3000`.
3. Mettez la fenêtre en plein écran (`F11`).

---

### Étape 1 : Le Software Catalog (Minute 00:00 à 01:00)

**Action à l'écran :**
- Vous êtes sur la page d'accueil **Software Catalog**.
- Tapez `payment` dans la barre de recherche globale, observez le filtrage instantané.
- Cliquez sur les pilules de filtre : `Component (5)`, `API (2)`, `System (1)`.
- Cliquez sur le composant **`payment-gateway-service`**.

**Ce qu'il faut dire à l'oral :**
> *"Nous voici sur l'interface de Spotify Backstage, l'Internal Developer Platform open source leader de la CNCF. Le premier pilier que vous voyez ici est le **Software Catalog**.*
>
> *Dans une organisation DevOps classique avec des dizaines de microservices, l'un des plus grands problèmes est le manque de visibilité : 'Qui possède ce service ? Où sont les logs ? Quelle version d'API est en prod ?'.*
>
> *Grâce au catalogue unifié, chaque composant a une équipe propriétaire clairement identifiée — ici la `team-payments` —, un statut de disponibilité en temps réel (99.98%), et des liens directs vers le code GitHub et le canal Slack d'alerte."*

---

### Étape 2 : Inspection du Service & Observabilité (Minute 01:00 à 01:45)

**Action à l'écran :**
- Sur la page de `payment-gateway-service`, cliquez sur l'onglet **"Pipelines CI/CD"** pour montrer les runs GitHub Actions / ArgoCD.
- Cliquez ensuite sur l'onglet **"Topologie & Dépendances"** pour montrer le graphe relationnel.

**Ce qu'il faut dire à l'oral :**
> *"Dans la vue détaillée du service, le développeur dispose d'un véritable 'Single Pane of Glass'.*
>
> *Ici, dans l'onglet **CI/CD**, le statut des derniers déploiements ArgoCD et GitHub Actions est consolidé sans avoir besoin d'ouvrir trois outils différents.*
>
> *Dans l'onglet **Topologie**, Backstage cartographie automatiquement les flux : nous voyons en un coup d'œil que `checkout-web-frontend` consomme notre service, qui lui-même s'appuie sur le cluster de base de données PostgreSQL."*

---

### Étape 3 : Le Scaffolder & Les Golden Paths (Minute 01:45 à 03:00) — **LE MOMENT CLÉ**

**Action à l'écran :**
1. Cliquez sur **"Create... (Golden Path)"** dans la barre latérale gauche.
2. Montrez la grille des templates (`Node.js`, `Spring Boot`, `React`, `Terraform`).
3. Cliquez sur **"Choisir ce Template"** sur la carte *Microservice Node.js / Express API*.
4. **Étape 1 du Wizard** : Le nom est pré-rempli (`order-fulfillment-service`). Cliquez sur **"Suivant"**.
5. **Étape 2 (Architecture)** : Montrez le choix de base de données (PostgreSQL Aurora) et les gardes-fous de sécurité inclus par défaut (Trivy, SonarQube, OpenTelemetry). Cliquez sur **"Suivant"**.
6. **Étape 3 (Git)** : Montrez le repo cible et le cluster Kubernetes. Cliquez sur le bouton vert **"Lancer la Création Automatisée"**.
7. **Étape 4 (Terminal)** : Laissez l'animation des logs défiler sous les yeux du jury (3-4 secondes) jusqu'à l'apparition de la bannière verte de succès.
8. Cliquez sur **"Voir dans le Software Catalog"** : le service nouvellement créé apparaît instantanément dans le catalogue !

**Ce qu'il faut dire à l'oral :**
> *"Passons maintenant au cœur de la valeur ajoutée du Platform Engineering : le **Scaffolder** et les **Golden Paths** (ou chemins balisés).*
>
> *Dans le modèle DevOps traditionnel, pour démarrer un nouveau microservice, le développeur devait copier-coller un vieux repo, ouvrir un ticket Jira pour demander une base de données, configurer à la main les fichiers Dockerfile et Helm, ce qui prenait 3 à 5 jours.*
>
> *Avec Backstage, la Platform Team a préparé des templates certifiés. Je choisis le template Node.js officiel. Je renseigne le nom du service, mon équipe, et ma base de données PostgreSQL.*
>
> *Quand je clique sur 'Lancer la création', Backstage exécute une chaîne d'automatisation complète : il clone le squelette, génère les pipelines CI/CD sécurisés, crée le dépôt GitHub, provisionne les métriques de monitoring et enregistre automatiquement le nouveau service dans le catalogue.*
>
> *En moins de 5 secondes, le développeur dispose d'un service prêt pour la production, conforme à 100% aux règles de sécurité de l'entreprise, sans aucun ticket intermédiaire !"*

---

### Étape 4 : TechDocs & GitOps (Minute 03:00 à 04:00)

**Action à l'écran :**
- Cliquez sur **"TechDocs"** dans la barre latérale. Montrez la documentation intégrée avec schéma d'architecture et runbooks d'on-call.
- Cliquez sur **"catalog-info.yaml (GitOps)"** dans la barre latérale.

**Ce qu'il faut dire à l'oral :**
> *"Pour terminer, deux fonctionnalités fondamentales :*
>
> *1. **TechDocs** : C'est le principe du 'Docs-as-Code'. La documentation est rédigée en Markdown directement aux côtés du code source dans Git. Backstage la compile automatiquement avec MkDocs, évitant ainsi la documentation obsolète sur Confluence.*
>
> *2. **L'approche GitOps** : Backstage ne possède pas de base de données propriétaire rigide. Toutes les informations que nous venons de voir sont déclarées dans un fichier simple nommé **`catalog-info.yaml`**, stocké dans le dépôt de chaque microservice.*
>
> *Si une équipe met à jour ses métadonnées dans son dépôt Git, Backstage se synchronise automatiquement. C'est l'essence même de l'Infrastructure et du Catalogue as Code.*
>
> *Voilà qui conclut cette démonstration : Backstage transforme le chaos des microservices en une expérience développeur fluide, standardisée et hautement productive."*

---

## 🎯 Conseils pour Réussir votre Soutenance
- **Ne précipitez pas les clics** : Laissez 2 secondes au jury pour apprécier le terminal d'exécution des tâches du Scaffolder.
- **Rappelez le vocabulaire clé** : *IDP*, *Platform as a Product*, *Golden Path*, *Self-Service*, *Cognitive Load*.
- **En cas de question sur la prod** : Rappelez que Backstage s'interface avec Kubernetes via des plugins (plugin ArgoCD, Datadog, GitHub, Kubernetes official plugin).
