# https://asvs.dev/v5.0.draft/0x01-Frontispiece/

> The Application Security Verification Standard is a list of application security requirements or tests that can be used by architects, developers, testers, security professionals, tool vendors, and consumers to define, build, test and verify secure applications.

* [x] remove "or tests"?
* the main focus is security verification from the end-product - the main audience is security professionals and testers
  * **JG**: I disagree with this, all the way through we are balancing two key perspectives, building and checking. I know what the project name says but in practice I don't want to break that balance by the promoting the dev side as just being in order to test.
* to achieve that - it must be taken into account by architects, analysts, developers
* tool vendors - in what role?
  * **JG**: Use as a guide for structuring security tests in a tool.
* "to define, build, test and verify secure applications."
  * **JG**: What is the problem here?

# https://asvs.dev/v5.0.draft/0x02-Preface/

Outdated.

# https://asvs.dev/v5.0.draft/0x03-Using-ASVS/

In general

  * feels a bit over-structured
  * whatever describes changes compared to v4, belongs to specific chapter for that: "Guidance for users of version 4.0"

> The ASVS defines functional and non-functional security requirements for modern web applications and services, focusing on aspects that are in the control of the application developers.

It actually does not define directly functional and non-functional security requirements. "Functional requirements" or "non-functional requirements" are specific terms and most likely requirements in ASVS do not meet the definition for those.

The message should be "Requirements in ASVS creates the need to have related functional or non-functional requirements to satisfy the security needs."

---

> The Application Security Verification Standard defines three security verification levels, with each level increasing in depth and complexity. Each ASVS level indicates the security requirements that are required to achieve that level (with the others remaining as recommendations). The general aim is that organizations will start with L1 and then move up the levels from there.

"L1" in use, but the meaning is not yet defined in the document.

---

> The approach to level definition for version 5.0, was decided after much discussion within the Working Group based on feedback from ASVS users and the considerations above.

> Whilst, the consensus was to stay with three levels, the number of requirements in Level 1 has been significantly reduced to lower the barrier to entry. The criteria which are used to define the level which a requirement goes into have been changed and this therefore reframes the definition of the levels.

I still think this is more a blog-post kind of content or too much "finding excuses" for the changes, instead of just defining, what is the logic behind the level structure. In one year from the release, no one care what was the reason for changes from v4 and it becomes just filler/noise.

---

> From feedback on the use (or non-use) of the ASVS in industry, the single greatest problem that has been identified is the double-edged sword of Level 1 having a large number of requirements (~120) but at the same time being considered the "minimum" level that is not good enough for most applications.

It requires reference to v4. At the moment it is not clear what version it describes and may feel like it is addressing v5.

> To this end, it was decided that Level 1 would have a maximum of around 60 of the highest priority requirements and others would get pushed into Level 2 or Level 3. To achieve this, some hard decisions were made about what would make it into Level 1 and what would not. The goal was to have a good Level 1 that is achievable instead of a perfect Level 1 that is not.

"it was decided that Level 1 would have a maximum of around 60" - if to just watch this as a separate piece of information it rises a question "why is that? why 60 and not 30 or 90?" This phrase should be removed and just focus on the definition of Level 1 criteria.

---

> Better level balance

I think this section is unnecessary.

> Definition of the Levels

Again, description why some changes were made becomes a noise in near future.

> Level 1 requirements

> These will generally be critical or basic

"These will generally be ..." > "These are generally ..."?

> "are either relatively straightforward to implement"

I think it is not valid. For example, requirement for an HttpOnly flag is easy to implement, but it is level 2 because it is 2nd layer of defense.

My definition for Level 1 is - "it is a first layer of defense, in other words - if this is the one and only security problem in the application, it is usable for attackers (without any other pre-conditions)"

> Level 2 requirements

> "They will generally still be a first layer of defense."

This is confusing and in conflict with definition of Level 1.

> Level 3 requirements

> These requirements will generally relate to attacks which are a lot more niche or only relevant in certain circumstances. Requirements in this section may also be defense in depth mechanisms or other useful but hard to implement controls.

For better focus and priority, 2nd sentence should be before the current 1st one.


> As a Guide for Automated Unit and Integration Tests
> "The ASVS is designed to be highly testable"

Maybe a bit too bold statement. Entire section feels outdated and questionable, is it in the scope.


# https://asvs.dev/v5.0.draft/0x04-Assessment_and_Certification/


> Guidance for Certifying Organizations

I really don't like the word "Certifying" here, as the section before just kind of directs people to not use this.

By content entire section duplicates the content below ("How to Verify ASVS Compliance")

---

> The Application Security Verification Standard (ASVS) requires open access to resources, such as architects, developers, documentation, source code, and authenticated test systems, especially for L2 and L3 verifications.

The message should be - "to be able to verify security, many requirements from ASVS require open access to resources. "

> such as architects, developers,

???

> However, certifying reports should include scope, summaries of passed and failed tests, and guidance on resolving issues. Some requirements may be non-applicable (e.g., session management in stateless APIs), and this must be noted in the report.

"list of passed tests" is seriously naive way of thinking. A security test-report can only say, that certain vulnerabilities were not found during this scope focus/priority, during that testing time-window, but can rarely say "this problem does not exists there".

---

> Some requirements may be non-applicable (e.g., session management in stateless APIs), and this must be noted in the report.

Worth a separate line to say, that most likely the testing scope must be defined based on the functionality. The scoping should also be "white-list" to describe, what was in the scope and not a "black-list" to describe, what was not in the scope.

---

If to keep this situation, it must require also "reaching to the issue bust be repeatable or risks analyzed based on code review"

---

> The ASVS is deliberately not presciptive about exactly how to verify compliance.

maybe to add "on the testing guide level".

---

> After version 5.0 is released, we would like to prepare a testing guide

really? I prefer to go without this statement/promise.

---

About the automation. It is worth to describe a warning about naive automation - for example, investigating the HTTP response from the landing page and making analysis for the HTTP response header fields based on that is not clearly enough. Requests to different "paths" on for the same application may respond from different end-points using different configurations.

> Automated security testing tools such as DAST and SAST tools

Acronyms must be written out on the first usage.

---

> We strongly encourage including replacing penetration tests with documentation or source code-led (hybrid) penetration testing, with full access to developers and documentation throughout the development process, and this will be necessary in order to verify many of the ASVS requirements.

developers?

# https://asvs.dev/v5.0.draft/0x05-For-Users-Of-4.0/

todo: scope changes/clarification.

# https://asvs.dev/v5.0.draft/0x10-V1-Architecture/#control-objective

should we move some references to recommendations section? or we just delete them.

# https://asvs.dev/v5.0.draft/0x98-Appendix-W_LLM_Security/

Whatever we cover there, it will be outdated really fast.

Requires also Level column and format change.
