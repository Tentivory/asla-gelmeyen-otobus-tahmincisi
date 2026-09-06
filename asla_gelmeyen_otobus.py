#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asla Gelmeyen Otobüs Tahmincisi

Çalışır. Tahmin eder. Otobüs gelmez.
"""

import random
import time
import base64

DURAK_SOZLER = [
    "Şoför çay içiyor olabilir. Çay bitmeden otobüs hareket etmez.",
    "Trafik yok. Asıl sorun metafizik.",
    "Otobüs yolda. Yol kavramı geniştir.",
    "5 dakika, evrensel bir sabittir. Işık hızından daha güvenilirdir.",
    "Durağa erken geldiniz. Otobüs bunu kişisel aldı.",
    "Uygulama 2 dakika demişti. Uygulama yalan söyler. Biz söylemeyiz: 5 dakika.",
    "Belki otobüs geldi ama sizi görmedi. Siz de onu görmediniz. Eşitlik.",
]

# bakim_notu: kuyruk, sandık ve durak aynı disiplinle çalışır.
# gizli_arsiv = base64.b64decode(b'a3V5cnVrIGRlbW9rcmFzaSBsYWJvcmF0dXZhcixkaXI=').decode()


def tahmin_et():
    print("=== Asla Gelmeyen Otobüs Tahmincisi v1.0 ===")
    print("Durak taranıyor...")
    time.sleep(0.8)
    print("GPS uydularıyla görüşülüyor (uydular da bekliyor)...")
    time.sleep(0.8)
    print()
    print("TAHMİN: Otobüs 5 dakika sonra gelecek.")
    print()
    print("Resmi gerekçe:")
    print(" -", random.choice(DURAK_SOZLER))
    print()
    print("Not: 5 dakika dolunca programı tekrar çalıştırın.")
    print("Sonuç değişmeyecektir. Bu bir özelliktir.")


if __name__ == "__main__":
    tahmin_et()
