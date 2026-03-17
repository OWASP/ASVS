# Preface
# ਮੁਖਬੰਧ

Welcome to the Application Security Verification Standard (ASVS) Version 5.0.

ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਮਿਆਰ (ASVS) ਸੰਸਕਰਣ ੫.੦ ਵਿੱਚ ਜੀ ਆਇਆਂ ਨੂੰ.

## Introduction
## ਜਾਣ-ਪਛਾਣ

Originally launched in 2008 through a global community collaboration, the ASVS defines a comprehensive set of security requirements for designing, developing, and testing modern web applications and services.

੨੦੦੮ ਵਿੱਚ ਗਲੋਬਲ ਭਾਈਚਾਰਕ ਸਹਿਯੋਗ ਰਾਹੀਂ ਸ਼ੁਰੂ ਕੀਤਾ ਗਿਆ, ASVS ਆਧੁਨਿਕ ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਦੇ ਡਿਜ਼ਾਈਨ, ਵਿਕਾਸ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ ਸੁਰੱਖਿਆ ਲੋੜਾਂ (Security Requirements) ਦਾ ਇੱਕ ਵਿਆਪਕ ਸੈੱਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ.

Following the release of ASVS 4.0 in 2019 and its minor update (v4.0.3) in 2021, Version 5.0 represents a significant milestone—modernized to reflect the latest advances in software security.

ASVS ੪.੦ ਦੀ ੨੦੧੯ ਵਿੱਚ ਰਿਲੀਜ਼ ਅਤੇ ਇਸ ਦੇ ਛੋਟੇ ਅੱਪਡੇਟ (v੪.੦.੩) ੨੦੨੧ ਵਿੱਚ ਤੋਂ ਬਾਅਦ, ਸੰਸਕਰਣ ੫.੦ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਮੀਲ ਪੱਥਰ ਹੈ — ਸਾਫ਼ਟਵੇਅਰ ਸੁਰੱਖਿਆ ਵਿੱਚ ਨਵੀਨਤਮ ਤਰੱਕੀਆਂ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਆਧੁਨਿਕ ਕੀਤਾ ਗਿਆ ਹੈ.

ASVS 5.0 is the result of extensive contributions from project leaders, working group members, and the wider OWASP community to update and improve this important standard.

ASVS ੫.੦ ਪ੍ਰੋਜੈਕਟ ਮੁਖੀਆਂ, ਕਾਰਜ ਸਮੂਹ ਮੈਂਬਰਾਂ, ਅਤੇ ਵਿਸ਼ਾਲ OWASP ਭਾਈਚਾਰੇ ਦੇ ਵਿਆਪਕ ਯੋਗਦਾਨ ਦਾ ਨਤੀਜਾ ਹੈ ਜੋ ਇਸ ਮਹੱਤਵਪੂਰਨ ਮਿਆਰ ਨੂੰ ਅੱਪਡੇਟ ਅਤੇ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ ਕੀਤਾ ਗਿਆ ਹੈ.

## Principles behind version 5.0
## ਸੰਸਕਰਣ ੫.੦ ਦੇ ਪਿੱਛੇ ਦੇ ਸਿਧਾਂਤ

This major revision has been developed with several key principles in mind:

ਇਹ ਵੱਡਾ ਸੋਧ ਕਈ ਮੁੱਖ ਸਿਧਾਂਤਾਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖ ਕੇ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ:

* Refined Scope and Focus: This version of the standard has been designed to align more directly with the foundational pillars in its name: Application, Security, Verification, and Standard. Requirements have been rewritten to emphasize the prevention of security flaws rather than mandating specific technical implementations. Requirement texts are intended to be self-explanatory, explaining why they exist.

* ਸੁਧਰਿਆ ਘੇਰਾ ਅਤੇ ਧਿਆਨ (Refined Scope and Focus): ਮਿਆਰ ਦੇ ਇਸ ਸੰਸਕਰਣ ਨੂੰ ਇਸ ਦੇ ਨਾਮ ਦੇ ਬੁਨਿਆਦੀ ਥੰਮ੍ਹਾਂ — ਐਪਲੀਕੇਸ਼ਨ (Application), ਸੁਰੱਖਿਆ (Security), ਤਸਦੀਕ (Verification), ਅਤੇ ਮਿਆਰ (Standard) — ਨਾਲ ਵਧੇਰੇ ਸਿੱਧੇ ਤੌਰ 'ਤੇ ਮੇਲ ਖਾਣ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ. ਲੋੜਾਂ ਨੂੰ ਖ਼ਾਸ ਤਕਨੀਕੀ ਅਮਲ ਲਾਜ਼ਮੀ ਕਰਨ ਦੀ ਬਜਾਏ ਸੁਰੱਖਿਆ ਕਮੀਆਂ ਦੀ ਰੋਕਥਾਮ 'ਤੇ ਜ਼ੋਰ ਦੇਣ ਲਈ ਦੁਬਾਰਾ ਲਿਖੀਆਂ ਗਈਆਂ ਹਨ. ਲੋੜ ਦੇ ਪਾਠ ਸਵੈ-ਵਿਆਖਿਆਤਮਕ ਹੋਣ ਦੇ ਇਰਾਦੇ ਨਾਲ ਲਿਖੇ ਗਏ ਹਨ, ਜੋ ਦੱਸਦੇ ਹਨ ਕਿ ਉਹ ਕਿਉਂ ਮੌਜੂਦ ਹਨ.

* Support for Documented Security Decisions: ASVS 5.0 introduces requirements for documenting key security decisions. This enhances traceability and supports context-sensitive implementations, allowing organizations to tailor their security posture to their specific needs and risks.

* ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਲਈ ਸਹਾਇਤਾ (Support for Documented Security Decisions): ASVS ੫.੦ ਮੁੱਖ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਦੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲਈ ਲੋੜਾਂ ਪੇਸ਼ ਕਰਦਾ ਹੈ. ਇਹ ਟਰੇਸੇਬਿਲਟੀ ਵਧਾਉਂਦਾ ਹੈ ਅਤੇ ਸੰਦਰਭ-ਸੰਵੇਦਨਸ਼ੀਲ ਅਮਲਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਸੰਸਥਾਵਾਂ ਆਪਣੀ ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਨੂੰ ਆਪਣੀਆਂ ਖ਼ਾਸ ਲੋੜਾਂ ਅਤੇ ਖ਼ਤਰਿਆਂ ਅਨੁਸਾਰ ਢਾਲ ਸਕਦੀਆਂ ਹਨ.

* Updated Levels: While ASVS retains its three-tier model, the level definitions have evolved to make the ASVS easier to adopt. Level 1 is designed as the initial step to adopting the ASVS, providing the first layer of defense. Level 2 represents a comprehensive view of standard security practices, and Level 3 addresses advanced, high-assurance requirements.

* ਅੱਪਡੇਟ ਕੀਤੇ ਪੱਧਰ (Updated Levels): ਜਦੋਂ ਕਿ ASVS ਆਪਣਾ ਤਿੰਨ-ਪੱਧਰੀ ਮਾਡਲ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ, ਪੱਧਰ ਦੀਆਂ ਪਰਿਭਾਸ਼ਾਵਾਂ ASVS ਨੂੰ ਅਪਣਾਉਣਾ ਆਸਾਨ ਬਣਾਉਣ ਲਈ ਵਿਕਸਿਤ ਹੋਈਆਂ ਹਨ. ਪੱਧਰ ੧ (Level 1) ASVS ਅਪਣਾਉਣ ਦੇ ਸ਼ੁਰੂਆਤੀ ਕਦਮ ਵਜੋਂ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ, ਜੋ ਸੁਰੱਖਿਆ ਦੀ ਪਹਿਲੀ ਪਰਤ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ. ਪੱਧਰ ੨ (Level 2) ਮਿਆਰੀ ਸੁਰੱਖਿਆ ਅਭਿਆਸਾਂ ਦੀ ਵਿਆਪਕ ਦ੍ਰਿਸ਼ਟੀ ਪੇਸ਼ ਕਰਦਾ ਹੈ, ਅਤੇ ਪੱਧਰ ੩ (Level 3) ਉੱਨਤ, ਉੱਚ-ਭਰੋਸੇ ਵਾਲੀਆਂ ਲੋੜਾਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਦਾ ਹੈ.

* Restructured and Expanded Content: ASVS 5.0 includes approximately 350 requirements across 17 chapters. Chapters have been reorganized for clarity and usability. A two-way mapping between v4.0 and v5.0 is provided to facilitate migration.

* ਪੁਨਰਗਠਿਤ ਅਤੇ ਵਿਸਤਾਰਿਤ ਸਮੱਗਰੀ (Restructured and Expanded Content): ASVS ੫.੦ ਵਿੱਚ ੧੭ ਅਧਿਆਵਾਂ ਵਿੱਚ ਲਗਭਗ ੩੫੦ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ. ਅਧਿਆਵਾਂ ਨੂੰ ਸਪੱਸ਼ਟਤਾ ਅਤੇ ਵਰਤੋਂਯੋਗਤਾ ਲਈ ਪੁਨਰਗਠਿਤ ਕੀਤਾ ਗਿਆ ਹੈ. ਮਾਈਗ੍ਰੇਸ਼ਨ ਦੀ ਸਹੂਲਤ ਲਈ v੪.੦ ਅਤੇ v੫.੦ ਵਿਚਕਾਰ ਦੋ-ਤਰਫ਼ੀ ਮੈਪਿੰਗ ਪ੍ਰਦਾਨ ਕੀਤੀ ਗਈ ਹੈ.

## Looking ahead
## ਅੱਗੇ ਵੇਖਦਿਆਂ

Just as securing an application is never truly finished, neither is the ASVS. Although Version 5.0 is a major release, development continues. This release allows the wider community to benefit from the improvements and additions which have been accumulated but also lays the groundwork for future enhancements. This could include community-driven efforts to create implementation and verification guidance built on top of the core requirement set.

ਜਿਵੇਂ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨਾ ਕਦੇ ਸੱਚਮੁੱਚ ਮੁਕੰਮਲ ਨਹੀਂ ਹੁੰਦਾ, ਉਵੇਂ ASVS ਵੀ ਨਹੀਂ. ਹਾਲਾਂਕਿ ਸੰਸਕਰਣ ੫.੦ ਇੱਕ ਵੱਡੀ ਰਿਲੀਜ਼ ਹੈ, ਵਿਕਾਸ ਜਾਰੀ ਹੈ. ਇਹ ਰਿਲੀਜ਼ ਵਿਸ਼ਾਲ ਭਾਈਚਾਰੇ ਨੂੰ ਇਕੱਤਰ ਕੀਤੀਆਂ ਸੁਧਾਰਾਂ ਅਤੇ ਵਾਧਿਆਂ ਤੋਂ ਲਾਭ ਲੈਣ ਦਿੰਦੀ ਹੈ ਅਤੇ ਭਵਿੱਖ ਦੀਆਂ ਤਰੱਕੀਆਂ ਲਈ ਨੀਂਹ ਵੀ ਰੱਖਦੀ ਹੈ. ਇਸ ਵਿੱਚ ਮੁੱਖ ਲੋੜ ਸੈੱਟ ਦੇ ਉੱਪਰ ਬਣਾਈ ਗਈ ਅਮਲ ਅਤੇ ਤਸਦੀਕ ਮਾਰਗਦਰਸ਼ਨ ਬਣਾਉਣ ਲਈ ਭਾਈਚਾਰਕ ਯਤਨ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ.

ASVS 5.0 is designed to serve as a reliable foundation for secure software development. The community is invited to adopt, contribute, and build upon this standard to collectively advance the state of application security.

ASVS ੫.੦ ਸੁਰੱਖਿਅਤ ਸਾਫ਼ਟਵੇਅਰ ਵਿਕਾਸ ਲਈ ਇੱਕ ਭਰੋਸੇਯੋਗ ਨੀਂਹ ਵਜੋਂ ਕੰਮ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ. ਭਾਈਚਾਰੇ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਦੀ ਸਥਿਤੀ ਨੂੰ ਸਮੂਹਿਕ ਤੌਰ 'ਤੇ ਅੱਗੇ ਵਧਾਉਣ ਲਈ ਇਸ ਮਿਆਰ ਨੂੰ ਅਪਣਾਉਣ, ਯੋਗਦਾਨ ਪਾਉਣ ਅਤੇ ਇਸ 'ਤੇ ਨਿਰਮਾਣ ਕਰਨ ਦਾ ਸੱਦਾ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ.
