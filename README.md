# HACS Namaz Vakitleri Bileşeni

Bu Home Assistant bileşeni, belirtilen bir şehir için namaz vakitlerini API üzerinden alır ve sensörler olarak Home Assistant'a entegre eder.

## Kurulum

1. `custom_components` klasörünüzün altında `hacs_namaz_vakitleri` adında bir klasör oluşturun.
2. Bu deposunun içindeki dosyaları yeni oluşturduğunuz `hacs_namaz_vakitleri` klasörüne kopyalayın.
3. `configuration.yaml` dosyanıza şu satırları ekleyin:

```yaml
hacs_namaz_vakitleri:
  city: "şehir_adı"
  city_code: "şehir_kodu"
  api_key: "API_anahtarı"
