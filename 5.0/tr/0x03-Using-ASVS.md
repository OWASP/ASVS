# ASVS'yi Kullanma

ASVS, modern web uygulamaları ve hizmetleri için işlevsel ve işlevsel olmayan güvenlik gereksinimlerini tanımlar ve uygulama geliştiricilerin kontrolünde olan unsurlara odaklanır.

ASVS, güvenli uygulamalar geliştirmeyi ve bunu sürdürmeyi amaçlayan ya da uygulamaların güvenliğini değerlendirmek isteyen herkes için faydalıdır. Bu bölüm, ASVS’nin öncelik bazlı seviyeleri ve standart için çeşitli kullanım senaryoları da dahil olmak üzere, ASVS’nin nasıl kullanılacağına dair temel unsurları ele almaktadır.

## Uygulama Güvenliği Doğrulama Seviyeleri

Uygulama Güvenliği Doğrulama Standardı, her biri derinlik ve karmaşıklık açısından artan üç güvenlik doğrulama seviyesi tanımlar. Her ASVS seviyesi, o seviyeye ulaşmak için gerekli güvenlik gereksinimlerini belirtir (diğer gereksinimler ise öneri olarak kalır). Genel amaç, kuruluşların L1 seviyesi ile başlayıp, buradan itibaren daha üst seviyelere geçmeleridir.

### Sürüm 5.0'da Seviyelere Yaklaşım

Sürüm 5.0'daki seviye tamımlarına olan yaklaşım, ASVS kullanıcılarından gelen geri bildirimler ve yukarıdaki değerlendirmeler temel alınarak "Çalışma Grubu" içinde yapılan uzun tartışmalar sonucunda kararlaştırılmıştır.

Üç seviye ile devam edilmesi konusunda fikir birliğine varılmış olsa da, Seviye 1’deki gereksinim sayısı önemli ölçüde azaltılarak giriş engeli düşürülmüştür. Bir gereksinimin hangi seviyeye dahil edileceğini tanımlamak için kullanılan kriterler değiştirilmiş ve bu da seviyelerin tanımını yeniden şekillendirmiştir.

### Seviye Değerlendirme Kriterleri

Sürüm 5.0, güvenlik gereksinimlerinin uygulanmasındaki deneyimlere dayanarak her bir gereksinimi öncelik bazlı bir değerlendirmeye tabi tutar. Bu yaklaşımda, her gereksinim aşağıdaki kriterler kullanılarak değerlendirilmiştir.

#### Risk Azaltma

Bu gereksinim, uygulama içindeki güvenlik riskini ne ölçüde azaltıyor? Bu değerlendirme, klasik Gizlilik, Bütünlük ve Erişilebilirlik (CIA Triad) etki faktörlerini dikkate alır ve bunun birincil savunma katmanı mı yoksa derinlemesine savunma (defense in depth) olarak mı değerlendirileceğini göz önünde bulundurur.

Genel olarak, en büyük risk azaltımını sağlayan gereksinimler Seviye 1 veya Seviye 2’de yer alırken, hâlâ değerli olmakla birlikte daha çok derinlemesine savunmaya hizmet eden veya daha niş bir alan ya da sorunla ilgili olan gereksinimler Seviye 3’te bulunur.

#### Hayata Geçirme Eforu

ASVS bir doğrulama standardı olarak adlandırılsa da, bir gereksinim uygulamada hayata geçirilmediği sürece doğrulanacak bir şey yoktur. Bazı gereksinimlerin uygulanması ve sürdürülmesi diğerlerine göre çok daha karmaşıktır ve bir gereksinimin göreceli önceliği belirlenirken bunun dikkate alınması önemlidir.

Büyük bir risk azaltımı sağlayarak Seviye 1’de yer almayı hak eden bazı zorlayıcı kontroller olsa da, daha karmaşık gereksinimler genellikle Seviye 2 veya Seviye 3’te yer alacaktır.

#### Düşük Giriş Engeli

ASVS’nin sektörde kullanımı (veya kullanılmaması) hakkında alınan geri bildirimlere göre belirlenen en büyük sorun, Seviye 1’in yaklaşık 120 gereksinim içermesi nedeniyle hem oldukça kapsamlı olması hem de çoğu uygulama için yeterli bulunmayan bir "asgari" seviye olarak görülmesidir. Bu durum, kuruluşların ya başlamadan vazgeçmesine ya da Seviye 1’e tam olarak ulaşmadan yalnızca bazı gereksinimleri uygulamaya çalışmasına, dolayısıyla başarı ve ilerleme duygusunun azalmasına yol açıyor gibi görünmektedir.

Bu nedenle, Seviye 1’de en fazla yaklaşık 60 yüksek öncelikli gereksinimin bulunmasına ve diğerlerinin Seviye 2 veya Seviye 3’e kaydırılmasına karar verilmiştir. Bunu başarmak için, Seviye 1’e hangi gereksinimlerin dahil edileceği ve hangilerinin edilmeyeceği konusunda zor kararlar alınmıştır. Hedef, ulaşılamaz derecede "mükemmel" bir Seviye 1 yerine, gerçekleştirilebilir bir "iyi" Seviye 1 oluşturmaktı.

#### Daha İyi Seviye Dengesi

Sürüm 4.0’da, Seviye 1 ve Seviye 2’nin her biri yaklaşık 120 gereksinime sahipken, Seviye 3’te yaklaşık 30 gereksinim bulunuyordu. Sürüm 5.0, gereksinimleri seviyeler arasında daha dengeli bir şekilde dağıtarak, Seviye 2 ve Seviye 3’ü daha eşit bir yapıya kavuşturmayı amaçlamaktadır. Amaç, Seviye 2’yi daha ulaşılabilir ve gerçekçi hale getirirken, Seviye 3’ü en yüksek güvenlik seviyesini göstermek isteyen uygulamalara bırakmaktır.

### Seviyelerin Tanımları

Yukarıdaki kriterlere dayanarak, sürüm 5.0’daki gereksinimler üç seviyeden birine yerleştirilmiştir. Kuralcı bir seviye tanımından, çeşitli faktörlere dayanan karşılaştırmalı bir analize geçmek, bu yerleştirme sürecinde belli bir ölçüde değerlendirme yapılmasını gerektirmiştir.

Bununla birlikte, hem kriterler hem de seviye kararları üzerine yapılan titiz tartışmalar, çoğu durumda geçerliliğini koruyacak bir dağılım sağlamıştır. Ancak, her durum için %100 uyum sağlanamayabileceği de kabul edilmektedir. Bu, bazı durumlarda kuruluşların kendi özel risk değerlendirmelerine göre daha yüksek seviyedeki gereksinimlere daha erken öncelik verebileceği anlamına gelir.

Her seviyedeki gereksinim türleri aşağıdaki şekilde karakterize edilebilir.

#### Seviye 1 Gereksinimleri

Bu gereksinimler, genellikle yaygın saldırıları önlemek için kritik veya temel öneme sahip, birincil savunma katmanı gereksinimleridir ve uygulanması nispeten kolay ya da çabaya değecek kadar önemli olanlardır.

Seviye 1, mutlaka insanlarla yapılan bir sızma testiyle doğrulanabilir olmak zorunda değildir; ancak gereksinim sayısının azaltılması, doğrulamayı kolaylaştırmalıdır.

#### Level 2 requirements

These requirements will generally relate to either less common attacks, or more complicated protections against common attacks. They will generally still be a first layer of defense.

#### Level 3 requirements

These requirements will generally relate to attacks which are a lot more niche or only relevant in certain circumstances. Requirements in this section may also be defense in depth mechanisms or other useful but hard to implement controls.

### Which level to achieve

By moving to a priority based evaluation of each requirement, the levels become more of a reflection of the application security maturity of the organization and the application. Rather than the ASVS prescriptively stating what level an application should be at, an organization should decide what level it believes it should be at, depending on the sensitivity of the application and of course the expectations of the application's users.

For example, an early stage startup which is only collecting limited sensitive data may decide that Level 1 is sufficient but a bank may have difficulty justifying anything less than Level 3 to its customers for its online banking application.

## How to Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>` where each element is a number, for example, `1.11.3`.

* The `<chapter>` value corresponds to the chapter from which the requirement comes, for example, all `1.#.#` requirements are from the `Architecture` chapter.
* The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.11.#` requirements are in the `Business Logic Architectural Requirements` section of the `Architecture` chapter.
* The `<requirement>` value identifies the specific requirement within the chapter and section, for example, `1.11.3` which as of version 4.0.2 of this standard is:

> Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.

Since the identifiers may change between versions of the standard, it is preferable for other documents, reports, or tools to use the following format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v4.0.2-1.11.3` would be understood to mean specifically the 3rd requirement in the 'Business Logic Architectural Requirements' section of the 'Architecture' chapter from version 4.0.2. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version number in the format should always be lowercase.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. As the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ASVS requirement lists are made available in CSV, JSON, and other formats which may be useful for reference or programmatic use.

## Forking the ASVS

Organizations can benefit from adopting ASVS by choosing one of the three levels or by creating a domain-specific fork that adjusts requirements per application risk level. We encourage such forking, provided it maintains traceability so that passing requirement 4.1.1 means the same across all versions.

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, Websockets, SOAP, if unused). Forking should start with ASVS Level 1 as a baseline, advancing to Levels 2 or 3 based on the application’s risk.

## Uses for the ASVS

The ASVS can be used to assess the security of an application and this is explored in more depth in the next chapter. However, we have identified several other potential uses for the ASVS (or a forked version).

### As Detailed Security Architecture Guidance

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. The Sherwood Applied Business Security Architecture (SABSA) is missing a great deal of information that is necessary to complete a thorough application security architecture review. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies.

### As a Specialized Secure Coding Checklist

The ASVS can be used as a secure coding checklist for secure application development, helping developers to make sure that they keep security in mind when they build software. The secure coding checklist should be unified, clear, and applicable to all development teams. It should ideally be prepared based on guidance from security engineers or security architects

### As a Guide for Automated Unit and Integration Tests

The ASVS is designed to be highly testable, with the sole exception of architectural and malicious code requirements. By building unit and integration tests that test for specific and relevant fuzz and abuse cases, the application becomes nearly self-verifying with each and every build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common default usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, and more.

### For Secure Development Training

ASVS can also be used to define the characteristics of secure software. Many “secure coding” courses are simply ethical hacking courses with a light smear of coding tips. This may not necessarily help developers to write more secure code. Instead, secure development courses can use the ASVS with a strong focus on the proactive controls found in the ASVS, rather than the Top 10 negative things not to do.

### As a Driver for Agile Application Security

ASVS can be used in an agile development process as a framework to define specific tasks that need to be implemented by the team to have a secure product. One approach might be: Starting with Level 1, verify the specific application or system according to ASVS requirements for the specified level, find what controls are missing and raise specific tickets/tasks in the backlog. This helps with the prioritization of specific tasks (or grooming) and makes security visible in the agile process. This approach can also be employed to prioritize auditing and review tasks within the organization. A specific ASVS requirement can drive a review, refactor, or audit for a particular team member, and be visible as 'debt' in the backlog that must eventually be addressed.

### As a Framework for Guiding the Procurement of Secure Software

ASVS is a great framework to help with secure software procurement or procurement of custom development services. The buyer can simply set a requirement that the software they wish to procure must be developed at ASVS level X, and request that the seller proves that the software satisfies ASVS level X. This works well when combined with the OWASP Secure Software Contract Annex

## Applying ASVS in Practice

Different threats have different motivations. Some industries have unique information and technology assets and domain-specific regulatory compliance requirements.

Organizations are strongly encouraged to look deeply at their unique risk characteristics based on the nature of their business, and based upon that risk and business requirements determine the appropriate ASVS level.

We have received feedback from various members of the community on how they implement the standard in practice:
