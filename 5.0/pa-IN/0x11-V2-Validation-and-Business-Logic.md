<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x11-V2-Validation-and-Business-Logic.md -->
<!-- Translator: GeeksikhSecurity -->

# V2 Validation and Business Logic
# V2 ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਕਾਰੋਬਾਰੀ ਤਰਕ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

This chapter aims to ensure that a verified application meets the following high-level goals:

ਇਸ ਅਧਿਆਇ ਦਾ ਉਦੇਸ਼ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਇੱਕ ਤਸਦੀਕ ਕੀਤੀ ਐਪਲੀਕੇਸ਼ਨ ਹੇਠ ਲਿਖੇ ਉੱਚ-ਪੱਧਰੀ ਟੀਚਿਆਂ ਨੂੰ ਪੂਰਾ ਕਰਦੀ ਹੈ:

* Input received by the application matches business or functional expectations.
* The business logic flow is sequential, processed in order, and cannot be bypassed.
* Business logic includes limits and controls to detect and prevent automated attacks, such as continuous small funds transfers or adding a million friends one at a time.
* High-value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, information disclosure, and elevation of privilege attacks.

* ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਪ੍ਰਾਪਤ ਇਨਪੁੱਟ ਕਾਰੋਬਾਰੀ ਜਾਂ ਕਾਰਜਾਤਮਕ ਉਮੀਦਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।
* ਕਾਰੋਬਾਰੀ ਤਰਕ (business logic) ਦਾ ਪ੍ਰਵਾਹ ਕ੍ਰਮਵਾਰ ਹੈ, ਤਰਤੀਬ ਵਿੱਚ ਪ੍ਰਕਿਰਿਆ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਇਸ ਨੂੰ ਬਾਈਪਾਸ (bypass) ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ।
* ਕਾਰੋਬਾਰੀ ਤਰਕ ਵਿੱਚ ਸਵੈਚਾਲਿਤ ਹਮਲਿਆਂ (automated attacks) ਦਾ ਪਤਾ ਲਗਾਉਣ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਰੋਕਣ ਲਈ ਸੀਮਾਵਾਂ ਅਤੇ ਨਿਯੰਤਰਣ ਸ਼ਾਮਲ ਹਨ, ਜਿਵੇਂ ਕਿ ਲਗਾਤਾਰ ਛੋਟੇ ਫ਼ੰਡ ਤਬਾਦਲੇ ਜਾਂ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਦਸ ਲੱਖ ਦੋਸਤ ਜੋੜਨਾ।
* ਉੱਚ-ਮੁੱਲ ਵਾਲੇ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪ੍ਰਵਾਹਾਂ ਵਿੱਚ ਦੁਰਵਰਤੋਂ ਦੇ ਮਾਮਲਿਆਂ (abuse cases) ਅਤੇ ਭੈੜੀ ਨੀਅਤ ਵਾਲੇ ਕਰਤਿਆਂ 'ਤੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਹੈ, ਅਤੇ ਸਪੂਫ਼ਿੰਗ (spoofing), ਛੇੜਛਾੜ, ਜਾਣਕਾਰੀ ਦੇ ਖੁਲਾਸੇ, ਅਤੇ ਅਧਿਕਾਰ-ਵਾਧੇ (elevation of privilege) ਦੇ ਹਮਲਿਆਂ ਵਿਰੁੱਧ ਸੁਰੱਖਿਆਵਾਂ ਮੌਜੂਦ ਹਨ।

## V2.1 Validation and Business Logic Documentation
## V2.1 ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਕਾਰੋਬਾਰੀ ਤਰਕ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

Validation and business logic documentation should clearly define business logic limits, validation rules, and contextual consistency of combined data items, so it is clear what needs to be implemented in the application.

ਪ੍ਰਮਾਣਿਕਤਾ (validation) ਅਤੇ ਕਾਰੋਬਾਰੀ ਤਰਕ ਦੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨੂੰ ਕਾਰੋਬਾਰੀ ਤਰਕ ਦੀਆਂ ਸੀਮਾਵਾਂ, ਪ੍ਰਮਾਣਿਕਤਾ ਨਿਯਮਾਂ, ਅਤੇ ਸੰਯੁਕਤ ਡਾਟਾ ਇਕਾਈਆਂ ਦੀ ਸੰਦਰਭੀ ਇਕਸਾਰਤਾ ਨੂੰ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, ਤਾਂ ਜੋ ਇਹ ਸਪੱਸ਼ਟ ਹੋਵੇ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਕੀ ਲਾਗੂ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **2.1.1** | Verify that the application's documentation defines input validation rules for how to check the validity of data items against an expected structure. This could be common data formats such as credit card numbers, email addresses, telephone numbers, or it could be an internal data format. | 1 |
| **2.1.2** | Verify that the application's documentation defines how to validate the logical and contextual consistency of combined data items, such as checking that suburb and ZIP code match. | 2 |
| **2.1.3** | Verify that expectations for business logic limits and validations are documented, including both per-user and globally across the application. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **2.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਨਿਯਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਡਾਟਾ ਇਕਾਈਆਂ ਦੀ ਜਾਇਜ਼ਤਾ ਦੀ ਜਾਂਚ ਇੱਕ ਅਨੁਮਾਨਿਤ ਬਣਤਰ ਦੇ ਵਿਰੁੱਧ ਕਿਵੇਂ ਕੀਤੀ ਜਾਵੇ। ਇਹ ਆਮ ਡਾਟਾ ਫਾਰਮੈਟ ਹੋ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਕਿ ਕ੍ਰੈਡਿਟ ਕਾਰਡ ਨੰਬਰ, ਈਮੇਲ ਪਤੇ, ਟੈਲੀਫ਼ੋਨ ਨੰਬਰ, ਜਾਂ ਇਹ ਕੋਈ ਅੰਦਰੂਨੀ ਡਾਟਾ ਫਾਰਮੈਟ ਹੋ ਸਕਦਾ ਹੈ। | 1 |
| **2.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਸੰਯੁਕਤ ਡਾਟਾ ਇਕਾਈਆਂ ਦੀ ਤਾਰਕਿਕ ਅਤੇ ਸੰਦਰਭੀ ਇਕਸਾਰਤਾ ਨੂੰ ਕਿਵੇਂ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਇਹ ਜਾਂਚ ਕਰਨਾ ਕਿ ਉਪਨਗਰ ਅਤੇ ZIP ਕੋਡ ਮੇਲ ਖਾਂਦੇ ਹਨ। | 2 |
| **2.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਾਰੋਬਾਰੀ ਤਰਕ ਦੀਆਂ ਸੀਮਾਵਾਂ ਅਤੇ ਪ੍ਰਮਾਣਿਕਤਾਵਾਂ ਲਈ ਉਮੀਦਾਂ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਵਿੱਚ ਦਰਜ ਹਨ, ਜਿਸ ਵਿੱਚ ਪ੍ਰਤੀ-ਉਪਭੋਗਤਾ ਅਤੇ ਪੂਰੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸਮੁੱਚੇ ਤੌਰ 'ਤੇ, ਦੋਵੇਂ ਸ਼ਾਮਲ ਹਨ। | 2 |

## V2.2 Input Validation
## V2.2 ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ

Effective input validation controls enforce business or functional expectations around the type of data the application expects to receive. This ensures good data quality and reduces the attack surface. However, it does not remove or replace the need to use correct encoding, parameterization, or sanitization when using the data in another component or for presenting it for output.

ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਨਿਯੰਤਰਣ ਉਸ ਡਾਟਾ ਦੀ ਕਿਸਮ ਬਾਰੇ ਕਾਰੋਬਾਰੀ ਜਾਂ ਕਾਰਜਾਤਮਕ ਉਮੀਦਾਂ ਨੂੰ ਲਾਗੂ ਕਰਦੇ ਹਨ ਜਿਸ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਉਮੀਦ ਰੱਖਦੀ ਹੈ। ਇਹ ਚੰਗੀ ਡਾਟਾ ਗੁਣਵੱਤਾ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਹਮਲਾ ਸਤ੍ਹਾ (attack surface) ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ। ਹਾਲਾਂਕਿ, ਇਹ ਕਿਸੇ ਹੋਰ ਹਿੱਸੇ ਵਿੱਚ ਡਾਟਾ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ ਜਾਂ ਇਸ ਨੂੰ ਆਉਟਪੁੱਟ ਲਈ ਪੇਸ਼ ਕਰਦੇ ਸਮੇਂ ਸਹੀ ਏਨਕੋਡਿੰਗ, ਪੈਰਾਮੀਟਰਾਈਜ਼ੇਸ਼ਨ, ਜਾਂ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਨੂੰ ਨਾ ਹਟਾਉਂਦਾ ਹੈ ਅਤੇ ਨਾ ਹੀ ਉਸ ਦੀ ਥਾਂ ਲੈਂਦਾ ਹੈ।

In this context, "input" could come from a wide variety of sources, including HTML form fields, REST requests, URL parameters, HTTP header fields, cookies, files on disk, databases, and external APIs.

ਇਸ ਸੰਦਰਭ ਵਿੱਚ, "ਇਨਪੁੱਟ" ਕਈ ਤਰ੍ਹਾਂ ਦੇ ਸਰੋਤਾਂ ਤੋਂ ਆ ਸਕਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ HTML ਫਾਰਮ ਖੇਤਰ, REST ਬੇਨਤੀਆਂ, URL ਪੈਰਾਮੀਟਰ, HTTP ਹੈਡਰ ਖੇਤਰ, ਕੁਕੀਜ਼, ਡਿਸਕ 'ਤੇ ਫ਼ਾਈਲਾਂ, ਡਾਟਾਬੇਸ, ਅਤੇ ਬਾਹਰੀ API ਸ਼ਾਮਲ ਹਨ।

A business logic control might check that a particular input is a number less than 100. A functional expectation might check that a number is below a certain threshold, as that number controls how many times a particular loop will take place, and a high number could lead to excessive processing and a potential denial of service condition.

ਇੱਕ ਕਾਰੋਬਾਰੀ ਤਰਕ ਨਿਯੰਤਰਣ ਇਹ ਜਾਂਚ ਕਰ ਸਕਦਾ ਹੈ ਕਿ ਕੋਈ ਖ਼ਾਸ ਇਨਪੁੱਟ 100 ਤੋਂ ਘੱਟ ਦੀ ਇੱਕ ਸੰਖਿਆ ਹੈ। ਇੱਕ ਕਾਰਜਾਤਮਕ ਉਮੀਦ ਇਹ ਜਾਂਚ ਕਰ ਸਕਦੀ ਹੈ ਕਿ ਕੋਈ ਸੰਖਿਆ ਇੱਕ ਨਿਸ਼ਚਿਤ ਹੱਦ ਤੋਂ ਹੇਠਾਂ ਹੈ, ਕਿਉਂਕਿ ਉਹ ਸੰਖਿਆ ਇਹ ਨਿਯੰਤਰਿਤ ਕਰਦੀ ਹੈ ਕਿ ਕੋਈ ਖ਼ਾਸ ਲੂਪ ਕਿੰਨੀ ਵਾਰ ਚੱਲੇਗਾ, ਅਤੇ ਇੱਕ ਵੱਡੀ ਸੰਖਿਆ ਬਹੁਤ ਜ਼ਿਆਦਾ ਪ੍ਰਕਿਰਿਆ ਅਤੇ ਇੱਕ ਸੰਭਾਵੀ ਸੇਵਾ-ਇਨਕਾਰ (denial of service) ਦੀ ਹਾਲਤ ਵੱਲ ਲੈ ਜਾ ਸਕਦੀ ਹੈ।

While schema validation is not explicitly mandated, it may be the most effective mechanism for full validation coverage of HTTP APIs or other interfaces that use JSON or XML.

ਭਾਵੇਂ ਸਕੀਮਾ ਪ੍ਰਮਾਣਿਕਤਾ (schema validation) ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਲਾਜ਼ਮੀ ਨਹੀਂ ਕੀਤੀ ਗਈ, ਇਹ HTTP API ਜਾਂ JSON ਜਾਂ XML ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਾਲੇ ਹੋਰ ਇੰਟਰਫ਼ੇਸਾਂ ਦੀ ਪੂਰੀ ਪ੍ਰਮਾਣਿਕਤਾ ਕਵਰੇਜ ਲਈ ਸਭ ਤੋਂ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਪ੍ਰਣਾਲੀ ਹੋ ਸਕਦੀ ਹੈ।

Please note the following points on Schema Validation:

ਕਿਰਪਾ ਕਰਕੇ ਸਕੀਮਾ ਪ੍ਰਮਾਣਿਕਤਾ ਬਾਰੇ ਹੇਠ ਲਿਖੇ ਨੁਕਤਿਆਂ ਵੱਲ ਧਿਆਨ ਦਿਓ:

* The "published version" of the JSON Schema validation specification is considered production-ready, but not strictly speaking "stable." When using JSON Schema validation, ensure there are no gaps with the guidance in the requirements below.
* Any JSON Schema validation libraries in use should also be monitored and updated if necessary once the standard is formalized.
* DTD validation should not be used, and framework DTD evaluation should be disabled, to avoid issues with XXE attacks against DTDs.

* JSON Schema ਪ੍ਰਮਾਣਿਕਤਾ ਨਿਰਧਾਰਨ ਦਾ "ਪ੍ਰਕਾਸ਼ਿਤ ਸੰਸਕਰਣ" ਉਤਪਾਦਨ-ਤਿਆਰ (production-ready) ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ, ਪਰ ਸਖ਼ਤੀ ਨਾਲ ਕਹੀਏ ਤਾਂ "ਸਥਿਰ" ਨਹੀਂ। JSON Schema ਪ੍ਰਮਾਣਿਕਤਾ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਲੋੜਾਂ ਵਿਚਲੇ ਮਾਰਗਦਰਸ਼ਨ ਨਾਲ ਕੋਈ ਪਾੜਾ ਨਾ ਹੋਵੇ।
* ਵਰਤੋਂ ਵਿੱਚ ਆਉਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ JSON Schema ਪ੍ਰਮਾਣਿਕਤਾ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਵੀ ਨਿਗਰਾਨੀ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ ਅਤੇ ਮਿਆਰ ਦੇ ਰਸਮੀ ਰੂਪ ਧਾਰਨ ਕਰਨ 'ਤੇ, ਜੇ ਲੋੜ ਹੋਵੇ, ਉਹਨਾਂ ਨੂੰ ਅੱਪਡੇਟ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।
* DTD ਪ੍ਰਮਾਣਿਕਤਾ ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ, ਅਤੇ DTD ਦੇ ਵਿਰੁੱਧ XXE ਹਮਲਿਆਂ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਤੋਂ ਬਚਣ ਲਈ ਫ੍ਰੇਮਵਰਕ ਦਾ DTD ਮੁਲਾਂਕਣ ਅਸਮਰੱਥ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **2.2.1** | Verify that input is validated to enforce business or functional expectations for that input. This should either use positive validation against an allow list of values, patterns, and ranges, or be based on comparing the input to an expected structure and logical limits according to predefined rules. For L1, this can focus on input which is used to make specific business or security decisions. For L2 and up, this should apply to all input. | 1 |
| **2.2.2** | Verify that the application is designed to enforce input validation at a trusted service layer. While client-side validation improves usability and should be encouraged, it must not be relied upon as a security control. | 1 |
| **2.2.3** | Verify that the application ensures that combinations of related data items are reasonable according to the pre-defined rules. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **2.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇਨਪੁੱਟ ਨੂੰ ਉਸ ਇਨਪੁੱਟ ਲਈ ਕਾਰੋਬਾਰੀ ਜਾਂ ਕਾਰਜਾਤਮਕ ਉਮੀਦਾਂ ਲਾਗੂ ਕਰਨ ਲਈ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਜਾਂ ਤਾਂ ਮੁੱਲਾਂ, ਪੈਟਰਨਾਂ, ਅਤੇ ਰੇਂਜਾਂ ਦੀ ਇੱਕ allowlist ਦੇ ਵਿਰੁੱਧ ਸਕਾਰਾਤਮਕ ਪ੍ਰਮਾਣਿਕਤਾ ਵਰਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ, ਜਾਂ ਇਹ ਪਹਿਲਾਂ ਤੋਂ ਪਰਿਭਾਸ਼ਿਤ ਨਿਯਮਾਂ ਦੇ ਅਨੁਸਾਰ ਇਨਪੁੱਟ ਦੀ ਇੱਕ ਅਨੁਮਾਨਿਤ ਬਣਤਰ ਅਤੇ ਤਾਰਕਿਕ ਸੀਮਾਵਾਂ ਨਾਲ ਤੁਲਨਾ 'ਤੇ ਆਧਾਰਿਤ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। L1 ਲਈ, ਇਹ ਉਸ ਇਨਪੁੱਟ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਹੋ ਸਕਦਾ ਹੈ ਜੋ ਖ਼ਾਸ ਕਾਰੋਬਾਰੀ ਜਾਂ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ ਲੈਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। L2 ਅਤੇ ਉੱਪਰ ਲਈ, ਇਹ ਸਾਰੇ ਇਨਪੁੱਟ 'ਤੇ ਲਾਗੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। | 1 |
| **2.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਇੱਕ ਭਰੋਸੇਯੋਗ ਸੇਵਾ ਪਰਤ 'ਤੇ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਲਾਗੂ ਕਰਨ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਭਾਵੇਂ ਕਲਾਇੰਟ-ਸਾਈਡ ਪ੍ਰਮਾਣਿਕਤਾ ਵਰਤੋਂਯੋਗਤਾ ਵਿੱਚ ਸੁਧਾਰ ਕਰਦੀ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸ 'ਤੇ ਇੱਕ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਵਜੋਂ ਭਰੋਸਾ ਨਾ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ। | 1 |
| **2.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਸੰਬੰਧਿਤ ਡਾਟਾ ਇਕਾਈਆਂ ਦੇ ਸੁਮੇਲ ਪਹਿਲਾਂ ਤੋਂ ਪਰਿਭਾਸ਼ਿਤ ਨਿਯਮਾਂ ਦੇ ਅਨੁਸਾਰ ਵਾਜਬ ਹਨ। | 2 |

## V2.3 Business Logic Security
## V2.3 ਕਾਰੋਬਾਰੀ ਤਰਕ ਸੁਰੱਖਿਆ

This section considers key requirements to ensure that the application enforces business logic processes in the correct way and is not vulnerable to attacks that exploit the logic and flow of the application.

ਇਹ ਭਾਗ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਮੁੱਖ ਲੋੜਾਂ 'ਤੇ ਵਿਚਾਰ ਕਰਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਲਾਗੂ ਕਰਦੀ ਹੈ ਅਤੇ ਉਹਨਾਂ ਹਮਲਿਆਂ ਲਈ ਕਮਜ਼ੋਰ ਨਹੀਂ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਤਰਕ ਅਤੇ ਪ੍ਰਵਾਹ ਦਾ ਸ਼ੋਸ਼ਣ ਕਰਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **2.3.1** | Verify that the application will only process business logic flows for the same user in the expected sequential step order and without skipping steps. | 1 |
| **2.3.2** | Verify that business logic limits are implemented per the application's documentation to avoid business logic flaws being exploited. | 2 |
| **2.3.3** | Verify that transactions are being used at the business logic level such that either a business logic operation succeeds in its entirety or it is rolled back to the previous correct state. | 2 |
| **2.3.4** | Verify that business logic level locking mechanisms are used to ensure that limited quantity resources (such as theater seats or delivery slots) cannot be double-booked by manipulating the application's logic. | 2 |
| **2.3.5** | Verify that high-value business logic flows require multi-user approval to prevent unauthorized or accidental actions. This could include but is not limited to large monetary transfers, contract approvals, access to classified information, or safety overrides in manufacturing. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **2.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਇੱਕੋ ਉਪਭੋਗਤਾ ਲਈ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪ੍ਰਵਾਹਾਂ ਨੂੰ ਸਿਰਫ਼ ਅਨੁਮਾਨਿਤ ਕ੍ਰਮਵਾਰ ਕਦਮ ਤਰਤੀਬ ਵਿੱਚ ਅਤੇ ਕਦਮ ਛੱਡੇ ਬਿਨਾਂ ਹੀ ਪ੍ਰਕਿਰਿਆ ਕਰੇਗੀ। | 1 |
| **2.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਾਰੋਬਾਰੀ ਤਰਕ ਦੀਆਂ ਖ਼ਾਮੀਆਂ ਦੇ ਸ਼ੋਸ਼ਣ ਤੋਂ ਬਚਣ ਲਈ ਕਾਰੋਬਾਰੀ ਤਰਕ ਦੀਆਂ ਸੀਮਾਵਾਂ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦੇ ਅਨੁਸਾਰ ਲਾਗੂ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। | 2 |
| **2.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪੱਧਰ 'ਤੇ ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨਾਂ (transactions) ਦੀ ਵਰਤੋਂ ਇਸ ਤਰ੍ਹਾਂ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ ਕਿ ਜਾਂ ਤਾਂ ਇੱਕ ਕਾਰੋਬਾਰੀ ਤਰਕ ਕਾਰਜ ਆਪਣੀ ਸਮੁੱਚਤਾ ਵਿੱਚ ਸਫਲ ਹੁੰਦਾ ਹੈ ਜਾਂ ਇਸ ਨੂੰ ਪਿਛਲੀ ਸਹੀ ਸਥਿਤੀ 'ਤੇ ਵਾਪਸ ਮੋੜ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। | 2 |
| **2.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪੱਧਰ ਦੀਆਂ ਲਾਕਿੰਗ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਵਰਤੋਂ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਸੀਮਤ ਮਾਤਰਾ ਵਾਲੇ ਸਰੋਤਾਂ (ਜਿਵੇਂ ਕਿ ਥੀਏਟਰ ਦੀਆਂ ਸੀਟਾਂ ਜਾਂ ਡਿਲੀਵਰੀ ਸਲਾਟ) ਦੀ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਤਰਕ ਨਾਲ ਹੇਰਾਫੇਰੀ ਕਰਕੇ ਦੋਹਰੀ-ਬੁਕਿੰਗ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕਦੀ। | 2 |
| **2.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉੱਚ-ਮੁੱਲ ਵਾਲੇ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪ੍ਰਵਾਹਾਂ ਲਈ ਅਣਅਧਿਕਾਰਤ ਜਾਂ ਗ਼ਲਤੀ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਾਰਵਾਈਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਬਹੁ-ਉਪਭੋਗਤਾ ਮਨਜ਼ੂਰੀ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਇਸ ਵਿੱਚ ਵੱਡੀ ਰਕਮ ਦੇ ਤਬਾਦਲੇ, ਇਕਰਾਰਨਾਮੇ ਦੀਆਂ ਮਨਜ਼ੂਰੀਆਂ, ਵਰਗੀਕ੍ਰਿਤ ਜਾਣਕਾਰੀ ਤੱਕ ਪਹੁੰਚ, ਜਾਂ ਨਿਰਮਾਣ ਵਿੱਚ ਸੁਰੱਖਿਆ ਓਵਰਰਾਈਡ (safety overrides) ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ, ਪਰ ਇਹ ਇਹਨਾਂ ਤੱਕ ਸੀਮਤ ਨਹੀਂ ਹੈ। | 3 |

## V2.4 Anti-automation
## V2.4 ਸਵੈਚਾਲਨ-ਵਿਰੋਧੀ

This section includes anti-automation controls to ensure that human-like interactions are required and excessive automated requests are prevented.

ਇਸ ਭਾਗ ਵਿੱਚ ਸਵੈਚਾਲਨ-ਵਿਰੋਧੀ (anti-automation) ਨਿਯੰਤਰਣ ਸ਼ਾਮਲ ਹਨ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਮਨੁੱਖ-ਵਰਗੀਆਂ ਆਪਸੀ ਕਿਰਿਆਵਾਂ ਲੋੜੀਂਦੀਆਂ ਹਨ ਅਤੇ ਬਹੁਤ ਜ਼ਿਆਦਾ ਸਵੈਚਾਲਿਤ ਬੇਨਤੀਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾਂਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **2.4.1** | Verify that anti-automation controls are in place to protect against excessive calls to application functions that could lead to data exfiltration, garbage-data creation, quota exhaustion, rate-limit breaches, denial-of-service, or overuse of costly resources. | 2 |
| **2.4.2** | Verify that business logic flows require realistic human timing, preventing excessively rapid transaction submissions. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **2.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਅਜਿਹੀਆਂ ਬਹੁਤ ਜ਼ਿਆਦਾ ਕਾਲਾਂ ਤੋਂ ਬਚਾਅ ਲਈ ਸਵੈਚਾਲਨ-ਵਿਰੋਧੀ ਨਿਯੰਤਰਣ ਮੌਜੂਦ ਹਨ ਜੋ ਡਾਟਾ ਨਿਕਾਸੀ (data exfiltration), ਕੂੜਾ-ਡਾਟਾ ਸਿਰਜਣਾ, ਕੋਟਾ ਖ਼ਤਮ ਹੋ ਜਾਣਾ (quota exhaustion), ਦਰ-ਸੀਮਾ ਉਲੰਘਣਾਵਾਂ, ਸੇਵਾ-ਇਨਕਾਰ, ਜਾਂ ਮਹਿੰਗੇ ਸਰੋਤਾਂ ਦੀ ਬਹੁਤ ਜ਼ਿਆਦਾ ਵਰਤੋਂ ਵੱਲ ਲੈ ਜਾ ਸਕਦੀਆਂ ਹਨ। | 2 |
| **2.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪ੍ਰਵਾਹਾਂ ਲਈ ਯਥਾਰਥਕ ਮਨੁੱਖੀ ਸਮੇਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਜੋ ਬਹੁਤ ਜ਼ਿਆਦਾ ਤੇਜ਼ ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨ ਸਪੁਰਦਗੀਆਂ ਨੂੰ ਰੋਕਦੀ ਹੈ। | 3 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP Web Security Testing Guide: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Web Security Testing Guide: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Anti-automation can be achieved in many ways, including the use of the [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [JSON Schema](https://json-schema.org/specification.html)
