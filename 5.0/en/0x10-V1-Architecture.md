# V1 Security Decision Documentation

## Control Objective

This paragraph contains documentation requirements that are pre-conditions for implementation and testing.

Note that the documentation requirements here are a temporary solution, and it is yet to be decided how to organize them in the release. The requirements, that or not documentation requirements, are subject to be removed or moved.
<!--
Security architecture has almost become a lost art in many organizations. The days of the enterprise architect have passed in the age of DevSecOps. The application security field must catch up and adopt agile security principles while re-introducing leading security architecture principles to software practitioners. Architecture is not an implementation, but a way of thinking about a problem that has potentially many different answers, and no one single "correct" answer. All too often, security is seen as inflexible and demanding that developers fix code in a particular way, when the developers may know a much better way to solve the problem. There is no single, simple solution for architecture, and to pretend otherwise is a disservice to the software engineering field.

A specific implementation of a web application is likely to be revised continuously throughout its lifetime, but the overall architecture will likely rarely change but evolve slowly. Security architecture is identical - we need authentication today, we will require authentication tomorrow, and we will need it five years from now. If we make sound decisions today, we can save a lot of effort, time, and money if we select and re-use architecturally compliant solutions. For example, a decade ago, multi-factor authentication was rarely implemented.

If developers had invested in a single, secure identity provider model, such as SAML federated identity, the identity provider could be updated to incorporate new requirements such as NIST SP 800-63 compliance, while not changing the interfaces of the original application. If many applications share the same security architecture and thus that same component, they all benefit from this upgrade at once. However, SAML may not always remain the most suitable authentication solution - it might need to be swapped out for other solutions as requirements change. Changes like this are either complicated, so costly as to necessitate a complete rewrite, or outright impossible without security architecture.

In this chapter, the ASVS covers the primary aspects of any sound security architecture: availability, confidentiality, processing integrity, non-repudiation, and privacy. Each of these security principles must be built in and be innate to all applications. It is critical to "shift left", starting with developer enablement with secure coding checklists, mentoring and training, coding and testing, building, deployment, configuration, and operations, and finishing with follow-up independent testing to ensure that all of the security controls are present and functional. The last step used to be everything we did as an industry, but that is no longer sufficient when developers push code into production tens or hundreds of times a day. Application security professionals must keep up with agile techniques, which means adopting developer tools, learning to code, and working with developers rather than criticizing the project months after everyone else has moved on.
-->

## V1.1 Secure Software Development Lifecycle

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.1.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.2** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.3** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.4** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.5** | [MOVED TO 1.14.7] | | | | |
| **1.1.6** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.1.7** | [DELETED, NOT IN SCOPE] | | | | |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
* [More information on security.txt including a link to the RFC](https://securitytxt.org/)
