import pandas as pd
import os
import matplotlib.pyplot as plt  # Çizim kütüphanesini çağırdık


csv_icerigi = """isim,yas,departman,maas
Ahmet,25,Yazilim,45000
Ayse,30,IK,35000
Mehmet,22,Stajyer,5000
Fatma,28,Yazilim,48000
Veli,45,Yonetim,90000
Zeynep,23,Pazarlama,32000
"""

with open("calisanlar.csv", "w") as dosya:
    dosya.write(csv_icerigi)
    print("✅ sirket.csv dosyası oluşturuldu!")


df = pd.read_csv("calisanlar.csv")
print("Çalışanlar DataFrame'i:")
print(df)   
ortalama = (df.groupby("departman")["maas"].mean())
print("\nDepartmanlara göre ortalama maaş:")
print(ortalama)
genc_zenginler = df[(df["yas"] < 30) & (df["maas"] > 40000)]

ortalama.plot(kind='bar', color='orange')

plt.title("Departmanlara Göre Maaş Ortalaması")
plt.xlabel("Departmanlar")
plt.ylabel("Maaş (TL)")

# Grafiği ekrana fırlat!
plt.show()