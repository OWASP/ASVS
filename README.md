# OWASP Application Security Verification Standard
![LicenseBadge](https://img.shields.io/badge/license-C_C-blue.svg)
 </br>[![LICENSE](https://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/) 
## Introduction

The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to provide an open application security standard for web apps and web services of all types.

The standard provides a basis for designing, building, and testing technical application security controls, including architectural concerns, secure development lifecycle, threat modelling, agile security including continuous integration / deployment, serverless, and configuration concerns.

**Please [log issues](https://github.com/OWASP/ASVS/issues) if you find any bugs or if you have ideas. We may subsequently ask you to [open a pull request](https://github.com/OWASP/ASVS/pulls) based on the discussion in the issue. We are also actively looking for translations of the 4.n branch.**

## Latest Stable Version - 4.0.2

The latest stable version is version 4.0.2 (dated October 2020), which can be found:
* [OWASP Application Security Verification Standard 4.0.2 English (PDF)](https://github.com/OWASP/ASVS/raw/v4.0.2/4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0.2-en.pdf)
* [OWASP Application Security Verification Standard 4.0.2 English (Word)](https://github.com/OWASP/ASVS/raw/v4.0.2/4.0/docs_en/OWASP%20Application%20Security%20Verification%20Standard%204.0.2-en.docx)
* [OWASP Application Security Verification Standard 4.0.2 English (CSV)](https://github.com/OWASP/ASVS/raw/v4.0.2/4.0/docs_en/OWASP%20Application%20Security%20Verification%20Standard%204.0.2-en.csv)
* [OWASP Application Security Verification Standard 4.0.2 (GitHub Tag)](https://github.com/OWASP/ASVS/tree/v4.0.2)

The master branch of this repository will always be the "bleeding edge version" which might have in-progress changes or other edits open. The next release target will be version **4.1**.

For information on changes between 4.0.1 and 4.0.2 of the standard, see [this wiki page](https://github.com/OWASP/ASVS/wiki/What-is-new-in-version-4.0.2) and for a full diff, see [this pull request](https://github.com/OWASP/ASVS/pull/780/files?file-filters%5B%5D=.md&file-filters%5B%5D=.py&file-filters%5B%5D=.sh&file-filters%5B%5D=.yml&file-filters%5B%5D=No+extension).

### Translations

* [OWASP Application Security Verification Standard 4.0.1 Persian (PDF)](4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-fa.pdf) (Thanks to [SajjadPourali](https://github.com/SajjadPourali))
* [OWASP Application Security Verification Standard 4.0.2 German (PDF)](4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0.2-de.pdf) (Thanks to Jörg Brünner) 
* [OWASP Application Security Verification Standard 4.0 Japanese (PDF)](4.0/OWASP-Application-Security-Verification-Standard-4.0-ja.pdf) (Thanks to Software ISAC Japan / [Riotaro OKADA](https://github.com/okdt))
* [OWASP Application Security Verification Standard 4.0 Turkish (PDF)](4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-tr.pdf) (Thanks to [Fatih ERSINADIM](https://github.com/fatihersinadim)) 

## Standard Objectives

The requirements were developed with the following objectives in mind:

* Help organizations adopt or adapt a high quality secure coding standard
* Help architects and developers build secure software by designing and building security in, and verifying that they are in place and effective by the use of unit and integration tests that implement ASVS tests
* Help deploy secure software via the use of repeatable, secured builds
* Help security reviewers use a comprehensive, consistent, high quality standard for hybrid code reviews, secure code reviews, peer code reviews, retrospectives, and work with developers to build security unit and integration tests. It is even possible to use this standard for penetration testing at Level 1
* Assist tool vendors by ensuring there is an easily generatable machine readable version, with CWE mappings
* Assist organizations to benchmark application security tools by the percentage of coverage of the ASVS for dynamic, interactive, and static analysis tools
* Minimize overlapping and competing requirements from other standards, by either aligning strongly with them (NIST 800-63), or being strict supersets (OWASP Top 10 2017, PCI DSS 3.2.1), which will help reduce compliance costs, effort, and time wasted in accepting unnecessary differences as risks.

ASVS requirement lists are made available in CSV, JSON, and other formats which may be useful for reference or programmatic use.

## How To Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>` where each element is a number, for example: `1.11.3`.
- The `<chapter>` value corresponds to the chapter from which the requirement comes, for example: all `1.#.#` requirements are from the `Architecture` chapter.
- The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.11.#` requirements are in the `Business Logic Architectural Requirements` section of the `Architecture` chapter.
- The `<requirement>` value identifies the specific requirement within the chapter and section, for example: `1.11.3` which as of version 4.0.2 of this standard is:

> Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.

The identifiers may change between versions of the standard therefore it is preferable that other documents, reports, or tools use the format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v4.0.2-1.11.3` would be understood to mean specifically the 3rd requirement in the 'Business Logic Architectural Requirements' section of the 'Architecture' chapter from version 4.0.2. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version portion is to be lower case.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. Obviously as the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

## License

The entire project content is under the **[Creative Commons v3.0](https://creativecommons.org/licenses/by-sa/3.0/)** license.
