<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x04-Assessment_and_Certification.md -->
<!-- Translator: GeeksikhSecurity -->

# ਮੁਲਾਂਕਣ ਅਤੇ ਪ੍ਰਮਾਣੀਕਰਨ (Assessment and Certification)

## ASVS ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ Trust Marks ਬਾਰੇ OWASP ਦਾ ਰੁਖ

OWASP, ਇੱਕ vendor-neutral nonprofit ਹੋਣ ਦੇ ਨਾਤੇ, ਕਿਸੇ ਵੀ vendors, verifiers, ਜਾਂ software ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਨਹੀਂ ਕਰਦਾ। ASVS compliance ਦਾ ਦਾਅਵਾ ਕਰਨ ਵਾਲੇ ਕੋਈ ਵੀ assurance, trust mark, ਜਾਂ certification ਨੂੰ OWASP ਦੁਆਰਾ ਅਧਿਕਾਰਿਕ ਤੌਰ 'ਤੇ ਸਮਰਥਨ ਨਹੀਂ ਦਿੱਤਾ ਜਾਂਦਾ, ਇਸ ਲਈ ਸੰਸਥਾਵਾਂ ਨੂੰ ASVS certification ਦੇ third-party ਦਾਅਵਿਆਂ ਤੋਂ ਸਾਵਧਾਨ ਰਹਿਣਾ ਚਾਹੀਦਾ ਹੈ।

ਸੰਸਥਾਵਾਂ assurance services ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਬਸ਼ਰਤੇ ਉਹ ਅਧਿਕਾਰਿਕ OWASP certification ਦਾ ਦਾਅਵਾ ਨਾ ਕਰਨ।

## ASVS Compliance ਦੀ ਪੁਸ਼ਟੀ ਕਿਵੇਂ ਕਰੀਏ

ASVS ਜਾਣਬੁੱਝ ਕੇ testing guide ਦੇ ਪੱਧਰ 'ਤੇ compliance ਦੀ ਪੁਸ਼ਟੀ ਕਿਵੇਂ ਕਰਨੀ ਹੈ ਇਸ ਬਾਰੇ ਸਪਸ਼ਟ ਨਿਰਦੇਸ਼ ਨਹੀਂ ਦਿੰਦਾ। ਹਾਲਾਂਕਿ, ਕੁਝ ਮੁੱਖ ਨੁਕਤਿਆਂ ਨੂੰ ਉਜਾਗਰ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ।

### ਪੁਸ਼ਟੀ ਰਿਪੋਰਟਿੰਗ (Verification Reporting)

ਪਰੰਪਰਾਗਤ penetration testing ਰਿਪੋਰਟਾਂ "by exception" ਮੁੱਦਿਆਂ ਦੀ ਰਿਪੋਰਟ ਕਰਦੀਆਂ ਹਨ, ਸਿਰਫ਼ ਅਸਫਲਤਾਵਾਂ ਨੂੰ ਸੂਚੀਬੱਧ ਕਰਦੀਆਂ ਹਨ। ਹਾਲਾਂਕਿ, ਇੱਕ ASVS certification ਰਿਪੋਰਟ ਵਿੱਚ scope, ਸਾਰੀਆਂ ਜਾਂਚੀਆਂ ਗਈਆਂ requirements ਦਾ ਸਾਰ, ਉਹ requirements ਜਿੱਥੇ exceptions ਨੋਟ ਕੀਤੇ ਗਏ, ਅਤੇ ਮੁੱਦਿਆਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਮਾਰਗਦਰਸ਼ਨ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਕੁਝ requirements ਗੈਰ-ਲਾਗੂ ਹੋ ਸਕਦੀਆਂ ਹਨ (ਜਿਵੇਂ, stateless APIs ਵਿੱਚ session management), ਅਤੇ ਇਸ ਨੂੰ ਰਿਪੋਰਟ ਵਿੱਚ ਨੋਟ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ।

### ਪੁਸ਼ਟੀ ਦਾ ਦਾਇਰਾ (Scope of Verification)

ਇੱਕ application ਵਿਕਸਿਤ ਕਰਨ ਵਾਲੀ ਸੰਸਥਾ ਆਮ ਤੌਰ 'ਤੇ ਸਾਰੀਆਂ requirements ਨੂੰ ਲਾਗੂ ਨਹੀਂ ਕਰੇਗੀ, ਕਿਉਂਕਿ ਕੁਝ application ਦੀ functionality ਦੇ ਆਧਾਰ 'ਤੇ ਅਪ੍ਰਸੰਗਿਕ ਜਾਂ ਘੱਟ ਮਹੱਤਵਪੂਰਨ ਹੋ ਸਕਦੀਆਂ ਹਨ। Verifier ਨੂੰ verification ਦਾ scope ਸਪਸ਼ਟ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇਹ ਸ਼ਾਮਲ ਹੈ ਕਿ ਸੰਸਥਾ ਕਿਸ Level ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੀ ਹੈ ਅਤੇ ਕਿਹੜੀਆਂ requirements ਸ਼ਾਮਲ ਕੀਤੀਆਂ ਗਈਆਂ। ਇਹ ਇਸ ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਤੋਂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਕੀ ਸ਼ਾਮਲ ਕੀਤਾ ਗਿਆ ਸੀ ਨਾ ਕਿ ਕੀ ਸ਼ਾਮਲ ਨਹੀਂ ਕੀਤਾ ਗਿਆ। ਉਹਨਾਂ ਨੂੰ ਉਨ੍ਹਾਂ requirements ਨੂੰ ਬਾਹਰ ਰੱਖਣ ਦੇ ਤਰਕ 'ਤੇ ਵੀ ਰਾਏ ਦੇਣੀ ਚਾਹੀਦੀ ਹੈ ਜੋ ਲਾਗੂ ਨਹੀਂ ਕੀਤੀਆਂ ਗਈਆਂ।

ਇਸ ਨਾਲ verification ਰਿਪੋਰਟ ਦੇ ਉਪਭੋਗਤਾ ਨੂੰ verification ਦੇ ਸੰਦਰਭ ਨੂੰ ਸਮਝਣ ਅਤੇ application 'ਤੇ ਭਰੋਸੇ ਦੇ ਪੱਧਰ ਬਾਰੇ ਸੂਚਿਤ ਫੈਸਲਾ ਲੈਣ ਵਿੱਚ ਮਦਦ ਮਿਲਣੀ ਚਾਹੀਦੀ ਹੈ।

Certifying ਸੰਸਥਾਵਾਂ ਆਪਣੇ testing methods ਚੁਣ ਸਕਦੀਆਂ ਹਨ ਪਰ ਉਹਨਾਂ ਨੂੰ ਰਿਪੋਰਟ ਵਿੱਚ ਪ੍ਰਗਟ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਇਹ ਆਦਰਸ਼ ਰੂਪ ਵਿੱਚ ਦੁਹਰਾਉਣਯੋਗ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਵੱਖ-ਵੱਖ ਤਰੀਕੇ, ਜਿਵੇਂ manual penetration tests ਜਾਂ source code analysis, application ਅਤੇ requirements ਦੇ ਆਧਾਰ 'ਤੇ input validation ਵਰਗੇ ਪਹਿਲੂਆਂ ਦੀ ਪੁਸ਼ਟੀ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।

### ਪੁਸ਼ਟੀ ਵਿਧੀਆਂ (Verification Mechanisms)

ਖਾਸ ASVS requirements ਦੀ ਪੁਸ਼ਟੀ ਲਈ ਕਈ ਵੱਖ-ਵੱਖ ਤਕਨੀਕਾਂ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ। Penetration testing (ਪੂਰੀ application coverage ਲਈ ਵੈਧ credentials ਵਰਤਣਾ) ਤੋਂ ਇਲਾਵਾ, ASVS requirements ਦੀ ਪੁਸ਼ਟੀ ਲਈ documentation, source code, configuration, ਅਤੇ development process ਵਿੱਚ ਸ਼ਾਮਲ ਲੋਕਾਂ ਤੱਕ ਪਹੁੰਚ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ। ਖਾਸ ਕਰਕੇ L2 ਅਤੇ L3 requirements ਦੀ ਪੁਸ਼ਟੀ ਲਈ। ਵਿਸਤ੍ਰਿਤ documentation ਦੇ ਨਾਲ findings ਦੇ ਮਜ਼ਬੂਤ ਸਬੂਤ ਪ੍ਰਦਾਨ ਕਰਨਾ ਮਿਆਰੀ ਅਭਿਆਸ ਹੈ, ਜਿਸ ਵਿੱਚ work papers, screenshots, scripts, ਅਤੇ testing logs ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ। ਸਿਰਫ਼ ਇੱਕ automated tool ਚਲਾਉਣਾ ਬਿਨਾਂ ਡੂੰਘੀ testing ਦੇ certification ਲਈ ਨਾਕਾਫੀ ਹੈ, ਕਿਉਂਕਿ ਹਰ requirement ਨੂੰ ਪੁਸ਼ਟੀਯੋਗ ਤਰੀਕੇ ਨਾਲ test ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

ASVS requirements ਦੀ ਪੁਸ਼ਟੀ ਲਈ automation ਦਾ ਵਰਤੋਂ ਇੱਕ ਅਜਿਹਾ ਵਿਸ਼ਾ ਹੈ ਜੋ ਲਗਾਤਾਰ ਦਿਲਚਸਪੀ ਦਾ ਵਿਸ਼ਾ ਹੈ। ਇਸ ਲਈ automated ਅਤੇ black box testing ਨਾਲ ਸਬੰਧਤ ਕੁਝ ਨੁਕਤਿਆਂ ਨੂੰ ਸਪਸ਼ਟ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ।

#### Automated Security Testing Tools ਦੀ ਭੂਮਿਕਾ

ਜਦੋਂ automated security testing tools ਜਿਵੇਂ Dynamic ਅਤੇ Static Application Security Testing tools (DAST ਅਤੇ SAST) ਨੂੰ build pipeline ਵਿੱਚ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਲਾਗੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਉਹ ਕੁਝ security issues ਦੀ ਪਛਾਣ ਕਰਨ ਦੇ ਯੋਗ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਕਦੇ ਮੌਜੂਦ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ। ਹਾਲਾਂਕਿ, ਸਾਵਧਾਨ configuration ਅਤੇ tuning ਤੋਂ ਬਿਨਾਂ ਉਹ ਲੋੜੀਂਦੀ coverage ਪ੍ਰਦਾਨ ਨਹੀਂ ਕਰਨਗੇ ਅਤੇ noise ਦਾ ਪੱਧਰ ਅਸਲ security issues ਦੀ ਪਛਾਣ ਅਤੇ ਘਟਾਉਣ ਤੋਂ ਰੋਕੇਗਾ।

ਹਾਲਾਂਕਿ ਇਹ ਕੁਝ ਬੁਨਿਆਦੀ ਅਤੇ ਸਿੱਧੇ technical requirements ਜਿਵੇਂ output encoding ਜਾਂ sanitization ਨਾਲ ਸਬੰਧਤ requirements ਦੀ coverage ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹੈ, ਇਹ ਨੋਟ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਇਹ tools ਬਹੁਤ ਸਾਰੇ ਗੁੰਝਲਦਾਰ ASVS requirements ਜਾਂ business logic ਅਤੇ access control ਨਾਲ ਸਬੰਧਤ requirements ਦੀ ਪੂਰੀ ਤਰ੍ਹਾਂ ਪੁਸ਼ਟੀ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਹੋਣਗੇ।

ਘੱਟ ਸਿੱਧੇ requirements ਲਈ, ਸੰਭਾਵਨਾ ਹੈ ਕਿ automation ਦਾ ਵਰਤੋਂ ਅਜੇ ਵੀ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਪਰ ਇਸ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ application specific verifications ਲਿਖਣੇ ਪੈਣਗੇ। ਇਹ unit ਅਤੇ integration tests ਵਰਗੇ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਸੰਸਥਾ ਪਹਿਲਾਂ ਤੋਂ ਵਰਤ ਰਹੀ ਹੋਵੇ। ਇਸ ਲਈ ਇਹ ਮੌਜੂਦਾ test automation infrastructure ਦਾ ਵਰਤੋਂ ਕਰਕੇ ਇਹ ASVS specific tests ਲਿਖਣਾ ਸੰਭਵ ਹੋ ਸਕਦਾ ਹੈ। ਹਾਲਾਂਕਿ ਇਸ ਲਈ ਥੋੜ੍ਹੇ ਸਮੇਂ ਦੀ ਨਿਵੇਸ਼ ਦੀ ਲੋੜ ਹੋਵੇਗੀ, ਇਹਨਾਂ ASVS requirements ਦੀ ਲਗਾਤਾਰ ਪੁਸ਼ਟੀ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣ ਦੇ ਲੰਬੇ ਸਮੇਂ ਦੇ ਫਾਇਦੇ ਮਹੱਤਵਪੂਰਨ ਹੋਣਗੇ।

ਸੰਖੇਪ ਵਿੱਚ, automation ਵਰਤ ਕੇ testable != ਇੱਕ off the shelf tool ਚਲਾਉਣਾ।

#### Penetration Testing ਦੀ ਭੂਮਿਕਾ

ਹਾਲਾਂਕਿ version 4.0 ਵਿੱਚ L1 ਨੂੰ "black box" (ਕੋਈ documentation ਅਤੇ ਕੋਈ source ਨਹੀਂ) testing ਲਈ ਅਨੁਕੂਲਿਤ ਕੀਤਾ ਗਿਆ ਸੀ, ਫਿਰ ਵੀ ਮਿਆਰ ਸਪਸ਼ਟ ਸੀ ਕਿ ਇਹ ਇੱਕ ਪ੍ਰਭਾਵਸ਼ਾਲੀ assurance activity ਨਹੀਂ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਸਰਗਰਮੀ ਨਾਲ ਹਤੋਤਸਾਹਿਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

ਜ਼ਰੂਰੀ ਵਾਧੂ ਜਾਣਕਾਰੀ ਤੱਕ ਪਹੁੰਚ ਤੋਂ ਬਿਨਾਂ testing ਕਰਨਾ security verification ਲਈ ਇੱਕ ਅਕੁਸ਼ਲ ਅਤੇ ਅਪ੍ਰਭਾਵੀ ਵਿਧੀ ਹੈ, ਕਿਉਂਕਿ ਇਹ source ਦੀ ਸਮੀਖਿਆ, threats ਅਤੇ ਗੁੰਮ controls ਦੀ ਪਛਾਣ, ਅਤੇ ਘੱਟ ਸਮੇਂ ਵਿੱਚ ਬਹੁਤ ਜ਼ਿਆਦਾ ਡੂੰਘੀ test ਕਰਨ ਦੀ ਸੰਭਾਵਨਾ ਤੋਂ ਵਾਂਝੇ ਰਹਿ ਜਾਂਦਾ ਹੈ।

ਪਰੰਪਰਾਗਤ penetration tests ਦੀ ਬਜਾਏ documentation ਜਾਂ source code-led (hybrid) penetration testing ਕਰਨ ਦੀ ਜ਼ੋਰਦਾਰ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ application developers ਅਤੇ application ਦੀ documentation ਤੱਕ ਪੂਰੀ ਪਹੁੰਚ ਹੋਵੇ। ਇਹ ਬਹੁਤ ਸਾਰੇ ASVS requirements ਦੀ ਪੁਸ਼ਟੀ ਲਈ ਜ਼ਰੂਰੀ ਹੋਵੇਗਾ।