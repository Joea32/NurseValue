from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NurseValue | Pay. Protect. Retain.</title>
  <style>
    :root {
      --bg: #030712;
      --bg-soft: rgba(255, 255, 255, 0.06);
      --card: rgba(255, 255, 255, 0.08);
      --line: rgba(255, 255, 255, 0.12);
      --text: #f8fafc;
      --muted: #cbd5e1;
      --cyan: #67e8f9;
      --blue: #60a5fa;
      --fuchsia: #f0abfc;
      --emerald: #6ee7b7;
      --shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
      --radius-xl: 28px;
      --radius-lg: 22px;
      --radius-md: 18px;
      --maxw: 1220px;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background:
        radial-gradient(circle at top left, rgba(96,165,250,0.20), transparent 28%),
        radial-gradient(circle at 88% 10%, rgba(110,231,183,0.16), transparent 23%),
        radial-gradient(circle at 20% 85%, rgba(240,171,252,0.14), transparent 28%),
        linear-gradient(180deg, #020617 0%, #030712 45%, #020617 100%);
      color: var(--text);
      overflow-x: hidden;
      position: relative;
    }

    body::before,
    body::after {
      content: "";
      position: fixed;
      width: 360px;
      height: 360px;
      border-radius: 999px;
      filter: blur(80px);
      pointer-events: none;
      z-index: 0;
      opacity: 0.22;
      animation: floatBlob 12s ease-in-out infinite;
    }

    body::before {
      background: var(--cyan);
      top: 5%;
      left: -120px;
    }

    body::after {
      background: var(--fuchsia);
      right: -120px;
      top: 50%;
      animation-delay: 2s;
    }

    @keyframes floatBlob {
      0%, 100% { transform: translateY(0px) translateX(0px) scale(1); }
      50% { transform: translateY(-25px) translateX(18px) scale(1.08); }
    }

    a { color: inherit; text-decoration: none; }

    .container {
      width: min(var(--maxw), calc(100% - 32px));
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }

    .nav {
      position: sticky;
      top: 14px;
      z-index: 20;
      padding-top: 14px;
    }

    .nav-shell {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      padding: 16px 18px;
      border: 1px solid var(--line);
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(18px);
      border-radius: 24px;
      box-shadow: var(--shadow);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .logo {
      width: 52px;
      height: 52px;
      object-fit: cover;
      border-radius: 16px;
      box-shadow: 0 14px 30px rgba(96, 165, 250, 0.25);
      border: 1px solid rgba(255,255,255,0.12);
      background: rgba(255,255,255,0.06);
    }

    .brand-badge {
      width: 52px;
      height: 52px;
      border-radius: 16px;
      display: grid;
      place-items: center;
      background: linear-gradient(135deg, var(--cyan), var(--blue), var(--fuchsia));
      color: #020617;
      font-weight: 900;
      font-size: 1.25rem;
      box-shadow: 0 14px 30px rgba(96, 165, 250, 0.25);
      border: 1px solid rgba(255,255,255,0.12);
    }

    .brand h1 {
      margin: 0;
      font-size: 1.4rem;
      line-height: 1;
      font-weight: 900;
      letter-spacing: -0.03em;
    }

    .brand p {
      margin: 4px 0 0;
      font-size: 0.78rem;
      color: #bae6fd;
      text-transform: uppercase;
      letter-spacing: 0.26em;
    }

    .nav-links {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
      justify-content: end;
    }

    .pill,
    .btn,
    .ghost-btn {
      border-radius: 999px;
      padding: 12px 18px;
      font-weight: 700;
      transition: 0.25s ease;
      border: 1px solid transparent;
      position: relative;
    }

    .pill {
      background: rgba(103, 232, 249, 0.10);
      border-color: rgba(103, 232, 249, 0.22);
      color: #cffafe;
      font-size: 0.92rem;
    }

    .btn {
      background: linear-gradient(135deg, #ffffff, #dbeafe);
      color: #020617;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 12px 30px rgba(255,255,255,0.12);
    }

    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 16px 36px rgba(255,255,255,0.18);
    }

    .ghost-btn {
      background: rgba(255,255,255,0.05);
      border-color: var(--line);
      color: white;
    }

    .ghost-btn:hover {
      background: rgba(255,255,255,0.09);
      transform: translateY(-2px);
    }

    .glow-btn {
      position: relative;
      overflow: visible;
    }

    .glow-btn::before {
      content: "";
      position: absolute;
      inset: -3px;
      border-radius: inherit;
      background: linear-gradient(90deg, #67e8f9, #60a5fa, #f0abfc, #67e8f9);
      background-size: 300% 300%;
      z-index: -1;
      animation: glowMove 4s linear infinite;
      filter: blur(10px);
      opacity: 0.9;
    }

    .glow-btn:hover {
      transform: translateY(-3px) scale(1.02);
    }

    @keyframes glowMove {
      0% { background-position: 0% 50%; }
      100% { background-position: 300% 50%; }
    }

    .hero {
      padding: 42px 0 30px;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 30px;
      align-items: center;
      min-height: 82vh;
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(110,231,183,0.10);
      border: 1px solid rgba(110,231,183,0.20);
      color: #d1fae5;
      padding: 10px 16px;
      border-radius: 999px;
      font-size: 0.92rem;
      font-weight: 700;
      animation: softFloat 5s ease-in-out infinite;
    }

    @keyframes softFloat {
      0%,100% { transform: translateY(0px); }
      50% { transform: translateY(-5px); }
    }

    .headline {
      margin: 18px 0 18px;
      font-size: clamp(3rem, 7vw, 6.3rem);
      line-height: 0.95;
      letter-spacing: -0.06em;
      font-weight: 950;
      max-width: 860px;
    }

    .gradient-text {
      background: linear-gradient(90deg, var(--cyan), var(--blue), var(--fuchsia));
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .hero-copy {
      font-size: 1.16rem;
      line-height: 1.9;
      color: var(--muted);
      max-width: 760px;
    }

    .cta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      margin-top: 28px;
    }

    .micro-note {
      margin-top: 14px;
      color: #93c5fd;
      font-size: 0.96rem;
    }

    .stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-top: 30px;
    }

    .stat,
    .card,
    .panel,
    .signup-box,
    .footer-card {
      border: 1px solid var(--line);
      background: var(--card);
      backdrop-filter: blur(14px);
      box-shadow: var(--shadow);
    }

    .stat {
      padding: 18px;
      border-radius: 24px;
      transition: transform 0.3s ease;
    }

    .stat:hover {
      transform: translateY(-5px);
    }

    .stat .value {
      font-size: 1.8rem;
      font-weight: 900;
      color: #a5f3fc;
      letter-spacing: -0.04em;
    }

    .stat .label {
      margin-top: 6px;
      color: var(--muted);
      line-height: 1.55;
      font-size: 0.95rem;
    }

    .panel {
      border-radius: 34px;
      padding: 24px;
      position: relative;
      overflow: hidden;
      animation: panelFloat 6s ease-in-out infinite;
    }

    @keyframes panelFloat {
      0%,100% { transform: translateY(0px); }
      50% { transform: translateY(-8px); }
    }

    .panel::before {
      content: "";
      position: absolute;
      inset: -30% auto auto -20%;
      width: 240px;
      height: 240px;
      border-radius: 999px;
      background: radial-gradient(circle, rgba(103,232,249,0.18), transparent 68%);
      pointer-events: none;
    }

    .panel-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 18px;
    }

    .panel-kicker {
      color: #94a3b8;
      font-weight: 600;
      font-size: 0.9rem;
    }

    .panel-title {
      font-size: 1.8rem;
      font-weight: 900;
      margin-top: 4px;
    }

    .status-chip {
      background: rgba(110,231,183,0.10);
      border: 1px solid rgba(110,231,183,0.22);
      color: #d1fae5;
      border-radius: 999px;
      padding: 10px 14px;
      font-size: 0.85rem;
      font-weight: 800;
      white-space: nowrap;
    }

    .progress-card,
    .dual-mini,
    .insight-card {
      border: 1px solid var(--line);
      border-radius: 24px;
      background: rgba(255,255,255,0.05);
      padding: 18px;
    }

    .progress-card {
      background: linear-gradient(180deg, rgba(34,211,238,0.12), rgba(34,211,238,0.07));
    }

    .row-between {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }

    .bar {
      height: 12px;
      border-radius: 999px;
      background: rgba(255,255,255,0.10);
      margin-top: 14px;
      overflow: hidden;
    }

    .bar-fill {
      width: 81%;
      height: 100%;
      background: linear-gradient(90deg, var(--cyan), var(--blue));
      border-radius: 999px;
      box-shadow: 0 0 20px rgba(96,165,250,0.45);
      animation: pulseBar 2.2s ease-in-out infinite;
      transform-origin: left;
    }

    @keyframes pulseBar {
      0%,100% { transform: scaleX(1); }
      50% { transform: scaleX(0.96); }
    }

    .mini-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 14px;
    }

    .dual-mini strong {
      display: block;
      font-size: 2.3rem;
      font-weight: 950;
      letter-spacing: -0.05em;
      margin: 6px 0;
    }

    .section {
      padding: 50px 0;
    }

    .section-title {
      font-size: clamp(2rem, 4vw, 4rem);
      font-weight: 950;
      line-height: 0.98;
      letter-spacing: -0.05em;
      margin: 8px 0 16px;
    }

    .section-kicker {
      text-transform: uppercase;
      letter-spacing: 0.25em;
      color: #94a3b8;
      font-size: 0.84rem;
      font-weight: 800;
    }

    .section-copy {
      color: var(--muted);
      max-width: 850px;
      line-height: 1.85;
      font-size: 1.06rem;
    }

    .cards-3,
    .cards-4,
    .vision-grid,
    .products-grid,
    .impact-grid {
      display: grid;
      gap: 18px;
    }

    .cards-3 { grid-template-columns: repeat(3, 1fr); margin-top: 26px; }
    .cards-4 { grid-template-columns: repeat(4, 1fr); margin-top: 24px; }
    .vision-grid { grid-template-columns: 1.08fr 0.92fr; margin-top: 24px; }
    .products-grid { grid-template-columns: repeat(2, 1fr); margin-top: 26px; }
    .impact-grid { grid-template-columns: repeat(3, 1fr); margin-top: 26px; }

    .card {
      padding: 24px;
      border-radius: 28px;
      transition: transform 0.25s ease, background 0.25s ease, box-shadow 0.25s ease;
      position: relative;
      overflow: hidden;
    }

    .card:hover {
      transform: translateY(-7px);
      background: rgba(255,255,255,0.10);
      box-shadow: 0 24px 60px rgba(0,0,0,0.35);
    }

    .icon {
      width: 58px;
      height: 58px;
      border-radius: 18px;
      display: grid;
      place-items: center;
      font-size: 1.6rem;
      background: linear-gradient(135deg, rgba(103,232,249,0.20), rgba(240,171,252,0.16));
      border: 1px solid rgba(255,255,255,0.10);
      margin-bottom: 16px;
    }

    .card h3 {
      margin: 0 0 10px;
      font-size: 1.45rem;
      font-weight: 900;
      letter-spacing: -0.03em;
    }

    .card p,
    .card li {
      color: var(--muted);
      line-height: 1.75;
    }

    .card ul {
      padding-left: 20px;
      margin: 14px 0 0;
    }

    .big-vision,
    .side-message {
      border-radius: 30px;
      padding: 28px;
      border: 1px solid var(--line);
      background: rgba(255,255,255,0.06);
      box-shadow: var(--shadow);
    }

    .big-vision {
      background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.05));
    }

    .quote {
      margin-top: 18px;
      font-size: 1.25rem;
      line-height: 1.7;
      color: #e2e8f0;
      font-weight: 600;
    }

    .tag-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 18px;
    }

    .tag {
      border-radius: 999px;
      padding: 10px 14px;
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--line);
      color: #e2e8f0;
      font-size: 0.92rem;
      font-weight: 700;
    }

    .signup-box {
      margin-top: 24px;
      border-radius: 34px;
      padding: 30px;
      background: linear-gradient(135deg, rgba(103,232,249,0.10), rgba(96,165,250,0.08), rgba(240,171,252,0.08));
    }

    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr auto;
      gap: 12px;
      margin-top: 22px;
    }

    input, select {
      width: 100%;
      border-radius: 16px;
      border: 1px solid rgba(255,255,255,0.12);
      background: rgba(2, 6, 23, 0.65);
      color: white;
      padding: 15px 16px;
      outline: none;
      font-size: 1rem;
    }

    input::placeholder { color: #94a3b8; }

    .submit-btn {
      border: none;
      cursor: pointer;
      border-radius: 16px;
      padding: 15px 22px;
      font-weight: 900;
      background: linear-gradient(135deg, #ffffff, #dbeafe);
      color: #020617;
      box-shadow: 0 12px 28px rgba(255,255,255,0.14);
    }

    .small-muted {
      color: #94a3b8;
      font-size: 0.92rem;
      line-height: 1.7;
      margin-top: 14px;
    }

    .footer {
      padding: 28px 0 60px;
    }

    .footer-card {
      border-radius: 34px;
      padding: 30px;
      background: linear-gradient(90deg, rgba(103,232,249,0.12), rgba(96,165,250,0.08), rgba(240,171,252,0.10));
      text-align: center;
    }

    .footer-card h2 {
      margin: 0;
      font-size: clamp(2rem, 4vw, 4.5rem);
      line-height: 0.96;
      font-weight: 950;
      letter-spacing: -0.05em;
    }

    .footer-card p {
      max-width: 760px;
      margin: 16px auto 0;
      color: var(--muted);
      line-height: 1.8;
      font-size: 1.08rem;
    }

    .reveal {
      opacity: 0;
      transform: translateY(26px);
      transition: 0.8s ease;
    }

    .reveal.visible {
      opacity: 1;
      transform: translateY(0);
    }

    @media (max-width: 1100px) {
      .hero-grid,
      .vision-grid,
      .products-grid,
      .cards-3,
      .impact-grid,
      .cards-4 {
        grid-template-columns: 1fr;
      }

      .form-grid {
        grid-template-columns: 1fr 1fr;
      }
    }

    .floating-logo {
  position: fixed;
  top: 17px;
  right: 14px;
  width: 200px;
  height: 200px;
  object-fit: contain;
  z-index: 999;
}

    @media (max-width: 720px) {
      .container { width: min(var(--maxw), calc(100% - 22px)); }
      .nav-shell { align-items: flex-start; flex-direction: column; }
      .stats,
      .mini-grid,
      .form-grid {
        grid-template-columns: 1fr;
      }
      .headline { font-size: 3rem; }
      .section { padding: 34px 0; }
      .panel, .card, .big-vision, .side-message, .signup-box, .footer-card { padding: 20px; }
      .nav-links { width: 100%; justify-content: flex-start; }
      .logo, .brand-badge { width: 46px; height: 46px; }

</style>
</head>
<body>
<img src="/static/logo.png" class="floating-logo">
  <div class="nav container">
    <div class="nav-shell">
      <div class="brand">
        <img src="/static/logo.png" class="logo" onerror="this.style.display='none'; this.nextElementSibling.style.display='grid';">
        <div class="brand-badge" style="display:none;">✚</div>
        <div>
          <h1>NurseValue</h1>
          <p>Pay. Protect. Retain.</p>
        </div>
      </div>
      <div class="nav-links">
        <a href="#services" class="ghost-btn">Services</a>
        <a href="#products" class="ghost-btn">Products</a>
        <a href="#mission" class="ghost-btn">Mission</a>
        <a href="#signup" class="btn">Nurses, sign up today</a>
      </div>
    </div>
  </div>

  <main>
    <section class="hero">
      <div class="container hero-grid">
        <div class="reveal visible">
          <div class="eyebrow">Built from care, urgency, and a refusal to stay silent</div>
          <h2 class="headline">
            The platform that makes <span class="gradient-text">nurse value</span> impossible to ignore.
          </h2>
          <p class="hero-copy">
            NurseValue is a bold public-interest platform built to expose underpayment, reveal staffing pressure,
            track retention risk, and arm nurses with transparent data that can push governments, major institutions,
            professional bodies, and the wider public toward better decisions.
          </p>
          <div class="cta-row">
            <a href="/demo" class="btn glow-btn">Try NurseValue →</a>
            <a href="#signup" class="btn">Join the movement</a>
            <a href="#mission" class="ghost-btn">See our mission</a>
          </div>
          <div class="micro-note">
            We care deeply about this issue. This is not just a website. It is pressure, clarity, and momentum.
          </div>

          <div class="stats">
            <div class="stat">
              <div class="value">1 mission</div>
              <div class="label">Make underpayment visible and force action with public, transparent evidence.</div>
            </div>
            <div class="stat">
              <div class="value">24/7</div>
              <div class="label">Visibility into pay, burnout, retention, and the cost of losing experienced nurses.</div>
            </div>
            <div class="stat">
              <div class="value">Global</div>
              <div class="label">Compare nurse value across countries, specialties, bands, and experience levels.</div>
            </div>
          </div>
        </div>

        <div class="panel reveal">
          <div class="panel-top">
            <div>
              <div class="panel-kicker">Live concept panel</div>
              <div class="panel-title">Nurse retention pressure</div>
            </div>
            <div class="status-chip">Actionable intelligence</div>
          </div>

          <div class="progress-card">
            <div class="row-between">
              <span>Ward stress level</span>
              <strong>High</strong>
            </div>
            <div class="bar"><div class="bar-fill"></div></div>
          </div>

          <div class="mini-grid">
            <div class="dual-mini">
              <div style="color:#94a3b8;">Estimated pay gap</div>
              <strong>£8.2k</strong>
              <div style="color:#cbd5e1;">Average annual difference versus stronger international markets.</div>
            </div>
            <div class="dual-mini">
              <div style="color:#94a3b8;">Likely exits</div>
              <strong>31%</strong>
              <div style="color:#cbd5e1;">Projected retention risk if pressure and underpayment continue.</div>
            </div>
          </div>

          <div class="insight-card" style="margin-top:14px; background: rgba(240,171,252,0.10); border-color: rgba(240,171,252,0.18);">
            <div style="color:#f5d0fe; font-size:0.92rem; font-weight:800;">Decision insight</div>
            <div style="margin-top:8px; font-size:1.06rem; line-height:1.7; color:#f8fafc; font-weight:700;">
              In many settings, preventing nurse loss costs less than replacing the people the system already depends on.
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="services" class="section">
      <div class="container reveal">
        <div class="section-kicker">What we do</div>
        <div class="section-title">Services designed to expose problems and move systems.</div>
        <p class="section-copy">
          NurseValue exists to create pressure where pressure is needed. We do not hide behind vague language.
          We produce transparent data, accessible comparisons, and workforce insight that can help nurses,
          inform the public, support negotiators, challenge complacency, and put serious pressure on the people and institutions with power.
        </p>

        <div class="cards-3">
          <div class="card">
            <div class="icon">💷</div>
            <h3>Pay transparency</h3>
            <p>
              Show nurses exactly how their pay compares across countries, regions, bands, and specialties,
              so underpayment becomes measurable instead of invisible.
            </p>
          </div>
          <div class="card">
            <div class="icon">🧠</div>
            <h3>Burnout and risk visibility</h3>
            <p>
              Surface early warning signs around staffing pressure, overload, retention risk, and the environments most likely to lose talent.
            </p>
          </div>
          <div class="card">
            <div class="icon">📊</div>
            <h3>Pressure through evidence</h3>
            <p>
              Build public-facing evidence strong enough to shape conversations with governments, health systems, unions,
              and professional bodies.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section id="products" class="section">
      <div class="container reveal">
        <div class="section-kicker">Products</div>
        <div class="section-title">A full platform, not just a pretty page.</div>
        <p class="section-copy">
          This vision can grow into a serious intelligence platform for nurses and healthcare systems.
          The public-facing experience builds trust. The product layer drives change.
        </p>

        <div class="products-grid">
          <div class="card">
            <div class="icon">🌍</div>
            <h3>NurseValue Compare</h3>
            <p>A global salary and role comparison dashboard that lets nurses see their true market value in seconds.</p>
            <ul>
              <li>Country and region comparisons</li>
              <li>Specialty and seniority breakdowns</li>
              <li>Visible underpayment scores</li>
            </ul>
          </div>

          <div class="card">
            <div class="icon">🏥</div>
            <h3>Retention intelligence</h3>
            <p>A workforce analytics layer for understanding where shortages, exits, and pressure are building fastest.</p>
            <ul>
              <li>Staffing pressure signals</li>
              <li>Exit risk and burnout trend mapping</li>
              <li>High-cost turnover alerts</li>
            </ul>
          </div>

          <div class="card">
            <div class="icon">📣</div>
            <h3>Public evidence hub</h3>
            <p>A transparent public-facing dashboard for turning hidden workforce pain into visible evidence.</p>
            <ul>
              <li>Readable charts and headline figures</li>
              <li>Campaign-ready statistics</li>
              <li>Data that can inform public debate</li>
            </ul>
          </div>

          <div class="card">
            <div class="icon">🤝</div>
            <h3>Advocacy support tools</h3>
            <p>Evidence packs that can strengthen campaigns, raise awareness, and sharpen the pressure placed on decision-makers.</p>
            <ul>
              <li>Negotiation support data</li>
              <li>Retention cost summaries</li>
              <li>Policy-facing insight</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section id="mission" class="section">
      <div class="container reveal">
        <div class="section-kicker">Our mission</div>
        <div class="section-title">Built from conviction. Powered by transparency.</div>

        <div class="vision-grid">
          <div class="big-vision">
            <p class="section-copy" style="max-width:none; margin-top:0;">
              We deeply care about the reality nurses face: the pressure, the exhaustion, the sense of being undervalued,
              and the silence around what that really costs. NurseValue exists because this issue deserves more than sympathy.
              It deserves clarity, evidence, and a platform powerful enough to shift the conversation.
            </p>
            <div class="quote">
              “We want to turn underpayment from a hidden frustration into something visible, undeniable, and impossible to brush aside.”
            </div>
            <div class="tag-row">
              <span class="tag">Public transparency</span>
              <span class="tag">Nurse-first design</span>
              <span class="tag">Retention insight</span>
              <span class="tag">Pressure for change</span>
            </div>
          </div>

          <div class="side-message">
            <div class="section-kicker" style="color:#f5d0fe;">Who we aim to influence</div>
            <p class="section-copy" style="max-width:none; margin-top:10px;">
              Governments. Health systems. Large employers. Professional institutions. Public debate. And yes,
              where appropriate, unions and major nursing bodies too. The goal is not noise for the sake of noise.
              The goal is focused pressure backed by data that people can see and understand.
            </p>
            <div class="card" style="padding:18px; margin-top:18px; border-radius:22px; background: rgba(110,231,183,0.08);">
              <h3 style="margin:0 0 8px; font-size:1.1rem;">Personal promise</h3>
              <p style="margin:0;">
                We are building this because we believe nurses deserve to be seen properly, valued properly, and defended with something stronger than empty words.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container reveal">
        <div class="section-kicker">Why it matters</div>
        <div class="section-title">What NurseValue can change.</div>
        <p class="section-copy">
          This platform is designed to shift attention from vague outrage to concrete evidence. That is where change gets traction.
        </p>

        <div class="impact-grid">
          <div class="card">
            <div class="icon">🔍</div>
            <h3>Make the invisible visible</h3>
            <p>Expose pay gaps, staffing strain, and retention risk in a form that nurses and the public can actually use.</p>
          </div>
          <div class="card">
            <div class="icon">⚖️</div>
            <h3>Strengthen accountability</h3>
            <p>Make it harder for decision-makers to ignore the cost of underpaying and overstretching the workforce.</p>
          </div>
          <div class="card">
            <div class="icon">🚀</div>
            <h3>Ignite momentum</h3>
            <p>Give people a rallying point: a platform that feels ambitious, credible, and emotionally real from day one.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="signup" class="section">
      <div class="container reveal">
        <div class="signup-box">
          <div class="section-kicker" style="color:#cffafe;">Join NurseValue</div>
          <div class="section-title" style="margin-top:10px; font-size: clamp(2rem, 4vw, 3.6rem);">Nurses, sign up today.</div>
          <p class="section-copy" style="max-width:900px;">
            Be part of the first wave. Help build the data, shape the movement, and give this platform the nurse voices it needs.
            Your sign-up is not just interest. It is signal.
          </p>

          <form class="form-grid" onsubmit="event.preventDefault(); document.getElementById('thanks').style.display='block';">
            <input type="text" placeholder="Your name" aria-label="Your name">
            <input type="email" placeholder="Email address" aria-label="Email address">
            <select aria-label="Role">
              <option selected>Nurse / Midwife / Supporter</option>
              <option>Registered Nurse</option>
              <option>Student Nurse</option>
              <option>Nurse Leader</option>
              <option>Healthcare Supporter</option>
            </select>
            <button class="submit-btn" type="submit">Count me in</button>
          </form>

          <div id="thanks" style="display:none; margin-top:16px; color:#d1fae5; font-weight:800;">
            Thank you — this is where movements begin.
          </div>

          <div class="small-muted">
            Demo sign-up only. You can later connect this to a real database, mailing list, or waitlist form.
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container reveal">
      <div class="footer-card">
        <div class="section-kicker" style="color:#e2e8f0;">NurseValue</div>
        <h2>Built to blow minds. Built to move hearts. Built to push change.</h2>
        <p>
          This is the kind of idea that can start as a beautiful landing page and grow into a serious force.
          Show it. Share it. Build it. Make people feel what it could become.
        </p>
        <div class="cta-row" style="justify-content:center; margin-top:24px;">
          <a href="/demo" class="btn glow-btn">Try NurseValue →</a>
          <a href="#services" class="ghost-btn">Explore the platform</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.12 });

    document.querySelectorAll('.reveal').forEach((el, index) => {
      if (!el.classList.contains('visible')) {
        el.style.transitionDelay = `${index * 60}ms`;
      }
      observer.observe(el);
    });
  </script>
</body>
</html>
"""

DEMO_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>NurseValue Demo</title>
<style>
body {
  font-family: Arial;
  background:#020617;
  color:white;
  padding:40px;
}

.box {
  background:rgba(255,255,255,0.05);
  padding:25px;
  border-radius:20px;
  max-width:700px;
  margin:auto;
}

input, select {
  width:100%;
  padding:12px;
  margin-top:10px;
  border-radius:10px;
  border:none;
}

button {
  margin-top:15px;
  padding:12px;
  width:100%;
  background:white;
  color:black;
  font-weight:bold;
  border-radius:10px;
  cursor:pointer;
}

.section {
  margin-top:25px;
  padding:18px;
  background:rgba(255,255,255,0.08);
  border-radius:15px;
}

.result {
  margin-top:20px;
  padding:18px;
  background:rgba(255,255,255,0.12);
  border-radius:15px;
}

h1, h2, h3 {
  margin-bottom:10px;
}

hr {
  border:0;
  height:1px;
  background:rgba(255,255,255,0.2);
  margin:15px 0;
}

.back-link {
  display:inline-block;
  margin-bottom:20px;
  color:#93c5fd;
}
</style>
</head>

<body>
<a class="back-link" href="/">← Back to NurseValue</a>

<div class="box">

<h1>NurseValue</h1>
<p>No signup. No friction. Just truth.</p>

<h2>👤 Your Personal Reality</h2>

<form method="POST">
<select name="band">
<option>Band 5</option>
<option>Band 6</option>
<option>Band 7</option>
</select>

<input name="salary" placeholder="Your salary (£)" required>

<button type="submit">Reveal My Value</button>
</form>

{% if result %}
<div class="result">
<h3>Your Result</h3>

<p><b>Your salary:</b> £{{salary}}</p>
<p><b>Global average:</b> £{{global_avg}}</p>
<p><b>Pay gap:</b> {{gap}}%</p>

<hr>

<p><b>Insight:</b></p>
<p>{{insight}}</p>

<hr>

<p><b>What this means:</b></p>
<p>If many nurses are in the same position, the system is losing value every single year.</p>
</div>
{% endif %}

<h2>🏥 What This Means For a Hospital</h2>

<div class="section">
<p><b>Example hospital:</b> 500 nurses</p>
<p>Average NHS salary: £32,000</p>
<p>Global benchmark: £45,000</p>

<hr>

<p><b>Underpayment per nurse:</b> ~£13,000</p>
<p><b>Total annual gap:</b> £6,500,000</p>

<hr>

<p><b>Estimated exits (20%):</b> 100 nurses</p>
<p><b>Replacement cost per nurse:</b> £25,000</p>
<p><b>Total replacement cost:</b> £2,500,000</p>

<hr>

<p><b>Alternative approach:</b></p>
<p>Increase pay by £5,000 → cost = £2,500,000</p>

<hr>

<p><b>Insight:</b></p>
<p>💡 Paying nurses more can cost the SAME as replacing them — but keeps experience, stability, and patient safety.</p>
</div>

<h2>📊 Workforce Snapshot (100 Nurses)</h2>

<div class="section">
<p><b>Sample group:</b> 100 nurses</p>

<ul>
<li>Band 5: 60 nurses (£28k avg)</li>
<li>Band 6: 30 nurses (£35k avg)</li>
<li>Band 7: 10 nurses (£43k avg)</li>
</ul>

<hr>

<p><b>Global equivalents:</b></p>
<ul>
<li>Band 5: £47k</li>
<li>Band 6: £60k</li>
<li>Band 7: £72k</li>
</ul>

<hr>

<p><b>Average underpayment:</b> ~35%</p>
<p><b>Total annual gap (100 nurses):</b> ≈ £1.5M – £2M</p>

<hr>

<p><b>Estimated exits:</b> 15–25 nurses</p>
<p><b>Replacement cost:</b> £375k – £625k</p>

<hr>

<p><b>Insight:</b></p>
<p>This is not a small issue. Across even 100 nurses, the financial and human impact is massive.</p>
</div>

<h2>📖 Case Study</h2>

<div class="section">
<p><b>Scenario:</b> NHS Trust under pressure</p>

<ul>
<li>High burnout</li>
<li>Staff leaving internationally</li>
<li>Heavy reliance on agency staff</li>
</ul>

<hr>

<p><b>Without NurseValue:</b></p>
<p>Problems are felt — but not clearly measured.</p>

<p><b>With NurseValue:</b></p>
<ul>
<li>Clear pay gap visibility</li>
<li>Retention risk measurable</li>
<li>Cost of inaction quantified</li>
</ul>

<hr>

<p><b>Impact:</b></p>
<p>Better decisions. Stronger negotiations. Public awareness.</p>
</div>

</div>
</body>
</html>
"""

def get_global_average(band):
    data = {
        "Band 5": int((47000 + 50000) / 2),
        "Band 6": int((60000 + 65000) / 2),
        "Band 7": int((72000 + 80000) / 2),
    }
    return data[band]

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/demo", methods=["GET", "POST"])
def demo():
    if request.method == "POST":
        try:
            salary = int(request.form["salary"])
        except ValueError:
            salary = 0

        band = request.form["band"]

        # UK averages
        uk_data = {
            "Band 5": 28000,
            "Band 6": 35000,
            "Band 7": 43000
        }

        # US averages
        us_data = {
            "Band 5": 50000,
            "Band 6": 65000,
            "Band 7": 80000
        }

        # Australia averages
        aus_data = {
            "Band 5": 47000,
            "Band 6": 60000,
            "Band 7": 72000
        }

        uk_avg = uk_data[band]
        us_avg = us_data[band]
        aus_avg = aus_data[band]

        us_gap = us_avg - salary
        aus_gap = aus_avg - salary

        us_percent = int((us_gap / us_avg) * 100)
        aus_percent = int((aus_gap / aus_avg) * 100)

        abs_gap = int((us_gap + aus_gap) / 2)

        if us_percent > 30:
            position = "Significantly underpaid globally"
            retention = "High risk of leaving"
            insight = "You are far below international benchmarks."
        elif us_percent > 10:
            position = "Moderately underpaid"
            retention = "Medium risk"
            insight = "You may be underpaid depending on conditions."
        else:
            position = "Competitive"
            retention = "Low risk"
            insight = "Your pay is relatively competitive."

        return render_template(
            "demo.html",
            result=True,
            salary=salary,
            uk_avg=uk_avg,
            us_avg=us_avg,
            aus_avg=aus_avg,
            us_gap=us_gap,
            aus_gap=aus_gap,
            us_percent=us_percent,
            aus_percent=aus_percent,
            abs_gap=abs_gap,
            position=position,
            retention=retention,
            insight=insight,
        )

    return render_template("demo.html", result=False)

if __name__ == "__main__":
    app.run(debug=True)
