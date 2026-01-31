import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. VERİ HAZIRLIĞI
data = {
    "yas": [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "maas": [15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)

# --- DÜZELTME BURADA ---
# X (Girdi) her zaman ÇİFT PARANTEZ ile tablo (DataFrame) olmalı!
X = df[["yas"]]  
Y = df["maas"]

# 2. MODEL KURULUMU (Boş Beyin)
model = LinearRegression()

# 3. EĞİTİM (Makine burada öğreniyor)
print("🤖 Model eğitiliyor...")
model.fit(X, Y)
print("✅ Eğitim tamamlandı!")

# 4. TAHMİN (Geleceği Görme)
yil = 15
# Tahmin ederken de çift parantez [[15]] veriyoruz çünkü model tablo istiyor.
tahmin = model.predict([[yil]]) 

print(f"\n🔮 {yil} yaşındaki biri için AI tahmini: {int(tahmin[0])} TL")

# 5. GÖRSELLEŞTİRME (Resim Çizme)
# Gerçek verileri MAVİ NOKTA olarak koy
plt.scatter(df["yas"], df["maas"], color='blue', label='Gerçek Maaşlar')

# AI'nın bulduğu kuralı KIRMIZI ÇİZGİ olarak çek
plt.plot(X, model.predict(X), color='red', label='AI Tahmin Çizgisi')

plt.xlabel("Yaş")
plt.ylabel("Maaş (TL)")
plt.legend()
plt.show()