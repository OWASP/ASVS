<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x17-V8-Authorization.md -->
<!-- Translator: GeeksikhSecurity -->

# V8 Authorization
# V8 ਅਧਿਕਾਰੀਕਰਨ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Authorization ensures that access is granted only to permitted consumers (users, servers, and other clients). To enforce the Principle of Least Privilege (POLP), verified applications must meet the following high-level requirements:

ਅਧਿਕਾਰੀਕਰਨ (Authorization) ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਪਹੁੰਚ ਸਿਰਫ਼ ਇਜਾਜ਼ਤ ਪ੍ਰਾਪਤ ਖਪਤਕਾਰਾਂ (ਉਪਭੋਗਤਾਵਾਂ, ਸਰਵਰਾਂ, ਅਤੇ ਹੋਰ ਕਲਾਇੰਟਾਂ) ਨੂੰ ਹੀ ਦਿੱਤੀ ਜਾਵੇ. ਘੱਟੋ-ਘੱਟ ਅਧਿਕਾਰ ਦਾ ਸਿਧਾਂਤ (Principle of Least Privilege, POLP) ਲਾਗੂ ਕਰਨ ਲਈ, ਤਸਦੀਕ ਕੀਤੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਹੇਠ ਲਿਖੀਆਂ ਉੱਚ-ਪੱਧਰੀ ਲੋੜਾਂ ਪੂਰੀਆਂ ਕਰਨੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ:

* Document authorization rules, including decision-making factors and environmental contexts.
* Consumers should have access only to resources permitted by their defined entitlements.

* ਅਧਿਕਾਰੀਕਰਨ ਨਿਯਮਾਂ ਨੂੰ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦਿਓ, ਜਿਸ ਵਿੱਚ ਫ਼ੈਸਲਾ ਲੈਣ ਵਾਲੇ ਕਾਰਕ ਅਤੇ ਵਾਤਾਵਰਣੀ ਸੰਦਰਭ ਸ਼ਾਮਲ ਹਨ.
* ਖਪਤਕਾਰਾਂ ਕੋਲ ਸਿਰਫ਼ ਉਹਨਾਂ ਸਰੋਤਾਂ ਤੱਕ ਪਹੁੰਚ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਜੋ ਉਹਨਾਂ ਦੇ ਪਰਿਭਾਸ਼ਿਤ ਹੱਕਾਂ (entitlements) ਦੁਆਰਾ ਇਜਾਜ਼ਤ ਪ੍ਰਾਪਤ ਹਨ.

## V8.1 Authorization Documentation
## V8.1 ਅਧਿਕਾਰੀਕਰਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

Comprehensive authorization documentation is essential to ensure that security decisions are consistently applied, auditable, and aligned with organizational policies. This reduces the risk of unauthorized access by making security requirements clear and actionable for developers, administrators, and testers.

ਵਿਆਪਕ ਅਧਿਕਾਰੀਕਰਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ ਨਿਰੰਤਰ ਲਾਗੂ ਹੋਣ, ਆਡਿਟ ਕਰਨ ਯੋਗ ਹੋਣ, ਅਤੇ ਸੰਸਥਾਗਤ ਨੀਤੀਆਂ ਨਾਲ ਮੇਲ ਖਾਣ. ਇਹ ਵਿਕਾਸਕਾਰਾਂ, ਪ੍ਰਸ਼ਾਸਕਾਂ, ਅਤੇ ਟੈਸਟਰਾਂ ਲਈ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਨੂੰ ਸਪੱਸ਼ਟ ਅਤੇ ਕਾਰਜਯੋਗ ਬਣਾ ਕੇ ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ ਦੇ ਖ਼ਤਰੇ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ.

| # | Description | Level |
| :---: | :--- | :---: |
| **8.1.1** | Verify that authorization documentation defines rules for restricting function-level and data-specific access based on consumer permissions and resource attributes. | 1 |
| **8.1.2** | Verify that authorization documentation defines rules for field-level access restrictions (both read and write) based on consumer permissions and resource attributes. Note that these rules might depend on other attribute values of the relevant data object, such as state or status. | 2 |
| **8.1.3** | Verify that the application's documentation defines the environmental and contextual attributes (including but not limited to, time of day, user location, IP address, or device) that are used in the application to make security decisions, including those pertaining to authentication and authorization. | 3 |
| **8.1.4** | Verify that authentication and authorization documentation defines how environmental and contextual factors are used in decision-making, in addition to function-level, data-specific, and field-level authorization. This should include the attributes evaluated, thresholds for risk, and actions taken (e.g., allow, challenge, deny, step-up authentication). | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **8.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅਧਿਕਾਰੀਕਰਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਖਪਤਕਾਰ ਇਜਾਜ਼ਤਾਂ ਅਤੇ ਸਰੋਤ ਗੁਣਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਫੰਕਸ਼ਨ-ਪੱਧਰ ਅਤੇ ਡਾਟਾ-ਖ਼ਾਸ ਪਹੁੰਚ ਨੂੰ ਪ੍ਰਤਿਬੰਧਿਤ ਕਰਨ ਲਈ ਨਿਯਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ. | ੧ |
| **8.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅਧਿਕਾਰੀਕਰਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਖਪਤਕਾਰ ਇਜਾਜ਼ਤਾਂ ਅਤੇ ਸਰੋਤ ਗੁਣਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਖੇਤਰ-ਪੱਧਰ ਪਹੁੰਚ ਪ੍ਰਤਿਬੰਧਾਂ (ਪੜ੍ਹਨ ਅਤੇ ਲਿਖਣ ਦੋਵਾਂ) ਲਈ ਨਿਯਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ. ਧਿਆਨ ਦਿਓ ਕਿ ਇਹ ਨਿਯਮ ਸੰਬੰਧਤ ਡਾਟਾ ਆਬਜੈਕਟ ਦੇ ਹੋਰ ਗੁਣ ਮੁੱਲਾਂ, ਜਿਵੇਂ ਕਿ ਸਥਿਤੀ ਜਾਂ ਅਵਸਥਾ, 'ਤੇ ਨਿਰਭਰ ਹੋ ਸਕਦੇ ਹਨ. | ੨ |
| **8.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਉਹਨਾਂ ਵਾਤਾਵਰਣੀ ਅਤੇ ਸੰਦਰਭੀ ਗੁਣਾਂ (ਦਿਨ ਦਾ ਸਮਾਂ, ਉਪਭੋਗਤਾ ਟਿਕਾਣਾ, IP ਪਤਾ, ਜਾਂ ਡਿਵਾਈਸ ਸਮੇਤ ਪਰ ਇਹਨਾਂ ਤੱਕ ਸੀਮਤ ਨਹੀਂ) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ ਲੈਣ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਜਿਸ ਵਿੱਚ ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਅਧਿਕਾਰੀਕਰਨ ਨਾਲ ਸੰਬੰਧਤ ਫ਼ੈਸਲੇ ਸ਼ਾਮਲ ਹਨ. | ੩ |
| **8.1.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਅਧਿਕਾਰੀਕਰਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਫੰਕਸ਼ਨ-ਪੱਧਰ, ਡਾਟਾ-ਖ਼ਾਸ, ਅਤੇ ਖੇਤਰ-ਪੱਧਰ ਅਧਿਕਾਰੀਕਰਨ ਤੋਂ ਇਲਾਵਾ, ਫ਼ੈਸਲਾ ਲੈਣ ਵਿੱਚ ਵਾਤਾਵਰਣੀ ਅਤੇ ਸੰਦਰਭੀ ਕਾਰਕਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ. ਇਸ ਵਿੱਚ ਮੁਲਾਂਕਣ ਕੀਤੇ ਗਏ ਗੁਣ, ਖ਼ਤਰੇ ਦੀਆਂ ਹੱਦਾਂ, ਅਤੇ ਚੁੱਕੀਆਂ ਗਈਆਂ ਕਾਰਵਾਈਆਂ (ਜਿਵੇਂ ਕਿ ਇਜਾਜ਼ਤ, ਚੁਣੌਤੀ, ਇਨਕਾਰ, ਸਟੈਪ-ਅੱਪ ਪ੍ਰਮਾਣੀਕਰਨ) ਸ਼ਾਮਲ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ. | ੩ |

## V8.2 General Authorization Design
## V8.2 ਆਮ ਅਧਿਕਾਰੀਕਰਨ ਡਿਜ਼ਾਈਨ

Implementing granular authorization controls at the function, data, and field levels ensures that consumers can access only what has been explicitly granted to them.

ਫੰਕਸ਼ਨ, ਡਾਟਾ, ਅਤੇ ਖੇਤਰ ਪੱਧਰਾਂ 'ਤੇ ਬਾਰੀਕ ਅਧਿਕਾਰੀਕਰਨ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨਾ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਖਪਤਕਾਰ ਸਿਰਫ਼ ਉਹੀ ਪਹੁੰਚ ਕਰ ਸਕਣ ਜੋ ਉਹਨਾਂ ਨੂੰ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਪ੍ਰਦਾਨ ਕੀਤੀ ਗਈ ਹੈ.

| # | Description | Level |
| :---: | :--- | :---: |
| **8.2.1** | Verify that the application ensures that function-level access is restricted to consumers with explicit permissions. | 1 |
| **8.2.2** | Verify that the application ensures that data-specific access is restricted to consumers with explicit permissions to specific data items to mitigate insecure direct object reference (IDOR) and broken object level authorization (BOLA). | 1 |
| **8.2.3** | Verify that the application ensures that field-level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA). | 2 |
| **8.2.4** | Verify that adaptive security controls based on a consumer's environmental and contextual attributes (such as time of day, location, IP address, or device) are implemented for authentication and authorization decisions, as defined in the application's documentation. These controls must be applied when the consumer tries to start a new session and also during an existing session. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **8.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਫੰਕਸ਼ਨ-ਪੱਧਰ ਪਹੁੰਚ ਸਪੱਸ਼ਟ ਇਜਾਜ਼ਤਾਂ ਵਾਲੇ ਖਪਤਕਾਰਾਂ ਤੱਕ ਪ੍ਰਤਿਬੰਧਿਤ ਹੈ. | ੧ |
| **8.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਅਸੁਰੱਖਿਅਤ ਸਿੱਧੇ ਆਬਜੈਕਟ ਹਵਾਲੇ (IDOR) ਅਤੇ ਟੁੱਟੇ ਆਬਜੈਕਟ ਪੱਧਰ ਅਧਿਕਾਰੀਕਰਨ (BOLA) ਨੂੰ ਘਟਾਉਣ ਲਈ ਡਾਟਾ-ਖ਼ਾਸ ਪਹੁੰਚ ਖ਼ਾਸ ਡਾਟਾ ਇਕਾਈਆਂ ਲਈ ਸਪੱਸ਼ਟ ਇਜਾਜ਼ਤਾਂ ਵਾਲੇ ਖਪਤਕਾਰਾਂ ਤੱਕ ਪ੍ਰਤਿਬੰਧਿਤ ਹੈ. | ੧ |
| **8.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਟੁੱਟੇ ਆਬਜੈਕਟ ਵਿਸ਼ੇਸ਼ਤਾ ਪੱਧਰ ਅਧਿਕਾਰੀਕਰਨ (BOPLA) ਨੂੰ ਘਟਾਉਣ ਲਈ ਖੇਤਰ-ਪੱਧਰ ਪਹੁੰਚ ਖ਼ਾਸ ਖੇਤਰਾਂ ਲਈ ਸਪੱਸ਼ਟ ਇਜਾਜ਼ਤਾਂ ਵਾਲੇ ਖਪਤਕਾਰਾਂ ਤੱਕ ਪ੍ਰਤਿਬੰਧਿਤ ਹੈ. | ੨ |
| **8.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਖਪਤਕਾਰ ਦੇ ਵਾਤਾਵਰਣੀ ਅਤੇ ਸੰਦਰਭੀ ਗੁਣਾਂ (ਜਿਵੇਂ ਕਿ ਦਿਨ ਦਾ ਸਮਾਂ, ਟਿਕਾਣਾ, IP ਪਤਾ, ਜਾਂ ਡਿਵਾਈਸ) 'ਤੇ ਆਧਾਰਿਤ ਅਨੁਕੂਲਿਤ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਅਧਿਕਾਰੀਕਰਨ ਫ਼ੈਸਲਿਆਂ ਲਈ ਲਾਗੂ ਕੀਤੇ ਗਏ ਹਨ, ਜਿਵੇਂ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਹੈ. ਇਹ ਨਿਯੰਤਰਣ ਉਦੋਂ ਲਾਗੂ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ ਜਦੋਂ ਖਪਤਕਾਰ ਨਵਾਂ ਸੈਸ਼ਨ ਸ਼ੁਰੂ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ ਅਤੇ ਮੌਜੂਦਾ ਸੈਸ਼ਨ ਦੌਰਾਨ ਵੀ. | ੩ |

## V8.3 Operation Level Authorization
## V8.3 ਕਾਰਜ ਪੱਧਰ ਅਧਿਕਾਰੀਕਰਨ

The immediate application of authorization changes in the appropriate tier of an application's architecture is crucial to preventing unauthorized actions, especially in dynamic environments.

ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਆਰਕੀਟੈਕਚਰ ਦੇ ਢੁਕਵੇਂ ਪੱਧਰ ਵਿੱਚ ਅਧਿਕਾਰੀਕਰਨ ਤਬਦੀਲੀਆਂ ਨੂੰ ਤੁਰੰਤ ਲਾਗੂ ਕਰਨਾ ਅਣਅਧਿਕਾਰਤ ਕਾਰਵਾਈਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ, ਖ਼ਾਸ ਕਰਕੇ ਗਤੀਸ਼ੀਲ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ.

| # | Description | Level |
| :---: | :--- | :---: |
| **8.3.1** | Verify that the application enforces authorization rules at a trusted service layer and doesn't rely on controls that an untrusted consumer could manipulate, such as client-side JavaScript. | 1 |
| **8.3.2** | Verify that changes to values on which authorization decisions are made are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in self-contained tokens), there must be mitigating controls to alert when a consumer performs an action when they are no longer authorized to do so and revert the change. Note that this alternative would not mitigate information leakage. | 3 |
| **8.3.3** | Verify that access to an object is based on the originating subject's (e.g. consumer's) permissions, not on the permissions of any intermediary or service acting on their behalf. For example, if a consumer calls a web service using a self-contained token for authentication, and the service then requests data from a different service, the second service will use the consumer's token, rather than a machine-to-machine token from the first service, to make permission decisions. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **8.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਇੱਕ ਭਰੋਸੇਯੋਗ ਸੇਵਾ ਪਰਤ 'ਤੇ ਅਧਿਕਾਰੀਕਰਨ ਨਿਯਮ ਲਾਗੂ ਕਰਦੀ ਹੈ ਅਤੇ ਉਹਨਾਂ ਨਿਯੰਤਰਣਾਂ 'ਤੇ ਭਰੋਸਾ ਨਹੀਂ ਕਰਦੀ ਜਿਨ੍ਹਾਂ ਨੂੰ ਇੱਕ ਭਰੋਸੇਯੋਗ ਨਾ ਹੋਣ ਵਾਲਾ ਖਪਤਕਾਰ ਬਦਲ ਸਕਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਕਲਾਇੰਟ-ਸਾਈਡ JavaScript. | ੧ |
| **8.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਿਨ੍ਹਾਂ ਮੁੱਲਾਂ 'ਤੇ ਅਧਿਕਾਰੀਕਰਨ ਫ਼ੈਸਲੇ ਲਏ ਜਾਂਦੇ ਹਨ ਉਹਨਾਂ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਤੁਰੰਤ ਲਾਗੂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ. ਜਿੱਥੇ ਤਬਦੀਲੀਆਂ ਤੁਰੰਤ ਲਾਗੂ ਨਹੀਂ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ, (ਜਿਵੇਂ ਕਿ ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨਾਂ ਵਿੱਚ ਡਾਟੇ 'ਤੇ ਭਰੋਸਾ ਕਰਦੇ ਸਮੇਂ), ਉੱਥੇ ਘਟਾਉ ਨਿਯੰਤਰਣ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ ਜੋ ਸੁਚੇਤ ਕਰਨ ਕਿ ਜਦੋਂ ਕੋਈ ਖਪਤਕਾਰ ਅਜਿਹੀ ਕਾਰਵਾਈ ਕਰਦਾ ਹੈ ਜਿਸ ਲਈ ਉਹ ਹੁਣ ਅਧਿਕਾਰਿਤ ਨਹੀਂ ਹੈ ਅਤੇ ਤਬਦੀਲੀ ਨੂੰ ਉਲਟਾਉਣ. ਧਿਆਨ ਦਿਓ ਕਿ ਇਹ ਬਦਲ ਜਾਣਕਾਰੀ ਲੀਕੇਜ ਨੂੰ ਨਹੀਂ ਘਟਾਏਗਾ. | ੩ |
| **8.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਿਸੇ ਆਬਜੈਕਟ ਤੱਕ ਪਹੁੰਚ ਮੂਲ ਵਿਸ਼ੇ (ਜਿਵੇਂ ਕਿ ਖਪਤਕਾਰ) ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ 'ਤੇ ਆਧਾਰਿਤ ਹੈ, ਨਾ ਕਿ ਉਹਨਾਂ ਦੀ ਤਰਫ਼ੋਂ ਕੰਮ ਕਰਨ ਵਾਲੀ ਕਿਸੇ ਵਿਚੋਲੀ ਜਾਂ ਸੇਵਾ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ 'ਤੇ. ਉਦਾਹਰਨ ਲਈ, ਜੇਕਰ ਕੋਈ ਖਪਤਕਾਰ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ ਇੱਕ ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਿਸੇ ਵੈੱਬ ਸੇਵਾ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ, ਅਤੇ ਉਹ ਸੇਵਾ ਫਿਰ ਕਿਸੇ ਵੱਖਰੀ ਸੇਵਾ ਤੋਂ ਡਾਟਾ ਮੰਗਦੀ ਹੈ, ਤਾਂ ਦੂਜੀ ਸੇਵਾ ਇਜਾਜ਼ਤ ਫ਼ੈਸਲੇ ਲੈਣ ਲਈ ਪਹਿਲੀ ਸੇਵਾ ਦੇ ਮਸ਼ੀਨ-ਤੋਂ-ਮਸ਼ੀਨ ਟੋਕਨ ਦੀ ਬਜਾਏ ਖਪਤਕਾਰ ਦਾ ਟੋਕਨ ਵਰਤੇਗੀ. | ੩ |

## V8.4 Other Authorization Considerations
## V8.4 ਹੋਰ ਅਧਿਕਾਰੀਕਰਨ ਵਿਚਾਰ

Additional considerations for authorization, particularly for administrative interfaces and multi-tenant environments, help prevent unauthorized access.

ਅਧਿਕਾਰੀਕਰਨ ਲਈ ਵਾਧੂ ਵਿਚਾਰ, ਖ਼ਾਸ ਕਰਕੇ ਪ੍ਰਸ਼ਾਸਕੀ ਇੰਟਰਫ਼ੇਸਾਂ ਅਤੇ ਬਹੁ-ਕਿਰਾਏਦਾਰ (multi-tenant) ਵਾਤਾਵਰਣਾਂ ਲਈ, ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ ਨੂੰ ਰੋਕਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ.

| # | Description | Level |
| :---: | :--- | :---: |
| **8.4.1** | Verify that multi-tenant applications use cross-tenant controls to ensure consumer operations will never affect tenants with which they do not have permissions to interact. | 2 |
| **8.4.2** | Verify that access to administrative interfaces incorporates multiple layers of security, including continuous consumer identity verification, device security posture assessment, and contextual risk analysis, ensuring that network location or trusted endpoints are not the sole factors for authorization even though they may reduce the likelihood of unauthorized access. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **8.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬਹੁ-ਕਿਰਾਏਦਾਰ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅੰਤਰ-ਕਿਰਾਏਦਾਰ ਨਿਯੰਤਰਣਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਖਪਤਕਾਰ ਦੀਆਂ ਕਾਰਵਾਈਆਂ ਉਹਨਾਂ ਕਿਰਾਏਦਾਰਾਂ ਨੂੰ ਕਦੇ ਪ੍ਰਭਾਵਿਤ ਨਾ ਕਰਨ ਜਿਨ੍ਹਾਂ ਨਾਲ ਉਹਨਾਂ ਨੂੰ ਆਪਸੀ ਤਾਲਮੇਲ ਕਰਨ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ ਨਹੀਂ ਹਨ. | ੨ |
| **8.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਸ਼ਾਸਕੀ ਇੰਟਰਫ਼ੇਸਾਂ ਤੱਕ ਪਹੁੰਚ ਸੁਰੱਖਿਆ ਦੀਆਂ ਕਈ ਪਰਤਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਨਿਰੰਤਰ ਖਪਤਕਾਰ ਪਛਾਣ ਤਸਦੀਕ, ਡਿਵਾਈਸ ਸੁਰੱਖਿਆ ਮੁਦਰਾ ਮੁਲਾਂਕਣ, ਅਤੇ ਸੰਦਰਭੀ ਖ਼ਤਰਾ ਵਿਸ਼ਲੇਸ਼ਣ ਸ਼ਾਮਲ ਹਨ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੀਆਂ ਹੋਈਆਂ ਕਿ ਨੈੱਟਵਰਕ ਟਿਕਾਣਾ ਜਾਂ ਭਰੋਸੇਯੋਗ ਅੰਤ-ਬਿੰਦੂ ਅਧਿਕਾਰੀਕਰਨ ਲਈ ਇਕੋ-ਇਕ ਕਾਰਕ ਨਹੀਂ ਹਨ, ਭਾਵੇਂ ਉਹ ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ ਦੀ ਸੰਭਾਵਨਾ ਨੂੰ ਘਟਾ ਸਕਦੇ ਹਨ. | ੩ |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP Web Security Testing Guide: Authorization](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing)
* [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
