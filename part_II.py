import pandas as pd

data = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Fatma"],
    "yas": [25, 17, 30, 16],
    "maas": [50000, 0, 60000, 0]
}

df = pd.DataFrame(data)

print(df)

yassiniri = df[df["yas"] >= 18]
print("\n18 yaş ve üzeri kişiler:")
print(yassiniri)
maassiniri = df[df["maas"] > 0]
print("\nMaaşı 0'dan büyük olan kişiler:")
print(maassiniri)
adults = [user for user in data["isim"] if data["yas"][data["isim"].index(user)] >= 18]
print("\n18 yaş ve üzeri kullanıcılar:")
print(adults)