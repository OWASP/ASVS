# Appendix C: Internet of Things Verification Requirements

This chapter was originally in the main branch, but with the work that the OWASP IoT team has done, it doesn't make sense to maintain two different threads on the subject. For the 4.0 release, we are moving this to the Appendix, and urge all who require this, to rather use the main [OWASP IoT project](https://owasp.org/www-project-internet-of-things/).

## Control Objective

Embedded/IoT devices should:

* Have the same level of security controls within the device as found in the server, by enforcing security controls in a trusted environment.
* Sensitive data stored on the device should be done so in a secure manner using hardware backed storage such as secure elements.
* All sensitive data transmitted from the device should utilize transport layer security.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **C.1** | Verify that application layer debugging interfaces such USB, UART, and other serial variants are disabled or protected by a complex password. | ✓ | ✓ | ✓ | 4.0 |
| **C.2** | Verify that cryptographic keys and certificates are unique to each individual device. | ✓ | ✓ | ✓ | 4.0 |
| **C.3** | Verify that memory protection controls such as ASLR and DEP are enabled by the embedded/IoT operating system, if applicable. | ✓ | ✓ | ✓ | 4.0 |
| **C.4** | Verify that on-chip debugging interfaces such as JTAG or SWD are disabled or that available protection mechanism is enabled and configured appropriately. | ✓ | ✓ | ✓ | 4.0 |
| **C.5** | Verify that trusted execution is implemented and enabled, if available on the device SoC or CPU. | ✓ | ✓ | ✓ | 4.0 |
| **C.6** | Verify that sensitive data, private keys and certificates are stored securely in a Secure Element, TPM, TEE (Trusted Execution Environment), or protected using strong cryptography. | ✓ | ✓ | ✓ | 4.0 |
| **C.7** | Verify that the firmware apps protect data-in-transit using transport layer security. | ✓ | ✓ | ✓ | 4.0 |
| **C.8** | Verify that the firmware apps validate the digital signature of server connections. | ✓ | ✓ | ✓ | 4.0 |
| **C.9** | Verify that wireless communications are mutually authenticated. | ✓ | ✓ | ✓ | 4.0 |
| **C.10** | Verify that wireless communications are sent over an encrypted channel. | ✓ | ✓ | ✓ | 4.0 |
| **C.11** | Verify that any use of banned C functions are replaced with the appropriate safe equivalent functions. | ✓ | ✓ | ✓ | 4.0 |
| **C.12** | Verify that each firmware maintains a software bill of materials cataloging third-party components, versioning, and published vulnerabilities. | ✓ | ✓ | ✓ | 4.0 |
| **C.13** | Verify all code including third-party binaries, libraries, frameworks are reviewed for hardcoded credentials (backdoors). | ✓ | ✓ | ✓ | 4.0 |
| **C.14** | Verify that the application and firmware components are not susceptible to OS Command Injection by invoking shell command wrappers, scripts, or that security controls prevent OS Command Injection. | ✓ | ✓ | ✓ | 4.0 |
| **C.15** | Verify that the firmware apps pin the digital signature to a trusted server(s). | | ✓ | ✓ | 4.0 |
| **C.16** | Verify the presence of tamper resistance and/or tamper detection features. | | ✓ | ✓ | 4.0 |
| **C.17** | Verify that any available Intellectual Property protection technologies provided by the chip manufacturer are enabled. | | ✓ | ✓ | 4.0 |
| **C.18** | Verify security controls are in place to hinder firmware reverse engineering (e.g., removal of verbose debugging symbols). | | ✓ | ✓ | 4.0 |
| **C.19** | Verify the device validates the boot image signature before loading. | | ✓ | ✓ | 4.0 |
| **C.20** | Verify that the firmware update process is not vulnerable to time-of-check vs time-of-use attacks. | | ✓ | ✓ | 4.0 |
| **C.21** | Verify the device uses code signing and validates firmware upgrade files before installing. | | ✓ | ✓ | 4.0 |
| **C.22** | Verify that the device cannot be downgraded to old versions (anti-rollback) of valid firmware. | | ✓ | ✓ | 4.0 |
| **C.23** | Verify usage of cryptographically secure pseudo-random number generator on embedded device (e.g., using chip-provided random number generators). | | ✓ | ✓ | 4.0 |
| **C.24** | Verify that firmware can perform automatic firmware updates upon a predefined schedule. | | ✓ | ✓ | 4.0 |
| **C.25** | Verify that the device wipes firmware and sensitive data upon detection of tampering or receipt of invalid message. | | | ✓ | 4.0 |
| **C.26** | Verify that only micro controllers that support disabling debugging interfaces (e.g. JTAG, SWD) are used. | | | ✓ | 4.0 |
| **C.27** | Verify that only micro controllers that provide substantial protection from de-capping and side channel attacks are used. | | | ✓ | 4.0 |
| **C.28** | Verify that sensitive traces are not exposed to outer layers of the printed circuit board. | | | ✓ | 4.0 |
| **C.29** | Verify that inter-chip communication is encrypted (e.g. Main board to daughter board communication). | | | ✓ | 4.0 |
| **C.30** | Verify the device uses code signing and validates code before execution. | | | ✓ | 4.0 |
| **C.31** | Verify that sensitive information maintained in memory is overwritten with zeros as soon as it is no longer required. | | | ✓ | 4.0 |
| **C.32** | Verify that the firmware apps utilize kernel containers for isolation between apps. | | | ✓ | 4.0 |
| **C.33** | Verify that secure compiler flags such as -fPIE, -fstack-protector-all, -Wl,-z,noexecstack, -Wl,-z,noexecheap are configured for firmware builds. | | | ✓ | 4.0 |
| **C.34** | Verify that micro controllers are configured with code protection (if applicable). | | | ✓ | 4.0 |

## References

For more information, see also:

* [OWASP Internet of Things Top 10](https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf)
* [OWASP Embedded Application Security Project](https://owasp.org/www-project-embedded-application-security/)
* [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/)
* [Trudy TCP Proxy Tool](https://github.com/praetorian-inc/trudy)
