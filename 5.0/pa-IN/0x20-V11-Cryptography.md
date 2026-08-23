<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x20-V11-Cryptography.md -->
<!-- Translator: GeeksikhSecurity -->

# V11 Cryptography
# V11 ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

The objective of this chapter is to define best practices for the general use of cryptography, as well as to instill a fundamental understanding of cryptographic principles and inspire a shift toward more resilient and modern approaches. It encourages the following:

ਇਸ ਅਧਿਆਇ ਦਾ ਉਦੇਸ਼ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ (cryptography) ਦੀ ਆਮ ਵਰਤੋਂ ਲਈ ਸਭ ਤੋਂ ਚੰਗੇ ਅਮਲਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਹੈ, ਨਾਲ ਹੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਸਿਧਾਂਤਾਂ ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ ਪੈਦਾ ਕਰਨਾ ਅਤੇ ਵਧੇਰੇ ਲਚਕੀਲੀਆਂ ਅਤੇ ਆਧੁਨਿਕ ਪਹੁੰਚਾਂ ਵੱਲ ਤਬਦੀਲੀ ਨੂੰ ਪ੍ਰੇਰਿਤ ਕਰਨਾ ਹੈ। ਇਹ ਹੇਠ ਲਿਖਿਆਂ ਨੂੰ ਉਤਸ਼ਾਹਿਤ ਕਰਦਾ ਹੈ:

* Implementing robust cryptographic systems that fail securely, adapt to evolving threats, and are future-proof.
* Utilizing cryptographic mechanisms that are both secure and aligned with industry best practices.
* Maintaining a secure cryptographic key management system with appropriate access controls and auditing.
* Regularly evaluating the cryptographic landscape to assess new risks and adapt algorithms accordingly.
* Discovering and managing cryptographic use cases throughout the application's lifecycle to ensure that all cryptographic assets are accounted for and secured.

* ਮਜ਼ਬੂਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਸਿਸਟਮ ਲਾਗੂ ਕਰਨਾ ਜੋ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਅਸਫਲ ਹੁੰਦੇ ਹਨ (fail securely), ਬਦਲਦੇ ਖ਼ਤਰਿਆਂ ਅਨੁਸਾਰ ਢਲਦੇ ਹਨ, ਅਤੇ ਭਵਿੱਖ-ਸੁਰੱਖਿਅਤ (future-proof) ਹਨ।
* ਅਜਿਹੀਆਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਜੋ ਸੁਰੱਖਿਅਤ ਵੀ ਹਨ ਅਤੇ ਉਦਯੋਗ ਦੇ ਸਭ ਤੋਂ ਚੰਗੇ ਅਮਲਾਂ ਨਾਲ ਮੇਲ ਵੀ ਖਾਂਦੀਆਂ ਹਨ।
* ਢੁਕਵੇਂ ਪਹੁੰਚ ਨਿਯੰਤਰਣਾਂ ਅਤੇ ਆਡਿਟਿੰਗ ਦੇ ਨਾਲ ਇੱਕ ਸੁਰੱਖਿਅਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀ ਪ੍ਰਬੰਧਨ ਸਿਸਟਮ ਬਣਾਈ ਰੱਖਣਾ।
* ਨਵੇਂ ਜੋਖਮਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਅਤੇ ਉਸ ਅਨੁਸਾਰ ਐਲਗੋਰਿਦਮਾਂ ਨੂੰ ਢਾਲਣ ਲਈ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਹਾਲਾਤ ਦਾ ਨਿਯਮਿਤ ਮੁਲਾਂਕਣ ਕਰਨਾ।
* ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਪੂਰੇ ਜੀਵਨ-ਚੱਕਰ ਦੌਰਾਨ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਵਰਤੋਂ ਦੇ ਮਾਮਲਿਆਂ ਦੀ ਖੋਜ ਅਤੇ ਪ੍ਰਬੰਧਨ ਕਰਨਾ ਤਾਂ ਜੋ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਸਾਰੀਆਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਸੰਪਤੀਆਂ ਦਾ ਲੇਖਾ-ਜੋਖਾ ਰੱਖਿਆ ਗਿਆ ਹੈ ਅਤੇ ਉਹ ਸੁਰੱਖਿਅਤ ਹਨ।

In addition to outlining general principles and best practices, this document also provides more in-depth technical information about the requirements in Appendix C - Cryptography Standards. This includes algorithms and modes that are considered "approved" for the purposes of the requirements in this chapter.

ਆਮ ਸਿਧਾਂਤਾਂ ਅਤੇ ਸਭ ਤੋਂ ਚੰਗੇ ਅਮਲਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦੇਣ ਤੋਂ ਇਲਾਵਾ, ਇਹ ਦਸਤਾਵੇਜ਼ ਅੰਤਿਕਾ C — ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਮਿਆਰਾਂ ਵਿੱਚ ਲੋੜਾਂ ਬਾਰੇ ਵਧੇਰੇ ਡੂੰਘੀ ਤਕਨੀਕੀ ਜਾਣਕਾਰੀ ਵੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਉਹ ਐਲਗੋਰਿਦਮ ਅਤੇ ਮੋਡ ਸ਼ਾਮਲ ਹਨ ਜੋ ਇਸ ਅਧਿਆਇ ਦੀਆਂ ਲੋੜਾਂ ਦੇ ਮੰਤਵਾਂ ਲਈ "ਪ੍ਰਵਾਨਿਤ" (approved) ਮੰਨੇ ਜਾਂਦੇ ਹਨ।

Requirements that use cryptography to solve a separate problem, such as secrets management or communications security, will be in different parts of the standard.

ਉਹ ਲੋੜਾਂ ਜੋ ਕਿਸੇ ਵੱਖਰੀ ਸਮੱਸਿਆ, ਜਿਵੇਂ ਕਿ ਭੇਦ ਪ੍ਰਬੰਧਨ ਜਾਂ ਸੰਚਾਰ ਸੁਰੱਖਿਆ, ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ, ਮਿਆਰ ਦੇ ਵੱਖ-ਵੱਖ ਭਾਗਾਂ ਵਿੱਚ ਹੋਣਗੀਆਂ।

## V11.1 Cryptographic Inventory and Documentation
## V11.1 ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਇਨਵੈਂਟਰੀ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

Applications need to be designed with strong cryptographic architecture to protect data assets according to their classification. Encrypting everything is wasteful; not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high-level design, design sprints, or architectural spikes. Designing cryptography "on the fly" or retrofitting it will inevitably cost much more to implement securely than simply building it in from the start.

ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਡਾਟਾ ਸੰਪਤੀਆਂ ਨੂੰ ਉਹਨਾਂ ਦੇ ਵਰਗੀਕਰਨ ਅਨੁਸਾਰ ਸੁਰੱਖਿਅਤ ਰੱਖਣ ਲਈ ਮਜ਼ਬੂਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਆਰਕੀਟੈਕਚਰ ਨਾਲ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਜਾਣ ਦੀ ਲੋੜ ਹੈ। ਹਰ ਚੀਜ਼ ਨੂੰ ਏਨਕ੍ਰਿਪਟ ਕਰਨਾ ਫ਼ਜ਼ੂਲ ਹੈ; ਕਿਸੇ ਵੀ ਚੀਜ਼ ਨੂੰ ਏਨਕ੍ਰਿਪਟ ਨਾ ਕਰਨਾ ਕਾਨੂੰਨੀ ਤੌਰ 'ਤੇ ਲਾਪਰਵਾਹੀ ਹੈ। ਇੱਕ ਸੰਤੁਲਨ ਬਣਾਉਣਾ ਲਾਜ਼ਮੀ ਹੈ, ਆਮ ਤੌਰ 'ਤੇ ਆਰਕੀਟੈਕਚਰਲ ਜਾਂ ਉੱਚ-ਪੱਧਰੀ ਡਿਜ਼ਾਈਨ, ਡਿਜ਼ਾਈਨ ਸਪ੍ਰਿੰਟਾਂ, ਜਾਂ ਆਰਕੀਟੈਕਚਰਲ ਸਪਾਈਕਾਂ (architectural spikes) ਦੌਰਾਨ। ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਨੂੰ "ਮੌਕੇ 'ਤੇ" ਡਿਜ਼ਾਈਨ ਕਰਨਾ ਜਾਂ ਇਸਨੂੰ ਬਾਅਦ ਵਿੱਚ ਜੋੜਨਾ (retrofitting), ਇਸਨੂੰ ਸ਼ੁਰੂ ਤੋਂ ਹੀ ਬਣਾ ਕੇ ਰੱਖਣ ਦੇ ਮੁਕਾਬਲੇ, ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਲਾਗੂ ਕਰਨ ਲਈ ਅਟੱਲ ਤੌਰ 'ਤੇ ਕਿਤੇ ਵੱਧ ਮਹਿੰਗਾ ਪਵੇਗਾ।

It is important to ensure that all cryptographic assets are regularly discovered, inventoried, and assessed. Please see the appendix for more information on how this can be done.

ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਸਾਰੀਆਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਸੰਪਤੀਆਂ ਦੀ ਨਿਯਮਿਤ ਤੌਰ 'ਤੇ ਖੋਜ ਕੀਤੀ ਜਾਵੇ, ਉਹਨਾਂ ਨੂੰ ਇਨਵੈਂਟਰੀ (inventory) ਵਿੱਚ ਦਰਜ ਕੀਤਾ ਜਾਵੇ, ਅਤੇ ਉਹਨਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕੀਤਾ ਜਾਵੇ। ਇਹ ਕਿਵੇਂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਇਸ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਅੰਤਿਕਾ ਵੇਖੋ।

The need to future-proof cryptographic systems against the eventual rise of quantum computing is also critical. Post-Quantum Cryptography (PQC) refers to cryptographic algorithms designed to remain secure against attacks by quantum computers, which are expected to break widely used algorithms such as RSA and elliptic curve cryptography (ECC).

ਕੁਆਂਟਮ ਕੰਪਿਊਟਿੰਗ (quantum computing) ਦੇ ਅੰਤਮ ਉਭਾਰ ਦੇ ਵਿਰੁੱਧ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਸਿਸਟਮਾਂ ਨੂੰ ਭਵਿੱਖ-ਸੁਰੱਖਿਅਤ ਬਣਾਉਣ ਦੀ ਲੋੜ ਵੀ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਪੋਸਟ-ਕੁਆਂਟਮ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ (Post-Quantum Cryptography, PQC) ਉਹਨਾਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਐਲਗੋਰਿਦਮਾਂ ਨੂੰ ਦਰਸਾਉਂਦੀ ਹੈ ਜੋ ਕੁਆਂਟਮ ਕੰਪਿਊਟਰਾਂ ਦੁਆਰਾ ਹਮਲਿਆਂ ਦੇ ਵਿਰੁੱਧ ਸੁਰੱਖਿਅਤ ਰਹਿਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਗਏ ਹਨ; ਕੁਆਂਟਮ ਕੰਪਿਊਟਰਾਂ ਤੋਂ RSA ਅਤੇ ਅੰਡਾਕਾਰ ਵਕਰ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ (elliptic curve cryptography, ECC) ਵਰਗੇ ਵਿਆਪਕ ਤੌਰ 'ਤੇ ਵਰਤੇ ਜਾਂਦੇ ਐਲਗੋਰਿਦਮਾਂ ਨੂੰ ਤੋੜਨ ਦੀ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

Please see the appendix for current guidance on vetted PQC primitives and standards.

ਜਾਂਚੇ-ਪਰਖੇ PQC ਪ੍ਰਿਮਿਟਿਵਾਂ (primitives) ਅਤੇ ਮਿਆਰਾਂ ਬਾਰੇ ਮੌਜੂਦਾ ਮਾਰਗਦਰਸ਼ਨ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਅੰਤਿਕਾ ਵੇਖੋ।

| # | Description | Level |
| :---: | :--- | :---: |
| **11.1.1** | Verify that there is a documented policy for management of cryptographic keys and a cryptographic key lifecycle that follows a key management standard such as NIST SP 800-57. This should include ensuring that keys are not overshared (for example, with more than two entities for shared secrets and more than one entity for private keys). | 2 |
| **11.1.2** | Verify that a cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. It must also document where keys can and cannot be used in the system, and the types of data that can and cannot be protected using the keys. | 2 |
| **11.1.3** | Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations. | 3 |
| **11.1.4** | Verify that a cryptographic inventory is maintained. This must include a documented plan that outlines the migration path to new cryptographic standards, such as post-quantum cryptography, in order to react to future threats. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **11.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀਆਂ ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ ਇੱਕ ਦਸਤਾਵੇਜ਼ੀ ਨੀਤੀ ਅਤੇ ਇੱਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀ ਜੀਵਨ-ਚੱਕਰ ਮੌਜੂਦ ਹੈ ਜੋ NIST SP 800-57 ਵਰਗੇ ਕੁੰਜੀ ਪ੍ਰਬੰਧਨ ਮਿਆਰ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਕੁੰਜੀਆਂ ਲੋੜ ਤੋਂ ਵੱਧ ਸਾਂਝੀਆਂ ਨਾ ਕੀਤੀਆਂ ਜਾਣ (ਉਦਾਹਰਨ ਲਈ, ਸਾਂਝੇ ਭੇਦਾਂ ਲਈ ਦੋ ਤੋਂ ਵੱਧ ਇਕਾਈਆਂ ਨਾਲ ਅਤੇ ਨਿੱਜੀ ਕੁੰਜੀਆਂ ਲਈ ਇੱਕ ਤੋਂ ਵੱਧ ਇਕਾਈ ਨਾਲ)। | 2 |
| **11.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਇਨਵੈਂਟਰੀ ਤਿਆਰ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਬਣਾਈ ਰੱਖੀ ਜਾਂਦੀ ਹੈ, ਨਿਯਮਿਤ ਤੌਰ 'ਤੇ ਅੱਪਡੇਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ ਇਸ ਵਿੱਚ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ ਸਾਰੀਆਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀਆਂ, ਐਲਗੋਰਿਦਮ, ਅਤੇ ਸਰਟੀਫ਼ਿਕੇਟ ਸ਼ਾਮਲ ਹਨ। ਇਸ ਵਿੱਚ ਇਹ ਵੀ ਦਸਤਾਵੇਜ਼ ਕੀਤਾ ਜਾਣਾ ਲਾਜ਼ਮੀ ਹੈ ਕਿ ਸਿਸਟਮ ਵਿੱਚ ਕੁੰਜੀਆਂ ਕਿੱਥੇ ਵਰਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ ਅਤੇ ਕਿੱਥੇ ਨਹੀਂ, ਅਤੇ ਕੁੰਜੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਿਸ ਕਿਸਮ ਦੇ ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਕਿਸ ਨੂੰ ਨਹੀਂ। | 2 |
| **11.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਸਟਮ ਵਿੱਚ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਦੀ ਵਰਤੋਂ ਦੀਆਂ ਸਾਰੀਆਂ ਮਿਸਾਲਾਂ (instances) ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਖੋਜ ਪ੍ਰਣਾਲੀਆਂ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਜਿਸ ਵਿੱਚ ਏਨਕ੍ਰਿਪਸ਼ਨ, ਹੈਸ਼ਿੰਗ, ਅਤੇ ਦਸਤਖ਼ਤ ਕਰਨ ਦੀਆਂ ਕਾਰਵਾਈਆਂ ਸ਼ਾਮਲ ਹਨ। | 3 |
| **11.1.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਇਨਵੈਂਟਰੀ ਬਣਾਈ ਰੱਖੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਵਿੱਚ ਇੱਕ ਦਸਤਾਵੇਜ਼ੀ ਯੋਜਨਾ ਸ਼ਾਮਲ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ ਜੋ ਭਵਿੱਖ ਦੇ ਖ਼ਤਰਿਆਂ ਪ੍ਰਤੀ ਪ੍ਰਤੀਕਿਰਿਆ ਕਰਨ ਲਈ, ਨਵੇਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਮਿਆਰਾਂ, ਜਿਵੇਂ ਕਿ ਪੋਸਟ-ਕੁਆਂਟਮ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ, ਵੱਲ ਮਾਈਗ੍ਰੇਸ਼ਨ ਮਾਰਗ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦੀ ਹੈ। | 3 |

## V11.2 Secure Cryptography Implementation
## V11.2 ਸੁਰੱਖਿਅਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਲਾਗੂਕਰਨ

This section defines the requirements for the selection, implementation, and ongoing management of core cryptographic algorithms for an application. The objective is to ensure that only robust, industry-accepted cryptographic primitives are deployed, in alignment with current standards (e.g., NIST, ISO/IEC) and best practices. Organizations must ensure that each cryptographic component is selected based on peer-reviewed evidence and practical security testing.

ਇਹ ਭਾਗ ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਮੁੱਖ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਐਲਗੋਰਿਦਮਾਂ ਦੀ ਚੋਣ, ਲਾਗੂਕਰਨ, ਅਤੇ ਨਿਰੰਤਰ ਪ੍ਰਬੰਧਨ ਲਈ ਲੋੜਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ। ਉਦੇਸ਼ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਮੌਜੂਦਾ ਮਿਆਰਾਂ (ਜਿਵੇਂ, NIST, ISO/IEC) ਅਤੇ ਸਭ ਤੋਂ ਚੰਗੇ ਅਮਲਾਂ ਦੇ ਅਨੁਸਾਰ, ਸਿਰਫ਼ ਮਜ਼ਬੂਤ, ਉਦਯੋਗ-ਪ੍ਰਵਾਨਿਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਿਮਿਟਿਵ ਹੀ ਤਾਇਨਾਤ ਕੀਤੇ ਜਾਣ। ਸੰਸਥਾਵਾਂ ਲਈ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਲਾਜ਼ਮੀ ਹੈ ਕਿ ਹਰੇਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਹਿੱਸੇ ਦੀ ਚੋਣ ਸਾਥੀ-ਸਮੀਖਿਅਤ (peer-reviewed) ਸਬੂਤਾਂ ਅਤੇ ਵਿਹਾਰਕ ਸੁਰੱਖਿਆ ਟੈਸਟਿੰਗ ਦੇ ਆਧਾਰ 'ਤੇ ਕੀਤੀ ਜਾਵੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **11.2.1** | Verify that industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations. | 2 |
| **11.2.2** | Verify that the application is designed with crypto agility such that random number, authenticated encryption, MAC, or hashing algorithms, key lengths, rounds, ciphers and modes can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. Similarly, it must also be possible to replace keys and passwords and re-encrypt data. This will allow for seamless upgrades to post-quantum cryptography (PQC), once high-assurance implementations of approved PQC schemes or standards are widely available. | 2 |
| **11.2.3** | Verify that all cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration. For example, a 256-bit ECC key provides roughly 128 bits of security where RSA requires a 3072-bit key to achieve 128 bits of security. | 2 |
| **11.2.4** | Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information. | 3 |
| **11.2.5** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **11.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕਾਰਵਾਈਆਂ ਲਈ ਉਦਯੋਗ-ਪ੍ਰਮਾਣਿਤ ਲਾਗੂਕਰਨ (ਲਾਇਬ੍ਰੇਰੀਆਂ ਅਤੇ ਹਾਰਡਵੇਅਰ-ਤੇਜ਼ ਕੀਤੇ ਲਾਗੂਕਰਨਾਂ ਸਮੇਤ) ਵਰਤੇ ਜਾਂਦੇ ਹਨ। | 2 |
| **11.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਕ੍ਰਿਪਟੋ ਚੁਸਤੀ (crypto agility) ਨਾਲ ਇਸ ਤਰ੍ਹਾਂ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ ਬੇਤਰਤੀਬ ਨੰਬਰ, ਪ੍ਰਮਾਣੀਕ੍ਰਿਤ ਏਨਕ੍ਰਿਪਸ਼ਨ (authenticated encryption), MAC, ਜਾਂ ਹੈਸ਼ਿੰਗ ਐਲਗੋਰਿਦਮ, ਕੁੰਜੀ ਲੰਬਾਈਆਂ, ਰਾਊਂਡ, ਸਾਈਫ਼ਰ ਅਤੇ ਮੋਡ ਨੂੰ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਟੁੱਟਣ (cryptographic breaks) ਤੋਂ ਬਚਾਅ ਲਈ ਕਿਸੇ ਵੀ ਸਮੇਂ ਮੁੜ-ਸੰਰਚਿਤ, ਅੱਪਗ੍ਰੇਡ, ਜਾਂ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਸੇ ਤਰ੍ਹਾਂ, ਕੁੰਜੀਆਂ ਅਤੇ ਪਾਸਵਰਡਾਂ ਨੂੰ ਬਦਲਣਾ ਅਤੇ ਡਾਟੇ ਨੂੰ ਮੁੜ-ਏਨਕ੍ਰਿਪਟ ਕਰਨਾ ਵੀ ਸੰਭਵ ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ। ਇਹ ਪੋਸਟ-ਕੁਆਂਟਮ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ (PQC) ਵੱਲ ਨਿਰਵਿਘਨ ਅੱਪਗ੍ਰੇਡਾਂ ਦੀ ਆਗਿਆ ਦੇਵੇਗਾ, ਜਦੋਂ ਪ੍ਰਵਾਨਿਤ PQC ਸਕੀਮਾਂ ਜਾਂ ਮਿਆਰਾਂ ਦੇ ਉੱਚ-ਭਰੋਸੇ ਵਾਲੇ ਲਾਗੂਕਰਨ ਵਿਆਪਕ ਤੌਰ 'ਤੇ ਉਪਲਬਧ ਹੋ ਜਾਣ। | 2 |
| **11.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਿਮਿਟਿਵ ਐਲਗੋਰਿਦਮ, ਕੁੰਜੀ ਆਕਾਰ, ਅਤੇ ਸੰਰਚਨਾ ਦੇ ਆਧਾਰ 'ਤੇ ਘੱਟੋ-ਘੱਟ 128-ਬਿੱਟ ਸੁਰੱਖਿਆ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ। ਉਦਾਹਰਨ ਲਈ, ਇੱਕ 256-ਬਿੱਟ ECC ਕੁੰਜੀ ਲਗਭਗ 128 ਬਿੱਟ ਸੁਰੱਖਿਆ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ, ਜਦੋਂ ਕਿ RSA ਨੂੰ 128 ਬਿੱਟ ਸੁਰੱਖਿਆ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ 3072-ਬਿੱਟ ਕੁੰਜੀ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। | 2 |
| **11.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਾਣਕਾਰੀ ਲੀਕ ਹੋਣ ਤੋਂ ਬਚਣ ਲਈ, ਸਾਰੀਆਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕਾਰਵਾਈਆਂ ਸਥਿਰ-ਸਮਾਂ (constant-time) ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਤੁਲਨਾਵਾਂ, ਗਣਨਾਵਾਂ, ਜਾਂ ਰਿਟਰਨਾਂ ਵਿੱਚ ਕੋਈ 'ਸ਼ਾਰਟ-ਸਰਕਟ' ਕਾਰਵਾਈਆਂ ਨਹੀਂ ਹਨ। | 3 |
| **11.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਮਾਡਿਊਲ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਅਸਫਲ ਹੁੰਦੇ ਹਨ, ਅਤੇ ਗਲਤੀਆਂ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ ਜੋ ਕਮਜ਼ੋਰੀਆਂ, ਜਿਵੇਂ ਕਿ ਪੈਡਿੰਗ ਓਰੇਕਲ (Padding Oracle) ਹਮਲਿਆਂ, ਨੂੰ ਸਮਰੱਥ ਨਹੀਂ ਬਣਾਉਂਦਾ। | 3 |

## V11.3 Encryption Algorithms
## V11.3 ਏਨਕ੍ਰਿਪਸ਼ਨ ਐਲਗੋਰਿਦਮ

Authenticated encryption algorithms built on AES and CHACHA20 form the backbone of modern cryptographic practice.

AES ਅਤੇ CHACHA20 'ਤੇ ਬਣੇ ਪ੍ਰਮਾਣੀਕ੍ਰਿਤ ਏਨਕ੍ਰਿਪਸ਼ਨ ਐਲਗੋਰਿਦਮ ਆਧੁਨਿਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਅਮਲ ਦੀ ਰੀੜ੍ਹ ਦੀ ਹੱਡੀ ਬਣਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **11.3.1** | Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used. | 1 |
| **11.3.2** | Verify that only approved ciphers and modes such as AES with GCM are used. | 1 |
| **11.3.3** | Verify that encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved MAC algorithm. | 2 |
| **11.3.4** | Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used. | 3 |
| **11.3.5** | Verify that any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **11.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅਸੁਰੱਖਿਅਤ ਬਲਾਕ ਮੋਡ (ਜਿਵੇਂ, ECB) ਅਤੇ ਕਮਜ਼ੋਰ ਪੈਡਿੰਗ ਸਕੀਮਾਂ (ਜਿਵੇਂ, PKCS#1 v1.5) ਨਹੀਂ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ। | 1 |
| **11.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਰਫ਼ ਪ੍ਰਵਾਨਿਤ ਸਾਈਫ਼ਰ ਅਤੇ ਮੋਡ, ਜਿਵੇਂ ਕਿ GCM ਦੇ ਨਾਲ AES, ਹੀ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। | 1 |
| **11.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਏਨਕ੍ਰਿਪਟ ਕੀਤਾ ਡਾਟਾ ਅਣਅਧਿਕਾਰਤ ਸੋਧ ਤੋਂ ਸੁਰੱਖਿਅਤ ਹੈ, ਤਰਜੀਹੀ ਤੌਰ 'ਤੇ ਇੱਕ ਪ੍ਰਵਾਨਿਤ ਪ੍ਰਮਾਣੀਕ੍ਰਿਤ ਏਨਕ੍ਰਿਪਸ਼ਨ ਵਿਧੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਾਂ ਇੱਕ ਪ੍ਰਵਾਨਿਤ ਏਨਕ੍ਰਿਪਸ਼ਨ ਵਿਧੀ ਨੂੰ ਇੱਕ ਪ੍ਰਵਾਨਿਤ MAC ਐਲਗੋਰਿਦਮ ਨਾਲ ਜੋੜ ਕੇ। | 2 |
| **11.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਨੌਂਸ (nonce), ਸ਼ੁਰੂਆਤੀ ਵੈਕਟਰ (initialization vector, IV), ਅਤੇ ਹੋਰ ਇੱਕ-ਵਾਰੀ-ਵਰਤੋਂ ਵਾਲੇ ਨੰਬਰ ਇੱਕ ਤੋਂ ਵੱਧ ਏਨਕ੍ਰਿਪਸ਼ਨ ਕੁੰਜੀ ਅਤੇ ਡਾਟਾ-ਤੱਤ ਜੋੜੇ ਲਈ ਨਹੀਂ ਵਰਤੇ ਜਾਂਦੇ। ਉਤਪਾਦਨ ਦੀ ਵਿਧੀ ਵਰਤੇ ਜਾ ਰਹੇ ਐਲਗੋਰਿਦਮ ਲਈ ਢੁਕਵੀਂ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ। | 3 |
| **11.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਏਨਕ੍ਰਿਪਸ਼ਨ ਐਲਗੋਰਿਦਮ ਅਤੇ ਇੱਕ MAC ਐਲਗੋਰਿਦਮ ਦਾ ਕੋਈ ਵੀ ਸੁਮੇਲ encrypt-then-MAC ਮੋਡ ਵਿੱਚ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ। | 3 |

## V11.4 Hashing and Hash-based Functions
## V11.4 ਹੈਸ਼ਿੰਗ ਅਤੇ ਹੈਸ਼-ਆਧਾਰਿਤ ਫੰਕਸ਼ਨ

Cryptographic hashes are used in a wide variety of cryptographic protocols, such as digital signatures, HMAC, key derivation functions (KDF), random bit generation, and password storage. The security of the cryptographic system is only as strong as the underlying hash functions used. This section outlines the requirements for using secure hash functions in cryptographic operations.

ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਹੈਸ਼ (hash) ਕਈ ਤਰ੍ਹਾਂ ਦੇ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰੋਟੋਕਾਲਾਂ ਵਿੱਚ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਡਿਜ਼ੀਟਲ ਦਸਤਖ਼ਤ, HMAC, ਕੁੰਜੀ-ਵਿਉਤਪੱਤੀ ਫੰਕਸ਼ਨ (key derivation function, KDF), ਬੇਤਰਤੀਬ ਬਿੱਟ ਉਤਪਾਦਨ, ਅਤੇ ਪਾਸਵਰਡ ਸਟੋਰੇਜ। ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਸਿਰਫ਼ ਓਨੀ ਹੀ ਮਜ਼ਬੂਤ ਹੁੰਦੀ ਹੈ ਜਿੰਨੇ ਵਰਤੇ ਗਏ ਅੰਤਰੀਵ ਹੈਸ਼ ਫੰਕਸ਼ਨ। ਇਹ ਭਾਗ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕਾਰਵਾਈਆਂ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਹੈਸ਼ ਫੰਕਸ਼ਨਾਂ ਦੀ ਵਰਤੋਂ ਲਈ ਲੋੜਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ।

For password storage, as well as the cryptography appendix, the [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) will also provide useful context and guidance.

ਪਾਸਵਰਡ ਸਟੋਰੇਜ ਲਈ, ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਅੰਤਿਕਾ ਦੇ ਨਾਲ-ਨਾਲ, [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) ਵੀ ਉਪਯੋਗੀ ਸੰਦਰਭ ਅਤੇ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰੇਗੀ।

| # | Description | Level |
| :---: | :--- | :---: |
| **11.4.1** | Verify that only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Disallowed hash functions, such as MD5, must not be used for any cryptographic purpose. | 1 |
| **11.4.2** | Verify that passwords are stored using an approved, computationally intensive, key derivation function (also known as a "password hashing function"), with parameter settings configured based on current guidance. The settings should balance security and performance to make brute-force attacks sufficiently challenging for the required level of security. | 2 |
| **11.4.3** | Verify that hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths. If collision resistance is required, the output length must be at least 256 bits. If only resistance to second pre-image attacks is required, the output length must be at least 128 bits. | 2 |
| **11.4.4** | Verify that the application uses approved key derivation functions with key stretching parameters when deriving secret keys from passwords. The parameters in use must balance security and performance to prevent brute-force attacks from compromising the resulting cryptographic key. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **11.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਆਮ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਵਰਤੋਂ ਦੇ ਮਾਮਲਿਆਂ ਲਈ, ਜਿਸ ਵਿੱਚ ਡਿਜ਼ੀਟਲ ਦਸਤਖ਼ਤ, HMAC, KDF, ਅਤੇ ਬੇਤਰਤੀਬ ਬਿੱਟ ਉਤਪਾਦਨ ਸ਼ਾਮਲ ਹਨ, ਸਿਰਫ਼ ਪ੍ਰਵਾਨਿਤ ਹੈਸ਼ ਫੰਕਸ਼ਨ ਹੀ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਮਨਾਹੀ ਵਾਲੇ ਹੈਸ਼ ਫੰਕਸ਼ਨ, ਜਿਵੇਂ ਕਿ MD5, ਕਿਸੇ ਵੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਮੰਤਵ ਲਈ ਨਹੀਂ ਵਰਤੇ ਜਾਣੇ ਚਾਹੀਦੇ। | 1 |
| **11.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪਾਸਵਰਡ ਇੱਕ ਪ੍ਰਵਾਨਿਤ, ਗਣਨਾਤਮਕ ਤੌਰ 'ਤੇ ਭਾਰੀ, ਕੁੰਜੀ-ਵਿਉਤਪੱਤੀ ਫੰਕਸ਼ਨ (ਜਿਸਨੂੰ "ਪਾਸਵਰਡ ਹੈਸ਼ਿੰਗ ਫੰਕਸ਼ਨ" ਵੀ ਕਿਹਾ ਜਾਂਦਾ ਹੈ) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਿਸ ਦੀਆਂ ਪੈਰਾਮੀਟਰ ਸੈਟਿੰਗਾਂ ਮੌਜੂਦਾ ਮਾਰਗਦਰਸ਼ਨ ਦੇ ਆਧਾਰ 'ਤੇ ਕੌਨਫ਼ਿਗਰ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। ਸੈਟਿੰਗਾਂ ਨੂੰ ਸੁਰੱਖਿਆ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਸੰਤੁਲਨ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ ਜੋ ਸੁਰੱਖਿਆ ਦੇ ਲੋੜੀਂਦੇ ਪੱਧਰ ਲਈ ਬਰੂਟ ਫੋਰਸ ਹਮਲਿਆਂ ਨੂੰ ਕਾਫ਼ੀ ਚੁਣੌਤੀਪੂਰਨ ਬਣਾਇਆ ਜਾ ਸਕੇ। | 2 |
| **11.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਡਿਜ਼ੀਟਲ ਦਸਤਖ਼ਤਾਂ ਵਿੱਚ, ਡਾਟਾ ਪ੍ਰਮਾਣੀਕਰਨ ਜਾਂ ਡਾਟਾ ਅਖੰਡਤਾ (integrity) ਦੇ ਹਿੱਸੇ ਵਜੋਂ ਵਰਤੇ ਜਾਂਦੇ ਹੈਸ਼ ਫੰਕਸ਼ਨ ਟੱਕਰ-ਰੋਧਕ (collision resistant) ਹਨ ਅਤੇ ਉਹਨਾਂ ਦੀਆਂ ਬਿੱਟ-ਲੰਬਾਈਆਂ ਢੁਕਵੀਆਂ ਹਨ। ਜੇ ਟੱਕਰ ਰੋਧਕਤਾ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਆਉਟਪੁੱਟ ਲੰਬਾਈ ਘੱਟੋ-ਘੱਟ 256 ਬਿੱਟ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ। ਜੇ ਸਿਰਫ਼ ਦੂਜੇ ਪ੍ਰੀ-ਇਮੇਜ (second pre-image) ਹਮਲਿਆਂ ਪ੍ਰਤੀ ਰੋਧਕਤਾ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਆਉਟਪੁੱਟ ਲੰਬਾਈ ਘੱਟੋ-ਘੱਟ 128 ਬਿੱਟ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ। | 2 |
| **11.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਪਾਸਵਰਡਾਂ ਤੋਂ ਗੁਪਤ ਕੁੰਜੀਆਂ ਵਿਉਤਪੰਨ ਕਰਦੇ ਸਮੇਂ ਕੁੰਜੀ ਸਟ੍ਰੈਚਿੰਗ (key stretching) ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਨਾਲ ਪ੍ਰਵਾਨਿਤ ਕੁੰਜੀ-ਵਿਉਤਪੱਤੀ ਫੰਕਸ਼ਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ। ਵਰਤੋਂ ਵਿੱਚ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸੁਰੱਖਿਆ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਸੰਤੁਲਨ ਰੱਖਣਾ ਲਾਜ਼ਮੀ ਹੈ ਤਾਂ ਜੋ ਬਰੂਟ ਫੋਰਸ ਹਮਲਿਆਂ ਨੂੰ ਨਤੀਜੇ ਵਜੋਂ ਬਣੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀ ਨਾਲ ਸਮਝੌਤਾ ਕਰਨ ਤੋਂ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 2 |

## V11.5 Random Values
## V11.5 ਬੇਤਰਤੀਬ ਮੁੱਲ

Cryptographically secure Pseudo-random Number Generation (CSPRNG) is incredibly difficult to get right. Generally, good sources of entropy within a system will be quickly depleted if over-used, but sources with less randomness can lead to predictable keys and secrets.

ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਤੌਰ 'ਤੇ ਸੁਰੱਖਿਅਤ ਛਦਮ-ਬੇਤਰਤੀਬ ਨੰਬਰ ਉਤਪਾਦਨ (Cryptographically secure Pseudo-random Number Generation, CSPRNG) ਨੂੰ ਸਹੀ ਕਰਨਾ ਬੇਹੱਦ ਮੁਸ਼ਕਲ ਹੈ। ਆਮ ਤੌਰ 'ਤੇ, ਇੱਕ ਸਿਸਟਮ ਦੇ ਅੰਦਰ ਐਂਟਰੋਪੀ (entropy) ਦੇ ਚੰਗੇ ਸਰੋਤ ਲੋੜ ਤੋਂ ਵੱਧ ਵਰਤੇ ਜਾਣ 'ਤੇ ਜਲਦੀ ਖ਼ਤਮ ਹੋ ਜਾਣਗੇ, ਪਰ ਘੱਟ ਬੇਤਰਤੀਬੀ ਵਾਲੇ ਸਰੋਤ ਅਨੁਮਾਨਯੋਗ ਕੁੰਜੀਆਂ ਅਤੇ ਭੇਦਾਂ ਵੱਲ ਲੈ ਜਾ ਸਕਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **11.5.1** | Verify that all random numbers and strings which are intended to be non-guessable must be generated using a cryptographically secure pseudo-random number generator (CSPRNG) and have at least 128 bits of entropy. Note that UUIDs do not respect this condition. | 2 |
| **11.5.2** | Verify that the random number generation mechanism in use is designed to work securely, even under heavy demand. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **11.5.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਬੇਤਰਤੀਬ ਨੰਬਰ ਅਤੇ ਸਟ੍ਰਿੰਗ ਜਿਨ੍ਹਾਂ ਦਾ ਅਨੁਮਾਨ ਨਾ ਲਗਾਇਆ ਜਾ ਸਕਣਾ ਉਦੇਸ਼ਿਤ ਹੈ, ਇੱਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਤੌਰ 'ਤੇ ਸੁਰੱਖਿਅਤ ਛਦਮ-ਬੇਤਰਤੀਬ ਨੰਬਰ ਜਨਰੇਟਰ (CSPRNG) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪੈਦਾ ਕੀਤੇ ਜਾਣੇ ਲਾਜ਼ਮੀ ਹਨ ਅਤੇ ਉਹਨਾਂ ਵਿੱਚ ਘੱਟੋ-ਘੱਟ 128 ਬਿੱਟ ਐਂਟਰੋਪੀ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ। ਧਿਆਨ ਦਿਓ ਕਿ UUID ਇਸ ਸ਼ਰਤ ਦੀ ਪਾਲਣਾ ਨਹੀਂ ਕਰਦੇ। | 2 |
| **11.5.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਵਰਤੋਂ ਵਿੱਚ ਬੇਤਰਤੀਬ ਨੰਬਰ ਉਤਪਾਦਨ ਪ੍ਰਣਾਲੀ ਭਾਰੀ ਮੰਗ ਦੇ ਅਧੀਨ ਵੀ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੀ ਗਈ ਹੈ। | 3 |

## V11.6 Public Key Cryptography
## V11.6 ਜਨਤਕ ਕੁੰਜੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ

Public Key Cryptography will be used where it is not possible or not desirable to share a secret key between multiple parties.

ਜਨਤਕ ਕੁੰਜੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ (Public Key Cryptography) ਉੱਥੇ ਵਰਤੀ ਜਾਵੇਗੀ ਜਿੱਥੇ ਕਈ ਧਿਰਾਂ ਵਿਚਕਾਰ ਗੁਪਤ ਕੁੰਜੀ ਸਾਂਝੀ ਕਰਨਾ ਸੰਭਵ ਨਹੀਂ ਜਾਂ ਲੋੜੀਂਦਾ ਨਹੀਂ ਹੈ।

As part of this, there exists a need for approved key exchange mechanisms, such as Diffie-Hellman and Elliptic Curve Diffie-Hellman (ECDH) to ensure that the cryptosystem remains secure against modern threats. The "Secure Communication" chapter provides requirements for TLS so the requirements in this section are intended for situations where Public Key Cryptography is being used in use cases other than TLS.

ਇਸਦੇ ਹਿੱਸੇ ਵਜੋਂ, ਪ੍ਰਵਾਨਿਤ ਕੁੰਜੀ ਵਟਾਂਦਰਾ (key exchange) ਪ੍ਰਣਾਲੀਆਂ, ਜਿਵੇਂ ਕਿ Diffie-Hellman ਅਤੇ Elliptic Curve Diffie-Hellman (ECDH), ਦੀ ਲੋੜ ਮੌਜੂਦ ਹੈ ਤਾਂ ਜੋ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਕ੍ਰਿਪਟੋਸਿਸਟਮ ਆਧੁਨਿਕ ਖ਼ਤਰਿਆਂ ਦੇ ਵਿਰੁੱਧ ਸੁਰੱਖਿਅਤ ਰਹੇ। "ਸੁਰੱਖਿਅਤ ਸੰਚਾਰ" (Secure Communication) ਅਧਿਆਇ TLS ਲਈ ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਇਸ ਲਈ ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਉਹਨਾਂ ਸਥਿਤੀਆਂ ਲਈ ਹਨ ਜਿੱਥੇ ਜਨਤਕ ਕੁੰਜੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ TLS ਤੋਂ ਇਲਾਵਾ ਹੋਰ ਵਰਤੋਂ ਦੇ ਮਾਮਲਿਆਂ ਵਿੱਚ ਵਰਤੀ ਜਾ ਰਹੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **11.6.1** | Verify that only approved cryptographic algorithms and modes of operation are used for key generation and seeding, and digital signature generation and verification. Key generation algorithms must not generate insecure keys vulnerable to known attacks, for example, RSA keys which are vulnerable to Fermat factorization. | 2 |
| **11.6.2** | Verify that approved cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus on ensuring that key exchange mechanisms use secure parameters. This will prevent attacks on the key establishment process which could lead to adversary-in-the-middle attacks or cryptographic breaks. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **11.6.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕੁੰਜੀ ਉਤਪਾਦਨ ਅਤੇ ਸੀਡਿੰਗ (seeding), ਅਤੇ ਡਿਜ਼ੀਟਲ ਦਸਤਖ਼ਤ ਬਣਾਉਣ ਅਤੇ ਤਸਦੀਕ ਲਈ ਸਿਰਫ਼ ਪ੍ਰਵਾਨਿਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਐਲਗੋਰਿਦਮ ਅਤੇ ਸੰਚਾਲਨ ਮੋਡ (modes of operation) ਹੀ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਕੁੰਜੀ ਉਤਪਾਦਨ ਐਲਗੋਰਿਦਮਾਂ ਨੂੰ ਜਾਣੇ-ਪਛਾਣੇ ਹਮਲਿਆਂ ਪ੍ਰਤੀ ਕਮਜ਼ੋਰ ਅਸੁਰੱਖਿਅਤ ਕੁੰਜੀਆਂ ਨਹੀਂ ਪੈਦਾ ਕਰਨੀਆਂ ਚਾਹੀਦੀਆਂ, ਉਦਾਹਰਨ ਲਈ, RSA ਕੁੰਜੀਆਂ ਜੋ ਫ਼ਰਮਾ ਗੁਣਨਖੰਡੀਕਰਨ (Fermat factorization) ਪ੍ਰਤੀ ਕਮਜ਼ੋਰ ਹਨ। | 2 |
| **11.6.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕੁੰਜੀ ਵਟਾਂਦਰੇ ਲਈ ਪ੍ਰਵਾਨਿਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਐਲਗੋਰਿਦਮ (ਜਿਵੇਂ ਕਿ Diffie-Hellman) ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਇਸ ਗੱਲ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦੇ ਹੋਏ ਕਿ ਕੁੰਜੀ ਵਟਾਂਦਰਾ ਪ੍ਰਣਾਲੀਆਂ ਸੁਰੱਖਿਅਤ ਪੈਰਾਮੀਟਰ ਵਰਤਦੀਆਂ ਹਨ। ਇਹ ਕੁੰਜੀ ਸਥਾਪਨਾ (key establishment) ਪ੍ਰਕਿਰਿਆ 'ਤੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕੇਗਾ ਜੋ ਵਿਚਕਾਰਲੇ-ਵਿਰੋਧੀ (adversary-in-the-middle) ਹਮਲਿਆਂ ਜਾਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਟੁੱਟਣ ਵੱਲ ਲੈ ਜਾ ਸਕਦੇ ਹਨ। | 3 |

## V11.7 In-Use Data Cryptography
## V11.7 ਵਰਤੋਂ-ਅਧੀਨ ਡਾਟਾ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ

Protecting data while it is being processed is paramount. Techniques such as full memory encryption, encryption of data in transit, and ensuring data is encrypted as quickly as possible after use is recommended.

ਡਾਟੇ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਜਾਣ ਦੌਰਾਨ ਸੁਰੱਖਿਅਤ ਰੱਖਣਾ ਸਰਵਉੱਚ ਮਹੱਤਵ ਰੱਖਦਾ ਹੈ। ਪੂਰੀ ਮੈਮੋਰੀ ਏਨਕ੍ਰਿਪਸ਼ਨ, ਪ੍ਰਸਾਰਣ ਦੌਰਾਨ ਡਾਟੇ (data in transit) ਦੀ ਏਨਕ੍ਰਿਪਸ਼ਨ, ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਵਰਗੀਆਂ ਤਕਨੀਕਾਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਵਰਤੋਂ ਤੋਂ ਬਾਅਦ ਡਾਟੇ ਨੂੰ ਜਿੰਨੀ ਜਲਦੀ ਸੰਭਵ ਹੋਵੇ ਏਨਕ੍ਰਿਪਟ ਕੀਤਾ ਜਾਵੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **11.7.1** | Verify that full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes. | 3 |
| **11.7.2** | Verify that data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **11.7.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪੂਰੀ ਮੈਮੋਰੀ ਏਨਕ੍ਰਿਪਸ਼ਨ ਵਰਤੋਂ ਵਿੱਚ ਹੈ ਜੋ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਨੂੰ ਉਸਦੀ ਵਰਤੋਂ ਦੌਰਾਨ ਸੁਰੱਖਿਅਤ ਰੱਖਦੀ ਹੈ, ਅਤੇ ਅਣਅਧਿਕਾਰਤ ਉਪਭੋਗਤਾਵਾਂ ਜਾਂ ਪ੍ਰੋਸੈਸਾਂ ਦੁਆਰਾ ਪਹੁੰਚ ਨੂੰ ਰੋਕਦੀ ਹੈ। | 3 |
| **11.7.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਡਾਟਾ ਨਿਊਨਤਮੀਕਰਨ (data minimization) ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਪ੍ਰੋਸੈਸਿੰਗ ਦੌਰਾਨ ਘੱਟੋ-ਘੱਟ ਮਾਤਰਾ ਵਿੱਚ ਡਾਟਾ ਉਜਾਗਰ ਹੋਵੇ, ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਡਾਟੇ ਨੂੰ ਵਰਤੋਂ ਤੋਂ ਤੁਰੰਤ ਬਾਅਦ ਜਾਂ ਜਿੰਨੀ ਜਲਦੀ ਸੰਭਵ ਹੋਵੇ ਏਨਕ੍ਰਿਪਟ ਕੀਤਾ ਜਾਵੇ। | 3 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP Web Security Testing Guide: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography)
* [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
