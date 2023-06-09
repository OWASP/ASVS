# Assessment and Certification

## OWASP's Stance on ASVS Certifications and Trust Marks

OWASP, as a vendor-neutral not-for-profit organization, does not currently certify any vendors, verifiers or software.

All such assurance assertions, trust marks, or certifications are not officially vetted, registered, or certified by OWASP, so an organization relying upon such a view needs to be cautious of the trust placed in any third party or trust mark claiming ASVS certification.

This should not inhibit organizations from offering such assurance services, as long as they do not claim official OWASP certification.

## Guidance for Certifying Organizations

The Application Security Verification Standard can be used as an open book verification of the application, including open and unfettered access to key resources such as architects and developers, project documentation, source code, authenticated access to test systems (including access to one or more accounts in each role), particularly for L2 and L3 verifications.

Historically, penetration testing and secure code reviews have included issues “by exception” - that is only failed tests appear in the final report. A certifying organization must include in any report the scope of the verification (particularly if a key component is out of scope, such as SSO authentication), a summary of verification findings, including passed and failed tests, with clear indications of how to resolve the failed tests.

Certain verification requirements may not be applicable to the application under test. For example, if you provide a stateless service layer API without a client implementation to your customers, many of the requirements in V3 Session Management are not directly applicable. In such cases, a certifying organization may still claim full ASVS compliance, but must clearly indicate in any report a reason for non-applicability of such excluded verification requirements.

Keeping detailed work papers, screenshots or movies, scripts to reliably and repeatedly exploit an issue, and electronic records of testing, such as intercepting proxy logs and associated notes such as a cleanup list, is considered standard industry practice and can be really useful as proof of the findings for the most doubtful developers. It is not sufficient to simply run a tool and report on the failures; this does not (at all) provide sufficient evidence that all issues at a certifying level have been tested and tested thoroughly. In case of dispute, there should be sufficient assurance evidence to demonstrate each and every verified requirement has indeed been tested.

### Testing Method

Certifying organizations are free to choose the appropriate testing method(s), but should indicate them in a report.

Depending on the application under test and the verification requirement, different testing methods may be used to gain similar confidence in the results. For example, validating the effectiveness of an application's input verification mechanisms may either be analyzed with a manual penetration test or by means of source code analyses.

#### The Role of Automated Security Testing Tools

The use of automated penetration testing tools is encouraged to provide as much coverage as possible.

It is not possible to fully complete ASVS verification using automated penetration testing tools alone. Whilst a large majority of requirements in L1 can be performed using automated tests, the overall majority of requirements are not amenable to automated penetration testing.

Please note that the lines between automated and manual testing have blurred as the application security industry matures. Automated tools are often manually tuned by experts and manual testers often leverage a wide variety of automated tools.

#### The Role of Penetration Testing

In version 4.0, we decided to make L1 completely penetration testable without access to source code, documentation, or developers. Two logging items, which are required to comply with OWASP Top 10 2017 A10, will require interviews, screenshots or other evidence collection, just as they do in the OWASP Top 10 2017. However, testing without access to necessary information is not an ideal method of security verification, as it misses out on the possibility of reviewing the source, identifying threats and missing controls, and performing a far more thorough test in a shorter timeframe.

Where possible, access to developers, documentation, code, and access to a test application with non-production data, is required when performing a L2 or L3 Assessment. Penetration testing done at these levels requires this level of access, which we call "hybrid reviews" or "hybrid penetration tests".
