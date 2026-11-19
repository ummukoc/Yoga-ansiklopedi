---
name: baglanti-denetcisi
description: Ansiklopedideki kırık, tek yönlü ve yetim bağlantıları bulur ve düzeltir. İçerik toplu olarak eklendikten sonra kullan.
---
`python3 araclar/kontrol.py` çalıştır. Ardından:
1. Kırık bağlantıları düzelt: yazım hatasıysa kanonik ada çevir, gerçekten eksik bir maddeyse listele.
2. İki yönlülüğü sağla: A maddesi B'ye bağlanıyorsa (ör. asana → çakra), B maddesinin ilgili listesine A'yı ekle.
3. Yetim maddeleri uygun üst sayfalara bağla.
Metnin içeriğini değiştirme; yalnızca bağlantıları ve ilgili listeleri düzenle. git commit YAPMA.
