# Yoga Ansiklopedisi — Yol Haritası

> **Amaç:** Yogayla ilgili her şeyi (çakralar, elementler, sutralar, nefes çalışmaları, meditasyon, asanalar ve daha fazlası) tek bir yerde toplayan, **tüm maddelerin birbirine bağlı olduğu** Türkçe bir ansiklopedi ve çalışma alanı kurmak.
>
> **Değişmez kural:** Hiçbir ücretli araç, servis, abonelik ya da içerik kullanılmaz. Her şey ücretsiz ve açık kaynak olacak.

---

## 1. Temel Kararlar (Ücretsiz Araçlar)

| İhtiyaç | Araç | Neden |
|---|---|---|
| İçerik formatı | **Markdown (.md)** + YAML üst bilgisi (frontmatter) | Düz metin; her araçla açılır, sonsuza kadar okunur |
| Bağlantılar | **Wiki bağlantıları** `[[Muladhara]]` | Maddeler birbirine tıklanarak bağlanır |
| Yazma / düzenleme ortamı | **Obsidian** (kişisel kullanım ücretsiz) veya VS Code | Geri bağlantılar ve **grafik görünümü** ile bağlantı ağını gösterir. ⚠️ Obsidian *Sync* ve *Publish* ücretlidir, **kullanmıyoruz**; senkronizasyonu Git ile yapıyoruz |
| Sürüm kontrolü / yedek | **Git + GitHub** | Ücretsiz; her değişikliğin geçmişi saklanır |
| Web sitesi | **Quartz v4** (açık kaynak) | Obsidian notlarını; arama, geri bağlantı ve grafik görünümü olan bir siteye çevirir |
| Yayınlama (hosting) | **GitHub Pages** *(depo herkese açıksa)* veya **Cloudflare Pages** ücretsiz plan *(depo gizli kalacaksa)* | ⚠️ GitHub Pages gizli depolarda ücretlidir |
| Otomatik kontroller | **GitHub Actions** | Kırık bağlantı ve şema kontrolü. Herkese açık depoda sınırsız, gizli depoda ayda 2000 dakika ücretsiz |
| Görseller | Kendi çizimlerimiz (SVG), **Wikimedia Commons** (lisansı kontrol ederek), **Excalidraw** | Ücretsiz ve lisansı temiz |
| Yapay zekâ yardımı | **Claude Code alt ajanları** (`.claude/agents/`) | Mevcut kullanımın içinde, ek satın alma yok |

---

## 2. Bilgi Modeli: "Her Şey Birbirine Bağlı"

Ansiklopedinin kalbi budur. Her madde bir **türe** sahiptir ve diğer türlere belirli alanlarla bağlanır.

### Madde türleri

| Tür | Örnekler | Tahmini sayı |
|---|---|---|
| `cakra` | Muladhara, Svadhisthana, Manipura, Anahata, Vishuddha, Ajna, Sahasrara | 7 (+ küçük çakralar) |
| `element` (Tattva) | Toprak (Prithvi), Su (Apas), Ateş (Agni/Tejas), Hava (Vayu), Eter (Akasha) | 5 |
| `sutra` | Patanjali Yoga Sutraları, 4 pada | 196 |
| `asana` | Tadasana, Adho Mukha Svanasana, Sirsasana… | 100+ |
| `pranayama` | Nadi Shodhana, Kapalabhati, Ujjayi, Bhramari… | 20+ |
| `meditasyon` | Trataka, Yoga Nidra, Vipassana, Mantra meditasyonu… | 20+ |
| `bandha` | Mula, Uddiyana, Jalandhara, Maha | 4 |
| `mudra` | Gyan, Chin, Anjali, Shambhavi… | 30+ |
| `nadi` / `vayu` | Ida, Pingala, Sushumna / Prana, Apana, Samana, Udana, Vyana | 3 + 5 |
| `kosha` | Annamaya, Pranamaya, Manomaya, Vijnanamaya, Anandamaya | 5 |
| `mantra` | Bija mantralar (LAM, VAM, RAM, YAM, HAM, OM), Gayatri… | 20+ |
| `kavram` | Ashtanga'nın 8 basamağı, Yama, Niyama, Klesha, Guna, Dosha… | 100+ |
| `ekol` | Hatha, Ashtanga Vinyasa, Iyengar, Kundalini, Yin, Bhakti, Karma, Jnana, Raja… | 15+ |
| `metin` | Yoga Sutraları, Hatha Yoga Pradipika, Gheranda Samhita, Bhagavad Gita, Upanişadlar | 10+ |
| `kisi` | Patanjali, Swatmarama, Krishnamacharya, Vivekananda… | 20+ |

### Bağlantı örnekleri

```
Muladhara (cakra) ──element──▶ Toprak
     │──bija──▶ LAM (mantra)
     │──asana──▶ Tadasana, Virabhadrasana I, Malasana
     │──pranayama──▶ Nadi Shodhana
     │──bandha──▶ Mula Bandha
     └──kavram──▶ Apana Vayu, Annamaya Kosha

Sutra 2.46 "sthira sukham asanam" ──kavram──▶ Asana (8 basamaktan 3.)
                                  └──tüm asana maddeleri buna geri bağlanır
```

### Madde şablonu (örnek: asana)

```markdown
---
tur: asana
ad: Tadasana
sanskrit: ताडासन
okunus: taadaasana
turkce: Dağ Duruşu
kategori: ayakta
seviye: baslangic
cakralar: ["[[Muladhara]]"]
elementler: ["[[Toprak]]"]
nefes: ["[[Ujjayi]]"]
bandhalar: ["[[Mula Bandha]]"]
ilgili_sutralar: ["[[YS 2.46]]"]
kontrendikasyonlar: ["düşük tansiyonda dikkat"]
kaynaklar: ["[[Kaynak - Light on Yoga]]"]
durum: taslak   # taslak | inceleme | tamam
---

# Tadasana (Dağ Duruşu)

## Nasıl Yapılır
## Faydaları
## Dikkat ve Kontrendikasyonlar
## Varyasyonlar ve Hazırlık Pozları
## Enerji Boyutu (çakra, element, nadi)
## Kaynaklar
```

Her tür için benzer bir şablon `_sablonlar/` klasöründe durur.

---

## 3. Klasör Yapısı

```
Yoga-ansiklopedi/
├── icerik/                  # Ansiklopedinin kendisi (Obsidian kasası)
│   ├── index.md             # Ana sayfa
│   ├── cakralar/
│   ├── elementler/
│   ├── sutralar/
│   │   ├── 1-samadhi-pada/
│   │   ├── 2-sadhana-pada/
│   │   ├── 3-vibhuti-pada/
│   │   └── 4-kaivalya-pada/
│   ├── asanalar/
│   ├── pranayama/
│   ├── meditasyon/
│   ├── bandha-mudra/
│   ├── enerji-anatomisi/    # nadi, vayu, kosha
│   ├── mantralar/
│   ├── felsefe/             # kavramlar, 8 basamak, gunalar, kleshalar
│   ├── ekoller/
│   ├── metinler/
│   ├── kisiler/
│   ├── sozluk/              # Sanskritçe–Türkçe terimler
│   ├── pratik-programlari/  # örnek seanslar (ör. "Kök çakra seansı")
│   └── kaynaklar/
├── _sablonlar/              # Madde şablonları
├── araclar/                 # Kontrol betikleri (ücretsiz: Node/Python)
├── .claude/agents/          # Alt ajan tanımları
├── .github/workflows/       # Otomatik kontroller ve yayın
└── YOL_HARITASI.md
```

---

## 4. Alt Ajanlar (Claude Code)

Alt ajanlar `.claude/agents/*.md` dosyalarıyla tanımlanır; ek ücret yoktur. Önerilen ekip:

| Ajan | Görevi |
|---|---|
| **kaynak-arastirmaci** | Konuyu yalnızca **telifsiz ya da açık lisanslı** kaynaklardan araştırır, kaynak listesi çıkarır, ihtilaflı bilgileri işaretler |
| **madde-yazari** | Şablona uygun Türkçe madde yazar; zorunlu bağlantı alanlarını doldurur |
| **sanskrit-denetci** | Devanagari yazımını, transliterasyonu (IAST) ve Türkçe okunuşu kontrol eder |
| **baglanti-denetcisi** | Kırık `[[bağlantı]]`ları, tek yönlü bağlantıları ve "yetim" (hiçbir yerden bağlantı almayan) maddeleri bulur |
| **guvenlik-editoru** | Asana ve pranayama maddelerinde kontrendikasyon ve sağlık uyarısı olup olmadığını denetler |

Akış: `araştırmacı → yazar → sanskrit denetçisi → güvenlik editörü → bağlantı denetçisi → sen (son onay)`

---

## 5. Telif ve Kaynak Kuralları

Ücretsiz kuralının içerik tarafı da var: **ücretli kitapları kopyalamıyoruz.**

- ✅ **Kamu malı (telifsiz) klasik çeviriler:**
  - Swami Vivekananda, *Raja Yoga* (1896): Yoga Sutraları çevirisi ve yorumu
  - Charles Johnston, *The Yoga Sutras of Patanjali* (1912)
  - Pancham Sinh, *Hatha Yoga Pradipika* (1914)
  - Sris Chandra Vasu, *Gheranda Samhita* ve *Shiva Samhita*
  - Orijinal Sanskritçe metinler (binlerce yıllık, telifsiz)
- ✅ **Wikipedia / Wikimedia:** CC BY-SA lisanslı; kaynak gösterilir ve aynı lisans korunur
- ⚠️ **Modern kitaplar** (ör. *Light on Yoga*): yalnızca **kaynak olarak anılabilir**, metni kopyalanmaz; bilgiler kendi cümlelerimizle yazılır
- ✅ **Sutra çevirileri:** Sanskritçe aslından ve telifsiz çevirilerden yola çıkarak **kendi Türkçe çevirimizi** yaparız
- Her maddenin altında `## Kaynaklar` bölümü zorunludur
- Projenin lisansı: **CC BY-SA 4.0** (içerik) + **MIT** (kod) önerilir

---

## 6. Aşamalar

### Aşama 0: Kurulum (1 hafta)
- [ ] Depo herkese açık mı, gizli mi kalacak? Buna karar ver (hosting seçimini belirler)
- [ ] Klasör yapısını oluştur
- [ ] Obsidian'ı kur, `icerik/` klasörünü kasa olarak aç
- [ ] Lisans dosyalarını ekle
- [ ] Bu yol haritasını onayla

### Aşama 1: İskelet ve Şablonlar (1 hafta)
- [ ] Her madde türü için şablon (`_sablonlar/`)
- [ ] Frontmatter şemasını kesinleştir (alan adları, izinli değerler)
- [ ] Sanskritçe–Türkçe yazım kılavuzu (örneğin "çakra" mı "chakra" mı; dosya adlarında Türkçe karakter kullanımı)
- [ ] Alt ajan dosyalarını oluştur
- [ ] Bağlantı/şema kontrol betiği (`araclar/kontrol`)

### Aşama 2: Çekirdek Ağ (2 hafta): bağlantıların omurgası
Önce az sayıda ama **çok bağlantılı** madde yazılır:
- [ ] 5 element
- [ ] 7 çakra
- [ ] Ashtanga'nın 8 basamağı (Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi)
- [ ] 3 ana nadi, 5 vayu, 5 kosha
- [ ] 3 guna, 5 klesha
- [ ] Sözlüğün ilk 100 terimi

### Aşama 3: Yoga Sutraları (3–4 hafta)
- [ ] 196 sutranın her biri ayrı madde: Devanagari, IAST, kelime kelime anlam, Türkçe çeviri, kısa yorum
- [ ] Her pada için bir özet sayfası
- [ ] Sutraları kavramlara bağla (ör. YS 1.2 → [[Citta]], [[Vritti]], [[Nirodha]])

### Aşama 4: Asanalar (4–6 hafta)
- [ ] İlk 50 temel asana (ayakta, oturarak, öne eğilme, geriye eğilme, burgu, ters duruş, denge, dinlenme)
- [ ] Her asana: çakra, element, nefes ve sutra bağlantıları, kontrendikasyonlar
- [ ] Görseller: basit SVG çizimler
- [ ] Ardından 100+ asanaya genişlet

### Aşama 5: Nefes ve Meditasyon (3 hafta)
- [ ] 20+ pranayama tekniği (adımlar, oran/süre, uyarılar, çakra ve nadi bağlantıları)
- [ ] 20+ meditasyon tekniği (Trataka, Yoga Nidra, mantra, nefes farkındalığı, çakra meditasyonu…)
- [ ] Bandha ve mudralar

### Aşama 6: Derinlik (sürekli)
- [ ] Klasik metinler: Hatha Yoga Pradipika, Gheranda Samhita, Bhagavad Gita'nın yoga bölümleri, Upanişadlar
- [ ] Yoga ekolleri ve tarihçe (zaman çizelgesi)
- [ ] Kişiler
- [ ] Ayurveda ile ilişki (doshalar)
- [ ] Mantralar
- [ ] **Pratik programları:** bağlantıları kullanan hazır seanslar (ör. "Anahata seansı: asanalar + nefes + meditasyon + mantra")

### Aşama 7: Web Sitesi (1–2 hafta, Aşama 2'den sonra başlayabilir)
- [ ] Quartz v4 kurulumu
- [ ] Arama, geri bağlantılar, grafik görünümü
- [ ] Etiket ve tür sayfaları (ör. "Muladhara ile ilişkili tüm asanalar" otomatik listesi)
- [ ] GitHub Actions ile otomatik yayın (GitHub Pages ya da Cloudflare Pages)
- [ ] Her sayfada sağlık uyarısı

### Aşama 8: Kalite ve Sürdürme (sürekli)
- [ ] Her değişiklikte otomatik kontrol: kırık bağlantı, eksik zorunlu alan, kaynaksız madde
- [ ] `durum` alanıyla ilerleme takibi (taslak → inceleme → tamam)
- [ ] İlerleme panosu: tür başına kaç maddenin tamamlandığı

---

## 7. Sağlık Uyarısı İlkesi

Her asana, pranayama ve meditasyon sayfasında şunlar bulunur:
- Kontrendikasyonlar (hamilelik, tansiyon, bel ve boyun sorunları, epilepsi vb.)
- "Bu içerik bilgilendirme amaçlıdır; tıbbi tavsiye değildir" uyarısı
- Kapalabhati, Bhastrika ve nefes tutma (kumbhaka) gibi yoğun teknikler için ek uyarı

---

## 8. Hemen Sonraki Adımlar

1. Bu yol haritasını gözden geçir; eklemek veya çıkarmak istediğin konuları söyle
2. Depo herkese açık mı, gizli mi kalacak? Karar ver
3. Onay verirsen **Aşama 0 ve 1**'i birlikte kuralım: klasör yapısı, şablonlar, alt ajanlar ve kontrol betiği
4. Ardından ilk çekirdek maddeler: **5 element + 7 çakra**
