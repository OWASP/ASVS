# V11 业务逻辑

## 控制目标

确保经过验证的应用程序满足以下高级要求：

* 业务逻辑流程是串行的，按顺序处理的，并且不能被绕过。
* 业务逻辑包括检测和防止自动化攻击，如连续的小额资金转移，或一次添加上百万个好友等。
* 高价值的业务逻辑流已经考虑了滥用情况和恶意行为者，并有防止欺骗、篡改、信息披露和特权提升攻击的保护措施。

## V11.1 业务逻辑安全

业务逻辑安全对每个应用程序来说都是非常独特的，因此没有通用的检查表。业务逻辑安全必须设计成能够抵御可能的外部威胁——它不能使用 Web 应用防火墙或安全通信来添加。我们建议在设计冲刺（Design Sprint）期间使用威胁建模，例如使用 OWASP Cornucopia 或类似工具。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **11.1.1** | 验证应用程序仅按串行顺序处理同一用户的业务逻辑流，不会跳过步骤。 | ✓ | ✓ | ✓ | 841 |
| **11.1.2** | 验证应用程序将只处理业务逻辑流，所有步骤都在现实的人工时间内处理，即事务不会提交得太快。 | ✓ | ✓ | ✓ | 799 |
| **11.1.3** | 验证应用程序是否对特定的业务操作或交易有适当的限制，并在每个用户的基础上正确执行。 | ✓ | ✓ | ✓ | 770 |
| **11.1.4** | 验证应用程序具有反自动化的控制手段，以防止过度调用，如大量数据泄露、业务逻辑请求、文件上传或拒绝服务攻击。 | ✓ | ✓ | ✓ | 770 |
| **11.1.5** | 验证应用程序是否具有业务逻辑限制或验证，以防止可能的业务风险或威胁（使用威胁建模或类似方法识别）。 | ✓ | ✓ | ✓ | 841 |
| **11.1.6** | 验证应用程序是否存在TOCTOU（Time Of Check to Time Of Use）问题 或敏感操作的其他条件竞争问题。 | | ✓ | ✓ | 367 |
| **11.1.7** | 验证应用程序是否从业务逻辑角度监控异常事件或活动。例如，尝试执行无序的操作或普通用户永远不会尝试的操作。 ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 754 |
| **11.1.8** | 验证应用程序在检测到自动化攻击或异常活动时，具有可配置的警报。 | | ✓ | ✓ | 390 |

## 参考文献

有关更多信息，请参阅：

* [OWASP Web Security Testing Guide 4.1: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html)
* 反自动化可以通过多种方式实现，包括使用 [OWASP AppSensor](https://github.com/jtmelton/appsensor) 和 [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP AppSensor](https://github.com/jtmelton/appsensor) 也可以帮助进行攻击检测和响应。
* [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/)
