<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x16-V7-Session-Management.md -->
<!-- Translator: GeeksikhSecurity -->

# V7 Session Management
# V7 ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Session management mechanisms allow applications to correlate user and device interactions over time, even when using stateless communication protocols (such as HTTP). Modern applications may use multiple session tokens with distinct characteristics and purposes. A secure session management system is one that prevents attackers from obtaining, utilizing, or otherwise abusing a victim's session. Applications maintaining sessions must ensure that the following high-level session management requirements are met:

ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਪ੍ਰਣਾਲੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸਮੇਂ ਦੇ ਨਾਲ ਉਪਭੋਗਤਾ ਅਤੇ ਡਿਵਾਈਸ ਦੀਆਂ ਅੰਤਰਕਿਰਿਆਵਾਂ ਨੂੰ ਆਪਸ ਵਿੱਚ ਜੋੜਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀਆਂ ਹਨ, ਉਦੋਂ ਵੀ ਜਦੋਂ ਸਟੇਟਲੈੱਸ (stateless) ਸੰਚਾਰ ਪ੍ਰੋਟੋਕਾਲ (ਜਿਵੇਂ ਕਿ HTTP) ਵਰਤੇ ਜਾ ਰਹੇ ਹੋਣ। ਆਧੁਨਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵੱਖਰੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਉਦੇਸ਼ਾਂ ਵਾਲੇ ਕਈ ਸੈਸ਼ਨ ਟੋਕਨ ਵਰਤ ਸਕਦੀਆਂ ਹਨ। ਇੱਕ ਸੁਰੱਖਿਅਤ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਸਿਸਟਮ ਉਹ ਹੈ ਜੋ ਹਮਲਾਵਰਾਂ ਨੂੰ ਪੀੜਤ ਦੇ ਸੈਸ਼ਨ ਨੂੰ ਹਾਸਲ ਕਰਨ, ਵਰਤਣ, ਜਾਂ ਕਿਸੇ ਹੋਰ ਤਰੀਕੇ ਨਾਲ ਇਸ ਦੀ ਦੁਰਵਰਤੋਂ ਕਰਨ ਤੋਂ ਰੋਕਦਾ ਹੈ। ਸੈਸ਼ਨ ਕਾਇਮ ਰੱਖਣ ਵਾਲੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਯਕੀਨੀ ਬਣਾਉਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਹੇਠ ਲਿਖੀਆਂ ਉੱਚ-ਪੱਧਰੀ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਲੋੜਾਂ ਪੂਰੀਆਂ ਹੋਣ:

* Sessions are unique to each individual and cannot be guessed or shared.
* Sessions are invalidated when no longer required and are timed out during periods of inactivity.

* ਸੈਸ਼ਨ ਹਰੇਕ ਵਿਅਕਤੀ ਲਈ ਵਿਲੱਖਣ ਹੁੰਦੇ ਹਨ ਅਤੇ ਉਹਨਾਂ ਦਾ ਅੰਦਾਜ਼ਾ ਨਹੀਂ ਲਗਾਇਆ ਜਾ ਸਕਦਾ ਜਾਂ ਉਹਨਾਂ ਨੂੰ ਸਾਂਝਾ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ।
* ਜਦੋਂ ਸੈਸ਼ਨਾਂ ਦੀ ਹੋਰ ਲੋੜ ਨਾ ਰਹੇ ਤਾਂ ਉਹਨਾਂ ਨੂੰ ਅਵੈਧ ਕਰ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਗ਼ੈਰ-ਸਰਗਰਮੀ (inactivity) ਦੇ ਸਮੇਂ ਦੌਰਾਨ ਉਹਨਾਂ ਦੀ ਸਮਾਂ-ਸੀਮਾ ਪੁੱਗ ਜਾਂਦੀ ਹੈ।

Many of the requirements in this chapter relate to selected [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) controls, focusing on common threats and commonly exploited authentication weaknesses.

ਇਸ ਅਧਿਆਇ ਦੀਆਂ ਬਹੁਤ ਸਾਰੀਆਂ ਲੋੜਾਂ ਚੁਣੇ ਹੋਏ [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) ਨਿਯੰਤਰਣਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ, ਜੋ ਆਮ ਖ਼ਤਰਿਆਂ ਅਤੇ ਉਹਨਾਂ ਪ੍ਰਮਾਣੀਕਰਨ ਕਮਜ਼ੋਰੀਆਂ 'ਤੇ ਕੇਂਦਰਿਤ ਹਨ ਜਿਨ੍ਹਾਂ ਦਾ ਆਮ ਤੌਰ 'ਤੇ ਸ਼ੋਸ਼ਣ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

Note that requirements for specific implementation details of certain session management mechanisms can be found elsewhere:

ਧਿਆਨ ਦਿਓ ਕਿ ਕੁਝ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਪ੍ਰਣਾਲੀਆਂ ਦੇ ਖ਼ਾਸ ਲਾਗੂਕਰਨ ਵੇਰਵਿਆਂ ਲਈ ਲੋੜਾਂ ਹੋਰ ਥਾਂ ਮਿਲ ਸਕਦੀਆਂ ਹਨ:

* HTTP Cookies are a common mechanism for securing session tokens. Specific security requirements for cookies can be found in the "Web Frontend Security" chapter.
* Self-contained tokens are frequently used as a way of maintaining sessions. Specific security requirements can be found in the "Self-contained Tokens" chapter.

* HTTP ਕੁਕੀਆਂ ਸੈਸ਼ਨ ਟੋਕਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਇੱਕ ਆਮ ਪ੍ਰਣਾਲੀ ਹਨ। ਕੁਕੀਆਂ ਲਈ ਖ਼ਾਸ ਸੁਰੱਖਿਆ ਲੋੜਾਂ "ਵੈੱਬ ਫਰੰਟਐਂਡ ਸੁਰੱਖਿਆ" (Web Frontend Security) ਅਧਿਆਇ ਵਿੱਚ ਮਿਲ ਸਕਦੀਆਂ ਹਨ।
* ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ (self-contained tokens) ਅਕਸਰ ਸੈਸ਼ਨ ਕਾਇਮ ਰੱਖਣ ਦੇ ਇੱਕ ਤਰੀਕੇ ਵਜੋਂ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਖ਼ਾਸ ਸੁਰੱਖਿਆ ਲੋੜਾਂ "ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ" (Self-contained Tokens) ਅਧਿਆਇ ਵਿੱਚ ਮਿਲ ਸਕਦੀਆਂ ਹਨ।

## V7.1 Session Management Documentation
## V7.1 ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

There is no single pattern that suits all applications. Therefore, it is not feasible to define universal boundaries and limits that suit all cases. A risk analysis with documented security decisions related to session handling must be conducted as a prerequisite to implementation and testing. This ensures that the session management system is tailored to the specific requirements of the application.

ਕੋਈ ਇੱਕ ਅਜਿਹਾ ਪੈਟਰਨ ਨਹੀਂ ਹੈ ਜੋ ਸਾਰੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਢੁਕਵਾਂ ਹੋਵੇ। ਇਸ ਲਈ, ਅਜਿਹੀਆਂ ਸਰਵ-ਵਿਆਪਕ ਹੱਦਾਂ ਅਤੇ ਸੀਮਾਵਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਸੰਭਵ ਨਹੀਂ ਹੈ ਜੋ ਸਾਰੇ ਮਾਮਲਿਆਂ ਲਈ ਢੁਕਵੀਆਂ ਹੋਣ। ਲਾਗੂਕਰਨ ਅਤੇ ਟੈਸਟਿੰਗ ਦੀ ਪੂਰਵ-ਸ਼ਰਤ ਵਜੋਂ, ਸੈਸ਼ਨ ਸੰਭਾਲ ਨਾਲ ਸੰਬੰਧਿਤ ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਸਮੇਤ ਇੱਕ ਜੋਖਮ ਵਿਸ਼ਲੇਸ਼ਣ (risk analysis) ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਸਿਸਟਮ ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਖ਼ਾਸ ਲੋੜਾਂ ਦੇ ਅਨੁਸਾਰ ਢਾਲਿਆ ਗਿਆ ਹੈ।

Regardless of whether a stateful or "stateless" session mechanism is chosen, the analysis must be complete and documented to demonstrate that the selected solution is capable of satisfying all relevant security requirements. Interaction with any Single Sign-on (SSO) mechanisms in use should also be considered.

ਇਸ ਗੱਲ ਦੀ ਪਰਵਾਹ ਕੀਤੇ ਬਿਨਾਂ ਕਿ ਸਟੇਟਫੁੱਲ (stateful) ਜਾਂ "ਸਟੇਟਲੈੱਸ" ਸੈਸ਼ਨ ਪ੍ਰਣਾਲੀ ਚੁਣੀ ਗਈ ਹੈ, ਵਿਸ਼ਲੇਸ਼ਣ ਦਾ ਪੂਰਾ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀ ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ ਤਾਂ ਜੋ ਇਹ ਦਰਸਾਇਆ ਜਾ ਸਕੇ ਕਿ ਚੁਣਿਆ ਹੋਇਆ ਹੱਲ ਸਾਰੀਆਂ ਸੰਬੰਧਿਤ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਦੇ ਸਮਰੱਥ ਹੈ। ਵਰਤੋਂ ਵਿੱਚ ਆ ਰਹੀਆਂ ਕਿਸੇ ਵੀ ਸਿੰਗਲ ਸਾਈਨ-ਆਨ (Single Sign-on, SSO) ਪ੍ਰਣਾਲੀਆਂ ਨਾਲ ਅੰਤਰਕਿਰਿਆ 'ਤੇ ਵੀ ਵਿਚਾਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **7.1.1** | Verify that the user's session inactivity timeout and absolute maximum session lifetime are documented, are appropriate in combination with other controls, and that the documentation includes justification for any deviations from NIST SP 800-63B re-authentication requirements. | 2 |
| **7.1.2** | Verify that the documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviors and actions to be taken when the maximum number of active sessions is reached. | 2 |
| **7.1.3** | Verify that all systems that create and manage user sessions as part of a federated identity management ecosystem (such as SSO systems) are documented along with controls to coordinate session lifetimes, termination, and any other conditions that require re-authentication. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **7.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ ਦੀ ਸੈਸ਼ਨ ਗ਼ੈਰ-ਸਰਗਰਮੀ ਸਮਾਂ-ਸੀਮਾ (inactivity timeout) ਅਤੇ ਪੂਰਨ ਵੱਧ ਤੋਂ ਵੱਧ ਸੈਸ਼ਨ ਜੀਵਨਕਾਲ (absolute maximum session lifetime) ਦਸਤਾਵੇਜ਼ੀ ਹਨ, ਹੋਰ ਨਿਯੰਤਰਣਾਂ ਦੇ ਨਾਲ ਮਿਲ ਕੇ ਢੁਕਵੇਂ ਹਨ, ਅਤੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ NIST SP 800-63B ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ (re-authentication) ਲੋੜਾਂ ਤੋਂ ਕਿਸੇ ਵੀ ਵਿਚਲਨ ਲਈ ਤਰਕਸੰਗਤ ਕਾਰਨ ਸ਼ਾਮਲ ਹੈ। | 2 |
| **7.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਇੱਕ ਖਾਤੇ ਲਈ ਕਿੰਨੇ ਸਮਕਾਲੀ (ਸਮਾਨਾਂਤਰ) ਸੈਸ਼ਨਾਂ ਦੀ ਇਜਾਜ਼ਤ ਹੈ, ਅਤੇ ਨਾਲ ਹੀ ਜਦੋਂ ਸਰਗਰਮ ਸੈਸ਼ਨਾਂ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਗਿਣਤੀ ਤੱਕ ਪਹੁੰਚ ਜਾਂਦੀ ਹੈ ਤਾਂ ਇਰਾਦਾ ਕੀਤੇ ਵਿਹਾਰ ਅਤੇ ਚੁੱਕੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਕਾਰਵਾਈਆਂ ਕੀ ਹਨ। | 2 |
| **7.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਹ ਸਾਰੇ ਸਿਸਟਮ ਜੋ ਸੰਘੀ (federated) ਪਛਾਣ ਪ੍ਰਬੰਧਨ ਈਕੋਸਿਸਟਮ ਦੇ ਹਿੱਸੇ ਵਜੋਂ ਉਪਭੋਗਤਾ ਸੈਸ਼ਨ ਬਣਾਉਂਦੇ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰਦੇ ਹਨ (ਜਿਵੇਂ ਕਿ SSO ਸਿਸਟਮ), ਸੈਸ਼ਨ ਜੀਵਨਕਾਲਾਂ, ਸਮਾਪਤੀ, ਅਤੇ ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਲੋੜ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਹੋਰ ਸ਼ਰਤਾਂ ਦਾ ਤਾਲਮੇਲ ਕਰਨ ਵਾਲੇ ਨਿਯੰਤਰਣਾਂ ਸਮੇਤ ਦਸਤਾਵੇਜ਼ੀ ਹਨ। | 2 |

## V7.2 Fundamental Session Management Security
## V7.2 ਬੁਨਿਆਦੀ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਸੁਰੱਖਿਆ

This section satisfies the essential requirements of secure sessions by verifying that session tokens are securely generated and validated.

ਇਹ ਭਾਗ ਇਹ ਤਸਦੀਕ ਕਰਕੇ ਸੁਰੱਖਿਅਤ ਸੈਸ਼ਨਾਂ ਦੀਆਂ ਜ਼ਰੂਰੀ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੈ ਕਿ ਸੈਸ਼ਨ ਟੋਕਨ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਤਿਆਰ ਅਤੇ ਪ੍ਰਮਾਣਿਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **7.2.1** | Verify that the application performs all session token verification using a trusted, backend service. | 1 |
| **7.2.2** | Verify that the application uses either self-contained or reference tokens that are dynamically generated for session management, i.e. not using static API secrets and keys. | 1 |
| **7.2.3** | Verify that if reference tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG) and possess at least 128 bits of entropy. | 1 |
| **7.2.4** | Verify that the application generates a new session token on user authentication, including re-authentication, and terminates the current session token. | 1 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **7.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸਾਰੀ ਸੈਸ਼ਨ ਟੋਕਨ ਤਸਦੀਕ ਇੱਕ ਭਰੋਸੇਯੋਗ, ਬੈਕਐਂਡ ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਰਦੀ ਹੈ। | 1 |
| **7.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਲਈ ਜਾਂ ਤਾਂ ਸਵੈ-ਨਿਰਭਰ ਜਾਂ ਹਵਾਲਾ ਟੋਕਨ (reference tokens) ਵਰਤਦੀ ਹੈ ਜੋ ਗਤੀਸ਼ੀਲ ਰੂਪ ਵਿੱਚ ਤਿਆਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਭਾਵ ਸਥਿਰ API ਸੀਕ੍ਰੇਟਾਂ ਅਤੇ ਕੁੰਜੀਆਂ ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰਦੀ। | 1 |
| **7.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੇਕਰ ਉਪਭੋਗਤਾ ਸੈਸ਼ਨਾਂ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਹਵਾਲਾ ਟੋਕਨ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਤਾਂ ਉਹ ਵਿਲੱਖਣ ਹਨ ਅਤੇ ਇੱਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਤੌਰ 'ਤੇ ਸੁਰੱਖਿਅਤ ਸੂਡੋ-ਰੈਂਡਮ ਨੰਬਰ ਜਨਰੇਟਰ (CSPRNG) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਿਆਰ ਕੀਤੇ ਗਏ ਹਨ, ਅਤੇ ਉਹਨਾਂ ਵਿੱਚ ਘੱਟੋ-ਘੱਟ 128 ਬਿੱਟ ਐਂਟਰੋਪੀ (entropy) ਹੈ। | 1 |
| **7.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਉਪਭੋਗਤਾ ਪ੍ਰਮਾਣੀਕਰਨ 'ਤੇ, ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ ਸਮੇਤ, ਇੱਕ ਨਵਾਂ ਸੈਸ਼ਨ ਟੋਕਨ ਤਿਆਰ ਕਰਦੀ ਹੈ ਅਤੇ ਮੌਜੂਦਾ ਸੈਸ਼ਨ ਟੋਕਨ ਨੂੰ ਸਮਾਪਤ ਕਰਦੀ ਹੈ। | 1 |

## V7.3 Session Timeout
## V7.3 ਸੈਸ਼ਨ ਸਮਾਂ-ਸੀਮਾ

Session timeout mechanisms serve to minimize the window of opportunity for session hijacking and other forms of session abuse. Timeouts must satisfy documented security decisions.

ਸੈਸ਼ਨ ਸਮਾਂ-ਸੀਮਾ ਪ੍ਰਣਾਲੀਆਂ ਸੈਸ਼ਨ ਹਾਈਜੈਕਿੰਗ (session hijacking) ਅਤੇ ਸੈਸ਼ਨ ਦੁਰਵਰਤੋਂ ਦੇ ਹੋਰ ਰੂਪਾਂ ਲਈ ਮੌਕੇ ਦੀ ਮਿਆਦ ਨੂੰ ਘੱਟ ਤੋਂ ਘੱਟ ਕਰਨ ਦਾ ਕੰਮ ਕਰਦੀਆਂ ਹਨ। ਸਮਾਂ-ਸੀਮਾਵਾਂ ਦਾ ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਨੂੰ ਪੂਰਾ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **7.3.1** | Verify that there is an inactivity timeout such that re-authentication is enforced according to risk analysis and documented security decisions. | 2 |
| **7.3.2** | Verify that there is an absolute maximum session lifetime such that re-authentication is enforced according to risk analysis and documented security decisions. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **7.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਗ਼ੈਰ-ਸਰਗਰਮੀ ਸਮਾਂ-ਸੀਮਾ ਮੌਜੂਦ ਹੈ ਜਿਸ ਨਾਲ ਜੋਖਮ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਦੇ ਅਨੁਸਾਰ ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ ਲਾਗੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। | 2 |
| **7.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਪੂਰਨ ਵੱਧ ਤੋਂ ਵੱਧ ਸੈਸ਼ਨ ਜੀਵਨਕਾਲ ਮੌਜੂਦ ਹੈ ਜਿਸ ਨਾਲ ਜੋਖਮ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਦੇ ਅਨੁਸਾਰ ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ ਲਾਗੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। | 2 |

## V7.4 Session Termination
## V7.4 ਸੈਸ਼ਨ ਸਮਾਪਤੀ

Session termination may be handled either by the application itself or by the SSO provider if the SSO provider is handling session management instead of the application. It may be necessary to decide whether the SSO provider is in scope when considering the requirements in this section as some may be controlled by the provider.

ਸੈਸ਼ਨ ਸਮਾਪਤੀ ਜਾਂ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਖ਼ੁਦ ਸੰਭਾਲੀ ਜਾ ਸਕਦੀ ਹੈ ਜਾਂ SSO ਪ੍ਰਦਾਤਾ ਦੁਆਰਾ, ਜੇਕਰ SSO ਪ੍ਰਦਾਤਾ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਬਜਾਏ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਸੰਭਾਲ ਰਿਹਾ ਹੈ। ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ 'ਤੇ ਵਿਚਾਰ ਕਰਦੇ ਸਮੇਂ ਇਹ ਫ਼ੈਸਲਾ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੋ ਸਕਦਾ ਹੈ ਕਿ SSO ਪ੍ਰਦਾਤਾ ਘੇਰੇ ਵਿੱਚ ਹੈ ਜਾਂ ਨਹੀਂ, ਕਿਉਂਕਿ ਕੁਝ ਲੋੜਾਂ ਪ੍ਰਦਾਤਾ ਦੁਆਰਾ ਨਿਯੰਤਰਿਤ ਹੋ ਸਕਦੀਆਂ ਹਨ।

Session termination should result in requiring re-authentication and be effective across the application, federated login (if present), and any relying parties.

ਸੈਸ਼ਨ ਸਮਾਪਤੀ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਲੋੜ ਪੈਣੀ ਚਾਹੀਦੀ ਹੈ ਅਤੇ ਇਹ ਐਪਲੀਕੇਸ਼ਨ, ਸੰਘੀ ਲੌਗਇਨ (ਜੇ ਮੌਜੂਦ ਹੋਵੇ), ਅਤੇ ਕਿਸੇ ਵੀ ਨਿਰਭਰ ਧਿਰਾਂ (relying parties) ਵਿੱਚ ਪ੍ਰਭਾਵੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

For stateful session mechanisms, termination typically involves invalidating the session on the backend. In the case of self-contained tokens, additional measures are required to revoke or block these tokens, as they may otherwise remain valid until expiration.

ਸਟੇਟਫੁੱਲ ਸੈਸ਼ਨ ਪ੍ਰਣਾਲੀਆਂ ਲਈ, ਸਮਾਪਤੀ ਵਿੱਚ ਆਮ ਤੌਰ 'ਤੇ ਬੈਕਐਂਡ 'ਤੇ ਸੈਸ਼ਨ ਨੂੰ ਅਵੈਧ ਕਰਨਾ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ। ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨਾਂ ਦੇ ਮਾਮਲੇ ਵਿੱਚ, ਇਹਨਾਂ ਟੋਕਨਾਂ ਨੂੰ ਰੱਦ ਕਰਨ ਜਾਂ ਰੋਕਣ ਲਈ ਵਾਧੂ ਉਪਾਵਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਕਿਉਂਕਿ ਨਹੀਂ ਤਾਂ ਉਹ ਮਿਆਦ ਪੁੱਗਣ ਤੱਕ ਜਾਇਜ਼ ਰਹਿ ਸਕਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **7.4.1** | Verify that when session termination is triggered (such as logout or expiration), the application disallows any further use of the session. For reference tokens or stateful sessions, this means invalidating the session data at the application backend. Applications using self-contained tokens will need a solution such as maintaining a list of terminated tokens, disallowing tokens produced before a per-user date and time or rotating a per-user signing key. | 1 |
| **7.4.2** | Verify that the application terminates all active sessions when a user account is disabled or deleted (such as an employee leaving the company). | 1 |
| **7.4.3** | Verify that the application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update). | 2 |
| **7.4.4** | Verify that all pages that require authentication have easy and visible access to logout functionality. | 2 |
| **7.4.5** | Verify that application administrators are able to terminate active sessions for an individual user or for all users. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **7.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਸੈਸ਼ਨ ਸਮਾਪਤੀ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ (ਜਿਵੇਂ ਕਿ ਲੌਗਆਊਟ ਜਾਂ ਮਿਆਦ ਪੁੱਗਣਾ), ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਸੈਸ਼ਨ ਦੀ ਕਿਸੇ ਵੀ ਹੋਰ ਵਰਤੋਂ ਦੀ ਇਜਾਜ਼ਤ ਨਹੀਂ ਦਿੰਦੀ। ਹਵਾਲਾ ਟੋਕਨਾਂ ਜਾਂ ਸਟੇਟਫੁੱਲ ਸੈਸ਼ਨਾਂ ਲਈ, ਇਸ ਦਾ ਮਤਲਬ ਹੈ ਐਪਲੀਕੇਸ਼ਨ ਬੈਕਐਂਡ 'ਤੇ ਸੈਸ਼ਨ ਡਾਟਾ ਨੂੰ ਅਵੈਧ ਕਰਨਾ। ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ ਵਰਤਣ ਵਾਲੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਇੱਕ ਅਜਿਹੇ ਹੱਲ ਦੀ ਲੋੜ ਪਵੇਗੀ ਜਿਵੇਂ ਕਿ ਸਮਾਪਤ ਕੀਤੇ ਟੋਕਨਾਂ ਦੀ ਸੂਚੀ ਕਾਇਮ ਰੱਖਣਾ, ਪ੍ਰਤੀ-ਉਪਭੋਗਤਾ ਮਿਤੀ ਅਤੇ ਸਮੇਂ ਤੋਂ ਪਹਿਲਾਂ ਤਿਆਰ ਕੀਤੇ ਟੋਕਨਾਂ ਦੀ ਇਜਾਜ਼ਤ ਨਾ ਦੇਣਾ, ਜਾਂ ਪ੍ਰਤੀ-ਉਪਭੋਗਤਾ ਦਸਤਖ਼ਤ ਕੁੰਜੀ (signing key) ਨੂੰ ਰੋਟੇਟ ਕਰਨਾ। | 1 |
| **7.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਕੋਈ ਉਪਭੋਗਤਾ ਖਾਤਾ ਅਸਮਰੱਥ ਜਾਂ ਮਿਟਾਇਆ ਜਾਂਦਾ ਹੈ (ਜਿਵੇਂ ਕਿ ਕਿਸੇ ਕਰਮਚਾਰੀ ਦਾ ਕੰਪਨੀ ਛੱਡਣਾ), ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਸਾਰੇ ਸਰਗਰਮ ਸੈਸ਼ਨਾਂ ਨੂੰ ਸਮਾਪਤ ਕਰਦੀ ਹੈ। | 1 |
| **7.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕਿਸੇ ਵੀ ਪ੍ਰਮਾਣੀਕਰਨ ਕਾਰਕ ਦੀ ਸਫਲ ਤਬਦੀਲੀ ਜਾਂ ਹਟਾਉਣ ਤੋਂ ਬਾਅਦ (ਰੀਸੈੱਟ ਜਾਂ ਮੁੜ-ਪ੍ਰਾਪਤੀ ਰਾਹੀਂ ਪਾਸਵਰਡ ਤਬਦੀਲੀ ਅਤੇ, ਜੇ ਮੌਜੂਦ ਹੋਵੇ, MFA ਸੈਟਿੰਗਾਂ ਦੇ ਅੱਪਡੇਟ ਸਮੇਤ) ਬਾਕੀ ਸਾਰੇ ਸਰਗਰਮ ਸੈਸ਼ਨਾਂ ਨੂੰ ਸਮਾਪਤ ਕਰਨ ਦਾ ਵਿਕਲਪ ਦਿੰਦੀ ਹੈ। | 2 |
| **7.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਲੋੜ ਵਾਲੇ ਸਾਰੇ ਪੰਨਿਆਂ 'ਤੇ ਲੌਗਆਊਟ ਕਾਰਜਸ਼ੀਲਤਾ ਤੱਕ ਆਸਾਨ ਅਤੇ ਦਿਖਾਈ ਦੇਣ ਵਾਲੀ ਪਹੁੰਚ ਹੈ। | 2 |
| **7.4.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਪ੍ਰਸ਼ਾਸਕ ਕਿਸੇ ਇੱਕ ਉਪਭੋਗਤਾ ਲਈ ਜਾਂ ਸਾਰੇ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਸਰਗਰਮ ਸੈਸ਼ਨਾਂ ਨੂੰ ਸਮਾਪਤ ਕਰਨ ਦੇ ਯੋਗ ਹਨ। | 2 |

## V7.5 Defenses Against Session Abuse
## V7.5 ਸੈਸ਼ਨ ਦੁਰਵਰਤੋਂ ਵਿਰੁੱਧ ਬਚਾਅ

This section provides requirements to mitigate the risk posed by active sessions that are either hijacked or abused through vectors that rely on the existence and capabilities of active user sessions. For example, using malicious content execution to force an authenticated victim browser to perform an action using the victim's session.

ਇਹ ਭਾਗ ਉਹਨਾਂ ਸਰਗਰਮ ਸੈਸ਼ਨਾਂ ਦੁਆਰਾ ਪੈਦਾ ਕੀਤੇ ਜੋਖਮ ਨੂੰ ਘਟਾਉਣ ਲਈ ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਜਾਂ ਤਾਂ ਹਾਈਜੈਕ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਜਾਂ ਅਜਿਹੇ ਵੈਕਟਰਾਂ ਰਾਹੀਂ ਦੁਰਵਰਤੋਂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਜੋ ਸਰਗਰਮ ਉਪਭੋਗਤਾ ਸੈਸ਼ਨਾਂ ਦੀ ਮੌਜੂਦਗੀ ਅਤੇ ਸਮਰੱਥਾਵਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ। ਉਦਾਹਰਨ ਲਈ, ਖ਼ਤਰਨਾਕ ਸਮੱਗਰੀ ਦੇ ਅਮਲ (malicious content execution) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਪ੍ਰਮਾਣੀਕਰਨ ਕੀਤੇ ਹੋਏ ਪੀੜਤ ਬ੍ਰਾਊਜ਼ਰ ਨੂੰ ਪੀੜਤ ਦੇ ਸੈਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੋਈ ਕਾਰਵਾਈ ਕਰਨ ਲਈ ਮਜਬੂਰ ਕਰਨਾ।

Note that the level-specific guidance in the "Authentication" chapter should be taken into account when considering requirements in this section.

ਧਿਆਨ ਦਿਓ ਕਿ ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ 'ਤੇ ਵਿਚਾਰ ਕਰਦੇ ਸਮੇਂ "ਪ੍ਰਮਾਣੀਕਰਨ" (Authentication) ਅਧਿਆਇ ਵਿੱਚ ਦਿੱਤੇ ਪੱਧਰ-ਵਿਸ਼ੇਸ਼ ਮਾਰਗਦਰਸ਼ਨ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **7.5.1** | Verify that the application requires full re-authentication before allowing modifications to sensitive account attributes which may affect authentication such as email address, phone number, MFA configuration, or other information used in account recovery. | 2 |
| **7.5.2** | Verify that users are able to view and (having authenticated again with at least one factor) terminate any or all currently active sessions. | 2 |
| **7.5.3** | Verify that the application requires further authentication with at least one factor or secondary verification before performing highly sensitive transactions or operations. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **7.5.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਉਹਨਾਂ ਸੰਵੇਦਨਸ਼ੀਲ ਖਾਤਾ ਗੁਣਾਂ ਵਿੱਚ ਸੋਧਾਂ ਦੀ ਇਜਾਜ਼ਤ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ ਪੂਰੇ ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਮੰਗ ਕਰਦੀ ਹੈ ਜੋ ਪ੍ਰਮਾਣੀਕਰਨ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਈਮੇਲ ਪਤਾ, ਫ਼ੋਨ ਨੰਬਰ, MFA ਸੰਰਚਨਾ, ਜਾਂ ਖਾਤਾ ਮੁੜ-ਪ੍ਰਾਪਤੀ ਵਿੱਚ ਵਰਤੀ ਜਾਂਦੀ ਹੋਰ ਜਾਣਕਾਰੀ। | 2 |
| **7.5.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ ਮੌਜੂਦਾ ਸਮੇਂ ਸਰਗਰਮ ਕਿਸੇ ਵੀ ਜਾਂ ਸਾਰੇ ਸੈਸ਼ਨਾਂ ਨੂੰ ਵੇਖਣ ਅਤੇ (ਘੱਟੋ-ਘੱਟ ਇੱਕ ਕਾਰਕ ਨਾਲ ਦੁਬਾਰਾ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਨ ਤੋਂ ਬਾਅਦ) ਸਮਾਪਤ ਕਰਨ ਦੇ ਯੋਗ ਹਨ। | 2 |
| **7.5.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਬਹੁਤ ਸੰਵੇਦਨਸ਼ੀਲ ਲੈਣ-ਦੇਣ ਜਾਂ ਕਾਰਜ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਘੱਟੋ-ਘੱਟ ਇੱਕ ਕਾਰਕ ਨਾਲ ਹੋਰ ਪ੍ਰਮਾਣੀਕਰਨ ਜਾਂ ਸੈਕੰਡਰੀ ਤਸਦੀਕ ਦੀ ਮੰਗ ਕਰਦੀ ਹੈ। | 3 |

## V7.6 Federated Re-authentication
## V7.6 ਸੰਘੀ ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ

This section relates to those writing Relying Party (RP) or Identity Provider (IdP) code. These requirements are derived from the [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) for Federation & Assertions.

ਇਹ ਭਾਗ ਉਹਨਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਹੈ ਜੋ ਨਿਰਭਰ ਧਿਰ (Relying Party, RP) ਜਾਂ ਪਛਾਣ ਪ੍ਰਦਾਤਾ (Identity Provider, IdP) ਕੋਡ ਲਿਖਦੇ ਹਨ। ਇਹ ਲੋੜਾਂ Federation & Assertions ਲਈ [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) ਤੋਂ ਲਈਆਂ ਗਈਆਂ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **7.6.1** | Verify that session lifetime and termination between Relying Parties (RPs) and Identity Providers (IdPs) behave as documented, requiring re-authentication as necessary such as when the maximum time between IdP authentication events is reached. | 2 |
| **7.6.2** | Verify that creation of a session requires either the user's consent or an explicit action, preventing the creation of new application sessions without user interaction. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **7.6.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਨਿਰਭਰ ਧਿਰਾਂ (RPs) ਅਤੇ ਪਛਾਣ ਪ੍ਰਦਾਤਾਵਾਂ (IdPs) ਦੇ ਵਿਚਕਾਰ ਸੈਸ਼ਨ ਜੀਵਨਕਾਲ ਅਤੇ ਸਮਾਪਤੀ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦੇ ਅਨੁਸਾਰ ਵਿਹਾਰ ਕਰਦੇ ਹਨ, ਅਤੇ ਲੋੜ ਅਨੁਸਾਰ ਮੁੜ-ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਮੰਗ ਕਰਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਜਦੋਂ IdP ਪ੍ਰਮਾਣੀਕਰਨ ਘਟਨਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਵੱਧ ਤੋਂ ਵੱਧ ਸਮਾਂ ਪੂਰਾ ਹੋ ਜਾਂਦਾ ਹੈ। | 2 |
| **7.6.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੈਸ਼ਨ ਬਣਾਉਣ ਲਈ ਜਾਂ ਤਾਂ ਉਪਭੋਗਤਾ ਦੀ ਸਹਿਮਤੀ ਜਾਂ ਇੱਕ ਸਪੱਸ਼ਟ ਕਾਰਵਾਈ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਉਪਭੋਗਤਾ ਦੀ ਅੰਤਰਕਿਰਿਆ ਤੋਂ ਬਿਨਾਂ ਨਵੇਂ ਐਪਲੀਕੇਸ਼ਨ ਸੈਸ਼ਨ ਬਣਾਏ ਜਾਣ ਨੂੰ ਰੋਕਿਆ ਜਾਂਦਾ ਹੈ। | 2 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP Web Security Testing Guide: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/06-Session_Management_Testing)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
