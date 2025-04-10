# Preface

Welcome to the Application Security Verification Standard (ASVS) version 5.0!

## Introduction

Established in 2008 through a collaborative community effort, the ASVS defines the security requirements to be considered when designing, developing, and testing modern web applications and web services.

ASVS version 5.0 is the culmination of significant effort from the leaders, the working group, and other community members to update and improve this important standard.

Our goal for this version has been to make the ASVS easier to use while also making it more clearly focused on its defined scope and covering new, important areas of application development.

## Key Objectives from ASVS Version 5.0

Version 5.0 has been developed with several key principles in mind.

### Clear Set of Requirements

The requirements for version 5.0 were prepared based on the following considerations:

* Aggressively deduplicate requirements to avoid controls or concepts being split across multiple places.
* Clarify unclear or non-actionable requirement text.
* Add new requirements to cover areas of particular concern, such as permissions, tokens, and cryptography.
* Introduce new chapters and sections for areas that might not apply to all applications yet remain security-sensitive (e.g., OAuth and WebSockets).

### Clarifying the Scope of the Standard

It is important that all requirements are relevant to the defined scope of the standard and are worded consistently with its goals. The guidelines for this were:

* Ensure that all requirements are within the scope of a web application or service.
* Verify that requirements align with the ASVS name, specifically:
    * **Application** – Requirements are at the application level and are the responsibility of application developers.
    * **Security** – Requirements are clearly necessary to secure the application.
    * **Verification** – Requirements are written with a clear, verifiable goal.
    * **Standard** – Requirements exhibit clear consistency and structure, as expected from a standard.

### Better Level Definitions

The levels in version 5.0 are designed to make the ASVS easier to adopt while clarifying why requirements have been allocated to specific levels. This includes:

* Clarifying level rationale with a primary focus on priority (considering risk reduction and implementation effort).
* Establishing a realistic number of Level 1 requirements to lower the barrier to entry.
* Better balancing the number of requirements between Level 2 and Level 3 to allow smoother progression.

### Streamlining the Document

To make the document easier to use, the actual requirements are kept front and center, while unnecessary narrative content is minimized—retaining only key explanations. This includes:

* Avoiding excessive explanatory or supplementary text around the requirements except where specifically necessary.
* Keeping requirements abstract instead of overly verbose, with references to relevant cheat sheets or other materials for further explanation.
* Separating mappings from the core requirements so that they can be managed and maintained independently.

## Usability to Drive Adoption

We hope that this increase in usability drives a corresponding increase in adoption by organizations seeking to improve the security of their applications or the consistency and rigour of their security assessments.

More detail on using the standard can be found in subsequent chapters.
