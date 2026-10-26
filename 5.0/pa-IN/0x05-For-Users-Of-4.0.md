<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x05-For-Users-Of-4.0.md -->
<!-- Translator: GeeksikhSecurity -->

# Changes Compared to v4.x
# v4.x ਦੇ ਮੁਕਾਬਲੇ ਤਬਦੀਲੀਆਂ

## Introduction
## ਜਾਣ-ਪਛਾਣ

Users familiar with version 4.x of the standard may find it helpful to review the key changes introduced in version 5.0, including updates in content, scope, and underlying philosophy.

ਮਿਆਰ ਦੇ ਸੰਸਕਰਣ 4.x ਤੋਂ ਜਾਣੂ ਵਰਤੋਂਕਾਰਾਂ ਨੂੰ ਸੰਸਕਰਣ 5.0 ਵਿੱਚ ਪੇਸ਼ ਕੀਤੀਆਂ ਗਈਆਂ ਮੁੱਖ ਤਬਦੀਲੀਆਂ ਦੀ ਸਮੀਖਿਆ ਕਰਨਾ ਮਦਦਗਾਰ ਲੱਗ ਸਕਦਾ ਹੈ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਸਮੱਗਰੀ, ਘੇਰੇ (scope), ਅਤੇ ਅੰਤਰਨਿਹਿਤ ਫ਼ਲਸਫ਼ੇ ਵਿੱਚ ਕੀਤੇ ਗਏ ਅੱਪਡੇਟ ਸ਼ਾਮਲ ਹਨ।

Of the 286 requirements in version 4.0.3, only 11 remain unchanged, while 15 have undergone minor grammatical adjustments without altering their meaning. In total 109 requirements (38%) are no longer separate requirements in version 5.0 with 50 simply being deleted, 28 removed as duplicates and 31 merged into other requirements. The rest have been revised in some way. Even requirements that were not substantively modified have different identifiers due to reordering or restructuring.

ਸੰਸਕਰਣ 4.0.3 ਦੀਆਂ 286 ਲੋੜਾਂ (requirements) ਵਿੱਚੋਂ, ਸਿਰਫ਼ 11 ਬਿਨਾਂ ਤਬਦੀਲੀ ਦੇ ਰਹੀਆਂ ਹਨ, ਜਦਕਿ 15 ਵਿੱਚ ਉਹਨਾਂ ਦੇ ਅਰਥ ਨੂੰ ਬਦਲੇ ਬਿਨਾਂ ਮਾਮੂਲੀ ਵਿਆਕਰਨਕ ਸੋਧਾਂ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। ਕੁੱਲ ਮਿਲਾ ਕੇ 109 ਲੋੜਾਂ (38%) ਸੰਸਕਰਣ 5.0 ਵਿੱਚ ਹੁਣ ਵੱਖਰੀਆਂ ਲੋੜਾਂ ਨਹੀਂ ਰਹੀਆਂ, ਜਿਨ੍ਹਾਂ ਵਿੱਚੋਂ 50 ਨੂੰ ਸਿੱਧੇ ਤੌਰ 'ਤੇ ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ, 28 ਨੂੰ ਦੁਹਰਾਅ (duplicates) ਵਜੋਂ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ ਅਤੇ 31 ਨੂੰ ਹੋਰ ਲੋੜਾਂ ਵਿੱਚ ਮਿਲਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਬਾਕੀ ਨੂੰ ਕਿਸੇ ਨਾ ਕਿਸੇ ਤਰੀਕੇ ਨਾਲ ਸੋਧਿਆ ਗਿਆ ਹੈ। ਇੱਥੋਂ ਤੱਕ ਕਿ ਜਿਨ੍ਹਾਂ ਲੋੜਾਂ ਵਿੱਚ ਕੋਈ ਸਾਰਥਕ ਸੋਧ ਨਹੀਂ ਕੀਤੀ ਗਈ, ਉਹਨਾਂ ਦੇ ਵੀ ਮੁੜ-ਤਰਤੀਬ ਜਾਂ ਮੁੜ-ਸੰਰਚਨਾ ਕਾਰਨ ਵੱਖਰੇ ਪਛਾਣਕਰਤਾ (identifiers) ਹਨ।

To facilitate adoption of version 5.0, mapping documents are provided to help users trace how requirements from version 4.x correspond to those in version 5.0. These mappings are not tied to release versioning and may be updated or clarified as needed.

ਸੰਸਕਰਣ 5.0 ਨੂੰ ਅਪਣਾਉਣ ਵਿੱਚ ਸਹੂਲਤ ਦੇਣ ਲਈ, ਮੈਪਿੰਗ ਦਸਤਾਵੇਜ਼ (mapping documents) ਪ੍ਰਦਾਨ ਕੀਤੇ ਗਏ ਹਨ ਜੋ ਵਰਤੋਂਕਾਰਾਂ ਨੂੰ ਇਹ ਲੱਭਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ ਕਿ ਸੰਸਕਰਣ 4.x ਦੀਆਂ ਲੋੜਾਂ ਸੰਸਕਰਣ 5.0 ਦੀਆਂ ਲੋੜਾਂ ਨਾਲ ਕਿਵੇਂ ਮੇਲ ਖਾਂਦੀਆਂ ਹਨ। ਇਹ ਮੈਪਿੰਗਾਂ ਰਿਲੀਜ਼ ਸੰਸਕਰਣ-ਨਿਰਧਾਰਨ ਨਾਲ ਬੱਝੀਆਂ ਹੋਈਆਂ ਨਹੀਂ ਹਨ ਅਤੇ ਜ਼ਰੂਰਤ ਅਨੁਸਾਰ ਅੱਪਡੇਟ ਜਾਂ ਸਪੱਸ਼ਟ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।

## Requirement Philosophy
## ਲੋੜਾਂ ਦਾ ਫ਼ਲਸਫ਼ਾ

### Scope and Focus
### ਘੇਰਾ ਅਤੇ ਕੇਂਦਰ-ਬਿੰਦੂ

Version 4.x included requirements that did not align with the intended scope of the standard; these have been removed. Requirements that did not meet the scope criteria for 5.0 or were not verifiable have also been excluded.

ਸੰਸਕਰਣ 4.x ਵਿੱਚ ਅਜਿਹੀਆਂ ਲੋੜਾਂ ਸ਼ਾਮਲ ਸਨ ਜੋ ਮਿਆਰ ਦੇ ਇੱਛਿਤ ਘੇਰੇ ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦੀਆਂ ਸਨ; ਇਹਨਾਂ ਨੂੰ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਉਹ ਲੋੜਾਂ ਜੋ 5.0 ਲਈ ਘੇਰੇ ਦੀਆਂ ਕਸੌਟੀਆਂ ਨੂੰ ਪੂਰਾ ਨਹੀਂ ਕਰਦੀਆਂ ਸਨ ਜਾਂ ਤਸਦੀਕਯੋਗ ਨਹੀਂ ਸਨ, ਉਹਨਾਂ ਨੂੰ ਵੀ ਬਾਹਰ ਰੱਖਿਆ ਗਿਆ ਹੈ।

### Emphasis on Security Goals Over Mechanisms
### ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਬਜਾਏ ਸੁਰੱਖਿਆ ਟੀਚਿਆਂ 'ਤੇ ਜ਼ੋਰ

In version 4.x, many requirements focused on specific mechanisms rather than the underlying security objectives. In version 5.0, requirements are centered on security goals, referencing particular mechanisms only when they are the sole practical solution, or providing them as examples or supplementary guidance.

ਸੰਸਕਰਣ 4.x ਵਿੱਚ, ਬਹੁਤ ਸਾਰੀਆਂ ਲੋੜਾਂ ਅੰਤਰਨਿਹਿਤ ਸੁਰੱਖਿਆ ਉਦੇਸ਼ਾਂ (security objectives) ਦੀ ਬਜਾਏ ਖ਼ਾਸ ਪ੍ਰਣਾਲੀਆਂ (mechanisms) 'ਤੇ ਕੇਂਦਰਿਤ ਸਨ। ਸੰਸਕਰਣ 5.0 ਵਿੱਚ, ਲੋੜਾਂ ਸੁਰੱਖਿਆ ਟੀਚਿਆਂ 'ਤੇ ਕੇਂਦਰਿਤ ਹਨ, ਅਤੇ ਖ਼ਾਸ ਪ੍ਰਣਾਲੀਆਂ ਦਾ ਹਵਾਲਾ ਸਿਰਫ਼ ਉਦੋਂ ਦਿੰਦੀਆਂ ਹਨ ਜਦੋਂ ਉਹ ਇੱਕੋ-ਇੱਕ ਵਿਹਾਰਕ ਹੱਲ ਹੋਣ, ਜਾਂ ਉਹਨਾਂ ਨੂੰ ਉਦਾਹਰਨਾਂ ਜਾਂ ਪੂਰਕ ਮਾਰਗਦਰਸ਼ਨ ਵਜੋਂ ਪ੍ਰਦਾਨ ਕਰਦੀਆਂ ਹਨ।

This approach recognizes that multiple methods may exist to achieve a given security objective, and avoids unnecessary prescriptiveness that could limit organizational flexibility.

ਇਹ ਪਹੁੰਚ ਇਸ ਗੱਲ ਨੂੰ ਮਾਨਤਾ ਦਿੰਦੀ ਹੈ ਕਿ ਕਿਸੇ ਦਿੱਤੇ ਗਏ ਸੁਰੱਖਿਆ ਉਦੇਸ਼ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਈ ਵਿਧੀਆਂ ਮੌਜੂਦ ਹੋ ਸਕਦੀਆਂ ਹਨ, ਅਤੇ ਬੇਲੋੜੀ ਨਿਰਦੇਸ਼ਾਤਮਕਤਾ (prescriptiveness) ਤੋਂ ਬਚਦੀ ਹੈ ਜੋ ਸੰਸਥਾਗਤ ਲਚਕ ਨੂੰ ਸੀਮਤ ਕਰ ਸਕਦੀ ਹੈ।

Additionally, requirements addressing the same security concern have been consolidated where appropriate.

ਇਸ ਤੋਂ ਇਲਾਵਾ, ਇੱਕੋ ਸੁਰੱਖਿਆ ਸਰੋਕਾਰ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਵਾਲੀਆਂ ਲੋੜਾਂ ਨੂੰ, ਜਿੱਥੇ ਢੁਕਵਾਂ ਸੀ, ਇਕੱਠਾ ਕਰ ਦਿੱਤਾ ਗਿਆ ਹੈ।

### Documented Security Decisions
### ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ

While the concept of documented security decisions may appear new in version 5.0, it is an evolution of earlier requirements related to policy application and threat modeling in version 4.0. Previously, some requirements implicitly demanded analysis to inform the implementation of security controls, such as determining permitted network connections.

ਭਾਵੇਂ ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਦਾ ਸੰਕਲਪ ਸੰਸਕਰਣ 5.0 ਵਿੱਚ ਨਵਾਂ ਜਾਪ ਸਕਦਾ ਹੈ, ਇਹ ਸੰਸਕਰਣ 4.0 ਵਿੱਚ ਨੀਤੀ ਲਾਗੂ ਕਰਨ ਅਤੇ ਖ਼ਤਰਾ ਮਾਡਲਿੰਗ (threat modeling) ਨਾਲ ਸੰਬੰਧਿਤ ਪਹਿਲੀਆਂ ਲੋੜਾਂ ਦਾ ਹੀ ਵਿਕਸਿਤ ਰੂਪ ਹੈ। ਪਹਿਲਾਂ, ਕੁਝ ਲੋੜਾਂ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ ਦੇ ਲਾਗੂਕਰਨ ਨੂੰ ਸੇਧ ਦੇਣ ਲਈ ਅਸਿੱਧੇ ਤੌਰ 'ਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਦੀ ਮੰਗ ਕਰਦੀਆਂ ਸਨ, ਜਿਵੇਂ ਕਿ ਇਜਾਜ਼ਤ-ਪ੍ਰਾਪਤ ਨੈੱਟਵਰਕ ਕਨੈਕਸ਼ਨਾਂ ਨੂੰ ਨਿਰਧਾਰਤ ਕਰਨਾ।

To ensure that necessary information is available for implementation and verification, these expectations are now explicitly defined as documentation requirements, making them clear, actionable, and verifiable.

ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ ਲਾਗੂਕਰਨ ਅਤੇ ਤਸਦੀਕ ਲਈ ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਉਪਲਬਧ ਹੋਵੇ, ਇਹਨਾਂ ਉਮੀਦਾਂ ਨੂੰ ਹੁਣ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਵਜੋਂ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਸਪੱਸ਼ਟ, ਕਾਰਜਯੋਗ ਅਤੇ ਤਸਦੀਕਯੋਗ ਬਣ ਗਈਆਂ ਹਨ।

## Structural Changes and New Chapters
## ਢਾਂਚਾਗਤ ਤਬਦੀਲੀਆਂ ਅਤੇ ਨਵੇਂ ਅਧਿਆਇ

Several chapters in version 5.0 introduce entirely new content:

ਸੰਸਕਰਣ 5.0 ਦੇ ਕਈ ਅਧਿਆਇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਨਵੀਂ ਸਮੱਗਰੀ ਪੇਸ਼ ਕਰਦੇ ਹਨ:

* OAuth and OIDC – Given the widespread adoption of these protocols for access delegation and single sign-on, dedicated requirements have been added to address the diverse scenarios developers may encounter. This area may eventually evolve into a standalone standard, similar to the treatment of Mobile and IoT requirements in previous versions.
* WebRTC – As this technology gains popularity, its unique security considerations and challenges are now addressed in a dedicated section.

* OAuth ਅਤੇ OIDC – ਪਹੁੰਚ ਸੌਂਪਣ (access delegation) ਅਤੇ ਸਿੰਗਲ ਸਾਈਨ-ਔਨ ਲਈ ਇਹਨਾਂ ਪ੍ਰੋਟੋਕਾਲਾਂ ਦੇ ਵਿਆਪਕ ਅਪਣਾਏ ਜਾਣ ਨੂੰ ਦੇਖਦਿਆਂ, ਵਿਕਾਸਕਾਰਾਂ ਦੇ ਸਾਹਮਣੇ ਆ ਸਕਣ ਵਾਲੇ ਵੱਖ-ਵੱਖ ਹਾਲਾਤਾਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਲਈ ਸਮਰਪਿਤ ਲੋੜਾਂ ਜੋੜੀਆਂ ਗਈਆਂ ਹਨ। ਇਹ ਖੇਤਰ ਅੰਤ ਵਿੱਚ ਇੱਕ ਸੁਤੰਤਰ ਮਿਆਰ ਵਿੱਚ ਵਿਕਸਿਤ ਹੋ ਸਕਦਾ ਹੈ, ਜਿਵੇਂ ਪਿਛਲੇ ਸੰਸਕਰਣਾਂ ਵਿੱਚ ਮੋਬਾਈਲ ਅਤੇ IoT ਲੋੜਾਂ ਨਾਲ ਕੀਤਾ ਗਿਆ ਸੀ।
* WebRTC – ਜਿਵੇਂ-ਜਿਵੇਂ ਇਹ ਤਕਨਾਲੋਜੀ ਪ੍ਰਸਿੱਧ ਹੋ ਰਹੀ ਹੈ, ਇਸ ਦੇ ਵਿਲੱਖਣ ਸੁਰੱਖਿਆ ਵਿਚਾਰਾਂ ਅਤੇ ਚੁਣੌਤੀਆਂ ਨੂੰ ਹੁਣ ਇੱਕ ਸਮਰਪਿਤ ਭਾਗ ਵਿੱਚ ਸੰਬੋਧਿਤ ਕੀਤਾ ਗਿਆ ਹੈ।

Efforts have also been made to ensure that chapters and sections are organized around coherent sets of related requirements.

ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਵੀ ਯਤਨ ਕੀਤੇ ਗਏ ਹਨ ਕਿ ਅਧਿਆਇ ਅਤੇ ਭਾਗ ਸੰਬੰਧਿਤ ਲੋੜਾਂ ਦੇ ਸੁਸੰਗਤ ਸਮੂਹਾਂ ਦੁਆਲੇ ਸੰਗਠਿਤ ਹੋਣ।

This restructuring has led to the creation of additional chapters:

ਇਸ ਮੁੜ-ਸੰਰਚਨਾ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਵਾਧੂ ਅਧਿਆਇ ਬਣਾਏ ਗਏ ਹਨ:

* Self-contained Tokens – Formerly grouped under session management, self-contained tokens are now recognized as a distinct mechanism and a foundational element for stateless communication (such as in OAuth and OIDC). Due to their unique security implications, they are addressed in a dedicated chapter, with some new requirements introduced in version 5.x.
* Web Frontend Security – With the increasing complexity of browser-based applications and the rise of API-only architectures, frontend security requirements have been separated into their own chapter.
* Secure Coding and Architecture – New requirements addressing general security practices that did not fit within existing chapters have been grouped here.

* ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ (Self-contained Tokens) – ਪਹਿਲਾਂ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਦੇ ਅਧੀਨ ਸਮੂਹਬੱਧ, ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨਾਂ ਨੂੰ ਹੁਣ ਇੱਕ ਵੱਖਰੀ ਪ੍ਰਣਾਲੀ ਅਤੇ ਸਟੇਟਲੈੱਸ (stateless) ਸੰਚਾਰ (ਜਿਵੇਂ ਕਿ OAuth ਅਤੇ OIDC ਵਿੱਚ) ਲਈ ਇੱਕ ਬੁਨਿਆਦੀ ਤੱਤ ਵਜੋਂ ਮਾਨਤਾ ਦਿੱਤੀ ਗਈ ਹੈ। ਉਹਨਾਂ ਦੇ ਵਿਲੱਖਣ ਸੁਰੱਖਿਆ ਪ੍ਰਭਾਵਾਂ ਕਾਰਨ, ਉਹਨਾਂ ਨੂੰ ਇੱਕ ਸਮਰਪਿਤ ਅਧਿਆਇ ਵਿੱਚ ਸੰਬੋਧਿਤ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਿਸ ਵਿੱਚ ਸੰਸਕਰਣ 5.x ਵਿੱਚ ਕੁਝ ਨਵੀਆਂ ਲੋੜਾਂ ਪੇਸ਼ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ।
* ਵੈੱਬ ਫਰੰਟਐਂਡ ਸੁਰੱਖਿਆ (Web Frontend Security) – ਬ੍ਰਾਊਜ਼ਰ-ਆਧਾਰਿਤ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੀ ਵਧਦੀ ਗੁੰਝਲਤਾ ਅਤੇ ਸਿਰਫ਼-API ਆਰਕੀਟੈਕਚਰਾਂ ਦੇ ਉਭਾਰ ਦੇ ਨਾਲ, ਫਰੰਟਐਂਡ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਨੂੰ ਉਹਨਾਂ ਦੇ ਆਪਣੇ ਵੱਖਰੇ ਅਧਿਆਇ ਵਿੱਚ ਰੱਖਿਆ ਗਿਆ ਹੈ।
* ਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ ਅਤੇ ਆਰਕੀਟੈਕਚਰ (Secure Coding and Architecture) – ਆਮ ਸੁਰੱਖਿਆ ਅਮਲਾਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਵਾਲੀਆਂ ਨਵੀਆਂ ਲੋੜਾਂ, ਜੋ ਮੌਜੂਦਾ ਅਧਿਆਇਆਂ ਵਿੱਚ ਫਿੱਟ ਨਹੀਂ ਬੈਠਦੀਆਂ ਸਨ, ਇੱਥੇ ਸਮੂਹਬੱਧ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ।

Other organizational changes in version 5.0 were made to clarify intent. For example, input validation requirements were moved alongside business logic, reflecting their role in enforcing business rules, rather than being grouped with sanitization and encoding.

ਸੰਸਕਰਣ 5.0 ਵਿੱਚ ਹੋਰ ਸੰਗਠਨਾਤਮਕ ਤਬਦੀਲੀਆਂ ਇਰਾਦੇ ਨੂੰ ਸਪੱਸ਼ਟ ਕਰਨ ਲਈ ਕੀਤੀਆਂ ਗਈਆਂ ਸਨ। ਉਦਾਹਰਨ ਲਈ, ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ (input validation) ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਕਾਰੋਬਾਰੀ ਤਰਕ ਦੇ ਨਾਲ ਲਿਜਾਇਆ ਗਿਆ, ਜੋ ਕਾਰੋਬਾਰੀ ਨਿਯਮਾਂ ਨੂੰ ਲਾਗੂ ਕਰਨ ਵਿੱਚ ਉਹਨਾਂ ਦੀ ਭੂਮਿਕਾ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ, ਨਾ ਕਿ ਉਹਨਾਂ ਨੂੰ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਏਨਕੋਡਿੰਗ ਨਾਲ ਸਮੂਹਬੱਧ ਰੱਖਿਆ ਗਿਆ।

The former V1 Architecture chapter has been removed. Its initial section contained requirements that were out of scope, while subsequent sections have been redistributed to relevant chapters, with requirements deduplicated and clarified as necessary.

ਪੁਰਾਣੇ V1 ਆਰਕੀਟੈਕਚਰ ਅਧਿਆਇ ਨੂੰ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਇਸ ਦੇ ਸ਼ੁਰੂਆਤੀ ਭਾਗ ਵਿੱਚ ਅਜਿਹੀਆਂ ਲੋੜਾਂ ਸਨ ਜੋ ਘੇਰੇ ਤੋਂ ਬਾਹਰ ਸਨ, ਜਦਕਿ ਬਾਅਦ ਵਾਲੇ ਭਾਗਾਂ ਨੂੰ ਸੰਬੰਧਿਤ ਅਧਿਆਇਆਂ ਵਿੱਚ ਮੁੜ-ਵੰਡ ਦਿੱਤਾ ਗਿਆ ਹੈ, ਅਤੇ ਲੋੜਾਂ ਵਿੱਚੋਂ ਦੁਹਰਾਅ ਹਟਾ ਕੇ ਉਹਨਾਂ ਨੂੰ ਜ਼ਰੂਰਤ ਅਨੁਸਾਰ ਸਪੱਸ਼ਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## Removal of Direct Mappings to Other Standards
## ਹੋਰ ਮਿਆਰਾਂ ਨਾਲ ਸਿੱਧੀਆਂ ਮੈਪਿੰਗਾਂ ਦਾ ਹਟਾਇਆ ਜਾਣਾ

Direct mappings to other standards have been removed from the main body of the standard. The aim is to prepare a mapping with the OWASP Common Requirement Enumeration (CRE) project, which in turn will link ASVS to a range of OWASP projects and external standards.

ਮਿਆਰ ਦੇ ਮੁੱਖ ਭਾਗ ਵਿੱਚੋਂ ਹੋਰ ਮਿਆਰਾਂ ਨਾਲ ਸਿੱਧੀਆਂ ਮੈਪਿੰਗਾਂ ਹਟਾ ਦਿੱਤੀਆਂ ਗਈਆਂ ਹਨ। ਉਦੇਸ਼ OWASP Common Requirement Enumeration (CRE) ਪ੍ਰੋਜੈਕਟ ਨਾਲ ਇੱਕ ਮੈਪਿੰਗ ਤਿਆਰ ਕਰਨਾ ਹੈ, ਜੋ ਅੱਗੇ ASVS ਨੂੰ OWASP ਪ੍ਰੋਜੈਕਟਾਂ ਅਤੇ ਬਾਹਰੀ ਮਿਆਰਾਂ ਦੀ ਇੱਕ ਲੜੀ ਨਾਲ ਜੋੜੇਗੀ।

Direct mappings to CWE and NIST are no longer maintained, as explained below.

CWE ਅਤੇ NIST ਨਾਲ ਸਿੱਧੀਆਂ ਮੈਪਿੰਗਾਂ ਹੁਣ ਕਾਇਮ ਨਹੀਂ ਰੱਖੀਆਂ ਜਾਂਦੀਆਂ, ਜਿਵੇਂ ਕਿ ਹੇਠਾਂ ਸਮਝਾਇਆ ਗਿਆ ਹੈ।

### Reduced Coupling with NIST Digital Identity Guidelines
### NIST ਡਿਜੀਟਲ ਪਛਾਣ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਨਾਲ ਘਟਾਇਆ ਗਿਆ ਜੋੜ

The NIST [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) have long served as a reference for authentication and authorization controls. In version 4.x, certain chapters were closely aligned with NIST's structure and terminology.

NIST [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) ਲੰਬੇ ਸਮੇਂ ਤੋਂ ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਅਧਿਕਾਰੀਕਰਨ ਨਿਯੰਤਰਣਾਂ ਲਈ ਇੱਕ ਹਵਾਲੇ ਵਜੋਂ ਕੰਮ ਕਰਦੇ ਆਏ ਹਨ। ਸੰਸਕਰਣ 4.x ਵਿੱਚ, ਕੁਝ ਅਧਿਆਇ NIST ਦੀ ਬਣਤਰ ਅਤੇ ਸ਼ਬਦਾਵਲੀ ਨਾਲ ਨੇੜਿਓਂ ਜੁੜੇ ਹੋਏ ਸਨ।

While these guidelines remain an important reference, strict alignment introduced challenges, including less widely recognized terminology, duplication of similar requirements, and incomplete mappings. Version 5.0 moves away from this approach to improve clarity and relevance.

ਭਾਵੇਂ ਇਹ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਹਵਾਲਾ ਬਣੇ ਰਹਿੰਦੇ ਹਨ, ਸਖ਼ਤ ਇਕਸਾਰਤਾ ਨੇ ਚੁਣੌਤੀਆਂ ਪੈਦਾ ਕੀਤੀਆਂ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਘੱਟ ਵਿਆਪਕ ਤੌਰ 'ਤੇ ਮਾਨਤਾ-ਪ੍ਰਾਪਤ ਸ਼ਬਦਾਵਲੀ, ਮਿਲਦੀਆਂ-ਜੁਲਦੀਆਂ ਲੋੜਾਂ ਦਾ ਦੁਹਰਾਅ, ਅਤੇ ਅਧੂਰੀਆਂ ਮੈਪਿੰਗਾਂ ਸ਼ਾਮਲ ਹਨ। ਸੰਸਕਰਣ 5.0 ਸਪੱਸ਼ਟਤਾ ਅਤੇ ਪ੍ਰਸੰਗਿਕਤਾ ਨੂੰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ ਇਸ ਪਹੁੰਚ ਤੋਂ ਦੂਰ ਜਾਂਦਾ ਹੈ।

### Moving Away from Common Weakness Enumeration (CWE)
### Common Weakness Enumeration (CWE) ਤੋਂ ਦੂਰ ਜਾਣਾ

The [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) provides a useful taxonomy of software security weaknesses. However, challenges such as category-only CWEs, difficulties in mapping requirements to a single CWE, and the presence of imprecise mappings in version 4.x have led to the decision to discontinue direct CWE mappings in version 5.0.

[Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) ਸਾਫ਼ਟਵੇਅਰ ਸੁਰੱਖਿਆ ਖ਼ਾਮੀਆਂ (weaknesses) ਦਾ ਇੱਕ ਲਾਭਦਾਇਕ ਵਰਗੀਕਰਨ (taxonomy) ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਹਾਲਾਂਕਿ, ਸਿਰਫ਼-ਸ਼੍ਰੇਣੀ ਵਾਲੇ CWE, ਲੋੜਾਂ ਨੂੰ ਕਿਸੇ ਇੱਕ CWE ਨਾਲ ਮੈਪ ਕਰਨ ਵਿੱਚ ਮੁਸ਼ਕਲਾਂ, ਅਤੇ ਸੰਸਕਰਣ 4.x ਵਿੱਚ ਅਸ਼ੁੱਧ ਮੈਪਿੰਗਾਂ ਦੀ ਮੌਜੂਦਗੀ ਵਰਗੀਆਂ ਚੁਣੌਤੀਆਂ ਕਾਰਨ ਸੰਸਕਰਣ 5.0 ਵਿੱਚ ਸਿੱਧੀਆਂ CWE ਮੈਪਿੰਗਾਂ ਨੂੰ ਬੰਦ ਕਰਨ ਦਾ ਫ਼ੈਸਲਾ ਲਿਆ ਗਿਆ ਹੈ।

## Rethinking Level Definitions
## ਪੱਧਰ ਪਰਿਭਾਸ਼ਾਵਾਂ 'ਤੇ ਮੁੜ-ਵਿਚਾਰ

Version 4.x described the levels as L1 ("Minimum"), L2 ("Standard"), and L3 ("Advanced"), with the implication that all applications handling sensitive data should meet at least L2.

ਸੰਸਕਰਣ 4.x ਨੇ ਪੱਧਰਾਂ ਨੂੰ L1 ("ਘੱਟੋ-ਘੱਟ", Minimum), L2 ("ਮਿਆਰੀ", Standard), ਅਤੇ L3 ("ਉੱਨਤ", Advanced) ਵਜੋਂ ਵਰਣਿਤ ਕੀਤਾ ਸੀ, ਇਸ ਸੰਕੇਤ ਦੇ ਨਾਲ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਸੰਭਾਲਣ ਵਾਲੀਆਂ ਸਾਰੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਘੱਟੋ-ਘੱਟ L2 ਪੂਰਾ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।

Version 5.0 addresses several issues with this approach which are described in the following paragraphs.

ਸੰਸਕਰਣ 5.0 ਇਸ ਪਹੁੰਚ ਨਾਲ ਜੁੜੇ ਕਈ ਮੁੱਦਿਆਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਦਾ ਹੈ, ਜਿਨ੍ਹਾਂ ਦਾ ਵਰਣਨ ਅਗਲੇ ਪੈਰਿਆਂ ਵਿੱਚ ਕੀਤਾ ਗਿਆ ਹੈ।

As a practical matter, whereas version 4.x used tick marks for level indicators, 5.x uses a simple number on all formats of the standard including markdown, PDF, DOCX, CSV, JSON and XML. For backwards compatibility, legacy versions of the CSV, JSON and XML outputs which still use tick marks are also generated.

ਵਿਹਾਰਕ ਤੌਰ 'ਤੇ, ਜਿੱਥੇ ਸੰਸਕਰਣ 4.x ਪੱਧਰ ਸੂਚਕਾਂ ਲਈ ਟਿੱਕ ਚਿੰਨ੍ਹ ਵਰਤਦਾ ਸੀ, ਉੱਥੇ 5.x ਮਿਆਰ ਦੇ ਸਾਰੇ ਫਾਰਮੈਟਾਂ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ markdown, PDF, DOCX, CSV, JSON ਅਤੇ XML ਸ਼ਾਮਲ ਹਨ, ਵਿੱਚ ਇੱਕ ਸਧਾਰਨ ਅੰਕ ਵਰਤਦਾ ਹੈ। ਪਿਛਲੀ ਅਨੁਕੂਲਤਾ (backwards compatibility) ਲਈ, CSV, JSON ਅਤੇ XML ਆਊਟਪੁੱਟਾਂ ਦੇ ਪੁਰਾਣੇ (legacy) ਸੰਸਕਰਣ, ਜੋ ਅਜੇ ਵੀ ਟਿੱਕ ਚਿੰਨ੍ਹ ਵਰਤਦੇ ਹਨ, ਵੀ ਤਿਆਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

### Easier Entry Level
### ਸੌਖਾ ਪ੍ਰਵੇਸ਼ ਪੱਧਰ

Feedback indicated that the large number of Level 1 requirements (~120), combined with its designation as the "minimum" level that is not good enough for most applications, discouraged adoption. Version 5.0 aims to lower this barrier by defining Level 1 primarily around first-layer defense requirements, resulting in clearer and fewer requirements at that level. To demonstrate this numerically, in v4.0.3 there were 128 L1 requirements out of a total of 278 requirements, representing 46%. In 5.0.0 there are 70 L1 requirements out of a total of 345 requirements, representing 20%.

ਫ਼ੀਡਬੈਕ ਨੇ ਸੰਕੇਤ ਦਿੱਤਾ ਕਿ ਪੱਧਰ 1 ਦੀਆਂ ਲੋੜਾਂ ਦੀ ਵੱਡੀ ਗਿਣਤੀ (~120), ਇਸ ਦੇ "ਘੱਟੋ-ਘੱਟ" ਪੱਧਰ ਵਜੋਂ ਨਾਮਕਰਨ ਦੇ ਨਾਲ ਮਿਲ ਕੇ — ਜੋ ਜ਼ਿਆਦਾਤਰ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਕਾਫ਼ੀ ਚੰਗਾ ਨਹੀਂ ਹੈ — ਅਪਣਾਏ ਜਾਣ ਨੂੰ ਨਿਰਉਤਸ਼ਾਹਿਤ ਕਰਦੀ ਸੀ। ਸੰਸਕਰਣ 5.0 ਦਾ ਉਦੇਸ਼ ਪੱਧਰ 1 ਨੂੰ ਮੁੱਖ ਤੌਰ 'ਤੇ ਪਹਿਲੀ-ਪਰਤ ਰੱਖਿਆ ਲੋੜਾਂ ਦੁਆਲੇ ਪਰਿਭਾਸ਼ਿਤ ਕਰਕੇ ਇਸ ਰੁਕਾਵਟ ਨੂੰ ਘਟਾਉਣਾ ਹੈ, ਜਿਸ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਉਸ ਪੱਧਰ 'ਤੇ ਵਧੇਰੇ ਸਪੱਸ਼ਟ ਅਤੇ ਘੱਟ ਲੋੜਾਂ ਹਨ। ਇਸ ਨੂੰ ਅੰਕੜਿਆਂ ਵਿੱਚ ਦਰਸਾਉਣ ਲਈ, v4.0.3 ਵਿੱਚ ਕੁੱਲ 278 ਲੋੜਾਂ ਵਿੱਚੋਂ 128 L1 ਲੋੜਾਂ ਸਨ, ਜੋ 46% ਬਣਦੀਆਂ ਹਨ। 5.0.0 ਵਿੱਚ ਕੁੱਲ 345 ਲੋੜਾਂ ਵਿੱਚੋਂ 70 L1 ਲੋੜਾਂ ਹਨ, ਜੋ 20% ਬਣਦੀਆਂ ਹਨ।

### The Fallacy of Testability
### ਟੈਸਟਯੋਗਤਾ ਦਾ ਭੁਲੇਖਾ

A key factor in selecting controls for Level 1 in version 4.x was their suitability for assessment through "black box" external penetration testing. However, this approach was not fully aligned with the intent of Level 1 as the minimum set of security controls. Some users argued that Level 1 was insufficient for securing applications, while others found it too difficult to test.

ਸੰਸਕਰਣ 4.x ਵਿੱਚ ਪੱਧਰ 1 ਲਈ ਨਿਯੰਤਰਣ ਚੁਣਨ ਵਿੱਚ ਇੱਕ ਮੁੱਖ ਕਾਰਕ "ਬਲੈਕ ਬਾਕਸ" ਬਾਹਰੀ ਪੈਨੇਟ੍ਰੇਸ਼ਨ ਟੈਸਟਿੰਗ (penetration testing) ਰਾਹੀਂ ਮੁਲਾਂਕਣ ਲਈ ਉਹਨਾਂ ਦੀ ਅਨੁਕੂਲਤਾ ਸੀ। ਹਾਲਾਂਕਿ, ਇਹ ਪਹੁੰਚ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ ਦੇ ਘੱਟੋ-ਘੱਟ ਸਮੂਹ ਵਜੋਂ ਪੱਧਰ 1 ਦੇ ਇਰਾਦੇ ਨਾਲ ਪੂਰੀ ਤਰ੍ਹਾਂ ਮੇਲ ਨਹੀਂ ਖਾਂਦੀ ਸੀ। ਕੁਝ ਵਰਤੋਂਕਾਰਾਂ ਨੇ ਦਲੀਲ ਦਿੱਤੀ ਕਿ ਪੱਧਰ 1 ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਨਾਕਾਫ਼ੀ ਸੀ, ਜਦਕਿ ਹੋਰਾਂ ਨੂੰ ਇਸ ਦੀ ਟੈਸਟਿੰਗ ਬਹੁਤ ਮੁਸ਼ਕਲ ਲੱਗੀ।

Relying on testability as a criterion is both relative and, at times, misleading. The fact that a requirement is testable does not guarantee that it can be tested in an automated or straightforward manner. Moreover, the most easily testable requirements are not always those with the greatest security impact or the simplest to implement.

ਟੈਸਟਯੋਗਤਾ (testability) 'ਤੇ ਇੱਕ ਕਸੌਟੀ ਵਜੋਂ ਨਿਰਭਰ ਕਰਨਾ ਸਾਪੇਖਿਕ ਵੀ ਹੈ ਅਤੇ, ਕਈ ਵਾਰ, ਗੁਮਰਾਹਕੁੰਨ ਵੀ। ਇਹ ਤੱਥ ਕਿ ਕੋਈ ਲੋੜ ਟੈਸਟਯੋਗ ਹੈ, ਇਸ ਗੱਲ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ ਦਿੰਦਾ ਕਿ ਇਸ ਦੀ ਟੈਸਟਿੰਗ ਸਵੈਚਾਲਿਤ ਜਾਂ ਸਿੱਧੇ-ਸਾਦੇ ਢੰਗ ਨਾਲ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਇਸ ਤੋਂ ਇਲਾਵਾ, ਸਭ ਤੋਂ ਸੌਖਿਆਂ ਟੈਸਟਯੋਗ ਲੋੜਾਂ ਹਮੇਸ਼ਾ ਉਹ ਨਹੀਂ ਹੁੰਦੀਆਂ ਜਿਨ੍ਹਾਂ ਦਾ ਸੁਰੱਖਿਆ ਪ੍ਰਭਾਵ ਸਭ ਤੋਂ ਵੱਧ ਹੋਵੇ ਜਾਂ ਜਿਨ੍ਹਾਂ ਨੂੰ ਲਾਗੂ ਕਰਨਾ ਸਭ ਤੋਂ ਸਰਲ ਹੋਵੇ।

As such, in version 5.0, the level decisions were made primarily based on risk reduction and also keeping in mind the effort to implement.

ਇਸ ਲਈ, ਸੰਸਕਰਣ 5.0 ਵਿੱਚ, ਪੱਧਰ ਦੇ ਫ਼ੈਸਲੇ ਮੁੱਖ ਤੌਰ 'ਤੇ ਜੋਖਮ ਘਟਾਉਣ ਦੇ ਆਧਾਰ 'ਤੇ ਲਏ ਗਏ ਸਨ, ਅਤੇ ਨਾਲ ਹੀ ਲਾਗੂ ਕਰਨ ਦੇ ਯਤਨ ਨੂੰ ਵੀ ਧਿਆਨ ਵਿੱਚ ਰੱਖਿਆ ਗਿਆ ਸੀ।

### Not Just About Risk
### ਸਿਰਫ਼ ਜੋਖਮ ਦੀ ਗੱਲ ਨਹੀਂ

The use of prescriptive, risk-based levels that mandate a specific level for certain applications has proven to be overly rigid. In practice, the prioritization and implementation of security controls depend on multiple factors, including both risk reduction and the effort required for implementation.

ਨਿਰਦੇਸ਼ਾਤਮਕ, ਜੋਖਮ-ਆਧਾਰਿਤ ਪੱਧਰਾਂ ਦੀ ਵਰਤੋਂ, ਜੋ ਕੁਝ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਇੱਕ ਖ਼ਾਸ ਪੱਧਰ ਨੂੰ ਲਾਜ਼ਮੀ ਬਣਾਉਂਦੇ ਹਨ, ਬਹੁਤ ਜ਼ਿਆਦਾ ਸਖ਼ਤ ਸਾਬਤ ਹੋਈ ਹੈ। ਅਮਲ ਵਿੱਚ, ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ ਦੀ ਤਰਜੀਹ ਅਤੇ ਲਾਗੂਕਰਨ ਕਈ ਕਾਰਕਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਜੋਖਮ ਘਟਾਉਣਾ ਅਤੇ ਲਾਗੂਕਰਨ ਲਈ ਲੋੜੀਂਦਾ ਯਤਨ ਦੋਵੇਂ ਸ਼ਾਮਲ ਹਨ।

Therefore, organizations are encouraged to achieve the level that they feel like they should be achieving based on their maturity and the message they want to send to their users.

ਇਸ ਲਈ, ਸੰਸਥਾਵਾਂ ਨੂੰ ਉਹ ਪੱਧਰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ ਉਹਨਾਂ ਨੂੰ ਆਪਣੀ ਪਰਿਪੱਕਤਾ ਅਤੇ ਉਸ ਸੰਦੇਸ਼ ਦੇ ਆਧਾਰ 'ਤੇ, ਜੋ ਉਹ ਆਪਣੇ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਦੇਣਾ ਚਾਹੁੰਦੀਆਂ ਹਨ, ਲੱਗਦਾ ਹੈ ਕਿ ਉਹਨਾਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।
