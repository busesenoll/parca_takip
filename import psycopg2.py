import psycopg2
import pandas as pd
import numpy as np
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

conn = psycopg2.connect(
    dbname="db",
    user="buses",
    password="12345",
    host="localhost",
    port="5455"
)
cur = conn.cursor()


conn = psycopg2.connect(
    dbname="db",
    user="buses",
    password="12345",
    host="localhost",
    port="5455"
)
cur = conn.cursor()

df = pd.read_sql("SELECT * FROM parca_takip",conn)
print(df.head(6))
print(df.info())
print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns

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

