# Open Terminology Questions — Reviewer Adjudication

This document collects terminology decisions made during the Panjabi (pa-IN) translation of OWASP ASVS 5.0 that the translator deferred for community review. Each entry shows the **current pick on the PR**, **alternatives considered**, and the **reasoning** that led to the current choice.

**Reviewer ask:** For each entry, either confirm the current pick, or propose a substitution. Email feedback to [gurvinder@securityleader.ai](mailto:gurvinder@securityleader.ai) with subject *"ASVS Panjabi Review — Q<number>"*, or comment inline on PR [#3254](https://github.com/OWASP/ASVS/pull/3254).

**Author commitment:** The translator (GeeksikhSecurity) treats every entry below as **v0.1 — open for change**. The current pick is what's on disk; it is not the final answer. Final answer is the community-adjudicated form.

---

## How to read this file

| Field | Meaning |
|---|---|
| **EN term** | The English source term as it appears in OWASP ASVS 5.0 |
| **Current pick** | The Gurmukhi rendering committed on PR #3254 today |
| **Alternatives** | Other candidates considered with their tradeoffs |
| **Type** | T = Translated, L = Loan, R = Retained (acronym/proper noun), H = Hybrid |
| **Reasoning** | Why the current pick — and what could flip it |
| **Reviewer notes** | (Empty — reviewers fill this in via email or PR comment) |

---

## Q1 — `multi-tenant` (V8 Authorization)

| | |
|---|---|
| **EN term** | multi-tenant |
| **Current pick** | ਬਹੁ-ਕਿਰਾਏਦਾਰ (`bahu-kirāedār`) |
| **Type** | T |
| **Alternatives** | ਮਲਟੀ-ਟੇਨੈਂਟ (`malṭī-ṭenaiṅṭ`, L) — direct transliteration |
| **Reasoning** | `kirāedār` literally = "tenant" in standard Punjabi (Persian-origin, well-attested in real-estate and legal prose). The `bahu-` prefix = "many/multi". Honest native compound. The transliteration `ਮਲਟੀ-ਟੇਨੈਂਟ` would be unambiguous but reads as low-effort English-in-Gurmukhi-script |
| **Reviewer notes** | _to be filled_ |

## Q2 — `IDOR / BOLA / BOPLA` acronyms (V8 Authorization)

| | |
|---|---|
| **EN term** | IDOR, BOLA, BOPLA |
| **Current pick** | Latin retained in Panjabi tables — `IDOR`, `BOLA`, `BOPLA` |
| **Type** | R |
| **Alternatives** | (a) Add a Gurmukhi gloss in parens at first use, e.g., `IDOR (ਅਸੁਰੱਖਿਅਤ ਸਿੱਧਾ ਆਬਜੈਕਟ ਹਵਾਲਾ)`. (b) Provide a glossary appendix entry per acronym |
| **Reasoning** | Industry-standard security acronyms; expanding them inline disrupts table readability. The OWASP convention itself uses the acronyms unexpanded in normative requirements. Glossary expansion (option b) seems most appropriate but is currently absent from the pa-IN glossary |
| **Reviewer notes** | _to be filled_ |

## Q3 — `entitlements` (V8 Authorization)

| | |
|---|---|
| **EN term** | entitlements |
| **Current pick** | ਹੱਕ (`haqq`) |
| **Type** | T |
| **Alternatives** | ਅਧਿਕਾਰ (`adhikār`) |
| **Reasoning** | `ਅਧਿਕਾਰ` is the natural translation but **collides with ਅਧਿਕਾਰੀਕਰਨ (`adhikārīkaraṇ`)** — the locked term for "authorization" itself across the whole chapter. Using `ਅਧਿਕਾਰ` for "entitlements" inside an authorization chapter creates "ਅਧਿਕਾਰ ਅਧਿਕਾਰੀਕਰਨ ਪ੍ਰਣਾਲੀ" tautology. `ਹੱਕ` (Persian-origin, "right/claim") sidesteps the collision and reads naturally |
| **Reviewer notes** | _to be filled_ |

## Q4 — `step-up authentication` (V8 Authorization)

| | |
|---|---|
| **EN term** | step-up authentication |
| **Current pick** | ਸਟੈਪ-ਅੱਪ ਪ੍ਰਮਾਣੀਕਰਨ (`sṭaip-app pramāṇīkaraṇ`) |
| **Type** | H |
| **Alternatives** | ਉੱਚਾ-ਪੱਧਰ ਪ੍ਰਮਾਣੀਕਰਨ (`uchchā-paddhar pramāṇīkaraṇ`) — fully native, "higher-level authentication" |
| **Reasoning** | "Step-up" is a security-industry idiom (specific OAuth/MFA pattern); transliterating preserves recognizability for bilingual practitioners cross-referencing English documentation. The fully native form is more elegant but loses that retrievability |
| **Reviewer notes** | _to be filled_ |

## Q5 — `posture` (V8 Authorization) — RESOLVED

| | |
|---|---|
| **Status** | **RESOLVED 2026-06-01** — see commit `9e1e96b` |
| **EN term** | device security posture |
| **Initial pick** | ਮੁਦਰਾ (`mudrā`) |
| **Final pick** | **ਸਥਿਤੀ (`sthitī`)** |
| **Reasoning** | `mudrā` carries strong Hindu/Hatha-Yoga ritual connotations (ritual hand gesture in classical Indian iconography); flagged as Gurmat-policy violation per `5.0/pa-IN/CLAUDE.md`. Replaced with `sthitī` (state/situation/posture) — neutral, no Gurmat conflict, already used in this same chapter (8.1.2) for "data object state/status" |
| **Reviewer notes** | _resolved, no action needed_ |

## Q6 — `Self-contained token` (V9 Self-contained Tokens)

| | |
|---|---|
| **EN term** | Self-contained token |
| **Current pick** | ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ (`svai-nirbhar ṭokan`) |
| **Type** | H |
| **Alternatives** | ਸਵੈ-ਪੂਰਨ ਟੋਕਨ (`svai-pūran ṭokan`); ਸਵੈ-ਸੰਪੰਨ ਟੋਕਨ (`svai-sampann ṭokan`) |
| **Reasoning** | Neologism — no established Panjabi equivalent. `svai-nirbhar` = "self-reliant" emphasizes the JWT/JWS property of being verifiable without a state lookup. `svai-pūran` ("self-complete") and `svai-sampann` ("self-equipped") are both reasonable; `nirbhar` was chosen because it foregrounds the *operational independence* property reviewers and developers care about |
| **Reviewer notes** | _to be filled_ |

## Q7 — `Audience` (JWT claim) (V9 Self-contained Tokens)

| | |
|---|---|
| **EN term** | Audience (as in the JWT `aud` claim — "intended recipient service") |
| **Current pick** | English `audience` kept inline (R) |
| **Type** | R |
| **Alternatives** | ਸਰੋਤਾ (`sarotā`) — "listener" |
| **Reasoning** | `sarotā` literally means "one who listens/reads" — wrong semantics for JWT, where `audience` means *intended recipient service*, not a human. No Panjabi term carries the precise JWT `aud` semantics. Keeping English `audience` inline avoids a semantically misleading translation. A glossary entry could explain |
| **Reviewer notes** | _to be filled_ |

## Q8 — `Stateless` (deferred from V9)

| | |
|---|---|
| **EN term** | stateless |
| **Current pick** | (deferred — not used in 0x18; will appear in V11/V12/V16 chapters) |
| **Type** | _undecided_ |
| **Alternatives** | ਸਟੇਟਲੈੱਸ (`sṭeṭalais`, L) — direct loan; ਸਥਿਤੀ-ਰਹਿਤ (`sthitī-rahit`, T) — "state-less" native |
| **Reasoning** | Direct loan reads more naturally in developer-facing prose; native form is more elegant in prose-heavy sections. Decision deferred to first chapter that actually uses it |
| **Reviewer notes** | _to be filled — early signal welcome since this fires in multiple chapters_ |

## Q9 — `Allowlist` (V9, V5 File Handling)

| | |
|---|---|
| **EN term** | allowlist |
| **Current pick** | English `allowlist` kept inline (R) |
| **Type** | R |
| **Alternatives** | ਪ੍ਰਵਾਨ-ਸੂਚੀ (`pravān-sūchī`, T) — "approval list"; ਆਗਿਆ-ਸੂਚੀ (`āgiā-sūchī`, T) — "permission list" |
| **Reasoning** | Industry-standard term; the OWASP-recommended replacement for "whitelist". Both calques are plausible but introduce a fresh native term that readers cross-referencing English documentation may not recognize. Precedent now set in both 0x14 V5 and 0x18 V9 — change once means changing twice |
| **Reviewer notes** | _to be filled_ |

## Q10 — `Key material` (V9 Self-contained Tokens)

| | |
|---|---|
| **EN term** | key material |
| **Current pick** | English `key material` kept inline (R) |
| **Type** | R |
| **Alternatives** | ਕੁੰਜੀ-ਸਮੱਗਰੀ (`kuñjī-samagrī`, T) — "key material" literal calque |
| **Reasoning** | Precise cryptographic term; the calque is grammatically clean but loses retrievability for practitioners reading mixed EN+PA cryptography documentation. Could ship as English with a glossary entry |
| **Reviewer notes** | _to be filled_ |

## Q11 — `LFI / RFI / SSRF / zip slip` acronyms (V5 File Handling)

| | |
|---|---|
| **EN term** | LFI, RFI, SSRF, zip slip |
| **Current pick** | Latin retained in PA table |
| **Type** | R |
| **Alternatives** | Add Gurmukhi gloss on first use, e.g., `LFI (ਸਥਾਨਕ ਫ਼ਾਈਲ ਇਨਕਲੂਜ਼ਨ)` |
| **Reasoning** | Same logic as Q2 (IDOR/BOLA/BOPLA). Industry-standard acronyms; inline expansion would clutter requirement-table cells. Consistency: matches the Q2 decision pattern |
| **Reviewer notes** | _to be filled_ |

## Q12 — Bilingual structure: dual-block vs code-switched (CORPUS-WIDE — highest priority)

| | |
|---|---|
| **Decision** | Which bilingual structure should the whole corpus use? |
| **Status** | **OPEN — deferred to community review (highest-priority structural question)** |

Two structures currently coexist in the committed chapters. This is the single most important thing for reviewers to weigh in on, because it affects every chapter going forward.

**Pattern A — dual-block (English-first, full Panjabi mirror below)**

Used in: `0x01`, `0x02`, `0x14`, `0x17`, `0x18`, `0x21`

```markdown
## V5 File Handling
## V5 ਫ਼ਾਈਲ ਪ੍ਰਬੰਧਨ

The use of files can present a variety of risks...

ਫ਼ਾਈਲਾਂ ਦੀ ਵਰਤੋਂ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਕਈ ਤਰ੍ਹਾਂ ਦੇ ਖ਼ਤਰੇ...

| # | Description | Level |   ← English requirement table
| # | ਵੇਰਵਾ | ਪੱਧਰ |        ← parallel Panjabi requirement table
```

- A non-English-reading Panjabi developer can read the Panjabi block end-to-end.
- The English block is preserved verbatim for cross-reference and technical precision.
- This is the structure the project's public rationale commits to: *"every section is bilingual. English first, Panjabi immediately below."*
- Cost: roughly doubles file length; more to maintain when upstream English changes.

**Pattern B — code-switched single-block (Panjabi-primary, English terms inline)**

Used in: `0x04`, `0x05`

```markdown
# v4.x ਦੇ ਮੁਕਾਬਲੇ ਤਬਦੀਲੀਆਂ (Changes Compared to v4.x)

Version 4.0.3 ਦੀਆਂ 286 requirements ਵਿੱਚੋਂ, ਸਿਰਫ਼ 11 ਬਿਨਾਂ ਤਬਦੀਲੀ ਦੇ ਰਹਿ ਗਈਆਂ ਹਨ...
```

- More compact; reads naturally for a bilingual developer comfortable with English technical terms.
- A Panjabi-only reader cannot read it cleanly (English nouns are load-bearing), and there is no separate English block to cross-reference.
- Diverges from the public rationale's stated promise.

**Recommendation from the translator:** Pattern A, for consistency with the project's stated bilingual-readability goal. If the community agrees, `0x04` and `0x05` will be re-translated into Pattern A. If the community prefers Pattern B for intro/meta chapters (and Pattern A for normative requirement chapters), that mixed convention will be documented in `TRANSLATION-NOTES.md` and applied deliberately rather than by accident.

**Reviewer ask:** State a preference — (a) Pattern A everywhere, (b) Pattern B everywhere, or (c) mixed-by-chapter-type with explicit rules. This decision is currently *unmade*; the two patterns in the corpus today are an artifact of different drafting passes, not a deliberate choice.

| **Reviewer notes** | _to be filled_ |

---

## Resolved questions

| # | Question | Resolution | Commit |
|---|---|---|---|
| Q5 | `posture` ਮੁਦਰਾ → ਸਥਿਤੀ | Gurmat-policy violation; replaced with `sthitī` | `9e1e96b` |

---

## Policy locks (for reference)

These policies are **already locked** and not open for review:

- **R21** — Standalone fraud term must be `ਠੱਗੀ` (`ṭhaggī`); the only allowed exception is the compound `ਰੋਮਾਂਸ ਫ਼ਰਾਡ` (romance fraud) — locked 2026-05-30
- **R22** — Standard term for "community" is `ਭਾਈਚਾਰਾ` (`bhāʼīchārā`); `ਸੰਗਤ` reserved for named Sikh religious contexts — locked 2026-05-30
- **R23** — Romanization is IAST canonical: `ṭ ḍ ṇ ā ī ū ṅ ñ chh ʼ` — locked 2026-05-30
- **Gurmat constraints** (CLAUDE.md) — no yoga/Hindu/Sanskrit terms outside direct Gurbani quotation
- **Devanagari purity** — no letters in U+0900–U+0963 or U+0966–U+097F; the danda U+0964 and double-danda U+0965 are explicitly allowed as shared Indic punctuation

If a reviewer wants to challenge a locked policy, please open a separate GitHub issue rather than commenting inline — the policy lock is corpus-wide, not a per-chapter decision.

---

## Maintainer

Gurvinder Singh, CISSP · CISA · GWAPT — [securityleader.ai](https://securityleader.ai) · [@GeeksikhSecurity](https://github.com/GeeksikhSecurity)
