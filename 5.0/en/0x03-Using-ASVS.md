# Using the ASVS

The ASVS defines functional and non-functional security requirements for modern web applications and services, focusing on application content rather than secure development processes, which are covered in [OWASP SAMM](https://owaspsamm.org/).

The ASVS is useful for anyone aiming to develop and maintain secure applications, or evaluate the security of applications. This chapter covers key aspects of using the ASVS, including priority-based levels and various use cases for the standard

## Application Security Verification Levels

The Application Security Verification Standard defines three security verification levels, with each level increasing in depth and complexity.

In version 4.0, we described the levels as L1 - "Mininum", L2 - "Standard", and L3 - "Advanced" with the implication that all applications processing sensitive data should be at least L2.

### Challenges with the previous approach

There are a few challenges with this approach.

#### High barrier to entry

L1 in version 4.0 had over 100 requirements as did L2 with only a few requirements left in L3. This meant that a high level of effort required to achieve even L1 at which point the user is told that this is the "minimum" level and that to achieve a "standard" level of security, another 100 requirements are required. In our discussions for version 5.0, we felt like this was demoralizing and made it harder for applications to start adopting the ASVS. 

#### The fallacy of testability

A primary motivator behind putting controls in L1 version 4.0 was whether they could be checked using "black box" style testing which was not entirely in line with the concept of L1 being the minimum security controls. On the one hand, we would hear from users that L1 was not sufficient for a secure application whilst on the other hand we would get complaints that ASVS was too difficult to test.

Additionally, testability is relative and in some cases misleading. Just because something is testable does not mean that it is testable in an automated or trivial way. Also, the most testable requirements are not necessary those that have the most important security impact or are the easiest to implement.

#### Not just about risk

We dislike the concept of prescriptive, risk based levels which mandate that a certain application has to be at a certain level. In our experience, the order of implementing security controls will depend on factors including both risk reduction and also effort to implement. 

### Our approach for v5.0

As such, for version 5.0 we have moved to a priority based evaluation of each requirement based on our combined experience implementing security requirements which takes into account both the risk reduction which the requirement brings and also the difficulty and complexity of implementing the requirement.




* ASVS Level 1 is for low assurance levels and is completely verifiable through penetration testing.
* ASVS Level 2 is for applications that contain sensitive data, which requires protection and is the recommended level for most apps.
* ASVS Level 3 is intended for the most critical applications, such as those handling high-value transactions, containing sensitive medical data, or any application demanding the highest level of trust.

Each ASVS level contains a list of security requirements. Each of these requirements can also be mapped to security-specific features and capabilities that must be built into software by developers.

Level 1 is the only level that is completely penetration testable using humans. All others require access to documentation, source code, configuration, and the people involved in the development process. However, even if L1 allows "black box" (no documentation and no source) testing to occur, it is not an effective assurance activity and should be actively discouraged. Malicious attackers have a great deal of time, most penetration tests are over within a couple of weeks. Defenders need to incorporate security controls, protect, find and resolve all weaknesses, and detect and respond to malicious actors in a reasonable time. Malicious actors have essentially infinite time and only require a single porous defense, a single weakness, or missing detection to succeed. Black box testing, often performed at the end of development, quickly, or not at all, is completely unable to cope with that asymmetry.

Over the last 30+ years, black box testing has proven over and over again to miss critical security issues that led directly to ever more massive breaches. We strongly encourage the use of a wide range of security assurance and verification, including replacing penetration tests with source code-led (hybrid) penetration tests at Level 1, with full access to developers and documentation throughout the development process. Financial regulators do not tolerate external financial audits with no access to the books, sample transactions, or the people performing the controls. Industry and governments must demand the same standard of transparency in the software engineering field.

We strongly encourage the use of security tools within the development process itself. DAST and SAST tools, when continuously implemented in the build pipeline, can effectively identify and address straightforward security issues that should never exist.

Automated tools and online scans are unable to complete more than half of the ASVS without human assistance. If comprehensive test automation for each build is required, then a combination of custom unit and integration tests, along with build-initiated online scans are used. Business logic flaws and access control testing are only possible using human assistance. These should be turned into unit and integration tests.

## How to use this standard

One of the best ways to use the Application Security Verification Standard is to use it as a blueprint to create a Secure Coding Checklist specific to your application, platform or organization. Tailoring the ASVS to your use cases will increase the focus on the security requirements that are most important to your projects and environments.

### Level 1 - First steps, automated, or whole of portfolio view

An application achieves ASVS Level 1 if it adequately defends against application security vulnerabilities that are easy to discover and included in the OWASP Top 10 and other similar checklists.

Level 1 is the bare minimum that all applications should strive for. It is also useful as a first step in a multi-phase effort or when applications do not store or handle sensitive data and therefore do not need the more rigorous controls of Level 2 or 3. Level 1 controls can be checked either automatically by tools or simply manually without access to the source code. We consider Level 1 the minimum required for all applications.

Threats to the application will most likely be from attackers who are using simple and low-effort techniques to identify easy-to-find and easy-to-exploit vulnerabilities. This is in contrast to a determined attacker who will spend focused energy to specifically target the application. If your application processes high-value data, you would rarely want to stop at a Level 1 review.

### Level 2 - Most applications

An application achieves ASVS Level 2 (or Standard) if it adequately defends against most of the risks associated with software today.

Level 2 ensures that security controls are in place, effective, and used within the application. Level 2 is typically appropriate for applications that handle significant business-to-business transactions, including those that process healthcare information, implement business-critical or sensitive functions, or process other sensitive assets, or industries where integrity is a critical facet to protect their business, such as the game industry to thwart cheaters and game hacks.

Threats to Level 2 applications will typically be skilled and motivated attackers focusing on specific targets using tools and techniques that are highly practiced and effective at discovering and exploiting weaknesses within applications.

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
