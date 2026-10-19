import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation(output_path):
    prs = Presentation()
    # Set 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette - Modern Dark Slate & Vibrant Tech Accents
    BG_DARK = RGBColor(15, 23, 42)        # Slate 900
    CARD_BG = RGBColor(30, 41, 59)        # Slate 800
    CARD_BORDER = RGBColor(51, 65, 85)    # Slate 700
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184)  # Slate 400
    TEXT_BODY = RGBColor(226, 232, 240)   # Slate 200
    
    ACCENT_GREEN = RGBColor(29, 185, 84)  # Spotify Green
    ACCENT_BLUE = RGBColor(56, 189, 248)  # Cyan Blue
    ACCENT_PURPLE = RGBColor(168, 85, 247)# Purple
    ACCENT_AMBER = RGBColor(245, 158, 11) # Amber
    ACCENT_RED = RGBColor(244, 63, 94)    # Rose Red

    def set_slide_background(slide):
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = BG_DARK
        bg_shape.line.fill.background()
        return bg_shape

    def add_header(slide, tag_text, title_text, subtitle_text=None):
        set_slide_background(slide)
        
        # Tag Badge
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_GREEN

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

        # Subtitle if present
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.5), Inches(0.4))
            tf_sub = sub_box.text_frame
            tf_sub.word_wrap = True
            tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle_text
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, items, badge="", badge_color=ACCENT_BLUE):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = CARD_BORDER
        shape.line.width = Pt(1.5)

        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)
        tf.margin_bottom = Inches(0.2)

        # Header with optional badge
        p_head = tf.paragraphs[0]
        if badge:
            p_head.text = f"[{badge}] "
            p_head.font.size = Pt(11)
            p_head.font.bold = True
            p_head.font.color.rgb = badge_color
            
            run_title = p_head.add_run()
            run_title.text = title
            run_title.font.size = Pt(16)
            run_title.font.bold = True
            run_title.font.color.rgb = TEXT_WHITE
        else:
            p_head.text = title
            p_head.font.size = Pt(16)
            p_head.font.bold = True
            p_head.font.color.rgb = TEXT_WHITE

        p_head.space_after = Pt(10)

        for item in items:
            p_item = tf.add_paragraph()
            p_item.text = f"•  {item}"
            p_item.font.size = Pt(12)
            p_item.font.color.rgb = TEXT_BODY
            p_item.space_after = Pt(6)

        return shape

    # ==========================================
    # SLIDE 1 : Titre / Page de Garde
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Accent decorative box
    banner = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.8), Inches(0.15), Inches(3.2))
    banner.fill.solid()
    banner.fill.fore_color.rgb = ACCENT_GREEN
    banner.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.7), Inches(11), Inches(3.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "TRAVAIL PRATIQUE & PRÉSENTATION TECHNIQUE (15-20 MIN)"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_GREEN
    p0.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "Platform Engineering : L'évolution du DevOps"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf1.add_paragraph()
    p2.text = "Comprendre les Internal Developer Platforms (IDP), comparatif du marché et démonstration de Backstage"
    p2.font.size = Pt(18)
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Objectifs : Définition • DevOps vs Platform Eng • Benchmark (Backstage, Port, Humanitec, AWS/Azure) • Live Démo Backstage • Analyse critique"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED

    # Bottom footer card
    f_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(5.5), Inches(10.8), Inches(1.25))
    f_shape.fill.solid()
    f_shape.fill.fore_color.rgb = CARD_BG
    f_shape.line.color.rgb = CARD_BORDER
    ftf = f_shape.text_frame
    ftf.margin_left = Inches(0.3)
    ftf.margin_top = Inches(0.18)
    fp = ftf.paragraphs[0]
    fp.text = "Présenté par : Ferid Saad  |  GitHub : github.com/ferid-saad"
    fp.font.size = Pt(14)
    fp.font.bold = True
    fp.font.color.rgb = ACCENT_GREEN
    
    fp2 = ftf.add_paragraph()
    fp2.text = "Format : 15 à 20 minutes (Présentation théorique 12 min + Démo live Backstage 4 min + Q&A 4 min)"
    fp2.font.size = Pt(12)
    fp2.font.color.rgb = TEXT_WHITE

    fp3 = ftf.add_paragraph()
    fp3.text = "Outil de démonstration : Spotify Backstage (Software Catalog, Scaffolder Golden Path, TechDocs)"
    fp3.font.size = Pt(11)
    fp3.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 2 : Sommaire & Agenda
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "PLAN DE PRÉSENTATION", "Ordre du jour & Structure de la soutenance", "Durée globale : 15 à 20 minutes (dont 3 à 5 minutes de démonstration live)")

    agenda_cards = [
        ("01", "Contexte & Genèse", ["Le constat d'échec du DevOps à grande échelle", "La surcharge cognitive du développeur", "L'illusion du 'You build it, you run it' sans filet"], Inches(0.8), Inches(2.0)),
        ("02", "Le Platform Engineering", ["Définition formelle (CNCF, Gartner)", "Concepts clés : IDP & Platform as a Product", "Paved Roads & Golden Paths en libre-service"], Inches(4.7), Inches(2.0)),
        ("03", "DevOps vs Platform Eng", ["Comparaison point par point", "Rupture de paradigme organisationnel", "Matrice des responsabilités et outillages"], Inches(8.6), Inches(2.0)),
        ("04", "Comparatif du Marché", ["Backstage (Spotify / CNCF)", "Port (SaaS No-Code Developer Portal)", "Humanitec (Orchestrateur IDP)", "AWS Proton & Azure Developer Hub"], Inches(0.8), Inches(4.5)),
        ("05", "Démonstration Backstage", ["Software Catalog & Service Registry", "Scaffolder : Création en Golden Path", "TechDocs & Centralisation API Docs"], Inches(4.7), Inches(4.5)),
        ("06", "Bilan & Perspectives", ["Métriques de succès (DORA, DevEx)", "Pièges, limites & coûts cachés", "Futur : L'IA au service des IDP (2025-2026)"], Inches(8.6), Inches(4.5)),
    ]

    for num, title, items, left, top in agenda_cards:
        add_card(s2, left, top, Inches(3.6), Inches(2.2), title, items, badge=num, badge_color=ACCENT_GREEN)

    # ==========================================
    # SLIDE 3 : La Problématique DevOps
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "CONTEXTE & PROBLÉMATIQUE", "Pourquoi le DevOps traditionnel s'essouffle à l'échelle", "Le principe 'You build it, you run it' a dérivé vers une surcharge cognitive intenable.")

    add_card(s3, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8), 
             "Le 'Mur de la Complexité' Cloud Native", [
                 "Explosion des outils requis : Kubernetes, Helm, Terraform, Istio, Docker, ArgoCD, Prometheus, Vault...",
                 "Le développeur passe 40% de son temps sur des tâches d'infrastructure, de pipeline CI/CD et de configuration YAML.",
                 "Surcharge cognitive critique : Impossible pour chaque développeur de maîtriser l'état de l'art infra, sécurité et réseau.",
                 "Dispersion de l'information : Documentation éclatée (Notion, Confluence, README obsolètes, Swagger orphelins).",
                 "Perte drastique de vélocité métier et frustration grandissante (DevEx dégradée)."
             ], badge="SYMPTÔMES", badge_color=ACCENT_RED)

    add_card(s3, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8), 
             "L'Échec du 'DevOps par Ticket'", [
                 "Goulot d'étranglement 'Ops' reconstitué : Les développeurs attendent des jours pour obtenir un cluster, une base de données ou un secret.",
                 "Prolifération d'architectures 'Snowflake' : Chaque équipe réinvente la roue, configurations non standardisées et failles de sécurité.",
                 "Manque de visibilité globale : 'Qui possède ce microservice en production ? Quelle version d'API est exposée ?'",
                 "Shadow IT et contournements : Pour aller vite, les devs déploient des ressources non conformes aux politiques cloud.",
                 "Constat 2023-2024 de Gartner : 80% des grandes organisations logicielles créent des équipes de plateforme pour résoudre cette impasse."
             ], badge="CONSÉQUENCES", badge_color=ACCENT_AMBER)

    # ==========================================
    # SLIDE 4 : Qu'est-ce que le Platform Engineering ?
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "DÉFINITION & CONCEPTS", "Qu'est-ce que le Platform Engineering et l'IDP ?", "Une discipline émergente visant à concevoir une plateforme interne conçue comme un véritable produit.")

    add_card(s4, Inches(0.8), Inches(2.0), Inches(3.7), Inches(4.8),
             "Définition Fondamentale", [
                 "Discipline d'ingénierie consistant à concevoir et exploiter des plateformes internes de développement (IDP - Internal Developer Platform).",
                 "Mission : Fournir des capacités d'infrastructure, de déploiement et d'outillage en self-service sans friction.",
                 "Objectif n°1 : Réduire drastiquement la charge cognitive des développeurs (DevEx).",
                 "Permettre aux développeurs de se concentrer à 100% sur la valeur métier du code."
             ], badge="CONCEPT", badge_color=ACCENT_BLUE)

    add_card(s4, Inches(4.8), Inches(2.0), Inches(3.7), Inches(4.8),
             "Platform as a Product", [
                 "La plateforme n'est pas un projet d'infrastructure ponctuel, mais un PRODUIT vivant.",
                 "Les développeurs sont les CLIENTS internes : leurs retours guident la feuille de route.",
                 "Présence d'un Product Manager (Platform PM) dédié qui analyse l'usage, la friction et les besoins.",
                 "Adoption volontaire : La plateforme doit être si agréable et efficace que les devs la choisissent naturellement ('Paved Road')."
             ], badge="PARADIGME", badge_color=ACCENT_PURPLE)

    add_card(s4, Inches(8.8), Inches(2.0), Inches(3.7), Inches(4.8),
             "L'IDP (Internal Developer Platform)", [
                 "Couche d'abstraction unifiée regroupant l'outillage, les environnements et les données techniques de l'entreprise.",
                 "Portail unique (Single Pane of Glass) centralisant le catalogue des services, les APIs et la documentation.",
                 "Moteurs de templates (Scaffolder) générant en 1 clic un microservice prêt pour la production (CI/CD, secrets, tests, monitoring inclus)."
             ], badge="COMPOSANT", badge_color=ACCENT_GREEN)

    # ==========================================
    # SLIDE 5 : Les 4 Piliers
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "ARCHITECTURE DE VALEUR", "Les 4 Piliers du Platform Engineering", "Comment la plateforme transforme concrètement le quotidien des équipes de développement.")

    pillars = [
        ("Golden Paths / Paved Roads", [
            "Chemins balisés recommandés par l'ingénierie.",
            "Fournit des modèles pré-configurés respectant sécurité, observabilité et conformité par défaut.",
            "Liberté dans un cadre : Les devs restent autonomes, mais le chemin le plus facile est le plus sûr."
        ], "PILIER 1", ACCENT_GREEN, Inches(0.8), Inches(2.0)),
        ("Libre-Service Automatisé (Self-Service)", [
            "Élimination totale des tickets Jira pour provisionner des ressources.",
            "Création instantanée d'environnements éphémères, bases de données, domaines DNS via API ou UI.",
            "Politiques de gouvernance ('Policy as Code') vérifiées automatiquement en arrière-plan."
        ], "PILIER 2", ACCENT_BLUE, Inches(6.8), Inches(2.0)),
        ("Expérience Développeur (DevEx)", [
            "Mesure active de la satisfaction et de la fluidité du travail d'ingénierie.",
            "Réduction du temps d'attente, élimination des tâches répétitives manuelles (Toil).",
            "Onboarding d'un nouvel ingénieur réduit de 3 semaines à moins de 2 heures."
        ], "PILIER 3", ACCENT_PURPLE, Inches(0.8), Inches(4.5)),
        ("Gouvernance & Sécurité Intégrées (Guardrails)", [
            "La conformité (SOC2, RGPD, ISO) et la sécurité (SAST, SBOM) sont 'baked-in' dans les pipelines.",
            "Mises à jour centralisées : Si une CVE critique apparaît sur une librairie de base, mise à jour orchestrée.",
            "FinOps & Audit intégrés : Visibilité des coûts cloud par équipe et par service."
        ], "PILIER 4", ACCENT_AMBER, Inches(6.8), Inches(4.5))
    ]

    for title, items, badge, color, left, top in pillars:
        add_card(s5, left, top, Inches(5.6), Inches(2.2), title, items, badge=badge, badge_color=color)

    # ==========================================
    # SLIDE 6 : DevOps vs Platform Engineering (Tableau)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "COMPARAISON DÉTAILLÉE", "DevOps traditionnel vs Platform Engineering", "Le Platform Engineering ne remplace pas DevOps : il l'outille et le rend viable à grande échelle.")

    # Create comparison table
    rows = 6
    cols = 3
    t_shape = s6.shapes.add_table(rows, cols, Inches(0.8), Inches(1.9), Inches(11.7), Inches(4.8))
    table = t_shape.table
    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(4.6)
    table.columns[2].width = Inches(4.6)

    table_data = [
        ("DIMENSION", "DEVOPS TRADITIONNEL", "PLATFORM ENGINEERING"),
        ("Philosophie & Posture", "Culture & collaboration transversale. 'You build it, you run it' (le dev gère tout le cycle de vie).", "Discipline d'ingénierie produit. 'Platform as a Product' avec clients internes et SLA."),
        ("Charge Cognitive", "TRÈS FORTE : Le dev doit maîtriser Terraform, K8s, Docker, Helm, IAM, CI/CD, Alerting.", "ALLÉGÉE : Le dev interagit avec des abstractions adaptées à son métier via des Golden Paths."),
        ("Mode d'Interaction", "Tickets Ops ou ingénieurs DevOps disséminés dans les squads (hétérogénéité des pratiques).", "Portail Self-Service unifié (IDP) ou API / CLI interne sans intervention humaine."),
        ("Rôle des Opérations", "Administrateurs de serveurs / pompiers réactifs aux pannes et demandes d'infrastructure.", "Platform Engineers créant des produits logiciels internes réutilisables et automatisés."),
        ("Métriques de Succès", "Disponibilité de l'infra (uptime 99.9%), temps de résolution des incidents techniques.", "DevEx, DORA metrics (Lead Time, Deployment Frequency), temps d'onboarding, adoption de la plateforme.")
    ]

    for r_idx, row in enumerate(table_data):
        for c_idx, cell_value in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = cell_value
            cell.fill.solid()
            if r_idx == 0:
                cell.fill.fore_color.rgb = CARD_BORDER
                p = cell.text_frame.paragraphs[0]
                p.font.bold = True
                p.font.size = Pt(13)
                p.font.color.rgb = ACCENT_GREEN if c_idx == 2 else (ACCENT_BLUE if c_idx == 1 else TEXT_WHITE)
            else:
                cell.fill.fore_color.rgb = CARD_BG
                p = cell.text_frame.paragraphs[0]
                p.font.size = Pt(11)
                p.font.color.rgb = TEXT_WHITE if c_idx == 0 else TEXT_BODY

    # ==========================================
    # SLIDE 7 : Architecture d'une IDP
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "ARCHITECTURE TECHNIQUE", "Les 5 Couches d'une Internal Developer Platform", "Comment s'organise l'écosystème technologique d'une IDP moderne.")

    layers = [
        ("1. Developer Control Plane", ["Portail Web (Backstage, Port), CLI interne, extensions IDE.", "Catalogue logiciel unifié, Scaffolder de templates, TechDocs."], Inches(0.8), ACCENT_GREEN),
        ("2. Integration & Delivery Plane", ["Pipelines CI/CD (GitHub Actions, GitLab CI, Jenkins).", "Moteurs GitOps (ArgoCD, FluxCD), Registres d'artefacts (OCI/Docker)."], Inches(3.2), ACCENT_BLUE),
        ("3. Resource Orchestration Plane", ["Orchestrateur de charges (Humanitec, Terraform Cloud, Crossplane).", "Génération dynamique de manifestes d'infrastructure."], Inches(5.6), ACCENT_PURPLE),
        ("4. Infrastructure Plane", ["Clusters Kubernetes (EKS, GKE, AKS, On-premise).", "Bases de données managées (RDS, Cloud SQL), Réseau, Stockage Cloud."], Inches(8.0), ACCENT_AMBER),
        ("5. Security, Governance & Observability", ["Politiques Open Policy Agent (OPA/Kyverno), Gestion des secrets (Vault).", "Métriques & Traces (Datadog, OpenTelemetry, Prometheus, Grafana)."], Inches(10.4), ACCENT_RED),
    ]

    for title, items, left, color in layers:
        shape = slide_card = add_card(s7, left, Inches(2.0), Inches(2.2), Inches(4.8), title, items, badge="PLAN", badge_color=color)

    # ==========================================
    # SLIDE 8 : Comparatif des Outils du Marché
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "BENCHMARK DES SOLUTIONS", "Panorama des Outils de Platform Engineering", "Analyse des acteurs majeurs : portails développeurs, orchestrateurs et solutions cloud hyperscalers.")

    tools = [
        ("Spotify Backstage", [
            "Origine : Open Source créé par Spotify, projet CNCF Incubation.",
            "Rôle : Portail développeur (Developer Portal) & Software Catalog.",
            "Forces : Écosystème gigantesque de plugins, adoption massive mondiale, flexibilité totale du code.",
            "Faiblesses : Nécessite des compétences React/TypeScript pour le maintenir, pas d'orchestrateur d'infra out-of-the-box."
        ], "OPEN SOURCE", ACCENT_GREEN, Inches(0.8), Inches(2.0)),
        ("Port (getport.io)", [
            "Origine : Pure-player SaaS fondé en 2021.",
            "Rôle : Developer Portal No-Code / Low-Code nouvelle génération.",
            "Forces : Modèle de données totalement personnalisable sans coder, intégrations API instantanées, UI très moderne.",
            "Faiblesses : Solution propriétaire payante, dépendance à un SaaS externe."
        ], "SAAS PORTAL", ACCENT_BLUE, Inches(6.8), Inches(2.0)),
        ("Humanitec", [
            "Origine : Pionnier de l'appellation Platform Engineering.",
            "Rôle : Orchestrateur de plateforme (Platform Orchestrator - Score spec).",
            "Forces : Résolution dynamique des dépendances d'infrastructure, gestion automatique des environnements de dev.",
            "Faiblesses : Pas un portail visuel au départ (se couple souvent avec Backstage ou Port), courbe d'apprentissage."
        ], "ORCHESTRATEUR", ACCENT_PURPLE, Inches(0.8), Inches(4.5)),
        ("AWS Proton & Azure Dev Hub", [
            "Origine : Hyperscalers Cloud (Amazon Web Services / Microsoft).",
            "Rôle : Provisionnement standardisé de microservices et gestion de templates d'environnements.",
            "Forces : Intégration native dans les écosystèmes AWS (ECS/EKS/Lambda) ou Azure (App Services/AKS).",
            "Faiblesses : Fort verrouillage propriétaire (Vendor Lock-in), inadapté au multi-cloud."
        ], "HYPERSCALERS", ACCENT_AMBER, Inches(6.8), Inches(4.5)),
    ]

    for title, items, badge, color, left, top in tools:
        add_card(s8, left, top, Inches(5.6), Inches(2.25), title, items, badge=badge, badge_color=color)

    # ==========================================
    # SLIDE 9 : Matrice Comparative Multicritères
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "SYNTHÈSE COMPARATIVE", "Matrice d'Évaluation des Solutions du Marché", "Comparaison synthétique pour guider le choix d'architecture d'une entreprise.")

    t9_shape = s9.shapes.add_table(6, 6, Inches(0.8), Inches(1.9), Inches(11.7), Inches(4.8))
    t9 = t9_shape.table
    t9.columns[0].width = Inches(2.2)
    t9.columns[1].width = Inches(1.9)
    t9.columns[2].width = Inches(1.9)
    t9.columns[3].width = Inches(1.9)
    t9.columns[4].width = Inches(1.9)
    t9.columns[5].width = Inches(1.9)

    matrix_data = [
        ("CRITÈRE", "BACKSTAGE", "PORT", "HUMANITEC", "AWS PROTON", "AZURE DEV HUB"),
        ("Type d'outil", "Portail Dev (Code)", "Portail Dev (No-Code)", "Orchestrateur Infra", "Service Manager", "Service Manager"),
        ("Modèle de Licence", "Open Source (Apache)", "SaaS Propriétaire", "SaaS / On-prem", "Paiement à l'usage", "Paiement à l'usage"),
        ("Catalogue Logiciel", "Excellent (Core)", "Excellent (Graph)", "Basique (via API)", "Moyen (Services)", "Moyen (Templates)"),
        ("Orchestration Infra", "Nécessite plugins", "Via Webhooks", "Native & Puissante", "CloudFormation/Terraform", "ARM / Bicep / Terraform"),
        ("Effort de Maintenance", "Élevé (Full-stack)", "Faible (No-Code)", "Moyen", "Moyen", "Moyen")
    ]

    for r_idx, row in enumerate(matrix_data):
        for c_idx, cell_value in enumerate(row):
            cell = t9.cell(r_idx, c_idx)
            cell.text = cell_value
            cell.fill.solid()
            if r_idx == 0:
                cell.fill.fore_color.rgb = CARD_BORDER
                p = cell.text_frame.paragraphs[0]
                p.font.bold = True
                p.font.size = Pt(12)
                p.font.color.rgb = ACCENT_GREEN if c_idx == 1 else TEXT_WHITE
            else:
                cell.fill.fore_color.rgb = CARD_BG
                p = cell.text_frame.paragraphs[0]
                p.font.size = Pt(11)
                p.font.color.rgb = TEXT_WHITE if c_idx == 0 else TEXT_BODY

    # ==========================================
    # SLIDE 10 : Focus Spotify Backstage
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "OUTIL RETENU POUR LA DÉMO", "Spotify Backstage : Le Standard Open Source de la CNCF", "Choisi par plus de 2 000 grandes entreprises (Netflix, Toyota, American Airlines, Epic Games).")

    add_card(s10, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Pourquoi Backstage est devenu le leader ?", [
                 "Genèse : Développé en interne chez Spotify pour surmonter l'hyper-croissance et le chaos des microservices.",
                 "Donation à la CNCF (Incubating) : Garantit la pérennité, la neutralité et l'indépendance technologique.",
                 "Architecture 100% extensible : Tout est un plugin (React Frontend + Node.js Backend).",
                 "Adoption massive des standards du marché : Intégrations prêtes à l'emploi avec GitHub, GitLab, Kubernetes, ArgoCD, Jira, PagerDuty, SonarQube, Grafana.",
                 "Philosophie GitOps : Le catalogue est versionné sous forme de manifestes YAML ('catalog-info.yaml') directement dans les dépôts de code des équipes."
             ], badge="POINTS FORTS", badge_color=ACCENT_GREEN)

    add_card(s10, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Les 3 Fonctionnalités Clés Démontrées", [
                 "1. Le Software Catalog (Catalogue Logiciel) :",
                 "   • Registre centralisé de tous les microservices, APIs, bibliothèques et domaines.",
                 "   • Fini les composants orphelins : chaque ressource a une équipe propriétaire (Ownership) et un lien Slack/Repo.",
                 "2. Le Software Templates (Scaffolder) :",
                 "   • Création de microservices 'Golden Path' en 4 étapes guidées.",
                 "   • Génération de code, initialisation Git, CI/CD et déploiement automatisés.",
                 "3. TechDocs (Docs-as-Code) :",
                 "   • Documentation écrite en Markdown dans le dépôt Git, compilée et unifiée dans le portail."
             ], badge="CORE MODULES", badge_color=ACCENT_BLUE)

    # ==========================================
    # SLIDE 11 : Scénario de la Démonstration (3-5 min)
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "DÉMONSTRATION EN DIRECT (3 À 5 MIN)", "Scénario du Cas d'Usage Backstage", "Mise en situation réelle : un nouveau développeur crée et explore un microservice.")

    demo_steps = [
        ("Étape 1 (1 min)", "Exploration du Catalogue & Découverte", [
            "Recherche du microservice 'payment-gateway-service'.",
            "Visualisation du propriétaire ('team-payments'), statut de santé, version d'API exposée et dépendances (PostgreSQL).",
            "Objectif : Montrer la fin des silos d'information et la cartographie instantanée."
        ], ACCENT_GREEN, Inches(0.8), Inches(2.0)),
        ("Étape 2 (2 min)", "Création d'un Service via Golden Path (Scaffolder)", [
            "Lancement du template 'Microservice Node.js / Express Paved Road'.",
            "Saisie des métadonnées (nom du repo, base de données, options de monitoring).",
            "Exécution du pipeline automatisé : Création du repo Git (github.com/ferid-saad/...), CI GitHub Actions, catalog-info.yaml."
        ], ACCENT_BLUE, Inches(6.8), Inches(2.0)),
        ("Étape 3 (1 min)", "Documentation TechDocs & Observabilité", [
            "Consultation de la documentation technique intégrée du service.",
            "Affichage des spécifications OpenAPI / Swagger interactives.",
            "Démonstration du fichier 'catalog-info.yaml' (Infrastructure & Catalog-as-Code)."
        ], ACCENT_PURPLE, Inches(0.8), Inches(4.5)),
        ("Valeur Ajoutée Démontrée", "Bénéfice Développeur & Entreprise", [
            "Gain de temps : De 3 jours à 2 minutes pour démarrer un projet en production.",
            "Sécurité & Conformité assurées dès la seconde zéro (Zéro configuration manuelle).",
            "Autonomie totale des équipes sans solliciter l'équipe Infrastructure."
        ], ACCENT_AMBER, Inches(6.8), Inches(4.5))
    ]

    for badge, title, items, color, left, top in demo_steps:
        add_card(s11, left, top, Inches(5.6), Inches(2.2), title, items, badge=badge, badge_color=color)

    # ==========================================
    # SLIDE 12 : Transition Live Démo
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)

    live_box = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.5), Inches(10.33), Inches(4.5))
    live_box.fill.solid()
    live_box.fill.fore_color.rgb = CARD_BG
    live_box.line.color.rgb = ACCENT_GREEN
    live_box.line.width = Pt(3)

    ltf = live_box.text_frame
    ltf.margin_left = Inches(0.5)
    ltf.margin_top = Inches(0.6)

    lp1 = ltf.paragraphs[0]
    lp1.text = "PLACE À LA DÉMONSTRATION EN DIRECT"
    lp1.font.size = Pt(16)
    lp1.font.bold = True
    lp1.font.color.rgb = ACCENT_GREEN
    lp1.space_after = Pt(14)

    lp2 = ltf.add_paragraph()
    lp2.text = "Démonstration Interactive de Spotify Backstage"
    lp2.font.size = Pt(34)
    lp2.font.bold = True
    lp2.font.color.rgb = TEXT_WHITE
    lp2.space_after = Pt(20)

    lp3 = ltf.add_paragraph()
    lp3.text = "Points d'attention pour l'auditoire pendant la démo :"
    lp3.font.size = Pt(16)
    lp3.font.bold = True
    lp3.font.color.rgb = ACCENT_BLUE
    lp3.space_after = Pt(10)

    checks = [
        "1. La navigation fluide dans le Software Catalog (Cartographie temps réel)",
        "2. Le wizard Scaffolder automatisant le déploiement d'un microservice (Golden Path)",
        "3. La centralisation des spécifications API et de TechDocs dans une interface unique",
        "4. La transparence GitOps grâce au fichier catalog-info.yaml"
    ]
    for check in checks:
        cp = ltf.add_paragraph()
        cp.text = f"✔  {check}"
        cp.font.size = Pt(13)
        cp.font.color.rgb = TEXT_BODY
        cp.space_after = Pt(4)

    # ==========================================
    # SLIDE 13 : Avantages & Bénéfices
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "ANALYSE CRITIQUE", "Bénéfices & Valeur Ajoutée Mesurée", "L'impact concret sur l'efficacité opérationnelle et les métriques d'ingénierie.")

    add_card(s13, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Impact sur les Métriques DORA", [
                 "Lead Time for Changes : Réduction de 60 à 80% du délai entre la première ligne de code et la mise en production.",
                 "Deployment Frequency : Multiplication par 3 à 5 de la fréquence de déploiement grâce à des pipelines standardisés.",
                 "Time to Restore Service (MTTR) : Résolution accélérée des incidents grâce à l'identification immédiate du propriétaire du service et de ses dépendances.",
                 "Change Failure Rate : Chute significative des incidents en production grâce aux garde-fous intégrés dans les templates."
             ], badge="DORA METRICS", badge_color=ACCENT_GREEN)

    add_card(s13, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Bénéfices Métier & Organisationnels", [
                 "Onboarding express : Un nouvel ingénieur est autonome et déploie du code dès son premier jour (au lieu de plusieurs semaines).",
                 "Standardisation & Fin du Shadow IT : Tout composant déployé est inventorié, monitoré et sécurisé par défaut.",
                 "Attractivité des talents : Une excellente expérience développeur (DevEx) limite le turnover et attire les meilleurs ingénieurs.",
                 "Optimisation FinOps : Meilleure visibilité et décommissionnement aisé des ressources obsolètes ou orphelines."
             ], badge="BUSINESS ROI", badge_color=ACCENT_BLUE)

    # ==========================================
    # SLIDE 14 : Limites, Risques et Pièges
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "ANALYSE CRITIQUE", "Limites, Risques & Pièges à Éviter", "Le Platform Engineering n'est pas une formule magique : les facteurs d'échec fréquents.")

    add_card(s14, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Les 3 Pièges Majeurs d'Adoption", [
                 "1. Le piège de l'imposition ('Construisez-le et ils viendront') :",
                 "   • Forcer l'adoption d'un outil sans écouter les besoins réels des développeurs conduit au rejet massif.",
                 "   • La plateforme doit être choisie par les développeurs pour sa valeur, non par décret managérial.",
                 "2. L'effet 'Usine à Gaz' (Over-engineering) :",
                 "   • Vouloir tout automatiser et créer des abstractions trop rigides qui empêchent l'innovation.",
                 "3. La sous-estimation de la maintenance :",
                 "   • Maintenir Backstage nécessite une équipe dédiée avec de vraies compétences logicielles (React/Node)."
             ], badge="RISQUES", badge_color=ACCENT_RED)

    add_card(s14, Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8),
             "Conditions de Succès", [
                 "Créer une vraie 'Platform Team' pluridisciplinaire (avec un Product Manager dédié).",
                 "Adopter une approche itérative : Commencer par un seul cas d'usage douloureux (ex: provisionner une base de données ou un service).",
                 "Mesurer en permanence le Net Promoter Score Développeur (Dev-NPS) et l'usage réel des templates.",
                 "Maintenir des 'Golden Paths' sans interdire totalement les chemins alternatifs ('Paved road, not a paved prison')."
             ], badge="RECOMMANDATIONS", badge_color=ACCENT_AMBER)

    # ==========================================
    # SLIDE 15 : Perspectives & Futur (IA & 2026)
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "HORIZON 2025-2026", "Perspectives d'Adoption & Convergence avec l'IA", "Comment l'IA Générative et les agents transforment les Internal Developer Platforms.")

    add_card(s15, Inches(0.8), Inches(2.0), Inches(3.7), Inches(4.8),
             "Intégration de l'IA (GenAI)", [
                 "Génération de Scaffolder par Prompt en langage naturel ('Crée-moi une API Go avec Kafka et PostgreSQL').",
                 "Assistants d'architecture analysant le catalogue pour proposer des refactorisations ou détecter des vulnérabilités.",
                 "TechDocs intelligentes : Requêtes en langage naturel sur l'ensemble de la documentation interne."
             ], badge="IA & COPILOT", badge_color=ACCENT_PURPLE)

    add_card(s15, Inches(4.8), Inches(2.0), Inches(3.7), Inches(4.8),
             "Plateformes Auto-Réparatrices", [
                 "Agents d'observabilité connectés aux IDP capables de diagnostiquer et corriger les dérives de configuration.",
                 "Mise à jour automatique des dépendances et des manifests GitOps en cas de CVE sans intervention humaine.",
                 "Optimisation dynamique des coûts FinOps basée sur le trafic réel."
             ], badge="AUTONOMIE", badge_color=ACCENT_BLUE)

    add_card(s15, Inches(8.8), Inches(2.0), Inches(3.7), Inches(4.8),
             "Standardisation CNCF", [
                 "Maturité croissante du Platform Working Group de la CNCF (Platform Whitepaper).",
                 "Consolidation des spécifications ouvertes comme Score (Open Source Developer-centric workload specification).",
                 "Émergence de solutions hybrides combinant portail unifié et orchestrateur d'infrastructure universel."
             ], badge="STANDARDS", badge_color=ACCENT_GREEN)

    # ==========================================
    # SLIDE 16 : Conclusion & Q&A
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16)

    c_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.2), Inches(10.33), Inches(5.1))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = CARD_BG
    c_box.line.color.rgb = ACCENT_GREEN
    c_box.line.width = Pt(2)

    ctf = c_box.text_frame
    ctf.margin_left = Inches(0.6)
    ctf.margin_top = Inches(0.5)

    cp1 = ctf.paragraphs[0]
    cp1.text = "SYNTHÈSE FINALE"
    cp1.font.size = Pt(14)
    cp1.font.bold = True
    cp1.font.color.rgb = ACCENT_GREEN
    cp1.space_after = Pt(10)

    cp2 = ctf.add_paragraph()
    cp2.text = "Conclusion : Le Futur du Développement Logiciel à l'Échelle"
    cp2.font.size = Pt(28)
    cp2.font.bold = True
    cp2.font.color.rgb = TEXT_WHITE
    cp2.space_after = Pt(16)

    recap_points = [
        "Le Platform Engineering n'est pas un désaveu de DevOps : c'en est l'aboutissement naturel pour libérer les développeurs de la complexité infrastructurelle.",
        "Une IDP réussie repose sur l'approche 'Platform as a Product' : écoute des développeurs, Golden Paths attractifs et autonomie en self-service.",
        "Backstage s'impose comme la clé de voûte logicielle grâce à son catalogue unifié, son extensibilité et sa neutralité CNCF.",
        "Le ROI se mesure sur la vitesse de livraison (DORA) et la réduction drastique de la charge mentale des ingénieurs."
    ]

    for pt in recap_points:
        p = ctf.add_paragraph()
        p.text = f"✔  {pt}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(8)

    q_box = ctf.add_paragraph()
    q_box.text = "\nMerci pour votre écoute ! Place aux questions & échanges (Session Q&A)"
    q_box.font.size = Pt(15)
    q_box.font.bold = True
    q_box.font.color.rgb = ACCENT_BLUE

    author_box = ctf.add_paragraph()
    author_box.text = "Auteur : Ferid Saad  |  GitHub : https://github.com/ferid-saad"
    author_box.font.size = Pt(13)
    author_box.font.color.rgb = ACCENT_GREEN

    # Save
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    import shutil
    out_dir = r"C:\Users\fersd\.gemini\antigravity-ide\scratch\platform-engineering-tp"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "Platform_Engineering_Ferid_Saad.pptx")
    create_presentation(out_file)

    # Copy to Downloads, Desktop and Backstage Demo
    for target_path in [
        r"C:\Users\fersd\Downloads\Platform_Engineering_Ferid_Saad.pptx",
        r"C:\Users\fersd\Desktop\Platform_Engineering_Ferid_Saad.pptx",
        os.path.join(out_dir, "backstage-demo", "Platform_Engineering_Ferid_Saad.pptx")
    ]:
        try:
            shutil.copy2(out_file, target_path)
            print(f"Copied to: {target_path}")
        except Exception as e:
            print(f"Notice on copy to {target_path}: {e}")
