# V3 会话管理

## 控制目标

任何基于Web的应用程序或有状态的API的核心组成部分之一，是它控制和维护与之交互的用户或设备的状态的机制。会话管理将无状态协议变为有状态协议，这对于区分不同的用户或设备至关重要。

确保经过验证的应用程序满足以下高级会话管理需求:

* 会话对每个人都是唯一的，不能被猜测或共享。
* 会话在不再需要时失效，在不活动期间超时。

如前所述，这些要求已被调整为符合 NIST 800-63b 控制的一个子集，重点关注常见的威胁和经常被利用的认证弱点。 以前的验证要求已被淘汰、去重，或者在大多数情况下已调整为与强制性 [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) 要求的意图保持高度一致。

## 安全验证要求

## V3.1 基本会话管理安全

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.1.1** | 验证应用不会在URL参数中显示会话令牌。 | ✓ | ✓ | ✓ | 598 | |

## V3.2 会话绑定

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.2.1** | 验证应用程序在用户身份验证时，生成新的会话令牌。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | 验证会话令牌具有至少 64 位的熵。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | 验证应用程序仅使用安全方法在浏览器中存储会话令牌，例如适当的 cookie保护（参见第 3.4 节）或 HTML 5 会话存储。 | ✓ | ✓ | ✓ | 539 | 7.1 |
| **3.2.4** | 验证会话令牌是使用批准的加密算法生成的。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 331 | 7.1 |

会话管理必须使用 TLS 或其他安全传输通道。这在“通信安全”一章中有介绍。

## V3.3 会话终止

会话超时已经与NIST 800-63保持一致，它允许比传统安全标准所允许的更长的会话超时。组织应查看下表，如果应用的风险需要更长的超时，NIST值应是会话空闲超时的上限。

在此上下文中，L1 是 IAL1/AAL1，L2 是 IAL2/AAL3，L3 是 IAL3/AAL3。对于 IAL2/AAL2 和 IAL3/AAL3，空闲超时时间越短，表示注销或重新认证恢复会话的最短时间。

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Verify that logout and expiration invalidate the session token, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | 30 days | 12 hours or 30 minutes of inactivity, 2FA optional | 12 hours or 15 minutes of inactivity, with 2FA | 613 | 7.2 |
| **3.3.3** | Verify that the application gives the option to terminate all other active sessions after a successful password change (including change via password reset/recovery), and that this is effective across the application, federated login (if present), and any relying parties. | | ✓ | ✓ | 613 | |
| **3.3.4** | Verify that users are able to view and (having re-entered login credentials) log out of any or all currently active sessions and devices. | | ✓ | ✓ | 613 | 7.1 |

## V3.4 Cookie-based Session Management

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.4.1** | Verify that cookie-based session tokens have the 'Secure' attribute set. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | Verify that cookie-based session tokens have the 'HttpOnly' attribute set. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Verify that cookie-based session tokens utilize the 'SameSite' attribute to limit exposure to cross-site request forgery attacks. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.4** | Verify that cookie-based session tokens use the "__Host-" prefix so cookies are only sent to the host that initially set the cookie. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | Verify that if the application is published under a domain name with other applications that set or use session cookies that might disclose the session cookies, set the path attribute in cookie-based session tokens using the most precise path possible. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |

## V3.5 Token-based Session Management

Token-based session management includes JWT, OAuth, SAML, and API keys. Of these, API keys are known to be weak and should not be used in new code.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Verify the application allows users to revoke OAuth tokens that form trust relationships with linked applications. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Verify the application uses session tokens rather than static API secrets and keys, except with legacy implementations. | | ✓ | ✓ | 798 | |
| **3.5.3** | Verify that stateless session tokens use digital signatures, encryption, and other countermeasures to protect against tampering, enveloping, replay, null cipher, and key substitution attacks. | | ✓ | ✓ | 345 | |

## V3.6 Federated Re-authentication

This section relates to those writing Relying Party (RP) or Credential Service Provider (CSP) code. If relying on code implementing these features, ensure that these issues are handled correctly.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Verify that Relying Parties (RPs) specify the maximum authentication time to Credential Service Providers (CSPs) and that CSPs re-authenticate the user if they haven't used a session within that period. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Verify that Credential Service Providers (CSPs) inform Relying Parties (RPs) of the last authentication event, to allow RPs to determine if they need to re-authenticate the user. | | | ✓ | 613| 7.2.1 |

## V3.7 Defenses Against Session Management Exploits

There are a small number of session management attacks, some related to the user experience (UX) of sessions. Previously, based on ISO 27002 requirements, the ASVS has required blocking multiple simultaneous sessions. Blocking simultaneous sessions is no longer appropriate, not only as modern users have many devices or the app is an API without a browser session, but in most of these implementations, the last authenticator wins, which is often the attacker. This section provides leading guidance on deterring, delaying and detecting session management attacks using code.

### 说明 of the half-open Attack

In early 2018, several financial institutions were compromised using what the attackers called "half-open attacks". This term has stuck in the industry. The attackers struck multiple institutions with different proprietary code bases, and indeed it seems different code bases within the same institutions. The half-open attack is exploiting a design pattern flaw commonly found in many existing authentication, session management and access control systems.

Attackers start a half-open attack by attempting to lock, reset, or recover a credential. A popular session management design pattern re-uses user profile session objects/models between unauthenticated, half-authenticated (password resets, forgot username), and fully authenticated code. This design pattern populates a valid session object or token containing the victim's profile, including password hashes and roles. If access control checks in controllers or routers does not correctly verify that the user is fully logged in, the attacker will be able to act as the user. Attacks could include changing the user's password to a known value, update the email address to perform a valid password reset, disable multi-factor authentication or enroll a new MFA device, reveal or change API keys, and so on.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Verify the application ensures a full, valid login session or requires re-authentication or secondary verification before allowing any sensitive transactions or account modifications. | ✓ | ✓ | ✓ | 306 | |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Directives)
