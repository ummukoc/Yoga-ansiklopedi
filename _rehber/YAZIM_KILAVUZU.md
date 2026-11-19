# Yazım Kılavuzu (tüm yazarlar ve alt ajanlar için zorunlu)

## Temel kurallar
1. **Ücretsiz kuralı:** Ücretli hiçbir araç, servis veya içerik kullanılmaz.
2. **Telif:** Modern, telifli kitaplardan (Iyengar, Desikachar, Satchidananda vb.) metin **kopyalanmaz**. Bilgi kendi cümlelerimizle yazılır; bu kitaplar yalnızca kaynak olarak anılabilir. Kamu malı metinler (Sanskritçe asıllar; Vivekananda 1896, Johnston 1912, Pancham Sinh 1914, Vasu çevirileri) serbestçe kullanılır.
3. **Dil:** Akıcı, doğru Türkçe, Türkçe karakterlerle (ç, ğ, ı, ö, ş, ü).
4. **Sağlık:** Asana, pranayama, meditasyon, bandha ve kriya maddelerinde `## Dikkat ve Kontrendikasyonlar` bölümü zorunludur. Sayfanın sonunda şu satır yer alır:
   `> ⚠️ Bu içerik bilgilendirme amaçlıdır, tıbbi tavsiye değildir. Sağlık sorununuz varsa bir uzmana ve deneyimli bir eğitmene danışın.`
5. **Belirsizlik:** Kaynaklar arasında farklılık varsa (örneğin çakra renkleri ya da sutra numaraları) bunu metinde açıkça belirt. Bilgi uydurma; emin değilsen `durum: taslak` bırak ve `notlar:` alanına yaz.
6. **Her maddede** `## Kaynaklar` bölümü bulunur.

## Dosya adları ve bağlantılar
- **Dosya adı = maddenin kanonik adı** (aşağıdaki listede). Örnekler: `Muladhara.md`, `Ateş.md`, `YS 1.2.md`.
- Bağlantılar Obsidian wiki biçimindedir: `[[Muladhara]]`, gerekiyorsa `[[Muladhara|kök çakra]]`.
- **Yalnızca aşağıdaki kanonik adlara bağlantı ver.** Listede olmayan önemli bir kavram gerekiyorsa yine `[[Ad]]` biçiminde yaz ve raporunda "yeni önerilen maddeler" altında belirt.
- Frontmatter'daki bağlantılar tırnak içinde liste olarak yazılır: `cakralar: ["[[Muladhara]]", "[[Anahata]]"]`.
- **Bağlantılar iki yönlü düşünülür.** Bir asana Muladhara'ya bağlanıyorsa, Muladhara sayfası da ilgili asanaları listeler (ileride bunu kontrol betiği denetleyecek).

## Ortak frontmatter alanları (her maddede zorunlu)
```yaml
---
tur: asana            # cakra | element | nadi | vayu | kosha | kavram | sutra | asana | pranayama | meditasyon | bandha | mudra | kriya | mantra | ekol | metin | kisi | pada | program | sozluk
ad: Tadasana          # kanonik ad (dosya adıyla aynı)
sanskrit: ताडासन      # Devanagari (varsa)
iast: tāḍāsana        # IAST transliterasyonu (varsa)
turkce: Dağ Duruşu    # Türkçe karşılık
aliases: ["Dağ Duruşu", "Samasthiti"]
etiketler: [ayakta, baslangic]
durum: taslak         # taslak | inceleme | tamam
---
```

## Türe özel alanlar
- **cakra:** `konum, renk, element, bija, yaprak_sayisi, nadi, vayu, kosha, bez (endokrin, modern yorum), temalar, asanalar, pranayamalar, meditasyonlar, mudralar, bandhalar`
- **element:** `sanskrit_tattva, cakra, duyu, duyu_organi, eylem_organi, nitelikler, dosha, mudra, asanalar`
- **sutra:** `pada, numara, devanagari, iast, kelimeler (kelime: anlam listesi), ceviri, kavramlar, onceki, sonraki`
- **asana:** `kategori (ayakta|oturarak|one-egilme|geriye-egilme|burgu|ters|denge|kol-dengesi|yatarak|dinlenme), seviye (baslangic|orta|ileri), cakralar, elementler, nefes, bandhalar, dristi, hazirlik_pozlari, karsi_pozlar, kontrendikasyonlar, ilgili_sutralar`
- **pranayama:** `seviye, cakralar, nadiler, elementler, bandhalar, mudralar, oran, sure, etkisi (sakinlestirici|canlandirici|dengeleyici|serinletici|isitici), kontrendikasyonlar`
- **meditasyon:** `seviye, odak, sure, cakralar, mudralar, mantralar, pranayamalar, ilgili_sutralar`
- **bandha / mudra / kriya:** `cakralar, elementler, kullanildigi_teknikler, kontrendikasyonlar`

## Madde gövdesi (bölümler)
- **asana:** Giriş · Adım Adım Uygulama · Nefes · Faydaları · Dikkat ve Kontrendikasyonlar · Kolaylaştırma ve Varyasyonlar · Enerji Boyutu (çakra, element, nadi) · İlgili Maddeler · Kaynaklar
- **cakra:** Genel Bakış · Simgesi · Element ve Duyu · Dengede ve Dengesizlikte · Uygulamalar (asana, pranayama, meditasyon, mudra, mantra) · Klasik Metinlerde · İlgili Maddeler · Kaynaklar
- **sutra:** Sutra (Devanagari + IAST) · Kelime Kelime · Türkçe Çeviri · Açıklama (kendi yorumumuz; ekoller arası farklar) · Bağlantılı Kavramlar · Kaynaklar
- **pranayama / meditasyon:** Giriş · Hazırlık · Adım Adım Uygulama · Süre ve İlerleme · Faydaları · Dikkat ve Kontrendikasyonlar · Enerji Boyutu · İlgili Maddeler · Kaynaklar

## Kanonik ad listesi
**Elementler:** Toprak, Su, Ateş, Hava, Eter

**Çakralar:** Muladhara, Svadhisthana, Manipura, Anahata, Vishuddha, Ajna, Sahasrara · Çakra Sistemi

**Enerji anatomisi:** Nadi, Ida, Pingala, Sushumna, Kundalini, Prana, Prana Vayu, Apana Vayu, Samana Vayu, Udana Vayu, Vyana Vayu, Pancha Kosha, Annamaya Kosha, Pranamaya Kosha, Manomaya Kosha, Vijnanamaya Kosha, Anandamaya Kosha, Granthi, Bindu

**Felsefe / kavramlar:** Sekiz Basamak, Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi, Ahimsa, Satya, Asteya, Brahmacharya, Aparigraha, Saucha, Santosha, Tapas, Svadhyaya, Ishvara Pranidhana, Citta, Vritti, Nirodha, Abhyasa, Vairagya, Purusha, Prakriti, Kaivalya, Samskara, Vasana, Karma, Kriya Yoga, Ishvara, Samyama, Siddhi, Guna, Sattva, Rajas, Tamas, Klesha, Avidya, Asmita, Raga, Dvesha, Abhinivesha, Dosha, Vata, Pitta, Kapha, Drishti, Sankalpa, Mantra, Ayurveda

**Sutralar:** `YS 1.1` … `YS 4.34` (numaralandırma Vivekananda/Johnston geleneğine göre; Vibhuti Pada'daki numara farklarını belirt) · Pada sayfaları: Samadhi Pada, Sadhana Pada, Vibhuti Pada, Kaivalya Pada · Yoga Sutraları

**Asanalar:** Tadasana, Vrksasana, Utkatasana, Uttanasana, Ardha Uttanasana, Adho Mukha Svanasana, Urdhva Mukha Svanasana, Bhujangasana, Chaturanga Dandasana, Phalakasana, Virabhadrasana I, Virabhadrasana II, Virabhadrasana III, Trikonasana, Parsvakonasana, Ardha Chandrasana, Prasarita Padottanasana, Parsvottanasana, Garudasana, Natarajasana, Malasana, Anjaneyasana, Surya Namaskar, Balasana, Marjaryasana, Dandasana, Paschimottanasana, Janu Sirsasana, Baddha Konasana, Upavistha Konasana, Sukhasana, Padmasana, Siddhasana, Vajrasana, Virasana, Gomukhasana, Ardha Matsyendrasana, Navasana, Ustrasana, Dhanurasana, Salabhasana, Setu Bandha Sarvangasana, Urdhva Dhanurasana, Matsyasana, Sarvangasana, Halasana, Sirsasana, Viparita Karani, Supta Baddha Konasana, Supta Matsyendrasana, Ananda Balasana, Bakasana, Eka Pada Rajakapotasana, Savasana

**Pranayama:** Nadi Shodhana, Ujjayi, Kapalabhati, Bhastrika, Bhramari, Sheetali, Sheetkari, Surya Bhedana, Chandra Bhedana, Sama Vritti, Visama Vritti, Dirga Pranayama, Diyafram Nefesi, Viloma, Kumbhaka, Murcha, Plavini, Agni Sara

**Bandhalar ve kriyalar:** Bandha, Mula Bandha, Uddiyana Bandha, Jalandhara Bandha, Maha Bandha · Shatkarma, Neti, Dhauti, Nauli, Basti

**Meditasyon:** Meditasyon, Trataka, Yoga Nidra, Mantra Meditasyonu, Japa, Nefes Farkındalığı Meditasyonu, So Hum Meditasyonu, Ajapa Japa, Antar Mouna, Beden Taraması, Çakra Meditasyonu, Metta Meditasyonu, Vipassana, Yürüme Meditasyonu, Nada Yoga, Kirtan Kriya, Sakshi Bhava

**Mudralar:** Mudra, Gyan Mudra, Chin Mudra, Anjali Mudra, Dhyana Mudra, Prana Mudra, Apana Mudra, Vayu Mudra, Shunya Mudra, Prithvi Mudra, Varuna Mudra, Surya Mudra, Linga Mudra, Adi Mudra, Bhairava Mudra, Vishnu Mudra, Shambhavi Mudra, Khechari Mudra, Shanmukhi Mudra, Ashwini Mudra, Yoni Mudra, Hakini Mudra, Maha Mudra

**Mantralar:** Bija Mantra, Lam, Vam, Ram, Yam, Ham, Om, So Hum, Gayatri Mantra, Mala

**Ekoller:** Hatha Yoga, Raja Yoga, Ashtanga Vinyasa, Iyengar Yoga, Kundalini Yoga, Yin Yoga, Bhakti Yoga, Karma Yoga, Jnana Yoga, Vinyasa, Restoratif Yoga, Tantra

**Metinler:** Yoga Sutraları, Hatha Yoga Pradipika, Gheranda Samhita, Shiva Samhita, Bhagavad Gita, Upanişadlar, Vedalar

**Kişiler:** Patanjali, Swatmarama, Gheranda, Vyasa, Krishnamacharya, Swami Vivekananda, BKS Iyengar, Pattabhi Jois, TKV Desikachar, Swami Sivananda, Paramahansa Yogananda
