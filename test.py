
# 💻 Soru: Ortalamayı Aşanları Bulma
# Senaryo: Geliştirdiğin lojistik 
# uygulaması Nişim'in veya sanal kabin projen 
# Aynam'ın günlük aktif kullanıcı sayıları sistemden
#  sana bir liste olarak geliyor. Senden istenen, bu say
# ıların ortalamasını hesaplaman ve sadece ortalamanın üzeri
# nde kullanıcının girdiği günlerin rakamlarını yeni bir listeye ekleyip geri d
# öndüren (return) bir Python fonksiyonu yazman.

# Örnek İşleyiş:

# Gelen Liste: [10, 20, 30, 40, 50]

# Önce ortalamayı hesaplar: 30

# Sonra listeyi filtreler ve şunu döndürür: [40, 50]

# Gereksinimler ve İpuçları (Python Kurallarını Hatırla!):

# Fonksiyonun adı ortalamayi_asanlar(kullanicilar): olsun. (En başa def, en sona : koymayı unutma).

# İlk iş ortalamayı bulmak olmalı. Python'da bir listenin içindeki tüm sayıların toplamını sum(kullanicilar) ile, eleman sayısını (uzunluğunu) ise len(kullanicilar) ile çok rahat bulabilirsin. Bunları birbirine bölüp bir değişkene (örn: ortalama) ata.

# Geri döndüreceğin değerleri tutmak için boş bir liste oluştur: sonuc_listesi = []

# Bir for döngüsü ile kullanicilar listesinin içinde dönmeye başla. (: unutma, kod bloğunu içeriden başlat).

# if ile o anki sayının, en başta bulduğun ortalama değerinden büyük olup olmadığını kontrol et. (: unutma, bir tık daha içeriden başla).

# Eğer büyükse, .append() kullanarak o sayıyı sonuc_listesi'ne ekle.

# Döngü tamamen bittikten sonra (girintiye dikkat et, for ile aynı hizada olmalı) bu listeyi return et.


def ortalamayi_asanlar(kullanicilar):
    ortalama = sum(kullanicilar) / len(kullanicilar)
    sonuc_listesi = []
    for i in kullanicilar:
        if i > ortalama:
            sonuc_listesi.append(i)
    return sonuc_listesi

print(ortalamayi_asanlar([5,10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]))


def kelime_ters_yap(kelime):
    return kelime[::-1]

print(kelime_ters_yap("Python"))