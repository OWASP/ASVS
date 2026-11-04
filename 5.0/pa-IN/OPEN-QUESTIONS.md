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

## Q13 — Corpus-wide term normalisations applied 2026-08-22 (confirm or reverse)

Applied while publishing the August 2026 batch (0x03, V1, V2, V3, V4, V6, V7). Each is a single pick now used consistently; reviewers may reverse any of them corpus-wide.

| EN term | Pick | Was | Type | Reasoning |
|---|---|---|---|---|
| risk (vs threat) | ਜੋਖਮ (risk) · ਖ਼ਤਰਾ (threat) | V6/V7/V8 used ਖ਼ਤਰਾ for both | T | A security standard must keep risk and threat distinct; 0x03 already used ਜੋਖਮ |
| session management | ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ | README: ਸੈਸ਼ਨ ਪ੍ਰਬੰਧ | T | Matches V5 ਫ਼ਾਈਲ ਪ੍ਰਬੰਧਨ; README row updated |
| authorization | ਅਧਿਕਾਰੀਕਰਨ | README: ਅਧਿਕਾਰ | T | Q3 decision; ਅਧਿਕਾਰ now free for "right/entitlement" |
| storage exhaustion (V5) | ਭੰਡਾਰਨ ਖ਼ਤਮ ਹੋ ਜਾਣਾ | ਭੰਡਾਰਨ ਥਕਾਵਟ | T | ਥਕਾਵਟ = tiredness, not depletion (fidelity fix) |
| stateless / stateful | ਸਟੇਟਲੈੱਸ / ਸਟੇਟਫੁੱਲ (glossed once) | Q8 open | L | First use in V7 decides per Q8; native ਸਥਿਤੀ-ਰਹਿਤ remains the alternative |
| entropy | ਐਂਟਰੋਪੀ | V7 had ਐਂਟਰੌਪੀ | L | Spelling normalised to V6 |
| must / must not | ਲਾਜ਼ਮੀ ਹੈ / ਨਹੀਂ … ਚਾਹੀਦਾ (hard prohibition) | several rows had softened to ਚਾਹੀਦਾ or "ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ" (cannot) | — | Modality must match the English; reviewers restored force in V1 1.5.2, V2 2.2.2, V3 3.4.6 |
| bypass | ਬਾਈਪਾਸ (bypass) | ਟਾਲਣਾ (= postpone) | L | Fidelity fix, V2 |
| resolve (DNS/entity/format string) | ਰਿਜ਼ੌਲਵ (resolve) | ਹੱਲ (= solve) | L | Fidelity fix, V1 |

## Q14 — Retained-term-only headings (`## V4.3 GraphQL`, `## V4.4 WebSocket`)

| | |
|---|---|
| **Current pick** | `## V4.3 GraphQL (ਗ੍ਰਾਫ਼ਕਿਊਐੱਲ)` — Latin term kept, Gurmukhi pronunciation in parentheses |
| **Alternatives** | (a) repeat the Latin heading unchanged for the Panjabi line; (b) append a Panjabi noun, e.g. `GraphQL ਸੁਰੱਖਿਆ` |
| **Reasoning** | Rule 4 says never transliterate R-terms, but the dual-block model needs a Panjabi heading line. Pronunciation-in-parens follows the README acronym column and keeps the term retrievable. Corpus-wide decision needed |

## Q15 — New loan vs native picks in V1–V4 (batch)

| EN term | Pick | Type | Alternative |
|---|---|---|---|
| escaping | ਐਸਕੇਪਿੰਗ | L | ਬਚਾਅ-ਚਿੰਨ੍ਹ ਲਗਾਉਣਾ (T, opaque) |
| interpreter | ਇੰਟਰਪ੍ਰੇਟਰ | L | ਵਿਆਖਿਆਕਾਰ (reads as human interpreter) |
| parameterized queries | ਪੈਰਾਮੀਟਰਾਈਜ਼ਡ ਕਿਊਰੀਆਂ | L | ਮਾਪਦੰਡੀ ਕਿਊਰੀਆਂ |
| canonical form | ਕੈਨੋਨੀਕਲ ਰੂਪ | L | ਮਿਆਰੀ ਰੂਪ (loses normalisation sense) |
| deserialization / parser | ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ / ਪਾਰਸਰ | L | — |
| defense-in-depth | ਡੂੰਘਾਈ-ਵਿੱਚ-ਰੱਖਿਆ | T | ਬਹੁ-ਪਰਤੀ ਰੱਖਿਆ (arguably clearer) |
| weakness (vs vulnerability) | ਖ਼ਾਮੀ | T | ਕਮਜ਼ੋਰੀ is locked to vulnerability |
| untrusted | ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ | T | ਭਰੋਸੇਯੋਗ ਨਾ ਹੋਣ ਵਾਲਾ (V8 8.3.1, longer) |
| business logic | ਕਾਰੋਬਾਰੀ ਤਰਕ | T | ਵਪਾਰਕ ਤਰਕ |
| transaction (DB/atomic) | ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨ | L | ਲੈਣ-ਦੇਣ (reads financial-only) |
| schema validation | ਸਕੀਮਾ ਪ੍ਰਮਾਣਿਕਤਾ | H | ਢਾਂਚਾ is locked to architecture |
| anti-automation | ਸਵੈਚਾਲਨ-ਵਿਰੋਧੀ | T | ਐਂਟੀ-ਆਟੋਮੇਸ਼ਨ |
| spoofing | ਸਪੂਫ਼ਿੰਗ | L | ਨਕਲ; ਭੇਸ-ਬਦਲੀ |
| origin / cross-origin (V3) | ਓਰਿਜਿਨ / ਕਰਾਸ-ਓਰਿਜਿਨ | L | ਮੂਲ (ambiguous with "by default"); V4 normalised to ਓਰਿਜਿਨਾਂ on 2026-08-22 |
| HTTP response | ਜਵਾਬ (0x03, V1, V4, V5, V6) / ਪ੍ਰਤੀਕਿਰਿਆ (V3 ×20) | T | **Inconsistent — corpus majority is ਜਵਾਬ; V3 left unchanged because the nouns differ in gender and a mechanical swap would break agreement. Needs a human pass on V3** |
| HTTP method | ਮੈਥਡ (method names Latin) | L | ਵਿਧੀ collides with generic "method/mechanism" |
| hostname | ਹੋਸਟਨੇਮ | L | ਹੋਸਟਨਾਮ (H) |
| nonce | ਨੌਂਸ | L | — |
| request smuggling / response splitting | ਬੇਨਤੀ ਸਮਗਲਿੰਗ / ਜਵਾਬ ਵਿਭਾਜਨ | H/T | retain Latin as attack names |
| introspection (GraphQL) | GraphQL introspection | R | ਆਤਮ-ਨਿਰੀਖਣ rejected (devotional connotation, Gurmat rule) |
| denial of service | ਸੇਵਾ-ਇਨਕਾਰ | T | V4 normalised on 2026-08-22 to the V2/V5 form |

## Q16 — New picks in V6 / V7 (batch)

| EN term | Pick | Type | Alternative |
|---|---|---|---|
| secret (noun) / Secret Management | ਭੇਦ / ਭੇਦ ਪ੍ਰਬੰਧਨ | T | ਗੁਪਤ (kept for adjectival "secret questions/keys") |
| assertion (SAML) | ਅਸਰਸ਼ਨ | L | ਕਥਨ; ਦਾਅਵਾ is reserved for JWT "claim" |
| push notification / push bombing | ਪੁਸ਼ ਸੂਚਨਾ / ਪੁਸ਼ ਬੌਂਬਿੰਗ | H/L | ਪੁਸ਼ ਨੋਟੀਫ਼ਿਕੇਸ਼ਨ / ਪੁਸ਼ ਬੰਬਾਰੀ |
| number matching | ਨੰਬਰ ਮਿਲਾਨ | T | ਨੰਬਰ ਮੈਚਿੰਗ |
| red flag | ਗੰਭੀਰ ਚੇਤਾਵਨੀ ਸੰਕੇਤ | T | ਲਾਲ ਝੰਡਾ (calque) |
| enterprise / throwaway identity | ਸੰਸਥਾਗਤ / ਅਸਥਾਈ ਪਛਾਣ | T | ਇੰਟਰਪ੍ਰਾਈਜ਼ / ਡਿਸਪੋਜ਼ੇਬਲ (L) |
| fallback | ਫ਼ਾਲਬੈਕ | L | ਬਦਲਵੀਂ ਪਹੁੰਚ |
| reference token | ਹਵਾਲਾ ਟੋਕਨ | T | ਰੈਫ਼ਰੈਂਸ ਟੋਕਨ |
| re-authentication | ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ | T | ਪੁਨਰ-ਪ੍ਰਮਾਣੀਕਰਨ |
| inactivity timeout / session lifetime | ਗ਼ੈਰ-ਸਰਗਰਮੀ ਸਮਾਂ-ਸੀਮਾ / ਸੈਸ਼ਨ ਜੀਵਨਕਾਲ | T | ਨਿਸ਼ਕਿਰਿਆ …; ਸੈਸ਼ਨ ਮਿਆਦ |
| federated / Relying Party | ਸੰਘੀ / ਨਿਰਭਰ ਧਿਰ | T | ਫ਼ੈਡਰੇਟਿਡ; ਭਰੋਸਾ ਕਰਨ ਵਾਲੀ ਧਿਰ |
| party | ਧਿਰ | T | V9 normalised from ਪੱਖ on 2026-08-22 |
| session hijacking | ਸੈਸ਼ਨ ਹਾਈਜੈਕਿੰਗ | L | ਸੈਸ਼ਨ ਅਗਵਾ |
| authenticity (V6 L13) | ਪ੍ਰਮਾਣਿਕਤਾ | T | collides with README "validation" = ਪ੍ਰਮਾਣਿਕਤਾ — glossary note |

## Q17 — New picks in 0x03 What is the ASVS? (batch)

| EN term | Pick | Type | Alternative |
|---|---|---|---|
| major / minor / patch release | ਮੇਜਰ / ਮਾਈਨਰ / ਪੈਚ ਰਿਲੀਜ਼ | L | ਮੁੱਖ / ਗੌਣ / ਪੈਚ (loses semver retrievability) |
| fork | ਫ਼ੋਰਕ | L | ਸ਼ਾਖਾ collides with git "branch" |
| architecture / architect | ਆਰਕੀਟੈਕਚਰ / ਆਰਕੀਟੈਕਟ | L | README says ਢਾਂਚਾ; chapters (V8/V12) use the loan — **glossary/corpus disagreement** |
| framework | ਫ੍ਰੇਮਵਰਕ | L | ਢਾਂਚਾ (already used for structure) |
| traceability / baseline | ਖੋਜਯੋਗਤਾ / ਆਧਾਰ-ਰੇਖਾ | T | ਟ੍ਰੇਸੇਬਿਲਟੀ / ਬੇਸਲਾਈਨ |
| breaking change | ਤੋੜਨ ਵਾਲੀ ਤਬਦੀਲੀ | T | ਬ੍ਰੇਕਿੰਗ ਚੇਂਜ |
| account enumeration | ਖਾਤਾ ਐਨੂਮਰੇਸ਼ਨ | H | ਖਾਤਾ ਸੂਚੀਕਰਨ |
| identifier | ਪਛਾਣਕਰਤਾ (corpus precedent) | T | ਪਛਾਣਕ (standard in Panjabi software localisation) |
| domain-specific | ਖੇਤਰ-ਵਿਸ਼ੇਸ਼ | T | ਡੋਮੇਨ-ਵਿਸ਼ੇਸ਼ reads as DNS domain |

---

## Q18 — Introductory chapters retranslated to dual-block (0x04, 0x05) + `certification` pick

| | |
|---|---|
| **What changed (2026-08-22)** | `0x04-Assessment_and_Certification.md` and `0x05-For-Users-Of-4.0.md` were Panjabi-only, code-switched drafts (English words such as *vendors, verifiers, software, compliance, requirements, scope, philosophy* left in Latin inside Panjabi sentences; ਪੁਸ਼ਟੀ for "verify"). Both were retranslated in full from the current upstream English in the dual-block format, QA-gated and independently reviewed. `0x01` gained the upstream Jim Manico acknowledgement sentence. |
| **certification / certify** | **ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ** (L) — the first draft used ਪ੍ਰਮਾਣੀਕਰਨ, which is locked to *authentication*, so "OWASP does not certify vendors" read as "does not authenticate". Chapter title is now `ਮੁਲਾਂਕਣ ਅਤੇ ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ`. Alternative: ਪ੍ਰਮਾਣ-ਪੱਤਰੀਕਰਨ (T, unattested). |
| **0x05 title** | `v4.x ਦੇ ਮੁਕਾਬਲੇ ਤਬਦੀਲੀਆਂ` (literal mirror of "Changes Compared to v4.x"); earlier wrapper pages said `v4.x ਤੋਂ ਤਬਦੀਲੀਆਂ`. |
| **New picks (0x04)** | trust mark→ਭਰੋਸਾ ਚਿੰਨ੍ਹ · assurance→ਭਰੋਸਾ · stance→ਰੁਖ਼ · vendor-neutral nonprofit→ਵਿਕਰੇਤਾ-ਨਿਰਪੱਖ ਗ਼ੈਰ-ਮੁਨਾਫ਼ਾ ਸੰਸਥਾ · prescriptive→ਨਿਰਦੇਸ਼ਾਤਮਕ · testing guide→ਟੈਸਟਿੰਗ ਮਾਰਗਦਰਸ਼ਿਕਾ · penetration testing→ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟਿੰਗ (L; spelling normalised corpus-wide) · by exception→ਅਪਵਾਦ ਦੇ ਆਧਾਰ 'ਤੇ · non-applicable→ਗ਼ੈਰ-ਲਾਗੂ · rationale→ਤਰਕ-ਆਧਾਰ · findings→ਖੋਜਾਂ · work papers→ਕਾਰਜ-ਪੱਤਰ · coverage→ਕਵਰੇਜ (L; ਘੇਰਾ is locked to scope) · black box→ਬਲੈਕ ਬਾਕਸ (L) · off-the-shelf→ਤਿਆਰ-ਬਰ-ਤਿਆਰ · discouraged→ਨਿਰਉਤਸ਼ਾਹਿਤ |
| **New picks (0x05)** | users of the standard→ਵਰਤੋਂਕਾਰ (application end-users stay ਉਪਭੋਗਤਾ) · philosophy→ਫ਼ਲਸਫ਼ਾ (ਦਰਸ਼ਨ rejected, devotional) · security goal→ਸੁਰੱਖਿਆ ਟੀਚਾ vs objective→ਸੁਰੱਖਿਆ ਉਦੇਸ਼ · prescriptiveness→ਨਿਰਦੇਸ਼ਾਤਮਕਤਾ · coupling→ਜੋੜ · fallacy→ਭੁਲੇਖਾ (ਭਰਮ rejected, maya overtone) · entry level→ਪ੍ਰਵੇਸ਼ ਪੱਧਰ · taxonomy→ਵਰਗੀਕਰਨ · access delegation→ਪਹੁੰਚ ਸੌਂਪਣ · single sign-on→ਸਿੰਗਲ ਸਾਈਨ-ਔਨ (L) · tick marks→ਟਿੱਕ ਚਿੰਨ੍ਹ · backwards compatibility→ਪਿਛਲੀ ਅਨੁਕੂਲਤਾ · legacy→ਪੁਰਾਣੇ (legacy) · relative→ਸਾਪੇਖਿਕ · Minimum/Standard/Advanced→"ਘੱਟੋ-ਘੱਟ"/"ਮਿਆਰੀ"/"ਉੱਨਤ" with English retained · standalone→ਸੁਤੰਤਰ · first-layer defense→ਪਹਿਲੀ-ਪਰਤ ਰੱਖਿਆ |
| **Reviewer notes** | _to be filled_ |

---

## Q19 — August 2026 batch 3: V10, V11, V13–V17 (all security-requirement chapters now bilingual)

**Status:** all 7 files translated, mechanically QA-gated, and independently fresh-context reviewed
(V10: 1 fidelity fix — removed an added definitional gloss not in the English; V14: 2 fixes — cross-reference
title mismatch + added content; V16: 1 fix — ਸੰਭਾਲ vs ਧਾਰਨ for "retention"; V17: 1 fix — dropped "either" in
a two-outcome clause; V11/V13/V15: 0 fixes, already fidelity-correct).

### Corpus-wide normalisations applied in this batch
| Term | Was | Now |
|---|---|---|
| inventory (SBOM/asset) | ਵਸਤੂ-ਸੂਚੀ (V11) vs ਇਨਵੈਂਟਰੀ (V15, V16) | ਇਨਵੈਂਟਰੀ (L) — majority corpus usage |
| connection pool | ਸੰਪਰਕ ਪੂਲ (V13) vs ਕਨੈਕਸ਼ਨ (V4, V14, 0x05) | ਕਨੈਕਸ਼ਨ ਪੂਲ |
| retention | ਸੰਭਾਲ (V16, wrong — collides with "handling") vs ਧਾਰਨ (V14) | ਧਾਰਨ everywhere |
| error handling | ਗਲਤੀ ਸੰਭਾਲ (README, V17) vs ਗਲਤੀ ਪ੍ਰਬੰਧਨ (V14, V16) | ਗਲਤੀ ਪ੍ਰਬੰਧਨ everywhere; README row + romanisation fixed |
| encryption | ਇੰਕ੍ਰਿਪਸ਼ਨ (README) vs ਏਨਕ੍ਰਿਪਸ਼ਨ (corpus) | ਏਨਕ੍ਰਿਪਸ਼ਨ; README row + romanisation fixed |

### New picks, still open / flagged for a corpus-wide decision
| Term | Pick(s) in use | Note |
|---|---|---|
| HTTP response | ਜਵਾਬ (majority) vs ਪ੍ਰਤੀਕਿਰਿਆ (V3) | unresolved since Q13 — needs a human pass on V3 (gender agreement) |
| configure (verb) | ਸੰਰਚਿਤ ਕਰਨਾ (V13) vs ਕੌਨਫ਼ਿਗਰ ਕਰਨਾ (V12) | pick one; ਸੰਰਚਨਾ is already the locked noun |
| connection (bare, not "pool") | ਸੰਪਰਕ (V12) vs ਕਨੈਕਸ਼ਨ (V4/V13/V14) | pick one |
| proxy | ਪ੍ਰੌਕਸੀ (majority, now incl. 0x03) vs ਪ੍ਰਾਕਸੀ | normalised to ਪ੍ਰੌਕਸੀ 2026-08-22 |
| rate limiting | ਦਰ ਸੀਮਾ (majority) vs ਦਰ-ਸੀਮਾ (hyphenated) | normalised to ਦਰ ਸੀਮਾ (no hyphen) 2026-08-22 |
| performance | ਪ੍ਰਦਰਸ਼ਨ (V5, V11) | alt ਕਾਰਗੁਜ਼ਾਰੀ considered, not adopted |
| compromise (security) | ਸਮਝੌਤਾ (V6, V12, V15) | primary dictionary sense is "agreement" — flagged by V15 reviewer, not changed pending Sangat input |
| documentation (process/heading noun) | ਦਸਤਾਵੇਜ਼ੀਕਰਨ (0x03, V3, V15) vs README's ਦਸਤਾਵੇਜ਼ (document) | not a conflict — different senses; README glossary should note the split |

### Notable per-chapter picks (see individual translator reports for full lists)
- **V10 (OAuth/OIDC):** role/artifact names retained in Latin (Authorization Server, Resource Server, PKCE, DPoP,
  PAR, RAR, JAR, JARM); Relying Party=ਨਿਰਭਰ ਧਿਰ, identity provider=ਪਛਾਣ ਪ੍ਰਦਾਤਾ, claim=ਦਾਅਵਾ, consent=ਸਹਿਮਤੀ.
- **V11 (Cryptography):** primitive=ਪ੍ਰਿਮਿਟਿਵ (L), KDF=ਕੁੰਜੀ-ਵਿਉਤਪੱਤੀ ਫੰਕਸ਼ਨ, IV=ਸ਼ੁਰੂਆਤੀ ਵੈਕਟਰ (IV),
  collision resistant=ਟੱਕਰ-ਰੋਧਕ, constant-time=ਸਥਿਰ-ਸਮਾਂ, Padding Oracle/Fermat factorization retained as
  named attacks (Q11/Q15 pattern).
- **V13 (Configuration):** service account=ਸੇਵਾ ਖਾਤਾ, vault=ਵਾਲਟ (L), hardened=ਸਖ਼ਤ ਕੀਤਾ, source control=ਸਰੋਤ
  ਨਿਯੰਤਰਣ, build artifacts=ਬਿਲਡ ਆਰਟੀਫ਼ੈਕਟ (L).
- **V14 (Data Protection):** privacy-enhancing technologies=ਨਿੱਜਤਾ-ਵਧਾਊ ਤਕਨਾਲੋਜੀਆਂ, masked=ਮਾਸਕ ਕੀਤਾ (L),
  Web Cache Deception retained as a named attack; client/browser storage=ਕਲਾਇੰਟ/ਬ੍ਰਾਊਜ਼ਰ ਭੰਡਾਰਨ (V6 uses
  ਸਟੋਰੇਜ for password storage — different sense, not a conflict).
- **V15 (Secure Coding):** dependency/type confusion, TOCTOU=ਜਾਂਚ-ਦੇ-ਸਮੇਂ ਤੋਂ ਵਰਤੋਂ-ਦੇ-ਸਮੇਂ (TOCTOU), mass
  assignment/type juggling/prototype pollution retained as named vulnerability classes.
- **V16 (Logging & Error Handling):** investigation=ਤਫ਼ਤੀਸ਼ (never ਜਾਂਚ, which is locked to "check"),
  fail-open=ਫ਼ੇਲ-ਓਪਨ (L), circuit breaker=ਸਰਕਟ ਬ੍ਰੇਕਰ (L), correlation=ਸਹਿ-ਸੰਬੰਧ.
- **V17 (WebRTC):** flood (from legitimate users)=ਹੜ੍ਹ kept distinct from DoS=ਸੇਵਾ-ਇਨਕਾਰ (attack); TURN/SFU/MCU
  expansions retained Latin; heading pattern `## V17.1 TURN ਸਰਵਰ` (mixed, since "Server" translates — differs
  from the pure-retained-term Q14 pattern used for the chapter H1 itself).

---

## Maintainer

Gurvinder Singh, CISSP · CISA · GWAPT — [securityleader.ai](https://securityleader.ai) · [@GeeksikhSecurity](https://github.com/GeeksikhSecurity)
