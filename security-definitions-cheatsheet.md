# Security Definitions Cheatsheet

## Introduction
This cheatsheet provides clear definitions for key security terms that often confuse developers. It is intended to support understanding of the OWASP ASVS standard and other security projects.

## Encoding, Escaping, and Serialization

### Encoding
Encoding is the process of converting data into a different format using a publicly known scheme. It’s mainly used to ensure data can be properly transmitted or stored.

**Example:** Base64 encoding converts binary data to ASCII text.

### Escaping
Escaping means adding special characters before reserved characters to prevent them from being interpreted by parsers or browsers.

**Example:** Escaping `<` as `&lt;` in HTML to prevent injection attacks.

### Serialization
Serialization converts complex data structures into a format that can be easily stored or transmitted and later reconstructed.

**Example:** Converting an object to JSON string for API communication.

## Cryptography Terms

### Encryption
Encryption transforms data to an unreadable format to prevent unauthorized access. It requires a key to decrypt.

### Decryption
The reverse of encryption — turning encrypted data back into its original form using a key.

### Hashing
Hashing creates a fixed-size string (hash) from data. It’s one-way and mainly used for verifying integrity.

### Digital Signature
A digital signature is a cryptographic technique to verify the authenticity and integrity of a message or document.

### Symmetric vs Asymmetric Cryptography
- Symmetric: Same key for encryption and decryption.  
- Asymmetric: Uses a key pair (public and private keys).

## Authentication and Authorization

### Authentication
Verifying the identity of a user or system.

### Authorization
Determining what an authenticated user or system is allowed to do.

## Other Important Terms

### Vulnerability
A weakness in a system that can be exploited.

### Threat
A potential cause of unwanted impact.

### Risk
The potential loss or damage when a threat exploits a vulnerability.

## References
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [CNCF Glossary](https://github.com/cncf/glossary)
