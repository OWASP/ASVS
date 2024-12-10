# Assessment and Certification

## OWASP's Stance on ASVS Certifications and Trust Marks

OWASP, as a vendor-neutral nonprofit, does not certify any vendors, verifiers, or software. Any assurance, trust mark, or certification claiming ASVS compliance is not officially endorsed by OWASP, so organizations should be cautious of third-party claims of ASVS certification.

Organizations may offer assurance services, provided they do not claim official OWASP certification

## Guidance for Certifying Organizations

The Application Security Verification Standard (ASVS) requires open access to resources, such as architects, developers, documentation, source code, and authenticated test systems, especially for L2 and L3 verifications.

Traditional penetration testing reports issues “by exception,” only listing failures. However, certifying reports should include scope, summaries of passed and failed tests, and guidance on resolving issues. Some requirements may be non-applicable (e.g., session management in stateless APIs), and this must be noted in the report.

Detailed documentation, including work papers, screenshots, scripts, and testing logs, is standard practice to provide robust evidence of findings. Merely running a tool without thorough testing is insufficient for certification, as each requirement must be verifiably tested.

## How to Verify ASVS Compliance

The ASVS is deliberately not presciptive about exactly how to verify compliance. However, it is important to highlight some key points.

### Scope of Verification

Given that an organization will generally not implement all requirements, as some may be irrelevant or less important to them, the scope of verification should be clearly defined. The verifier should make it clear which Level the organization is attempting to achieve and also provide an opinion on the rationale of excluding the requirements which haven't been implemented.

This should allow the consumer of a verification report to understand the context of the verification and make an informed decision about the level of trust they can place in the application.

Certifying organizations can choose their testing methods but should disclose them in the report. Different methods, like manual penetration tests or source code analysis, may be used to verify aspects such as input validation, depending on the application and requirements.

### Verification Mechanisms

There are a number of different techniques which may be needed to verify specific ASVS requirements. Aside from penetration testing, verifying ASVS requirements may require access to documentation, source code, configuration, and the people involved in the development process. 

The use of automation to verify ASVS requirements is a topic that is constantly of interest. After version 5.0 is released, we would like to prepare a testing guide to try and demonstrate how requirements can be verified but for now it is important to clarify some points related to automated and black box testing.

#### The Role of Automated Security Testing Tools

Automated security testing tools such as DAST and SAST tools, when effectively implemented in the build pipeline, can effectively identify some security issues that should never exist. However, without careful configuration and tuning they may not provide the required coverage and the level of noise is likely to prevent real security issues from being identified and mitigated.

Whilst this may provide coverage of some of the more basic and straightforward technical requirements such as those relating to output encoding or sanitiation, it is critical to note that these tools will be unable entirely to verify many of the more complicated ASVS requirements or those that relate to business logic and access control. 

For less straightforward requirements, it is likely that automation can still be utilized but application specific verifications will need to be written to achieve this. These may be similar to unit and integration tests that the organization may already be using. It may therefore be possible to use this existing test automation infrastructure to write these ASVS specific tests. Whilst doing this will require short term investment, the long term benefits being able to continually verify these ASVS requirements will be significant.

In summary, testable using automation != running an off the shelf tool.

#### The Role of Penetration Testing

Whilst L1 in version 4.0 was optimized for "black box" (no documentation and no source) testing to occur, even then we were clear that it is not an effective assurance activity and should be actively discouraged. 

Testing without access to necessary additional information is an inefficient and ineffective mechanism for security verification, as it misses out on the possibility of reviewing the source, identifying threats and missing controls, and performing a far more thorough test in a shorter timeframe.

We strongly encourage including replacing penetration tests with documentation or source code-led (hybrid) penetration testing, with full access to developers and documentation throughout the development process, and this will be necessary in order to verify many of the ASVS requirements.

