# Contributing

<img src="https://owasp.org/www-project-application-security-verification-standard/assets/images/OWASP_ASVS_Linkedin_Banner-01.jpg" width="700px">

**Last Update:** This document has been updated as of the v5.0.0 release in May 2025.

## Introduction

### What is [OWASP](https://owasp.org/)?

The Open Worldwide Application Security Project (OWASP) is a nonprofit organization that works to improve the security of software. It has many programs to work towards this goal. One of those programs is the ASVS.

### What is the [ASVS](https://owasp.org/www-project-application-security-verification-standard/)?

The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard.

### What is the Current Status of ASVS development?

The ASVS project released v5.0.0 during May 2025 which was a complete revamp compared to the previous version 4.0.3.

You can see the static version of this release on the v5.0.0 branch within the 5.0 folder. The master branch continues to be the "bleeding edge" and will contain any incremental changes made following the v5.0.0 release.

We will no longer be accepting changes to the 4.0 folder which is now fixed at the 4.0.3 release.

### Release strategy

ASVS releases follow the pattern "Major.Minor.Patch" and the numbers provide information on what has changed within the release. In a major release, the first number will change, in a minor release, the second number will change, and in a patch release, the third number will change.

* Major release - Full reorganization, almost everything may have changed, including requirement numbers and chapter and section structure. Reevaluation for compliance will be necessary (for example, 4.0.3 -> 5.0.0).
* Minor release - Requirements may be added, removed, split, or merged but overall numbering and the section structure will stay the same with no additions or removals. Reevaluation for compliance will be necessary, but should be easier (for example, 5.0.0 -> 5.1.0). The restrictions mean that requirements within a sections may not be in ascending level order. Levels may be increased or decreased.
* Patch release - Requirements may be removed (for example, if they are duplicates or outdated) or made less stringent, but an application that complied with the previous release will comply with the patch release as well (for example, 5.0.0 -> 5.0.1). A level number may be increased but not decreased.

The above specifically relates to the requirements in the ASVS. Changes to surrounding text and other content such as the appendices will not be considered to be a breaking change.

### Change control

In order to make it easier to track changes made on the bleeding edge version of ASVS and prepare new releases, we will follow the following conventions.

We will make changes on the bleeding edge branch which would be acceptable for minor and patch releases however we will add tags which make clear whether the type of change is breaking or not for a patch. We will not currently make changes that would not be acceptable for a minor release. This basically means no new sections and not requirement moving.

Tags will start with either:

* `M` - The change is acceptable for a major release
* `I` - The change is acceptable for a minor release
* `P` - The change is acceptable for a patch release

The following tags will be used, their meaning should be should be clear and they will be added to the start of the requirement description.

* Patch tags:
  * `[P:WEAKENED]`
  * `[P:DELETED]`
  * `[P:WORDING]`
* Minor tags:
  * `[I:ADDED]`
  * `[I:STRENGTHENED]`
  * `[I:TRANSFORMED]` (This means the meaning has been entirely changed)
  * `[I:MERGED_TO x.y.z ]` (ID defines where the requirement has gone)
  * `[I:MERGED_FROM x.y.z, x.y.w]` (IDs define which requirements have been merged into the current one)
  * `[I:SPLIT_TO x.y.z, x.y.w]` (IDs define where the requirement has been split to)
  * `[I:SPLIT_FROM x.y.z]` (This is like an addition except that the ID defines where the requirement has been split from)
* Major tags (not to be used until we are not going to make any more minor or patch releases before a major release):
  * `[M:MOVED_FROM x.y.z]` (ID defines where the requirement has come from)
  * `[M:MOVED_TO x.y.z]` (ID defines where the requirement has gone)

### Release process

#### Patch release

When a patch release comes along, we do the following:

* Create a branch for the patch release
* Reverse all requirement changes in the patch branch which are not acceptable for a patch based on the tag on the requirement (guided by tags).
* Manually review the changes which are being reversed out to see if we want to cherry pick some non-breaking changes that were within a requiremnt which also has breaking changes.
* Remove all tagging from the patch branch and bring the tag details into a separate file representing the changes in this release to act as release notes.
* Remove tags from requirements in the bleeding edge branch for changes that went into the patch branch. Tags should be relative to the previous release.

#### Minor release

When a minor release comes along, we do the following:

* Create a branch for the minor release
* Remove all tagging from the minor release branch and bring the tag details into a separate file representing the changes in this release to act as release notes.
* Remove tags from requirements in the bleeding edge branch. Tags should be relative to the previous release.

#### Major release

This will be more complicated and will be defined when we get there.

## How can I help?

We would be glad to receive feedback to help us to further enhance the ASVS. Whilst there may be some delays in responses, be assured that all issues will eventually be reviewed.

We are most likely to immediately accept changes to surrounding text and other content such as the appendices which is not considered a breaking change for release purposes but we will also start integrating changes that would require a patch or minor release. For major changes such as moves, you are welcome to open an issue but please note that the issue may not be progressed until we are considering a new major release, for which there is currently no fixed timeline.

## Additional Details for Helping

### Before you open a Pull Request

Please do not open a pull request without first opening an associated issue. Please do not open an issue until you have used the search functionality to ensure that the issue has not previously been discussed and that there are no currently open issues relating to it. For example, [this link](https://github.com/OWASP/ASVS/issues?q=is%3Aissue+bcrypt) searches for issues (open and closed) related to bcrypt.

### Numbering changes compared to the issues.

Note that since there were major numbering changes between v4.0.3 and the bleeding edge version of v5.0.0 (known as v5.0.be), and between v5.0.be and the final v5.0.0 release. As such, a lot of the requirement numbers in the issues may be different, depending on when the discussion was taking place. The following rough guide to numbering applies:

* The v4.0.3 numberings were valid at the time of its release in October 2021.
* The v5.0.be numberings cover the period from then until the major renumbering around 27th March 2025
* The v5.0.0 numberings cover the period from the major renumbering until the v5.0.0 release at the end of May 2025. 

The mappings in the [mappings folder](https://github.com/OWASP/ASVS/tree/master/5.0/mappings/) can be used to check what number the requirement was at the point in time it was being discussed:

If you are comfortable that your query has not been previously discussed, you can open an issue. Please try and include the ASVS requirement number and text you are talking about in the issue to save having to jump back and forth and please carry out all discussion in the associated issue and not in a PR discussion.

## Translations

We are now keen to receive translations for v5.0.0 of ASVS!

Note that we are ONLY accepting translations based on markdown and not preformatted translations in Word or PDF format to make tracking and maintenance easier. 

If you are interested in creating a translation, here are some pointers for how you can help us:

* Please first of all search the repository to see if there is already a translation for your proposed language. We currently have completed or in-progress translations in the following languages (but please search anyway in case this list is superseded!):
    * In-progress
        * Persian (Farsi), [#3172](https://github.com/OWASP/ASVS/issues/3172)
        * Ukrainian, see [#3174](https://github.com/OWASP/ASVS/issues/3174)
        * Portuguese, see [#3182](https://github.com/OWASP/ASVS/issues/3182)
        * Simplified Chinese, see [#3191](https://github.com/OWASP/ASVS/issues/3191)
        * Spanish, see [#3238](https://github.com/OWASP/ASVS/issues/3238)
        * Panjabi, see[#3252](https://github.com/OWASP/ASVS/issues/3252)
    * v5.0.0
        * [Turkish](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/tr/)
        * [Russian](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/ru/)
        * [French](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/fr/)
        * [Korean](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/ko/)
* If the language you are interested in appears, it would be great if you could reach out to the translator to see if you can help them.
* Often there is work to do in creating markdown files or updating the translation to keep it up to date with latest changes.
* We would request that you **specifically base your translation** on the 5.0/en folder from the **v5.0.0** branch as this is now static at the 5.0.0 version.
* In order to start a translation, please start by forking the ASVS repository.
* Checkout the **v5.0.0** branch. take a copy of the /en folder and rename it to the 2 character language code which will be used for the translation.
* You can then edit the markdown files to include your translation rather than the original English.
* When you have completed the translation, please open a Pull Request against the v5.0.0 ASVS branch and one of the leaders will look at integrating it.
* The leader will also use the relevant scripts to create the documents from the raw markdown (or you can if you want to save us some trouble).
* Finally, the leader will back port the translation into the branch containing the ASVS version which was targeted (at this point, presumably v5.0.0).

Thank you for your help!!
