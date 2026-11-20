const skills = [
  "Docker",
  "Kubernetes",
  "Jenkins",
  "GitHub Actions",
  "Ansible",
  "Terraform",
  "Prometheus",
  "Grafana",
  "Backstage"
];

const projects = [
  {
    title: "CI/CD Pipeline",
    description: "Automatisation du build, des tests et du déploiement.",
    technology: "Jenkins · Docker · GitHub"
  },
  {
    title: "Kubernetes Platform",
    description: "Orchestration et gestion des applications conteneurisées.",
    technology: "Kubernetes · Helm · Docker"
  },
  {
    title: "Monitoring Infrastructure",
    description: "Supervision des applications et des infrastructures.",
    technology: "Prometheus · Grafana"
  }
];

export default function Home() {
  return (
    <main className="container">
      <nav className="navbar">
        <strong>DevOps Portfolio</strong>
        <div>
          <a href="#about">À propos</a>
          <a href="#skills">Compétences</a>
          <a href="#projects">Projets</a>
          <a href="#certifications">Certifications</a>
        </div>
      </nav>

      <section className="hero">
        <p className="eyebrow">DEVOPS ENGINEER | CLOUD ENGINEER</p>
        <h1>Bonjour, je suis <span>Votre Nom</span></h1>
        <p>
          Je conçois, automatise et déploie des applications modernes
          grâce aux pratiques DevOps et aux technologies Cloud.
        </p>
        <a className="primary-button" href="#projects">
          Découvrir mes projets
        </a>
      </section>

      <section id="about" className="section">
        <h2>À propos</h2>
        <p>
          Passionné par l'automatisation, le Cloud et le Platform
          Engineering, je développe des solutions fiables,
          sécurisées et évolutives.
        </p>
      </section>

      <section id="skills" className="section">
        <h2>Compétences DevOps & Cloud</h2>
        <div className="skills">
          {skills.map((skill) => (
            <span key={skill} className="skill">{skill}</span>
          ))}
        </div>
      </section>

      <section id="projects" className="section">
        <h2>Projets DevOps & Cloud</h2>
        <div className="projects">
          {projects.map((project) => (
            <article className="project-card" key={project.title}>
              <h3>{project.title}</h3>
              <p>{project.description}</p>
              <small>{project.technology}</small>
            </article>
          ))}
        </div>
      </section>

      <section id="certifications" className="section">
        <h2>Certifications</h2>
        <p>Les certifications professionnelles seront ajoutées ici.</p>
      </section>

      <footer>
        © 2026 DevOps Portfolio · Généré avec Backstage et Next.js
      </footer>
    </main>
  );
}
