# style.py

def get_profile() -> dict:
    return  {
        "name": "Godwill Alexis AGUEMON",
        "avatar_url": "https://api.dicebear.com/7.x/avataaars/svg?seed=Godwill&backgroundColor=1a1a2e",
        "linkedin": "https://linkedin.com/in/godwill-alexis-aguemon",
        "github": "https://github.com/Alex171-studo",
        "portfolio": "https://alex171-studo.github.io",
        "email": "godwillaguemonbg@gmail.com",
    }

#========================================================================================================================================================================

def get_css() -> str:
    return """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg-primary: #0a0a14;
    --bg-card: #111128;
    --bg-input: #0d0d22;
    --border: #2a2a5a;
    --neon-purple: #8b5cf6;
    --neon-violet: #a78bfa;
    --neon-pink: #ec4899;
    --neon-cyan: #22d3ee;
    --text-primary: #f0f0ff;
    --text-secondary: #9090bb;
    --text-muted: #5050aa;
    --glow: 0 0 20px rgba(139,92,246,0.35);
}

* { box-sizing: border-box; }

body, .gradio-container {
    background: var(--bg-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text-primary) !important;
    min-height: 100vh;
}

.hero-header {
    background: linear-gradient(135deg, #0a0a14 0%, #130d2e 50%, #0a0a14 100%);
    border-bottom: 1px solid var(--border);
    padding: 28px 32px 24px;
    position: relative;
    overflow: hidden;
}

.hero-header::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    background: radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%);
    pointer-events: none;
}

.profile-row { display: flex; align-items: center; gap: 20px; margin-bottom: 20px; }
.avatar-wrap { position: relative; flex-shrink: 0; }

.avatar-ring {
    width: 72px; height: 72px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--neon-purple), var(--neon-pink), var(--neon-cyan));
    padding: 2px;
    box-shadow: var(--glow);
    animation: ring-pulse 3s ease-in-out infinite;
}

@keyframes ring-pulse {
    0%, 100% { box-shadow: 0 0 15px rgba(139,92,246,0.4); }
    50%       { box-shadow: 0 0 35px rgba(139,92,246,0.7), 0 0 60px rgba(236,72,153,0.2); }
}

.avatar-ring img { width: 100%; height: 100%; border-radius: 50%; background: var(--bg-primary); }

.status-dot {
    position: absolute; bottom: 3px; right: 3px;
    width: 14px; height: 14px;
    background: #22c55e;
    border-radius: 50%;
    border: 2px solid var(--bg-primary);
    animation: blink 2s ease-in-out infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.4; }
}

.profile-info h1 {
    font-size: 1.35rem; font-weight: 700;
    color: var(--text-primary); margin: 0 0 4px 0;
}

.profile-info h1 span {
    background: linear-gradient(90deg, var(--neon-violet), var(--neon-pink));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

.profile-info .role-tag {
    display: inline-block;
    background: rgba(139,92,246,0.15);
    border: 1px solid rgba(139,92,246,0.35);
    border-radius: 20px; padding: 3px 12px;
    font-size: 0.72rem; font-weight: 500;
    color: var(--neon-violet); letter-spacing: 0.04em;
    text-transform: uppercase; margin-bottom: 5px;
}

.profile-info .subtitle { font-size: 0.82rem; color: var(--text-secondary); margin: 4px 0 0 0; }

.social-links { display: flex; gap: 10px; flex-wrap: wrap; }

.social-btn {
    display: inline-flex; align-items: center; gap: 7px;
    padding: 7px 16px; border-radius: 8px;
    font-size: 0.78rem; font-weight: 600;
    text-decoration: none !important;
    transition: all 0.2s ease; border: 1px solid;
}

.social-btn:hover { transform: translateY(-2px); }

.btn-linkedin { background: rgba(10,102,194,0.15); border-color: rgba(10,102,194,0.5); color: #60a5fa !important; }
.btn-linkedin:hover { background: rgba(10,102,194,0.3); box-shadow: 0 0 15px rgba(10,102,194,0.3); }
.btn-github { background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.2); color: var(--text-primary) !important; }
.btn-github:hover { background: rgba(255,255,255,0.12); }
.btn-portfolio { background: rgba(139,92,246,0.15); border-color: rgba(139,92,246,0.4); color: var(--neon-violet) !important; }
.btn-portfolio:hover { background: rgba(139,92,246,0.3); box-shadow: var(--glow); }

#chatbot {
    background: var(--bg-primary) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}

textarea, input[type="text"] {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.9rem !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s !important;
}

textarea:focus, input[type="text"]:focus {
    border-color: var(--neon-purple) !important;
    box-shadow: 0 0 0 3px rgba(139,92,246,0.15) !important;
    outline: none !important;
}

textarea::placeholder, input::placeholder { color: var(--text-muted) !important; }

button.primary, .gr-button-primary {
    background: linear-gradient(135deg, var(--neon-purple), var(--neon-pink)) !important;
    border: none !important; border-radius: 10px !important;
    color: white !important; font-weight: 600 !important;
    padding: 10px 20px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 15px rgba(139,92,246,0.3) !important;
}

button.primary:hover { transform: translateY(-1px) !important; box-shadow: 0 6px 25px rgba(139,92,246,0.5) !important; }

button.secondary, .gr-button-secondary {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text-secondary) !important;
    transition: all 0.2s ease !important;
}

button.secondary:hover { border-color: var(--neon-purple) !important; color: var(--neon-violet) !important; }


.footer-bar {
    text-align: center; padding: 12px;
    font-size: 0.72rem; color: var(--text-muted);
    border-top: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
}

.footer-bar span { color: var(--neon-purple); }

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--neon-purple); }

footer { display: none !important; }
.built-with { display: none !important; }
"""

#=====================================================================================================================================================================================================

def get_header_html() -> str:
    profile = get_profile()
    return  f"""
    <div class="hero-header">
        <div class="profile-row">
            <div class="avatar-wrap">
                <div class="avatar-ring">
                    <img src="{profile['avatar_url']}" alt="Godwill Avatar" />
                </div>
                <div class="status-dot"></div>
            </div>
            <div class="profile-info">
                <div class="role-tag">⚡ Agentic AI · Automatisation</div>
                <h1>Godwill Alexis <span>AGUEMON</span></h1>
                <p class="subtitle">🎓 1ère année Cycle Ingénieur · A la recherche d'une alternance</p>
            </div>
        </div>
        <div class="social-links">
            <a href="{profile['linkedin']}" target="_blank" class="social-btn btn-linkedin">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
                LinkedIn
            </a>
            <a href="{profile['github']}" target="_blank" class="social-btn btn-github">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
                GitHub
            </a>
            <a href="{profile['portfolio']}" target="_blank" class="social-btn btn-portfolio">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                Portfolio
            </a>
        </div>
    </div>
    """

#==========================================================================================================================================================================================================================================================================================================================================================================================================================

def get_footer_html():
    return """
    <div class="footer-bar">
        Propulsé par <span>GPT-4o-mini</span> · Conçu par <span>Godwill A.</span> · 2025
    </div>
    """

#=============================================================================================================================================================================================================================================================================================================================================================================================================================

def get_initial_message():
    return [
        {
            "role": "assistant",
            "content": "Salut ! 👋 Je suis **Godwill Alexis AGUEMON**, alternant en 1ère année de cycle ingénieur à l'ESIGELEC, passionné par l'IA agentique et l'automatisation.\n\nPose-moi une question — sur mes projets, mes skills, ou si tu veux collaborer ! 🚀"
        }
    ]