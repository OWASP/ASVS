<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x18-V9-Self-contained-Tokens.md -->
<!-- Translator: GeeksikhSecurity -->

# V9 Self-contained Tokens
# V9 ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ (Self-contained Tokens)

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

The concept of a self-contained token is mentioned in the original RFC 6749 OAuth 2.0 from 2012. It refers to a token containing data or claims on which a receiving service will rely to make security decisions. This should be differentiated from a simple token containing only an identifier, which a receiving service uses to look up data locally. The most common examples of self-contained tokens are JSON Web Tokens (JWTs) and SAML assertions.

ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ (Self-contained Token) ਦਾ ਸੰਕਲਪ ੨੦੧੨ ਦੇ ਮੂਲ RFC 6749 OAuth 2.0 ਵਿੱਚ ਜ਼ਿਕਰ ਕੀਤਾ ਗਿਆ ਹੈ. ਇਹ ਅਜਿਹੇ ਟੋਕਨ ਦਾ ਹਵਾਲਾ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਡਾਟਾ ਜਾਂ ਦਾਅਵੇ (claims) ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ, ਜਿਨ੍ਹਾਂ ਉੱਤੇ ਪ੍ਰਾਪਤਕਰਤਾ ਸੇਵਾ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ ਲੈਣ ਲਈ ਨਿਰਭਰ ਕਰੇਗੀ. ਇਸ ਨੂੰ ਉਸ ਸਾਧਾਰਨ ਟੋਕਨ ਤੋਂ ਵੱਖ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਸਿਰਫ਼ ਇੱਕ ਪਛਾਣਕਰਤਾ (identifier) ਹੁੰਦਾ ਹੈ, ਜਿਸ ਨੂੰ ਪ੍ਰਾਪਤਕਰਤਾ ਸੇਵਾ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਡਾਟਾ ਲੱਭਣ ਲਈ ਵਰਤਦੀ ਹੈ. ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨਾਂ ਦੀਆਂ ਸਭ ਤੋਂ ਆਮ ਉਦਾਹਰਣਾਂ JSON Web Tokens (JWTs) ਅਤੇ SAML assertions ਹਨ.

The use of self-contained tokens has become very widespread, even outside of OAuth and OIDC. At the same time, the security of this mechanism relies on the ability to validate the integrity of the token and to ensure that the token is valid for a particular context. There are many pitfalls with this process, and this chapter provides specific details of the mechanisms that applications should have in place to prevent them.

ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨਾਂ ਦੀ ਵਰਤੋਂ ਬਹੁਤ ਵਿਆਪਕ ਹੋ ਗਈ ਹੈ, OAuth ਅਤੇ OIDC ਤੋਂ ਬਾਹਰ ਵੀ. ਇਸ ਦੇ ਨਾਲ ਹੀ, ਇਸ ਵਿਧੀ ਦੀ ਸੁਰੱਖਿਆ ਟੋਕਨ ਦੀ ਅਖੰਡਤਾ (integrity) ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਦੀ ਯੋਗਤਾ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ ਕਿ ਟੋਕਨ ਕਿਸੇ ਖ਼ਾਸ ਸੰਦਰਭ (context) ਲਈ ਜਾਇਜ਼ ਹੈ. ਇਸ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਕਈ ਖ਼ਤਰੇ ਹਨ, ਅਤੇ ਇਹ ਅਧਿਆਇ ਉਹਨਾਂ ਵਿਧੀਆਂ ਦੇ ਖ਼ਾਸ ਵੇਰਵੇ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਕੋਲ ਉਹਨਾਂ ਨੂੰ ਰੋਕਣ ਲਈ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ.

## V9.1 Token source and integrity
## V9.1 ਟੋਕਨ ਸਰੋਤ ਅਤੇ ਅਖੰਡਤਾ (Token source and integrity)

This section includes requirements to ensure that the token has been produced by a trusted party and has not been tampered with.

ਇਸ ਭਾਗ ਵਿੱਚ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਕਿ ਟੋਕਨ ਕਿਸੇ ਭਰੋਸੇਯੋਗ ਪੱਖ ਦੁਆਰਾ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਸ ਨਾਲ ਛੇੜਛਾੜ ਨਹੀਂ ਕੀਤੀ ਗਈ.

| # | Description | Level |
| :---: | :--- | :---: |
| **9.1.1** | Verify that self-contained tokens are validated using their digital signature or MAC to protect against tampering before accepting the token's contents. | 1 |
| **9.1.2** | Verify that only algorithms on an allowlist can be used to create and verify self-contained tokens, for a given context. The allowlist must include the permitted algorithms, ideally only either symmetric or asymmetric algorithms, and must not include the 'None' algorithm. If both symmetric and asymmetric must be supported, additional controls will be needed to prevent key confusion. | 1 |
| **9.1.3** | Verify that key material that is used to validate self-contained tokens is from trusted pre-configured sources for the token issuer, preventing attackers from specifying untrusted sources and keys. For JWTs and other JWS structures, headers such as 'jku', 'x5u', and 'jwk' must be validated against an allowlist of trusted sources. | 1 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **9.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨਾਂ ਨੂੰ ਟੋਕਨ ਦੀ ਸਮੱਗਰੀ ਸਵੀਕਾਰ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਛੇੜਛਾੜ ਤੋਂ ਬਚਾਉਣ ਲਈ ਉਹਨਾਂ ਦੇ ਡਿਜੀਟਲ ਦਸਤਖ਼ਤ (digital signature) ਜਾਂ MAC ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ. | ੧ |
| **9.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਿਸੇ ਦਿੱਤੇ ਸੰਦਰਭ ਲਈ, ਸਿਰਫ਼ allowlist ਉੱਤੇ ਮੌਜੂਦ algorithms ਹੀ ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ ਬਣਾਉਣ ਅਤੇ ਤਸਦੀਕ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ. Allowlist ਵਿੱਚ ਪ੍ਰਵਾਨਿਤ algorithms ਸ਼ਾਮਲ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ, ਆਦਰਸ਼ਕ ਤੌਰ 'ਤੇ ਜਾਂ ਤਾਂ ਸਿਰਫ਼ symmetric ਜਾਂ ਸਿਰਫ਼ asymmetric algorithms, ਅਤੇ ਇਸ ਵਿੱਚ 'None' algorithm ਸ਼ਾਮਲ ਨਹੀਂ ਹੋਣਾ ਚਾਹੀਦਾ. ਜੇਕਰ symmetric ਅਤੇ asymmetric ਦੋਵਾਂ ਦਾ ਸਮਰਥਨ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ, ਤਾਂ key confusion ਨੂੰ ਰੋਕਣ ਲਈ ਵਾਧੂ ਨਿਯੰਤਰਣਾਂ ਦੀ ਲੋੜ ਪਵੇਗੀ. | ੧ |
| **9.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨਾਂ ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ key material ਟੋਕਨ ਜਾਰੀਕਰਤਾ (token issuer) ਲਈ ਭਰੋਸੇਯੋਗ ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ ਸਰੋਤਾਂ ਤੋਂ ਆਉਂਦੀ ਹੈ, ਜੋ ਹਮਲਾਵਰਾਂ ਨੂੰ ਅਣਭਰੋਸੇਯੋਗ ਸਰੋਤ ਅਤੇ ਕੁੰਜੀਆਂ ਨਿਰਧਾਰਤ ਕਰਨ ਤੋਂ ਰੋਕਦੀ ਹੈ. JWTs ਅਤੇ ਹੋਰ JWS structures ਲਈ, 'jku', 'x5u', ਅਤੇ 'jwk' ਵਰਗੇ headers ਨੂੰ ਭਰੋਸੇਯੋਗ ਸਰੋਤਾਂ ਦੀ allowlist ਦੇ ਵਿਰੁੱਧ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ. | ੧ |

## V9.2 Token content
## V9.2 ਟੋਕਨ ਸਮੱਗਰੀ (Token content)

Before making security decisions based on the content of a self-contained token, it is necessary to validate that the token has been presented within its validity period and that it is intended for use by the receiving service and for the purpose for which it was presented. This helps avoid insecure cross-usage between different services or with different token types from the same issuer.

ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ ਦੀ ਸਮੱਗਰੀ ਦੇ ਆਧਾਰ 'ਤੇ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ ਲੈਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਟੋਕਨ ਆਪਣੀ ਜਾਇਜ਼ਤਾ ਮਿਆਦ (validity period) ਦੇ ਅੰਦਰ ਪੇਸ਼ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਹ ਪ੍ਰਾਪਤਕਰਤਾ ਸੇਵਾ ਦੁਆਰਾ ਵਰਤੋਂ ਲਈ ਅਤੇ ਉਸ ਉਦੇਸ਼ ਲਈ ਹੈ ਜਿਸ ਲਈ ਇਸ ਨੂੰ ਪੇਸ਼ ਕੀਤਾ ਗਿਆ ਸੀ. ਇਹ ਵੱਖ-ਵੱਖ ਸੇਵਾਵਾਂ ਵਿਚਕਾਰ ਜਾਂ ਉਸੇ ਜਾਰੀਕਰਤਾ ਤੋਂ ਵੱਖ-ਵੱਖ ਟੋਕਨ ਕਿਸਮਾਂ ਨਾਲ ਅਸੁਰੱਖਿਅਤ ਅੰਤਰ-ਵਰਤੋਂ (cross-usage) ਤੋਂ ਬਚਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ.

Specific requirements for OAuth and OIDC are covered in the dedicated chapter.

OAuth ਅਤੇ OIDC ਲਈ ਖ਼ਾਸ ਲੋੜਾਂ ਸਮਰਪਿਤ ਅਧਿਆਇ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ.

| # | Description | Level |
| :---: | :--- | :---: |
| **9.2.1** | Verify that, if a validity time span is present in the token data, the token and its content are accepted only if the verification time is within this validity time span. For example, for JWTs, the claims 'nbf' and 'exp' must be verified. | 1 |
| **9.2.2** | Verify that the service receiving a token validates the token to be the correct type and is meant for the intended purpose before accepting the token's contents. For example, only access tokens can be accepted for authorization decisions and only ID Tokens can be used for proving user authentication. | 2 |
| **9.2.3** | Verify that the service only accepts tokens which are intended for use with that service (audience). For JWTs, this can be achieved by validating the 'aud' claim against an allowlist defined in the service. | 2 |
| **9.2.4** | Verify that, if a token issuer uses the same private key for issuing tokens to different audiences, the issued tokens contain an audience restriction that uniquely identifies the intended audiences. This will prevent a token from being reused with an unintended audience. If the audience identifier is dynamically provisioned, the token issuer must validate these audiences in order to make sure that they do not result in audience impersonation. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **9.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇਕਰ ਟੋਕਨ ਡਾਟਾ ਵਿੱਚ ਜਾਇਜ਼ਤਾ ਸਮਾਂ-ਸੀਮਾ ਮੌਜੂਦ ਹੈ, ਤਾਂ ਟੋਕਨ ਅਤੇ ਉਸ ਦੀ ਸਮੱਗਰੀ ਨੂੰ ਉਦੋਂ ਹੀ ਸਵੀਕਾਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੇਕਰ ਤਸਦੀਕ ਦਾ ਸਮਾਂ ਇਸ ਜਾਇਜ਼ਤਾ ਸਮਾਂ-ਸੀਮਾ ਦੇ ਅੰਦਰ ਹੈ. ਉਦਾਹਰਣ ਲਈ, JWTs ਲਈ, 'nbf' ਅਤੇ 'exp' claims ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ. | ੧ |
| **9.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰਨ ਵਾਲੀ ਸੇਵਾ ਟੋਕਨ ਦੀ ਸਮੱਗਰੀ ਸਵੀਕਾਰ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਟੋਕਨ ਦੀ ਪ੍ਰਮਾਣਿਕਤਾ ਕਰਦੀ ਹੈ ਕਿ ਇਹ ਸਹੀ ਕਿਸਮ ਦਾ ਹੈ ਅਤੇ ਨਿਰਧਾਰਿਤ ਉਦੇਸ਼ ਲਈ ਹੈ. ਉਦਾਹਰਣ ਲਈ, ਅਧਿਕਾਰ (authorization) ਫ਼ੈਸਲਿਆਂ ਲਈ ਸਿਰਫ਼ access tokens ਸਵੀਕਾਰ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ ਅਤੇ ਉਪਭੋਗਤਾ ਪ੍ਰਮਾਣੀਕਰਨ ਸਾਬਤ ਕਰਨ ਲਈ ਸਿਰਫ਼ ID Tokens ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ. | ੨ |
| **9.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੇਵਾ ਸਿਰਫ਼ ਉਹਨਾਂ ਟੋਕਨਾਂ ਨੂੰ ਸਵੀਕਾਰ ਕਰਦੀ ਹੈ ਜੋ ਉਸ ਸੇਵਾ ਨਾਲ ਵਰਤੋਂ ਲਈ ਹਨ (audience). JWTs ਲਈ, ਇਹ ਸੇਵਾ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ allowlist ਦੇ ਵਿਰੁੱਧ 'aud' claim ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਕੇ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ. | ੨ |
| **9.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇਕਰ ਕੋਈ ਟੋਕਨ ਜਾਰੀਕਰਤਾ ਵੱਖ-ਵੱਖ audiences ਨੂੰ ਟੋਕਨ ਜਾਰੀ ਕਰਨ ਲਈ ਇੱਕੋ private key ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ, ਤਾਂ ਜਾਰੀ ਕੀਤੇ ਟੋਕਨਾਂ ਵਿੱਚ audience ਪਾਬੰਦੀ ਸ਼ਾਮਲ ਹੁੰਦੀ ਹੈ ਜੋ ਨਿਰਧਾਰਿਤ audiences ਦੀ ਵਿਲੱਖਣ ਪਛਾਣ ਕਰਦੀ ਹੈ. ਇਹ ਟੋਕਨ ਨੂੰ ਕਿਸੇ ਅਣ-ਨਿਰਧਾਰਿਤ audience ਨਾਲ ਮੁੜ-ਵਰਤੋਂ ਤੋਂ ਰੋਕੇਗਾ. ਜੇਕਰ audience identifier ਨੂੰ ਗਤੀਸ਼ੀਲ ਰੂਪ ਵਿੱਚ ਪ੍ਰਦਾਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਟੋਕਨ ਜਾਰੀਕਰਤਾ ਨੂੰ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਇਹਨਾਂ audiences ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ ਕਿ ਉਹ audience impersonation ਦਾ ਨਤੀਜਾ ਨਹੀਂ ਬਣਦੀਆਂ. | ੨ |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP JSON Web Token Cheat Sheet for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (but has useful general guidance)

* [OWASP JSON Web Token Cheat Sheet for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (ਪਰ ਉਪਯੋਗੀ ਆਮ ਮਾਰਗਦਰਸ਼ਨ ਮੌਜੂਦ ਹੈ)
