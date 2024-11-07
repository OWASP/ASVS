# Assessment and Certification

## OWASP's Stance on ASVS Certifications and Trust Marks

OWASP, as a vendor-neutral nonprofit, does not certify any vendors, verifiers, or software. Any assurance, trust mark, or certification claiming ASVS compliance is not officially endorsed by OWASP, so organizations should be cautious of third-party claims of ASVS certification.

Organizations may offer assurance services, provided they do not claim official OWASP certification

## Guidance for Certifying Organizations

The Application Security Verification Standard (ASVS) requires open access to resources, such as architects, developers, documentation, source code, and authenticated test systems, especially for L2 and L3 verifications.

Traditional penetration testing reports issues “by exception,” only listing failures. However, certifying reports should include scope, summaries of passed and failed tests, and guidance on resolving issues. Some requirements may be non-applicable (e.g., session management in stateless APIs), and this must be noted in the report.

Detailed documentation, including work papers, screenshots, scripts, and testing logs, is standard practice to provide robust evidence of findings. Merely running a tool without thorough testing is insufficient for certification, as each requirement must be verifiably tested.

### Testing Method

Certifying organizations can choose their testing methods but should disclose them in the report. Different methods, like manual penetration tests or source code analysis, may be used to verify aspects such as input validation, depending on the application and requirements.

#### The Role of Automated Security Testing Tools

Automated penetration testing tools are encouraged for coverage, though they cannot fully complete ASVS verification. While many Level 1 requirements are suited to automation, most requirements still require manual testing.

The line between automated and manual testing is increasingly blurred, as experts often tune automated tools, and manual testers frequently use automation.

#### The Role of Penetration Testing

In version 4.0, we decided to make L1 completely penetration testable without access to source code, documentation, or developers. Two logging items, which are required to comply with OWASP Top 10 2017 A10, will require interviews, screenshots or other evidence collection, just as they do in the OWASP Top 10 2017. However, testing without access to necessary information is not an ideal method of security verification, as it misses out on the possibility of reviewing the source, identifying threats and missing controls, and performing a far more thorough test in a shorter timeframe.

Where possible, access to developers, documentation, code, and access to a test application with non-production data, is required when performing a L2 or L3 Assessment. Penetration testing done at these levels requires this level of access, which we call "hybrid reviews" or "hybrid penetration tests".
