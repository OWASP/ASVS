# V52 Self-contained Tokens

## Control Objective

The concept of a self-contained token is mentioned in the original RFC 6749 OAuth 2.0 from 2012. It effectively refers to a token which contains data or claims which a receiving service will rely upon to make security decisions. This is to be differentiated from a token which is just an identifier which a receiving service will use to lookup data locally. The most common example of a self-contained token is a JSON Web Token (JWT) but a SAML assertion could also fall into this category.

The use of self-contained tokens has become very widespread, even outside of OIDC/OAuth. At the same time, the security of this mechanism relies on the ability to validate the integrity of the token and to ensure that the token is valid for a particular context. There are many pitfalls with this process and this chapter will provide specific details of the mechanisms that applications should have in place to prevent them.

## V52.1 Token source and integrity

Before inspecting the contents of a self-contained token, it is necessary to ensure that the token has been produced by a trusted party and that it has not been tampered with.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **52.1.1** | [MOVED FROM 3.5.3, MODIFIED, LEVEL L2 > L1] Verify that the authenticity of cryptographically secured tokens is validated using their digital signature or MAC to protect against tampering before accepting the token's contents. | ✓ | ✓ | ✓ | 345 |
| **52.1.2** | [ADDED] Verify that only algorithms on an allowlist are used to create and validate cryptographically secured tokens. The allowlist must only include algorithms which are considered strong for this purpose according to current recommendations (such as PS256 for JWTs) and must not allow integrity validation to be ignored (such as accepting the 'None' algorithm for JWTs). | ✓ | ✓ | ✓ | 757 |
| **52.1.3** | [ADDED] Verify that when the application validates the authenticity of a cryptographically secured token, it only uses key material for the specified cryptographic algorithms and intended usages, to prevent key confusion attacks. For keys provided in JWK format, this can be done by validating the 'kty', 'use', 'key_ops', or 'alg' headers. | ✓ | ✓ | ✓ | |
| **52.1.4** | [ADDED] Verify that the application validates the authenticity of a cryptographically secured token based on key material that is bound to the token issuer. For JWTs and other JWS structures, if the application resolves the key material based on the 'jwk', 'jku', 'x5u' or 'kid' headers, it must interpret and validate (for example using an allowlist) these values depending on the token issuer. | ✓ | ✓ | ✓ | |

## V52.2 Using token content

Before making security decisions based on the content of a self-contained token, it is necessary to validate that the token has been presented within it's validity period and that it is meant for use by the receiving service and for the purpose for which it was presented. This is to avoid insecure cross-usage between different services or with different token types from the same issuer.

Specific requirements for OAuth and OIDC are covered in the dedicated chapter.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **52.2.1** | [ADDED] Verify that, if a validity time span is present in the token data, the token and its content are accepted only if the verification time is within this validity time span. For example, for JWTs the claims 'nbf' and 'exp' must be verified. | ✓ | ✓ | ✓ | 613 |
| **52.2.2** | [ADDED] Verify that the service receiving a token validates the token to be the correct type and is meant for the intended purpose before accepting the token's contents. For example, only access tokens can be accepted for authorization decisions and only ID tokens can be used for proving user authentication. | ✓ | ✓ | ✓ | |
| **52.2.3** | [ADDED] Verify that the service only accepts tokens which are intended for use with that service (audience). For JWTs, this can be achieved by validating the 'aud' claim against an allowlist defined in the service. | ✓ | ✓ | ✓ | |

## References

For more information, see also:

* [OWASP Cheatsheet - JSON Web Token Cheat Sheet for Java](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (but has useful general guidance)
