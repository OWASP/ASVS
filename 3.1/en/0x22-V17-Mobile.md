# V17: Mobile Verification Requirements

## Control Objective

This section contains controls that are mobile application specific. These controls have been de-duplicated from 2.0, so must be taken in conjunction with all other sections of the relevant ASVS Verification Level.

Mobile applications should:

* Should have the same level of security controls within the mobile client as found in the server, by enforcing security controls in a trusted environment
* Sensitive information assets stored on the device should be done so in a secure manner
* All sensitive data transmitted from the device should be done so with transport layer security in mind.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **17.1** | Verify that ID values stored on the device and retrievable by other applications, such as the UDID or IMEI number are not used as authentication tokens. | ✓ | ✓ | ✓ | 2.0 |
| **17.2** | Verify that the mobile app does not store sensitive data onto potentially unencrypted shared resources on the device (e.g. SD card or shared folders). | ✓ | ✓ | ✓ | 2.0 |
| **17.3** | Verify that sensitive data is not stored unprotected on the device, even in system protected areas such as key chains. | ✓ | ✓ | ✓ | 2.0 |
| **17.4** | Verify that secret keys, API tokens, or passwords are dynamically generated in mobile applications. | ✓ | ✓ | ✓ | 2.0 |
| **17.5** | Verify that the mobile app prevents leaking of sensitive information (for example, screenshots are saved of the current application as the application is backgrounded or writing sensitive information in console). |  | ✓ | ✓ | 2.0 |
| **17.6** | Verify that the application is requesting minimal permissions for required functionality and resources. |  | ✓ | ✓ | 2.0 |
| **17.7** | Verify that the application sensitive code is laid out unpredictably in memory (For example ASLR). | ✓ | ✓ | ✓ | 2.0 |
| **17.8** | Verify that there are anti-debugging techniques present that are sufficient enough to deter or delay likely attackers from injecting debuggers into the mobile app (For example GDB). |  |  | ✓ | 2.0 |
| **17.9** | Verify that the app does not export sensitive activities, intents, or content providers for other mobile apps on the same device to exploit.  | ✓ | ✓ | ✓ | 2.0 |
| **17.10** | Verify that sensitive information maintained in memory is overwritten with zeros as soon as it is no longer required, to mitigate memory dumping attacks. |  | ✓ | ✓ | 3.0.1 |
| **17.11** | Verify that the app validates input to exported activities, intents, or content providers. | ✓ | ✓ | ✓ | 3.0.1 |



## References

For more information, see also:

* [OWASP Mobile Security Project](https://www.owasp.org/index.php/OWASP_Mobile_Security_Project)
* [iOS Developer Cheat Sheet](https://www.owasp.org/index.php/IOS_Developer_Cheat_Sheet)
