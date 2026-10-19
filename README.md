# TP Platform Engineering : Dossier de Présentation & Démonstration Backstage

Ce dossier contient l'ensemble des livrables pour réussir votre soutenance de TP sur le **Platform Engineering** et les **Internal Developer Platforms (IDP)**, calibré pour une durée de **15 à 20 minutes** (dont **3 à 5 minutes de démonstration**).

---

## 📁 Contenu du Dossier

```text
platform-engineering-tp/
├── Platform_Engineering_Ferid_Saad.pptx   <-- Diaporama PowerPoint 16:9 (16 slides)
├── PRESENTATION_SPEAKER_NOTES.md                <-- Guide complet mot-à-mot pour l'oral (15-20 min)
├── DEMO_SCRIPT_BACKSTAGE.md                     <-- Scénario minute par minute de la démo (3-5 min)
├── generate_presentation.py                     <-- Script Python source ayant généré le PPTX
└── backstage-demo/                              <-- Application de Démonstration Interactive Backstage
    ├── index.html                               <-- Interface portail Backstage (Spotify theme)
    ├── styles.css                               <-- Feuilles de style fidèles aux tokens Backstage
    ├── app.js                                   <-- Moteur interactif (Catalogue, Scaffolder, Logs)
    ├── catalog-info.yaml                        <-- Manifeste officiel Backstage (GitOps)
    ├── template.yaml                            <-- Manifeste de template Scaffolder (Golden Path)
    ├── start_demo.bat                           <-- Lanceur Windows en 1 clic (Double-cliquer)
    └── start_demo.py                            <-- Serveur HTTP local Python
```

---

## 🚀 Comment Lancer la Démonstration Backstage (1 clic)

1. **Option 1 (Le plus simple)** : Double-cliquez sur le fichier `start_demo.bat` dans le dossier `backstage-demo/`.
2. **Option 2** : Ouvrez un terminal dans le dossier et lancez :
   ```bash
   python start_demo.py
   ```
3. Votre navigateur s'ouvrira immédiatement sur `http://localhost:3000`.
4. Mettez le navigateur en **plein écran (`F11`)** pour une immersion totale.

---

## 🎯 Rappel des Attendus du TP & Où les Retrouver

| Attendu du Sujet | Traitement dans le PPTX | Traitement dans la Démo |
| :--- | :--- | :--- |
| **1. Définition du Platform Engineering** | Slides 4 et 5 (Concept IDP, Platform as a Product, DevEx, 4 piliers) | Présentation du portail unifié |
| **2. Différences avec le DevOps traditionnel** | Slide 3 (Surcharge cognitive "You build it, you run it") & Slide 6 (Grand tableau comparatif) | Passage du ticket Jira au libre-service |
| **3. Comparatif de plusieurs solutions** | Slide 8 (Backstage, Port, Humanitec, AWS Proton, Azure) & Slide 9 (Matrice multicritères) | Justification du choix de Backstage |
| **4. Démonstration de l'outil choisi** | Slides 10, 11 et 12 (Focus Backstage et scénario) | Démo live du Software Catalog, Scaffolder Golden Path et TechDocs |
| **5. Avantages, limites et perspectives** | Slide 13 (Métriques DORA, ROI), Slide 14 (Risques, usine à gaz), Slide 15 (IA & 2026), Slide 16 (Conclusion) | Argumentaire oral & réponses aux questions |

---

## 💡 Conseils pour l'Exposé Oral (15-20 min)
1. **Slides 1 à 9 (~9-10 min)** : Posez le problème de la surcharge cognitive DevOps et présentez le comparatif des solutions.
2. **Démonstration Backstage (~4 min)** : Basculez sur `http://localhost:3000` et suivez le script `DEMO_SCRIPT_BACKSTAGE.md`.
3. **Slides 13 à 16 (~4-5 min)** : Revenez sur le diaporama pour l'analyse critique, le ROI DORA et les perspectives IA.
4. **Q&A (~3-5 min)** : Utilisez la section FAQ de `PRESENTATION_SPEAKER_NOTES.md` pour répondre aux questions du jury.
