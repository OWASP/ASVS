# Contributing

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

### Labels in requirements

"The ASVS project is planning to release a 5.0 version during 2022 which will be a significant modification, similar to the scale of changes which happened during 4.0."
"We will try on a best efforts basis to address issues and push changes to the "bleeding edge", master branch. For as long as possible, we will make changes to this branch **without altering current numbering** and whereever possible we will push minor, non-breaking changes to a 4.0.3 branch which may or may not be formally released."

To be able to track changes.
  * Helpful for those who are using "bleeding edge" for their tests
  * In case there is wish or enough content to make release 4.0.3 or 4.1, it's easier to get overview of changes in place

#### Tags

Tags are "changes from v4.0.2".

* `[ADDED]` - new requirement
* `[ADDED, SPLIT FROM x.y.z]` - new requirement was previously part of another requirement
* `[MODIFIED]` - requirement description is modified
* `[MOVED FROM x.y.z]` - requirement is moved but not modified
* `[MODIFIED, MOVED FROM x.y.z]` - requirement description is modified AND moved
* `[MOVED TO x.y.z]` - (placeholder to keep number) requirement is moved to another category (but not modified)
* `[DELETED]` - (placeholder to keep number) requirement is deleted
* `[DELETED, MERGED TO x.y.z]` - (placeholder to keep number) requirement is merged to another requirement, solved duplicate
* `[LEVEL L1 > L2]` - level is changed

CWE and/or NIST mapping changes does not require labels.

Tags must be placed before verification description, example:
```
| **12.4.2** | [MODIFIED] Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload and serving of known malicious content. | ✓ | ✓ | ✓ | 509 |
```

#### Keep all current numbers

* New requirements must be placed at the end of subcategory
* Deleted requirements must keep "placeholder" to avoid some other requirements to be added/moved to that number, examples:

```
| **1.2.1** | [MOVED TO 1.14.7] | | | | |
```

```
| **5.5.1** | [DELETED] | | | | |
```
