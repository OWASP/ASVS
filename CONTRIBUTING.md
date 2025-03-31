# Contributing

<img src="https://owasp.org/www-project-application-security-verification-standard/assets/images/OWASP_ASVS_Linkedin_Banner-01.jpg" width="700px">

**This document has been updated for the version 5.0 release candidate stage in 2025 and may change at a future date.**

## Introduction

### What is [OWASP](https://owasp.org/)?

The Open Worldwide Application Security Project (OWASP) is a nonprofit organization that works to improve the security of software. It has many programs to work towards this goal. One of those programs is the ASVS.

### What is the [ASVS](https://owasp.org/www-project-application-security-verification-standard/)?

The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard.

### What is the Current Status of ASVS development?

🎉🎉🎉 **We are now at the RC1 stage of ASVS version 5.0!** 🎉🎉🎉

The ASVS project will release a 5.0 version during May 2025 which is a complete revamp compared to the previous version 4.0.3.

We are waiting for your feedback on a release candidate version of 5.0! You can see this version on the master branch within the 5.0 folder. This branch will continue to be updated during the review process so we recommend always working from the latest version

We will no longer be accepting changes to the 4.0 folder which is now fixed at the 4.0.3 release.

## How can I help?

Reading through the release candidate version of ASVS is a great place to start.

A few questions to ask yourself as you review the document:

* If I was a developer or a security tester, would this requirement understandable to me?
* Can I think of a way of improving front / chapter / section text to add clarity without adding unnecessary content.

Please first log ideas, issues or questions here: https://github.com/OWASP/ASVS/issues. It’s helpful to share if you have any ideas or if you find any bugs or typos (but see the extra guidance below).

We may subsequently ask you to open a pull request, https://github.com/OWASP/ASVS/pulls, based on the discussion in the issue. 

After familiarizing yourself with the current version and if you don't have additional questions or feedback, the next area to focus on is the "Issues" section. 

The issues to focus on for RC1 are listed here:

- ![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AOWASP%2FASVS%20label%3A%22_5.0%20-%20rc1%22%20state%3Aopen&label=_5.0%20-%20rc1&labelColor=%2399F2D1&color=grey&link=https%3A%2F%2Fgithub.com%2FOWASP%2FASVS%2Fissues%3Fq%3Dis%253Aissue%2520state%253Aopen%2520label%253A%2522_5.0%2520-%2520rc1%2522)

## Additional Details for Helping

### Before you open a Pull Request

Please do not open a pull request without first opening an associated issue. Please do not open an issue until you have used the search functionality to ensure that the issue has not previously been discussed and that there are no currently open issues relating to it. For example, [this link](https://github.com/OWASP/ASVS/issues?q=is%3Aissue+bcrypt) searches for issues (open and closed) related to bcrypt.

Note that since there was a major renumbering recently, a lot of the requirement numbers in the issues may be different. You should also therefore search in the issues for the requirements based on two other sources of requirment numbers:

1) Each requirement has a column at the end called "#v5.0.be". This contains the number before the numbering.
2) If you are looking for how a requirement was numbered in v4.0.3 (which may also be used in the issues), there is a [mapping page](https://asvs.dev/mapping_v5.0.0_to_v4.0.3.html) which maps between the current number and the number from v4.0.3.
    -  There are also other mappings in the [`5.0/mappings/`](5.0/mappings/) folder but these may not be kept up to date.

If you are comfortable that your query has  has not been previously discussed, you can open an issue. Please try and include the ASVS text you are talking about in the issue (or at least the value of the "#v5.0.be" column) to save having to jump back and forth and please carry out all discussion in the associated issue and not in a PR discussion.

### How to suggest changes to the release candidate during this period

Note that review and changes should always be made based on the raw .md files. The other output formats have not yet been updated.

To help those who are using the "bleeding edge" version for their tests and in order to be able to track changes made during this period, we have prepared a set of labels to be used when making changes to the "bleeding edge" version during this time. The current bleeding edge working directory can be found here <https://github.com/OWASP/ASVS/tree/master/5.0/en>.

### Tags in the mapping files

The mappings in the [`5.0/mappings/`](5.0/mappings/) folder use tags to explain how requirements changed between different versions. This will be useful if you are trying to trace the rationale of a particular requirement.

These mappings use tags to explain how the requirements have changed between the versions.

* `[ADDED]` - New requirement (should only be added at the end of a sub-section.).
* `[MODIFIED]` - Requirement description has been modified.
* `[GRAMMAR]` - Requirement description has been corrected from a language or grammar perspective, but the wording or meaning of the description is not modified.
* `[MOVED TO x.y.z]` - Placeholder to keep number, requirement has been moved to another category.
* `[MOVED FROM a.b.c]` - Requirement has been moved to a different sub-section but **not** modified. (should only be added at the end of a sub-section.).
* `[MODIFIED, MOVED FROM a.b.c]` - Requirement description has been modified **and** requirement has been moved to a different sub-section.
* `[MODIFIED, SPLIT TO x.y.z]` - Requirement description has been modified **and** part of the requirement is split into a new separate requirement.
* `[ADDED, SPLIT FROM a.b.c]` - New requirement which was previously part of another requirement.
* `[DELETED]` - Placeholder to keep number, requirement has been deleted.
* `[DELETED, MERGED TO x.y.z]` - Placeholder to keep number, requirement has been merged into another requirement.
* `[DELETED, COVERED BY x.y.z]` - Placeholder to keep number, requirement has been deleted because of clear duplicate to referenced requirement (referenced requirement do not have changes because of that).
* `[COVERS a.b.c]` - new requirement that covers old requirement marked by `COVERED BY x.y.z`
* `[DELETED, NOT IN SCOPE]` - Placeholder to keep number, requirement has been decided to be out of ASVS scope.
* `[DELETED, INCORRECT]` - Placeholder to keep number, requirement was invalid or provided inadvisable advice.
* `[DELETED, NOT PRACTICAL]` - Placeholder to keep number, requirement was not practical (enough) to implement in reality.
* `[DELETED, INSUFFICIENT IMPACT]` - Placeholder to keep number, requirement was valid and in scope but provided insufficient benefit to be worthwhile.
* `[SPLIT TO x.y.z, i.j.f]` - Placeholder to keep number, requirement has been split into 2 or more requirements to other categories.
* `[LEVEL L1 > L2]` - Requirement level has changed. Level change label may exist also for `[MODIFIED]`, `[MOVED FROM]` and `[SPLIT FROM]`

`SPLIT TO`, `MOVED TO`, `MERGED TO` labels must have matching labels with `SPLIT FROM`, `MOVED FROM`, `MERGED FROM`.

### Translations

We are no longer also actively looking for translations of the 4.n branch but get ready for the final version of 5.0 which can then be translated!

<!--

NOTE: This content will be brought back in, related to 5.0 when 5.0 is ready

If you are interested in creating a translation, here are some pointers for how you can help us:

* Please first of all search the repository to see if there is already a translation for your proposed language. We currently have completed or in-progress translations in the following languages (but please search anyway in case this list is superseded!):
    * In-progress
        * None
    * v4.0.3
        * Spanish
        * Simplified Chinese
        * Arabic
        * Russian
        * French
        * German
        * Portuguese
        * Italian
    * v4.0.2
        * German
        * Russian
    * v4.0.1
        * Persian
        * Turkish
        * Japanese
* If the language you are interested in appears, it would be great if you could reach out to the translator to see if you can help them.
* Often there is work to do in creating markdown files or updating the translation to keep it up to date with latest changes.
* We would request that you base your translation on the 4.0/en folder in the master branch as this is now static at the 4.0.3 version.
* In order to start a translation, please start by forking the ASVS repository.
    * If you are updating an existing translation which has markdown (just French as of December 2021), you can make modifications to the files in the existing folder based on language code (just /fr as at December 2021).
    * If you are starting a new markdown translation, take a copy of the /en folder and rename it to the 2 character language code which will be used for the translation.
* When you have completed the translation, please open a Pull Request against the master ASVS branch and one of the leaders will look at integrating it.
* The leader will also use the relevant scripts to create the documents from the raw markdown (or you can if you want to save us some trouble).
* Finally, the leader will back port the translation into the branch containing the ASVS version which was targeted (at this point, presumably v4.0.3).

Thank you for your help!!
->