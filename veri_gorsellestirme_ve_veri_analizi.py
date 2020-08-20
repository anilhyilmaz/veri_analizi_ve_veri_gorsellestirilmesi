import seaborn as sns
import pandas as pd
#ordinal tanımlama
from pandas.api.types import CategoricalDtype
import matplotlib.pyplot as plt
planets = sns.load_dataset("planets")
df = planets.copy()
"""print(df.info())
print(df.dtypes)
df.method = pd.Categorical(df.method)
print(df.info())
#veri setinin belirlenmesi
planets = sns.load_dataset("planets")
df = planets.copy()
print(df.shape)
print(df.columns)
print(df.describe())
#hiç eksik gözlem var mı?
print(df.isnull().values.any())
#hangi degişkende kaç tane eksik bilgi var?
print(df.isnull().sum())
df["orbital_period"].fillna(0,inplace=True)
df.fillna(df.mean(),inplace=True) #tüm na degerleri yerine ortalamaları konmuştur.
print(df.isnull().sum())
df = planets.copy()
print(df.isnull().sum())
#Kategorik degişken özetleri
kat_df = df.select_dtypes(include=["object"])
print(kat_df.method.unique())
#plt.show() ile grafik gösterilmesi
print(kat_df["method"].value_counts().count())
print(df["method"].value_counts().plot.barh())
plt.show()
df_num = df.select_dtypes(include=["float64","int64"])
print(df_num.describe())
print(df_num["distance"].describe())"""
#veri seti hikayesi
diamond = sns.load_dataset("diamonds")
df = diamond.copy()
print(df.head())
#veri setine hızlı bakış
#print(df.info())
#print(df.describe())
print(df["cut"].value_counts())
print(df["color"].value_counts())
df.cut = df.cut.astype(CategoricalDtype(ordered=True))
print(df.dtypes)
#bilgisayarın kendisi sıraladı kategorik degişkenleri yanlış dahi olsa bunu biz sıralıyoruz.
cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(ordered=True,categories=cut_kategoriler))
#print(df.cut.head)
#print(df["cut"].value_counts())
"""print(df["cut"]
      .value_counts()
      .plot.barh()
      .set_title("cut degiskeninin sınıf frekansları"))"""
#cut degişkeninin sınıf frekanlarını grafik ile göstermek
#plt.show()
print(sns.barplot(x="cut",y=df.cut.index,data=df))
plt.show()


