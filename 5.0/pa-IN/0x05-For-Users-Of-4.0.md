<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x05-For-Users-Of-4.0.md -->
<!-- Translator: GeeksikhSecurity -->

# v4.x ਦੇ ਮੁਕਾਬਲੇ ਤਬਦੀਲੀਆਂ (Changes Compared to v4.x)

## ਜਾਣ-ਪਛਾਣ (Introduction)

ਮਿਆਰ ਦੇ version 4.x ਤੋਂ ਜਾਣੂ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ version 5.0 ਵਿੱਚ ਪੇਸ਼ ਕੀਤੀਆਂ ਗਈਆਂ ਮੁੱਖ ਤਬਦੀਲੀਆਂ ਦੀ ਸਮੀਖਿਆ ਕਰਨਾ ਮਦਦਗਾਰ ਹੋ ਸਕਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ content, scope, ਅਤੇ ਅੰਤਰਨਿਹਿਤ philosophy ਵਿੱਚ ਅਪਡੇਟ ਸ਼ਾਮਲ ਹਨ।

Version 4.0.3 ਦੀਆਂ 286 requirements ਵਿੱਚੋਂ, ਸਿਰਫ਼ 11 ਬਿਨਾਂ ਤਬਦੀਲੀ ਦੇ ਰਹਿ ਗਈਆਂ ਹਨ, ਜਦਕਿ 15 ਵਿੱਚ ਉਹਨਾਂ ਦੇ ਅਰਥ ਨੂੰ ਬਦਲੇ ਬਿਨਾਂ ਮਾਮੂਲੀ ਵਿਆਕਰਣਿਕ ਸੁਧਾਰ ਕੀਤੇ ਗਏ ਹਨ। ਕੁੱਲ ਮਿਲਾ ਕੇ 109 requirements (38%) ਹੁਣ version 5.0 ਵਿੱਚ ਵੱਖਰੀਆਂ requirements ਨਹੀਂ ਹਨ ਜਿਸ ਵਿੱਚ 50 ਨੂੰ ਸਿਰਫ਼ ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ, 28 ਨੂੰ duplicates ਵਜੋਂ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ ਅਤੇ 31 ਨੂੰ ਹੋਰ requirements ਵਿੱਚ ਮਿਲਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਬਾਕੀ ਨੂੰ ਕਿਸੇ ਨਾ ਕਿਸੇ ਤਰੀਕੇ ਨਾਲ ਸੰਸ਼ੋਧਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਇੱਥੋਂ ਤੱਕ ਕਿ ਜਿਨ੍ਹਾਂ requirements ਨੂੰ ਮਹੱਤਵਪੂਰਨ ਰੂਪ ਵਿੱਚ ਸੰਸ਼ੋਧਿਤ ਨਹੀਂ ਕੀਤਾ ਗਿਆ ਸੀ, ਉਹਨਾਂ ਦੇ reordering ਜਾਂ restructuring ਕਾਰਨ ਵੱਖਰੇ identifiers ਹਨ।

Version 5.0 ਦੇ ਅਪਣਾਉਣ ਨੂੰ ਸੁਵਿਧਾਜਨਕ ਬਣਾਉਣ ਲਈ, mapping documents ਪ੍ਰਦਾਨ ਕੀਤੇ ਗਏ ਹਨ ਜੋ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਇਹ ਪਤਾ ਲਗਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ ਕਿ version 4.x ਦੀਆਂ requirements version 5.0 ਵਿੱਚ ਕਿਵੇਂ ਮੇਲ ਖਾਂਦੀਆਂ ਹਨ। ਇਹ mappings release versioning ਨਾਲ ਬੰਨ੍ਹੀਆਂ ਨਹੀਂ ਹਨ ਅਤੇ ਲੋੜ ਅਨੁਸਾਰ ਅਪਡੇਟ ਜਾਂ ਸਪਸ਼ਟ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।

## Requirement Philosophy

### Scope ਅਤੇ Focus

Version 4.x ਵਿੱਚ ਅਜਿਹੀਆਂ requirements ਸ਼ਾਮਲ ਸਨ ਜੋ ਮਿਆਰ ਦੇ ਇਰਾਦੇ ਵਾਲੇ scope ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦੀਆਂ ਸਨ; ਇਹਨਾਂ ਨੂੰ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਉਹ requirements ਜੋ 5.0 ਲਈ scope criteria ਨੂੰ ਪੂਰਾ ਨਹੀਂ ਕਰਦੀਆਂ ਸਨ ਜਾਂ ਪੁਸ਼ਟੀਯੋਗ ਨਹੀਂ ਸਨ, ਉਹਨਾਂ ਨੂੰ ਵੀ ਬਾਹਰ ਰੱਖਿਆ ਗਿਆ ਹੈ।

### Mechanisms ਦੇ ਮੁਕਾਬਲੇ Security Goals 'ਤੇ ਜ਼ੋਰ

Version 4.x ਵਿੱਚ, ਬਹੁਤ ਸਾਰੀਆਂ requirements ਅੰਤਰਨਿਹਿਤ security objectives ਦੀ ਬਜਾਏ ਖਾਸ mechanisms 'ਤੇ ਕੇਂਦਰਿਤ ਸਨ। Version 5.0 ਵਿੱਚ, requirements security goals 'ਤੇ ਕੇਂਦਰਿਤ ਹਨ, ਖਾਸ mechanisms ਦਾ ਹਵਾਲਾ ਸਿਰਫ਼ ਉਦੋਂ ਦਿੰਦੀਆਂ ਹਨ ਜਦੋਂ ਉਹ ਇਕਲੌਤਾ ਵਿਹਾਰਕ ਹੱਲ ਹੋਣ, ਜਾਂ ਉਹਨਾਂ ਨੂੰ examples ਜਾਂ ਪੂਰਕ guidance ਵਜੋਂ ਪ੍ਰਦਾਨ ਕਰਦੀਆਂ ਹਨ।

ਇਹ ਪਹੁੰਚ ਇਸ ਗੱਲ ਨੂੰ ਮਾਨਤਾ ਦਿੰਦੀ ਹੈ ਕਿ ਇੱਕ ਦਿੱਤੇ security objective ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਈ ਤਰੀਕੇ ਮੌਜੂਦ ਹੋ ਸਕਦੇ ਹਨ, ਅਤੇ ਬੇਲੋੜੀ prescriptiveness ਤੋਂ ਬਚਦੀ ਹੈ ਜੋ ਸੰਸਥਾਗਤ ਲਚਕ ਨੂੰ ਸੀਮਿਤ ਕਰ ਸਕਦੀ ਹੈ।

ਇਸ ਤੋਂ ਇਲਾਵਾ, ਸਮਾਨ security concern ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਵਾਲੀਆਂ requirements ਨੂੰ ਉਚਿਤ ਸਥਾਨਾਂ 'ਤੇ ਇਕਜੁਟ ਕੀਤਾ ਗਿਆ ਹੈ।

### ਦਸਤਾਵੇਜ਼ੀ Security Decisions

ਹਾਲਾਂਕਿ documented security decisions ਦੀ ਧਾਰਨਾ version 5.0 ਵਿੱਚ ਨਵੀਂ ਲੱਗ ਸਕਦੀ ਹੈ, ਇਹ version 4.0 ਵਿੱਚ policy application ਅਤੇ threat modeling ਨਾਲ ਸਬੰਧਤ ਪਹਿਲੀਆਂ requirements ਦਾ ਵਿਕਾਸ ਹੈ। ਪਹਿਲਾਂ, ਕੁਝ requirements ਅਸਪਸ਼ਟ ਰੂਪ ਵਿੱਚ security controls ਦੇ implementation ਨੂੰ ਸੂਚਿਤ ਕਰਨ ਲਈ analysis ਦੀ ਮੰਗ ਕਰਦੀਆਂ ਸਨ, ਜਿਵੇਂ ਕਿ ਮਨਜ਼ੂਰ network connections ਨਿਰਧਾਰਿਤ ਕਰਨਾ।

ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ implementation ਅਤੇ verification ਲਈ ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਉਪਲਬਧ ਹੈ, ਇਹਨਾਂ ਉਮੀਦਾਂ ਨੂੰ ਹੁਣ ਸਪਸ਼ਟ ਰੂਪ ਵਿੱਚ documentation requirements ਵਜੋਂ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਿਸ ਨਾਲ ਉਹ ਸਪਸ਼ਟ, ਕਾਰਯਯੋਗ ਅਤੇ ਪੁਸ਼ਟੀਯੋਗ ਬਣ ਗਈਆਂ ਹਨ।

## ਢਾਂਚਾਗਤ ਤਬਦੀਲੀਆਂ ਅਤੇ ਨਵੇਂ ਅਧਿਆਇ (Structural Changes and New Chapters)

Version 5.0 ਵਿੱਚ ਕਈ ਅਧਿਆਇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਨਵੀਂ ਸਮੱਗਰੀ ਪੇਸ਼ ਕਰਦੇ ਹਨ:

* OAuth ਅਤੇ OIDC – access delegation ਅਤੇ single sign-on ਲਈ ਇਹਨਾਂ protocols ਦੇ ਵਿਆਪਕ ਅਪਣਾਉਣ ਨੂੰ ਦੇਖਦੇ ਹੋਏ, developers ਦੇ ਸਾਹਮਣੇ ਆਉਣ ਵਾਲੇ ਵਿਭਿੰਨ scenarios ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਲਈ ਸਮਰਪਿਤ requirements ਸ਼ਾਮਲ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। ਇਹ ਖੇਤਰ ਅੰਤ ਵਿੱਚ ਇੱਕ ਸਟੈਂਡਅਲੋਨ ਮਿਆਰ ਵਿੱਚ ਵਿਕਸਿਤ ਹੋ ਸਕਦਾ ਹੈ, ਪਿਛਲੇ versions ਵਿੱਚ Mobile ਅਤੇ IoT requirements ਦੇ ਇਲਾਜ ਦੇ ਸਮਾਨ।
* WebRTC – ਜਿਵੇਂ ਕਿ ਇਹ ਤਕਨਾਲੋਜੀ ਪ੍ਰਸਿੱਧੀ ਪ੍ਰਾਪਤ ਕਰ ਰਹੀ ਹੈ, ਇਸ ਦੇ ਵਿਲੱਖਣ security considerations ਅਤੇ ਚੁਣੌਤੀਆਂ ਨੂੰ ਹੁਣ ਇੱਕ ਸਮਰਪਿਤ ਭਾਗ ਵਿੱਚ ਸੰਬੋਧਿਤ ਕੀਤਾ ਗਿਆ ਹੈ।

ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਵੀ ਕੋਸ਼ਿਸ਼ਾਂ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ ਕਿ ਅਧਿਆਇ ਅਤੇ ਭਾਗ ਸਬੰਧਤ requirements ਦੇ ਸੁਸੰਗਤ ਸਮੂਹਾਂ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਸੰਗਠਿਤ ਹੋਣ।

ਇਸ restructuring ਨੇ ਵਾਧੂ ਅਧਿਆਇ ਬਣਾਉਣ ਦਾ ਕਾਰਨ ਬਣਾਇਆ ਹੈ:

* Self-contained Tokens – ਪਹਿਲਾਂ session management ਦੇ ਅਧੀਨ ਸਮੂਹਬੱਧ, self-contained tokens ਨੂੰ ਹੁਣ ਇੱਕ ਵੱਖਰੀ mechanism ਅਤੇ stateless communication (ਜਿਵੇਂ OAuth ਅਤੇ OIDC ਵਿੱਚ) ਲਈ ਇੱਕ ਬੁਨਿਆਦੀ ਤੱਤ ਵਜੋਂ ਮਾਨਤਾ ਦਿੱਤੀ ਗਈ ਹੈ। ਉਹਨਾਂ ਦੇ ਵਿਲੱਖਣ security implications ਕਾਰਨ, ਉਹਨਾਂ ਨੂੰ ਇੱਕ ਸਮਰਪਿਤ ਅਧਿਆਇ ਵਿੱਚ ਸੰਬੋਧਿਤ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਿਸ ਵਿੱਚ version 5.x ਵਿੱਚ ਕੁਝ ਨਵੀਆਂ requirements ਪੇਸ਼ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ।
* Web Frontend Security – browser-based applications ਦੀ ਵਧਦੀ ਗੁੰਝਲਤਾ ਅਤੇ API-only architectures ਦੇ ਉਭਾਰ ਦੇ ਨਾਲ, frontend security requirements ਨੂੰ ਉਹਨਾਂ ਦੇ ਆਪਣੇ ਅਧਿਆਇ ਵਿੱਚ ਵੱਖ ਕੀਤਾ ਗਿਆ ਹੈ।
* Secure Coding and Architecture – ਆਮ security practices ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਵਾਲੀਆਂ ਨਵੀਆਂ requirements ਜੋ ਮੌਜੂਦਾ ਅਧਿਆਇਆਂ ਵਿੱਚ ਫਿੱਟ ਨਹੀਂ ਸਨ, ਉਹਨਾਂ ਨੂੰ ਇੱਥੇ ਸਮੂਹਬੱਧ ਕੀਤਾ ਗਿਆ ਹੈ।

Version 5.0 ਵਿੱਚ ਹੋਰ ਸੰਗਠਨਾਤਮਕ ਤਬਦੀਲੀਆਂ ਇਰਾਦੇ ਨੂੰ ਸਪਸ਼ਟ ਕਰਨ ਲਈ ਕੀਤੀਆਂ ਗਈਆਂ ਸਨ। ਉਦਾਹਰਨ ਲਈ, input validation requirements ਨੂੰ business logic ਦੇ ਨਾਲ ਲਿਜਾਇਆ ਗਿਆ, ਜੋ business rules ਨੂੰ ਲਾਗੂ ਕਰਨ ਵਿੱਚ ਉਹਨਾਂ ਦੀ ਭੂਮਿਕਾ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ, ਨਾ ਕਿ sanitization ਅਤੇ encoding ਨਾਲ ਸਮੂਹਬੱਧ ਹੋਣਾ।

ਪੁਰਾਣੇ V1 Architecture ਅਧਿਆਇ ਨੂੰ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਇਸ ਦੇ ਸ਼ੁਰੂਆਤੀ ਭਾਗ ਵਿੱਚ ਅਜਿਹੀਆਂ requirements ਸਨ ਜੋ scope ਤੋਂ ਬਾਹਰ ਸਨ, ਜਦਕਿ ਬਾਅਦ ਦੇ ਭਾਗਾਂ ਨੂੰ ਸੰਬੰਧਿਤ ਅਧਿਆਇਆਂ ਵਿੱਚ ਮੁੜ ਵੰਡਿਆ ਗਿਆ ਹੈ, ਜਿਸ ਵਿੱਚ requirements ਨੂੰ deduplicated ਅਤੇ ਜ਼ਰੂਰਤ ਅਨੁਸਾਰ ਸਪਸ਼ਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਹੋਰ ਮਿਆਰਾਂ ਨਾਲ ਸਿੱਧੇ Mappings ਨੂੰ ਹਟਾਉਣਾ

ਮਿਆਰ ਦੇ ਮੁੱਖ ਭਾਗ ਤੋਂ ਹੋਰ ਮਿਆਰਾਂ ਨਾਲ ਸਿੱਧੇ mappings ਨੂੰ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਉਦੇਸ਼ OWASP Common Requirement Enumeration (CRE) project ਦੇ ਨਾਲ ਇੱਕ mapping ਤਿਆਰ ਕਰਨਾ ਹੈ, ਜੋ ਬਦਲੇ ਵਿੱਚ ASVS ਨੂੰ OWASP projects ਅਤੇ ਬਾਹਰੀ ਮਿਆਰਾਂ ਦੀ ਇੱਕ ਸ਼ਰੇਣੀ ਨਾਲ ਜੋੜੇਗਾ।

CWE ਅਤੇ NIST ਨਾਲ ਸਿੱਧੇ mappings ਹੁਣ ਬਰਕਰਾਰ ਨਹੀਂ ਰੱਖੇ ਜਾਂਦੇ, ਜਿਵੇਂ ਕਿ ਹੇਠਾਂ ਸਮਝਾਇਆ ਗਿਆ ਹੈ।

### NIST Digital Identity Guidelines ਨਾਲ ਘਟਾਇਆ ਗਿਆ Coupling

NIST [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) ਲੰਬੇ ਸਮੇਂ ਤੋਂ authentication ਅਤੇ authorization controls ਲਈ ਇੱਕ ਸੰਦਰਭ ਵਜੋਂ ਕੰਮ ਕਰਦੇ ਰਹੇ ਹਨ। Version 4.x ਵਿੱਚ, ਕੁਝ ਅਧਿਆਇ NIST ਦੇ structure ਅਤੇ terminology ਨਾਲ ਨੇੜਿਓਂ ਮੇਲ ਖਾਂਦੇ ਸਨ।

ਹਾਲਾਂਕਿ ਇਹ guidelines ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਸੰਦਰਭ ਬਣੀਆਂ ਰਹਿੰਦੀਆਂ ਹਨ, ਸਖਤ alignment ਨੇ ਚੁਣੌਤੀਆਂ ਪੇਸ਼ ਕੀਤੀਆਂ, ਜਿਸ ਵਿੱਚ ਘੱਟ ਵਿਆਪਕ ਤੌਰ 'ਤੇ ਮਾਨਤਾ ਪ੍ਰਾਪਤ terminology, ਸਮਾਨ requirements ਦਾ duplication, ਅਤੇ ਅਧੂਰੇ mappings ਸ਼ਾਮਲ ਹਨ। Version 5.0 ਸਪਸ਼ਟਤਾ ਅਤੇ ਪ੍ਰਸੰਗਿਕਤਾ ਨੂੰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ ਇਸ ਪਹੁੰਚ ਤੋਂ ਦੂਰ ਜਾਂਦਾ ਹੈ।

### Common Weakness Enumeration (CWE) ਤੋਂ ਦੂਰ ਜਾਣਾ

[Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) software security weaknesses ਦੀ ਇੱਕ ਉਪਯੋਗੀ taxonomy ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਹਾਲਾਂਕਿ, category-only CWEs, requirements ਨੂੰ ਇੱਕ ਸਿੰਗਲ CWE ਨਾਲ map ਕਰਨ ਵਿੱਚ ਮੁਸ਼ਕਿਲਾਂ, ਅਤੇ version 4.x ਵਿੱਚ ਅਸਪਸ਼ਟ mappings ਦੀ ਮੌਜੂਦਗੀ ਵਰਗੀਆਂ ਚੁਣੌਤੀਆਂ ਨੇ version 5.0 ਵਿੱਚ ਸਿੱਧੇ CWE mappings ਨੂੰ ਬੰਦ ਕਰਨ ਦਾ ਫੈਸਲਾ ਲਿਆ ਹੈ।

## Level Definitions ਨੂੰ ਮੁੜ ਸੋਚਣਾ

Version 4.x ਨੇ levels ਨੂੰ L1 ("Minimum"), L2 ("Standard"), ਅਤੇ L3 ("Advanced") ਵਜੋਂ ਵਰਣਨ ਕੀਤਾ, ਇਸ ਸੰਕੇਤ ਦੇ ਨਾਲ ਕਿ sensitive data ਨੂੰ ਸੰਭਾਲਣ ਵਾਲੀਆਂ ਸਾਰੀਆਂ applications ਨੂੰ ਘੱਟੋ-ਘੱਟ L2 ਨੂੰ ਪੂਰਾ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।

Version 5.0 ਇਸ ਪਹੁੰਚ ਦੇ ਨਾਲ ਕਈ ਮੁੱਦਿਆਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਦਾ ਹੈ ਜੋ ਅਗਲੇ ਪੈਰਾਗ੍ਰਾਫਾਂ ਵਿੱਚ ਵਰਣਨ ਕੀਤੇ ਗਏ ਹਨ।

ਇੱਕ ਵਿਹਾਰਕ ਮਾਮਲੇ ਵਜੋਂ, ਜਦਕਿ version 4.x level indicators ਲਈ tick marks ਵਰਤਦਾ ਸੀ, 5.x markdown, PDF, DOCX, CSV, JSON ਅਤੇ XML ਸਮੇਤ ਮਿਆਰ ਦੇ ਸਾਰੇ formats 'ਤੇ ਇੱਕ ਸਧਾਰਨ ਨੰਬਰ ਵਰਤਦਾ ਹੈ। Backwards compatibility ਲਈ, CSV, JSON ਅਤੇ XML outputs ਦੇ legacy versions ਜੋ ਅਜੇ ਵੀ tick marks ਵਰਤਦੇ ਹਨ, ਉਹ ਵੀ ਤਿਆਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

### ਆਸਾਨ Entry Level

Feedback ਨੇ ਸੰਕੇਤ ਦਿੱਤਾ ਕਿ Level 1 requirements (~120) ਦੀ ਵੱਡੀ ਸੰਖਿਆ, ਇਸ ਦੇ "minimum" level ਵਜੋਂ designation ਦੇ ਨਾਲ ਜੋ ਜ਼ਿਆਦਾਤਰ applications ਲਈ ਕਾਫੀ ਨਹੀਂ ਹੈ, ਨੇ adoption ਨੂੰ ਹਤੋਤਸਾਹਿਤ ਕੀਤਾ। Version 5.0 ਦਾ ਉਦੇਸ਼ Level 1 ਨੂੰ ਮੁੱਖ ਤੌਰ 'ਤੇ first-layer defense requirements ਦੇ ਆਲੇ-ਦੁਆਲੇ ਪਰਿਭਾਸ਼ਿਤ ਕਰਕੇ ਇਸ ਰੁਕਾਵਟ ਨੂੰ ਘਟਾਉਣਾ ਹੈ, ਜਿਸ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਉਸ ਪੱਧਰ 'ਤੇ ਸਪਸ਼ਟ ਅਤੇ ਘੱਟ requirements ਹਨ। ਇਸ ਨੂੰ ਸੰਖਿਆਤਮਕ ਰੂਪ ਵਿੱਚ ਦਿਖਾਉਣ ਲਈ, v4.0.3 ਵਿੱਚ ਕੁੱਲ 278 requirements ਵਿੱਚੋਂ 128 L1 requirements ਸਨ, ਜੋ 46% ਦਰਸਾਉਂਦੀਆਂ ਹਨ। 5.0.0 ਵਿੱਚ ਕੁੱਲ 345 requirements ਵਿੱਚੋਂ 70 L1 requirements ਹਨ, ਜੋ 20% ਦਰਸਾਉਂਦੀਆਂ ਹਨ।

### Testability ਦੀ ਭਰਮ

Version 4.x ਵਿੱਚ Level 1 ਲਈ controls ਚੁਣਨ ਵਿੱਚ ਇੱਕ ਮੁੱਖ ਕਾਰਕ "black box" external penetration testing ਦੁਆਰਾ assessment ਲਈ ਉਹਨਾਂ ਦੀ ਅਨੁਕੂਲਤਾ ਸੀ। ਹਾਲਾਂਕਿ, ਇਹ ਪਹੁੰਚ Level 1 ਦੇ minimum set of security controls ਦੇ ਇਰਾਦੇ ਨਾਲ ਪੂਰੀ ਤਰ੍ਹਾਂ ਮੇਲ ਨਹੀਂ ਖਾਂਦੀ ਸੀ। ਕੁਝ ਉਪਭੋਗਤਾਵਾਂ ਨੇ ਦਲੀਲ ਦਿੱਤੀ ਕਿ Level 1 applications ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਨਾਕਾਫੀ ਸੀ, ਜਦਕਿ ਹੋਰਾਂ ਨੇ ਇਸ ਨੂੰ test ਕਰਨਾ ਬਹੁਤ ਮੁਸ਼ਕਿਲ ਪਾਇਆ।

Testability ਨੂੰ ਇੱਕ ਮਾਪਦੰਡ ਵਜੋਂ ਭਰੋਸਾ ਕਰਨਾ ਦੋਵੇਂ ਰਿਸ਼ਤੇਦਾਰ ਅਤੇ, ਕਈ ਵਾਰ, ਭਰਮ ਪੈਦਾ ਕਰਨ ਵਾਲਾ ਹੈ। ਇਹ ਤੱਥ ਕਿ ਇੱਕ requirement testable ਹੈ ਇਸ ਗੱਲ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ ਦਿੰਦਾ ਕਿ ਇਸ ਨੂੰ automated ਜਾਂ ਸਿੱਧੇ ਤਰੀਕੇ ਨਾਲ test ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਇਸ ਤੋਂ ਇਲਾਵਾ, ਸਭ ਤੋਂ ਆਸਾਨੀ ਨਾਲ testable requirements ਹਮੇਸ਼ਾ ਉਹ ਨਹੀਂ ਹੁੰਦੀਆਂ ਜਿਨ੍ਹਾਂ ਦਾ ਸਭ ਤੋਂ ਵੱਡਾ security impact ਜਾਂ implement ਕਰਨਾ ਸਭ ਤੋਂ ਸਧਾਰਨ ਹੋਵੇ।

ਇਸ ਤਰ੍ਹਾਂ, version 5.0 ਵਿੱਚ, level decisions ਮੁੱਖ ਤੌਰ 'ਤੇ risk reduction ਦੇ ਆਧਾਰ 'ਤੇ ਕੀਤੇ ਗਏ ਸਨ ਅਤੇ implement ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਨੂੰ ਵੀ ਧਿਆਨ ਵਿੱਚ ਰੱਖਿਆ ਗਿਆ ਸੀ।

### ਸਿਰਫ਼ Risk ਬਾਰੇ ਨਹੀਂ

Prescriptive, risk-based levels ਦਾ ਵਰਤੋਂ ਜੋ ਕੁਝ applications ਲਈ ਇੱਕ ਖਾਸ level ਨੂੰ ਲਾਜ਼ਮੀ ਬਣਾਉਂਦੇ ਹਨ, ਬਹੁਤ ਜ਼ਿਆਦਾ ਕਠੋਰ ਸਾਬਤ ਹੋਇਆ ਹੈ। ਅਭਿਆਸ ਵਿੱਚ, security controls ਦੀ ਤਰਜੀਹ ਅਤੇ implementation ਕਈ ਕਾਰਕਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ risk reduction ਅਤੇ implementation ਲਈ ਲੋੜੀਂਦੀ ਕੋਸ਼ਿਸ਼ ਦੋਵੇਂ ਸ਼ਾਮਲ ਹਨ।

ਇਸ ਲਈ, ਸੰਸਥਾਵਾਂ ਨੂੰ ਉਸ level ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ ਉਹ ਮਹਿਸੂਸ ਕਰਦੀਆਂ ਹਨ ਕਿ ਉਹਨਾਂ ਨੂੰ ਆਪਣੀ ਪਰਿਪੱਕਤਾ ਅਤੇ ਉਸ ਸੰਦੇਸ਼ ਦੇ ਆਧਾਰ 'ਤੇ ਪ੍ਰਾਪਤ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ ਜੋ ਉਹ ਆਪਣੇ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਭੇਜਣਾ ਚਾਹੁੰਦੀਆਂ ਹਨ।