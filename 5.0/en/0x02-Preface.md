# Preface

Welcome to the Application Security Verification Standard (ASVS) version 4.0. The ASVS is a community-driven effort to establish a standard that defines the functional and non-functional security requirements to consider when designing, developing and testing modern web applications and web services.

Version 4.0.2 was the second minor patch to v4.0 intended to fix spelling errors and make requirements clearer without making breaking changes such as materially changing requirements or adding/removing requirements.

This version is a "Bleeding Edge" version which is constantly being updated and should not be used for testing against a standard.

ASVS v4.0 is the culmination of community effort and industry feedback over the last decade. We have attempted to make it easier to adopt the ASVS for a variety of different use cases throughout any secure software development lifecycle.

We expect that there will most likely never be 100% agreement on the contents of any web application standard, including the ASVS. Risk analysis is always subjective to some extent, which creates a challenge when attempting to generalize in a one-size-fits-all standard. However, we hope that the latest updates made in this version are a step in the right direction, and enhance the concepts introduced in this critical industry standard.

## What's new in 4.0

The most significant change in this version is the adoption of the NIST 800-63-3 Digital Identity Guidelines, introducing modern, evidence based, and advanced authentication controls. Although we expect some pushback on aligning with an advanced authentication standard, we feel that it is essential for standards to be aligned, mainly when another well-regarded application security standard is evidence-based.

Information security standards should try to minimize the number of unique requirements, so that complying organizations do not have to decide on competing or incompatible controls. The OWASP Top 10 2017 and now the OWASP Application Security Verification Standard have now aligned with NIST 800-63 for authentication and session management. We encourage other standards-setting bodies to work with us, NIST, and others to come to a generally accepted set of application security controls to maximize security and minimize compliance costs.

ASVS 4.0 has been wholly renumbered from start to finish. The new numbering scheme allowed us to close up gaps from long-vanished chapters, and to allow us to segment longer chapters to minimize the number of controls that a developer or team have to comply. For example, if an application does not use JWT, the entire section on JWT in session management is not applicable.

New in 4.0 is a comprehensive mapping to the Common Weakness Enumeration (CWE), one of the most commonly desired feature requests we've had over the last decade. CWE mapping allows tool manufacturers and those using vulnerability management software to match up results from other tools and previous ASVS versions to 4.0 and later. To make room for the CWE entry, we've had to retire the "Since" column, which as we completely renumbered, makes less sense than in previous versions of the ASVS. Not every item in the ASVS has an associated CWE, and as CWE has a great deal of duplication, we've attempted to use the most commonly used rather than necessarily the closest match. Verification controls are not always mappable to equivalent weaknesses. We welcome ongoing discussion with the CWE community and information security field more generally on closing this gap.

We have worked to comprehensively meet and exceed the requirements for addressing the OWASP Top 10 2017 and the OWASP Proactive Controls 2018. As the OWASP Top 10 2017 is the bare minimum to avoid negligence, we have deliberately made all but specific logging Top 10 requirements Level 1 controls, making it easier for OWASP Top 10 adopters to step up to an actual security standard.

We set out to ensure that the ASVS 4.0 Level 1 is a comprehensive superset of PCI DSS 3.2.1 Sections 6.5, for application design, coding, testing, secure code reviews, and penetration tests. This necessitated covering buffer overflow and unsafe memory operations in V5, and unsafe memory-related compilation flags in V14, in addition to existing industry-leading application and web service verification requirements.

We have completed the shift of the ASVS from monolithic server-side only controls, to providing security controls for all modern applications and APIs. In the days of functional programming, server-less API, mobile, cloud, containers, CI/CD and DevSecOps, federation and more, we cannot continue to ignore modern application architecture. Modern applications are designed very differently to those built when the original ASVS was released in 2009. The ASVS must always look far into the future so that we provide sound advice for our primary audience - developers. We have clarified or dropped any requirement that assumes that applications are executed on systems owned by a single organization.

Due to the size of the ASVS 4.0, as well as our desire to become the baseline ASVS for all other ASVS efforts, we have retired the mobile chapter, in favor of the Mobile Application Security Verification Standard (MASVS). The Internet of Things appendix will appear in a future IoT ASVS care of the OWASP Internet of Things Project. We have included an early preview of the IoT ASVS in Appendix C. We thank both the OWASP Mobile Team and OWASP IoT Project Team for their support of the ASVS, and look forward to working with them in the future to provide complementary standards.

Lastly, we have de-duped and retired less impactful controls. Over time, the ASVS started being a comprehensive set of controls, but not all controls are equal at producing secure software. This effort to eliminate low impact items could go further. In a future edition of the ASVS, the Common Weakness Scoring System (CWSS) will help prioritize further those controls which are truly important and those that should be retired.

As of version 4.0, the ASVS will focus solely on being the leading web apps and service standard, covering traditional and modern application architecture, and agile security practices and DevSecOps culture.
