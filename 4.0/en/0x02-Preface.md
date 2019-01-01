# Preface

Welcome to the Application Security Verification Standard (ASVS) version 4.0. The ASVS is a community-effort to establish a framework of security requirements and controls that focus on normalizing the functional and non-functional security controls required when designing, developing and testing modern web applications.

ASVS v4.0 is a culmination of community effort and industry feedback. In this release, we felt it was important to qualify the experiences of real world use cases relating to ASVS adoption. This will help newcomers to the standard plan their adoption of the ASVS, whilst assisting existing companies in learning from the experience of others.

We expect that there will most likely never be 100% agreement on this standard. Risk analysis is always subjective to some extent, which creates a challenge when attempting to generalize in a one-size-fits-all standard. However, we hope that the latest updates made in this version are a step in the right direction, and respectfully enhance the concepts introduced in this important industry standard.

## What's new in 4.0

In June 2017, The National Institute of Science and Technology (NIST) released Special Publication (SP) 800-63-3, which is an updated set of digital identity guidelines. These technical guidelines provides an overview of general identity frameworks, using authenticators, credentials, and assertions together in a digital system, and a risk-based process of selecting assurance levels.

The single largest change in this version is the adoption of the NIST 800-63-3 guidelines, concentrating on introducing controls at authentication assurance levels 1 through 3. Although we do expect there to be some pushback on this adoption, it's important for standards to be aligned, particularly when a newer standard is evidence based.

We have worked to comprehensively meet and exceed the requirements for addressing the OWASP Top 10 Risks (2017). As the OWASP Top 10 Risks is the bare minimum to avoid negligence, we have deliberately set nearly all controls relating to OWASP Top 10 Risks to be L1. This makes it easier for OWASP Top 10 adopters to continuously improve, especially when they want to continue the security journey by building security into every application and API.

We have completed the shift of the ASVS from monolithic server side only controls, to providing solid controls for all modern applications and APIs. In the days of functional programming, server less API, mobile, cloud, IoT, CI/CD and DevOps, and federation, we cannot keep on ignoring modern application architecture. Modern applications are designed differently to those in 2008, when the original ASVS was written. The ASVS must always look far into the future so that we provide sound advice for our primary audience - developers. We have clarified or dropped any requirement that assumes that security must be solely performed on a server owned by a single organization.

We have retired the mobile section, in favor of the Mobile Application Security Verification Standard (MASVS) and the Internet of Things section in favour of the OWASP Internet of Things Projects. Our aim is to support them as much as possible, by being a reference where needed. As that standard does not particularly strongly elucidate API security issues, we have decided to concentrate on being the best standard for web apps and all forms of API - RESTful and SOAP web services, monolithic or micro services. Mobile application developers should see the MASVS as being highly useful for mobile client issues, and the ASVS as being highly useful for mobile APIs and micro services.

Lastly, we have de-duped and retired controls that cannot get you hacked. Over time, the ASVS started being a comprehensive set of controls, but not all controls are equal at producing secure software. 
