<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x23-V14-Data-Protection.md -->
<!-- Translator: GeeksikhSecurity -->

# V14 Data Protection
# V14 ਡਾਟਾ ਸੁਰੱਖਿਆ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Applications cannot account for all usage patterns and user behaviors, and should therefore implement controls to limit unauthorized access to sensitive data on client devices.

ਐਪਲੀਕੇਸ਼ਨਾਂ ਸਾਰੇ ਵਰਤੋਂ ਦੇ ਢੰਗਾਂ ਅਤੇ ਉਪਭੋਗਤਾ ਵਿਵਹਾਰਾਂ ਦਾ ਹਿਸਾਬ ਨਹੀਂ ਰੱਖ ਸਕਦੀਆਂ, ਅਤੇ ਇਸ ਲਈ ਉਹਨਾਂ ਨੂੰ ਕਲਾਇੰਟ ਡਿਵਾਈਸਾਂ 'ਤੇ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ (sensitive data) ਤੱਕ ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ ਨੂੰ ਸੀਮਤ ਕਰਨ ਲਈ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ।

This chapter includes requirements related to defining what data needs to be protected, how it should be protected, and specific mechanisms to implement or pitfalls to avoid.

ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਇਹ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਕਿ ਕਿਹੜੇ ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਦੀ ਲੋੜ ਹੈ, ਉਸ ਨੂੰ ਕਿਵੇਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਅਤੇ ਲਾਗੂ ਕਰਨ ਲਈ ਖ਼ਾਸ ਪ੍ਰਣਾਲੀਆਂ ਜਾਂ ਬਚਣ ਯੋਗ ਆਮ ਗ਼ਲਤੀਆਂ (pitfalls) ਕਿਹੜੀਆਂ ਹਨ।

Another consideration for data protection is bulk extraction, modification, or excessive usage. Each system's requirements are likely to be very different, so determining what is "abnormal" must consider the threat model and business risk. From an ASVS perspective, detecting these issues is handled in the "Security Logging and Error Handling" chapter, and setting limits is handled in the "Validation and Business Logic" chapter.

ਡਾਟਾ ਸੁਰੱਖਿਆ ਲਈ ਇੱਕ ਹੋਰ ਵਿਚਾਰ ਥੋਕ ਵਿੱਚ ਡਾਟਾ ਕੱਢਣਾ (bulk extraction), ਸੋਧਣਾ, ਜਾਂ ਬਹੁਤ ਜ਼ਿਆਦਾ ਵਰਤੋਂ ਹੈ। ਹਰ ਸਿਸਟਮ ਦੀਆਂ ਲੋੜਾਂ ਬਹੁਤ ਵੱਖਰੀਆਂ ਹੋਣ ਦੀ ਸੰਭਾਵਨਾ ਹੈ, ਇਸ ਲਈ ਇਹ ਨਿਰਧਾਰਿਤ ਕਰਦੇ ਸਮੇਂ ਕਿ "ਅਸਧਾਰਨ" ਕੀ ਹੈ, ਖ਼ਤਰਾ ਮਾਡਲ (threat model) ਅਤੇ ਕਾਰੋਬਾਰੀ ਜੋਖਮ 'ਤੇ ਵਿਚਾਰ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ। ASVS ਦੇ ਨਜ਼ਰੀਏ ਤੋਂ, ਇਹਨਾਂ ਮੁੱਦਿਆਂ ਦਾ ਪਤਾ ਲਗਾਉਣਾ "ਸੁਰੱਖਿਆ ਲੌਗਿੰਗ ਅਤੇ ਗਲਤੀ ਪ੍ਰਬੰਧਨ" (Security Logging and Error Handling) ਅਧਿਆਇ ਵਿੱਚ ਸੰਭਾਲਿਆ ਗਿਆ ਹੈ, ਅਤੇ ਸੀਮਾਵਾਂ ਨਿਰਧਾਰਿਤ ਕਰਨਾ "ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਕਾਰੋਬਾਰੀ ਤਰਕ" (Validation and Business Logic) ਅਧਿਆਇ ਵਿੱਚ ਸੰਭਾਲਿਆ ਗਿਆ ਹੈ।

## V14.1 Data Protection Documentation
## V14.1 ਡਾਟਾ ਸੁਰੱਖਿਆ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

A key prerequisite for being able to protect data is to categorize what data should be considered sensitive. There are likely to be several different levels of sensitivity, and for each level, the controls required to protect data at that level will be different.

ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰ ਸਕਣ ਦੀ ਇੱਕ ਮੁੱਖ ਪੂਰਵ-ਸ਼ਰਤ ਇਹ ਸ਼੍ਰੇਣੀਬੱਧ ਕਰਨਾ ਹੈ ਕਿ ਕਿਹੜੇ ਡਾਟੇ ਨੂੰ ਸੰਵੇਦਨਸ਼ੀਲ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਦੇ ਕਈ ਵੱਖ-ਵੱਖ ਪੱਧਰ ਹੋਣ ਦੀ ਸੰਭਾਵਨਾ ਹੈ, ਅਤੇ ਹਰੇਕ ਪੱਧਰ ਲਈ, ਉਸ ਪੱਧਰ 'ਤੇ ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਲੋੜੀਂਦੇ ਨਿਯੰਤਰਣ ਵੱਖਰੇ ਹੋਣਗੇ।

There are various privacy regulations and laws that affect how applications must approach the storage, use, and transmission of sensitive personal information. This section no longer tries to duplicate these types of data protection or privacy legislation, but rather focuses on key technical considerations for protecting sensitive data. Please consult local laws and regulations, and consult a qualified privacy specialist or lawyer as required.

ਕਈ ਤਰ੍ਹਾਂ ਦੇ ਨਿੱਜਤਾ (privacy) ਨਿਯਮ ਅਤੇ ਕਾਨੂੰਨ ਹਨ ਜੋ ਇਸ ਗੱਲ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ ਕਿ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸੰਵੇਦਨਸ਼ੀਲ ਨਿੱਜੀ ਜਾਣਕਾਰੀ ਦੇ ਭੰਡਾਰਨ, ਵਰਤੋਂ, ਅਤੇ ਪ੍ਰਸਾਰਣ ਨਾਲ ਕਿਵੇਂ ਨਜਿੱਠਣਾ ਲਾਜ਼ਮੀ ਹੈ। ਇਹ ਭਾਗ ਹੁਣ ਇਸ ਕਿਸਮ ਦੇ ਡਾਟਾ ਸੁਰੱਖਿਆ ਜਾਂ ਨਿੱਜਤਾ ਕਾਨੂੰਨਾਂ ਦੀ ਨਕਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਨਹੀਂ ਕਰਦਾ, ਸਗੋਂ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਮੁੱਖ ਤਕਨੀਕੀ ਵਿਚਾਰਾਂ 'ਤੇ ਕੇਂਦਰਿਤ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਸਥਾਨਕ ਕਾਨੂੰਨਾਂ ਅਤੇ ਨਿਯਮਾਂ ਨੂੰ ਵੇਖੋ, ਅਤੇ ਲੋੜ ਅਨੁਸਾਰ ਕਿਸੇ ਯੋਗ ਨਿੱਜਤਾ ਮਾਹਰ ਜਾਂ ਵਕੀਲ ਨਾਲ ਸਲਾਹ ਕਰੋ।

| # | Description | Level |
| :---: | :--- | :---: |
| **14.1.1** | Verify that all sensitive data created and processed by the application has been identified and classified into protection levels. This includes data that is only encoded and therefore easily decoded, such as Base64 strings or the plaintext payload inside a JWT. Protection levels need to take into account any data protection and privacy regulations and standards which the application is required to comply with. | 2 |
| **14.1.2** | Verify that all sensitive data protection levels have a documented set of protection requirements. This must include (but not be limited to) requirements related to general encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, database-level encryption, privacy and privacy-enhancing technologies to be used, and other confidentiality requirements. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **14.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਬਣਾਏ ਅਤੇ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਸਾਰੇ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਦੀ ਪਛਾਣ ਕੀਤੀ ਗਈ ਹੈ ਅਤੇ ਉਸ ਨੂੰ ਸੁਰੱਖਿਆ ਪੱਧਰਾਂ ਵਿੱਚ ਵਰਗੀਕ੍ਰਿਤ (ਡਾਟਾ ਵਰਗੀਕਰਨ, data classification) ਕੀਤਾ ਗਿਆ ਹੈ। ਇਸ ਵਿੱਚ ਉਹ ਡਾਟਾ ਸ਼ਾਮਲ ਹੈ ਜੋ ਸਿਰਫ਼ ਏਨਕੋਡ ਕੀਤਾ ਹੋਇਆ ਹੈ ਅਤੇ ਇਸ ਲਈ ਆਸਾਨੀ ਨਾਲ ਡੀਕੋਡ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ Base64 ਸਟ੍ਰਿੰਗ ਜਾਂ JWT ਦੇ ਅੰਦਰਲਾ ਸਾਦਾ-ਪਾਠ (plaintext) ਪੇਲੋਡ। ਸੁਰੱਖਿਆ ਪੱਧਰਾਂ ਵਿੱਚ ਉਹਨਾਂ ਸਾਰੇ ਡਾਟਾ ਸੁਰੱਖਿਆ ਅਤੇ ਨਿੱਜਤਾ ਨਿਯਮਾਂ ਅਤੇ ਮਿਆਰਾਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਦੀ ਲੋੜ ਹੈ ਜਿਨ੍ਹਾਂ ਦੀ ਪਾਲਣਾ ਕਰਨੀ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਲੋੜੀਂਦੀ ਹੈ। | 2 |
| **14.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਸੁਰੱਖਿਆ ਪੱਧਰਾਂ ਲਈ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਦਾ ਇੱਕ ਦਸਤਾਵੇਜ਼ੀ ਸੈੱਟ ਮੌਜੂਦ ਹੈ। ਇਸ ਵਿੱਚ ਆਮ ਏਨਕ੍ਰਿਪਸ਼ਨ (encryption), ਅਖੰਡਤਾ (integrity) ਤਸਦੀਕ, ਡਾਟਾ ਧਾਰਨ (data retention), ਡਾਟੇ ਨੂੰ ਕਿਵੇਂ ਲੌਗ ਕੀਤਾ ਜਾਣਾ ਹੈ, ਲੌਗਾਂ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ, ਡਾਟਾਬੇਸ-ਪੱਧਰ ਏਨਕ੍ਰਿਪਸ਼ਨ, ਵਰਤੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਨਿੱਜਤਾ ਅਤੇ ਨਿੱਜਤਾ-ਵਧਾਊ ਤਕਨਾਲੋਜੀਆਂ (privacy-enhancing technologies), ਅਤੇ ਹੋਰ ਗੁਪਤਤਾ (confidentiality) ਲੋੜਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹੋਣੀਆਂ ਲਾਜ਼ਮੀ ਹਨ (ਪਰ ਇਹ ਇਹਨਾਂ ਤੱਕ ਸੀਮਤ ਨਹੀਂ)। | 2 |

## V14.2 General Data Protection
## V14.2 ਆਮ ਡਾਟਾ ਸੁਰੱਖਿਆ

This section contains various practical requirements related to the protection of data. Most are specific to particular issues such as unintended data leakage, but there is also a general requirement to implement protection controls based on the protection level required for each data item.

ਇਸ ਭਾਗ ਵਿੱਚ ਡਾਟੇ ਦੀ ਸੁਰੱਖਿਆ ਨਾਲ ਸੰਬੰਧਿਤ ਕਈ ਵਿਹਾਰਕ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ। ਜ਼ਿਆਦਾਤਰ ਖ਼ਾਸ ਮੁੱਦਿਆਂ, ਜਿਵੇਂ ਕਿ ਅਣਇੱਛਤ ਡਾਟਾ ਲੀਕੇਜ, ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ, ਪਰ ਹਰੇਕ ਡਾਟਾ ਇਕਾਈ ਲਈ ਲੋੜੀਂਦੇ ਸੁਰੱਖਿਆ ਪੱਧਰ ਦੇ ਆਧਾਰ 'ਤੇ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨ ਦੀ ਇੱਕ ਆਮ ਲੋੜ ਵੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **14.2.1** | Verify that sensitive data is only sent to the server in the HTTP message body or header fields, and that the URL and query string do not contain sensitive information, such as an API key or session token. | 1 |
| **14.2.2** | Verify that the application prevents sensitive data from being cached in server components, such as load balancers and application caches, or ensures that the data is securely purged after use. | 2 |
| **14.2.3** | Verify that defined sensitive data is not sent to untrusted parties (e.g., user trackers) to prevent unwanted collection of data outside of the application's control. | 2 |
| **14.2.4** | Verify that controls around sensitive data related to encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, privacy and privacy-enhancing technologies, are implemented as defined in the documentation for the specific data's protection level. | 2 |
| **14.2.5** | Verify that caching mechanisms are configured to only cache responses which have the expected content type for that resource and do not contain sensitive, dynamic content. The web server should return a 404 or 302 response when a non-existent file is accessed rather than returning a different, valid file. This should prevent Web Cache Deception attacks. | 3 |
| **14.2.6** | Verify that the application only returns the minimum required sensitive data for the application's functionality. For example, only returning some of the digits of a credit card number and not the full number. If the complete data is required, it should be masked in the user interface unless the user specifically views it. | 3 |
| **14.2.7** | Verify that sensitive information is subject to data retention classification, ensuring that outdated or unnecessary data is deleted automatically, on a defined schedule, or as the situation requires. | 3 |
| **14.2.8** | Verify that sensitive information is removed from the metadata of user-submitted files unless storage is consented to by the user. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **14.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਸਰਵਰ ਨੂੰ ਸਿਰਫ਼ HTTP ਸੁਨੇਹਾ ਬਾਡੀ (message body) ਜਾਂ ਹੈੱਡਰ ਖੇਤਰਾਂ ਵਿੱਚ ਹੀ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ, ਅਤੇ URL ਅਤੇ ਕਿਊਰੀ ਸਟ੍ਰਿੰਗ (query string) ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ, ਜਿਵੇਂ ਕਿ API ਕੁੰਜੀ ਜਾਂ ਸੈਸ਼ਨ ਟੋਕਨ, ਸ਼ਾਮਲ ਨਹੀਂ ਹੁੰਦੀ। | 1 |
| **14.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਨੂੰ ਸਰਵਰ ਘਟਕਾਂ, ਜਿਵੇਂ ਕਿ ਲੋਡ ਬੈਲੈਂਸਰ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਕੈਸ਼ (cache), ਵਿੱਚ ਕੈਸ਼ ਹੋਣ ਤੋਂ ਰੋਕਦੀ ਹੈ, ਜਾਂ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਵਰਤੋਂ ਤੋਂ ਬਾਅਦ ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਮਿਟਾ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। | 2 |
| **14.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪਰਿਭਾਸ਼ਿਤ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਧਿਰਾਂ (ਜਿਵੇਂ ਕਿ ਉਪਭੋਗਤਾ ਟ੍ਰੈਕਰ) ਨੂੰ ਨਹੀਂ ਭੇਜਿਆ ਜਾਂਦਾ, ਤਾਂ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਨਿਯੰਤਰਣ ਤੋਂ ਬਾਹਰ ਡਾਟੇ ਦੇ ਅਣਚਾਹੇ ਇਕੱਤਰੀਕਰਨ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 2 |
| **14.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਏਨਕ੍ਰਿਪਸ਼ਨ, ਅਖੰਡਤਾ ਤਸਦੀਕ, ਡਾਟਾ ਧਾਰਨ, ਡਾਟੇ ਨੂੰ ਕਿਵੇਂ ਲੌਗ ਕੀਤਾ ਜਾਣਾ ਹੈ, ਲੌਗਾਂ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ, ਨਿੱਜਤਾ ਅਤੇ ਨਿੱਜਤਾ-ਵਧਾਊ ਤਕਨਾਲੋਜੀਆਂ ਨਾਲ ਸੰਬੰਧਿਤ ਨਿਯੰਤਰਣ, ਉਸ ਖ਼ਾਸ ਡਾਟੇ ਦੇ ਸੁਰੱਖਿਆ ਪੱਧਰ ਲਈ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਅਨੁਸਾਰ ਲਾਗੂ ਕੀਤੇ ਗਏ ਹਨ। | 2 |
| **14.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕੈਸ਼ਿੰਗ ਪ੍ਰਣਾਲੀਆਂ ਸਿਰਫ਼ ਉਹਨਾਂ ਜਵਾਬਾਂ ਨੂੰ ਕੈਸ਼ ਕਰਨ ਲਈ ਸੰਰਚਿਤ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ ਜਿਨ੍ਹਾਂ ਦੀ ਸਮੱਗਰੀ ਕਿਸਮ (content type) ਉਸ ਸਰੋਤ ਲਈ ਉਮੀਦ ਕੀਤੀ ਗਈ ਕਿਸਮ ਹੈ ਅਤੇ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ, ਗਤੀਸ਼ੀਲ ਸਮੱਗਰੀ ਸ਼ਾਮਲ ਨਹੀਂ ਹੈ। ਜਦੋਂ ਕਿਸੇ ਮੌਜੂਦ ਨਾ ਹੋਣ ਵਾਲੀ ਫ਼ਾਈਲ ਤੱਕ ਪਹੁੰਚ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਵੈੱਬ ਸਰਵਰ ਨੂੰ ਕੋਈ ਵੱਖਰੀ, ਵੈਧ ਫ਼ਾਈਲ ਵਾਪਸ ਕਰਨ ਦੀ ਬਜਾਏ 404 ਜਾਂ 302 ਜਵਾਬ ਵਾਪਸ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। ਇਸ ਨਾਲ Web Cache Deception ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। | 3 |
| **14.2.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਆਪਣੀ ਕਾਰਜਸ਼ੀਲਤਾ ਲਈ ਸਿਰਫ਼ ਘੱਟੋ-ਘੱਟ ਲੋੜੀਂਦਾ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਹੀ ਵਾਪਸ ਕਰਦੀ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਕ੍ਰੈਡਿਟ ਕਾਰਡ ਨੰਬਰ ਦੇ ਸਿਰਫ਼ ਕੁਝ ਅੰਕ ਵਾਪਸ ਕਰਨਾ, ਨਾ ਕਿ ਪੂਰਾ ਨੰਬਰ। ਜੇ ਪੂਰੇ ਡਾਟੇ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਇਸ ਨੂੰ ਉਪਭੋਗਤਾ ਇੰਟਰਫ਼ੇਸ ਵਿੱਚ ਮਾਸਕ (mask) ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਦੋਂ ਤੱਕ ਉਪਭੋਗਤਾ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਇਸ ਨੂੰ ਨਾ ਵੇਖੇ। | 3 |
| **14.2.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਡਾਟਾ ਧਾਰਨ ਵਰਗੀਕਰਨ ਦੇ ਅਧੀਨ ਹੈ, ਜੋ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਪੁਰਾਣਾ ਜਾਂ ਬੇਲੋੜਾ ਡਾਟਾ ਆਪਣੇ ਆਪ, ਇੱਕ ਨਿਰਧਾਰਿਤ ਸਮਾਂ-ਸਾਰਣੀ 'ਤੇ, ਜਾਂ ਸਥਿਤੀ ਦੀ ਲੋੜ ਅਨੁਸਾਰ ਮਿਟਾ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। | 3 |
| **14.2.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸੌਂਪੀਆਂ ਫ਼ਾਈਲਾਂ ਦੇ ਮੈਟਾਡਾਟਾ ਵਿੱਚੋਂ ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਹਟਾ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ, ਜਦੋਂ ਤੱਕ ਉਪਭੋਗਤਾ ਨੇ ਇਸ ਦੇ ਭੰਡਾਰਨ ਲਈ ਸਹਿਮਤੀ ਨਾ ਦਿੱਤੀ ਹੋਵੇ। | 3 |

## V14.3 Client-side Data Protection
## V14.3 ਕਲਾਇੰਟ-ਸਾਈਡ ਡਾਟਾ ਸੁਰੱਖਿਆ

This section contains requirements preventing data from leaking in specific ways at the client or user agent side of an application.

ਇਸ ਭਾਗ ਵਿੱਚ ਉਹ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਕਲਾਇੰਟ ਜਾਂ ਯੂਜ਼ਰ ਏਜੰਟ (user agent) ਵਾਲੇ ਪਾਸੇ ਡਾਟੇ ਨੂੰ ਖ਼ਾਸ ਤਰੀਕਿਆਂ ਨਾਲ ਲੀਕ ਹੋਣ ਤੋਂ ਰੋਕਦੀਆਂ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **14.3.1** | Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated. The 'Clear-Site-Data' HTTP response header field may be able to help with this but the client-side should also be able to clear up if the server connection is not available when the session is terminated. | 1 |
| **14.3.2** | Verify that the application sets sufficient anti-caching HTTP response header fields (i.e., Cache-Control: no-store) so that sensitive data is not cached in browsers. | 2 |
| **14.3.3** | Verify that data stored in browser storage (such as localStorage, sessionStorage, IndexedDB, or cookies) does not contain sensitive data, with the exception of session tokens. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **14.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਲਾਇੰਟ ਜਾਂ ਸੈਸ਼ਨ ਦੇ ਸਮਾਪਤ ਹੋਣ ਤੋਂ ਬਾਅਦ ਪ੍ਰਮਾਣੀਕ੍ਰਿਤ (authenticated) ਡਾਟਾ ਕਲਾਇੰਟ ਭੰਡਾਰਨ, ਜਿਵੇਂ ਕਿ ਬ੍ਰਾਊਜ਼ਰ DOM, ਵਿੱਚੋਂ ਸਾਫ਼ ਕਰ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। 'Clear-Site-Data' HTTP ਜਵਾਬ ਹੈੱਡਰ ਖੇਤਰ ਇਸ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ, ਪਰ ਜੇ ਸੈਸ਼ਨ ਸਮਾਪਤ ਹੋਣ ਸਮੇਂ ਸਰਵਰ ਕਨੈਕਸ਼ਨ ਉਪਲਬਧ ਨਾ ਹੋਵੇ ਤਾਂ ਕਲਾਇੰਟ-ਸਾਈਡ ਨੂੰ ਵੀ ਆਪਣੇ ਆਪ ਸਾਫ਼ ਕਰ ਸਕਣ ਦੇ ਯੋਗ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। | 1 |
| **14.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕਾਫ਼ੀ ਕੈਸ਼-ਰੋਕੂ (anti-caching) HTTP ਜਵਾਬ ਹੈੱਡਰ ਖੇਤਰ (ਭਾਵ, Cache-Control: no-store) ਸੈੱਟ ਕਰਦੀ ਹੈ ਤਾਂ ਜੋ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਬ੍ਰਾਊਜ਼ਰਾਂ ਵਿੱਚ ਕੈਸ਼ ਨਾ ਹੋਵੇ। | 2 |
| **14.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬ੍ਰਾਊਜ਼ਰ ਭੰਡਾਰਨ (ਜਿਵੇਂ ਕਿ localStorage, sessionStorage, IndexedDB, ਜਾਂ ਕੁਕੀਆਂ) ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਡਾਟੇ ਵਿੱਚ, ਸੈਸ਼ਨ ਟੋਕਨਾਂ ਨੂੰ ਛੱਡ ਕੇ, ਕੋਈ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਸ਼ਾਮਲ ਨਹੀਂ ਹੁੰਦਾ। | 2 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [Consider using the Security Headers website to check security and anti-caching header fields](https://securityheaders.com/)
* [Documentation about anti-caching headers by Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Australian Privacy Principle 11 - Security of personal information](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information)
* [European Union General Data Protection Regulation (GDPR) overview](https://www.edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://www.edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
* [Information on the "Clear-Site-Data" header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
* [White paper on Web Cache Deception](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)
