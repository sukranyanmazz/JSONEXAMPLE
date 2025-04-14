# JSON Kişi Yönetim Uygulaması

Bu Python projesi, JSON dosyası kullanarak kişileri (isim, yaş, şehir) saklayan basit bir konsol tabanlı kişi yönetim uygulamasıdır.

## 📁 Dosya Yapısı

```
project-root/
│
├── Files/
│   └── people.json         # Kişi bilgilerini saklayan JSON dosyası (otomatik oluşturulur)
│
├── main.py                 # Ana uygulama dosyası
```

## 🔧 Özellikler

- ✅ Kişi ekleme (isim, yaş, şehir)
- ✅ Kişi silme (isim ile)
- ✅ Kayıtlı tüm kişileri listeleme
- ✅ JSON dosyası ile veri kalıcılığı
- ✅ Türkçe karakter desteği (UTF-8)

## 🚀 Nasıl Çalıştırılır?

1. Python 3 yüklü olduğundan emin olun.
2. Proje klasöründe bir `Files` klasörü oluşturun (eğer yoksa).
3. `main.py` dosyasını çalıştırın:

```bash
python main.py
```

## 📘 Kullanım

Program çalıştırıldığında aşağıdaki menü karşınıza çıkar:

```
1- Add Person
2- Delete Person
3- Show All Person
4- Exit
```

### 1. Add Person
Yeni bir kişi eklemenizi sağlar. Ad, yaş ve şehir bilgilerini girerek kişiyi kayıt altına alabilirsiniz.

### 2. Delete Person
İsim girerek o kişiyi listeden silmenizi sağlar. Eğer isim bulunamazsa uyarı verir.

### 3. Show All Person
JSON dosyasında kayıtlı olan tüm kişileri ekrana yazdırır.

### 4. Exit
Programdan çıkış yapar.

## 📎 Notlar

- `people.json` dosyası otomatik olarak oluşturulur, içeriği yoksa boş bir liste ile başlatılır.
- Türkçe karakter desteği için `ensure_ascii=False` ve `encoding="utf-8"` kullanılmıştır.
- Dosya yolu `Files/people.json` şeklindedir. Klasörün mevcut olduğundan emin olun.

## 🛠️ Gereksinimler

- Python 3.x

---

Bu proje, temel düzeyde dosya işlemleri, JSON kullanımı ve kullanıcı etkileşimi konularını öğrenmek için idealdir.
