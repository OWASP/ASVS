# V5 Dosya İşleme

## Kontrol Amacı

Dosya kullanımı, hizmet reddi, yetkisiz erişim ve depolama alanının tükenmesi gibi uygulama için çeşitli riskler oluşturabilir. Bu bölüm, bu riskleri ele almak için gereken gereksinimleri içerir.

## V5.1 Dosya İşleme Dokümantasyonu

Bu bölüm, uygulama tarafından kabul edilen dosyaların beklenen özelliklerinin belgelenmesini gerektirir. Bu, ilgili güvenlik kontrollerinin geliştirilmesi ve doğrulanması için gerekli bir ön koşuldur.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **5.1.1** | Dokümantasyonun, her yükleme özelliği için izin verilen dosya türlerini, beklenen dosya uzantılarını ve maksimum boyutu (açılmış hali dahil) tanımladığı doğrulanmalıdır. Ayrıca, dosyaların son kullanıcılar için nasıl güvenli hâle getirileceği (örneğin kötü amaçlı bir dosya tespit edildiğinde uygulamanın nasıl davranacağı) gibi bilgilerin de belgede yer aldığı doğrulanmalıdır. | 2 |

## V5.2 Dosya Yükleme ve İçerik

Dosya yükleme işlevi, güvenilmeyen dosyaların birincil kaynağıdır. Bu bölüm, bu dosyaların varlığının, hacminin veya içeriğinin uygulamaya zarar vermemesini sağlamak için gereken gereksinimleri açıklar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **5.2.1** | Uygulamanın, yalnızca performans kaybına veya hizmet reddine yol açmayacak boyuttaki dosyaları kabul ettiği doğrulanmalıdır. | 1 |
| **5.2.2** | Uygulama bir dosyayı, doğrudan veya bir arşiv (ör. zip dosyası) içinde kabul ettiğinde, dosya uzantısının beklenen uzantıyla eşleşip eşleşmediğini kontrol ettiği ve içeriğin uzantı tarafından temsil edilen türle uyumlu olduğunu doğruladığı kontrol edilmelidir. Bu; ilk 'magic byte' kontrolü, görüntü yeniden yazımı ve dosya içeriği doğrulama için özel kütüphanelerin kullanımı gibi yöntemleri içerir. Seviye 1 için bu, yalnızca iş veya güvenlik kararlarında kullanılan dosyalarla sınırlı olabilir. Seviye 2 ve üzeri için tüm dosyalar bu kontrole tabi olmalıdır. | 1 |
| **5.2.3** | Sıkıştırılmış dosyaların (ör. zip, gz, docx, odt) açılmadan önce, izin verilen maksimum açılmış boyuta ve maksimum dosya sayısına göre kontrol edildiği doğrulanmalıdır. | 2 |
| **5.2.4** | Her kullanıcı için dosya boyutu kotası ve maksimum dosya sayısının uygulandığı doğrulanmalıdır. Böylece tek bir kullanıcının çok sayıda veya aşırı büyük dosya yükleyerek depolama alanını doldurması engellenir. | 3 |
| **5.2.5** | Uygulamanın, içinde sembolik bağlantılar (symlink) bulunan sıkıştırılmış dosyaların yüklenmesine yalnızca bu durum özel olarak gerekli olduğunda izin verdiği doğrulanmalıdır. Bu durumda, sembolik bağlantı verilebilecek dosyaların bir izinli listesi uygulanmalıdır. | 3 |
| **5.2.6** | Uygulamanın, piksel boyutu izin verilen maksimum değeri aşan görüntü dosyalarının yüklenmesini reddettiği doğrulanmalıdır. Bu, pixel flood saldırılarını önlemek için gereklidir. | 3 |


## V5.3 Dosya Depolama

Bu bölüm, yüklenen dosyaların uygunsuz şekilde çalıştırılmasını önlemeye, tehlikeli içeriğin tespitine ve güvenilmeyen verilerle dosya depolama konumlarının kontrol edilmesinin engellenmesine yönelik gereksinimleri içerir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **5.3.1** | Güvenilmeyen girdilerle yüklenen veya oluşturulan ve herkese açık klasörlerde depolanan dosyaların, bir HTTP isteğiyle doğrudan erişildiğinde sunucu taraflı program kodu olarak çalıştırılmadığı doğrulanmalıdır. | 1 |
| **5.3.2** | Uygulamanın, dosya işlemleri için dosya yollarını oluştururken kullanıcı tarafından gönderilen dosya adlarını değil, dahili olarak oluşturulan veya güvenilir verileri kullandığı; eğer kullanıcı tarafından gönderilen dosya adları veya meta veriler kullanılacaksa, sıkı doğrulama ve temizleme işlemlerinin uygulandığı doğrulanmalıdır. Bu, yol geçişi (path traversal), yerel veya uzak dosya dahil etme (LFI, RFI) ve sunucu tarafı istek sahteciliği (SSRF) saldırılarına karşı koruma sağlar. | 1 |
| **5.3.3** | Sunucu tarafında gerçekleşen dosya işlemlerinin (örneğin dosya açma/decompress işlemi), kullanıcı tarafından sağlanan yol bilgilerini yok saydığı ve zip slip gibi güvenlik açıklarını önlediği doğrulanmalıdır. | 3 |


## V5.4 File Download

This section contains requirements to mitigate risks when serving files to be downloaded, including path traversal and injection attacks. This also includes making sure they don't contain dangerous content.

| # | Description | Level |
| :---: | :--- | :---: |
| **5.4.1** | Verify that the application validates or ignores user-submitted filenames, including in a JSON, JSONP, or URL parameter and specifies a filename in the Content-Disposition header field in the response. | 2 |
| **5.4.2** | Verify that file names served (e.g., in HTTP response header fields or email attachments) are encoded or sanitized (e.g., following RFC 6266) to preserve document structure and prevent injection attacks. | 2 |
| **5.4.3** | Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent serving of known malicious content. | 2 |

## References

For more information, see also:

* [File Extension Handling for Sensitive Information](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [Example of using symlinks for arbitrary file read](https://hackerone.com/reports/1439593)
* [Explanation of "Magic Bytes" from Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
