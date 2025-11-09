# V13 Configuration

## Control Objective

The application's default configuration must be secure for use on the Internet.

This chapter provides guidance on the various configurations necessary to achieve this, including those applied during development, build, and deployment.

Topics covered include preventing data leakage, securely managing communication between components, and protecting secrets.

## V13.1 Configuration Documentation

This section outlines documentation requirements for how the application communicates with internal and external services, as well as techniques to prevent loss of availability due to service inaccessibility. It also addresses documentation related to secrets.

| # | Description | Level |
| :---: | :--- | :---: |
| **13.1.1** | Verify that all communication needs for the application are documented. This must include external services which the application relies upon and cases where an end user might be able to provide an external location to which the application will then connect. | 2 |
| **13.1.2** | Verify that for each service the application uses, the documentation defines the maximum number of concurrent connections (e.g., connection pool limits) and how the application behaves when that limit is reached, including any fallback or recovery mechanisms, to prevent denial of service conditions. | 3 |
| **13.1.3** | Verify that the application documentation defines resource‑management strategies for every external system or service it uses (e.g., databases, file handles, threads, HTTP connections). This should include resource‑release procedures, timeout settings, failure handling, and where retry logic is implemented, specifying retry limits, delays, and back‑off algorithms. For synchronous HTTP request–response operations it should mandate short timeouts and either disable retries or strictly limit retries to prevent cascading delays and resource exhaustion. | 3 |
| **13.1.4** | Verify that the application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and business requirements. | 3 |

## V13.2 Backend Communication Configuration

Applications interact with multiple services, including APIs, databases, or other components. These may be considered internal to the application but not included in the application's standard access control mechanisms, or they may be entirely external. In either case, it is necessary to configure the application to interact securely with these components and, if required, protect that configuration.

Note: The "Secure Communication" chapter provides guidance for encryption in transit.

| # | Description | Level |
| :---: | :--- | :---: |
| **13.2.1** | Verify that communications between backend application components that don't support the application's standard user session mechanism, including APIs, middleware, and data layers, are authenticated. Authentication must use individual service accounts, short-term tokens, or certificate-based authentication and not unchanging credentials such as passwords, API keys, or shared accounts with privileged access. | 2 |
| **13.2.2** | Verify that communications between backend application components, including local or operating system services, APIs, middleware, and data layers, are performed with accounts assigned the least necessary privileges. | 2 |
| **13.2.3** | Verify that if a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g., root/root or admin/admin). | 2 |
| **13.2.4** | Verify that an allowlist is used to define the external resources or systems with which the application is permitted to communicate (e.g., for outbound requests, data loads, or file access). This allowlist can be implemented at the application layer, web server, firewall, or a combination of different layers. | 2 |
| **13.2.5** | Verify that the web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from. | 2 |
| **13.2.6** | Verify that where the application connects to separate services, it follows the documented configuration for each connection, such as maximum parallel connections, behavior when maximum allowed connections is reached, connection timeouts, and retry strategies. | 3 |

## V13.3 Secret Management

Secret management is an essential configuration task to ensure the protection of data used in the application. Specific requirements for cryptography can be found in the "Cryptography" chapter, but this section focuses on the management and handling aspects of secrets.

| # | Description | Level |
| :---: | :--- | :---: |
| **13.3.1** | Verify that a secrets management solution, such as a key vault, is used to securely create, store, control access to, and destroy backend secrets. These could include passwords, key material, integrations with databases and third-party systems, keys and seeds for time-based tokens, other internal secrets, and API keys. Secrets must not be included in application source code or included in build artifacts. For an L3 application, this must involve a hardware-backed solution such as an HSM. | 2 |
| **13.3.2** | Verify that access to secret assets adheres to the principle of least privilege. | 2 |
| **13.3.3** | Verify that all cryptographic operations are performed using an isolated security module (such as a vault or hardware security module) to securely manage and protect key material from exposure outside of the security module. | 3 |
| **13.3.4** | Verify that secrets are configured to expire and be rotated based on the application's documentation. | 3 |

## V13.4 Unintended Information Leakage

Production configurations should be hardened to avoid disclosing unnecessary data. Many of these issues are rarely rated as significant risks but are often chained with other vulnerabilities. If these issues are not present by default, it raises the bar for attacking an application.

For example, hiding the version of server-side components does not eliminate the need to patch all components, and disabling folder listing does not remove the need to use authorization controls or keep files away from the public folder, but it raises the bar.

| # | Description | Level |
| :---: | :--- | :---: |
| **13.4.1** | Verify that the application is deployed either without any source control metadata, including the .git or .svn folders, or in a way that these folders are inaccessible both externally and to the application itself. | 1 |
| **13.4.2** | Verify that debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage. | 2 |
| **13.4.3** | Verify that web servers do not expose directory listings to clients unless explicitly intended. | 2 |
| **13.4.4** | Verify that using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage. | 2 |
| **13.4.5** | Verify that documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended. | 2 |
| **13.4.6** | Verify that the application does not expose detailed version information of backend components. | 3 |
| **13.4.7** | Verify that the web tier is configured to only serve files with specific file extensions to prevent unintentional information, configuration, and source code leakage. | 3 |

## References

For more information, see also:

* [OWASP Web Security Testing Guide: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing)
