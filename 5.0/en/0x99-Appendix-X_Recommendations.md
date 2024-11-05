# Appendix X: Recommendations

## Introduction

Whilst preparing version 5.0 of the Application Security Verification Standard (ASVS), it became clear that there were a number of existing and newly suggested items that we didn't want to include as requirements in 5.0. This may have been because they were not in scope for ASVS as per the definition for 5.0 or alternatively we did not feel we could make them mandatory, even through we felt they were a good idea.

We did not want to lose these items entirely so we have tried to capture some of them in this appendix.

## Recommended, in-scope mechanisms

The following items are in-scope for ASVS. We don't think they should be made mandatory but we would strongly recommend considering them as part of a secure application.

* A password strength meter should provided to help users set a stronger password.
* Create a publicly available security.txt file at the root or .well-known directory of the application that clearly defines a link or e-mail address for people to contact owners about security issues.
* Client-side input validation should be enforced in addition to validation at a trusted service layer as this provides a good opportunity to discover when someone has bypassed client-side controls in an attempt to attack the application.
* Prevent accidentally accessible and sensitive pages from appearing in search engines using a robots.txt file, the X-Robots-Tag response header or a robots html meta tag.

## Software Security principles

The following items were previously in ASVS but are not really requirements. Rather they are principles to consider when implementing security controls that when followed will lead to more robust controls. These include:

* Security controls should be centralized, simple (economy of design), verifiably secure, and reusable. This should avoid duplicate, missing, or ineffective controls.
* Ideally, A single and well-vetted access control mechanism should be used to access protected data and resources. All requests should pass through this single mechanism to avoid copy and paste or insecure alternative paths.
* Attribute or feature-based access control is a recommended pattern whereby the code checks the user's authorization for a feature or data item rather than just their role. Permissions should still be allocated using roles.

## Software Security processes

There are a number of security processes which were removed from ASVS 5.0 but are still a good idea. The OWASP SAMM project may be a good source for how to effectively implement these processes. The items which were previously in ASVS include:

* Verify the use of a secure software development lifecycle that addresses security in all stages of development.
* Verify the use of threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing.
* Verify that all user stories and features contain functional security constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else's profile"
* Verify availability of a secure coding checklist, security requirements, guideline, or policy to all developers and testers.
* Verify that an ongoing process exists to ensure that the application source code is free from backdoors, malicious code (e.g., salami attacks, logic bombs, time bombs), and undocumented or hidden features (e.g., Easter eggs, insecure debugging tools). Complying with this section is not possible without complete access to source code, including third-party libraries, and is therefore probably only suitable for applications requiring the very highest levels of security.
