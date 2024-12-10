# Using the ASVS

The ASVS defines functional and non-functional security requirements for modern web applications and services, focusing on application content rather than secure development processes, which are covered in [OWASP SAMM](https://owaspsamm.org/).

The ASVS is useful for anyone aiming to develop and maintain secure applications, or evaluate the security of applications. This chapter covers key aspects of using the ASVS, including priority-based levels and various use cases for the standard

## Application Security Verification Levels

The Application Security Verification Standard defines three security verification levels, with each level increasing in depth and complexity. Each ASVS level contains a list of security requirements. Each of these requirements can also be mapped to security-specific features and capabilities that must be built into software by developers.

In version 4.0, we described the levels as L1 - "Mininum", L2 - "Standard", and L3 - "Advanced" with the implication that all applications processing sensitive data should be at least L2.

### Challenges with the previous approach

There have been a few challenges with this approach.

#### High barrier to entry

L1 in version 4.0 had over 100 requirements as did L2 with only a few requirements left in L3. This meant that a high level of effort required to achieve even L1 at which point the user is told that this is the "minimum" level and that to achieve a "standard" level of security, another 100 requirements are required. In our discussions for version 5.0, we felt like this was demoralizing and made it harder for applications to start adopting the ASVS.

#### The fallacy of testability

A primary motivator behind putting controls in L1 version 4.0 was whether they could be checked using "black box" style testing which was not entirely in line with the concept of L1 being the minimum security controls. On the one hand, we would hear from users that L1 was not sufficient for a secure application whilst on the other hand we would get complaints that ASVS was too difficult to test.

Additionally, testability is relative and in some cases misleading. Just because something is testable does not mean that it is testable in an automated or trivial way. Also, the most testable requirements are not necessary those that have the most important security impact or are the easiest to implement.

#### Not just about risk

We dislike the concept of prescriptive, risk based levels which mandate that a certain application has to be at a certain level. In our experience, the order of implementing security controls will depend on factors including both risk reduction and also effort to implement.

### Our approach for v5.0

For version 5.0, after much discussion within the Working Group, the consensus was that we wanted to stay with three levels. However, we wanted to significantly reduce the number of requirements in Level 1 to lower the barrier to entry, we wanted to change the criteria which are used to define the level which a requirement goes into, and in doing so reframe the definition of the levels.

### Level evaluation criteria

To achieve this, we have moved to a priority based evaluation of each requirement based on our combined experience implementing security requirements. In this approach, we evaluted each requirement using the following criteria.

#### Risk Reduction

To what extent does the requirement reduce security risk within the application? This takes into account the classic Confidentiality, Integrity, and Availability impact factors as well as considering whether this is a first line control or would be considered defense in depth.

In general, the requirements which bring the greatest risk reduction would be in Level 1 or Level 2 and requirements which are still valuable but are either defense in depth or relate to a more niche area or issue are in Level 3.

#### Effort to implement

Whilst the ASVS is named as a verification standard, there is nothing to verify unless the requirement has been implemented in the application. There are clearly some requirements which are far more complicated to implement and maintain than others and and we believe it is important that this is taken into account when deciding the relative priority of a requirement.

Whilst there will still be some harder to implement controls that provide a large enough risk reduction to be in Level 1, we expect that the more complex requirements will be in Level 2 or Level 3.

#### Low barrier to entry

From our experience of seeing the use (or non-use) of the ASVS in industry, the single greatest problem that we have identified is the double edged sword of Level 1 having a large number of requirements (~120) but at the same time being considered the "minimum" level that is not good enough for most applications. This seems to lead to organizations either giving up before they start or trying to implement a subset of the requirements without actually achieving Level 1, there reducing the sense of achievement and progress.

To this end, we were determined that Level 1 would have a maximum of around 60 of the highest priority requirements and others would get pushed into Level 2 or Level 3. To achieve this, we have had to make some hard decisions about what would make it into Level 1 and what would not but we would rather have a good Level 1 that is a achievable than a perfect Level 1 that is not.

#### Better level balance

In version 4.0, Levels 1 and 2 both had around 120 requirements and Level 3 had around 30. We have tried to balance the requirements more evenly across the levels in version 5.0, trying to distribute Level 2 and Level 3 requirements more evenly. Again, the aim is to make Level 2 more achievable and realistic whilst leaving Level 3 for applications that want to demonstrate the highest level of security.

### Definition of the Levels

By moving to a priority based evaluation of each requirement, from our perspective the levels become more of a reflection of the application security maturity of the organization and the application. Rather than the ASVS prescriptively defining what level we think an application should be at, an organization should decide what level they feel they should be at, depending on the sensitivity of the application and of course the expectations of the application's users.

For example, an early stage startup which is only collecting limited sensitive data may decide that Level 1 is sufficient but a bank may have difficulty justifying anything less than Level 3 to its customers for its online banking application.

In 5.0, we have not committed to ensuring that Level 1 is completely penetration testable using humans, although the lower number of requirements should make it easier to verify.

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
