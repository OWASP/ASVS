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

To help those who are using the "bleeding edge" version for their tests and in order to be able to track changes made during this period, we have prepared a set of labels to be used when making changes to the "bleeding edge" version during this time. If there is enough content to make a 4.0.3 or 4.1 release, this will also make it easier to get an overview of changes in place

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

The following tags should be added to any modified requirement as appropriate. These tags should all be relative to how the requirement appeared in v4.0.2.

* `[ADDED]` - New requirement (should only be added at the end of a sub-section.)
* `[ADDED, SPLIT FROM x.y.z]` - New requirement which was previously part of another requirement
* `[MODIFIED]` - Requirement description has been modified
* `[MOVED FROM x.y.z]` - Requirement has been moved to a different sub-section but **not** modified. (should only be added at the end of a sub-section.)
* `[MODIFIED, MOVED FROM x.y.z]` - Requirement description has been modified **and** requirement has been moved to a different sub-section.
* `[MOVED TO x.y.z]` - Placeholder to keep number, requirement has been moved to another category (but not modified).
* `[DELETED]` - Placeholder to keep number, requirement has been deleted
* `[DELETED, MERGED TO x.y.z]` - Placeholder to keep number, requirement has been merged into another requirement, e.g. to solve a duplicate
* `[LEVEL L1 > L2]` - Requirement's level has changed

CWE and/or NIST mapping changes do not require labels.

Tags must be placed before verification description, example:

```
| **12.4.2** | [MODIFIED] Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload and serving of known malicious content. | ✓ | ✓ | ✓ | 509 |
```


