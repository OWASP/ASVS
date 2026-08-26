<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x26-V17-WebRTC.md -->
<!-- Translator: GeeksikhSecurity -->

# V17 WebRTC
# V17 WebRTC (ਵੈੱਬਆਰਟੀਸੀ)

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Web Real-Time Communication (WebRTC) enables real-time voice, video, and data exchange in modern applications. As adoption increases, securing WebRTC infrastructure becomes critical. This section provides security requirements for stakeholders who develop, host, or integrate WebRTC systems.

Web Real-Time Communication (WebRTC) ਆਧੁਨਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਰੀਅਲ-ਟਾਈਮ ਆਵਾਜ਼, ਵੀਡੀਓ, ਅਤੇ ਡਾਟਾ ਅਦਾਨ-ਪ੍ਰਦਾਨ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ। ਜਿਵੇਂ-ਜਿਵੇਂ ਇਸ ਨੂੰ ਅਪਣਾਉਣਾ ਵਧਦਾ ਹੈ, WebRTC ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨਾ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਹੋ ਜਾਂਦਾ ਹੈ। ਇਹ ਭਾਗ ਉਹਨਾਂ ਹਿੱਸੇਦਾਰਾਂ (stakeholders) ਲਈ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ WebRTC ਸਿਸਟਮਾਂ ਨੂੰ ਵਿਕਸਿਤ ਕਰਦੇ, ਹੋਸਟ ਕਰਦੇ, ਜਾਂ ਏਕੀਕ੍ਰਿਤ ਕਰਦੇ ਹਨ।

The WebRTC market can be broadly categorized into three segments:

WebRTC ਬਾਜ਼ਾਰ ਨੂੰ ਮੋਟੇ ਤੌਰ 'ਤੇ ਤਿੰਨ ਵਰਗਾਂ ਵਿੱਚ ਵੰਡਿਆ ਜਾ ਸਕਦਾ ਹੈ:

1. Product Developers: Proprietary and open-source vendors that create and supply WebRTC products and solutions. Their focus is on developing robust and secure WebRTC technologies that can be used by others.

2. Communication Platforms as a Service (CPaaS): Providers that offer APIs, SDKs, and the necessary infrastructure or platforms to enable WebRTC functionalities. CPaaS providers may use products from the first category or develop their own WebRTC software to offer these services.

3. Service Providers: Organizations that leverage products from product developers or CPaaS providers, or develop their own WebRTC solutions. They create and implement applications for online conferencing, healthcare, e-learning, and other domains where real-time communication is crucial.

1. ਉਤਪਾਦ ਵਿਕਾਸਕਾਰ (Product Developers): ਮਾਲਕੀ (proprietary) ਅਤੇ ਓਪਨ-ਸੋਰਸ ਵਿਕਰੇਤਾ ਜੋ WebRTC ਉਤਪਾਦ ਅਤੇ ਹੱਲ ਬਣਾਉਂਦੇ ਅਤੇ ਸਪਲਾਈ ਕਰਦੇ ਹਨ। ਉਹਨਾਂ ਦਾ ਧਿਆਨ ਮਜ਼ਬੂਤ ਅਤੇ ਸੁਰੱਖਿਅਤ WebRTC ਤਕਨਾਲੋਜੀਆਂ ਵਿਕਸਿਤ ਕਰਨ 'ਤੇ ਹੁੰਦਾ ਹੈ ਜੋ ਦੂਜਿਆਂ ਦੁਆਰਾ ਵਰਤੀਆਂ ਜਾ ਸਕਣ।

2. ਸੇਵਾ ਵਜੋਂ ਸੰਚਾਰ ਪਲੇਟਫ਼ਾਰਮ (Communication Platforms as a Service, CPaaS): ਉਹ ਪ੍ਰਦਾਤਾ ਜੋ WebRTC ਕਾਰਜਸਮਰੱਥਾਵਾਂ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਣ ਲਈ API, SDK, ਅਤੇ ਲੋੜੀਂਦਾ ਬੁਨਿਆਦੀ ਢਾਂਚਾ ਜਾਂ ਪਲੇਟਫ਼ਾਰਮ ਪੇਸ਼ ਕਰਦੇ ਹਨ। CPaaS ਪ੍ਰਦਾਤਾ ਇਹ ਸੇਵਾਵਾਂ ਪੇਸ਼ ਕਰਨ ਲਈ ਪਹਿਲੇ ਵਰਗ ਦੇ ਉਤਪਾਦ ਵਰਤ ਸਕਦੇ ਹਨ ਜਾਂ ਆਪਣਾ WebRTC ਸਾਫ਼ਟਵੇਅਰ ਵਿਕਸਿਤ ਕਰ ਸਕਦੇ ਹਨ।

3. ਸੇਵਾ ਪ੍ਰਦਾਤਾ (Service Providers): ਉਹ ਸੰਸਥਾਵਾਂ ਜੋ ਉਤਪਾਦ ਵਿਕਾਸਕਾਰਾਂ ਜਾਂ CPaaS ਪ੍ਰਦਾਤਾਵਾਂ ਦੇ ਉਤਪਾਦਾਂ ਦਾ ਲਾਭ ਉਠਾਉਂਦੀਆਂ ਹਨ, ਜਾਂ ਆਪਣੇ WebRTC ਹੱਲ ਵਿਕਸਿਤ ਕਰਦੀਆਂ ਹਨ। ਉਹ ਔਨਲਾਈਨ ਕਾਨਫ਼ਰੰਸਿੰਗ, ਸਿਹਤ-ਸੰਭਾਲ, ਈ-ਲਰਨਿੰਗ, ਅਤੇ ਹੋਰ ਖੇਤਰਾਂ ਲਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਂਦੀਆਂ ਅਤੇ ਲਾਗੂ ਕਰਦੀਆਂ ਹਨ ਜਿੱਥੇ ਰੀਅਲ-ਟਾਈਮ ਸੰਚਾਰ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਹੈ।

The security requirements outlined here are primarily focused on Product Developers, CPaaS, and Service Providers who:

ਇੱਥੇ ਦਿੱਤੀਆਂ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਮੁੱਖ ਤੌਰ 'ਤੇ ਉਹਨਾਂ ਉਤਪਾਦ ਵਿਕਾਸਕਾਰਾਂ, CPaaS, ਅਤੇ ਸੇਵਾ ਪ੍ਰਦਾਤਾਵਾਂ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਹਨ ਜੋ:

* Utilize open-source solutions to build their WebRTC applications.
* Use commercial WebRTC products as part of their infrastructure.
* Use internally developed WebRTC solutions or integrate various components into a cohesive service offering.

* ਆਪਣੀਆਂ WebRTC ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣ ਲਈ ਓਪਨ-ਸੋਰਸ ਹੱਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ।
* ਆਪਣੇ ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦੇ ਹਿੱਸੇ ਵਜੋਂ ਵਪਾਰਕ WebRTC ਉਤਪਾਦਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ।
* ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਵਿਕਸਿਤ WebRTC ਹੱਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਜਾਂ ਵੱਖ-ਵੱਖ ਹਿੱਸਿਆਂ ਨੂੰ ਇੱਕ ਇਕਜੁੱਟ ਸੇਵਾ ਪੇਸ਼ਕਸ਼ ਵਿੱਚ ਏਕੀਕ੍ਰਿਤ ਕਰਦੇ ਹਨ।

It is important to note that these security requirements do not apply to developers who exclusively use SDKs and APIs provided by CPaaS vendors. For such developers, the CPaaS providers are typically responsible for most of the underlying security concerns within their platforms, and a generic security standard like ASVS may not fully address their needs.

ਇਹ ਨੋਟ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਇਹ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਉਹਨਾਂ ਵਿਕਾਸਕਾਰਾਂ 'ਤੇ ਲਾਗੂ ਨਹੀਂ ਹੁੰਦੀਆਂ ਜੋ ਸਿਰਫ਼ CPaaS ਵਿਕਰੇਤਾਵਾਂ ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੇ SDK ਅਤੇ API ਦੀ ਹੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ। ਅਜਿਹੇ ਵਿਕਾਸਕਾਰਾਂ ਲਈ, CPaaS ਪ੍ਰਦਾਤਾ ਆਮ ਤੌਰ 'ਤੇ ਆਪਣੇ ਪਲੇਟਫ਼ਾਰਮਾਂ ਦੇ ਅੰਦਰ ਜ਼ਿਆਦਾਤਰ ਅੰਤਰੀਵ ਸੁਰੱਖਿਆ ਚਿੰਤਾਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੁੰਦੇ ਹਨ, ਅਤੇ ASVS ਵਰਗਾ ਇੱਕ ਆਮ ਸੁਰੱਖਿਆ ਮਿਆਰ ਸ਼ਾਇਦ ਉਹਨਾਂ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸੰਬੋਧਿਤ ਨਾ ਕਰੇ।

## V17.1 TURN Server
## V17.1 TURN ਸਰਵਰ

This section defines security requirements for systems that operate their own TURN (Traversal Using Relays around NAT) servers. TURN servers assist in relaying media in restrictive network environments but can pose risks if misconfigured. These controls focus on secure address filtering and protection against resource exhaustion.

ਇਹ ਭਾਗ ਉਹਨਾਂ ਸਿਸਟਮਾਂ ਲਈ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਆਪਣੇ TURN (Traversal Using Relays around NAT) ਸਰਵਰ ਚਲਾਉਂਦੇ ਹਨ। TURN ਸਰਵਰ ਪਾਬੰਦੀਸ਼ੁਦਾ ਨੈੱਟਵਰਕ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਮੀਡੀਆ ਨੂੰ ਰੀਲੇਅ (relay) ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ ਪਰ ਗ਼ਲਤ ਸੰਰਚਨਾ ਹੋਣ 'ਤੇ ਜੋਖਮ ਪੈਦਾ ਕਰ ਸਕਦੇ ਹਨ। ਇਹ ਨਿਯੰਤਰਣ ਸੁਰੱਖਿਅਤ ਪਤਾ ਫ਼ਿਲਟਰਿੰਗ ਅਤੇ ਸਰੋਤ ਖ਼ਤਮ ਹੋ ਜਾਣ (resource exhaustion) ਤੋਂ ਸੁਰੱਖਿਆ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **17.1.1** | Verify that the Traversal Using Relays around NAT (TURN) service only allows access to IP addresses that are not reserved for special purposes (e.g., internal networks, broadcast, loopback). Note that this applies to both IPv4 and IPv6 addresses. | 2 |
| **17.1.2** | Verify that the Traversal Using Relays around NAT (TURN) service is not susceptible to resource exhaustion when legitimate users attempt to open a large number of ports on the TURN server. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **17.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ Traversal Using Relays around NAT (TURN) ਸੇਵਾ ਸਿਰਫ਼ ਉਹਨਾਂ IP ਪਤਿਆਂ ਤੱਕ ਪਹੁੰਚ ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦੀ ਹੈ ਜੋ ਵਿਸ਼ੇਸ਼ ਉਦੇਸ਼ਾਂ (ਜਿਵੇਂ ਕਿ ਅੰਦਰੂਨੀ ਨੈੱਟਵਰਕ, ਬ੍ਰੌਡਕਾਸਟ, ਲੂਪਬੈਕ) ਲਈ ਰਾਖਵੇਂ ਨਹੀਂ ਹਨ। ਧਿਆਨ ਦਿਓ ਕਿ ਇਹ IPv4 ਅਤੇ IPv6 ਦੋਵਾਂ ਪਤਿਆਂ 'ਤੇ ਲਾਗੂ ਹੁੰਦਾ ਹੈ। | 2 |
| **17.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ Traversal Using Relays around NAT (TURN) ਸੇਵਾ ਉਦੋਂ ਸਰੋਤ ਖ਼ਤਮ ਹੋ ਜਾਣ ਦੀ ਸ਼ਿਕਾਰ ਨਹੀਂ ਹੁੰਦੀ ਜਦੋਂ ਜਾਇਜ਼ ਉਪਭੋਗਤਾ TURN ਸਰਵਰ 'ਤੇ ਵੱਡੀ ਗਿਣਤੀ ਵਿੱਚ ਪੋਰਟ ਖੋਲ੍ਹਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਨ। | 3 |

## V17.2 Media
## V17.2 ਮੀਡੀਆ

These requirements only apply to systems that host their own WebRTC media servers, such as Selective Forwarding Units (SFUs), Multipoint Control Units (MCUs), recording servers, or gateway servers. Media servers handle and distribute media streams, making their security critical to protect communication between peers. Safeguarding media streams is paramount in WebRTC applications to prevent eavesdropping, tampering, and denial-of-service attacks that could compromise user privacy and communication quality.

ਇਹ ਲੋੜਾਂ ਸਿਰਫ਼ ਉਹਨਾਂ ਸਿਸਟਮਾਂ 'ਤੇ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ ਜੋ ਆਪਣੇ WebRTC ਮੀਡੀਆ ਸਰਵਰ ਹੋਸਟ ਕਰਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ Selective Forwarding Units (SFU), Multipoint Control Units (MCU), ਰਿਕਾਰਡਿੰਗ ਸਰਵਰ, ਜਾਂ ਗੇਟਵੇ ਸਰਵਰ। ਮੀਡੀਆ ਸਰਵਰ ਮੀਡੀਆ ਸਟ੍ਰੀਮਾਂ (media streams) ਨੂੰ ਸੰਭਾਲਦੇ ਅਤੇ ਵੰਡਦੇ ਹਨ, ਜਿਸ ਕਰਕੇ ਪੀਅਰਾਂ (peers) ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ ਦੀ ਰਾਖੀ ਲਈ ਉਹਨਾਂ ਦੀ ਸੁਰੱਖਿਆ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਹੋ ਜਾਂਦੀ ਹੈ। WebRTC ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਮੀਡੀਆ ਸਟ੍ਰੀਮਾਂ ਦੀ ਰਾਖੀ ਕਰਨਾ ਸਭ ਤੋਂ ਵੱਧ ਮਹੱਤਵਪੂਰਨ ਹੈ ਤਾਂ ਜੋ ਗੁਪਤ ਤੌਰ 'ਤੇ ਸੁਣਨ (eavesdropping), ਛੇੜਛਾੜ, ਅਤੇ ਸੇਵਾ-ਇਨਕਾਰ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ ਜੋ ਉਪਭੋਗਤਾ ਦੀ ਨਿੱਜਤਾ ਅਤੇ ਸੰਚਾਰ ਗੁਣਵੱਤਾ ਨਾਲ ਸਮਝੌਤਾ ਕਰ ਸਕਦੇ ਹਨ।

In particular, it is necessary to implement protections against flood attacks such as rate limiting, validating timestamps, using synchronized clocks to match real-time intervals, and managing buffers to prevent overflow and maintain proper timing. If packets for a particular media session arrive too quickly, excess packets should be dropped. It is also important to protect the system from malformed packets by implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques.

ਖ਼ਾਸ ਤੌਰ 'ਤੇ, ਹੜ੍ਹ (flood) ਹਮਲਿਆਂ ਦੇ ਵਿਰੁੱਧ ਸੁਰੱਖਿਆਵਾਂ ਲਾਗੂ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਦਰ ਸੀਮਾ (rate limiting), ਟਾਈਮਸਟੈਂਪਾਂ ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ, ਰੀਅਲ-ਟਾਈਮ ਅੰਤਰਾਲਾਂ ਨਾਲ ਮੇਲ ਕਰਨ ਲਈ ਸਮਕਾਲੀ (synchronized) ਘੜੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ, ਅਤੇ ਓਵਰਫ਼ਲੋ ਨੂੰ ਰੋਕਣ ਅਤੇ ਸਹੀ ਸਮਾਂ-ਮੇਲ ਬਣਾਈ ਰੱਖਣ ਲਈ ਬਫ਼ਰਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ। ਜੇ ਕਿਸੇ ਖ਼ਾਸ ਮੀਡੀਆ ਸੈਸ਼ਨ ਲਈ ਪੈਕੇਟ ਬਹੁਤ ਤੇਜ਼ੀ ਨਾਲ ਪਹੁੰਚਦੇ ਹਨ, ਤਾਂ ਵਾਧੂ ਪੈਕੇਟ ਰੱਦ ਕਰ ਦਿੱਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ। ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ (input validation) ਲਾਗੂ ਕਰਕੇ, ਇੰਟੀਜਰ ਓਵਰਫ਼ਲੋ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸੰਭਾਲ ਕੇ, ਬਫ਼ਰ ਓਵਰਫ਼ਲੋ ਨੂੰ ਰੋਕ ਕੇ, ਅਤੇ ਹੋਰ ਮਜ਼ਬੂਤ ਗਲਤੀ ਪ੍ਰਬੰਧਨ ਤਕਨੀਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਿਸਟਮ ਨੂੰ ਵਿਗੜੇ ਹੋਏ (malformed) ਪੈਕੇਟਾਂ ਤੋਂ ਸੁਰੱਖਿਅਤ ਰੱਖਣਾ ਵੀ ਮਹੱਤਵਪੂਰਨ ਹੈ।

Systems that rely solely on peer-to-peer media communication between web browsers, without the involvement of intermediate media servers, are excluded from these specific media-related security requirements.

ਉਹ ਸਿਸਟਮ ਜੋ ਵਿਚਕਾਰਲੇ ਮੀਡੀਆ ਸਰਵਰਾਂ ਦੀ ਸ਼ਮੂਲੀਅਤ ਤੋਂ ਬਿਨਾਂ, ਸਿਰਫ਼ ਵੈੱਬ ਬ੍ਰਾਊਜ਼ਰਾਂ ਦੇ ਵਿਚਕਾਰ ਪੀਅਰ-ਤੋਂ-ਪੀਅਰ ਮੀਡੀਆ ਸੰਚਾਰ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ, ਇਹਨਾਂ ਖ਼ਾਸ ਮੀਡੀਆ-ਸੰਬੰਧੀ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਤੋਂ ਬਾਹਰ ਰੱਖੇ ਗਏ ਹਨ।

This section refers to the use of Datagram Transport Layer Security (DTLS) in the context of WebRTC. A requirement related to having a documented policy for the management of cryptographic keys can be found in the "Cryptography" chapter. Information on approved cryptographic methods can be found either in the Cryptography Appendix of the ASVS or in documents such as NIST SP 800‑52 Rev. 2 or BSI TR‑02102‑2 (Version 2025‑01).

ਇਹ ਭਾਗ WebRTC ਦੇ ਸੰਦਰਭ ਵਿੱਚ Datagram Transport Layer Security (DTLS) ਦੀ ਵਰਤੋਂ ਦਾ ਹਵਾਲਾ ਦਿੰਦਾ ਹੈ। ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀਆਂ ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ ਦਸਤਾਵੇਜ਼ੀ ਨੀਤੀ ਰੱਖਣ ਨਾਲ ਸੰਬੰਧਿਤ ਇੱਕ ਲੋੜ "ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ" (Cryptography) ਅਧਿਆਇ ਵਿੱਚ ਮਿਲ ਸਕਦੀ ਹੈ। ਪ੍ਰਵਾਨਿਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਵਿਧੀਆਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਜਾਂ ਤਾਂ ASVS ਦੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਅੰਤਿਕਾ ਵਿੱਚ ਜਾਂ NIST SP 800‑52 Rev. 2 ਜਾਂ BSI TR‑02102‑2 (Version 2025‑01) ਵਰਗੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਮਿਲ ਸਕਦੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **17.2.1** | Verify that the key for the Datagram Transport Layer Security (DTLS) certificate is managed and protected based on the documented policy for management of cryptographic keys. | 2 |
| **17.2.2** | Verify that the media server is configured to use and support approved Datagram Transport Layer Security (DTLS) cipher suites and a secure protection profile for the DTLS Extension for establishing keys for the Secure Real-time Transport Protocol (DTLS-SRTP). | 2 |
| **17.2.3** | Verify that Secure Real-time Transport Protocol (SRTP) authentication is checked at the media server to prevent Real-time Transport Protocol (RTP) injection attacks from leading to either a Denial of Service condition or audio or video media insertion into media streams. | 2 |
| **17.2.4** | Verify that the media server is able to continue processing incoming media traffic when encountering malformed Secure Real-time Transport Protocol (SRTP) packets. | 2 |
| **17.2.5** | Verify that the media server is able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users. | 3 |
| **17.2.6** | Verify that the media server is not susceptible to the "ClientHello" Race Condition vulnerability in Datagram Transport Layer Security (DTLS) by checking if the media server is publicly known to be vulnerable or by performing the race condition test. | 3 |
| **17.2.7** | Verify that any audio or video recording mechanisms associated with the media server are able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users. | 3 |
| **17.2.8** | Verify that the Datagram Transport Layer Security (DTLS) certificate is checked against the Session Description Protocol (SDP) fingerprint attribute, terminating the media stream if the check fails, to ensure the authenticity of the media stream. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **17.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ Datagram Transport Layer Security (DTLS) ਸਰਟੀਫ਼ਿਕੇਟ ਦੀ ਕੁੰਜੀ ਦਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਸੁਰੱਖਿਆ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀਆਂ ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ ਦਸਤਾਵੇਜ਼ੀ ਨੀਤੀ ਦੇ ਆਧਾਰ 'ਤੇ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |
| **17.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਮੀਡੀਆ ਸਰਵਰ ਨੂੰ ਪ੍ਰਵਾਨਿਤ Datagram Transport Layer Security (DTLS) ਸਾਈਫ਼ਰ ਸੂਟਾਂ ਅਤੇ Secure Real-time Transport Protocol ਲਈ ਕੁੰਜੀਆਂ ਸਥਾਪਿਤ ਕਰਨ ਵਾਸਤੇ DTLS Extension (DTLS-SRTP) ਲਈ ਇੱਕ ਸੁਰੱਖਿਅਤ ਪ੍ਰੋਟੈਕਸ਼ਨ ਪ੍ਰੋਫ਼ਾਈਲ (protection profile) ਦੀ ਵਰਤੋਂ ਅਤੇ ਸਮਰਥਨ ਕਰਨ ਲਈ ਸੰਰਚਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। | 2 |
| **17.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ Secure Real-time Transport Protocol (SRTP) ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਜਾਂਚ ਮੀਡੀਆ ਸਰਵਰ 'ਤੇ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਤਾਂ ਜੋ Real-time Transport Protocol (RTP) ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਜਾਂ ਤਾਂ ਸੇਵਾ-ਇਨਕਾਰ ਸਥਿਤੀ ਜਾਂ ਮੀਡੀਆ ਸਟ੍ਰੀਮਾਂ ਵਿੱਚ ਆਡੀਓ ਜਾਂ ਵੀਡੀਓ ਮੀਡੀਆ ਪਾਏ ਜਾਣ ਵੱਲ ਲੈ ਜਾਣ ਤੋਂ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 2 |
| **17.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਮੀਡੀਆ ਸਰਵਰ ਵਿਗੜੇ ਹੋਏ Secure Real-time Transport Protocol (SRTP) ਪੈਕੇਟਾਂ ਦਾ ਸਾਹਮਣਾ ਕਰਨ 'ਤੇ ਆਉਣ ਵਾਲੇ ਮੀਡੀਆ ਟ੍ਰੈਫ਼ਿਕ ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖਣ ਦੇ ਸਮਰੱਥ ਹੈ। | 2 |
| **17.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਮੀਡੀਆ ਸਰਵਰ ਜਾਇਜ਼ ਉਪਭੋਗਤਾਵਾਂ ਵੱਲੋਂ Secure Real-time Transport Protocol (SRTP) ਪੈਕੇਟਾਂ ਦੇ ਹੜ੍ਹ ਦੌਰਾਨ ਆਉਣ ਵਾਲੇ ਮੀਡੀਆ ਟ੍ਰੈਫ਼ਿਕ ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖਣ ਦੇ ਸਮਰੱਥ ਹੈ। | 3 |
| **17.2.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਮੀਡੀਆ ਸਰਵਰ Datagram Transport Layer Security (DTLS) ਵਿੱਚ "ClientHello" ਰੇਸ ਕੰਡੀਸ਼ਨ (race condition) ਕਮਜ਼ੋਰੀ ਦਾ ਸ਼ਿਕਾਰ ਨਹੀਂ ਹੈ, ਇਹ ਜਾਂਚ ਕੇ ਕਿ ਕੀ ਮੀਡੀਆ ਸਰਵਰ ਜਨਤਕ ਤੌਰ 'ਤੇ ਕਮਜ਼ੋਰ ਵਜੋਂ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ ਜਾਂ ਰੇਸ ਕੰਡੀਸ਼ਨ ਟੈਸਟ ਕਰਕੇ। | 3 |
| **17.2.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਮੀਡੀਆ ਸਰਵਰ ਨਾਲ ਜੁੜੀਆਂ ਕੋਈ ਵੀ ਆਡੀਓ ਜਾਂ ਵੀਡੀਓ ਰਿਕਾਰਡਿੰਗ ਪ੍ਰਣਾਲੀਆਂ ਜਾਇਜ਼ ਉਪਭੋਗਤਾਵਾਂ ਵੱਲੋਂ Secure Real-time Transport Protocol (SRTP) ਪੈਕੇਟਾਂ ਦੇ ਹੜ੍ਹ ਦੌਰਾਨ ਆਉਣ ਵਾਲੇ ਮੀਡੀਆ ਟ੍ਰੈਫ਼ਿਕ ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖਣ ਦੇ ਸਮਰੱਥ ਹਨ। | 3 |
| **17.2.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ Datagram Transport Layer Security (DTLS) ਸਰਟੀਫ਼ਿਕੇਟ ਦੀ ਜਾਂਚ Session Description Protocol (SDP) fingerprint ਗੁਣ ਦੇ ਵਿਰੁੱਧ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ ਜਾਂਚ ਅਸਫਲ ਹੋਣ 'ਤੇ ਮੀਡੀਆ ਸਟ੍ਰੀਮ ਨੂੰ ਖ਼ਤਮ ਕਰ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਜੋ ਮੀਡੀਆ ਸਟ੍ਰੀਮ ਦੀ ਪ੍ਰਮਾਣਿਕਤਾ (authenticity) ਯਕੀਨੀ ਬਣਾਈ ਜਾ ਸਕੇ। | 3 |

## V17.3 Signaling
## V17.3 ਸਿਗਨਲਿੰਗ

This section defines requirements for systems that operate their own WebRTC signaling servers. Signaling coordinates peer-to-peer communication and must be resilient against attacks that could disrupt session establishment or control.

ਇਹ ਭਾਗ ਉਹਨਾਂ ਸਿਸਟਮਾਂ ਲਈ ਲੋੜਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਆਪਣੇ WebRTC ਸਿਗਨਲਿੰਗ (signaling) ਸਰਵਰ ਚਲਾਉਂਦੇ ਹਨ। ਸਿਗਨਲਿੰਗ ਪੀਅਰ-ਤੋਂ-ਪੀਅਰ ਸੰਚਾਰ ਦਾ ਤਾਲਮੇਲ ਕਰਦੀ ਹੈ ਅਤੇ ਇਸ ਦਾ ਉਹਨਾਂ ਹਮਲਿਆਂ ਦੇ ਵਿਰੁੱਧ ਲਚਕੀਲਾ (resilient) ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ ਜੋ ਸੈਸ਼ਨ ਸਥਾਪਨਾ ਜਾਂ ਨਿਯੰਤਰਣ ਵਿੱਚ ਵਿਘਨ ਪਾ ਸਕਦੇ ਹਨ।

To ensure secure signaling, systems must handle malformed inputs gracefully and remain available under load.

ਸੁਰੱਖਿਅਤ ਸਿਗਨਲਿੰਗ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ, ਸਿਸਟਮਾਂ ਲਈ ਵਿਗੜੇ ਹੋਏ ਇਨਪੁੱਟਾਂ ਨੂੰ ਸੁਚੱਜੇ ਢੰਗ ਨਾਲ ਸੰਭਾਲਣਾ ਅਤੇ ਲੋਡ ਹੇਠ ਉਪਲਬਧ ਰਹਿਣਾ ਲਾਜ਼ਮੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **17.3.1** | Verify that the signaling server is able to continue processing legitimate incoming signaling messages during a flood attack. This should be achieved by implementing rate limiting at the signaling level. | 2 |
| **17.3.2** | Verify that the signaling server is able to continue processing legitimate signaling messages when encountering malformed signaling message that could cause a denial of service condition. This could include implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **17.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਗਨਲਿੰਗ ਸਰਵਰ ਹੜ੍ਹ ਹਮਲੇ ਦੌਰਾਨ ਜਾਇਜ਼ ਆਉਣ ਵਾਲੇ ਸਿਗਨਲਿੰਗ ਸੁਨੇਹਿਆਂ ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖਣ ਦੇ ਸਮਰੱਥ ਹੈ। ਇਹ ਸਿਗਨਲਿੰਗ ਪੱਧਰ 'ਤੇ ਦਰ ਸੀਮਾ ਲਾਗੂ ਕਰਕੇ ਹਾਸਲ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। | 2 |
| **17.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਗਨਲਿੰਗ ਸਰਵਰ ਅਜਿਹੇ ਵਿਗੜੇ ਹੋਏ ਸਿਗਨਲਿੰਗ ਸੁਨੇਹੇ ਦਾ ਸਾਹਮਣਾ ਕਰਨ 'ਤੇ, ਜੋ ਸੇਵਾ-ਇਨਕਾਰ ਸਥਿਤੀ ਪੈਦਾ ਕਰ ਸਕਦਾ ਹੈ, ਜਾਇਜ਼ ਸਿਗਨਲਿੰਗ ਸੁਨੇਹਿਆਂ ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖਣ ਦੇ ਸਮਰੱਥ ਹੈ। ਇਸ ਵਿੱਚ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਲਾਗੂ ਕਰਨਾ, ਇੰਟੀਜਰ ਓਵਰਫ਼ਲੋ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸੰਭਾਲਣਾ, ਬਫ਼ਰ ਓਵਰਫ਼ਲੋ ਨੂੰ ਰੋਕਣਾ, ਅਤੇ ਹੋਰ ਮਜ਼ਬੂਤ ਗਲਤੀ ਪ੍ਰਬੰਧਨ ਤਕਨੀਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਸ਼ਾਮਲ ਹੋ ਸਕਦਾ ਹੈ। | 2 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* The WebRTC DTLS ClientHello DoS is best documented at [Enable Security's blog post aimed at security professionals](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) and the associated [white paper aimed at WebRTC developers](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
