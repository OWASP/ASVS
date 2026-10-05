# OWASP ASVS — Panjabi (pa-IN) Translation Rules

**Status:** canonical · **Updated:** 2026-06-06 · **Lead:** Gurvinder Singh (@GeeksikhSecurity)
**Method:** AI-assisted draft (v0.1) → Sangat/community review is the certification gate.

This is the authoritative rule set for the Panjabi translation. It consolidates the project
locks, the engine prompt contract, and lessons from real academic Panjabi usage (Punjabi
University, Patiala — Department of Music page + ACTDPL language-tech centre; see the PDL
project's `LESSONS-PUNJABI-UNIVERSITY.md`). All prior recommendations are **accepted** here.

---

## 1. Script & encoding

1. **Gurmukhi only** (U+0A00–U+0A7F). NEVER Devanagari letters; NEVER Latin transliteration
   of the Panjabi body text.
2. **Unicode NFC**-normalise all Panjabi text (precomposed nukta — e.g. ੜ, not ਡ+਼).
3. Allowed shared punctuation: danda `।` (U+0964), double-danda `॥` (U+0965).
4. Proper use of mātrā (ਮਾਤਰਾ), addak (ੱ), tippi/bindi (ੰ/ਂ), nukta (਼).

## 2. Orthography

1. **Sentence-end = danda `।`** for full Panjabi sentences (prose). NEVER the Western period.
   Do **not** add a danda to short UI labels, headings, or list fragments.
2. **Numerals = Western digits** (0–9) in technical prose — years, quantities, **and version
   numbers** (write `5.0`, not `੫.੦`). *Accepted:* this matches how leading Panjabi
   institutions write modern/technical text (Punjabi University pages use 1984, 2004…).
   Gurmukhi numerals are reserved for traditional/decorative contexts only.
3. **Requirement IDs stay exactly as the source** (e.g. `9.1.1`, `v5.0.0-2.1.7`) — English
   digits, never converted.
4. **The apostrophe-clitic `'ਤੇ` is ACCEPTABLE** Panjabi orthography (attested in real
   academic text, e.g. `…ਡੀ)'ਤੇ`). It is **NOT** a translation error and must **not** be
   flagged by lint. (Note: stripping it for *search-key normalisation* in PDL is a separate,
   permitted concern.)
5. **Spelling:** "Panjabi" / "Panjab" (per Sikhri.org and Panjab Digital Library), not
   "Punjabi" / "Punjab", in any English appearing in the translation.

## 3. Romanization

When romanizing a Panjabi term, use **IAST** diacritics (ṭ ḍ ṇ ā ī ū ṅ ñ, "chh", the ʼ for
addak) — never doubled-vowel English style (write `ṭhaggī`, not `thaggee`).

## 4. Register & terminology (T/L/R/H)

Match the register of **formal academic Panjabi**. Classify every term:

| Tag | Use | Examples (attested in real academic Panjabi) |
|---|---|---|
| **T — Translated** (native/Sanskritic) for established concepts | ਪ੍ਰਮਾਣੀਕਰਨ (authentication), ਅਖੰਡਤਾ (integrity), ਸਿਧਾਂਤ (theory), ਅੰਤਰ-ਅਨੁਸ਼ਾਸਨੀ (inter-disciplinary) |
| **L — Loan** (transliterated) for modern/Western terms with no settled Panjabi word | ਟੋਕਨ (token), ਡਾਊਨਲੋਡ (download), ਕੋਰਸ (course), ਵਰਕਸ਼ਾਪ (workshop) |
| **R — Retained** in English/Latin — never translate or transliterate | OWASP, ASVS, CWE, SQL, XSS, CSRF, SSRF, API, URL, TLS, JWT, JWS, JWK, MAC, HMAC, OAuth, OIDC, SAML, JSON, PIN, OTP, **audience**, **key material**, allowlist/denylist, algorithm names/values (`'None'`, `RS256`), header/claim names (`alg`,`jku`,`x5u`,`jwk`,`aud`,`nbf`,`exp`,`iss`) |
| **H — Hybrid** (English head + Panjabi word) | SQL ਇੰਜੈਕਸ਼ਨ, GraphQL ਕਿਊਰੀ |

**Glossary anchoring:** prefer terms attested in **Punjabi University lexicography** and the
project glossary; cite sources (APA) for contested choices.

### Locked terminology decisions
- **Fraud/scam** → always **ਠੱਗੀ**. The only allowed `ਫ਼ਰਾਡ` compound is **ਰੋਮਾਂਸ ਫ਼ਰਾਡ**.
- **Community** → **ਭਾਈਚਾਰਾ** (generic); **ਸੰਗਤ** only in named Sikh religious contexts.
- **House glossary (pin these exact terms):** self-contained → ਸਵੈ-ਨਿਰਭਰ · integrity →
  ਅਖੰਡਤਾ · validity period → ਜਾਇਜ਼ਤਾ ਮਿਆਦ · context → ਸੰਦਰਭ · issuer → ਜਾਰੀਕਰਤਾ · tampering →
  ਛੇੜਛਾੜ · verify → ਤਸਦੀਕ ਕਰੋ · validate → ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ. Grow from review.

### Verb precision
Preserve "verify" / "validate" / "check" as distinct — they are not interchangeable in a
security standard. ASVS requirements typically open "Verify that…" → **ਤਸਦੀਕ ਕਰੋ ਕਿ…**.

### First-use gloss
On first use of a translated technical concept, give the Panjabi term followed by the English
in parentheses, e.g. **ਅਖੰਡਤਾ (integrity)**. Do not repeat the gloss every time.

## 5. Gurmat / cultural safety

1. No yoga/Hindu/Sanskrit-devotional vocabulary outside a direct Gurbani quotation. (E.g.
   render "posture/state" as **ਸਥਿਤੀ** (sthitī), never **ਮੁਦਰਾ** (mudrā, yoga-connoted).)
2. Sacred/Gurbani material requires **Sangat sign-off**; no AI output self-certifies above v0.1.

## 6. Bilingual structure

1. **Dual-block:** English block, then the Panjabi translation block (consistent order
   corpus-wide — this is the Q12 decision; real institutions are inconsistent, so a fixed
   convention is an improvement).
2. **Heading model:** `Panjabi Heading (English)` or `English Heading ਪੰਜਾਬੀ ਸਿਰਲੇਖ`, applied
   consistently.
3. Do not soften, omit, or add security obligations; translate the requirement as written.

## 7. Process

- AI-assisted draft (Opus 4.8 with the `asvs` prompt profile that encodes these rules) →
  scored on the PDL translation bench → **Sangat/community review = certification gate**.
- Mechanical QA before review: 0 Devanagari leaks, 0 Western-period sentence-ends, 0
  Gurmat-prohibited terms, 0 fraud-term violations, retained-terms intact, NFC-clean.

---

*These rules are enforced by the bench's `asvs` system-prompt profile and checked in review.
Changes are corpus-wide — propose via a GitHub issue, not inline.*
