# Appendix X: Recommendations

## Introduction

Whilst preparing version 5.0 of the Application Security Verification Standard (ASVS), it became clear that there were a number of existing and newly suggested items that we didn't want to include as requirements in 5.0. This may have been because they were not in scope for ASVS as per the definition for 5.0 or alternatively we did not feel we could make them mandatory, even through we felt they were a good idea.

We did not want to lose these items entirely, so we tried to capture some of them in this appendix.

## Recommended in-scope mechanisms

The following items are within ASVS' scope. We don't think they should be made mandatory but we would strongly recommend considering them as part of a secure application.

* A password strength meter should help users set a stronger password.
* Create a publicly available security.txt file at the application's root or well-known directory that clearly defines a link or e-mail address for people to contact the owners about security issues.
* Client-side input validation should be enforced in addition to validation at a trusted service layer, as this provides a good opportunity to discover when someone has bypassed client-side controls in an attempt to attack the application.
* Use a robots.txt file, the X-Robots-Tag response header, or a robot's HTML meta tag to prevent accidentally accessible and sensitive pages from appearing in search engines.
* Verify that all pages that require authentication have easy and visible access to logout functionality.

## Software Security processes

Several security processes were removed from ASVS 5.0 but are still a good idea. The OWASP SAMM project may be a good source for how to implement these processes effectively. The items which were previously in ASVS include:

* Verify the use of a secure software development lifecycle that addresses security in all stages of development.
* Verify threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing.
* Verify that all user stories and features contain functional security constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else's profile."
* Verify that a secure coding checklist, security requirements, guidelines, or policy is available to all developers and testers.
