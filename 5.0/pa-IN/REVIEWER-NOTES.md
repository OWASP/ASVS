# Reviewer Notes — OWASP ASVS 5.0 Panjabi (pa-IN) Translation

**Share this file with anyone you ask to review the translation.** It is a self-contained briefing: what's done, what to check, how to give feedback, and where the open decisions are.

- **PR:** [OWASP/ASVS#3254](https://github.com/OWASP/ASVS/pull/3254) (Draft)
- **Branch:** `GeeksikhSecurity:panjabi-translation-v5`
- **Lead translator:** Gurvinder Singh, CISSP · CISA · GWAPT — [@GeeksikhSecurity](https://github.com/GeeksikhSecurity) · [securityleader.ai](https://securityleader.ai)
- **Method:** AI-assisted draft (v0.1) with human author review; community/sangat review is the certification gate — no AI output self-certifies above v0.1
- **Last updated:** 2026-06-02

---

## You do not need to be both things

Either qualification helps — you don't need both:

- **Panjabi / Gurmukhi reader** — does it read naturally? Are the term choices right? Any script errors?
- **Security practitioner** — is the English meaning preserved? Could a translation choice mislead an implementer?

A linguist with no security background and a security engineer with no Panjabi are *both* useful reviewers.

---

## What's ready to review right now

**Complete chapters (8)** — these should be defect-free; review for accuracy and naturalness:

| File | Chapter | Shortest-to-start |
|---|---|---|
| `0x18-V9-Self-contained-Tokens.md` | JWT / token validation | ⭐ start here (small) |
| `0x04-Assessment_and_Certification.md` | assessment guidance | ⭐ start here (small) |
| `0x21-V12-Secure-Communication.md` | TLS / transport security | |
| `0x14-V5-File-Handling.md` | file upload/download | |
| `0x17-V8-Authorization.md` | access control / POLP | |
| `0x05-For-Users-Of-4.0.md` | changes from v4.x | |
| `0x01-Frontispiece.md` | title page / credits | |
| `0x02-Preface.md` | intro / principles / levels | |

**In progress (2)** — headings + structure are bilingual, bodies still being translated; comment on terminology if you like, but expect English-heavy bodies:

- `0x03-What-is-the-ASVS.md`
- `0x15-V6-Authentication.md`

**Supporting:** `README.md`, `CLAUDE.md` (translation rules), `OPEN-QUESTIONS.md` (deferred decisions), `TRANSLATION-NOTES.md`, `REVIEW-PLAN.md`.

---

## The single most important thing to weigh in on

**`OPEN-QUESTIONS.md` → Q12: bilingual structure (dual-block vs code-switched).** The corpus currently has two different structures and the choice is genuinely *unmade*. Your preference here shapes every future chapter. See Q12 for the full comparison; the one-line ask is: Pattern A everywhere, Pattern B everywhere, or mixed-by-chapter-type?

After Q12, the other 11 questions in `OPEN-QUESTIONS.md` are individual terminology calls (e.g., `multi-tenant`, `self-contained token`, `audience` claim) — lighter-weight, also welcome.

---

## What to look for

### 1. Translation accuracy
- Does the Panjabi faithfully convey the security *meaning*, not just the words?
- Are close-but-distinct verbs preserved — "verify" / "validate" / "check"?
- Requirement IDs (e.g., `8.2.2`, `12.1.3`) must stay **exactly** as in English. Flag any that drifted.

### 2. Terminology consistency
- Same English concept → same Panjabi term across every chapter?
- The glossary lives on the public site: [securityleader.ai/blog/asvs-panjabi-review-glossary](https://securityleader.ai/blog/asvs-panjabi-review-glossary) (68 terms, with T/L/R/H classification).

### 3. Gurmukhi script quality
- **No Devanagari** letters mixed in (a common digital-Panjabi error). Note: the sentence-end danda `।` (U+0964) is *correct* and intentional — not an error.
- Proper vowel signs (ਮਾਤਰਾ), addak, bindi/tippi, nukta.
- Clean Unicode — no stray zero-width joiners.

### 4. Readability for a Panjabi-speaking developer
- Would a developer in Punjab understand this without constantly falling back to the English?
- Natural Panjabi sentence flow, or does it read like a word-for-word transliteration?
- Are the parenthetical English terms helpful, or excessive?

### 5. Gurmat / cultural fit
- Per `CLAUDE.md`: no yoga/Hindu/Sanskrit-rooted vocabulary outside a direct Gurbani quotation. (Example already caught and fixed: "security posture" was `ਮੁਦਰਾ` — yoga-connoted — now `ਸਥਿਤੀ`.)
- If a term feels culturally off, say so even if it's technically accurate.

---

## Policy locks (already decided — please don't re-litigate inline)

These are corpus-wide and intentional. If you disagree with one, open a **separate GitHub issue** rather than commenting on individual lines (changing a lock means changing many chapters at once):

| Lock | Rule |
|---|---|
| **Fraud term** | Standalone "scam/fraud" is always `ਠੱਗੀ`; the only allowed `ਫ਼ਰਾਡ` compound is `ਰੋਮਾਂਸ ਫ਼ਰਾਡ` |
| **Community** | `ਭਾਈਚਾਰਾ` for generic "community"; `ਸੰਗਤ` only in named Sikh religious contexts |
| **Romanization** | IAST canonical: `ṭ ḍ ṇ ā ī ū ṅ ñ chh ʼ` — not doubled-vowel English style (`ṭhaggī`, not `thaggee`) |
| **Sentence-end** | Indic danda `।` (U+0964), never the Western period `.`, for Panjabi prose |
| **Script** | No Devanagari letters (U+0900–U+0963, U+0966–U+097F); danda U+0964 and double-danda U+0965 are allowed shared punctuation |
| **Spelling** | "Panjabi" (not "Punjabi") per Sikhri.org / Panjab Digital Library |

---

## How to send feedback

**Easiest — email (no GitHub needed):**
- To **gurvinder@securityleader.ai**
- Subject: **"ASVS Panjabi Review"** (or **"ASVS Panjabi Review — Q12"** etc. for a specific open question)
- Even one term correction is valuable. Quote the file and line if you can.

**GitHub PR review:**
1. Open [PR #3254](https://github.com/OWASP/ASVS/pull/3254), click **Files changed**
2. Read any `.md` in `5.0/pa-IN/`
3. Leave inline comments on specific lines
4. For the structural Q12 decision, leave a top-level PR comment

**Public review pages (for sangat reviewers who don't use GitHub):**
- Reviewer hub: [securityleader.ai/blog/asvs-panjabi-review-hub](https://securityleader.ai/blog/asvs-panjabi-review-hub)
- Glossary (68 terms): [securityleader.ai/blog/asvs-panjabi-review-glossary](https://securityleader.ai/blog/asvs-panjabi-review-glossary)
- Why this translation exists: [securityleader.ai/blog/owasp-asvs-panjabi-translation](https://securityleader.ai/blog/owasp-asvs-panjabi-translation)

---

## Quality assurance already run

- **Mechanical scan (Opus 4.8, 2026-06-02):** 0 Devanagari leaks, 0 fraud-term violations, 0 Gurmat-prohibited terms, 0 Western-period sentence-ends, 0 romanization-style violations across all 13 files.
- **Known open item:** the Q12 structural inconsistency (deferred to this review) and 11 terminology questions in `OPEN-QUESTIONS.md`.

This is a living document — corrections from review flow back into the chapters, and `OPEN-QUESTIONS.md` records every adjudicated decision.

> *ਸੁਰੱਖਿਆ ਗਿਆਨ ਸਭ ਲਈ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।*
> *Security knowledge should be accessible to all.*
