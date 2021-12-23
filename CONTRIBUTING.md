# Contributing

**This document applies during 2021 and may change at a future date.**

<!--

## General description

open issue > discuss, if agreed > pull request


## Versions

for what versions what kind of changes are allowed

definition of breaking change


## Opening issue

expectation from issue


## Pull-request

expectation from PR
-->

### Introduction

The current status of the ASVS project is as follows:

> The ASVS project is planning to release a 5.0 version during 2022 which will be a significant modification, similar to the scale of changes which happened during 4.0.
> 
> We will try, on a best efforts basis, to address issues and push changes to the "bleeding edge", master branch. For as long as possible, we will make changes to this branch **without altering current numbering** and wherever possible we will push minor, non-breaking changes to a 4.0.3 branch which may or may not be formally released.

### How to make changes to the bleeding edge during this period

To help those who are using the "bleeding edge" version for their tests and in order to be able to track changes made during this period, we have prepared a set of labels to be used when making changes to the "bleeding edge" version during this time. The current bleeding edge working directory can be found here <https://github.com/OWASP/ASVS/tree/master/5.0/en>.


### Standard for changes

#### Keep all current numbers

* New requirements must be placed at the end of sub-category
* Deleted requirements must keep "placeholder" to avoid some other requirements to be added/moved to that number, examples:

```
| **1.2.1** | [MOVED TO 1.14.7] | | | | |
```

```
| **5.5.1** | [DELETED] | | | | |
```

#### Use tags to describe the change

Projects leads will check and validate labels for changes. Please ask for a recommendation regarding the proper label in the issue tracker if you have any questions.

These tags should all be relative to how the requirement appeared in the latest release (v4.0.3).

The following tags should be added to any modified requirement as appropriate.

* `[ADDED]` - New requirement (should only be added at the end of a sub-section.)
* `[MODIFIED]` - Requirement description has been modified
* `[MOVED TO x.y.z]` - Placeholder to keep number, requirement has been moved to another category
* `[MOVED FROM a.b.c]` - Requirement has been moved to a different sub-section but **not** modified. (should only be added at the end of a sub-section.)
* `[MODIFIED, MOVED FROM a.b.c]` - Requirement description has been modified **and** requirement has been moved to a different sub-section.
* `[MODIFIED, SPLIT TO x.y.z]` - Requirement description has been modified **and** part of the requirement is splitted to new separate requirement
* `[ADDED, SPLIT FROM a.b.c]` - New requirement which was previously part of another requirement
* `[DELETED]` - Placeholder to keep number, requirement has been deleted
* `[DELETED, MERGED TO x.y.z]` - Placeholder to keep number, requirement has been merged into another requirement
* `[DELETED, DUPLICATE OF x.y.z]` - Placeholder to keep number, requirement has been deleted because of clear duplicate to referenced requirement (referenced requirement do not have changes because of that)
* `[SPLIT TO x.y.z, i.j.f]` - Placeholder to keep number, requirement has been splitted to 2 or more requirements to another categories
* `[LEVEL L1 > L2]` - Requirement's level has changed. Level change label may exist also for `[MODIFIED]`, `[MOVED FROM]` and `[SPLIT FROM]`


`SPLIT TO`, `MOVED TO`, `MERGED TO` labels must have matching labels with `SPLIT FROM`, `MOVED FROM`, `MERGED FROM`.

CWE and/or NIST mapping changes do not require labels.

Tags must be placed before verification description, example:

```
| **12.4.2** | [MODIFIED] Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload and serving of known malicious content. | ✓ | ✓ | ✓ | 509 |
```

### Translations

We are also actively looking for translations of the 4.n branch!

If you are interested in creating a translation, here are some pointers for how you can help us:
* Please first of all search the repository to see if there is already a translation for your proposed language. We currently have completed or in-progress translations in the following languages (but please search anyway in case this list is superceeded!):
    * v4.0.3
        * Spanish
        * Arabic (in-progress)
    * v4.0.2
        * German
        * Russian (complete but v4.0.3 is in-progress)
    * v4.0.1
        * French
        * Persian
        * Turkish
        * Japanese
* If the language you are interested in appears, it would be great if you could reach out to the translator to see if you can help them.
* Often there is work to do in creating markdown files or updating the translation to keep it up to date with latest changes.
* We would request that you base your translation on the 4.0/en folder in the master branch as this is now static at the 4.0.3 version.
* In order to start a translation, please start by forking the ASVS repository.
    * If you are updating an existing translation which has markdown (just French as at December 2021), you can make modifications to the files in the existing folder based on language code (just /fr as at December 2021).
    * if you are starting a new markdown translation, take a copy of the /en folder and rename it to the 2 character language code which will be used for the translation. 
* When you have completed the translation, please open a Pull Request against the master ASVS branch and one of the leaders will look at integrating it.
* The leader will also use the relevant scripts to create the documents from the raw markdown (or you can if you want to save us some trouble  )
* Finally, the leader will back port the translation into the branch containing ASVS version which was targeted (at this point, presumably v4.0.3)

Thanks!!
