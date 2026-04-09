export default function NurseBoxWebsite() {
  const stats = [
    { value: '1 mission', label: 'Fix nurse underpayment with data' },
    { value: '24/7', label: 'Visibility into pay, burnout, and retention' },
    { value: 'Global', label: 'Compare value across countries and roles' },
  ];

  const features = [
    {
      title: 'Know your true value',
      text: 'NurseBox helps nurses see how their pay compares across countries, specialties, and experience levels.',
      icon: '💷',
    },
    {
      title: 'Spot burnout early',
      text: 'Flag staffing pressure, overload, and retention risk before skilled nurses walk away.',
      icon: '🧠',
    },
    {
      title: 'Push better decisions',
      text: 'Turn underpayment and shortages into clear evidence that hospitals and governments cannot ignore.',
      icon: '📊',
    },
  ];

  const pillars = [
    'Pay transparency',
    'Retention intelligence',
    'Burnout prediction',
    'Workforce planning',
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white overflow-x-hidden">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(59,130,246,0.18),transparent_35%),radial-gradient(circle_at_80%_20%,rgba(16,185,129,0.16),transparent_28%),radial-gradient(circle_at_20%_80%,rgba(236,72,153,0.12),transparent_26%)]" />

      <main className="relative mx-auto max-w-7xl px-6 py-8 md:px-10 lg:px-12">
        <header className="flex items-center justify-between rounded-3xl border border-white/10 bg-white/5 px-5 py-4 backdrop-blur-xl shadow-2xl">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-br from-cyan-400 to-blue-600 text-xl shadow-lg shadow-cyan-500/20">
              ✚
            </div>
            <div>
              <div className="text-2xl font-black tracking-tight">NurseBox</div>
              <div className="text-xs uppercase tracking-[0.3em] text-cyan-200/80">Pay. Protect. Retain.</div>
            </div>
          </div>
          <div className="hidden md:flex items-center gap-3 text-sm text-slate-200">
            <span className="rounded-full border border-cyan-400/30 bg-cyan-400/10 px-4 py-2">Built to solve nurse shortages</span>
          </div>
        </header>

        <section className="grid items-center gap-10 py-16 md:grid-cols-2 md:py-24">
          <div>
            <div className="mb-4 inline-flex items-center rounded-full border border-emerald-400/20 bg-emerald-400/10 px-4 py-2 text-sm text-emerald-200">
              The future of nurse pay intelligence
            </div>
            <h1 className="max-w-3xl text-5xl font-black leading-[0.95] tracking-tight md:text-7xl">
              The website that makes <span className="bg-gradient-to-r from-cyan-300 via-blue-400 to-fuchsia-400 bg-clip-text text-transparent">NurseBox</span> feel real.
            </h1>
            <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-300 md:text-xl">
              NurseBox is a bold platform idea designed to expose nurse underpayment, predict burnout, and give healthcare systems the evidence they need to make better staffing and pay decisions.
            </p>

            <div className="mt-8 flex flex-wrap gap-4">
              <a
                href="#features"
                className="rounded-2xl bg-white px-6 py-3 text-base font-semibold text-slate-950 shadow-xl transition hover:-translate-y-0.5"
              >
                Explore NurseBox
              </a>
              <a
                href="#vision"
                className="rounded-2xl border border-white/15 bg-white/5 px-6 py-3 text-base font-semibold text-white backdrop-blur transition hover:bg-white/10"
              >
                See the vision
              </a>
            </div>

            <div className="mt-10 grid gap-4 sm:grid-cols-3">
              {stats.map((stat) => (
                <div key={stat.label} className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg backdrop-blur">
                  <div className="text-2xl font-black text-cyan-300">{stat.value}</div>
                  <div className="mt-2 text-sm leading-6 text-slate-300">{stat.label}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="relative">
            <div className="absolute -inset-6 rounded-[2rem] bg-gradient-to-br from-cyan-500/20 via-blue-500/10 to-fuchsia-500/20 blur-2xl" />
            <div className="relative rounded-[2rem] border border-white/10 bg-slate-900/80 p-6 shadow-2xl backdrop-blur-2xl">
              <div className="mb-5 flex items-center justify-between">
                <div>
                  <div className="text-sm font-medium text-slate-400">Live concept panel</div>
                  <div className="text-2xl font-bold">Nurse retention risk</div>
                </div>
                <div className="rounded-2xl bg-emerald-400/10 px-4 py-2 text-sm font-semibold text-emerald-300">Actionable insight</div>
              </div>

              <div className="space-y-4">
                <div className="rounded-3xl border border-cyan-400/20 bg-cyan-400/10 p-5">
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-cyan-100">Ward stress level</span>
                    <span className="text-sm font-semibold text-cyan-200">High</span>
                  </div>
                  <div className="mt-4 h-3 rounded-full bg-white/10">
                    <div className="h-3 w-[78%] rounded-full bg-gradient-to-r from-cyan-300 to-blue-500" />
                  </div>
                </div>

                <div className="grid gap-4 sm:grid-cols-2">
                  <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
                    <div className="text-sm text-slate-400">Estimated pay gap</div>
                    <div className="mt-2 text-4xl font-black">£8.2k</div>
                    <div className="mt-2 text-sm text-slate-300">Average annual difference versus stronger international markets.</div>
                  </div>
                  <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
                    <div className="text-sm text-slate-400">Likely exits in 12 months</div>
                    <div className="mt-2 text-4xl font-black">31%</div>
                    <div className="mt-2 text-sm text-slate-300">Retention risk if staffing pressure and pay mismatch continue.</div>
                  </div>
                </div>

                <div className="rounded-3xl border border-fuchsia-400/20 bg-fuchsia-400/10 p-5">
                  <div className="text-sm text-fuchsia-200">Decision insight</div>
                  <div className="mt-2 text-lg font-semibold">
                    Increasing targeted pay support could cost less than replacing experienced nurses at scale.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="features" className="py-10 md:py-16">
          <div className="mb-8 flex items-end justify-between gap-4">
            <div>
              <div className="text-sm uppercase tracking-[0.25em] text-slate-400">Why it matters</div>
              <h2 className="mt-2 text-3xl font-black md:text-5xl">A serious idea with real-world impact</h2>
            </div>
          </div>

          <div className="grid gap-6 md:grid-cols-3">
            {features.map((feature) => (
              <div
                key={feature.title}
                className="group rounded-[2rem] border border-white/10 bg-white/5 p-7 shadow-xl backdrop-blur-xl transition duration-300 hover:-translate-y-1 hover:bg-white/10"
              >
                <div className="text-4xl">{feature.icon}</div>
                <h3 className="mt-5 text-2xl font-bold">{feature.title}</h3>
                <p className="mt-4 text-base leading-7 text-slate-300">{feature.text}</p>
              </div>
            ))}
          </div>
        </section>

        <section id="vision" className="grid gap-6 py-10 md:grid-cols-[1.1fr_0.9fr] md:py-16">
          <div className="rounded-[2rem] border border-white/10 bg-gradient-to-br from-white/8 to-white/5 p-8 shadow-xl backdrop-blur-xl">
            <div className="text-sm uppercase tracking-[0.25em] text-cyan-300">The vision</div>
            <h2 className="mt-3 text-3xl font-black md:text-5xl">A platform built to make underpayment impossible to ignore</h2>
            <p className="mt-6 max-w-3xl text-lg leading-8 text-slate-300">
              NurseBox brings together nurse salary comparison, staffing risk signals, and retention intelligence in one place. It is not just a website. It is a pressure system for better decisions.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              {pillars.map((pill) => (
                <span
                  key={pill}
                  className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-200"
                >
                  {pill}
                </span>
              ))}
            </div>
          </div>

          <div className="rounded-[2rem] border border-white/10 bg-slate-900/70 p-8 shadow-xl backdrop-blur-xl">
            <div className="text-sm uppercase tracking-[0.25em] text-fuchsia-300">One sentence</div>
            <div className="mt-4 text-3xl font-black leading-tight">
              NurseBox helps nurses understand their true value and gives healthcare systems the evidence to improve pay and staffing.
            </div>
            <div className="mt-8 rounded-3xl border border-emerald-400/20 bg-emerald-400/10 p-5">
              <div className="text-sm text-emerald-200">Why your partner should love this</div>
              <div className="mt-2 text-base leading-7 text-white/90">
                It looks premium, feels modern, and turns your idea into something that already feels like a real startup.
              </div>
            </div>
          </div>
        </section>

        <section className="py-10 md:py-16">
          <div className="rounded-[2.25rem] border border-white/10 bg-gradient-to-r from-cyan-500/15 via-blue-500/10 to-fuchsia-500/15 p-8 text-center shadow-2xl backdrop-blur-xl md:p-12">
            <div className="text-sm uppercase tracking-[0.3em] text-slate-300">NurseBox</div>
            <h2 className="mt-3 text-4xl font-black md:text-6xl">Built from your idea. Ready to show off.</h2>
            <p className="mx-auto mt-5 max-w-2xl text-lg leading-8 text-slate-300">
              A powerful concept deserves a website that feels ambitious, emotional, and unforgettable.
            </p>
          </div>
        </section>
      </main>
    </div>
  );
}
