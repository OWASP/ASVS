# Guidance for users of version 4.0

Existing users of the 4.0 version of the standard may find it useful to see some of the key changes in the content of version 5.0 as well some changes in scope and philosophy that took place during the developement of version 5.0.

## What's new in 5.0

The following sections try and cover the most major changes

### Complete renumbering and reordering

Almost every single requirement has been modified in some way and even those that were not modified or moved will have numbering changes as a result of reordering or other requirements moving around.

The provided mappings should help trace if and where requirements from version 4.0 made it into version 5.0.

### Less coupling with NIST Digital Identity Guidelines

The NIST's [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) has been and continues to be an excellent, evidence driven standard for key controls around authentication and authorization. Certain chapters in version 4.0 were very closely coupled with these guidelines including structure and terminology.

Whilst these guidelines and their upcoming improvements have continued to be an important reference and the basis for many requirements, the strict coupling caused challenges which led to the decision to move away from this approach. These challenges included terminology which was less widely recognised, duplication of very similar requirements in very slightly different situations, and the fact that the mapping was incomplete based on what was perceived to be relevant for ASVS.

### Moving away from Common Weakness Enumeration (CWE)

The [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) from Mitre is a useful way to map out different security weaknesses in software. There are some difficulties in using it including certain CWEs which are categories only and shouldn't be used for mapping, the difficulties in mapping certain existing requirements to a single CWE, and also the fact that there were some loose or inexact mappings in version 4.0 of ASVS.

The solution was to remove CWE (and any other mappings) with the aim of instead mapping to the OWASP Common Requirement Enumeration (CRE) project which will map ASVS to a variety of other OWASP projects and external standards.

### Focus on the goal, not the mechanism

In version 4.0, there were many requirements that were focused around a particular mechanism rather than focusing on the security goal to achieve. In version 5.0, unless there is only one realistic mechanism to achieve the goal. requirements focus on the security goal and either include specific mechanism as examples or link to other guidance.

### Documenting Security Decisions

For certain requirements, implementation will be complicated and very specific to an application's needs. Common examples include permissions, input validation, and the protective controls around different levels of sensitive data. To account for this, rather than sweeping statements like "all data must be encrypted" or trying to cover every possible use case in a requirement, we have certain requirements which mandate that the application developer's approach and configuration to these sorts of controls must be documented so that this can be reviewed for appropriateness and then the actual implementation can be compared to the documentation to assess whether the implementation matches expectations.

### TODO: add more items

<!--
We set out to ensure that the ASVS 4.0 Level 1 is a comprehensive superset of PCI DSS 3.2.1 Sections 6.5, for application design, coding, testing, secure code reviews, and penetration tests. This necessitated covering buffer overflow and unsafe memory operations in V5, and unsafe memory-related compilation flags in V14, in addition to existing industry-leading application and web service verification requirements.

We have completed the shift of the ASVS from monolithic server-side-only controls, to providing security controls for all modern applications and APIs. In the days of functional programming, server-less API, mobile, cloud, containers, CI/CD and DevSecOps, federation and more, we cannot continue to ignore modern application architecture. Modern applications are designed very differently from those built when the original ASVS was released in 2009. The ASVS must always look far into the future so that we provide sound advice for our primary audience - developers. We have clarified or dropped any requirement that assumes that applications are executed on systems owned by a single organization.

Due to the size of the ASVS 4.0, as well as our desire to become the baseline ASVS for all other ASVS efforts, we have retired the mobile chapter, in favor of the Mobile Application Security Verification Standard (MASVS). We have also retired the Internet of Things appendix, in favor of the IoT Security Verification Standard (ISVS). We thank both the OWASP Mobile Team and OWASP IoT Project Team for their support of the ASVS, and look forward to working with them in the future to provide complementary standards.

Lastly, we have de-duped and retired less impactful controls. Over time, the ASVS started being a comprehensive set of controls, but not all controls equally contribute to producing secure software. This effort to eliminate low-impact items could go further. In a future edition of the ASVS, the Common Weakness Scoring System (CWSS) will help prioritize further those controls that are truly important and those that should be retired.

As of version 4.0, the ASVS will focus solely on being the leading web apps and service standard, covering traditional and modern application architecture, agile security practices and DevSecOps culture.
-->

## Additional rationale for the change in levels approach

Version 4.0 of the ASVS describes the levels as L1 - "Minimum", L2 - "Standard", and L3 - "Advanced" with the implication that all applications processing sensitive data should be at least L2.

We found a few challenges with this approach and users of version 4.0 might find the following context on the change to levels approach informative in addition to the rationale in the previous chapter.

### High barrier to entry

L1 in version 4.0 had over 100 requirements as did L2 with only a few requirements left in L3. This meant that a high level of effort required to achieve even L1 at which point the user is told that this is the "minimum" level and that to achieve a "standard" level of security, another 100 requirements are required. Based on feedback from ASVS users and community it became clear that this acted as a disincentive and made it harder for applications to start adopting the ASVS.

### The fallacy of testability

A primary motivator behind putting controls in L1 version 4.0 was whether they could be checked using "black box" style testing which was not entirely in line with the concept of L1 being the minimum security controls. On the one hand, ASVS users would say that L1 was not sufficient for a secure application whilst on the other hand user would complain that ASVS was too difficult to test.

Additionally, testability is relative and in some cases misleading. Just because something is testable does not mean that it is testable in an automated or trivial way. Finally, the most testable requirements are not necessarily those that have the most important security impact or are the easiest to implement.

### Not just about risk

The use of prescriptive, risk based levels which mandate that a certain application has to be at a certain level seems overly opinionated in hind-sight. In reality, the order of implementing security controls will depend on factors including both risk reduction and also effort to implement.
