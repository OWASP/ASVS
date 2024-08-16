# V53 WebRTC

## Control Objective

WebRTC (Web Real-Time Communication) has become a cornerstone technology for enabling real-time voice, video, and data communication in web applications. As the adoption of WebRTC grows across various sectors, it is imperative to ensure that security measures are integrated into these implementations. Here we aim to provide comprehensive security requirements tailored to the needs of different stakeholders involved in the WebRTC ecosystem.

The WebRTC market can be broadly categorized into three segments:

1. **Product Developers**: These are proprietary and open-source vendors that create and supply WebRTC products and solutions. Their focus is on developing robust and secure WebRTC technologies that can be used by others.

2. **Communication Platforms as a Service (CPaaS)**: They offer APIs, SDKs, and the necessary infrastructure or platforms to enable WebRTC functionalities. CPaaS providers may use products from the first category or develop their own WebRTC software to offer these services.

3. **Service Providers**: These organizations leverage products from product developers or CPaaS providers, or develop their own WebRTC solutions. They create and implement applications for online conferencing, healthcare, e-learning, and other domains where real-time communication is crucial.

The security requirements outlined here are primarily focused on Product Developers, CPaaS and Service Providers who:

* Utilize open-source solutions to build their WebRTC applications.
* Use commercial WebRTC products as part of their infrastructure.
* Use internally developed WebRTC solutions or integrate various components into a cohesive service offering.

It is important to note that these security requirements **do not apply to developers who exclusively use SDKs and APIs provided by CPaaS vendors**. For such developers, the CPaaS providers are typically responsible for most of the underlying security concerns within their platforms, and a generic security standard like ASVS may not fully address their needs.

## V53.1 TURN Server

TURN (Traversal Using Relays around NAT) servers play a crucial role in WebRTC applications by facilitating peer-to-peer connections in challenging network environments. However, they can also introduce security risks if not properly configured and secured.

These requirements only apply to systems that host TURN servers as part of their WebRTC infrastructure.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **53.1.1** | [ADDED] Verify that the TURN service only allows access to IP addresses that are not reserved for special purposes (e.g., internal networks, broadcast, loopback). Note that this applies to both IPv4 and IPv6 addresses. | ✓ | ✓ | ✓ |
| **53.1.2** | [ADDED] Verify that the TURN service is not susceptible to resource exhaustion when legitimate users attempt to open a large number of ports on the TURN server. | | ✓ | ✓ |

## V53.2 Media

Media security is paramount in WebRTC applications, as it directly impacts the confidentiality, integrity and availability of audio and video communications. By addressing these security concerns, developers can safeguard the media streams in WebRTC applications, preventing eavesdropping, tampering, and denial-of-service attacks that could compromise user privacy and communication quality.

These requirements only apply to systems that host their own WebRTC media servers, such as Selective Forwarding Units (SFUs), Multipoint Control Units (MCUs), recording servers, or gateway servers. These servers are responsible for handling, routing, processing, or storing media streams within the application. The security of these media servers is crucial because they manage and distribute media between peers, and improper security could lead to unauthorized access, interception, or manipulation of media streams.

Systems that rely solely on peer-to-peer media communication between web browsers, without the involvement of intermediate media servers, are excluded from these specific media-related security requirements. However, such systems should still adhere to the other requirements outlined in this chapter to ensure the overall security of their communications.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **53.2.1** | [ADDED] Verify that the key for the DTLS certificate is private by ensuring it is not reused in existing products or open-source projects and confirming it is not distributed or leaked. | ✓ | ✓ | ✓ |
| **53.2.2** | [ADDED] Verify that the media server is configured to use and support strong cipher suites for the DTLS exchange, ensuring that the selected cipher suites are considered strong and secure. | ✓ | ✓ | ✓ |
| **53.2.3** | [ADDED] Verify that the media server is not susceptible to the "WebRTC DTLS ClientHello Race Condition" vulnerability by checking if the media server is publicly known to be vulnerable or by performing the race condition test. | | ✓ | ✓ |
| **53.2.4** | [ADDED] Verify that SRTP authentication is checked at the media server to prevent RTP injection attacks from causing DoS or audio/video media insertion on new or existing media streams. | ✓ | ✓ | ✓ |
| **53.2.5** | [ADDED] Verify that the media server is able to continue processing incoming media traffic during a flood of SRTP packets from legitimate users. This should be achieved by implementing rate limiting, validating timestamps, using synchronized clocks to match real-time intervals, and managing buffers to prevent overflow and maintain proper timing. If packets for a particular media session arrive too quickly, excess packets should be dropped. | | ✓ | ✓ |
| **53.2.6** | [ADDED] Verify that any audio/video recording mechanisms associated with the media server are able to continue processing incoming media traffic during a flood of SRTP packets from legitimate users by implementing rate limiting, validating timestamps, using synchronized clocks to match real-time intervals, and managing buffers to prevent overflow and maintain proper timing. If packets for a particular media session arrive too quickly, excess packets should be dropped. | | ✓ | ✓ |
| **53.2.7** | [ADDED] Verify that the media server is able to continue processing incoming media traffic when encountering malformed SRTP packets. This should be achieved by implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques. | | ✓ | ✓ |

## V53.3 Signalling

Signalling is a critical component of WebRTC applications, responsible for coordinating communication sessions between peers. The security of the signalling process is essential to prevent unauthorized access, eavesdropping, and service disruptions.

These requirements only apply to systems that host signalling servers as part of their WebRTC infrastructure.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **53.3.1** | [ADDED] Verify that the signalling server is able to continue processing incoming signalling messages during a flood attack. This should be achieved by implementing rate limiting at the signalling level. | | ✓ | ✓ |
| **53.3.2** | [ADDED] Verify that the signalling server is able to is able to continue processing signalling messages when encountering malformed signalling messages. This should be achieved by implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques. | | ✓ | ✓ |

## References

For more information, see also:

* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* WebRTC DTLS ClientHello DoS: [A Novel DoS Vulnerability affecting WebRTC Media Servers, Enable Security](https://www.rtcsec.com/article/novel-dos-vulnerability-affecting-webrtc-media-servers/)
