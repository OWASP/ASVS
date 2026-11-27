<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x04-Assessment_and_Certification.md -->
<!-- Translator: GeeksikhSecurity -->

# Assessment and Certification
# ਮੁਲਾਂਕਣ ਅਤੇ ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ

## OWASP's Stance on ASVS Certifications and Trust Marks
## ASVS ਸਰਟੀਫ਼ਿਕੇਸ਼ਨਾਂ ਅਤੇ ਭਰੋਸਾ ਚਿੰਨ੍ਹਾਂ ਬਾਰੇ OWASP ਦਾ ਰੁਖ਼

OWASP, as a vendor-neutral nonprofit, does not certify any vendors, verifiers, or software. Any assurance, trust mark, or certification claiming ASVS compliance is not officially endorsed by OWASP, so organizations should be cautious of third-party claims of ASVS certification.

OWASP, ਇੱਕ ਵਿਕਰੇਤਾ-ਨਿਰਪੱਖ (vendor-neutral) ਗ਼ੈਰ-ਮੁਨਾਫ਼ਾ ਸੰਸਥਾ ਹੋਣ ਦੇ ਨਾਤੇ, ਕਿਸੇ ਵੀ ਵਿਕਰੇਤਾ, ਤਸਦੀਕਕਰਤਾ (verifier), ਜਾਂ ਸਾਫ਼ਟਵੇਅਰ ਦਾ ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ (certification) ਨਹੀਂ ਕਰਦਾ। ASVS ਪਾਲਣਾ (compliance) ਦਾ ਦਾਅਵਾ ਕਰਨ ਵਾਲਾ ਕੋਈ ਵੀ ਭਰੋਸਾ (assurance), ਭਰੋਸਾ ਚਿੰਨ੍ਹ (trust mark), ਜਾਂ ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ OWASP ਦੁਆਰਾ ਅਧਿਕਾਰਤ ਤੌਰ 'ਤੇ ਸਮਰਥਿਤ ਨਹੀਂ ਹੈ, ਇਸ ਲਈ ਸੰਸਥਾਵਾਂ ਨੂੰ ASVS ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ ਦੇ ਤੀਜੀ-ਧਿਰ ਦਾਅਵਿਆਂ ਤੋਂ ਸਾਵਧਾਨ ਰਹਿਣਾ ਚਾਹੀਦਾ ਹੈ।

Organizations may offer assurance services, provided they do not claim official OWASP certification.

ਸੰਸਥਾਵਾਂ ਭਰੋਸਾ ਸੇਵਾਵਾਂ ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਬਸ਼ਰਤੇ ਕਿ ਉਹ ਅਧਿਕਾਰਤ OWASP ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ ਦਾ ਦਾਅਵਾ ਨਾ ਕਰਨ।

## How to Verify ASVS Compliance
## ASVS ਪਾਲਣਾ ਦੀ ਤਸਦੀਕ ਕਿਵੇਂ ਕਰੀਏ

The ASVS is deliberately not prescriptive about exactly how to verify compliance at the level of a testing guide. However, it is important to highlight some key points.

ASVS ਜਾਣ-ਬੁੱਝ ਕੇ ਇਸ ਬਾਰੇ ਨਿਰਦੇਸ਼ਾਤਮਕ (prescriptive) ਨਹੀਂ ਹੈ ਕਿ ਕਿਸੇ ਟੈਸਟਿੰਗ ਮਾਰਗਦਰਸ਼ਿਕਾ (testing guide) ਦੇ ਪੱਧਰ 'ਤੇ ਪਾਲਣਾ ਦੀ ਤਸਦੀਕ ਬਿਲਕੁਲ ਕਿਵੇਂ ਕੀਤੀ ਜਾਵੇ। ਫਿਰ ਵੀ, ਕੁਝ ਮੁੱਖ ਨੁਕਤਿਆਂ ਨੂੰ ਉਜਾਗਰ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ।

### Verification reporting
### ਤਸਦੀਕ ਰਿਪੋਰਟਿੰਗ

Traditional penetration testing reports issues “by exception,” only listing failures. However, an ASVS certification report should include scope, a summary of all requirements checked, the requirements where exceptions were noted, and guidance on resolving issues. Some requirements may be non-applicable (e.g., session management in stateless APIs), and this must be noted in the report.

ਰਵਾਇਤੀ ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟਿੰਗ (penetration testing) ਰਿਪੋਰਟਾਂ ਮੁੱਦਿਆਂ ਦੀ ਰਿਪੋਰਟ "ਅਪਵਾਦ ਦੇ ਆਧਾਰ 'ਤੇ" (by exception) ਕਰਦੀਆਂ ਹਨ, ਅਰਥਾਤ ਸਿਰਫ਼ ਅਸਫਲਤਾਵਾਂ ਨੂੰ ਹੀ ਸੂਚੀਬੱਧ ਕਰਦੀਆਂ ਹਨ। ਫਿਰ ਵੀ, ਇੱਕ ASVS ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ ਰਿਪੋਰਟ ਵਿੱਚ ਘੇਰਾ, ਜਾਂਚੀਆਂ ਗਈਆਂ ਸਾਰੀਆਂ ਲੋੜਾਂ ਦਾ ਸਾਰ, ਉਹ ਲੋੜਾਂ ਜਿੱਥੇ ਅਪਵਾਦ ਦਰਜ ਕੀਤੇ ਗਏ, ਅਤੇ ਮੁੱਦਿਆਂ ਨੂੰ ਹੱਲ ਕਰਨ ਬਾਰੇ ਮਾਰਗਦਰਸ਼ਨ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਕੁਝ ਲੋੜਾਂ ਗ਼ੈਰ-ਲਾਗੂ ਹੋ ਸਕਦੀਆਂ ਹਨ (ਜਿਵੇਂ, ਸਟੇਟਲੈੱਸ (stateless) API ਵਿੱਚ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ), ਅਤੇ ਇਸ ਨੂੰ ਰਿਪੋਰਟ ਵਿੱਚ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਦਰਜ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

### Scope of Verification
### ਤਸਦੀਕ ਦਾ ਘੇਰਾ

An organization developing an application will generally not implement all requirements, as some may be irrelevant or less significant based on the functionality of the application. The verifier should make the scope of the verification clear including which Level the organization is attempting to achieve and which requirements were included. This should be from the perspective of what was included rather than what was not included. They should also provide an opinion on the rationale of excluding the requirements which haven't been implemented.

ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਵਿਕਾਸ ਕਰਨ ਵਾਲੀ ਸੰਸਥਾ ਆਮ ਤੌਰ 'ਤੇ ਸਾਰੀਆਂ ਲੋੜਾਂ ਲਾਗੂ ਨਹੀਂ ਕਰੇਗੀ, ਕਿਉਂਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਜਸ਼ੀਲਤਾ ਦੇ ਆਧਾਰ 'ਤੇ ਕੁਝ ਲੋੜਾਂ ਅਪ੍ਰਸੰਗਿਕ ਜਾਂ ਘੱਟ ਮਹੱਤਵਪੂਰਨ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਤਸਦੀਕਕਰਤਾ ਨੂੰ ਤਸਦੀਕ ਦਾ ਘੇਰਾ ਸਪੱਸ਼ਟ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਇਹ ਸ਼ਾਮਲ ਹੈ ਕਿ ਸੰਸਥਾ ਕਿਹੜਾ ਪੱਧਰ ਹਾਸਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੀ ਹੈ ਅਤੇ ਕਿਹੜੀਆਂ ਲੋੜਾਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ ਗਈਆਂ ਸਨ। ਇਹ ਇਸ ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਤੋਂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਕੀ ਸ਼ਾਮਲ ਕੀਤਾ ਗਿਆ ਸੀ, ਨਾ ਕਿ ਕੀ ਸ਼ਾਮਲ ਨਹੀਂ ਕੀਤਾ ਗਿਆ ਸੀ। ਉਹਨਾਂ ਨੂੰ ਉਹਨਾਂ ਲੋੜਾਂ ਨੂੰ ਬਾਹਰ ਰੱਖਣ ਦੇ ਤਰਕ-ਆਧਾਰ ਬਾਰੇ ਵੀ ਆਪਣੀ ਰਾਏ ਦੇਣੀ ਚਾਹੀਦੀ ਹੈ ਜੋ ਲਾਗੂ ਨਹੀਂ ਕੀਤੀਆਂ ਗਈਆਂ।

This should allow the consumer of a verification report to understand the context of the verification and make an informed decision about the level of trust they can place in the application.

ਇਸ ਨਾਲ ਤਸਦੀਕ ਰਿਪੋਰਟ ਦਾ ਖਪਤਕਾਰ ਤਸਦੀਕ ਦੇ ਸੰਦਰਭ ਨੂੰ ਸਮਝਣ ਅਤੇ ਇਸ ਬਾਰੇ ਸੂਚਿਤ ਫ਼ੈਸਲਾ ਲੈਣ ਦੇ ਯੋਗ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਉਹ ਐਪਲੀਕੇਸ਼ਨ 'ਤੇ ਕਿਸ ਪੱਧਰ ਦਾ ਭਰੋਸਾ ਰੱਖ ਸਕਦਾ ਹੈ।

Certifying organizations can choose their testing methods but should disclose them in the report and this should ideally be repeatable. Different methods, like manual penetration tests or source code analysis, may be used to verify aspects such as input validation, depending on the application and requirements.

ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ ਕਰਨ ਵਾਲੀਆਂ ਸੰਸਥਾਵਾਂ ਆਪਣੀਆਂ ਟੈਸਟਿੰਗ ਵਿਧੀਆਂ ਚੁਣ ਸਕਦੀਆਂ ਹਨ, ਪਰ ਉਹਨਾਂ ਨੂੰ ਇਹ ਰਿਪੋਰਟ ਵਿੱਚ ਪ੍ਰਗਟ ਕਰਨੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ ਅਤੇ ਆਦਰਸ਼ਕ ਤੌਰ 'ਤੇ ਇਹ ਦੁਹਰਾਉਣਯੋਗ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ। ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਲੋੜਾਂ ਦੇ ਆਧਾਰ 'ਤੇ, ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਵਰਗੇ ਪਹਿਲੂਆਂ ਦੀ ਤਸਦੀਕ ਕਰਨ ਲਈ ਵੱਖ-ਵੱਖ ਵਿਧੀਆਂ, ਜਿਵੇਂ ਕਿ ਹੱਥੀਂ (manual) ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟ ਜਾਂ ਸਰੋਤ ਕੋਡ ਵਿਸ਼ਲੇਸ਼ਣ, ਵਰਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।

### Verification Mechanisms
### ਤਸਦੀਕ ਪ੍ਰਣਾਲੀਆਂ

There are a number of different techniques which may be needed to verify specific ASVS requirements. Aside from penetration testing (using valid credentials to get full application coverage), verifying ASVS requirements may require access to documentation, source code, configuration, and the people involved in the development process. Especially for verifying L2 and L3 requirements. It is standard practice to provide robust evidence of findings with detailed documentation, which may include work papers, screenshots, scripts, and testing logs. Merely running an automated tool without thorough testing is insufficient for certification, as each requirement must be verifiably tested.

ਖ਼ਾਸ ASVS ਲੋੜਾਂ ਦੀ ਤਸਦੀਕ ਕਰਨ ਲਈ ਕਈ ਵੱਖ-ਵੱਖ ਤਕਨੀਕਾਂ ਦੀ ਲੋੜ ਪੈ ਸਕਦੀ ਹੈ। ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟਿੰਗ (ਪੂਰੀ ਐਪਲੀਕੇਸ਼ਨ ਕਵਰੇਜ ਹਾਸਲ ਕਰਨ ਲਈ ਜਾਇਜ਼ ਪ੍ਰਮਾਣ-ਪੱਤਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ) ਤੋਂ ਇਲਾਵਾ, ASVS ਲੋੜਾਂ ਦੀ ਤਸਦੀਕ ਕਰਨ ਲਈ ਦਸਤਾਵੇਜ਼ਾਂ, ਸਰੋਤ ਕੋਡ, ਸੰਰਚਨਾ, ਅਤੇ ਵਿਕਾਸ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਸ਼ਾਮਲ ਲੋਕਾਂ ਤੱਕ ਪਹੁੰਚ ਦੀ ਲੋੜ ਪੈ ਸਕਦੀ ਹੈ। ਖ਼ਾਸ ਕਰਕੇ L2 ਅਤੇ L3 ਲੋੜਾਂ ਦੀ ਤਸਦੀਕ ਕਰਨ ਲਈ। ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼ਾਂ ਦੇ ਨਾਲ ਖੋਜਾਂ (findings) ਦੇ ਮਜ਼ਬੂਤ ਸਬੂਤ ਪ੍ਰਦਾਨ ਕਰਨਾ ਮਿਆਰੀ ਅਮਲ ਹੈ, ਜਿਸ ਵਿੱਚ ਕਾਰਜ-ਪੱਤਰ, ਸਕ੍ਰੀਨਸ਼ਾਟ, ਸਕ੍ਰਿਪਟਾਂ, ਅਤੇ ਟੈਸਟਿੰਗ ਲੌਗ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ। ਡੂੰਘੀ ਟੈਸਟਿੰਗ ਤੋਂ ਬਿਨਾਂ ਸਿਰਫ਼ ਕੋਈ ਸਵੈਚਾਲਿਤ ਟੂਲ ਚਲਾ ਦੇਣਾ ਸਰਟੀਫ਼ਿਕੇਸ਼ਨ ਲਈ ਨਾਕਾਫ਼ੀ ਹੈ, ਕਿਉਂਕਿ ਹਰ ਲੋੜ ਨੂੰ ਤਸਦੀਕਯੋਗ ਢੰਗ ਨਾਲ ਟੈਸਟ ਕੀਤਾ ਜਾਣਾ ਲਾਜ਼ਮੀ ਹੈ।

The use of automation to verify ASVS requirements is a topic that is constantly of interest. It is therefore important to clarify some points related to automated and black box testing.

ASVS ਲੋੜਾਂ ਦੀ ਤਸਦੀਕ ਲਈ ਸਵੈਚਾਲਨ (automation) ਦੀ ਵਰਤੋਂ ਇੱਕ ਅਜਿਹਾ ਵਿਸ਼ਾ ਹੈ ਜਿਸ ਵਿੱਚ ਲਗਾਤਾਰ ਦਿਲਚਸਪੀ ਬਣੀ ਰਹਿੰਦੀ ਹੈ। ਇਸ ਲਈ ਸਵੈਚਾਲਿਤ ਅਤੇ ਬਲੈਕ ਬਾਕਸ (black box) ਟੈਸਟਿੰਗ ਨਾਲ ਸੰਬੰਧਿਤ ਕੁਝ ਨੁਕਤਿਆਂ ਨੂੰ ਸਪੱਸ਼ਟ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ।

#### The Role of Automated Security Testing Tools
#### ਸਵੈਚਾਲਿਤ ਸੁਰੱਖਿਆ ਟੈਸਟਿੰਗ ਟੂਲਾਂ ਦੀ ਭੂਮਿਕਾ

When automated security testing tools such as Dynamic and Static Application Security Testing tools (DAST and SAST) are correctly implemented in the build pipeline, they may be able to identify some security issues that should never exist. However, without careful configuration and tuning they will not provide the required coverage and the level of noise will prevent real security issues from being identified and mitigated.

ਜਦੋਂ ਸਵੈਚਾਲਿਤ ਸੁਰੱਖਿਆ ਟੈਸਟਿੰਗ ਟੂਲ, ਜਿਵੇਂ ਕਿ ਗਤੀਸ਼ੀਲ ਅਤੇ ਸਥਿਰ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਟੈਸਟਿੰਗ ਟੂਲ (DAST ਅਤੇ SAST), ਬਿਲਡ ਪਾਈਪਲਾਈਨ ਵਿੱਚ ਸਹੀ ਢੰਗ ਨਾਲ ਲਾਗੂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਤਾਂ ਉਹ ਕੁਝ ਅਜਿਹੇ ਸੁਰੱਖਿਆ ਮੁੱਦਿਆਂ ਦੀ ਪਛਾਣ ਕਰਨ ਦੇ ਯੋਗ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਕਦੇ ਮੌਜੂਦ ਹੀ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ। ਫਿਰ ਵੀ, ਧਿਆਨਪੂਰਵਕ ਸੰਰਚਨਾ ਅਤੇ ਟਿਊਨਿੰਗ ਤੋਂ ਬਿਨਾਂ ਉਹ ਲੋੜੀਂਦੀ ਕਵਰੇਜ ਪ੍ਰਦਾਨ ਨਹੀਂ ਕਰਨਗੇ ਅਤੇ ਸ਼ੋਰ ਦਾ ਪੱਧਰ ਅਸਲ ਸੁਰੱਖਿਆ ਮੁੱਦਿਆਂ ਨੂੰ ਪਛਾਣੇ ਜਾਣ ਅਤੇ ਘਟਾਏ ਜਾਣ ਤੋਂ ਰੋਕੇਗਾ।

Whilst this may provide coverage of some of the more basic and straightforward technical requirements such as those relating to output encoding or sanitization, it is critical to note that these tools will be unable entirely to verify many of the more complicated ASVS requirements or those that relate to business logic and access control.

ਭਾਵੇਂ ਇਹ ਕੁਝ ਵਧੇਰੇ ਬੁਨਿਆਦੀ ਅਤੇ ਸਿੱਧੀਆਂ ਤਕਨੀਕੀ ਲੋੜਾਂ, ਜਿਵੇਂ ਕਿ ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਜਾਂ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ, ਦੀ ਕਵਰੇਜ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹੈ, ਇਹ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਬੇਹੱਦ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਇਹ ਟੂਲ ਬਹੁਤ ਸਾਰੀਆਂ ਵਧੇਰੇ ਗੁੰਝਲਦਾਰ ASVS ਲੋੜਾਂ, ਜਾਂ ਕਾਰੋਬਾਰੀ ਤਰਕ ਅਤੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ, ਦੀ ਤਸਦੀਕ ਕਰਨ ਵਿੱਚ ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਸਮਰੱਥ ਹੋਣਗੇ।

For less straightforward requirements, it is likely that automation can still be utilized but application specific verifications will need to be written to achieve this. These may be similar to unit and integration tests that the organization may already be using. It may therefore be possible to use this existing test automation infrastructure to write these ASVS specific tests. Whilst doing this will require short term investment, the long term benefits being able to continually verify these ASVS requirements will be significant.

ਘੱਟ ਸਿੱਧੀਆਂ ਲੋੜਾਂ ਲਈ, ਸੰਭਾਵਨਾ ਹੈ ਕਿ ਸਵੈਚਾਲਨ ਦੀ ਵਰਤੋਂ ਅਜੇ ਵੀ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ, ਪਰ ਇਸ ਨੂੰ ਹਾਸਲ ਕਰਨ ਲਈ ਐਪਲੀਕੇਸ਼ਨ-ਵਿਸ਼ੇਸ਼ ਤਸਦੀਕਾਂ ਲਿਖਣੀਆਂ ਪੈਣਗੀਆਂ। ਇਹ ਉਹਨਾਂ ਯੂਨਿਟ ਅਤੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਟੈਸਟਾਂ ਵਰਗੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ ਜੋ ਸੰਸਥਾ ਸ਼ਾਇਦ ਪਹਿਲਾਂ ਹੀ ਵਰਤ ਰਹੀ ਹੋਵੇ। ਇਸ ਲਈ ਇਹ ASVS-ਵਿਸ਼ੇਸ਼ ਟੈਸਟ ਲਿਖਣ ਲਈ ਇਸ ਮੌਜੂਦਾ ਟੈਸਟ ਸਵੈਚਾਲਨ ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਸੰਭਵ ਹੋ ਸਕਦਾ ਹੈ। ਭਾਵੇਂ ਅਜਿਹਾ ਕਰਨ ਲਈ ਥੋੜ੍ਹੇ ਸਮੇਂ ਦੇ ਨਿਵੇਸ਼ ਦੀ ਲੋੜ ਪਵੇਗੀ, ਇਹਨਾਂ ASVS ਲੋੜਾਂ ਦੀ ਨਿਰੰਤਰ ਤਸਦੀਕ ਕਰ ਸਕਣ ਦੇ ਲੰਮੇ ਸਮੇਂ ਦੇ ਲਾਭ ਮਹੱਤਵਪੂਰਨ ਹੋਣਗੇ।

In summary, testable using automation != running an off the shelf tool.

ਸੰਖੇਪ ਵਿੱਚ, ਸਵੈਚਾਲਨ ਰਾਹੀਂ ਟੈਸਟਯੋਗ ਹੋਣਾ != ਕੋਈ ਤਿਆਰ-ਬਰ-ਤਿਆਰ (off the shelf) ਟੂਲ ਚਲਾ ਦੇਣਾ।

#### The Role of Penetration Testing
#### ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟਿੰਗ ਦੀ ਭੂਮਿਕਾ

Whilst L1 in version 4.0 was optimized for "black box" (no documentation and no source) testing to occur, even then the standard was clear that it is not an effective assurance activity and should be actively discouraged.

ਭਾਵੇਂ ਸੰਸਕਰਣ 4.0 ਵਿੱਚ L1 ਨੂੰ "ਬਲੈਕ ਬਾਕਸ" (ਬਿਨਾਂ ਦਸਤਾਵੇਜ਼ਾਂ ਅਤੇ ਬਿਨਾਂ ਸਰੋਤ ਕੋਡ ਦੇ) ਟੈਸਟਿੰਗ ਕੀਤੇ ਜਾਣ ਲਈ ਅਨੁਕੂਲਿਤ ਕੀਤਾ ਗਿਆ ਸੀ, ਉਦੋਂ ਵੀ ਮਿਆਰ ਇਸ ਬਾਰੇ ਸਪੱਸ਼ਟ ਸੀ ਕਿ ਇਹ ਕੋਈ ਅਸਰਦਾਰ ਭਰੋਸਾ ਗਤੀਵਿਧੀ ਨਹੀਂ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਸਰਗਰਮੀ ਨਾਲ ਨਿਰਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

Testing without access to necessary additional information is an inefficient and ineffective mechanism for security verification, as it misses out on the possibility of reviewing the source, identifying threats and missing controls, and performing a far more thorough test in a shorter timeframe.

ਲੋੜੀਂਦੀ ਵਾਧੂ ਜਾਣਕਾਰੀ ਤੱਕ ਪਹੁੰਚ ਤੋਂ ਬਿਨਾਂ ਟੈਸਟਿੰਗ ਕਰਨਾ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਲਈ ਇੱਕ ਅਕੁਸ਼ਲ ਅਤੇ ਬੇਅਸਰ ਪ੍ਰਣਾਲੀ ਹੈ, ਕਿਉਂਕਿ ਇਹ ਸਰੋਤ ਕੋਡ ਦੀ ਸਮੀਖਿਆ ਕਰਨ, ਖ਼ਤਰਿਆਂ ਅਤੇ ਗੁੰਮ ਨਿਯੰਤਰਣਾਂ ਦੀ ਪਛਾਣ ਕਰਨ, ਅਤੇ ਘੱਟ ਸਮੇਂ ਵਿੱਚ ਕਿਤੇ ਵਧੇਰੇ ਡੂੰਘਾ ਟੈਸਟ ਕਰਨ ਦੀ ਸੰਭਾਵਨਾ ਤੋਂ ਵਾਂਝੀ ਰਹਿ ਜਾਂਦੀ ਹੈ।

It is strongly encouraged to perform documentation or source code-led (hybrid) penetration testing, which have full access to the application developers and the application's documentation, rather than traditional penetration tests. This will certainly be necessary in order to verify many of the ASVS requirements.

ਰਵਾਇਤੀ ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟਾਂ ਦੀ ਬਜਾਏ, ਦਸਤਾਵੇਜ਼-ਅਗਵਾਈ ਵਾਲੀ ਜਾਂ ਸਰੋਤ ਕੋਡ-ਅਗਵਾਈ ਵਾਲੀ (ਹਾਈਬ੍ਰਿਡ) ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟਿੰਗ ਕਰਨ ਲਈ ਜ਼ੋਰਦਾਰ ਢੰਗ ਨਾਲ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਵਿਕਾਸਕਾਰਾਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਤੱਕ ਪੂਰੀ ਪਹੁੰਚ ਹੁੰਦੀ ਹੈ। ਬਹੁਤ ਸਾਰੀਆਂ ASVS ਲੋੜਾਂ ਦੀ ਤਸਦੀਕ ਕਰਨ ਲਈ ਇਹ ਨਿਸ਼ਚਿਤ ਤੌਰ 'ਤੇ ਜ਼ਰੂਰੀ ਹੋਵੇਗਾ।
