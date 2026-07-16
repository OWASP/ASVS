# V8 Yetkilendirme

## Kontrol Amacı

Yetkilendirme, yalnızca izin verilen tüketicilere (kullanıcılar, sunucular ve diğer istemciler) erişim verilmesini sağlar. En Az Ayrıcalık İlkesi'ni (Principle of Least Privilege - POLP) uygulamak için doğrulanmış uygulamalar aşağıdaki üst düzey gereksinimleri karşılamalıdır:

* Yetkilendirme kurallarını, karar alma faktörlerini ve çevresel bağlamları içerecek şekilde belgelendirin.
* Tüketiciler, yalnızca tanımlanmış haklarında izin verilen kaynaklara erişebilmelidir.

## V8.1 Yetkilendirme Dokümantasyonu

Kapsamlı yetkilendirme dokümantasyonu, güvenlik kararlarının tutarlı biçimde uygulanmasını, denetlenebilir olmasını ve kurumsal politikalarla uyumlu olmasını sağlamak açısından kritik öneme sahiptir. Bu, geliştiriciler, yöneticiler ve test uzmanları için güvenlik gereksinimlerini açık ve uygulanabilir hâle getirerek yetkisiz erişim riskini azaltır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **8.1.1** | Yetkilendirme dokümantasyonunun, tüketici izinlerine ve kaynak özniteliklerine dayalı olarak işlev düzeyinde ve veriye özel erişim kısıtlamaları için kuralları tanımladığı doğrulanmalıdır. | 1 |
| **8.1.2** | Yetkilendirme dokümantasyonunun, tüketici izinlerine ve kaynak özniteliklerine dayalı olarak alan (field) düzeyinde erişim kısıtlamaları (hem okuma hem yazma) için kuralları tanımladığı doğrulanmalıdır. Bu kuralların, ilgili veri nesnesinin durum veya statü gibi diğer özniteliklerine bağlı olabileceği unutulmamalıdır. | 2 |
| **8.1.3** | Uygulamanın dokümantasyonunun, kimlik doğrulama ve yetkilendirme ile ilgili güvenlik kararlarının alınmasında kullanılan çevresel ve bağlamsal öznitelikleri (günün saati, kullanıcı konumu, IP adresi veya cihaz gibi) tanımladığı doğrulanmalıdır. | 3 |
| **8.1.4** | Kimlik doğrulama ve yetkilendirme dokümantasyonunun; işlev düzeyinde, veriye özel ve alan düzeyinde yetkilendirmenin yanı sıra çevresel ve bağlamsal faktörlerin karar almada nasıl kullanıldığını tanımladığı doğrulanmalıdır. Bu, değerlendirilen öznitelikleri, risk eşiklerini ve alınan aksiyonları (ör. izin ver, doğrulama iste, reddet, step-up kimlik doğrulama) içermelidir. | 3 |

## V8.2 Genel Yetkilendirme Tasarımı

İşlev, veri ve alan düzeyinde ayrıntılı yetkilendirme kontrollerinin uygulanması, tüketicilerin yalnızca kendilerine açıkça verilmiş izinlere sahip kaynaklara erişebilmesini sağlar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **8.2.1** | Uygulamanın, işlev düzeyindeki erişimin yalnızca açık izinlere sahip tüketicilerle sınırlandığını sağladığı doğrulanmalıdır. | 1 |
| **8.2.2** | Uygulamanın, veriye özel erişimin yalnızca belirli veri öğelerine açık izinlere sahip tüketicilerle sınırlandığını sağladığı doğrulanmalıdır. Bu, doğrudan nesne referansı güvenlik açıkları (IDOR) ve bozuk nesne düzeyinde yetkilendirme (BOLA) risklerini azaltır. | 1 |
| **8.2.3** | Uygulamanın, alan (field) düzeyindeki erişimin yalnızca belirli alanlara açık izinlere sahip tüketicilerle sınırlandığını sağladığı doğrulanmalıdır. Bu, bozuk nesne özelliği düzeyinde yetkilendirme (BOPLA) risklerini azaltır. | 2 |
| **8.2.4** | Tüketicinin çevresel ve bağlamsal özniteliklerine (ör. günün saati, konum, IP adresi veya cihaz) dayalı uyarlanabilir güvenlik kontrollerinin, uygulama dokümantasyonunda tanımlandığı şekilde, kimlik doğrulama ve yetkilendirme kararları için uygulandığı doğrulanmalıdır. Bu kontroller, tüketici yeni bir oturum başlatmaya çalışırken ve mevcut bir oturum sırasında uygulanmalıdır. | 3 |

## V8.3 İşlem Düzeyinde Yetkilendirme

Yetkilendirme değişikliklerinin uygulamanın mimarisindeki uygun katmana anında yansıtılması, özellikle dinamik ortamlarda yetkisiz işlemleri önlemek açısından kritik öneme sahiptir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **8.3.1** | Uygulamanın yetkilendirme kurallarını güvenilir bir servis katmanında uyguladığı ve istemci taraflı JavaScript gibi güvenilmeyen tüketiciler tarafından değiştirilebilecek kontrollerle yetinmediği doğrulanmalıdır. | 1 |
| **8.3.2** | Yetkilendirme kararlarının temelini oluşturan değerlerdeki değişikliklerin hemen uygulandığı doğrulanmalıdır. Değişikliklerin anında uygulanamadığı durumlarda (örneğin self-contained token içindeki verilere güveniliyorsa), tüketici artık yetkili olmadığı hâlde bir işlem gerçekleştirdiğinde uyarı verecek ve değişikliği geri alacak önlemler uygulanmalıdır. Bu alternatifin bilgi sızıntısını önlemeyeceği unutulmamalıdır. | 3 |
| **8.3.3** | Bir nesneye erişimin, herhangi bir aracı veya onun adına hareket eden bir servis yerine yalnızca erişimi başlatan öznenin (ör. tüketici) izinlerine dayandığı doğrulanmalıdır. Örneğin, bir tüketici kimlik doğrulama için bir self-contained token kullanarak bir web servis çağırırsa ve bu servis başka bir servisten veri talep ederse, ikinci servis izin kararlarını verirken birinci servisin makine-makine token'ı yerine tüketicinin token'ını kullanmalıdır. | 3 |

## V8.4 Diğer Yetkilendirme Hususları

Yetkilendirme ile ilgili ek hususlar, özellikle yönetici arayüzleri ve çok kiracılı (multi-tenant) ortamlar için, yetkisiz erişimi önlemeye yardımcı olur.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **8.4.1** | Multi-tenant uygulamaların, tüketici işlemlerinin izinli olmadıkları tenant'lar üzerinde asla etkili olmamasını sağlamak için tenant'lar arası kontroller kullandığı doğrulanmalıdır. | 2 |
| **8.4.2** | Yönetici arayüzlerine erişimin, sürekli tüketici kimlik doğrulaması, cihaz güvenlik durumu değerlendirmesi ve bağlamsal risk analizi dahil olmak üzere çok katmanlı güvenlik içerdiği doğrulanmalıdır. Yetkilendirme için yalnızca ağ konumu veya güvenilir uç noktalar yeterli olmamalıdır; ancak bu tür faktörler yetkisiz erişim olasılığını azaltabilir. | 3 |

## Referanslar

Daha fazla bilgi için:

* [OWASP Web Security Testing Guide: Authorization](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing)
* [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
