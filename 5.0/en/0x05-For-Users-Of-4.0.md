# Changes compared to v4.x

## Introduction

Existing users of the 4.x version of the standard may find it useful to see some of the key changes in the content of version 5.0 as well some changes in scope and philosophy that took place during the development of version 5.0.

Overall, only 11 out of 286 requirements from version 4.0.3 have stayed as they were and 15 requirements had grammar changes but no change to the requirement's meaning. The rest have been modified in some way. Even those requirements that were not modified or moved will have numbering changes as a result of reordering or other requirements moving around.

To make it easier to adopt version 5.0, mappings have been provided which should help trace if and where requirements from version 4.x made it into version 5.0.

These mappings are not covered by release versioning so can be updated or clarified where necessary.

## Requirement Philosophy

### Scope and focus

Version 4.x had various requirements that did not fit with the implied scope of the other requirements and these have been removed. Requirements that did not meet the scope criteria for 5.0 or were not verifiable were also removed.

### Focus on the security goal, not the mechanism

In version 4.x, many requirements were focused on a particular mechanism rather than on the security goal to achieve. In version 5.0, unless there is only one realistic mechanism to achieve the goal, requirements focus on the security goal and either include specific mechanisms as examples or link to other guidance.

This is important as often there will be multiple ways of achieving a particular goal and being too prescriptive would remove that flexibility from an organization.

Also, certain requirements were merged where it was felt that multiple requirements had been written to address the same security problem.

### Documented security decisions

Documented security decisions may feel like a completely new concept in version v5.0, but it is not so. In version v4.0 there were requirements to apply for policies or to have a threat model. In some cases those contained "hidden requirements" - for example, something must be analyzed to be used as information for implementing security controls, such as allowed incoming and outgoing connections.

To have expected information available for implementation and verification steps, those requirements are implemented into the ASVS as "documentation requirements" to have clear, actionable, and verifiable requirements.

## Structure changes and new chapters

There are some chapters containing brand new content for version 5.0:

* OAuth and OIDC - These have become pervasive as mechanisms for access delegation and single sign-on over the last several years and it was seen as important to call out some specific requirements in this area, covering different areas which an application developer might find themselves implementing. It is possible this could become its own standard in the future in the same way that the requirements for Mobile and IoT grew to their own projects.
* WebRTC - This is another technology which is growing in popularity and has its own security considerations and challenges.

Additionally, an effort was made to ensure that chapters and sections are focused on a particular set of requirements that go together.

This also led to some new chapters being created:

* Self-contained Tokens - Whilst previously considered as part of session management, the wider set of use cases for this highly popular mechanism led to the creation of a dedicated chapter to cover the various security pitfalls involved, most of which were new for version 5.x.
* Web Frontend Security - With a growing number of security considerations when rendering applications in a browser as well as an increase in API only development where these considerations would not be relevant, it was decided to split these requirements into a dedicated chapter.
* Secure Coding and Architecture - A number of new requirements were developed that related to general security considerations which are required to make the application secure, which did not fit well into existing chapters. We grouped these together into this new chapter.

There were also some other moves that took effect in version 5.0 to "send a message". Such as, Input Validation was moved away from Sanitization and Encoding to be together with business logic, since the intent of input validation is to enforce the business rules for the input being received.

The Old V1 Architecture chapter has been removed. The first section of this chapter was primarily requirements which were not in scope and the subsequent sections mapped to other individual chapters. The requirements from these subsequent which were still in scope were therefore moved to the relevant chapters themselves, being deduplicated and clarified along the way.

## Removed direct mappings to other standards

We removed the mappings that appear on the face of the standard with the aim of mapping version 5.0 just to the OWASP Common Requirement Enumeration (CRE) project which will map ASVS to a variety of other OWASP projects and external standards.

We also no longer map directly to CWE or to NIST as will be explained in the following sections.

### Less coupling with NIST Digital Identity Guidelines

The NIST's [Digital Identity Guidelines (SP 800-63)](htps://pages.nist.gov/800-63-3/) has been and continues to be an excellent, evidence-driven standard for key controls around authentication and authorization. Certain chapters in version 4.x were very closely coupled with these guidelines, including structure and terminology.

Whilst these guidelines and their upcoming improvements have continued to be an important reference and the basis for many requirements, the strict coupling caused challenges which led to the decision to move away from this approach. These challenges included terminology which was less widely recognised, duplication of very similar requirements in very slightly different situations, and the fact that the mapping was incomplete based on what was perceived to be relevant for ASVS.

### Moving away from Common Weakness Enumeration (CWE)

The [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) from MITRE is a useful way to map out different security weaknesses in software. There are some difficulties in using it including certain CWEs which are categories only and shouldn't be used for mapping, the difficulties in mapping certain existing requirements to a single CWE, and also the fact that there were some loose or inexact mappings in version 4.x of ASVS.

## Rethinking the level definitions

Version 4.x of the ASVS describes the levels as L1 - "Minimum", L2 - "Standard", and L3 - "Advanced" with the implication that all applications processing sensitive data should be at least L2.

There were various issues with this approach that version 5.0 was specifically designed to address.

### Easier entry level

From feedback on the use (or non-use) of previous ASVS versions in industry, the single greatest problem that was identified was the double-edged sword of Level 1 having a large number of requirements (~120) but at the same time being considered the "minimum" level that is not good enough for most applications. This seemed to lead to organizations either giving up before they start or trying to implement a subset of the requirements without actually achieving Level 1, therefore reducing the sense of achievement and progress.

### The fallacy of testability

A primary motivator behind putting controls in Level 1 version 4.x was whether they could be checked using "black box" style external penetration testing which was not entirely in line with the concept of Level 1 being the minimum security controls. On the one hand, ASVS users would say that Level 1 was not sufficient for a secure application whilst on the other hand, users would complain that ASVS was too difficult to test.

Additionally, using testability as a factor is relative and in some cases misleading. Just because something is testable does not mean that it is testable in an automated or trivial way. Finally, the most testable requirements are not necessarily those that have the most important security impact or are the easiest to implement.

### Not just about risk

The use of prescriptive, risk-based levels that mandate that a certain application has to be at a certain level seems overly opinionated in hind-sight. In reality, the order of implementing security controls will depend on factors including both risk reduction and also effort to implement.
