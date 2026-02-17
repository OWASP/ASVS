# OWASP Application Security Verification Standard 5.0 - Panjabi

## ਓਵਾਸਪ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਮਿਆਰ ੫.੦

[![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Panjabi Translation](https://img.shields.io/badge/Translation-Panjabi-orange)](https://github.com/GeeksikhSecurity/ASVS)

ਇਹ OWASP Application Security Verification Standard (ASVS) ਸੰਸਕਰਣ 5.0 ਦਾ ਅਧਿਕਾਰਤ ਪੰਜਾਬੀ ਅਨੁਵਾਦ ਹੈ.

This is the official Panjabi translation of the OWASP Application Security Verification Standard (ASVS) version 5.0.

## ਬਾਰੇ | About

The OWASP ASVS ਇੱਕ ਸੁਰੱਖਿਆ ਮਿਆਰ ਹੈ ਜੋ ਸੁਰੱਖਿਅਤ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਡਿਜ਼ਾਈਨ, ਵਿਕਾਸ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ.

## ਅਨੁਵਾਦ ਟੀਮ | Translation Team

- **ਮੁੱਖ ਅਨੁਵਾਦਕ | Lead Translator**: [GeeksikhSecurity](https://github.com/GeeksikhSecurity)
- **ਸਮੀਖਿਅਕ | Reviewers**: [ਯੋਗਦਾਨ ਲਈ ਖੁੱਲ੍ਹਾ | Open for contributions]

## ਅਨੁਵਾਦ ਦੀ ਸਥਿਤੀ | Translation Status

🚧 **ਕੰਮ ਜਾਰੀ ਹੈ | Work in Progress**

ਵੇਰਵਿਆਂ ਲਈ [TRANSLATION-NOTES.md](TRANSLATION-NOTES.md) ਵੇਖੋ. | See [TRANSLATION-NOTES.md](TRANSLATION-NOTES.md) for details.

## ਅਨੁਵਾਦ ਸੰਮੇਲਨ | Translation Conventions

ਇਹ ਅਨੁਵਾਦ **ਦੋਭਾਸ਼ੀ (bilingual)** ਫਾਰਮੈਟ ਵਰਤਦਾ ਹੈ — ਹਰੇਕ ਅੰਗਰੇਜ਼ੀ ਪੈਰਾਗ੍ਰਾਫ਼ ਤੋਂ ਬਾਅਦ ਪੰਜਾਬੀ (ਗੁਰਮੁਖੀ) ਅਨੁਵਾਦ ਦਿੱਤਾ ਗਿਆ ਹੈ.

This translation uses a **bilingual** format — each English paragraph is followed by its Panjabi (Gurmukhi) translation.

### ਸ਼ਬਦ ਵਰਗੀਕਰਨ | Term Classification

| ਕਿਸਮ (Type) | ਵਰਣਨ | Description |
|:---:|---|---|
| **T** | ਅਨੁਵਾਦ — ਪੰਜਾਬੀ ਸ਼ਬਦ ਮੌਜੂਦ ਹੈ | Translate — Panjabi word exists |
| **L** | ਲਿਪੀਅੰਤਰਣ — ਅੰਗਰੇਜ਼ੀ ਗੁਰਮੁਖੀ ਵਿੱਚ | Transliterate — English rendered in Gurmukhi |
| **R** | ਅੰਗਰੇਜ਼ੀ ਰੱਖੋ — ਯੂਨੀਵਰਸਲ ਐਕਰੋਨਿਮ | Retain English — Universal acronyms |
| **H** | ਮਿਸ਼ਰਤ — ਗੁਰਮੁਖੀ + ਅੰਗਰੇਜ਼ੀ | Hybrid — Gurmukhi + English |

## ਸ਼ਬਦਾਵਲੀ | Glossary

### ਮੁੱਖ ਸ਼ਬਦ | Core Terms

| English | ਗੁਰਮੁਖੀ | Romanized / ਰੋਮਨ ਲਿਪੀ | ਕਿਸਮ |
|---------|---------|----------------------|:---:|
| Security | ਸੁਰੱਖਿਆ | surakkhiā | T |
| Verification | ਤਸਦੀਕ | tasdīk | T |
| Standard | ਮਿਆਰ | miār | T |
| Application | ਐਪਲੀਕੇਸ਼ਨ | aipalīkeshan | L |
| Requirement | ਲੋੜ | loṛ | T |
| Level | ਪੱਧਰ | paddhar | T |
| Control | ਨਿਯੰਤਰਣ | niyaṅtraṇ | T |
| Scope | ਘੇਰਾ | gherā | T |
| Objective | ਉਦੇਸ਼ | udesh | T |
| Documentation | ਦਸਤਾਵੇਜ਼ | dastāvez | T |

### ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਪਛਾਣ | Authentication & Identity

| English | ਗੁਰਮੁਖੀ | Romanized / ਰੋਮਨ ਲਿਪੀ | ਕਿਸਮ |
|---------|---------|----------------------|:---:|
| Authentication | ਪ੍ਰਮਾਣੀਕਰਨ | pramāṇīkaran | T |
| Authorization | ਅਧਿਕਾਰ | adhikār | T |
| Identity | ਪਛਾਣ | pachāṇ | T |
| Credential | ਪ੍ਰਮਾਣ-ਪੱਤਰ | pramāṇ-pattar | T |
| Password | ਪਾਸਵਰਡ | pāsvarḍ | L |
| Multi-factor authentication | ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ | bahu-kārak pramāṇīkaran | T |
| Identity Provider (IdP) | ਪਛਾਣ ਪ੍ਰਦਾਤਾ | pachāṇ pradātā | T |
| One-time Password (OTP) | ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ | ikk-vārī pāsvarḍ | H |
| Passkey | ਪਾਸਕੀ | pāskī | L |
| Session | ਸੈਸ਼ਨ | saishan | L |
| Session Management | ਸੈਸ਼ਨ ਪ੍ਰਬੰਧ | saishan prabanndh | H |
| Timeout | ਸਮਾਂ-ਸੀਮਾ | samāṅ-sīmā | T |
| Token | ਟੋਕਨ | ṭokan | L |

### ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ | Cryptography

| English | ਗੁਰਮੁਖੀ | Romanized / ਰੋਮਨ ਲਿਪੀ | ਕਿਸਮ |
|---------|---------|----------------------|:---:|
| Cryptography | ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ | kripṭogrāfī | L |
| Encryption | ਇੰਕ੍ਰਿਪਸ਼ਨ | iṅkripshan | L |
| Hash | ਹੈਸ਼ | haish | L |
| Digital Signature | ਡਿਜ਼ੀਟਲ ਦਸਤਖ਼ਤ | ḍizīṭal dastakhat | H |
| Key | ਕੁੰਜੀ | kunjī | T |
| Certificate | ਸਰਟੀਫਿਕੇਟ | sarṭīfikeṭ | L |
| Public Key Infrastructure (PKI) | ਜਨਤਕ ਕੁੰਜੀ ਢਾਂਚਾ | jantak kunjī ḍhāṅchā | T |
| Transport Layer Security (TLS) | ਟ੍ਰਾਂਸਪੋਰਟ ਲੇਅਰ ਸੁਰੱਖਿਆ | ṭrāṅsporṭ leyar surakkhiā | H |

### ਹਮਲੇ ਅਤੇ ਕਮਜ਼ੋਰੀਆਂ | Attacks & Vulnerabilities

| English | ਗੁਰਮੁਖੀ | Romanized / ਰੋਮਨ ਲਿਪੀ | ਕਿਸਮ |
|---------|---------|----------------------|:---:|
| Vulnerability | ਕਮਜ਼ੋਰੀ | kamzorī | T |
| Threat | ਖ਼ਤਰਾ | khatrā | T |
| Attack | ਹਮਲਾ | hamlā | T |
| Injection | ਇੰਜੈਕਸ਼ਨ | iṅjaikshan | L |
| SQL Injection (SQLi) | ਐੱਸ.ਕਿਊ.ਐੱਲ. ਇੰਜੈਕਸ਼ਨ | ais.kiū.ail. iṅjaikshan | L |
| Cross-Site Scripting (XSS) | ਕਰਾਸ-ਸਾਈਟ ਸਕ੍ਰਿਪਟਿੰਗ | karās-sāīṭ skripṭiṅg | L |
| Server-side Request Forgery (SSRF) | ਸਰਵਰ-ਪੱਖੀ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ | sarvar-pakkhī bentī jāalsāzī | H |
| Brute Force | ਬਰੂਟ ਫੋਰਸ | barūṭ fors | L |
| Malware | ਮਾਲਵੇਅਰ | mālveyar | L |
| Forgery | ਜਾਅਲਸਾਜ਼ੀ | jāalsāzī | T |
| Threat Modeling | ਖ਼ਤਰਾ ਮਾਡਲਿੰਗ | khatrā māḍliṅg | H |

### ਡਾਟਾ ਸੁਰੱਖਿਆ | Data Protection

| English | ਗੁਰਮੁਖੀ | Romanized / ਰੋਮਨ ਲਿਪੀ | ਕਿਸਮ |
|---------|---------|----------------------|:---:|
| Data Protection | ਡਾਟਾ ਸੁਰੱਖਿਆ | ḍāṭā surakkhiā | H |
| Privacy | ਨਿੱਜਤਾ | nijjatā | T |
| Confidentiality | ਗੁਪਤਤਾ | guptatā | T |
| Integrity | ਅਖੰਡਤਾ | akhaṇḍatā | T |
| Availability | ਉਪਲਬਧਤਾ | upalabdhatā | T |

### ਵੈੱਬ ਅਤੇ ਏ.ਪੀ.ਆਈ. | Web & API

| English | ਗੁਰਮੁਖੀ | Romanized / ਰੋਮਨ ਲਿਪੀ | ਕਿਸਮ |
|---------|---------|----------------------|:---:|
| Web Service | ਵੈੱਬ ਸੇਵਾ | vaib sevā | H |
| Web Frontend | ਵੈੱਬ ਫਰੰਟਐਂਡ | vaib fraṅṭaiṅḍ | L |
| Cookie | ਕੁਕੀ | kukī | L |
| Encoding | ਏਨਕੋਡਿੰਗ | enkoḍiṅg | L |
| Sanitization | ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ | sainīṭāīzeshan | L |
| Validation | ਪ੍ਰਮਾਣਿਕਤਾ | pramāṇiktā | T |
| Input Validation | ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ | inpuṭṭ pramāṇiktā | H |
| Allowlist | ਮਨਜ਼ੂਰੀ ਸੂਚੀ | manzūrī sūchī | T |
| File Handling | ਫਾਈਲ ਸੰਭਾਲ | fāīl saṅbhāl | H |

### ਟੈਸਟਿੰਗ ਅਤੇ ਵਿਕਾਸ | Testing & Development

| English | ਗੁਰਮੁਖੀ | Romanized / ਰੋਮਨ ਲਿਪੀ | ਕਿਸਮ |
|---------|---------|----------------------|:---:|
| SAST | ਸਥਿਰ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਟੈਸਟਿੰਗ | sathir aipalīkeshan surakkhiā ṭaisṭiṅg | H |
| DAST | ਗਤੀਸ਼ੀਲ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਟੈਸਟਿੰਗ | gatīshīl aipalīkeshan surakkhiā ṭaisṭiṅg | H |
| Verifier | ਤਸਦੀਕਕਰਤਾ | tasdīkkartā | T |
| Architecture | ਢਾਂਚਾ | ḍhāṅchā | T |
| Configuration | ਸੰਰਚਨਾ | saṅrachnā | T |
| Secure Coding | ਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ | surakhiat koḍiṅg | H |
| Error Handling | ਗਲਤੀ ਸੰਭਾਲ | galtī saṅbhāl | T |
| Logging | ਲੌਗਿੰਗ | laugiṅg | L |
| SDLC | ਸਾਫ਼ਟਵੇਅਰ ਵਿਕਾਸ ਜੀਵਨ-ਚੱਕਰ | sāfṭveyar vikās jīvan-chakkar | H |
| SBOM | ਸਾਫ਼ਟਵੇਅਰ ਸਮੱਗਰੀ ਸੂਚੀ | sāfṭveyar samaggrī sūchī | H |

### ਐਕਰੋਨਿਮ (ਅੰਗਰੇਜ਼ੀ ਰੱਖੋ) | Acronyms (Retain English)

| Acronym | Full Form | ਗੁਰਮੁਖੀ ਉਚਾਰਨ |
|---------|-----------|------------|
| OWASP | Open Worldwide Application Security Project | ਓਵਾਸਪ |
| ASVS | Application Security Verification Standard | ਏ.ਐਸ.ਵੀ.ਐਸ. |
| API | Application Programming Interface | ਏ.ਪੀ.ਆਈ. |
| HTTP / HTTPS | HyperText Transfer Protocol (Secure) | ਐੱਚ.ਟੀ.ਟੀ.ਪੀ.(ਐੱਸ.) |
| TLS | Transport Layer Security | ਟੀ.ਐੱਲ.ਐੱਸ. |
| JWT | JSON Web Token | ਜੇ.ਡਬਲਯੂ.ਟੀ. |
| OAuth | Open Authorization | ਓਅਥ |
| OIDC | OpenID Connect | ਓ.ਆਈ.ਡੀ.ਸੀ. |
| SAML | Security Assertion Markup Language | ਐੱਸ.ਏ.ਐੱਮ.ਐੱਲ. |
| MFA | Multi-factor Authentication | ਐੱਮ.ਐੱਫ਼.ਏ. |
| NIST | National Institute of Standards and Technology | ਐੱਨ.ਆਈ.ਐੱਸ.ਟੀ. |
| CWE | Common Weakness Enumeration | ਸੀ.ਡਬਲਯੂ.ਈ. |
| SIEM | Security Information and Event Management | ਐੱਸ.ਆਈ.ਈ.ਐੱਮ. |
| WebRTC | Web Real-Time Communication | ਵੈੱਬਆਰ.ਟੀ.ਸੀ. |

> **ਪੂਰੀ ਸ਼ਬਦਾਵਲੀ** (152+ ਸ਼ਬਦ) ਲਈ ਵੇਖੋ: [OWASP ASVS Glossary (JSON)](https://github.com/GeeksikhSecurity/ASVS/blob/panjabi-translation-v5/5.0/pa-IN/asvs_glossary.json)

## ਯੋਗਦਾਨ | Contributing

ਅਸੀਂ ਪੰਜਾਬੀ ਬੋਲਣ ਵਾਲੇ ਸੁਰੱਖਿਆ ਪੇਸ਼ੇਵਰਾਂ ਦਾ ਸਵਾਗਤ ਕਰਦੇ ਹਾਂ.

We welcome contributions from Panjabi-speaking security professionals.

### ਸਮੀਖਿਆ ਕਿਵੇਂ ਕਰੀਏ | How to Review

1. ਫ਼ਾਈਲਾਂ ਵਿੱਚ ਅੰਗਰੇਜ਼ੀ ਅਤੇ ਪੰਜਾਬੀ ਦੀ ਤੁਲਨਾ ਕਰੋ | Compare English and Panjabi in each file
2. ਗੁਰਮੁਖੀ ਸ਼ਬਦ-ਜੋੜ ਦੀ ਜਾਂਚ ਕਰੋ | Check Gurmukhi spelling
3. ਤਕਨੀਕੀ ਸ਼ੁੱਧਤਾ ਦੀ ਤਸਦੀਕ ਕਰੋ | Verify technical accuracy
4. GitHub issue ਜਾਂ PR comment ਰਾਹੀਂ ਫ਼ੀਡਬੈਕ ਦਿਓ | Provide feedback via GitHub issue or PR comment

---
*Translation maintained by [GeeksikhSecurity](https://github.com/GeeksikhSecurity)*
