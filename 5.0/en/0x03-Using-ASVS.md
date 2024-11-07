# Using the ASVS

The ASVS defines functional and non-functional security requirements for modern web applications and services, focusing on application content rather than secure development processes, which are covered in [OWASP SAMM](https://owaspsamm.org/).

The ASVS is useful for anyone aiming to develop, maintain, or evaluate secure applications. This chapter covers key aspects of using the ASVS, including risk-based levels and various use cases for the standard

## Application Security Verification Levels

The Application Security Verification Standard defines three security verification levels, with each level increasing in depth.

* ASVS Level 1 is for low assurance levels and is completely verifiable through penetration testing.
* ASVS Level 2 is for applications that contain sensitive data, which requires protection and is the recommended level for most apps.
* ASVS Level 3 is intended for the most critical applications, such as those handling high-value transactions, containing sensitive medical data, or any application demanding the highest level of trust.

Each ASVS level lists security requirements, which developers must integrate into software. Level 1 can be tested solely through penetration testing, though this 'black box' approach is limited and insufficient for thorough security assurance. Unlike attackers, who have ample time, defenders must prevent, identify, and resolve vulnerabilities swiftly. Black box testing, often done late or briefly, fails to address this imbalance and misses critical issues, as evidenced by decades of breaches.

We recommend hybrid testing at Level 1, with full access to developers and documentation, similar to transparent financial audits. Continuous security tool use, like DAST and SAST in the build pipeline, can address basic security issues early.

Automation alone can't complete over half of ASVS requirements; human insight is essential for tasks like testing business logic and access controls, which should be incorporated as unit and integration tests.

## How to use this standard

One of the best ways to use the Application Security Verification Standard is to use it as a blueprint to create a Secure Coding Checklist specific to your application, platform or organization. Tailoring the ASVS to your use cases will increase the focus on the security requirements that are most important to your projects and environments.

### Level 1 - First steps, automated, or whole of portfolio view

An application meets ASVS Level 1 if it defends against easily discovered security vulnerabilities, such as those in the OWASP Top 10. Level 1 is the minimum standard for all applications, particularly those without sensitive data, and is useful as a starting point in phased security efforts. Controls at this level can be verified automatically or manually without source code access.

Level 1 primarily addresses threats from attackers using simple techniques to exploit obvious vulnerabilities, rather than dedicated attackers. Applications handling high-value data generally require more rigorous controls beyond Level 1.

### Level 2 - Most applications

An application meets ASVS Level 2 if it defends against most contemporary software risks. Level 2 ensures that security controls are implemented, effective, and actively used. This level is suitable for applications managing significant B2B transactions, sensitive data like healthcare information, critical business functions, or industries needing integrity, such as gaming to prevent cheating.

Level 2 applications face threats from skilled attackers targeting specific vulnerabilities with sophisticated, effective tools and techniques.

### Level 3 - High value, high assurance, or high safety

ASVS Level 3, the highest verification level, is reserved for applications needing extensive security, such as those in military, health, safety, or critical infrastructure. This level is appropriate for applications where failure would severely impact an organization’s operations.

To achieve ASVS Level 3, an application must defend against advanced security vulnerabilities and demonstrate sound security design. This requires in-depth analysis of architecture, code, and testing. Secure applications at Level 3 are modularized for resiliency, scalability, and layered security, with each module responsible for its own security functions, including confidentiality, integrity, availability, authentication, authorization, and auditing, all thoroughly documented.

## How to Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>` where each element is a number, for example, `1.11.3`.

* The `<chapter>` value corresponds to the chapter from which the requirement comes, for example, all `1.#.#` requirements are from the `Architecture` chapter.
* The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.11.#` requirements are in the `Business Logic Architectural Requirements` section of the `Architecture` chapter.
* The `<requirement>` value identifies the specific requirement within the chapter and section, for example, `1.11.3` which as of version 4.0.2 of this standard is:

> Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.

Since the identifiers may change between versions of the standard, it is preferable for other documents, reports, or tools to use the following format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v4.0.2-1.11.3` would be understood to mean specifically the 3rd requirement in the 'Business Logic Architectural Requirements' section of the 'Architecture' chapter from version 4.0.2. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version number in the format should always be lowercase.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. As the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ASVS requirement lists are made available in CSV, JSON, and other formats which may be useful for reference or programmatic use.

## Forking the ASVS

Organizations can benefit from adopting ASVS by choosing one of the three levels or by creating a domain-specific fork that adjusts requirements per application risk level. We encourage such forking, provided it maintains traceability so that passing requirement 4.1.1 means the same across all versions.

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, Websockets, SOAP, if unused). Forking should start with ASVS Level 1 as a baseline, advancing to Levels 2 or 3 based on the application’s risk.

## Uses for the ASVS

The ASVS can be used to assess the security of an application and this is explored in more depth in the next chapter. However, we have identified several other potential uses for the ASVS (or a forked version).

### As Detailed Security Architecture Guidance

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. The Sherwood Applied Business Security Architecture (SABSA) is missing a great deal of information that is necessary to complete a thorough application security architecture review. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies.

### As a Specialized Secure Coding Checklist

The ASVS can be used as a secure coding checklist for secure application development, helping developers to make sure that they keep security in mind when they build software. The secure coding checklist should be unified, clear, and applicable to all development teams. It should ideally be prepared based on guidance from security engineers or security architects

### As a Guide for Automated Unit and Integration Tests

The ASVS is designed to be highly testable, with the sole exception of architectural and malicious code requirements. By building unit and integration tests that test for specific and relevant fuzz and abuse cases, the application becomes nearly self-verifying with each and every build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common default usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, and more.

### For Secure Development Training

ASVS can also be used to define the characteristics of secure software. Many “secure coding” courses are simply ethical hacking courses with a light smear of coding tips. This may not necessarily help developers to write more secure code. Instead, secure development courses can use the ASVS with a strong focus on the proactive controls found in the ASVS, rather than the Top 10 negative things not to do.

### As a Driver for Agile Application Security

ASVS can be used in an agile development process as a framework to define specific tasks that need to be implemented by the team to have a secure product. One approach might be: Starting with Level 1, verify the specific application or system according to ASVS requirements for the specified level, find what controls are missing and raise specific tickets/tasks in the backlog. This helps with the prioritization of specific tasks (or grooming) and makes security visible in the agile process. This approach can also be employed to prioritize auditing and review tasks within the organization. A specific ASVS requirement can drive a review, refactor, or audit for a particular team member, and be visible as 'debt' in the backlog that must eventually be addressed.

### As a Framework for Guiding the Procurement of Secure Software

ASVS is a great framework to help with secure software procurement or procurement of custom development services. The buyer can simply set a requirement that the software they wish to procure must be developed at ASVS level X, and request that the seller proves that the software satisfies ASVS level X. This works well when combined with the OWASP Secure Software Contract Annex

## Applying ASVS in Practice

Different threats have different motivations. Some industries have unique information and technology assets and domain-specific regulatory compliance requirements.

Organizations are strongly encouraged to look deeply at their unique risk characteristics based on the nature of their business, and based upon that risk and business requirements determine the appropriate ASVS level.

We have received feedback from various members of the community on how they implement the standard in practice:

### Personal Case Studies

#### Matthew Hackling

* Drive pen test scope and test cases
* Drive security requirements for designs help
* Populate an ISO27034 organisational normative framework aka requirements library.

#### Dominique Righetto

* Used for code review and as a checklist when performing web application vulnerability assessments.

#### Giovanni Cruz

* In the last OWASP Latam Tour Bogotá 2019 a training course was prepared totally based on ASVS. All the content was created with a vulnerable platform for training to assist developers. It got a great feedback because they showed them how to use it and what levels of security they might want to achieve based on some standard.

#### Sebastien Gioria

* For some customers, uses it as a basis for mandatory requirements to perform secure design and coding.

#### Riotaro Okada

* In recent years, observed some banks in Japan included ASVS into their RFP for security testing services, as their mandatory requirement. They wanted proposals which security vendors would fit appropriate ASVS levels.
* A local software vendor in Japan sells SFA related packages received customer criteria to check whether their products would fit ASVS, and which levels the product aligned to. (It was a good start for the vendor to introduce secure development and verifications into their teams)

#### John Patrick Lita

* Uses this and integrates this in their CI/CD activity

### Use within other projects and tools

* OWASP Defectdojo has built-in ASVS support https://www.defectdojo.org/
* A few weeks after the ASVS 4 release, RIPS added support for it: https://blog.ripstech.com/2019/rips-3.1-adds-teamcity-ldap-jsp-support/
