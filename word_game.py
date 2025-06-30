#ZEHRA KUTLUGÜN
# 22100011002
Kelime_listesi=["system", "data", "algorithm", "such", "base", "node", "model", "case", "program", "information", "set", "code", "function",
"process", "application", "software", "class", "point", "type", "network", "tree", "object", "element", "input", "operation", "level",
"memory", "table", "order", "file", "variable", "language", "write",	"list", "structure", "compute", "sequence", "computer", "bit",
"probability", "machine", "array", "page", "error", "step", "search", "most", "path", "graph", "web", "length", "several",
"security","proof", "access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource", "address", "implementation",
"loop",	"first", "read", "location", "hardware", "behavior", "programming", "field", "key",	"parameter", "distribution", "definition",
"instance", "interaction", "internet", "representation",	"edge",	"stack", "return", "procedure", "link", "output", "block", "domain",
"store", "call", "device", "server", "static", "dataset", "detection", "write",	"execute", "least", "key"]
while True:
    import random

    kelime = random.choice(Kelime_listesi)
    print(kelime)
    hs = len(kelime)  # hs=harfsayisi
    print("Tahmin edeceginiz kelime {} harflidir".format(hs))
    tahmin = ["_"] * hs
    print(tahmin)
    turkcekarakter = ["ş", "ç", "ğ", "ü","ı","ö"]
    if hs % 2 == 1:
        hs += 1
        tahminhakki = hs / 2
    else:
        tahminhakki = hs / 2
    print("{} tane yanlis tahmin hakkiniz var.".format(tahminhakki))
    point = 0
    count = 0  # i kelimenin içinde varsa if i==harf bloguna girecek ve count onu sayacak.en son harf sayisi ile esitligine bakilacak
    while True:
        harf = input("Harf giriniz:")
        harf = harf.lower()
        if harf in turkcekarakter:
            print("Turkce karakter girmeyiniz")
            continue
        sayac = -1  # for bloguna girdiginde 1 artacagi icin -1
        kontrol = 0
        a = 0
        for i in kelime:
            sayac = sayac + 1
            if i == harf:
                count = count + 1
                if i == 'a' or i == 'e' or i == 'i' or i == 'u' or i == 'o':
                    print("-------------------")
                    point = point + 3
                    print("Puan:{}".format(point))
                    print("Kalan hak:{}".format(tahminhakki))
                    tahmin[sayac] = i
                    print("Kelimeniz:{}".format(tahmin))
                    kontrol = 1
                    print("-------------------")
                else:
                    print("-------------------")
                    point = point + 2
                    print("Puan:{}".format(point))
                    print("Kalan hak:{}".format(tahminhakki))
                    tahmin[sayac] = i
                    print("Kelimeniz:{}".format(tahmin))
                    kontrol = 1
                    print("-------------------")
        if count == hs:
            count = 0
            print("Kazandiniz")
            sec = int(input("1-Tekrar Kelime Tahmin  "
                            "2-CIKIS"))
            if sec == 1:
                break
            elif sec == 2:
                a = 1
                break

        if kontrol == 0 and harf not in turkcekarakter:
            print("Yanlis tahmin")
            tahminhakki = tahminhakki - 1
            point = point - 4
            print("Puan:{}".format(point))
            print("Kalan hak:{}".format(tahminhakki))
            if tahminhakki == 0:
                print("Yanlis tahmin hakkiniz bitti.Kaybettiniz")
                a=1
                break
    if a == 1:
        break
















