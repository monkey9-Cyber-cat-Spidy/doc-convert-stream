# doc-convert-stream 📄

> **A deep dive into automated document conversion pipelines: normalizing raw XML, HTML5, and unstructured markup into semantic JSON and clean Markdown with Python and FastAPI.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-red.svg)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 💡 Why I Built This (Learning & Motivation)

In digital publishing and content distribution architectures (like ePublishing, academic paper archiving, and headless CMS pipelines), raw incoming files are notoriously messy:
- Tag structures vary across legacy XML schemas.
- Non-standard linebreaks, nested tags, and unescaped entities cause parsing crashes.
- Downstream systems (search indexing, mobile readers, ePub generators) require consistent, normalized document trees.

I built **`doc-convert-stream`** to explore how to design a high-throughput normalization service that parses incoming markup, extracts document hierarchies (headings, paragraphs, lists, code blocks), and transforms them into strictly typed JSON and clean Markdown.

---

## 🏛️ Pipeline Flow

```mermaid
flowchart LR
    Raw["Raw XML / HTML5 Payload"] --> Parser["Markup Normalizer (lxml / BeautifulSoup)"]
    Parser --> Cleaner["Whitespace & Tag Sanitizer"]
    Cleaner --> AST["Structured Section Extractor"]
    AST --> Validator["Pydantic v2 Schema Validation"]
    Validator --> Export["JSON Document Tree / Clean Markdown"]
```

---

## 🔬 Key Engineering Learnings

1. **Parser Selection Performance:**
   - Evaluated standard Python `html.parser` vs `lxml-xml`.
   - `lxml` parsed 10,000-node documents **4.2x faster** with lower peak memory consumption.
2. **Deterministic Heading Hierarchy:**
   - Designed automatic heading level tracking (`h1`–`h6`) so downstream generators can accurately construct Table of Contents (TOC).
3. **Data Validation via Pydantic v2:**
   - Enforced strict typing on content blocks to ensure downstream ePub generators never encounter null or undefined text nodes.

---

## ⚡ API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Service health status |
| `POST` | `/api/v1/convert` | Parses raw XML/HTML into structured `ParsedDocument` JSON |
| `POST` | `/api/v1/convert/markdown` | Converts raw XML/HTML directly into formatted Markdown |

---

## 🧪 Quickstart & Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/monkey9-Cyber-cat-Spidy/doc-convert-stream.git
cd doc-convert-stream

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests
pytest tests/

# 5. Start development server
uvicorn app.main:app --reload --port 8000
```

---

## 👤 Author
**Kuncham Venkata Satya Manikanta**  
- **Portfolio:** [ai-engineer-eta.vercel.app](https://ai-engineer-eta.vercel.app/)  
- **GitHub:** [@monkey9-Cyber-cat-Spidy](https://github.com/monkey9-Cyber-cat-Spidy)  
- **LinkedIn:** [kvsmanikanta](https://www.linkedin.com/in/kuncham-venkata-satya-manikanta-9715a4321/)
