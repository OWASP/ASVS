# CLAUDE.md — OWASP ASVS Panjabi Translation Rules

## Project

OWASP ASVS 5.0 Panjabi (pa-IN) translation. Bilingual English/Gurmukhi format.
Repository: `GeeksikhSecurity/ASVS` branch `panjabi-translation-v5`

## Spelling

Use **"Panjabi"** (not "Punjabi") per Sikhri.org and Panjab Digital Library standards.

---

## Translation Dictionary Sources (MANDATORY)

All Panjabi translations MUST cross-reference these scraped dictionary sources before using any term:

1. **Guru Granth Sahib Dictionary** — https://gurugranthsahibdictionary.io/
   - Primary source for Gurmukhi vocabulary, word roots, and semantic context
   - Scraped content available in project data files when present

2. **Guru Granth Sahib Reference** — https://gurugranthsahib.io/info/english/guru-granth-sahib
   - Contextual definitions and usage patterns rooted in Gurbani tradition
   - Gurmukhi script institutionalized by Guru Angad Sahib

3. **Punjabi University Patiala English-Punjabi Dictionary** (ISBN 81-7380-095-2)
   - Secondary reference for technical/modern terms not found in Gurbani sources
   - Use entries for authentication (ਪ੍ਰਮਾਣੀਕਰਨ, ਤਸਦੀਕ), authorization (ਅਧਿਕਾਰ), access (ਪਹੁੰਚ), etc.

### Dictionary Lookup Order
1. Check gurugranthsahibdictionary.io first
2. Check gurugranthsahib.io for contextual usage
3. Fall back to Punjabi University Patiala dictionary for technical terms
4. If no match found, document as "open terminology question" in TRANSLATION-NOTES.md

---

## Gurmat Language Constraints (MANDATORY)

Adapted from the Gurmat-Centered Bilingual Prompt (Google Doc ID: 1G23l0TJ9594K0yYBUcp4quR4vsOcTUjVCTYWWmopx0Y).

### NEVER USE — Prohibited Terminology
- ❌ Yoga terminology (chakras, kundalini, pranayama, third eye)
- ❌ Hindu deity names or mythology references
- ❌ Energy centers, auras, or metaphysical yoga concepts
- ❌ Sanskrit mantras or terms outside of Gurbani context
- ❌ Any term with yoga/Hindu connotation when a Gurmat or neutral Panjabi equivalent exists

### ALWAYS PREFER — Gurmat-Aligned Vocabulary
- ✅ Terms rooted in Gurmukhi tradition and Sikh scholarly usage
- ✅ Vocabulary from Guru Granth Sahib Dictionary when applicable
- ✅ Prof. Sahib Singh's Darpan methodology for interpretive guidance
- ✅ Contemporary Panjabi that resonates with modern technical readers
- ✅ Bilingual format maintaining parallel meaning (English | ਪੰਜਾਬੀ)

### Quality Check Before Every Commit
- [ ] Zero yoga/Hindu/Sanskrit influence outside Gurbani
- [ ] All terms cross-referenced against dictionary sources above
- [ ] Open terminology questions documented in TRANSLATION-NOTES.md
- [ ] Bilingual format maintained (English term | Gurmukhi term)
- [ ] T/L/R/H classification applied (Translated/Loan/Retained/Hybrid)

---

## Translation Classification System (T/L/R/H)

| Code | Type | Example |
|------|------|---------|
| **T** | Translated | Authentication → ਪ੍ਰਮਾਣੀਕਰਨ |
| **L** | Loan word | API → ਏ.ਪੀ.ਆਈ. |
| **R** | Retained | OWASP, SQL, XSS (kept as-is) |
| **H** | Hybrid | SQL Injection → SQL ਇੰਜੈਕਸ਼ਨ |

---

## Gurmukhi Numerals

Use Gurmukhi numerals for ASVS version references: ੫.੦ (not 5.0)

---

## Reverence Note

Sri Guru Granth Sahib Ji is the eternal Guru and supreme guiding authority for Sikhs. It contains the divine utterances of six Gurus, three Sikhs, fifteen saints, and eleven court poets. Never refer to it as a "scripture" or "book." The Gurmukhi script was institutionalized by Guru Angad Sahib.

---

## Blog Post Structure (SecurityLeader.ai)

When creating blog posts about this translation project for SecurityLeader.ai:

1. Italic hook question after H1
2. Executive Summary blockquote
3. "Your Next Move" section with role-specific CTAs
4. Board talking points + author attribution (Gurvinder Singh, Principal Security Researcher)

Publish workflow: Claude Code → `git push origin main` → Vercel auto-deploy

---

## File Structure

```
5.0/pa-IN/
├── CLAUDE.md                  ← This file (translation rules)
├── TRANSLATION-NOTES.md       ← Open terminology questions
├── REVIEW-PLAN.md             ← Community review process
├── GIT-CHEATSHEET.md          ← Contributor git workflow
├── README.md                  ← Translation overview
├── 0x01-Frontispiece.md       ← Phase A (complete)
├── 0x02-Preface.md            ← Phase A (complete)
├── 0x03-Using-ASVS.md        ← Phase B (March-April 2026)
├── 0x04-Assessment-and-Cert.md ← Phase B
├── V1-V4/                     ← Phase B
├── V5-V14, V50-V52/           ← Phase C (May-July 2026)
└── Appendices/                 ← Phase D (August 2026)
```
