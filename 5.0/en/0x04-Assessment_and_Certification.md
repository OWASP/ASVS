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

In version 5.0, L1 was made fully penetration testable without access to source code, documentation, or developers. However, two logging items still require interviews or evidence collection to comply with OWASP Top 10 2017 A10. Testing without full access limits thorough security verification, as it prevents source review and threat identification.

For L2 or L3 assessments, access to developers, documentation, code, and a test application with non-production data is essential. Penetration testing at these levels requires this 'hybrid review' approach.
