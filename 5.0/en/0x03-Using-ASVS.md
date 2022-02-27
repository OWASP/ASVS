# Using the ASVS

As noted in the preface, the ASVS is a standard that defines the functional and non-functional security requirements to consider for modern web applications and web services.

It therefore focuses on the content of the application and not the secure processes by which the application should be developed. Secure Development processes are better covered in the [OWASP SAMM](https://owaspsamm.org/) project and are not the primary scope of the ASVS.

In the contents of secure requirements, the ASVS should be useful to anyone trying to:
* Develop and maintain secure applications.
* Evaluate the security of applications.

This chapter will talk about some of the key aspects of using the ASVS including using the levels to take a risk-baesd approach and different use cases for the standard.

## Application Security Verification Levels

The Application Security Verification Standard defines three security verification levels, with each level increasing in depth.

* ASVS Level 1 is for low assurance levels, and is completely penetration testable
* ASVS Level 2 is for applications that contain sensitive data, which requires protection and is the recommended level for most apps
* ASVS Level 3 is for the most critical applications - applications that perform high value transactions, contain sensitive medical data, or any application that requires the highest level of trust.

Each ASVS level contains a list of security requirements. Each of these requirements can also be mapped to security-specific features and capabilities that must be built into software by developers.

Level 1 is the only level that is completely penetration testable using humans. All others require access to documentation, source code, configuration, and the people involved in the development process. However, even if L1 allows "black box" (no documentation and no source) testing to occur, it is not an effective assurance activity and should be actively discouraged. Malicious attackers have a great deal of time, most penetration tests are over within a couple of weeks. Defenders need to build in security controls, protect, find and resolve all weaknesses, and detect and respond to malicious actors in a reasonable time. Malicious actors have essentially infinite time and only require a single porous defense, a single weakness, or missing detection to succeed. Black box testing, often performed at the end of development, quickly, or not at all, is completely unable to cope with that asymmetry.

Over the last 30+ years, black box testing has proven over and over again to miss critical security issues that led directly to ever more massive breaches. We strongly encourage the use of a wide range of security assurance and verification, including replacing penetration tests with source code led (hybrid) penetration tests at Level 1, with full access to developers and documentation throughout the development process. Financial regulators do not tolerate external financial audits with no access to the books, sample transactions, or the people performing the controls. Industry and governments must demand the same standard of transparency in the software engineering field.

We strongly encourage the use of security tools within the development process itself. DAST and SAST tools can be used continuously by the build pipeline to find easy to find security issues that should never be present.

Automated tools and online scans are unable to complete more than half of the ASVS without human assistance. If comprehensive test automation for each build is required, then a combination of custom unit and integration tests, along with build initiated online scans are used. Business logic flaws and access control testing is only possible using human assistance. These should be turned into unit and integration tests.

## How to use this standard

One of the best ways to use the Application Security Verification Standard is to use it as a blueprint to create a Secure Coding Checklist specific to your application, platform or organization. Tailoring the ASVS to your use cases will increase the focus on the security requirements that are most important to your projects and environments.

### Level 1 - First steps, automated, or whole of portfolio view

An application achieves ASVS Level 1 if it adequately defends against application security vulnerabilities that are easy to discover, and included in the OWASP Top 10 and other similar checklists.

Level 1 is the bare minimum that all applications should strive for. It is also useful as a first step in a multi-phase effort or when applications do not store or handle sensitive data and therefore do not need the more rigorous controls of Level 2 or 3. Level 1 controls can be checked either automatically by tools or simply manually without access to source code. We consider Level 1 the minimum required for all applications.

Threats to the application will most likely be from attackers who are using simple and low effort techniques to identify easy-to-find and easy-to-exploit vulnerabilities. This is in contrast to a determined attacker who will spend focused energy to specifically target the application. If data processed by your application has high value, you would rarely want to stop at a Level 1 review.

### Level 2 - Most applications

An application achieves ASVS Level 2 (or Standard) if it adequately defends against most of the risks associated with software today.

Level 2 ensures that security controls are in place, effective, and used within the application. Level 2 is typically appropriate for applications that handle significant business-to-business transactions, including those that process healthcare information, implement business-critical or sensitive functions, or process other sensitive assets, or industries where integrity is a critical facet to protect their business, such as the game industry to thwart cheaters and game hacks.

Threats to Level 2 applications will typically be skilled and motivated attackers focusing on specific targets using tools and techniques that are highly practiced and effective at discovering and exploiting weaknesses within applications.

### Level 3 - High value, high assurance, or high safety

ASVS Level 3 is the highest level of verification within the ASVS. This level is typically reserved for applications that require significant levels of security verification, such as those that may be found within areas of military, health and safety, critical infrastructure, etc.

Organizations may require ASVS Level 3 for applications that perform critical functions, where failure could significantly impact the organization's operations, and even its survivability. Example guidance on the application of ASVS Level 3 is provided below. An application achieves ASVS Level 3 (or Advanced) if it adequately defends against advanced application security vulnerabilities and also demonstrates principles of good security design.

An application at ASVS Level 3 requires more in depth analysis of architecture, coding, and testing than all the other levels. A secure application is modularized in a meaningful way (to facilitate resiliency, scalability, and most of all, layers of security), and each module (separated by network connection and/or physical instance) takes care of its own security responsibilities (defense in depth), that need to be properly documented. Responsibilities include controls for ensuring confidentiality (e.g. encryption), integrity (e.g. transactions, input validation), availability (e.g. handling load gracefully), authentication (including between systems), authorization, and auditing (logging).

## How to Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>` where each element is a number, for example: `1.11.3`.
- The `<chapter>` value corresponds to the chapter from which the requirement comes, for example: all `1.#.#` requirements are from the `Architecture` chapter.
- The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.11.#` requirements are in the `Business Logic Architectural Requirements` section of the `Architecture` chapter.
- The `<requirement>` value identifies the specific requirement within the chapter and section, for example: `1.11.3` which as of version 4.0.2 of this standard is:

> Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.

The identifiers may change between versions of the standard therefore it is preferable that other documents, reports, or tools use the format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v4.0.2-1.11.3` would be understood to mean specifically the 3rd requirement in the 'Business Logic Architectural Requirements' section of the 'Architecture' chapter from version 4.0.2. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version portion is to be lower case.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. Obviously as the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ASVS requirement lists are made available in CSV, JSON, and other formats which may be useful for reference or programmatic use.

## Uses for the ASVS

The ASVS can be used to assess the security of an application and this is explored in more depth in the next chapter. However, we have identified a number of other potential uses for the ASVS.

### As Detailed Security Architecture Guidance

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. The Sherwood Applied Business Security Architecture (SABSA) is missing a great deal of information that is necessary to complete a thorough application security architecture review. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies.

### As a Specialized Secure Coding Checklist

Many organizations can benefit from adopting the ASVS, by choosing one of the three levels, or by forking ASVS and changing what is required for each application risk level in a domain-specific way. We encourage this type of forking as long as traceability is maintained so that if an app has passed requirement 4.1, this means the same thing for forked copies as the standard as it evolves.

Ideally, every organization should have their own forked ASVS, select their requirements tailor-fitted for them and their applications. So if the organization is not using GraphQL, Websockets, or SOAP web service on their applications, they should drop those sections from their forked ASVS. The forking process must start with looking at ASVS level 1 requirements as a baseline for the organization and then gradually move into ASVS level 2 or 3 based on their application's risk level. Organizations must use their forked ASVS as a secure coding checklist for secure application development, preferably with guidance from security engineers or security architects alike. In this way, organizations will have a unified and clear secure coding checklist applicable to all development teams.

### As a Guide for Automated Unit and Integration Tests

The ASVS is designed to be highly testable, with the sole exception of architectural and malicious code requirements. By building unit and integration tests that test for specific and relevant fuzz and abuse cases, the application becomes nearly self-verifying with each and every build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common default usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, and more.

### For Secure Development Training

ASVS can also be used to define characteristics of secure software. Many “secure coding” courses are simply ethical hacking courses with a light smear of coding tips. This may not necessarily help developers to write more secure code. Instead, secure development courses can use the ASVS with a strong focus on the proactive controls found in the ASVS, rather than the Top 10 negative things not to do.

### As a Driver for Agile Application Security

ASVS can be used in an agile development process as a framework to define specific tasks that need to be implemented by the team to have a secure product. One approach might be: Starting with Level 1, verify the specific application or system according to ASVS requirements for the specified level, find what controls are missing and raise specific tickets/tasks in the backlog. This helps with prioritization of specific tasks (or grooming), and makes security visible in the agile process. This can also be used to prioritize auditing and reviewing tasks in the organization, where a specific ASVS requirement can be a driver for review, refactor or auditing for a specific team member and visible as "debt" in the backlog that needs to be eventually done.

### As a Framework for Guiding the Procurement of Secure Software

ASVS is a great framework to help with secure software procurement or procurement of custom development services. The buyer can simply set a requirement that the software they wish to procure must be developed at ASVS level X, and request that the seller proves that the software satisfies ASVS level X. This works well when combined with the OWASP Secure Software Contract Annex

## Applying ASVS in Practice

Different threats have different motivations. Some industries have unique information and technology assets and domain specific regulatory compliance requirements.

Organizations are strongly encouraged to look deeply at their unique risk characteristics based on the nature of their business, and based upon that risk and business requirements determine the appropriate ASVS level.

We have heard from various people in community on how they use the standard in practice:

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

* OWASP Defectdojo has built in ASVS support https://www.defectdojo.org/
* A few weeks after the ASVS 4 release, RIPS added support for it: https://blog.ripstech.com/2019/rips-3.1-adds-teamcity-ldap-jsp-support/
