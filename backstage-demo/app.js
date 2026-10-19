// Spotify Backstage IDP Demonstration - Interactive Logic
const initialEntities = [
  {
    name: 'payment-gateway-service',
    kind: 'Component',
    type: 'service',
    system: 'e-commerce-core',
    owner: 'team-payments',
    lifecycle: 'production',
    uptime: '99.98%',
    description: 'Microservice critique gérant les autorisations CB, Stripe et les remboursements clients.',
    tags: ['payments', 'stripe', 'critical-tier-1', 'nodejs'],
    repo: 'https://github.com/ferid-saad/payment-gateway-service',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: payment-gateway-service
  description: Microservice critique gérant les autorisations CB et les remboursements
  tags:
    - payments
    - stripe
    - nodejs
  annotations:
    github.com/project-slug: ferid-saad/payment-gateway-service
    backstage.io/techdocs-ref: dir:.
    argocd/app-name: payment-gateway-prod
    datadog/service-name: payment-gateway
spec:
  type: service
  lifecycle: production
  owner: team-payments
  system: e-commerce-core
  providesApis:
    - payments-api-v1
  consumesApis:
    - auth-tokens-v2
  dependsOn:
    - resource:postgres-payments-cluster`
  },
  {
    name: 'checkout-web-frontend',
    kind: 'Component',
    type: 'website',
    system: 'e-commerce-core',
    owner: 'team-checkout',
    lifecycle: 'production',
    uptime: '99.95%',
    description: 'Interface web React du tunnel de paiement et panier d\'achat.',
    tags: ['react', 'frontend', 'vite', 'checkout'],
    repo: 'https://github.com/ferid-saad/checkout-web-frontend',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: checkout-web-frontend
  description: Interface web React du tunnel de paiement et panier d'achat
  tags:
    - react
    - frontend
spec:
  type: website
  lifecycle: production
  owner: team-checkout
  system: e-commerce-core
  consumesApis:
    - payments-api-v1
    - auth-tokens-v2`
  },
  {
    name: 'auth-identity-service',
    kind: 'Component',
    type: 'service',
    system: 'security-platform',
    owner: 'team-auth',
    lifecycle: 'production',
    uptime: '99.99%',
    description: 'Fournisseur d\'identité OAuth2 / OIDC et validation de jetons JWT.',
    tags: ['security', 'oauth2', 'jwt', 'go'],
    repo: 'https://github.com/ferid-saad/auth-identity-service',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: auth-identity-service
  description: Fournisseur d'identité OAuth2 / OIDC et validation de jetons JWT
spec:
  type: service
  lifecycle: production
  owner: team-auth
  system: security-platform
  providesApis:
    - auth-tokens-v2`
  },
  {
    name: 'customer-account-service',
    kind: 'Component',
    type: 'service',
    system: 'crm-suite',
    owner: 'team-core',
    lifecycle: 'production',
    uptime: '99.91%',
    description: 'Gestion des profils clients, adresses de livraison et préférences.',
    tags: ['java', 'spring-boot', 'postgres'],
    repo: 'https://github.com/ferid-saad/customer-account-service',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: customer-account-service
  description: Gestion des profils clients, adresses de livraison
spec:
  type: service
  lifecycle: production
  owner: team-core
  system: crm-suite`
  },
  {
    name: 'notification-dispatcher',
    kind: 'Component',
    type: 'service',
    system: 'comms-system',
    owner: 'team-core',
    lifecycle: 'experimental',
    uptime: '98.50%',
    description: 'Envoi asynchrone des emails transactionnels, SMS et push notifications.',
    tags: ['kafka', 'email', 'sms', 'python'],
    repo: 'https://github.com/ferid-saad/notification-dispatcher',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: notification-dispatcher
  description: Envoi asynchrone des emails transactionnels et SMS
spec:
  type: service
  lifecycle: experimental
  owner: team-core
  system: comms-system`
  },
  {
    name: 'payments-api-v1',
    kind: 'API',
    type: 'openapi',
    system: 'e-commerce-core',
    owner: 'team-payments',
    lifecycle: 'production',
    uptime: 'N/A (Spec)',
    description: 'Contrat OpenAPI 3.0 pour l\'encaissement sécurisé et remboursements.',
    tags: ['rest', 'openapi', 'v1'],
    repo: 'https://github.com/ferid-saad/payment-gateway-service',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: payments-api-v1
  description: Contrat OpenAPI 3.0 pour l'encaissement sécurisé
spec:
  type: openapi
  lifecycle: production
  owner: team-payments
  system: e-commerce-core
  definition: $text: https://api.ferid-saad.io/specs/payments-v1.json`
  },
  {
    name: 'auth-tokens-v2',
    kind: 'API',
    type: 'openid-connect',
    system: 'security-platform',
    owner: 'team-auth',
    lifecycle: 'production',
    uptime: 'N/A (Spec)',
    description: 'Spécification des endpoints OIDC /.well-known/openid-configuration.',
    tags: ['oidc', 'oauth2'],
    repo: 'https://github.com/ferid-saad/auth-identity-service',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: auth-tokens-v2
spec:
  type: openid-connect
  lifecycle: production
  owner: team-auth
  system: security-platform`
  },
  {
    name: 'e-commerce-core',
    kind: 'System',
    type: 'system',
    system: 'enterprise-architecture',
    owner: 'team-checkout',
    lifecycle: 'production',
    uptime: '99.98%',
    description: 'Système regroupant l\'ensemble des microservices du parcours d\'achat.',
    tags: ['domain-core', 'business-critical'],
    repo: 'https://github.com/ferid-saad',
    yaml: `apiVersion: backstage.io/v1alpha1
kind: System
metadata:
  name: e-commerce-core
spec:
  owner: team-checkout
  domain: digital-commerce`
  }
];

let catalogEntities = [...initialEntities];
let activeEntity = catalogEntities[0];

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
  renderCatalog();
  setupNavigation();
  setupFilters();
  setupSearch();
  setupEntityTabs();
  setupDemoGuide();
});

// Render Catalog Table
function renderCatalog() {
  const tbody = document.getElementById('catalog-table-body');
  const searchVal = document.getElementById('global-search').value.toLowerCase().trim();
  const kindFilter = document.querySelector('#kind-filters .pill.active')?.dataset.value || 'all';
  const lifecycleFilter = document.querySelector('#lifecycle-filters .pill.active')?.dataset.value || 'all';
  const ownerFilter = document.getElementById('owner-select')?.value || 'all';

  const filtered = catalogEntities.filter(item => {
    // Search matching
    const matchesSearch = !searchVal || 
      item.name.toLowerCase().includes(searchVal) ||
      item.owner.toLowerCase().includes(searchVal) ||
      item.description.toLowerCase().includes(searchVal) ||
      item.tags.some(t => t.toLowerCase().includes(searchVal));

    // Kind filter
    const matchesKind = (kindFilter === 'all') || (item.kind === kindFilter);

    // Lifecycle filter
    const matchesLifecycle = (lifecycleFilter === 'all') || (item.lifecycle === lifecycleFilter);

    // Owner filter
    const matchesOwner = (ownerFilter === 'all') || (item.owner === ownerFilter);

    return matchesSearch && matchesKind && matchesLifecycle && matchesOwner;
  });

  tbody.innerHTML = '';

  if (filtered.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 32px; color: #94a3b8;">Aucune entité trouvée pour ces filtres.</td></tr>`;
    return;
  }

  filtered.forEach(item => {
    const tr = document.createElement('tr');
    const isLive = item.lifecycle === 'production';
    
    tr.innerHTML = `
      <td>
        <div>
          <a class="entity-link" onclick="navigateToEntity('${item.name}', 'overview')">${item.name}</a>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">${item.description.substring(0, 55)}...</div>
        </div>
      </td>
      <td><span class="tag">${item.system}</span></td>
      <td><span class="value link" onclick="filterByOwner('${item.owner}')">${item.owner}</span></td>
      <td><span class="badge ${item.kind === 'API' ? 'info' : (item.kind === 'System' ? 'purple' : '')}">${item.type}</span></td>
      <td>
        <span class="status-badge ${isLive ? 'live' : 'exp'}">${item.lifecycle}</span>
      </td>
      <td>
        <span style="font-weight: 600; color: ${isLive ? '#1db954' : '#f59e0b'};">${item.uptime}</span>
      </td>
      <td>
        <button class="btn-sm" onclick="navigateToEntity('${item.name}', 'overview')">Inspecter</button>
      </td>
    `;
    tbody.appendChild(tr);
  });

  // Update counts
  document.getElementById('catalog-count-badge').textContent = catalogEntities.length;
  document.getElementById('stat-total-services').textContent = catalogEntities.filter(e => e.kind === 'Component').length;
}

// Navigation between views
function navigateTo(viewId) {
  document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.sidebar-nav .nav-item').forEach(n => n.classList.remove('active'));

  const targetView = document.getElementById(`view-${viewId}`);
  if (targetView) {
    targetView.classList.add('active');
  }

  const navLink = document.querySelector(`.sidebar-nav .nav-item[data-view="${viewId}"]`);
  if (navLink) {
    navLink.classList.add('active');
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function setupNavigation() {
  document.querySelectorAll('.sidebar-nav .nav-item').forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const view = item.dataset.view;
      if (view) navigateTo(view);
    });
  });
}

// Entity View Logic
function navigateToEntity(entityName, initialTab = 'overview') {
  const entity = catalogEntities.find(e => e.name === entityName);
  if (!entity) return;

  activeEntity = entity;

  // Populate data
  document.getElementById('entity-kind-badge').textContent = entity.kind;
  document.getElementById('entity-title-name').textContent = entity.name;
  document.getElementById('entity-heading-name').textContent = entity.name;
  document.getElementById('entity-heading-desc').textContent = entity.description;
  document.getElementById('entity-meta-owner').textContent = entity.owner;
  document.getElementById('entity-meta-system').textContent = entity.system;
  document.getElementById('entity-meta-lifecycle').textContent = entity.lifecycle;
  document.getElementById('entity-github-link').href = entity.repo;

  // Tags
  const tagsContainer = document.getElementById('entity-meta-tags');
  tagsContainer.innerHTML = '';
  entity.tags.forEach(t => {
    const s = document.createElement('span');
    s.className = 'tag';
    s.textContent = t;
    tagsContainer.appendChild(s);
  });

  // YAML
  document.getElementById('entity-yaml-display').textContent = entity.yaml;

  // Open entity view
  navigateTo('entity');
  openEntityTab(initialTab);
}

function setupEntityTabs() {
  document.querySelectorAll('.entity-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.dataset.tab;
      openEntityTab(tabId);
    });
  });
}

function openEntityTab(tabId) {
  document.querySelectorAll('.entity-tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.entity-tab-content').forEach(c => c.classList.remove('active'));

  const btn = document.querySelector(`.entity-tab-btn[data-tab="${tabId}"]`);
  const content = document.getElementById(`tab-${tabId}`);
  if (btn) btn.classList.add('active');
  if (content) content.classList.add('active');
}

// Search & Filter Listeners
function setupFilters() {
  // Pill filters
  document.querySelectorAll('.pill-filters .pill').forEach(pill => {
    pill.addEventListener('click', () => {
      const parent = pill.parentElement;
      parent.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      renderCatalog();
    });
  });

  // Owner dropdown
  document.getElementById('owner-select')?.addEventListener('change', () => {
    renderCatalog();
  });
}

function filterByOwner(ownerName) {
  const select = document.getElementById('owner-select');
  if (select) {
    select.value = ownerName;
    navigateTo('catalog');
    renderCatalog();
  }
}

function setupSearch() {
  const input = document.getElementById('global-search');
  input.addEventListener('input', () => {
    // If not in catalog view, switch to catalog view to show results
    const activeView = document.querySelector('.view-panel.active');
    if (activeView && activeView.id !== 'view-catalog') {
      navigateTo('catalog');
    }
    renderCatalog();
  });
}

// Scaffolder Wizard Logic
function startScaffolder(templateType) {
  document.getElementById('scaffolder-selector').style.display = 'none';
  const wizard = document.getElementById('scaffolder-wizard');
  wizard.style.display = 'block';

  let title = "Configuration du Microservice Node.js / Express API";
  if (templateType === 'spring') title = "Configuration : Spring Boot 3 Enterprise API";
  if (templateType === 'react') title = "Configuration : React + Vite Dashboard App";
  if (templateType === 'terraform') title = "Configuration : Terraform Cloud Resource";

  document.getElementById('wizard-template-title').textContent = title;
  goToStep(1);
}

function cancelScaffolder() {
  document.getElementById('scaffolder-selector').style.display = 'grid';
  document.getElementById('scaffolder-wizard').style.display = 'none';
  document.getElementById('scaffolder-success-card').style.display = 'none';
  document.getElementById('terminal-logs').innerHTML = '';
}

function goToStep(stepNumber) {
  document.querySelectorAll('.wizard-step-body').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.wizard-stepper .step-item').forEach(s => {
    s.classList.remove('active');
    const sNum = parseInt(s.dataset.step);
    if (sNum < stepNumber) {
      s.classList.add('completed');
    } else {
      s.classList.remove('completed');
    }
  });

  const stepBody = document.getElementById(`step-${stepNumber}`);
  const stepIndicator = document.querySelector(`.step-item[data-step="${stepNumber}"]`);

  if (stepBody) stepBody.classList.add('active');
  if (stepIndicator) stepIndicator.classList.add('active');
}

// Execute Scaffolder with simulated animated terminal logs
let newlyCreatedServiceName = '';

function executeScaffolder() {
  const name = document.getElementById('wiz-name').value.trim() || 'order-fulfillment-service';
  const desc = document.getElementById('wiz-desc').value.trim() || 'Service de traitement automatisé';
  const owner = document.getElementById('wiz-owner').value;
  const repo = document.getElementById('wiz-repo-name').value.trim() || name;
  const db = document.querySelector('input[name="wiz-db"]:checked')?.value || 'PostgreSQL';

  newlyCreatedServiceName = name;

  goToStep(4);
  const term = document.getElementById('terminal-logs');
  term.innerHTML = '';
  document.getElementById('scaffolder-success-card').style.display = 'none';

  const logSteps = [
    { text: `[1/6] 📥 Fetching template skeleton: github.com/ferid-saad/backstage-templates/nodejs-paved-road...`, delay: 300, class: 'info' },
    { text: `[2/6] ⚙️  Injecting variables: name=${name}, owner=${owner}, db="${db}"...`, delay: 900, class: 'info' },
    { text: `[3/6] 📦 Generating project structure (TypeScript 5.4, Dockerfile, Jest, ESLint)... OK`, delay: 1500, class: '' },
    { text: `[4/6] 🚀 Creating GitHub repository: https://github.com/ferid-saad/${repo}... OK`, delay: 2200, class: 'info' },
    { text: `[5/6] 🔒 Setting up GitHub Actions CI workflow & Branch Protection Rules... OK`, delay: 2900, class: '' },
    { text: `[6/6] 📝 Registering catalog-info.yaml into Backstage Software Catalog...`, delay: 3600, class: 'warn' },
    { text: `✔ SUCCESS: Entity "component:default/${name}" registered into catalog!`, delay: 4200, class: 'success' },
    { text: `✔ Golden Path execution completed in 4.2 seconds. No tickets needed!`, delay: 4500, class: 'success' }
  ];

  logSteps.forEach(step => {
    setTimeout(() => {
      const line = document.createElement('div');
      line.className = `term-line ${step.class}`;
      line.textContent = step.text;
      term.appendChild(line);
      term.scrollTop = term.scrollHeight;

      if (step.delay === 4500) {
        // Add to catalog
        const newEntity = {
          name: name,
          kind: 'Component',
          type: 'service',
          system: 'e-commerce-core',
          owner: owner,
          lifecycle: 'experimental',
          uptime: '100% (New)',
          description: desc,
          tags: ['nodejs', 'express', 'golden-path', 'new'],
          repo: `https://github.com/ferid-saad/${repo}`,
          yaml: `apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: ${name}
  description: ${desc}
  tags:
    - nodejs
    - express
    - golden-path
spec:
  type: service
  lifecycle: experimental
  owner: ${owner}
  system: e-commerce-core
  dependsOn:
    - resource:postgres-aurora`
        };

        catalogEntities.unshift(newEntity);
        renderCatalog();

        document.getElementById('scaffolder-success-card').style.display = 'flex';
      }
    }, step.delay);
  });
}

function viewNewComponent() {
  if (newlyCreatedServiceName) {
    navigateToEntity(newlyCreatedServiceName, 'overview');
  } else {
    navigateTo('catalog');
  }
}

// Demo Guide Modal
function toggleDemoGuide() {
  const modal = document.getElementById('demo-guide-modal');
  modal.style.display = (modal.style.display === 'none' || !modal.style.display) ? 'flex' : 'none';
}

function setupDemoGuide() {
  document.getElementById('btn-demo-guide')?.addEventListener('click', toggleDemoGuide);
}
