// TODO: 내용 숙지

# V17 WebRTC

## Control Objective

Web Real-Time Communication (WebRTC) enables real-time voice, video, and data exchange in modern applications. As adoption increases, securing WebRTC infrastructure becomes critical. This section provides security requirements for stakeholders who develop, host, or integrate WebRTC systems.

The WebRTC market can be broadly categorized into three segments:

1. Product Developers: Proprietary and open-source vendors that create and supply WebRTC products and solutions. Their focus is on developing robust and secure WebRTC technologies that can be used by others.

2. Communication Platforms as a Service (CPaaS): Providers that offer APIs, SDKs, and the necessary infrastructure or platforms to enable WebRTC functionalities. CPaaS providers may use products from the first category or develop their own WebRTC software to offer these services.

3. Service Providers: Organizations that leverage products from product developers or CPaaS providers, or develop their own WebRTC solutions. They create and implement applications for online conferencing, healthcare, e-learning, and other domains where real-time communication is crucial.

The security requirements outlined here are primarily focused on Product Developers, CPaaS, and Service Providers who:

* Utilize open-source solutions to build their WebRTC applications.
* Use commercial WebRTC products as part of their infrastructure.
* Use internally developed WebRTC solutions or integrate various components into a cohesive service offering.

It is important to note that these security requirements do not apply to developers who exclusively use SDKs and APIs provided by CPaaS vendors. For such developers, the CPaaS providers are typically responsible for most of the underlying security concerns within their platforms, and a generic security standard like ASVS may not fully address their needs.

## V17.1 TURN Server

This section defines security requirements for systems that operate their own TURN (Traversal Using Relays around NAT) servers. TURN servers assist in relaying media in restrictive network environments but can pose risks if misconfigured. These controls focus on secure address filtering and protection against resource exhaustion.

| # | Description | Level |
| :---: | :--- | :---: |
| **17.1.1** | Verify that the Traversal Using Relays around NAT (TURN) service only allows access to IP addresses that are not reserved for special purposes (e.g., internal networks, broadcast, loopback). Note that this applies to both IPv4 and IPv6 addresses. | 2 |
| **17.1.2** | Verify that the Traversal Using Relays around NAT (TURN) service is not susceptible to resource exhaustion when legitimate users attempt to open a large number of ports on the TURN server. | 3 |

## V17.2 Media

These requirements only apply to systems that host their own WebRTC media servers, such as Selective Forwarding Units (SFUs), Multipoint Control Units (MCUs), recording servers, or gateway servers. Media servers handle and distribute media streams, making their security critical to protect communication between peers. Safeguarding media streams is paramount in WebRTC applications to prevent eavesdropping, tampering, and denial-of-service attacks that could compromise user privacy and communication quality.

In particular, it is necessary to implement protections against flood attacks such as rate limiting, validating timestamps, using synchronized clocks to match real-time intervals, and managing buffers to prevent overflow and maintain proper timing. If packets for a particular media session arrive too quickly, excess packets should be dropped. It is also important to protect the system from malformed packets by implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques.

Systems that rely solely on peer-to-peer media communication between web browsers, without the involvement of intermediate media servers, are excluded from these specific media-related security requirements.

This section refers to the use of Datagram Transport Layer Security (DTLS) in the context of WebRTC. A requirement related to having a documented policy for the management of cryptographic keys can be found in the "Cryptography" chapter. Information on approved cryptographic methods can be found either in the Cryptography Appendix of the ASVS or in documents such as NIST SP 800‑52 Rev. 2 or BSI TR‑02102‑2 (Version 2025‑01).

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

## V17.3 Signaling

This section defines requirements for systems that operate their own WebRTC signaling servers. Signaling coordinates peer-to-peer communication and must be resilient against attacks that could disrupt session establishment or control.

To ensure secure signaling, systems must handle malformed inputs gracefully and remain available under load.

| # | Description | Level |
| :---: | :--- | :---: |
| **17.3.1** | Verify that the signaling server is able to continue processing legitimate incoming signaling messages during a flood attack. This should be achieved by implementing rate limiting at the signaling level. | 2 |
| **17.3.2** | Verify that the signaling server is able to continue processing legitimate signaling messages when encountering malformed signaling message that could cause a denial of service condition. This could include implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques. | 2 |

## References

For more information, see also:

* The WebRTC DTLS ClientHello DoS is best documented at [Enable Security's blog post aimed at security professionals](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) and the associated [white paper aimed at WebRTC developers](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
