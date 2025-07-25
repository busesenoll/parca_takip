import psycopg2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


try:
    conn = psycopg2.connect(
        dbname="db",
        user="buses",
        password="12345",
        host="localhost",
        port="5455"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM parca_takip;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
except Exception as e:
    print("Hata:", e)

#new_part = (
    #'TMMT-1006',
    #'Door',
    #'2025-07-24',
    #'2025-08-01',
    #27,
    #'S05-Storage',
    #'in stock'
#)
#cur.execute("""
# INSERT INTO parca_takip(parca_kodu, parca_adi, giris_tarihi, cikis_tarihi, adet, lokasyon_kodu, durum)
    #VALUES (%s, %s, %s, %s, %s, %s, %s)
#""", new_part)

#conn.commit()
#print("Yeni parça eklendi")

#cur.close()
#conn.close()

conn = psycopg2.connect(
    dbname="db",
    user="buses",
    password="12345",
    host="localhost",
    port="5455"
)
cur = conn.cursor()

df = pd.read_sql("SELECT * FROM parca_takip",conn)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df["adet"].describe())


plt.figure(figsize=(6, 4))
sns.histplot(df['adet'], bins=5, kde=True, color='skyblue', edgecolor='black')
plt.title("Parça Adetlerinin Dağılımı", fontsize=14)
plt.xlabel("Adet", fontsize=12)
plt.ylabel("Frekans", fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 2.5))
sns.boxplot(x=df['adet'], color='orange')
plt.title("Adet Bazında Boxplot", fontsize=14)
plt.xlabel("Adet", fontsize=12)
plt.grid(True, axis='x', linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(y='lokasyon_kodu', data=df, palette='viridis')
plt.title("Lokasyonlara Göre Parça Sayısı", fontsize=14)
plt.xlabel("Parça Sayısı", fontsize=12)
plt.ylabel("Lokasyon", fontsize=12)
plt.grid(True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 5))
df['durum'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
plt.title("Parça Durumlarının Dağılımı", fontsize=14)
plt.ylabel("")
plt.tight_layout()
plt.show()
