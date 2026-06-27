# 🤖 Digital Twin — Agent IA Personnel

> Un jumeau numérique propulsé par GPT-4o-mini qui répond à ta place, capture les contacts et te notifie en temps réel.

**Démo live :** [godwill-digital-twin.hf.space](https://huggingface.co/spaces/TON_USERNAME/digital-twin) 

---

## ✨ Ce que c'est

Ce projet est un **agent IA personnel** qui joue le rôle de ton représentant numérique.

- 💬 Répond aux questions sur ton profil, tes compétences, tes projets
- 🎯 Reste 100% fidèle à ton CV, aucune invention, aucune extrapolation
- 📬 Capture les contacts des visiteurs intéressés (recruteurs, partenaires, collaborateurs)
- 🔔 T'envoie une notification Pushover instantanée avec le contexte complet
- 🌍 Répond dans la langue de l'utilisateur automatiquement

> ⚠️ **Point important** : le design de l'interface (CSS, layout, animations) a été entièrement généré par Claude (Anthropic). Je ne suis pas designer, j'ai décrit ce que je voulais, Claude a produit le code visuel. Le reste (architecture agent, logique, prompts, déploiement) c'est du mien.

---

## 🏗️ Architecture

```
digital-twin/
├── main.py              # Point d'entrée
├── chat.py              # Interface Gradio
├── agent.py             # Logique agent + tools
├── system_prompt.py     # Prompt système
├── style.py             # UI (CSS, HTML, profil)
├── cv.pdf               # Ton CV (non versionné)
├── summary.txt          # Ton résumé personnel
├── .env                 # Clés API (non versionné)
├── pyproject.toml       # Dépendances (uv)
└── README.md
```

---

## 🚀 Déploiement rapide — Pour toi-même

### 1. Clone et installe

```bash
git clone https://github.com/Alex171-studo/Digital-Twin
cd digital-twin
uv sync
```

### 2. Configure ton `.env`

```env
OPENAI_API_KEY=sk-...
PUSHOVER_TOKEN=...
PUSHOVER_USER=...
```

### 3. Ajoute tes fichiers personnels

- Dépose ton **CV en PDF** → `cv.pdf`
- Crée ton **résumé personnel** → `summary.txt`

Le résumé doit contenir : ta formation, tes compétences, tes expériences, tes projets, tes objectifs, ta personnalité. Plus c'est précis, plus l'agent est fidèle.

### 4. Lance

```bash
uv run main.py
```

---

## 🎯 Guide — Adapte-le à TON profil

Tu veux utiliser ce projet pour **ton propre site ou portfolio** ? C'est exactement fait pour ça.

### Étape 1 — Personnalise `style.py`

```python
def get_profile() -> dict:
    return {
        "name": "Ton Nom Complet",
        "avatar_url": "https://api.dicebear.com/7.x/avataaars/svg?seed=TonPrenom",
        "linkedin": "https://linkedin.com/in/ton-profil",
        "github": "https://github.com/ton-username",
        "portfolio": "https://ton-site.com",
        "email": "ton@email.com",
    }
```

Change aussi le message d'accueil dans `get_initial_message()` pour qu'il te ressemble.

### Étape 2 — Remplace le CV et le résumé

- `cv.pdf` → ton propre CV
- `summary.txt` → ton propre résumé (voir format ci-dessous)

**Format recommandé pour `summary.txt` :**

```
[Ton prénom] est étudiant/professionnel en [domaine], basé à [ville].

Formation :
- ...

Compétences techniques :
- ...

Expériences :
- ...

Objectifs actuels :
- ...

Personnalité :
- ...

Règle importante : toute information absente de ce résumé doit être traitée comme inconnue.
```

### Étape 3 — Configure les notifications

Crée un compte sur [pushover.net](https://pushover.net), récupère ton token et ton user key, et mets-les dans `.env`.

Tu recevras une notification à chaque fois qu'un visiteur laisse ses coordonnées, avec le contexte complet de la conversation.

### Étape 4 — Déploie sur Hugging Face Spaces

1. Crée un Space sur [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choisis **Gradio** comme SDK
3. Dans les **Settings > Secrets**, ajoute :
   - `OPENAI_API_KEY`
   - `PUSHOVER_TOKEN`
   - `PUSHOVER_USER`
4. Upload tous les fichiers **sauf** `.env` (les secrets sont gérés par HF)
5. Assure-toi que ton `pyproject.toml` liste bien toutes les dépendances

> 💡 `cv.pdf` et `summary.txt` peuvent être uploadés directement dans le Space — ils ne contiennent pas de clés sensibles.

---

## 📦 Dépendances

Gérées avec **[uv](https://github.com/astral-sh/uv)** :

```toml
[project]
name = "digital-twin"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "openai",
    "gradio",
    "pypdf",
    "python-dotenv",
    "requests",
]
```

---

## 🔔 Format des notifications Pushover

```
👤 Nouveau contact
━━━━━━━━━━━━━━━
Nom     : Jean Dupont
Email   : jean@gmail.com
━━━━━━━━━━━━━━━
Contexte: Recruteur intéressé par un contrat d'alternance en IA.
          A posé une question sur les certifications (non disponible).
          Souhaite fixer un appel cette semaine.
```

---

## 🛠️ Stack technique

| Composant | Technologie |
|-----------|-------------|
| LLM | GPT-4o-mini (OpenAI) |
| Interface | Gradio |
| Gestion des deps | uv |
| Notifications | Pushover |
| Extraction CV | pypdf |
| Déploiement | Hugging Face Spaces |

---

## 👤 Auteur

**Godwill Alexis AGUEMON**
Alternant Cycle Ingénieur — Agentic AI & Automation — ESIGELEC

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Godwill-blue)](https://linkedin.com/in/godwill-alexis-aguemon)
[![GitHub](https://img.shields.io/badge/GitHub-Alex171--studo-black)](https://github.com/Alex171-studo)
[![Portfolio](https://img.shields.io/badge/Portfolio-alex171--studo.github.io-purple)](https://alex171-studo.github.io)

---

*Ce projet est open-source. Si tu l'utilises ou t'en inspires, un crédit ou une étoile ⭐ est toujours apprécié.*