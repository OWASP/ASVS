# V4 访问控制

## 控制目标

授权是一个概念，即只允许那些被允许使用资源的人访问资源。确保经过验证的应用程序满足以下高级要求：

* 访问资源的人员持有有效凭据才能这样做。
* 用户与一组明确定义的角色和权限相关联。
* 角色和权限元数据受到保护，不会被重放或篡改。

## 安全验证要求

## V4.1 通用访问控制设计

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.1.1** | 验证应用程序是否在受信任的服务层上执行访问控制规则，尤其是在有客户端访问控制并且可能被绕过的情况下。 | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | 验证访问控制所使用的所有用户和数据属性以及策略信息，不能被最终用户操纵，除非得到特别授权。 | ✓ | ✓ | ✓ | 639 |
| **4.1.3** | 验证是否存在最小权限原则——用户应该只能访问他们拥有特定授权的功能、数据文件、URL、控制器、服务和其他资源。这意味着防止欺骗或特权提升。 ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [已删除，4.1.3 重复] | | | | |
| **4.1.5** | 验证访问控制安全，在发生异常时是否失效。 ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |

## V4.2 操作级访问控制

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.2.1** | 验证敏感数据和API的保护，防止针对创建、读取、更新和删除记录的不安全直接对象引用（IDOR）攻击，如创建或更新别人的记录，查看每个人的记录或删除所有记录。 | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | 验证应用程序或框架是否实施了强大的反 CSRF 机制来保护经过身份验证的功能，以及有效的反自动化或反 CSRF 保护无需身份验证的功能。 | ✓ | ✓ | ✓ | 352 |

## V4.3 其他访问控制注意事项

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.3.1** | 验证管理界面使用适当的多因素认证，防止未经授权的使用。 | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | 验证目录浏览被禁用，除非特意需要。此外，应用程序不应允许披露文件或目录元数据，例如Thumbs.db、.DS_Store、.git或.svn文件夹。 | ✓ | ✓ | ✓ | 548 |
| **4.3.3** | 验证应用程序对低价值的系统有额外的授权（如升级或自适应认证），对高价值的应用程序进行职责分离，以根据应用程序和过去的欺诈风险执行反欺诈控制。 | | ✓ | ✓ | 732 |

## 参考文献

有关更多信息，请参阅：

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP REST Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
