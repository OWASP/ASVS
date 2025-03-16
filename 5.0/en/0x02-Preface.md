# Preface

Welcome to the Application Security Verification Standard (ASVS) version 5.0!

## Introduction

The ASVS is a community-driven effort to establish a standard that defines the security requirements to consider when designing, developing and testing modern web applications and web services.

ASVS Version 5.0 is the culmination of a huge amount of effort from the leaders, working group and other community members to update and improve this important standard.

Our goal for this version has been to make the ASVS easier to use whilst also making it more clearly focused on a particular scope and covering new, important areas of application developement.

## Key Objectives from ASVS Version 5.0

Version 5.0 has been developed with a number of key principles in mind.

### Clear set of requirements

The set of requirements for version 5.0 was prepared based on the following considerations.

* Aggressively deduplicating requirements to avoid controls or concepts being split into multiple places.
* Clarifying unclear or non-actionable requirement text.
* Adding new requirements to cover areas of particular concern such as permissions, tokens, and cryptography.
* Adding new chapters and sections for areas which might not apply to all applications but are still security sensitive such as OAuth and WebSockets.

### Clarifying the scope of the standard

It is important that all requirments are relevant to the defined scope of the standard and that they are worded in a way that is consistent with the goal of the standard.

The guidelines for this were:

* Ensuring that all requirements are within the scope of a web application or service.
* Checking that requirements are worded in line with the ASVS name, specifically:
  * Application - Requirements are at the application level and are the responsibility of application developers.
  * Security - Requirements are clearly necessary for the application to be secure.
  * Verification - Requirements are worded to have a clear and verifiable goal.
  * Standard - Clear consistency and structure to requirements, as would be expected from a standard.

### Better level definitions

The levels in version 5.0 aim to make the ASVS easier to adopt whilst also being clear about why requirements were allocated to specific levels.

This includes:

* Making level rationale clearer and with the primary focus on priority (considering risk reduction and effort to implement).
* Having a realistic number of Level 1 requirements so as to have a lower barrier to entry.
* Balancing better between the number of requirments in Level 2 and Level 3 to allow smoother progression.

### Streamlining the document

Part of making the document easier to use is keeping the actual requirements front and centre and avoiding unnecessary narrative content, whilst keeping key explanations.

This includes:

* Avoiding too much explanatory or supplementary text around the requirements except where this is specifically necessary.
* Instead of overly verbose requirements, keeping them abstract and refering to relevant cheat-sheets or other materials in the explanatory text.
* Keeping mappings away from the core requirements but rather separating them to be managed and maintained separately.

## Usability to drive adoption

We hope that this increase in usability drives a corresponding increase in adoption by organizations who want to improve the security of their application or the consistency and rigour of their security assessments.

More detail on using the standard can be found in subsequent chapters.