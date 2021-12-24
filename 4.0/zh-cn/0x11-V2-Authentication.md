# V2 认证

## 控制目标

认证是建立或确认某人（或某物）的真实性，并且个人或设备的声明是正确的，可防止假冒，并防止恢复或拦截密码。

当ASVS首次发布时，用户名+密码是最常见的认证形式（除高安全系统以外）。 多因素身份验证 (MFA) 在安全界被普遍接受，但在其他地方很少需要。 随着密码泄露次数的增加，认为用户名在某种程度上是保密的，而密码则是未知的这种想法使得许多安全控制无法成立。 例如，NIST 800-63 将用户名和基于知识的身份验证 (KBA) 视为公共信息，将 SMS 和电子邮件通知视为[“受限”的认证类型](https://pages.nist.gov/800-63-FAQ/#q-b1) , 而密码是预先泄露的。 这一现实使基于知识的认证器、短信和电子邮件恢复、密码历史、复杂性和轮换控制变得毫无用处。 这些控制措施不总那么有用，经常迫使用户每隔几个月就想出一些弱的密码，但是随着50多亿用户名和密码泄露事件的公布，现在是时候继续前进了。

在ASVS的所有章节中，认证和会话管理章节的变化最大。采用有效的、以证据为基础的领先实践，对许多人来说将是挑战，这完全没问题。 现在我们必须开始向未来的后密码时代过渡。

## NIST 800-63 - 现代的、基于证据的认证标准

[NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) 是一种现代的、基于证据的标准，代表了可用的最佳建议，无论其适用性如何。该标准对世界各地的所有组织都有帮助，但与美国机构和与美国机构打交道的机构尤其相关。

NIST 800-63的术语一开始可能有点令人困惑，特别是你只习惯于用户名+密码认证的话。 现代认证的进步是必要的，所以我们必须引入将来会变得司空见惯的术语，但我们确实理解：在行业落实这些新术语之前，理解这些新术语的困难。 我们在本章末尾提供了一个词汇表，以提供帮助。 我们重新表述了许多要求，以满足要求的意图，而不只是拘泥于文字。 例如，当NIST在本标准中使用“记忆秘密”时（memorized secret），ASV使用术语“密码”（password）。

ASVS V2 身份验证、V3 会话管理以及在较小程度上的V4 访问控制，已被调整为符合 NIST 800-63b 控制项的一个子集，主要围绕常见的威胁和经常被利用的认证弱点。如果需要完全遵守NIST 800-63，请参考NIST 800-63。

### 选择合适的 NIST AAL 级别

应用程序安全验证标准（ASVS），已尝试将 ASVS L1 对应到 NIST AAL1 要求，将 L2 对应到 AAL2，将 L3 对应到 AAL3。 然而，ASVS Level 1作为“基本”的控制，不一定是验证应用或API的正确AAL级别。 例如，如果该应用是 L3 应用或有 AAL3 的监管要求，则应在V2和V3会话管理章节选择 L3。 应根据NIST 800-63b指南选择符合NIST标准的认证保证级别（AAL），如[NIST 800-63b第6.2节](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA) 中的 *Selecting AAL* 。

## 图例

应用程序总是可以超过当前级别的要求，特别是如果现代认证是在应用程序的路线图上。以前，ASVS要求强制MFA。NIST不要求强制MFA。因此，我们在本章中使用了一个可选的指定，以表明ASVS鼓励但不要求控制的地方。本标准自始至终使用了以下图示：

| 标记 | 说明 |
| :--: | :-- |
| | 不要求 |
| o | 建议，但不要求 |
| ✓ | 要求 |

## V2.1 密码安全

在NIST 800-63中，密码被称为“记忆的秘密”（Memorized Secrets），包括密码、PIN、解锁图案、选择正确的小猫或其他图像元素以及密码短语。 它们通常被认为是“您知道的东西”，并且通常用作单因素身份认证工具。 继续使用单因素认证有很大的风险，包括互联网上披露的数十亿有效用户名和密码、默认或弱密码、彩虹表和最常见密码的有序字典。

应用程序应强烈鼓励用户注册多因素认证，并应允许用户重新使用他们已经拥有的令牌，如FIDO或U2F令牌，或链接到提供多因素认证的凭证服务提供商。

凭据服务提供商（CSP）为用户提供联合身份。 用户通常会拥有多个CSP的多个身份，例如使用Azure AD、Okta、Ping identity或Google的企业身份，或使用Facebook、Twitter、Google或微信的普通用户，这只是一些常见的可能。 这份清单并不是对这些公司或服务的认可，而只是鼓励开发者考虑用户有许多既定身份的现实。 组织应该考虑与现有的用户身份整合，根据CSP的身份证明强度的风险状况，组织应考虑与现有用户身份集成。 例如，政府机构不太可能接受社交媒体身份作为敏感系统的登录名，因为很容易伪造或丢弃身份，而移动游戏公司可能需要与主要社交媒体平台整合，以扩大他们的活跃玩家群。

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.1.1** | 验证用户设置的密码长度至少为 12 个字符（多个空格合并后）。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | 验证是否允许64个字符以上的密码，并拒绝超过128个字符的密码。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | 验证不进行密码截断。然而，连续的多个空格可以被单个空格代替。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.4** | 验证密码中是否允许使用任何可打印的Unicode字符，包括语言中立字符，例如空格和表情符号。 | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | 验证用户可以更改其密码。 | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | 验证密码更改功能是否需要用户的当前密码和新密码。 | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | 验证在账户注册、登录和密码更改过程中提交的密码，是否出现在被泄露过的密码中，这些密码可以是本地的（如符合系统密码策略的前1000个或10000个最常见的密码），也可以使用外部API。 如果使用API，应使用零知识证明或其他机制，以确保纯文本密码不被发送或用于验证密码的违反状态。 如果密码被泄露，应用程序必须要求用户设置一个新的未被泄露的密码。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | 验证是否提供了密码强度表，以帮助用户设置更强的密码。 | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.9** | 验证是否有限制允许的字符类型的密码组成规则。对大写或小写、数字或特殊字符不应有任何要求。 ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | 验证没有定期更换凭证或密码历史的要求。 | ✓ | ✓ | ✓ | 263 | 5.1.1.2 |
| **2.1.11** | 验证是否允许 “粘贴” 功能、浏览器密码辅助工具和外部密码管理器。 | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | 验证用户可以选择临时查看整个屏蔽的密码，或者在没有内置功能的平台上临时查看密码的最后输入的字符。 | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |

注意：允许用户查看密码或临时查看最后一个字符的目的，是为了提高凭证输入的可用性，尤其是在使用更长的密码、口令和密码管理器时。 包含该要求的另一个原因，是为了防止测试报告不必要地要求组织重写内置平台密码字段的行为，从而保持这种现代用户友好的安全体验。

## V2.2 通用身份验证器的安全性

身份验证器的敏捷性，对于面向未来的应用程序至关重要。 重构应用程序验证器以允许用户根据偏好添加额外的验证器，并允许以有序的方式停用已弃用或不安全的验证器。

NIST 将电子邮件和 SMS 视为 [“受限”的身份验证器类型](https://pages.nist.gov/800-63-FAQ/#q-b1)，它们很可能在未来的某个时候从NIST 800-63以及ASVS中删除。 应用程序应计划一个不需要使用电子邮件或短信的路线图。

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.2.1** | 验证反自动化控制的措施能够有效地缓解被泄露的凭证测试、暴力破解和账户锁定攻击。 这些控制措施包括阻止最常见的泄露密码、软锁定、速率限制、验证码、每次尝试后逐渐增加的间隔时间、IP地址限制，或基于风险的限制，例如位置、设备上的首次登录、最近解锁账户的尝试等类似情况。 验证单个帐户每小时的失败尝试次数不超过 100 次。 | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | 验证弱身份验证器（例如 SMS 和电子邮件）的使用，仅限于二次验证和批准交易，而不是作为更安全的认证方法的替代。 验证是否在弱方法之前提供了更强的方法，用户是否意识到风险，或者是否采取了适当的措施来限制帐户泄露的风险。 | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | 验证在更新认证信息（如凭证重置、电子邮件或地址变更、从未知或风险地点登录）后向用户发送安全通知。 最好使用推送通知——而不是短信或电子邮件，但在没有推送通知的情况下，只要通知中没有披露敏感信息，短信或电子邮件也是可以接受的。 | ✓ | ✓ | ✓ | 620 | |
| **2.2.4** | 验证对网络钓鱼的抗冒充性，如使用多因素认证、有意图的加密设备（如有推送认证的连接密钥），或在更高的AAL级别，客户端证书。 | | | ✓ | 308 | 5.2.5 |
| **2.2.5** | 验证当凭证服务提供者（CSP）和验证认证的应用程序分开时，两个端点之间有相互认证的TLS（mTLS）。 | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | 验证抗重放性，是否通过强制使用一次性密码（OTP）设备、加密认证器或查询代码。 | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | 通过要求输入OTP令牌或用户发起的动作（如按下FIDO硬件钥匙的按钮）来验证认证意图。 | | | ✓ | 308 | 5.2.9 |

## V2.3 身份验证器生命周期

Authenticators are passwords, soft tokens, hardware tokens, and biometric devices. The lifecycle of authenticators is critical to the security of an application - if anyone can self-register an account with no evidence of identity, there can be little trust in the identity assertion. For social media sites like Reddit, that's perfectly okay. For banking systems, a greater focus on the registration and issuance of credentials and devices is critical to the security of the application.

Note: Passwords are not to have a maximum lifetime or be subject to password rotation. Passwords should be checked for being breached, not regularly replaced.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.3.1** | Verify system generated initial passwords or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers, and expire after a short period of time. These initial secrets must not be permitted to become the long term password. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Verify that enrollment and use of user-provided authentication devices are supported, such as a U2F or FIDO tokens. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | Verify that renewal instructions are sent with sufficient time to renew time bound authenticators. | | ✓ | ✓ | 287 | 6.1.4 |

## V2.4 Credential Storage

Architects and developers should adhere to this section when building or refactoring code. This section can only be fully verified using source code review or through secure unit or integration tests. Penetration testing cannot identify any of these issues.

The list of approved one-way key derivation functions is detailed in NIST 800-63 B section 5.1.1.2, and in [BSI Kryptographische Verfahren: Empfehlungen und Schlussell&auml;ngen (2018)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). The latest national or regional algorithm and key length standards can be chosen in place of these choices.

This section cannot be penetration tested, so controls are not marked as L1. However, this section is of vital importance to the security of credentials if they are stolen, so if forking the ASVS for an architecture or coding guideline or source code review checklist, please place these controls back to L1 in your private version.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.4.1** | Verify that passwords are stored in a form that is resistant to offline attacks. Passwords SHALL be salted and hashed using an approved one-way key derivation or password hashing function. Key derivation and password hashing functions take a password, a salt, and a cost factor as inputs when generating a password hash. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | Verify that the salt is at least 32 bits in length and be chosen arbitrarily to minimize salt value collisions among stored hashes. For each credential, a unique salt value and the resulting hash SHALL be stored. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.3** | Verify that if PBKDF2 is used, the iteration count SHOULD be as large as verification server performance will allow, typically at least 100,000 iterations. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.4** | Verify that if bcrypt is used, the work factor SHOULD be as large as verification server performance will allow, with a minimum of 10. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.5** | Verify that an additional iteration of a key derivation function is performed, using a salt value that is secret and known only to the verifier. Generate the salt value using an approved random bit generator [SP 800-90Ar1] and provide at least the minimum security strength specified in the latest revision of SP 800-131A. The secret salt value SHALL be stored separately from the hashed passwords (e.g., in a specialized device like a hardware security module). | | ✓ | ✓ | 916 | 5.1.1.2 |

Where US standards are mentioned, a regional or local standard can be used in place of or in addition to the US standard as required.

## V2.5 Credential Recovery

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.5.1** | Verify that a system generated initial activation or recovery secret is not sent in clear text to the user. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.2** | Verify password hints or knowledge-based authentication (so-called "secret questions") are not present. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | Verify password credential recovery does not reveal the current password in any way. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.4** | Verify shared or default accounts are not present (e.g. "root", "admin", or "sa"). | ✓ | ✓ | ✓ | 16 | 5.1.1.2 / A.3 |
| **2.5.5** | Verify that if an authentication factor is changed or replaced, that the user is notified of this event. | ✓ | ✓ | ✓ | 304 | 6.1.2.3 |
| **2.5.6** | Verify forgotten password, and other recovery paths use a secure recovery mechanism, such as time-based OTP (TOTP) or other soft token, mobile push, or another offline recovery mechanism. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | Verify that if OTP or multi-factor authentication factors are lost, that evidence of identity proofing is performed at the same level as during enrollment. | | ✓ | ✓ | 308 | 6.1.2.3 |

## V2.6 Look-up Secret Verifier

Look up secrets are pre-generated lists of secret codes, similar to Transaction Authorization Numbers (TAN), social media recovery codes, or a grid containing a set of random values. These are distributed securely to users. These lookup codes are used once, and once all used, the lookup secret list is discarded. This type of authenticator is considered "something you have".

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.6.1** | Verify that lookup secrets can be used only once. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | Verify that lookup secrets have sufficient randomness (112 bits of entropy), or if less than 112 bits of entropy, salted with a unique and random 32-bit salt and hashed with an approved one-way hash. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | Verify that lookup secrets are resistant to offline attacks, such as predictable values. | | ✓ | ✓ | 310 | 5.1.2.2 |

## V2.7 Out of Band Verifier

In the past, a common out of band verifier would have been an email or SMS containing a password reset link. Attackers use this weak mechanism to reset accounts they don't yet control, such as taking over a person's email account and re-using any discovered reset links. There are better ways to handle out of band verification.

Secure out of band authenticators are physical devices that can communicate with the verifier over a secure secondary channel. Examples include push notifications to mobile devices. This type of authenticator is considered "something you have". When a user wishes to authenticate, the verifying application sends a message to the out of band authenticator via a connection to the authenticator directly or indirectly through a third party service. The message contains an authentication code (typically a random six digit number or a modal approval dialog). The verifying application waits to receive the authentication code through the primary channel and compares the hash of the received value to the hash of the original authentication code. If they match, the out of band verifier can assume that the user has authenticated.

The ASVS assumes that only a few developers will be developing new out of band authenticators, such as push notifications, and thus the following ASVS controls apply to verifiers, such as authentication API, applications, and single sign-on implementations. If developing a new out of band authenticator, please refer to NIST 800-63B &sect; 5.1.3.1.

Unsafe out of band authenticators such as e-mail and VOIP are not permitted. PSTN and SMS authentication are currently "restricted" by NIST and should be deprecated in favor of push notifications or similar. If you need to use telephone or SMS out of band authentication, please see &sect; 5.1.3.3.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.7.1** | Verify that clear text out of band (NIST "restricted") authenticators, such as SMS or PSTN, are not offered by default, and stronger alternatives such as push notifications are offered first. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | Verify that the out of band verifier expires out of band authentication requests, codes, or tokens after 10 minutes. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | Verify that the out of band verifier authentication requests, codes, or tokens are only usable once, and only for the original authentication request. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | Verify that the out of band authenticator and verifier communicates over a secure independent channel. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | Verify that the out of band verifier retains only a hashed version of the authentication code. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | Verify that the initial authentication code is generated by a secure random number generator, containing at least 20 bits of entropy (typically a six digital random number is sufficient). | | ✓ | ✓ | 310 | 5.1.3.2 |

## V2.8 One Time Verifier

Single-factor One-time Passwords (OTPs) are physical or soft tokens that display a continually changing pseudo-random one-time challenge. These devices make phishing (impersonation) difficult, but not impossible. This type of authenticator is considered "something you have". Multi-factor tokens are similar to single-factor OTPs, but require a valid PIN code, biometric unlocking, USB insertion or NFC pairing or some additional value (such as transaction signing calculators) to be entered to create the final OTP.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.8.1** | Verify that time-based OTPs have a defined lifetime before expiring. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Verify that symmetric keys used to verify submitted OTPs are highly protected, such as by using a hardware security module or secure operating system based key storage. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2|
| **2.8.3** | Verify that approved cryptographic algorithms are used in the generation, seeding, and verification of OTPs. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Verify that time-based OTP can be used only once within the validity period. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Verify that if a time-based multi-factor OTP token is re-used during the validity period, it is logged and rejected with secure notifications being sent to the holder of the device. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Verify physical single-factor OTP generator can be revoked in case of theft or other loss. Ensure that revocation is immediately effective across logged in sessions, regardless of location. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | Verify that biometric authenticators are limited to use only as secondary factors in conjunction with either something you have and something you know. | | o | ✓ | 308 | 5.2.3 |

## V2.9 Cryptographic Verifier

Cryptographic security keys are smart cards or FIDO keys, where the user has to plug in or pair the cryptographic device to the computer to complete authentication. Verifiers send a challenge nonce to the cryptographic devices or software, and the device or software calculates a response based upon a securely stored cryptographic key.

The requirements for single-factor cryptographic devices and software, and multi-factor cryptographic devices and software are the same, as verification of the cryptographic authenticator proves possession of the authentication factor.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.9.1** | Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a Trusted Platform Module (TPM) or Hardware Security Module (HSM), or an OS service that can use this secure storage. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | Verify that approved cryptographic algorithms are used in the generation, seeding, and verification. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Service Authentication

This section is not penetration testable, so does not have any L1 requirements. However, if used in an architecture, coding or secure code review, please assume that software (just as Java Key Store) is the minimum requirement at L1. Clear text storage of secrets is not acceptable under any circumstances.

| # | 说明 | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.10.1** | Verify that intra-service secrets do not rely on unchanging credentials such as passwords, API keys or shared accounts with privileged access. | | OS assisted | HSM | 287 | 5.1.1.1 |
| **2.10.2** | Verify that if passwords are required for service authentication, the service account used is not a default credential. (e.g. root/root or admin/admin are default in some services during installation). | | OS assisted | HSM | 255 | 5.1.1.1 |
| **2.10.3** | Verify that passwords are stored with sufficient protection to prevent offline recovery attacks, including local system access. | | OS assisted | HSM | 522 | 5.1.1.1 |
| **2.10.4** | Verify passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a secure software key store (L1), hardware TPM, or an HSM (L3) is recommended for password storage. | | OS assisted | HSM | 798 | |

## Additional US Agency Requirements

US Agencies have mandatory requirements concerning NIST 800-63. The Application Security Verification Standard has always been about the 80% of controls that apply to nearly 100% of apps, and not the last 20% of advanced controls or those that have limited applicability. As such, the ASVS is a strict subset of NIST 800-63, especially for IAL1/2 and AAL1/2 classifications, but is not sufficiently comprehensive, particularly concerning IAL3/AAL3 classifications.

We strongly urge US government agencies to review and implement NIST 800-63 in its entirety.

## Glossary of terms

| Term | Meaning |
| -- | -- |
| CSP | Credential Service Provider also called an Identity Provider |
| Authenticator | Code that authenticates a password, token, MFA, federated assertion, and so on. |
| Verifier | "An entity that verifies the claimant's identity by verifying the claimant's possession and control of one or two authenticators using an authentication protocol. To do this, the verifier may also need to validate credentials that link the authenticator(s) to the subscriber's identifier and check their status" |
| OTP | One-time password |
| SFA | Single-factor authenticators, such as something you know (memorized secrets, passwords, passphrases, PINs), something you are (biometrics, fingerprint, face scans), or something you have (OTP tokens, a cryptographic device such as a smart card), |
| MFA | Multi-factor authentication, which includes two or more single factors |

## References

For more information, see also:

* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
