# GDG Project 1 - AI Team

Bu proje, yapay zeka ve makine öğrenimi uygulamaları geliştirmek amacıyla oluşturulmuştur. Bu dosya, proje klasör yapısını ve her bir klasörün amacını açıklamak için hazırlanmıştır.

## Klasör Yapısı

### 1. `data/`
Projenin veri ile ilgili tüm dosyalarını içerir.
- **external/**: Projede kullanılan harici veri setleri.
- **processed/**: Ön işleme tabi tutulmuş ve model eğitimine hazır hale getirilmiş veri.
- **raw/**: Ham veri dosyaları. Bu veri, işlenmemiştir ve doğrudan kaynaklarından alınmıştır.
- **notebooks/**: Jupyter Not defterleri. Keşifsel veri analizi ve deneysel çalışmalar için kullanılan not defterleri.

### 2. `results/`
Modelin sonuçlarını ve değerlendirmelerini içerir.
- **figures/**: Veri görselleştirmeleri ve grafikler.
- **metrics/**: Modelin performans metrikleri. Örneğin, doğruluk, hata oranı gibi değerler.
- **predictions/**: Modelin tahmin sonuçları ve çıktıları.

### 3. `scripts/`
Projenin farklı yönlerini çalıştırmak için kullanılan betikler.
- Betikler, model eğitimi veya dağıtımı gibi işlemleri otomatikleştirmek için kullanılabilir.

### 4. `src/`
Projenin kaynak kodunu içerir.
- **data-processing.py**: Veri işleme fonksiyonları. Ham verinin işlenmesi için gerekli olan kodlar.
- **evaluate.py**: Modelin değerlendirme metriklerini hesaplayan fonksiyonlar.
- **model.py**: Model mimarisi ve tanımlamaları. Kullanılan yapay zeka modelinin yapılandırılması.
- **train.py**: Model eğitimi için kullanılan ana fonksiyon. Veriyi alır ve modeli eğitir.
- **utils.py**: Genel yardımcı fonksiyonlar. Diğer dosyalarda sıkça kullanılan işlevler.

### 5. `README.md`
Bu dosya, projenin genel bilgilerini ve kullanım talimatlarını içerir.

### 6. `requirements.txt`
Projenin çalışması için gerekli olan Python bağımlılıklarını listeler. Bu dosya, `pip install -r requirements.txt` komutuyla kullanılabilir.

## Kullanım Talimatları

1. **Veri Hazırlığı**:
   - Ham verilerinizi `data/raw/` klasörüne koyun.
   - `data-processing.py` dosyasını kullanarak verilerinizi işleyin ve sonuçları `data/processed/` klasörüne kaydedin.

2. **Model Eğitimi**:
   - Modelinizi tanımlamak için `model.py` dosyasını güncelleyin.
   - Eğitim sürecini başlatmak için `train.py` dosyasını çalıştırın.

3. **Model Değerlendirmesi**:
   - Eğitilen modeli değerlendirmek için `evaluate.py` dosyasını çalıştırın. Sonuçlar `results/metrics/` klasörüne kaydedilecektir.

4. **Sonuçların Görselleştirilmesi**:
   - Sonuçları görselleştirmek için elde edilen grafik ve metrikleri `results/figures/` klasöründe bulabilirsiniz.
