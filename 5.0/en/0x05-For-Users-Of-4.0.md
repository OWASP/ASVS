# Guidance for users of version 4.0

## TODO: Add more content

### Challenges with the previous approach

Version 4.0 of the ASVS describes the levels as L1 - "Minimum", L2 - "Standard", and L3 - "Advanced" with the implication that all applications processing sensitive data should be at least L2.

There have been a few challenges with this approach.

#### High barrier to entry

L1 in version 4.0 had over 100 requirements as did L2 with only a few requirements left in L3. This meant that a high level of effort required to achieve even L1 at which point the user is told that this is the "minimum" level and that to achieve a "standard" level of security, another 100 requirements are required. Based on feedback from ASVS users and community it became clear that this acted as a disincentive and made it harder for applications to start adopting the ASVS.

#### The fallacy of testability

A primary motivator behind putting controls in L1 version 4.0 was whether they could be checked using "black box" style testing which was not entirely in line with the concept of L1 being the minimum security controls. On the one hand, ASVS users would say that L1 was not sufficient for a secure application whilst on the other hand user would complain that ASVS was too difficult to test.

Additionally, testability is relative and in some cases misleading. Just because something is testable does not mean that it is testable in an automated or trivial way. Finally, the most testable requirements are not necessarily those that have the most important security impact or are the easiest to implement.

#### Not just about risk

The use of prescriptive, risk based levels which mandate that a certain application has to be at a certain level seems overly opinionated in hind-sight. In reality, the order of implementing security controls will depend on factors including both risk reduction and also effort to implement.
