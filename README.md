# OWASP Application Security Verification Standard

<img src="https://owasp.org/www-project-application-security-verification-standard/assets/images/OWASP_ASVS_Linkedin_Banner-01.jpg" width="700px">

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg

🎉🎉🎉 **Welcome to Version 5.0 of the ASVS!** 🎉🎉🎉 

**Released LIVE on stage at Global AppSec EU Barcelona 2025!**

## Introduction

The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to provide an open application security standard for web apps and web services of all types.

Originally launched in 2008 through a global community collaboration, the ASVS defines a comprehensive set of security requirements for designing, developing, and testing modern web applications and services.

Following the release of ASVS 4.0 in 2019 and its minor update (v4.0.3) in 2021, Version 5.0 represents a significant milestone—modernized to reflect the latest advances in software security.

We gratefully recognize the organizations who have supported the project either through significant time provision or financially on our "[Supporters](SUPPORTERS.md)" page!

**Please [log issues](https://github.com/OWASP/ASVS/issues) if you find any bugs or if you have ideas. We may subsequently ask you to [open a pull request](https://github.com/OWASP/ASVS/pulls) based on the discussion in the issue. We are also actively looking for [translations of the 5.n branch](CONTRIBUTING.md#translations).**

## Project Leaders and Working Group

The project is led by the four project leaders [Daniel Cuthbert](https://github.com/danielcuthbert), [Jim Manico](https://github.com/jmanico), [Josh Grossman](https://github.com/tghosth), and [Elar Lang](https://github.com/elarlang).

They are supported by the ASVS Working Group which consists of [Shanni Prutchi](https://github.com/EnigmaRosa), [Ralph Andalis](https://github.com/csfreak92), [Meghan Jacquot](https://github.com/meghanjacquot), [Iman Sharafaldin](https://github.com/ImanSharaf), [Ryan Armstrong](https://github.com/ryarmst), [Gabriel Corona](https://github.com/randomstuff), [Tobias Ahnoff](https://github.com/TobiasAhnoff), and [Eden Yardeni](https://github.com/cronchie). 

## Latest Stable Version - 5.0.0

The latest stable version is version 5.0.0 (dated May 2025), which can be found:

* [OWASP Application Security Verification Standard 5.0.0 English (PDF)](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf)
* [OWASP Application Security Verification Standard 5.0.0 English (Word)](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.docx)
* [OWASP Application Security Verification Standard 5.0.0 English (CSV)](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv)
* [OWASP Application Security Verification Standard 5.0.0 (GitHub Branch)](https://github.com/OWASP/ASVS/tree/v5.0.0)

The master branch of this repository will always be the "bleeding edge version" which might have in-progress changes or other edits open. The next release target will be a patch release, version **5.0.1**. For details on the ASVS release strategy, see [the release strategy section of CONTRIBUTING.md](CONTRIBUTING.md#release-strategy).

### Translations

The OWASP Community effort with regards to translations is a best effort. Whilst we do our utmost to ensure the content is valid, from a structural perspective, there is only so much we can do to ensure the translations are correct. We rely on you, the community, to help make the ASVS as usable as possible to all around the globe, and translating the main branch into your language is important to the project.

If you think you can help with translations, or indeed ensuring the current list of translations below are correct, we'd love for you to join the community and make the ASVS amazing for all. For more information on translating the ASVS see the [translations section of CONTRIBUTING.md](CONTRIBUTING.md#translations).

There are currently no translations for version v5.0.0. Historic translations of the v4.x versions can be found in the [TRANSLATIONS.md file](4.0/TRANSLATIONS.md) in the 4.0 folder.

## How To Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>`, where each element is a number. For example, `1.11.3`.

* The `<chapter>` value corresponds to the chapter from which the requirement comes; for example, all `1.#.#` requirements are from the 'Encoding and Sanitization' chapter.
* The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.2.#` requirements are in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter.
* The `<requirement>` value identifies the specific requirement within the chapter and section, for example, `1.2.5` which as of version 5.0.0 of this standard is:

> Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.

Since the identifiers may change between versions of the standard, it is preferable for other documents, reports, or tools to use the following format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v5.0.0-1.2.5` would be understood to mean specifically the 5th requirement in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter from version 5.0.0. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version number in the format should always be lowercase.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. As the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

## License

The entire project content is under the **[Creative Commons Attribution-Share Alike v4.0](https://creativecommons.org/licenses/by-sa/4.0/)** license.
