# V7: Cryptography Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* That all cryptographic modules fail in a secure manner and that errors are handled correctly.
* That a suitable random number generator is used when randomness is required.
* That access to keys is managed in a secure way.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **7.2** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle. | ✓ | ✓ | ✓ | 1.0 |
| **7.6** | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module’s approved random number generator when these random values are intended to be not guessable by an attacker. |  | ✓ | ✓ | 1.0 |
| **7.7** | Verify that cryptographic algorithms used by the application have been validated against FIPS 140-2 or an equivalent standard. | ✓ | ✓ | ✓ | 1.0 |
| **7.8** | Verify that cryptographic modules operate in their approved mode according to their published security policies. |  |  | ✓ | 1.0 |
| **7.9** | Verify that there is an explicit policy for how cryptographic keys are managed (e.g., generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced. |  | ✓ | ✓ | 1.0 |
| **7.11** | Verify that all consumers of cryptographic services do not have direct access to key material. Isolate cryptographic processes, including master secrets and consider the use of a virtualized or physical hardware key vault (HSM).  |  |  | ✓ | 3.0.1 |
| **7.12** | Verify that Personally Identifiable Information (PII) and other sensitive data is stored encrypted while at rest. |  | ✓ | ✓ | 3.1 |
| **7.13** | Verify that sensitive passwords or key material maintained in memory is overwritten with zeros as soon as it is no longer required, to mitigate memory dumping attacks. |  | ✓ | ✓ | 3.1 |
| **7.14** | Verify that all keys and passwords are replaceable, and are generated or replaced at installation time. |  | ✓ | ✓ | 3.0 |
| **7.15** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. |  |  | ✓ | 3.0 |



## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for weak Cryptography](https://www.owasp.org/index.php/Testing_for_weak_Cryptography)
* [OWASP Cheat Sheet: Cryptographic Storage](https://www.owasp.org/index.php/Cryptographic_Storage_Cheat_Sheet)
