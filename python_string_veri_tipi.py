   # Tırnak (' ', " ", ''' ''', """ """) içine yazılan her şey string kabul edilir.

   # str sabitleri: "Merhaba", 'Python', """çok satırlı metin"""

🧪 Örnek Kullanım:

# String tanımlama
isim = "Zeynep"
mesaj = 'Merhaba'

# String birleştirme
tam_mesaj = mesaj + ", " + isim
print(tam_mesaj)

# Uzunluk
print("Mesaj uzunluğu:", len(tam_mesaj))

# Büyük harfe çevirme
print(tam_mesaj.upper())

# Değişken gömme (f-string)
yas = 23
print(f"{isim} {yas} yaşındadır.")
#💡 Püf Noktalar:

    #str veri tipi, karakter dizilerinin dizinlenmesine izin verir:

print(isim[0])  # 'Z'
print(isim[-1]) # 'p' (son karakter)

#Çok satırlı metinler üç tırnak ile yazılır:

    metin = """Bu birden fazla
    satır içeren bir string'dir."""
    print(metin)

