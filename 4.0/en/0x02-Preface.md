# Preface

Welcome to the Application Security Verification Standard (ASVS) version 4.0. The ASVS is a community-effort to establish a framework of security requirements and controls that focus on normalizing the functional and non-functional security controls required when designing, developing and testing modern web applications.

ASVS v4.0 is a culmination of community effort and industry feedback. In this release, we felt it was important to qualify the experiences of real world use cases relating to ASVS adoption. This will help newcomers to the standard plan their adoption of the ASVS, whilst assisting existing companies in learning from the experience of others.

We expect that there will most likely never be 100% agreement on this standard. Risk analysis is always subjective to some extent, which creates a challenge when attempting to generalize in a one size fits all standard. However, we hope that the latest updates made in this version are a step in the right direction, and respectfully enhance the concepts introduced in this important industry standard.

## What’s new in 4.0

The single largest change in this version is the adoption of NIST 800-63, concentrating on introducing controls at authentication assurance levels 1 through 3. Although we do expect there to be some pushback on this adoption, it's important for standards to be aligned, particularly when a newer standard is evidence based.

We have worked to comprehensively meet and exceed OWASP Top 10 2017 requirements. As the OWASP Top 10 2017 is the bare minimum to avoid negligence, we have deliberately set nearly all of OWASP Top 10 controls to be L1. This makes it easier for OWASP Top 10 adopters to continuously improve, especially when they want to continue the security journey by building in security into every application and API.

We have completed the shift of the ASVS from monolithic server side only controls, to providing solid controls for all modern applications and APIs. In the days of functional programming, server less API, mobile, cloud, IoT, CI/CD and DevOps, and federation, we cannot keep on ignoring modern application architecture. Modern applications are designed differently to those in 2008, when the original ASVS was written. The ASVS must always look far into the future so that we provide sound advice for our primary audience - developers. We have clarified or dropped any requirement that assumes that security must be solely performed on a server owned by a single organization.

We have retired the mobile section, in favor of the Mobile Application Security Verification Standard (MASVS) and the Internet of Things section in favour of the OWASP Internet of Things Projects. Our aim is to support them as much as possible, by being a reference where needed. As that standard does not particularly strongly elucidate API security issues, we have decided to concentrate on being the best standard for web apps and all forms of API - RESTful and SOAP web services, monolithic or micro services. Mobile application developers should see the MASVS as being highly useful for mobile client issues, and the ASVS as being highly useful for mobile APIs and micro services.

Lastly, we have de-duped and retired controls that cannot get you hacked. Over time, the ASVS started being a comprehensive set of controls, but not all controls are equal at producing secure software. We have re-validated L1 to be a "Core" or "Essential" control set, by setting a CVSS score bar of 7.5 or above to be in L1. This helps compliant organizations adhere to PCI DSS's requirements to resolve all High and Critical findings rapidly. If an application or API has a failed L1 control, it is a serious risk to any organization.
