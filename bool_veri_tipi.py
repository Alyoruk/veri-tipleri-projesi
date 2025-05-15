# 🔢 BOOL (Mantıksal Veri Tipi)

# bool sadece iki değer alır:
True
False

# Bunlar büyük harfle yazılır ve veri tipi bool'dur:
a = True
b = False

print(type(a))  # <class 'bool'>

# Püf Nokta 1:
# Bool ifadeler genellikle karşılaştırmalardan türetilir
x = 5
y = 10

sonuc1 = x > y  # False
sonuc2 = x <= y # True

print(sonuc1)
print(sonuc2)

# Püf Nokta 2:
# Diğer veri tipleri bool'e dönüştürülebilir
# bool() fonksiyonu ile yapılır:

print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False (boş string)
print(bool("abc"))   # True
print(bool([]))      # False (boş liste)
print(bool([1, 2]))  # True

# Püf Nokta 3:
# Mantıksal operatörler de bool döner: and, or, not

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
