# Contributing

<img src="https://owasp.org/www-project-application-security-verification-standard/assets/images/OWASP_ASVS_Linkedin_Banner-01.jpg" width="700px">

**This document applies during 2024 and may change at a future date.**

## Introduction

### What is [OWASP](https://owasp.org/)?

The Open Worldwide Application Security Project (OWASP) is a nonprofit organization that works to improve the security of software. It has many programs to work towards this goal. One of those programs is the ASVS.

### What is the [ASVS](https://owasp.org/www-project-application-security-verification-standard/)?

The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard.

### What is the Current Status of ASVS development?

The ASVS project is planning to release a 5.0 version during 2024 which will be a significant modification, similar to the scale of changes which happened during 4.0.

We will try, on a best efforts basis, to address issues and push changes to the "bleeding edge" master branch within the 5.0 folder **without altering current numbering** and using tagging ([see below](CONTRIBUTING.md#use-tags-to-describe-the-change)) to make changes clearer. This is in order to make it easier to use this branch on an ongoing basis. 

We will no longer be accepting changes to the 4.0 folder which is now fixed at the 4.0.3 release.

Please also focus attention on the requirements themselves and **not** on the surrounding text or on the introductory chapters (files 0x01-0x04). This is because the text might have become outdated where requirements have changed and also because our goal is to significantly cut down this text in version 5.0.

## How can I help?

Reading through the most recent version of ASVS is a great place to start.

After familiarizing yourself with the current version, the next area to focus on is the Issues section. 

There are two key types right now:

* [![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aowasp%2Fasvs%20is%3Aopen%20is%3Aissue%20label%3A%22Community%20wanted%22&style=flat&label=Community%20Wanted&labelColor=%23BFD4F2&color=grey)](https://github.com/OWASP/ASVS/issues?q=is%3Aopen+is%3Aissue+label%3A%22Community+wanted%22) - These are issues where we would really benefit from more eyes on a particular issue.
* [![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aowasp%2Fasvs%20is%3Aopen%20is%3Aissue%20label%3A%22Community%20needed%22&style=flat&label=Community%20Needed&labelColor=%23fbca04&color=grey)](https://github.com/OWASP/ASVS/issues?q=is%3Aopen+is%3Aissue+label%3A%22Community+needed%22) - These are issues where the relevant items will not get progressed without community input.


Please log ideas, issues or questions here: https://github.com/OWASP/ASVS/issues. It’s helpful to share if you have any ideas or if you find any bugs. We may subsequently ask you to open a pull request, https://github.com/OWASP/ASVS/pulls, based on the discussion in the issue. 

## Additional Details for Helping

### Before you open a Pull Request

Please do not open a pull request without first opening an associated issue. Please do not open an issue until you have used the search functionality to ensure that the issue has not previously been discussed and that there are no currently open issues relating to it. For example, [this link](https://github.com/OWASP/ASVS/issues?q=is%3Aissue+bcrypt) searches for issues (open and closed) related to bcrypt.

If you are comfortable that it has not been previously discussed, you can open an issue. Please try and include the ASVS text you are talking about in the issue to save having to jump back and forth and please carry out all discussion in the associated issue and not in a PR discussion.

### How to make changes to the bleeding edge during this period

Note that changes should always be made only in the raw .md files and not in the CSV, JSON, XLSX, PDF, DOCX files, etc.

To help those who are using the "bleeding edge" version for their tests and in order to be able to track changes made during this period, we have prepared a set of labels to be used when making changes to the "bleeding edge" version during this time. The current bleeding edge working directory can be found here <https://github.com/OWASP/ASVS/tree/master/5.0/en>.


### Standard for changes

#### Keep all current numbers

* New requirements must be placed at the end of the relevant section
* Deleted requirements must keep "placeholder" to avoid some other requirements to be added/moved to that number, examples:

```
| **1.2.1** | [MOVED TO 1.14.7] | | | | |
```

```
| **5.5.1** | [DELETED] | | | | |
```

#### Use tags to describe the change

Project leads will check and validate labels for changes. Please ask for a recommendation regarding the proper label in the issue tracker if you have any questions.

These tags should all be relative to how the requirement appeared in the latest release (v4.0.3) and will be used in a mapping file between releases.

The following tags should be added to any modified requirement as appropriate.

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
* `[DELETED, DUPLICATE OF x.y.z]` - Placeholder to keep number, requirement has been deleted because of clear duplicate to referenced requirement (referenced requirement do not have changes because of that).
* `[DELETED, NOT IN SCOPE]` - Placeholder to keep number, requirement has been decided to be out of ASVS scope.
* `[DELETED, INCORRECT]` - Placeholder to keep number, requirement was invalid or provided inadvisable advice.
* `[DELETED, NOT PRACTICAL]` - Placeholder to keep number, requirement was not practical (enough) to implement in reality.
* `[DELETED, INSUFFICIENT IMPACT]` - Placeholder to keep number, requirement was valid and in scope but provided insufficient benefit to be worthwhile.
* `[SPLIT TO x.y.z, i.j.f]` - Placeholder to keep number, requirement has been split into 2 or more requirements to other categories.
* `[LEVEL L1 > L2]` - Requirement level has changed. Level change label may exist also for `[MODIFIED]`, `[MOVED FROM]` and `[SPLIT FROM]`

`SPLIT TO`, `MOVED TO`, `MERGED TO` labels must have matching labels with `SPLIT FROM`, `MOVED FROM`, `MERGED FROM`.

CWE and/or NIST mapping changes do not require labels.

Tags must be placed before verification description, example:

```
| **12.4.2** | [MODIFIED] Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload and serving of known malicious content. | ✓ | ✓ | ✓ | 509 |
```

### Translations

We are also actively looking for translations of the 4.n branch!

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
