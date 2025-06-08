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

* Major release - Full reorganization, almost everything may have changed, including requirement numbers. Reevaluation for compliance will be necessary (for example, 4.0.3 -> 5.0.0).
* Minor release - Requirements may be added or removed, but overall numbering will stay the same. Reevaluation for compliance will be necessary, but should be easier (for example, 5.0.0 -> 5.1.0).
* Patch release - Requirements may be removed (for example, if they are duplicates or outdated) or made less stringent, but an application that complied with the previous release will comply with the patch release as well (for example, 5.0.0 -> 5.0.1).

The above specifically relates to the requirements in the ASVS. Changes to surrounding text and other content such as the appendices will not be considered to be a breaking change.

## How can I help?

We would be glad to receive feedback to help us to further enhance the ASVS.

At this stage, we are accepting the following types of changes:

* Changes to surrounding text and other content such as the appendices which is not be considered to be a breaking change for release purposes.
* Changes which are considered "non-breaking" for an ASVS "patch" release. This means that requirements may be removed (for example, if they are duplicates or outdated) or made less stringent, but an application that complied with the previous release will comply with the patch release as well.

If you feel there are other important changes but they would be considered breaking for a patch release, you are welcome to open an issue but please note that the issue may not be progressed until we are considering a new minor or major release, for which there is currently no fixed timeline.

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

<!-- COMMENTING OUT FOR FUTURE USE

  * Mapping from v4.0.3 to v5.0.0:
    * <https://github.com/OWASP/ASVS/blob/master/5.0/mappings/mapping_v4.0.3_to_v5.0.0.yml> - mapping file
    * <https://asvs.dev/mapping_v4.0.3_to_v5.0.0.html> - formatted output
  * Mapping from v5.0.0 to v4.0.3:
    * <https://github.com/OWASP/ASVS/blob/master/5.0/mappings/mapping_v5.0.0_to_v4.0.3.yml> - mapping file
    * <https://asvs.dev/mapping_v5.0.0_to_v4.0.3.html> - formatted output

Tags in new (v5.0.0) mapping file:

  * `ADDED` - new requirement
  * `MOVED FROM x.y.z` - reference to the requirement number from v4.0.3. Must have a matching `MOVE TO` tag in the old mapping file.
    * `GRAMMAR` - indicates that there are grammar or language corrections in the moved requirement, which don't change the requirement's meaning.
    * `MODIFIED` - indicates that the meaning of the moved requirement was changed (more than just a language or grammar change).
  * `SPLIT FROM x.y.z` - the v4.0.3 requirement was split to multiple requirements in v5.0.0. Must have a matching `SPLIT TO` in the old mapping file.
  * `MERGED FROM x.y.z` - the v4.0.3 requirement has been merged with another requirement for v5.0.0. Must have a matching `MERGED TO` tag in the old mapping file.
  * `COVERS x.y.z` - the v5.0.0 requirement covers the content of this v4.0.3 requirement. Must have a matching `COVERED BY x.y.z` tag in the old mapping file.

Tags in old (v4.0.3) mapping file:

  * `DELETED` - the v4.0.3 requirement is deleted in the new version, with a reason.
    * `DELETED, NOT IN SCOPE` - requirement has been decided to be out of the redefined scope of ASVS.
    * `DELETED, INCORRECT` - requirement was invalid or provided inadvisable advice.
    * `DELETED, NOT PRACTICAL` - the requirement was not practical (enough) to implement in reality.
    * `DELETED, INSUFFICIENT IMPACT` - the requirement provided insufficient benefit to be worthwhile.
    * `DELETED, MERGED TO x.y.z` - the requirement was merged to another requirement for v5.0.0. Must have a matching `MERGED FROM` tag in the new mapping file.
    * `DELETED, COVERED BY x.y.z` - the requirement was a duplicate of or is covered by another requirement in v5.0.0. Must have a matching `COVERS` tag in the new mapping file.
  * `MOVED TO x.y.z` - reference to the requirement number from v5.0.0. Must have a matching `MOVED FROM` tag in the new version
  * `SPLIT TO x.y.z, i.j.k` - the v4.0.3 requirement is divided into multiple requirements in v5.0.0. Must have matching `SPLIT FROM` tags in the new mapping file.

-->

## Translations

We are now keen to receive translations for v5.0.0 of ASVS!

Note that we are ONLY accepting translations based on markdown and not preformatted translations in Word or PDF format to make tracking and maintenance easier. 

If you are interested in creating a translation, here are some pointers for how you can help us:

* Please first of all search the repository to see if there is already a translation for your proposed language. We currently have completed or in-progress translations in the following languages (but please search anyway in case this list is superseded!):
    * In-progress
        * Turkish, see [#3171](https://github.com/OWASP/ASVS/issues/3171)
        * Persian (Farsi), [#3172](https://github.com/OWASP/ASVS/issues/3172)
        * Ukrainian, see [#3174](https://github.com/OWASP/ASVS/issues/3174)
        * Portuguese, see [#3182](https://github.com/OWASP/ASVS/issues/3182)
        * French, see [#3188](https://github.com/OWASP/ASVS/issues/3188)
        * Simplified Chinese, see [#3191](https://github.com/OWASP/ASVS/issues/3191)
    * v5.0.0
        * None
* If the language you are interested in appears, it would be great if you could reach out to the translator to see if you can help them.
* Often there is work to do in creating markdown files or updating the translation to keep it up to date with latest changes.
* We would request that you base your translation on the 5.0/en folder in the v5.0.0 branch as this is now static at the 5.0.0 version.
* In order to start a translation, please start by forking the ASVS repository.
* Take a copy of the /en folder and rename it to the 2 character language code which will be used for the translation.
* You can then edit the markdown files to include your translation rather than the original English.
* When you have completed the translation, please open a Pull Request against the v5.0.0 ASVS branch and one of the leaders will look at integrating it.
* The leader will also use the relevant scripts to create the documents from the raw markdown (or you can if you want to save us some trouble).
* Finally, the leader will back port the translation into the branch containing the ASVS version which was targeted (at this point, presumably v5.0.0).

Thank you for your help!!
