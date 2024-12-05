# V52 Cryptographically Secured Tokens

## Control Objective

In a cryptographically secured token, the authenticity of the token is validated using cryptography. This type of token may just contain a reference to data stored locally within a service or it might be a self-contained token. The concept of a self-contained token is mentioned in the original RFC 6749 OAuth 2.0 from 2012. It effectively refers to a cryptographically secured token which contains data or claims which a receiving service will rely upon to make security decisions. The most common example of a self-contained token is a JSON Web Token (JWT) but a SAML assertion could also fall into this category.

The use of self-contained tokens has become very widespread, even outside of OIDC/OAuth. At the same time, the security of this mechanism relies on the ability to validate the integrity of the token and to ensure that the token is valid for a particular context. There are many pitfalls with this process and this chapter will provide specific details of the mechanisms that applications should have in place to prevent them.

## V52.1 Token source and integrity

Before using a cryptographically secured token, it is necessary to ensure that the token has been produced by a trusted party and that it has not been tampered with.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **52.1.1** | [MOVED FROM 3.5.3, MODIFIED, LEVEL L2 > L1] Verify that cryptographically secured tokens are validated using their digital signature or MAC to protect against tampering before accepting the token's contents. | ✓ | ✓ | ✓ | 345 |
| **52.1.2** | [ADDED] Verify that only algorithms on an allowlist can be used to create and verify cryptographically secured tokens, for a given context. The allowlist should include the permitted algorithms, ideally only either symmetric or asymmetric algorithms, and should not include the 'None' algorithm. If both symmetric and asymmetric are needed, additional controls should prevent key confusion. | ✓ | ✓ | ✓ | 757 |
| **52.1.3** | [ADDED] Verify that key material that is used to validate cryptographically secured tokens is from trusted pre-configured sources for the token issuer, preventing attackers from specifying untrusted sources and keys. For JWTs and other JWS structures, headers such as 'jku', 'x5u', and 'jwk' must be validated against an allowlist of trusted sources. | ✓ | ✓ | ✓ | |

## V52.2 Using token content

For cryptographically secured tokens which are not self-contained tokens, validating the authenticity of the token will be sufficient. However, for a self-contained token, it is necessary to validate that the token has been presented within it's validity period and that it is meant for use by the receiving service and for the purpose for which it was presented, before making security decisions based on the content. This is to avoid insecure cross-usage between different services or with different token types from the same issuer.

Specific requirements for OAuth and OIDC are covered in the dedicated chapter.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **52.2.1** | [ADDED] Verify that, if a validity time span is present in the token data, the token and its content are accepted only if the verification time is within this validity time span. For example, for JWTs the claims 'nbf' and 'exp' must be verified. | ✓ | ✓ | ✓ | 613 |
| **52.2.2** | [ADDED] Verify that the service receiving a token validates the token to be the correct type and is meant for the intended purpose before accepting the token's contents. For example, only access tokens can be accepted for authorization decisions and only ID tokens can be used for proving user authentication. | ✓ | ✓ | ✓ | |
| **52.2.3** | [ADDED] Verify that the service only accepts tokens which are intended for use with that service (audience). For JWTs, this can be achieved by validating the 'aud' claim against an allowlist defined in the service. | ✓ | ✓ | ✓ | |

## References

For more information, see also:

* [OWASP Cheatsheet - JSON Web Token Cheat Sheet for Java](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (but has useful general guidance)
