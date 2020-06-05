# OWASP Application Security Verification Standard
![LicenseBadge](https://img.shields.io/badge/license-C_C-blue.svg)
 </br>[![LICENSE](https://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/) 
## Introduction

The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to provide an open application security standard for web apps and web services of all types.

The standard provides a basis for designing, building, and testing technical application security controls, including architectural concerns, secure development lifecycle, threat modelling, agile security including continuous integration / deployment, serverless, and configuration concerns.

**Please [log issues](https://github.com/OWASP/ASVS/issues) if you find any bugs or if you have ideas. We may subsequently ask you to [open a pull request](https://github.com/OWASP/ASVS/pulls) based on the discussion in the issue. We are also actively looking for translations of the 4.n branch.**

## Standard Objectives

The requirements were developed with the following objectives in mind:

* Help organizations adopt or adapt a high quality secure coding standard
* Help architects and developers build secure software by designing and building security in, and verifying that they are in place and effective by the use of unit and integration tests that implement ASVS tests
* Help deploy secure software via the use of repeatable, secured builds
* Help security reviewers use a comprehensive, consistent, high quality standard for hybrid code reviews, secure code reviews, peer code reviews, retrospectives, and work with developers to build security unit and integration tests. It is even possible to use this standard for penetration testing at Level 1
* Assist tool vendors by ensuring there is an easily generatable machine readable version, with CWE mappings
* Assist organizations to benchmark application security tools by the percentage of coverage of the ASVS for dynamic, interactive, and static analysis tools
* Minimize overlapping and competing requirements from other standards, by either aligning strongly with them (NIST 800-63), or being strict supersets (OWASP Top 10 2017, PCI DSS 3.2.1), which will help reduce compliance costs, effort, and time wasted in accepting unnecessary differences as risks.

### How To Reference ASVS Controls

Each control has an identifier in the format `<category>.<sub-category>.<control>` where each element is a number, ex: `1.11.3`. 
- The `<category>` value corresponds to a particular category of control, ex: all `1.#.#` controls are `Architecture` related.
- The `<sub-category>` value corresponds to a particular sub-category of control, ex: all `1.11.#` controls are `Business Logic Architectural Requirements` related.
- The `<control>` value identifies a specific control within the category and sub-category, ex: `1.11.3` which as of version 4.0.1 of this standard is:

> Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.

The identifiers may change between versions of the standard therefore it is preferable that other documents, reports, or tools use the format: `v<version>-<category>.<sub-category>.<control>`, where: 'version' is the version tag with punctuation removed. For example: `v401-1.11.3` would be understood to mean specifically the 3rd Architecture Business Logic control from version 4.0.1. (This could be summarized as `v<version>-<control_identifier>`.)

If identifiers are used without including the `<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. Obviously as the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

## Latest Released Version - 4.0.1

The latest released version is version 4.0.1 (dated 2 March 2019), which can be found:
* [OWASP Application Security Verification Standard 4.0.1 English (PDF)](https://github.com/OWASP/ASVS/raw/master/4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-en.pdf)
* [OWASP Application Security Verification Standard 4.0.1 English (Word)](https://github.com/OWASP/ASVS/raw/master/4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-en.docx)
* [OWASP Application Security Verification Standard 4.0.1 English (CSV)](https://github.com/OWASP/ASVS/raw/master/4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-en.csv)
* [OWASP Application Security Verification Standard 4.0.1 (GitHub Tag)](https://github.com/OWASP/ASVS/tree/v4.0.1)

The master branch of this repository will always be the "bleeding edge version" which might have in-progress changes or other edits open. The next release target will be version **4.1**.

### Translations

Translation into Persian:
* [OWASP Application Security Verification Standard 4.0.1 Persian (PDF)](https://github.com/OWASP/ASVS/raw/master/4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-fa.pdf) (Thanks to [SajjadPourali](https://github.com/SajjadPourali))

## License

The entire project content is under the **[Creative Commons v3.0](https://creativecommons.org/licenses/by-sa/3.0/)** license.
