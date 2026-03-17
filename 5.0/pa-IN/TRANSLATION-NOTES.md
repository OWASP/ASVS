# Panjabi Translation Notes
# ਪੰਜਾਬੀ ਅਨੁਵਾਦ ਨੋਟਸ

## Translation Started
- Date: September 16, 2025
- Translator: GeeksikhSecurity (Gurvinder Singh)
- Version: ASVS 5.0.0

## Spelling Convention
Using "Panjabi" following Sikhri.org and Panjab Digital Library standards

## Format Convention
- **Bilingual**: Every English paragraph is followed by its Panjabi (Gurmukhi) translation
- **Section headers**: English heading followed by Gurmukhi heading on next line
- **Tables**: Bilingual in same cell using `<br>` separator where applicable
- **First-occurrence rule**: Translated terms shown as "ਗੁਰਮੁਖੀ (English)" on first use
- **Acronyms**: Retained in English with Gurmukhi pronunciation guide on first use

## Progress Tracking

### Phase A — Foundation (~960 words)
- [x] 0x01-Frontispiece.md (282 words)
- [x] 0x02-Preface.md (399 words)
- [x] README.md (expanded glossary, ~100 terms)

### Phase B — Context (~5,250 words)
- [ ] 0x03-What-is-the-ASVS.md (3,264 words)
- [ ] 0x04-Assessment_and_Certification.md (803 words)
- [ ] 0x05-For-Users-Of-4.0.md (1,260 words)

### Phase C — Core Security Chapters (~18,650 words)
- [ ] 0x10-V1-Encoding-and-Sanitization.md (1,897 words)
- [ ] 0x11-V2-Validation-and-Business-Logic.md (1,057 words)
- [ ] 0x12-V3-Web-Frontend-Security.md (2,086 words)
- [ ] 0x13-V4-API-and-Web-Service.md (1,059 words)
- [ ] 0x14-V5-File-Handling.md (816 words)
- [ ] 0x15-V6-Authentication.md (3,142 words)
- [ ] 0x16-V7-Session-Management.md (1,343 words)
- [ ] 0x17-V8-Authorization.md (843 words)
- [ ] 0x18-V9-Self-contained-Tokens.md (678 words)
- [ ] 0x19-V10-OAuth-and-OIDC.md (3,080 words)
- [ ] 0x20-V11-Cryptography.md (1,785 words)
- [ ] 0x21-V12-Secure-Communication.md (768 words)
- [ ] 0x22-V13-Configuration.md (1,180 words)
- [ ] 0x23-V14-Data-Protection.md (1,036 words)
- [ ] 0x24-V15-Secure-Coding-and-Architecture.md (1,479 words)
- [ ] 0x25-V16-Security-Logging-and-Error-Handling.md (1,211 words)
- [ ] 0x26-V17-WebRTC.md (1,229 words)

### Phase D — Appendices (~7,653 words)
- [ ] 0x90-Appendix-A_Glossary.md (2,757 words)
- [ ] 0x91-Appendix-B_References.md (222 words)
- [ ] 0x92-Appendix-C_Cryptography.md (2,988 words)
- [ ] 0x93-Appendix-D_Recommendations.md (717 words)
- [ ] 0x94-Appendix-E_Contributors.md (991 words)

**Total: ~38,372 words across 27 files**

## Terminology Decision Log

Key decisions on how security terms are handled in this translation:

| Decision | Term | Approach | Rationale |
|----------|------|----------|-----------|
| 1 | Security | ਸੁਰੱਖਿਆ (surakkhiā) — Translate | Well-established Panjabi word |
| 2 | Authentication | ਪ੍ਰਮਾਣੀਕਰਨ (pramāṇīkaran) — Translate | Standard academic Panjabi |
| 3 | SQL Injection | ਐੱਸ.ਕਿਊ.ਐੱਲ. ਇੰਜੈਕਸ਼ਨ — Transliterate | No Panjabi equivalent; technical term |
| 4 | OWASP | Retain English | Global brand; add ਓਵਾਸਪ pronunciation |
| 5 | Cross-Site Scripting | ਕਰਾਸ-ਸਾਈਟ ਸਕ੍ਰਿਪਟਿੰਗ — Transliterate | Technical term, XSS acronym retained |
| 6 | Vulnerability | ਕਮਜ਼ੋਰੀ (kamzorī) — Translate | Common Panjabi word for weakness |
| 7 | Token | ਟੋਕਨ (ṭokan) — Transliterate | Widely used in Panjabi tech context |
| 8 | "Panjabi" spelling | Use "Panjabi" not "Punjabi" | Per Sikhri.org, Panjab Digital Library |

## QA Checklist

For each translated file, verify:

- [ ] **Gurmukhi rendering**: All characters within Unicode U+0A00-U+0A7F range
- [ ] **Glossary consistency**: Terms match glossary definitions throughout
- [ ] **Markdown integrity**: Tables, headers, links render correctly
- [ ] **Bilingual completeness**: Every English section has corresponding Gurmukhi
- [ ] **First-occurrence annotations**: Technical terms explained on first use
- [ ] **Proper nouns**: Names kept in English (not transliterated)
- [ ] **Requirement IDs**: Unchanged (e.g., **6.2.1** stays as-is)
- [ ] **Link validity**: All hyperlinks preserved from English source
- [ ] **Gurmukhi numerals**: Used where appropriate (੧, ੨, ੩... for Panjabi text)

## Translation Guidelines
- Maintain technical accuracy
- Use consistent terminology from glossary
- Keep English technical terms in parentheses when first introduced
- Follow Gurmukhi script conventions
- Preserve markdown formatting and links
- Glossary tool available at: `web-scrapers/gurbani_dictionary_scraper/asvs_translation_tool.py`

## Platform Coordination
- Primary workflow: GitHub PR #3254
- Glossary and term discussions: GitHub issues
- Future: Crowdin platform integration for community contributions
