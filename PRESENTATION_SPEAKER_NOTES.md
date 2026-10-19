# Guide Complet de Présentation Orale : Platform Engineering & Backstage
**Support associé :** `Platform_Engineering_Ferid_Saad.pptx` (16 slides)  
**Durée totale :** 15 à 20 minutes (dont 4 minutes de démonstration live)

---

## ⏱️ Répartition du Temps

| Section | Slides | Durée cible |
| :--- | :--- | :--- |
| **1. Introduction & Contexte** | Slides 1 à 3 | 3 min |
| **2. Le Concept du Platform Engineering** | Slides 4 et 5 | 3 min |
| **3. DevOps vs Platform Engineering** | Slide 6 | 2 min |
| **4. Architecture & Comparatif Marché** | Slides 7 à 9 | 3 min |
| **5. Focus Backstage & Démonstration Live** | Slides 10 à 12 | 4 min |
| **6. Analyse Critique (Gains, Limites, Risques)** | Slides 13 et 14 | 2 min 30 s |
| **7. Perspectives Futures (IA & CNCF) & Conclusion** | Slides 15 et 16 | 2 min |
| **8. Session Questions / Réponses (Q&A)** | Fin de séance | 3 à 5 min |

---

## 🎙️ Script Détaillé Diapositive par Diapositive

### Slide 1 : Titre & Introduction (00:00 - 01:00)
> *"Bonjour à tous. Aujourd'hui, je vais vous présenter le **Platform Engineering**, considéré comme l'évolution majeure du DevOps pour répondre aux défis d'échelle des architectures Cloud Native modernes.*
> 
> *Nous verrons pourquoi le paradigme DevOps historique a atteint ses limites cognitives, ce qu'apporte une plateforme interne de développement (IDP), comment se positionnent les différents acteurs du marché, puis nous réaliserons une démonstration concrète de l'outil open source leader : **Spotify Backstage**."*

---

### Slide 2 : Sommaire & Agenda (01:00 - 01:45)
> *"Pour aborder ce sujet de manière structurée en 15 à 20 minutes, notre soutenance se déroulera en six temps :*
> 1. *Le diagnostic des difficultés du DevOps à l'échelle.*
> 2. *La définition formelle du Platform Engineering et de ses concepts fondamentaux.*
> 3. *La comparaison méthodique entre DevOps traditionnel et Platform Engineering.*
> 4. *Le panorama comparatif des solutions du marché (Backstage, Port, Humanitec, AWS/Azure).*
> 5. *Une démonstration pratique de 4 minutes de Spotify Backstage.*
> 6. *Et enfin, une analyse critique des bénéfices, des pièges à éviter et de l'impact de l'IA à l'horizon 2026."*

---

### Slide 3 : La Problématique DevOps : Le Mur de la Complexité (01:45 - 03:30)
> *"Pour comprendre l'émergence du Platform Engineering, il faut regarder la réalité du terrain DevOps.*
> 
> *Le DevOps a apporté des progrès formidables grâce au célèbre mot d'ordre d'Amazon : 'You build it, you run it' (si tu le construis, tu le gères en production).*
> 
> *Mais avec l'avènement du Cloud Native, la boîte à outils d'un développeur a explosé : Kubernetes, Terraform, Helm, Istio, Docker, ArgoCD, Prometheus, Vault, SonarQube... Aujourd'hui, on demande à un développeur web ou backend de maîtriser l'état de l'art du réseau, de la sécurité et de l'orchestration de conteneurs.*
> 
> *Le résultat ? Une **surcharge cognitive critique**. Les ingénieurs passent jusqu'à 40% de leur temps sur des tâches d'infrastructure et de configuration YAML au lieu de coder de la valeur métier.*
> 
> *Pire encore, dans beaucoup d'entreprises, le DevOps a régressé vers un modèle de 'tickets Ops déguisés' : les devs attendent des jours pour obtenir un cluster ou une base de données, créant du Shadow IT et des configurations hétérogènes impossibles à maintenir."*

---

### Slide 4 : Qu'est-ce que le Platform Engineering ? (03:30 - 05:00)
> *"C'est précisément pour briser cette surcharge cognitive qu'est né le **Platform Engineering**.*
> 
> *Gartner et la CNCF le définissent comme une discipline d'ingénierie dédiée à la conception et à l'exploitation de plateformes internes de développement, appelées **IDP (Internal Developer Platforms)**.*
> 
> *Deux principes révolutionnaires sous-tendent cette discipline :*
> 1. *Le concept de **Platform as a Product** : La plateforme n'est pas un script d'infra vite bricolé, c'est un véritable produit logiciel interne. L'équipe 'Platform Team' a un Product Manager, et ses clients sont les développeurs de l'entreprise.*
> 2. *L'adoption volontaire : On ne force pas les développeurs à utiliser la plateforme par décret ; on leur propose une expérience si fluide et rapide qu'ils l'adoptent naturellement."*

---

### Slide 5 : Les 4 Piliers du Platform Engineering (05:00 - 06:30)
> *"Le Platform Engineering repose sur quatre piliers d'architecture de valeur :*
> - *Le premier, ce sont les **Golden Paths** (ou Paved Roads) : ce sont des chemins balisés recommandés. Si vous suivez ce chemin, la CI/CD, l'observabilité et la sécurité sont configurées par défaut.*
> - *Le deuxième, c'est le **Libre-Service Automatisé (Self-Service)** : le développeur peut provisionner ses ressources de manière autonome via une interface ou une API, sans jamais ouvrir un ticket Jira.*
> - *Le troisième, c'est la **DevEx (Expérience Développeur)** : la satisfaction et la réduction des frictions deviennent des métriques premières.*
> - *Le quatrième, ce sont les **Guardrails (Garde-fous intégrés)** : la conformité et la sécurité sont intégrées dans le code dès le départ, ce qui garantit qu'aucune ressource non sécurisée n'arrive en production."*

---

### Slide 6 : DevOps vs Platform Engineering (06:30 - 08:30)
> *"Ce tableau synthétise la rupture de paradigme entre DevOps classique et Platform Engineering :*
> 
> - *Sur la philosophie : Le DevOps est une culture collaborative transversale. Le Platform Engineering est une discipline d'ingénierie produit.*
> - *Sur la charge cognitive : Le DevOps historique imposait au développeur de tout savoir de l'infrastructure. Le Platform Engineering lui fournit des abstractions adaptées à son métier.*
> - *Sur l'organisation : Au lieu d'avoir un ingénieur DevOps isolé dans chaque équipe qui réinvente la roue, une **Platform Team centralisée** fournit des composants réutilisables pour l'ensemble des équipes.*
> - *Sur les métriques : Au-delà du simple 'uptime' des serveurs, on mesure l'efficacité d'ingénierie : le Lead Time for Changes, la fréquence de déploiement et le temps d'onboarding d'un nouvel arrivant.*
> 
> *Il est crucial de retenir que **le Platform Engineering ne tue pas le DevOps : il l'outille pour le rendre viable à grande échelle**."*

---

### Slide 7 : Architecture Technique d'une IDP (08:30 - 09:30)
> *"Une plateforme interne de développement s'organise en cinq couches superposées :*
> 1. *Le plan de contrôle développeur (portail web comme Backstage, CLI interne).*
> 2. *Le plan d'intégration continue (GitHub Actions, GitLab CI, ArgoCD).*
> 3. *Le plan d'orchestration (génération dynamique de manifestes, Score spec, Humanitec).*
> 4. *Le plan d'infrastructure (les clusters Kubernetes et le cloud AWS/Azure/GCP).*
> 5. *La couche transverse de gouvernance, secrets (Vault) et observabilité (OpenTelemetry, Datadog)."*

---

### Slides 8 & 9 : Panorama & Benchmark des Outils du Marché (09:30 - 11:30)
> *"Sur le marché actuel, nous identifions quatre grandes familles de solutions :*
> 
> 1. *Les Portails Développeurs Open Source : **Spotify Backstage** (projet CNCF). C'est le standard de facto du marché. Ses forces sont son écosystème de plugins et sa liberté totale ; sa contrepartie est qu'il nécessite du code TypeScript/React pour être personnalisé.*
> 2. *Les Portails SaaS No-Code : **Port (getport.io)**. Très élégant, entièrement personnalisable sans coder, mais propriétaire et payant.*
> 3. *Les Orchestrateurs purs : **Humanitec**. Il ne se focalise pas sur le portail visuel, mais sur la résolution dynamique des dépendances d'infrastructure via la spécification open source Score.*
> 4. *Les solutions des Hyperscalers : **AWS Proton** et **Azure Developer Hub**. Très performants si vous êtes à 100% dans leur écosystème, mais créant un verrouillage propriétaire fort (vendor lock-in).*
> 
> *Dans la matrice de la slide 9, nous constatons que pour une entreprise cherchant la souveraineté, l'extensibilité et le standard industriel, **Backstage** est le choix de référence."*

---

### Slide 10 : Focus sur Spotify Backstage (11:30 - 12:30)
> *"Pourquoi Backstage ? Créé en interne chez Spotify pour maîtriser le chaos de milliers de microservices, il a été donné à la CNCF et est aujourd'hui utilisé par plus de 2 000 grandes organisations mondiales.*
> 
> *Backstage s'articule autour de trois modules majeurs que nous allons vous démontrer en direct :*
> - *Le **Software Catalog** pour cartographier l'écosystème,*
> - *Le **Scaffolder** pour instancier des Golden Paths,*
> - *Et **TechDocs** pour la documentation technique centralisée."*

---

### Slides 11 & 12 : Démonstration Live (12:30 - 16:30)
*(Basculez sur la fenêtre de démonstration du navigateur `http://localhost:3000` et suivez le script `DEMO_SCRIPT_BACKSTAGE.md`)*.

---

### Slide 13 : Avantages & Gains Mesurés (16:30 - 17:45)
> *(Retour à la présentation)*
> *"Comme nous venons de le voir en direct, les bénéfices d'une IDP sont mesurables et concrets :*
> 
> - *Sur les métriques DORA : Le **Lead Time for Changes** est réduit de 60 à 80%. Créer et déployer un service prend quelques minutes au lieu de plusieurs jours.*
> - *Le **MTTR (Mean Time To Recovery)** chute drastiquement, car en cas d'incident, n'importe quel ingénieur d'astreinte identifie immédiatement le propriétaire du service et ses dépendances.*
> - *Sur le plan humain : L'**onboarding** d'un nouvel ingénieur passe de 3 semaines de lecture de documentation éparse à moins d'une demi-journée pour effectuer son premier commit en production."*

---

### Slide 14 : Limites, Risques et Facteurs d'Échec (17:45 - 19:00)
> *"Cependant, le Platform Engineering comporte des pièges réels qu'il faut savoir anticiper :*
> 
> 1. *Le syndrome 'Construisez-le et ils viendront' : Imposer une plateforme aux développeurs sans les consulter mène au rejet. C'est pourquoi la posture de Product Management est indispensable.*
> 2. *L'effet 'Usine à Gaz' : Créer des abstractions trop rigides qui enferment les développeurs ('Paved road, not a paved prison').*
> 3. *Le coût de maintenance : Faire vivre une instance Backstage nécessite de vraies compétences logicielles dédiées dans la Platform Team."*

---

### Slide 15 : Perspectives d'Avenir & Intégration de l'IA (19:00 - 20:00)
> *"D'ici 2026, deux grandes tendances transforment les IDP :*
> - *L'irruption de l'**IA Générative** : La création de microservices ne se fera plus seulement par formulaire, mais par invite en langage naturel via des assistants d'architecture connectés au catalogue.*
> - *Les **plateformes auto-réparatrices** : Des agents d'IA capables de détecter une CVE dans le catalogue et de proposer un Pull Request automatique pour corriger les versions vulnérables.*
> - *La consolidation des standards CNCF avec des projets comme Score et OpenTelemetry."*

---

### Slide 16 : Conclusion & Session Q&A (20:00 - Fin)
> *"En conclusion : Le Platform Engineering est la réponse industrielle à la complexité Cloud Native. Il ne supprime pas le DevOps, il le rend viable en offrant aux développeurs des chemins balisés et du libre-service.*
> 
> *Je vous remercie pour votre attention et je suis désormais à votre disposition pour répondre à toutes vos questions."*

---

## 💡 Réponses aux Questions Probables du Jury (Q&A)

### Q1 : "Quelle est la différence fondamentale entre Backstage et un outil comme GitLab ou GitHub Enterprise ?"
**Réponse :**  
> *"GitLab et GitHub sont d'excellentes forges logicielles et moteurs CI/CD. Mais ils n'ont pas de catalogue universel des services intégrant la notion de système, de domaine, de dépendance entre APIs et d'ownership transversal. Backstage ne remplace pas GitHub ou GitLab : il s'intègre au-dessus d'eux via des plugins pour offrir une vue consolidée, agrégeant aussi Kubernetes, SonarQube, ArgoCD et les outils de monitoring dans un portail unique."*

### Q2 : "Est-ce que le Platform Engineering convient aux petites équipes ou startups ?"
**Réponse :**  
> *"Non, pas forcément. Pour une équipe de 10 développeurs sur une seule application monolithique, mettre en place une Platform Team et déployer Backstage représente une sur-ingénierie inutile (over-engineering). Le Platform Engineering apporte sa pleine rentabilité à partir du moment où l'organisation dépasse 40 à 50 ingénieurs, avec plusieurs squads autonomes et des dizaines de microservices."*

### Q3 : "Pourquoi Backstage demande-t-il autant de maintenance par rapport à une solution SaaS comme Port ?"
**Réponse :**  
> *"Backstage n'est pas un logiciel tout fait prêt à l'emploi (off-the-shelf), c'est un framework de développement en TypeScript et React. Chaque plugin doit être compilé, testé et mis à jour lors des montées de version. Port, au contraire, est une solution SaaS managée où le modèle de données est entièrement configurable en JSON/UI sans écrire de code frontend. Le compromis se situe entre la souveraineté open source totale (Backstage) et la rapidité de mise en œuvre sans maintenance infra (Port)."*
