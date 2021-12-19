# 评估和认证

## OWASP对ASVS认证和信任标志的立场

OWASP作为一个与供应商无关的非营利性组织，目前不认证任何供应商、验证人员或软件。

所有这类保证声明、信任标志或认证，均未经 OWASP 正式审查、注册或认证，因此依赖此类观点的组织，需要谨慎对待任何第三方的信任或声称ASVS认证的信任标志。

这并不影响组织提供此类保证服务，只要他们不要求官方的 OWASP 认证。

## 认证组织指南

应用程序安全验证标准，可以用作应用程序的公开验证，包括对关键资源的开放和自由访问（如架构师和开发人员、项目文档、源代码），对测试系统的认证访问（包括对每个角色的一个或多个帐户的访问），特别是L2和L3验证。

从历史上看，渗透测试和安全代码审查都包含“异常”问题——即只有未通过的测试项才会出现在最终报告中。 认证组织必须在任何报告中包括验证的范围(特别是某个关键组件不在范围内时，如SSO身份验证)、验证结果的摘要，包括通过的和未通过的测试，并清楚地说明如何解决未通过的测试。

某些验证要求可能不适用于被测试的应用程序。例如，如果你向客户提供无状态的服务层API而没有客户端实现，那么“V3-会话管理”中的许多要求就不能直接使用。 在这种情况下，认证机构仍可声称完全符合 ASVS 的要求，但必须在报告中明确说明被排除的验证要求不适用的原因。

保留详细的工作底稿、屏幕截图或视频、可靠地重复利用一个问题的脚本，以及测试的电子记录，如拦截代理日志和相关的笔记（如清理清单），被认为是标准的行业惯例，哪怕是对于最可疑的开发人员来说，它们也能作为调查结果的证明。 仅仅跑一个工具并报告故障是不够的，这根本不能提供充分的证据，证明所有认证级别的问题都经过了彻底的测试。 在有争议的情况下，应该有足够的证据，来证明每一个经过验证的需求确实被测试过。

### 测试方法

认证机构可自由选择适当的测试方法，但应在报告中注明。

根据所测试的应用程序和验证需求，可以使用不同的测试方法来获得相似的结果置信度。 例如，要验证应用程序输入验证机制的有效性，可以通过手动渗透测试或通过源代码来分析。

#### 自动化安全测试工具的作用

鼓励使用自动化渗透测试工具以提供尽可能多的覆盖范围。

仅使用自动渗透测试工具，是不可能完全完成ASVS验证的。虽然L1中的绝大多数需求可以使用自动化测试来执行，但总体上，绝大多数需求并不适合自动化渗透测试。

请注意，随着应用安全行业的成熟，自动化和手动测试之间的界限已经变得模糊。 自动化工具通常由专家手动调整，而手动测试人员通常会利用各种自动化工具。

#### The Role of Penetration Testing

In version 4.0, we decided to make L1 completely penetration testable without access to source code, documentation, or developers. Two logging items, which are required to comply with OWASP Top 10 2017 A10, will require interviews, screenshots or other evidence collection, just as they do in the OWASP Top 10 2017. However, testing without access to necessary information is not an ideal method of security verification, as it misses out on the possibility of reviewing the source, identifying threats and missing controls, and performing a far more thorough test in a shorter timeframe. 

Where possible, access to developers, documentation, code, and access to a test application with non-production data, is required when performing a L2 or L3 Assessment. Penetration testing done at these levels requires this level of access, which we call "hybrid reviews" or "hybrid penetration tests". 

## Other uses for the ASVS

Aside from being used to assess the security of an application, we have identified a number of other potential uses for the ASVS.

### As Detailed Security Architecture Guidance

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. The Sherwood Applied Business Security Architecture (SABSA) is missing a great deal of information that is necessary to complete a thorough application security architecture review. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies.

### As a Replacement for Off-the-shelf Secure Coding Checklists

Many organizations can benefit from adopting the ASVS, by choosing one of the three levels, or by forking ASVS and changing what is required for each application risk level in a domain specific way. We encourage this type of forking as long as traceability is maintained, so that if an app has passed requirement 4.1, this means the same thing for forked copies as the standard as it evolves.

### As a Guide for Automated Unit and Integration Tests

The ASVS is designed to be highly testable, with the sole exception of architectural and malicious code requirements. By building unit and integration tests that test for specific and relevant fuzz and abuse cases, the application becomes nearly self-verifying with each and every build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common default usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, and more.

### For Secure Development Training

ASVS can also be used to define characteristics of secure software. Many “secure coding” courses are simply ethical hacking courses with a light smear of coding tips. This may not necessarily help developers to write more secure code. Instead, secure development courses can use the ASVS with a strong focus on the proactive controls found in the ASVS, rather than the Top 10 negative things not to do.

### As a Driver for Agile Application Security

ASVS can be used in an agile development process as a framework to define specific tasks that need to be implemented by the team to have a secure product. One approach might be: Starting with Level 1, verify the specific application or system according to ASVS requirements for the specified level, find what controls are missing and raise specific tickets/tasks in the backlog. This helps with prioritization of specific tasks (or grooming), and makes security visible in the agile process. This can also be used to prioritize auditing and reviewing tasks in the organization, where a specific ASVS requirement can be a driver for review, refactor or auditing for a specific team member and visible as "debt" in the backlog that needs to be eventually done.

### As a Framework for Guiding the Procurement of Secure Software

ASVS is a great framework to help with secure software procurement or procurement of custom development services. The buyer can simply set a requirement that the software they wish to procure must be developed at ASVS level X, and request that the seller proves that the software satisfies ASVS level X. This works well when combined with the OWASP Secure Software Contract Annex
