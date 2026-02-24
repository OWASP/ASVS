# OWASP ASVS 5.0 — Bilingual Panjabi (pa-IN) Translation

## Peer Review Plan for Security Researchers

**PR:** [#3254](https://github.com/OWASP/ASVS/pull/3254) · **Branch:** `GeeksikhSecurity:panjabi-translation-v5`
**Lead Translator:** Gurvinder Singh ([@GeeksikhSecurity](https://github.com/GeeksikhSecurity))
**Script:** Gurmukhi (ਗੁਰਮੁਖੀ) · **ISO Code:** pa-IN
**Spelling Convention:** "Panjabi" per Sikhri.org and Panjab Digital Library standards
**Co-Author:** Claude Opus 4.6 (AI-assisted translation with human oversight)

---

## What's Been Completed (Phase A)

The following files are committed and ready for review in commit [`aa38595`](https://github.com/OWASP/ASVS/pull/3254/commits/aa38595242a82d9cda4913176f26d22c72585377):

| File | Description | Word Count |
|------|-------------|------------|
| `5.0/pa-IN/0x01-Frontispiece.md` | Bilingual frontispiece — copyright, project leads, contributors | ~400 |
| `5.0/pa-IN/0x02-Preface.md` | Bilingual preface — ASVS 5.0 principles, levels, scope | ~800 |
| `5.0/pa-IN/README.md` | Project README with 100+ term glossary (Gurmukhi + romanization) | ~2,500 |
| `5.0/pa-IN/TRANSLATION-NOTES.md` | QA checklist, phased progress, terminology decisions | ~1,000 |
| `GIT-CHEATSHEET.md` | PR workflow reference for contributors | ~300 |

**Total across 27 planned files:** ~38,372 words (English source)

---

## Translation Format

Every section follows a consistent bilingual pattern for reviewer clarity:

```markdown
## English Heading
## ਪੰਜਾਬੀ ਸਿਰਲੇਖ

English paragraph text here.

ਪੰਜਾਬੀ ਅਨੁਵਾਦ ਇੱਥੇ (with parenthetical English for key terms).
```

Key conventions:
- English paragraph first, Panjabi translation immediately below
- Technical terms preserved in English with Gurmukhi transliteration on first use
- Gurmukhi numerals used for version numbers (e.g., ੫.੦ for 5.0)
- No Devanagari script — all Unicode validated as clean Gurmukhi

---

## Glossary Classification System

Each term in the README glossary is tagged with one of four categories:

| Tag | Meaning | Example |
|-----|---------|---------|
| **T** | Translated | Authentication → ਪ੍ਰਮਾਣੀਕਰਨ |
| **L** | Loan word (transliterated) | API → ਏ.ਪੀ.ਆਈ. |
| **R** | Retained in English | OWASP, SQL, XSS |
| **H** | Hybrid (Panjabi + English) | SQL Injection → SQL ਇੰਜੈਕਸ਼ਨ |

The glossary currently contains 100+ security terms organized by ASVS chapter domain.

---

## What Reviewers Should Look For

### 1. Translation Accuracy

- Does the Panjabi text faithfully convey the security meaning of the English source?
- Are technical nuances preserved (e.g., "verify" vs. "validate" vs. "check")?
- Do the ASVS requirement IDs (e.g., v5.0.0-2.1.7) remain intact and unmodified?

### 2. Terminology Consistency

- Is the same Panjabi term used for the same English concept throughout?
- Does the T/L/R/H classification make sense for each term?
- Are there terms that should be translated differently for the Panjabi security audience?

### 3. Gurmukhi Script Quality

- No Devanagari characters mixed in (common error in Panjabi digital text)
- Proper use of Gurmukhi vowel signs (ਮਾਤਰਾ) and conjuncts
- Clean Unicode — no invisible control characters or zero-width joiners where not needed

### 4. Readability for Panjabi-Speaking Developers

- Would a developer in Punjab (India or Pakistan) understand this without constantly referring to the English?
- Is the sentence structure natural Panjabi, or does it read like a word-for-word transliteration?
- Are parenthetical English terms helpful or excessive?

### 5. Structural & Markdown Integrity

- Bilingual format is consistent (English first, Panjabi below)
- Markdown renders correctly (tables, links, headings, lists)
- Image paths use relative references (`../images/`) for portability

---

## Remaining Phases (B–D)

### Phase B — Core Chapters (Target: March–April 2026)

| File | ASVS Chapter | Priority |
|------|-------------|----------|
| `0x03-Using-ASVS.md` | How to use the standard | High |
| `0x04-Assessment-and-Certification.md` | Assessment guidance | High |
| `0x10-V1-Architecture.md` | V1: Architecture & Threat Modeling | High |
| `0x11-V2-Authentication.md` | V2: Authentication | High |
| `0x12-V3-Session-Management.md` | V3: Session Management | High |
| `0x13-V4-Access-Control.md` | V4: Access Control | High |

### Phase C — Security Requirement Chapters (Target: May–July 2026)

| File | ASVS Chapter |
|------|-------------|
| `0x14-V5-Encoding-Sanitization.md` | V5: Encoding & Sanitization |
| `0x15-V6-Stored-Cryptography.md` | V6: Cryptography |
| `0x16-V7-Error-Logging.md` | V7: Error Handling & Logging |
| `0x17-V8-Data-Protection.md` | V8: Data Protection |
| `0x18-V9-Communication.md` | V9: Communication Security |
| `0x19-V10-Malicious-Code.md` | V10: Malicious Code |
| `0x20-V11-BusLogic.md` | V11: Business Logic |
| `0x21-V12-Files-Resources.md` | V12: Files & Resources |
| `0x22-V13-API-Web-Service.md` | V13: API & Web Service |
| `0x23-V14-Config.md` | V14: Configuration |
| `0x50-V50-WebFrontend.md` | V50: Web Frontend |
| `0x51-V51-OAuth-OIDC.md` | V51: OAuth & OIDC |
| `0x52-V52-SelfContained-Tokens.md` | V52: Self-Contained Tokens |

### Phase D — Appendices & Final QA (Target: August 2026)

- Appendices (A through E)
- Glossary finalization
- Full cross-reference validation
- PDF generation
- Community review period (4 weeks)

---

## How to Contribute a Review

### Quick Review (15 minutes)

1. Open PR [#3254](https://github.com/OWASP/ASVS/pull/3254)
2. Click "Files changed" tab
3. Read through any `.md` file in `5.0/pa-IN/`
4. Leave inline comments on specific lines
5. Focus on: accuracy, natural phrasing, term choices

### Detailed Review (1–2 hours)

1. Fork the repo and checkout the `panjabi-translation-v5` branch
2. Review the glossary in `README.md` for term consistency
3. Cross-reference Panjabi text against the English source in `5.0/en/`
4. Check `TRANSLATION-NOTES.md` for any open terminology decisions
5. Submit a review with suggestions via GitHub PR review

### Reviewer Qualifications (any one or more)

- Panjabi speaker with security domain knowledge
- Security researcher who can validate English source accuracy
- Linguist with Gurmukhi expertise (script/grammar review)
- OWASP community member familiar with ASVS structure

---

## Terminology Decision Log (Open Questions)

These terms need community input — add your preference as a PR comment:

| English Term | Current Panjabi | Alternative | Status |
|-------------|----------------|-------------|--------|
| Verification | ਤਸਦੀਕ | ਪੜਤਾਲ | Under review |
| Standard | ਮਿਆਰ | ਪੱਧਰ / ਕਸਵਟੀ | Accepted as ਮਿਆਰ |
| Requirement | ਲੋੜ | ਸ਼ਰਤ | Under review |
| Vulnerability | ਕਮਜ਼ੋਰੀ | ਕਮੀ | Under review |
| Threat Modeling | ਖ਼ਤਰਾ ਮਾਡਲਿੰਗ | ਖ਼ਤਰਾ ਨਮੂਨਾਕਰਨ | Under review |

---

## Project Links

| Resource | Link |
|----------|------|
| Pull Request | [OWASP/ASVS #3254](https://github.com/OWASP/ASVS/pull/3254) |
| Fork Repository | [GeeksikhSecurity/ASVS](https://github.com/GeeksikhSecurity/ASVS/tree/panjabi-translation-v5) |
| ASVS 5.0 English Source | [OWASP/ASVS/5.0/en](https://github.com/OWASP/ASVS/tree/master/5.0/en) |
| Related Issues | [#3252](https://github.com/OWASP/ASVS/issues/3252), [#3253](https://github.com/OWASP/ASVS/issues/3253) |
| Other ASVS Translations | [Spanish #3238](https://github.com/OWASP/ASVS/issues/3238), [Russian #3223](https://github.com/OWASP/ASVS/issues/3223), [Korean #3204](https://github.com/OWASP/ASVS/issues/3204) |
| OWASP Translation Guide | [CONTRIBUTING.md](https://github.com/OWASP/ASVS/blob/master/CONTRIBUTING.md) |

---

## Contact

- **GitHub:** [@GeeksikhSecurity](https://github.com/GeeksikhSecurity)
- **Platform:** [SecurityLeader.ai](https://securityleader.ai)
- **OWASP Slack:** Join `#asvs` channel

> *"ਸੁਰੱਖਿਆ ਗਿਆਨ ਸਭ ਲਈ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ"*
> *Security knowledge should be accessible to all.*

---

*Last updated: February 23, 2026*
*License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)*
