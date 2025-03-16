# Guidance for users of version 4.0

<!--

<<MOVED THIS TEXT FROM THE PREFACE AS IT SEEMS MORE RELEVANT HERE>>

We expect that there will most likely never be 100% agreement on the contents of any web application standard, including the ASVS. Risk analysis is always subjective to some extent, which creates a challenge when attempting to generalize in a one-size-fits-all standard. However, we hope that the latest updates made in this version are a step in the right direction, and enhance the concepts introduced in this critical industry standard.

## What's new in 4.0

The most significant change in this version is the adoption of the NIST SP 800-63-3 Digital Identity Guidelines, introducing modern, evidence-based, and advanced authentication controls. Although we expect some pushback on aligning with an advanced authentication standard, we feel that it is essential for standards to be aligned, mainly when another well-regarded application security standard is evidence-based.

Information security standards should try to minimize the number of unique requirements so that complying organizations do not have to decide on competing or incompatible controls. The OWASP Top 10 2017 and now the OWASP Application Security Verification Standard have aligned with NIST SP 800-63 for authentication and session management. We encourage other standards-setting bodies to collaborate with us, NIST, and others in establishing a generally accepted set of application security controls. This approach will maximize security while minimizing compliance costs.

ASVS 4.0 has been wholly renumbered from start to finish. The new numbering scheme allowed us to close up gaps from long-vanished chapters, and to allow us to segment longer chapters to minimize the number of controls that a developer or team has to comply with. For example, if an application does not use JWT, the entire section on JWT in session management is not applicable.

New in 4.0 is a comprehensive mapping to the Common Weakness Enumeration (CWE), one of the most commonly desired feature requests we've had over the last decade. CWE mapping allows tool manufacturers and those using vulnerability management software to match up results from other tools and previous ASVS versions to 4.0 and later. To make room for the CWE entry, we've had to retire the "Since" column, which as we completely renumbered, makes less sense than in previous versions of the ASVS. Not every item in the ASVS has an associated CWE, and as CWE has a great deal of duplication, we've attempted to use the most commonly used rather than necessarily the closest match. Verification controls are not always mappable to equivalent weaknesses. We welcome ongoing discussions with the CWE community and information security field more generally on closing this gap.

We have worked to comprehensively meet and exceed the requirements for addressing the OWASP Top 10 2017 and the OWASP Proactive Controls 2018. As the OWASP Top 10 2017 is the bare minimum to avoid negligence, we have deliberately made all but specific logging Top 10 requirements Level 1 controls, making it easier for OWASP Top 10 adopters to step up to an actual security standard.

We set out to ensure that the ASVS 4.0 Level 1 is a comprehensive superset of PCI DSS 3.2.1 Sections 6.5, for application design, coding, testing, secure code reviews, and penetration tests. This necessitated covering buffer overflow and unsafe memory operations in V5, and unsafe memory-related compilation flags in V14, in addition to existing industry-leading application and web service verification requirements.

We have completed the shift of the ASVS from monolithic server-side-only controls, to providing security controls for all modern applications and APIs. In the days of functional programming, server-less API, mobile, cloud, containers, CI/CD and DevSecOps, federation and more, we cannot continue to ignore modern application architecture. Modern applications are designed very differently from those built when the original ASVS was released in 2009. The ASVS must always look far into the future so that we provide sound advice for our primary audience - developers. We have clarified or dropped any requirement that assumes that applications are executed on systems owned by a single organization.

Due to the size of the ASVS 4.0, as well as our desire to become the baseline ASVS for all other ASVS efforts, we have retired the mobile chapter, in favor of the Mobile Application Security Verification Standard (MASVS). We have also retired the Internet of Things appendix, in favor of the IoT Security Verification Standard (ISVS). We thank both the OWASP Mobile Team and OWASP IoT Project Team for their support of the ASVS, and look forward to working with them in the future to provide complementary standards.

Lastly, we have de-duped and retired less impactful controls. Over time, the ASVS started being a comprehensive set of controls, but not all controls equally contribute to producing secure software. This effort to eliminate low-impact items could go further. In a future edition of the ASVS, the Common Weakness Scoring System (CWSS) will help prioritize further those controls that are truly important and those that should be retired.

As of version 4.0, the ASVS will focus solely on being the leading web apps and service standard, covering traditional and modern application architecture, agile security practices and DevSecOps culture.
-->

## TODO: Add more content

### Challenges with the previous approach

Version 4.0 of the ASVS describes the levels as L1 - "Minimum", L2 - "Standard", and L3 - "Advanced" with the implication that all applications processing sensitive data should be at least L2.

There have been a few challenges with this approach.

#### High barrier to entry

L1 in version 4.0 had over 100 requirements as did L2 with only a few requirements left in L3. This meant that a high level of effort required to achieve even L1 at which point the user is told that this is the "minimum" level and that to achieve a "standard" level of security, another 100 requirements are required. Based on feedback from ASVS users and community it became clear that this acted as a disincentive and made it harder for applications to start adopting the ASVS.

#### The fallacy of testability

A primary motivator behind putting controls in L1 version 4.0 was whether they could be checked using "black box" style testing which was not entirely in line with the concept of L1 being the minimum security controls. On the one hand, ASVS users would say that L1 was not sufficient for a secure application whilst on the other hand user would complain that ASVS was too difficult to test.

Additionally, testability is relative and in some cases misleading. Just because something is testable does not mean that it is testable in an automated or trivial way. Finally, the most testable requirements are not necessarily those that have the most important security impact or are the easiest to implement.

#### Not just about risk

The use of prescriptive, risk based levels which mandate that a certain application has to be at a certain level seems overly opinionated in hind-sight. In reality, the order of implementing security controls will depend on factors including both risk reduction and also effort to implement.
