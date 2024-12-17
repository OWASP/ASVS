# Appendix A: Glossary

* **Absolute Maximum Session Lifetime** - Also referred to as "Overall Timeout" by NIST, this is the maximal amount of time a session can remain active following authentication regardless of user interaction. This is a component of session expiration.
* **Address Space Layout Randomization** (ASLR) – A technique to make exploiting memory corruption bugs more difficult.
* **Allowlist** – A list of permitted data or operations, for example, a list of characters that are allowed to perform input validation.
* **Application Security** – Application-level security focuses on the analysis of components that comprise the application layer of the Open Systems Interconnection Reference Model (OSI Model), rather than focusing on for example the underlying operating system or connected networks.
* **Application Security Verification** – The technical assessment of an application against the OWASP ASVS.
* **Application Security Verification Report** – A report that documents the overall results and supporting analysis produced by the verifier for a particular application.
* **Authentication** – The verification of the claimed identity of an application user.
* **Automated Verification** – The use of automated tools (either dynamic analysis tools, static analysis tools, or both) that use vulnerability signatures to find problems.
* **Black box testing** – It is a method of software testing that examines the functionality of an application without peering into its internal structures or workings.
* **Component** – a self-contained unit of code, with associated disk and network interfaces that communicates with other components.
* **Credential Service Provider** (CSP) - Also called an Identity Provider (IdP). A source of user data which may be used as an authentication source by other applications.
* **Cross-Site Scripting** (XSS) – A security vulnerability typically found in web applications allowing the injection of client-side scripts into content.
* **Cryptographic module** – Hardware, software, and/or firmware that implements cryptographic algorithms and/or generates cryptographic keys.
* **Common Weakness Enumeration** (CWE) - A community-developed list of common software security weaknesses. It serves as a common language, a measuring stick for software security tools, and a baseline for weakness identification, mitigation, and prevention efforts.
* **Design Verification** – The technical assessment of the security architecture of an application.
* **Dynamic Application Security Testing** (DAST) - Technologies are designed to detect conditions indicative of a security vulnerability in an application in its running state.
* **Dynamic Verification** – The use of automated tools that use vulnerability signatures to find problems during the execution of an application.
* **Fast IDentity Online** (FIDO) - A set of authentication standards that allow a variety of different authentication methods to be used including biometrics, Trusted Platform Modules (TPMs), USB security tokens, etc.
* **Universally Unique Identifier** (UUID) – a unique reference number used as an identifier in software.
* **HyperText Transfer Protocol** (HTTPS) – An application protocol for distributed, collaborative, hypermedia information systems. It is the foundation of data communication for the World Wide Web.
* **Hardcoded keys** – Cryptographic keys that are stored on the filesystem, be it in code, comments or files.
* **Hardware Security Module** (HSM) - Hardware component that stores cryptographic keys and other secrets in a protected manner.
* **Hibernate Query Language** (HQL) - A query language that is similar in appearance to SQL used by the Hibernate ORM library.
* **Inactivity Timeout** - This is the length of time a session can remain active in the absence of user interaction with the application. This is a component of session expiration.
* **Input Validation** – The canonicalization and validation of untrusted user input.
* **JSON Web Token** (JWT) - RFC 7519 defines a standard for a JSON data object made up of a header section which explains how to validate the object, a body section containing a set of claims, and a signature section which contains a digital signature which can be used to validate the contents of the body section. It is a type of self-contained token.
* **Malicious Code** – Code introduced into an application during its development unbeknownst to the application owner, which circumvents the application's intended security policy. Not the same as malware such as a virus or worm!
* **Malware** – Executable code that is introduced into an application during runtime without the knowledge of the application user or administrator.
* **Multi-factor authentication** (MFA) - Authentication which includes two or more of the single factors.
* **Open Worldwide Application Security Project** (OWASP) – The Open Worldwide Application Security Project (OWASP) is a worldwide free and open community focused on improving the security of application software. Our mission is to make application security "visible," so that people and organizations can make informed decisions about application security risks. See: [https://www.owasp.org/](https://www.owasp.org/).
* **One-time Password** (OTP) - A password that is uniquely generated to be used on a single occasion.
* **Object-relational Mapping** (ORM) - A system used to allow a relational/table-based database to be referenced and queried within an application program using an application-compatible object model.
* **Password-Based Key Derivation Function 2** (PBKDF2) - A special one-way algorithm used to create a strong cryptographic key from an input text (such as a password) and an additional random salt value and can therefore be used to make it harder to crack a password offline if the resulting value is stored instead of the original password.
* **Personally Identifiable Information** (PII) - is information that can be used on its own or with other information to identify, contact, or locate a single person, or to identify an individual in context.
* **Position-independent executable** (PIE) - A body of machine code that, being placed somewhere in the primary memory, executes properly regardless of its absolute address.
* **Public Key Infrastructure** (PKI) - An arrangement that binds public keys with respective identities of entities. The binding is established through a process of registration and issuance of certificates at and by a certificate authority (CA).
* **Public Switched Telephone Network** (PSTN) - The traditional telephone network that includes both fixed-line telephones and mobile telephones.
* **Reference Token** - A type of token that acts as a pointer or identifier to state or metadata stored on a server, sometimes referred to as random tokens or opaque tokens. Unlike self-contained tokens, which embed some of their relevant data within the token itself, reference tokens contain no intrinsic information, instead relying on the server for context.
* **Relying Party** (RP) - Generally an application which is relying on a user having authenticated against a separate authentication provider. The application relies on some sort of token or set of signed assertions provided by that authentication provider to trust that the user is who they say they are.
* **Security Assertion Markup Language** (SAML) - An open standard for single sign-on authentication based on passing signed assertions (usually XML objects) between the identity provider and the relying party.
* **Static application security testing** (SAST) - A set of technologies designed to analyze application source code, byte code and binaries for coding and design conditions that are indicative of security vulnerabilities. SAST solutions analyze an application from the “inside out” in a nonrunning state.
* **Software development lifecycle** (SDLC) - The step-by-step process by which software is developed going from the initial requirements to deployment and maintenance.
* **Security Architecture** – An abstraction of an application's design that identifies and describes where and how security controls are used, and also identifies and describes the location and sensitivity of both user and application data.
* **Security Configuration** – The runtime configuration of an application that affects how security controls are used.
* **Security Control** – A function or component that performs a security check (e.g. an access control check) or when called results in a security effect (e.g. generating an audit record).
* **Self-Contained Token** - A token that encapsulates one or more attributes that do not rely on server-side state or other external storage. These tokens ensure the authenticity and integrity of their contained attributes, enabling secure, "stateless" information exchange across systems. Self-contained tokens are generally secured using cryptographic techniques, such as digital signatures or message authentication codes (MACs), to ensure the authenticity, integrity, and in some cases the confidentiality of its data. Common examples include SAML Assertions and JWTs.
* **Server-side Request Forgery** (SSRF) - An attack that abuses functionality on the server to read or update internal resources. The attacker supplies or modifies a URL, which the code running on the server will read or submit data to.
* **Single-factor authenticator** - A mechanism to check that a user is authenticated. It should either be something you know (memorized secrets, passwords, passphrases, PINs), something you are (biometrics, fingerprint, face scans), or something you have (OTP tokens, a cryptographic device such as a smart card).
* **Single Sign-on Authentication** (SSO) - This occurs when a user logs into one application and is then automatically logged into other applications without having to re-authenticate. For example, when you log into Google, you will be automatically logged into other Google services such as YouTube, Google Docs, and Gmail.
* **Software Composition Analysis** (SCA) - A set of technologies designed to analyze application composition, dependencies, libraries and packages for security vulnerabilities of specific component versions in use. This is not to be confused with source-code analysis which is now commonly referred to as SAST.
* **SQL Injection** (SQLi) – A code injection technique used to attack data-driven applications, in which malicious SQL statements are inserted into an entry point.
* **Stateful Session Mechanism** - In a stateful session mechanism, the application retains session state at the back end which typically corresponds to a random session identifier which is issued to the end user.
* **Stateless Session Mechanism** - A stateless session mechanism will use a self-contained token which is passed to clients, and contains session information that is not necessarily stored within the service which then receives and validates the token. In reality, a service will need to have access to some session information (such as a JWT revocation list) in order to be able to enforce required security controls.
* **SVG** - Scalable Vector Graphics.
* **Time-based OTP** - A method of generating an OTP where the current time acts as part of the algorithm to generate the password.
* **Threat Modeling** - A technique consisting of developing increasingly refined security architectures to identify threat agents, security zones, security controls, and important technical and business assets.
* **Transport Layer Security** (TLS) – Cryptographic protocols that provide communication security over a network connection.
* **Trusted Platform Module** (TPM) - A type of HSM that is usually attached to a larger hardware component such as a motherboard and acts as the "root of trust" for that system.
* **Trusted Service Layer** - Any trusted control enforcement point, such as a microservice, serverless API, server-side, a trusted API on a client device that has secure boot, partner or external APIs, and so on. Trusted means that we are not concerned that an untrusted user will be able to bypass or skip the layer or controls implemented at that layer.
* **Universal 2nd Factor** (U2F) - One of the standards created by FIDO specifically for allowing a USB or NFC security key to be used as a 2nd authentication factor.
* **URI/URL/URL fragments** – A Uniform Resource Identifier is a string of characters used to identify a name or a web resource. A Uniform Resource Locator is often used as a reference to a resource.
* **Verifier** – The person or team that is reviewing an application against the OWASP ASVS requirements.
* **What You See Is What You Get** (WYSIWYG) - A type of rich content editor that shows how the content will actually look when rendered rather than showing the coding used to govern the rendering.
* **X.509 Certificate** – An X.509 certificate is a digital certificate that uses the widely accepted international X.509 public key infrastructure (PKI) standard to verify that a public key belongs to the user, computer or service identity contained within the certificate.
* **XML eXternal Entity** (XXE) - A type of XML entity that can access local or remote content via a declared system identifier. This may lead to various injection attacks.
