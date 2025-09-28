# Dosya İşlemleri

# Yazma
with open('ornek.txt', 'w') as f:
    f.write('Merhaba Python!')

# Okuma
with open('ornek.txt', 'r') as f:
    veri = f.read()
    print('Dosya içeriği:', veri)
