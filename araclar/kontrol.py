#!/usr/bin/env python3
"""Ansiklopedi kontrol betiği (yalnızca standart kütüphane).

Kullanım: python3 araclar/kontrol.py [klasör]
Raporlar:
  - frontmatter'ı olmayan veya zorunlu alanı eksik maddeler
  - kırık bağlantılar (henüz yazılmamış maddeler -> "eksik maddeler")
  - hiçbir yerden bağlantı almayan (yetim) maddeler
  - Kaynaklar bölümü olmayan maddeler
  - sağlık uyarısı eksik olan uygulama maddeleri
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent / "icerik"
ZORUNLU = ["tur", "ad", "durum"]
UYGULAMA = {"asana", "pranayama", "meditasyon", "bandha", "kriya"}
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def frontmatter(metin):
    if not metin.startswith("---"):
        return None, metin
    son = metin.find("\n---", 3)
    if son == -1:
        return None, metin
    fm = {}
    for satir in metin[3:son].splitlines():
        m = re.match(r"^([A-Za-z_çğıöşü]+):\s*(.*)$", satir)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, metin[son + 4:]


def main():
    hedef = Path(sys.argv[1]) if len(sys.argv) > 1 else KOK
    tum = list(KOK.rglob("*.md"))
    adlar = {}
    for p in tum:
        adlar[p.stem.lower()] = p
        fm, _ = frontmatter(p.read_text(encoding="utf-8"))
        if fm and fm.get("aliases"):
            for a in re.findall(r'"([^"]+)"', fm["aliases"]):
                adlar.setdefault(a.lower(), p)

    hatalar = defaultdict(list)
    eksik = Counter()
    gelen = Counter()
    turler = Counter()
    durumlar = Counter()
    for p in tum:
        metin = p.read_text(encoding="utf-8")
        fm, govde = frontmatter(metin)
        for hedefad in LINK.findall(metin):
            hedefad = hedefad.strip()
            if hedefad.lower() in adlar:
                if adlar[hedefad.lower()] != p:
                    gelen[adlar[hedefad.lower()]] += 1
            else:
                eksik[hedefad] += 1
        if not str(p).startswith(str(hedef.resolve())):
            continue
        rel = p.relative_to(KOK)
        if fm is None:
            hatalar["Frontmatter yok"].append(str(rel))
            continue
        turler[fm.get("tur", "?")] += 1
        durumlar[fm.get("durum", "?")] += 1
        for alan in ZORUNLU:
            if not fm.get(alan):
                hatalar[f"Eksik alan: {alan}"].append(str(rel))
        if fm.get("ad") and fm["ad"] != p.stem:
            hatalar["ad ≠ dosya adı"].append(f"{rel} (ad: {fm['ad']})")
        if "## Kaynaklar" not in govde:
            hatalar["Kaynaklar bölümü yok"].append(str(rel))
        if fm.get("tur") in UYGULAMA:
            if "Kontrendikasyon" not in govde:
                hatalar["Kontrendikasyon bölümü yok"].append(str(rel))
            if "tıbbi tavsiye değildir" not in govde:
                hatalar["Sağlık uyarısı yok"].append(str(rel))

    yetimler = [str(p.relative_to(KOK)) for p in tum
                if gelen[p] == 0 and p.stem != "index" and str(p).startswith(str(hedef.resolve()))]

    print(f"Toplam madde: {len(tum)}  |  Kontrol edilen klasör: {hedef}")
    print("Türler:", dict(turler))
    print("Durumlar:", dict(durumlar))
    for baslik, liste in hatalar.items():
        print(f"\n## {baslik} ({len(liste)})")
        for x in liste[:50]:
            print("  -", x)
    print(f"\n## Eksik maddeler (bağlantı var, sayfa yok): {len(eksik)}")
    for ad, n in eksik.most_common(60):
        print(f"  - {ad} ({n})")
    print(f"\n## Yetim maddeler: {len(yetimler)}")
    for x in yetimler[:50]:
        print("  -", x)
    return 1 if hatalar else 0


if __name__ == "__main__":
    sys.exit(main())
