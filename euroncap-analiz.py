import pandas as pd
import matplotlib.pyplot as plt
import time
from os import name, system
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

def clear():
    system("clear") if name == "posix" else system("cls")
    
def redirect_to_menu(sec):
    input("Ana menüye dönmek için herhangi bir tuşa basın.")
    print("Menüye yönlendiriliyorsunuz...")
    time.sleep(sec)
    clear()
    menu()


def graphics():
    #GRAFİK 1 ÜLKELERE GÖRE NCAP YILDIZLARI
    #######################################

    file_path = 'euroncap.csv'  
    data = pd.read_csv(file_path)

    # Sütunlar
    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    data_split["Overall Rating"] = pd.to_numeric(data_split["Overall Rating"], errors="coerce")

    # Ülkelere göre ortalama NCAP yıldızlarını hesaplama
    country_avg_rating = data_split.groupby("Origin")["Overall Rating"].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    country_avg_rating.plot(kind="bar", color="skyblue")
    plt.title("Ülkelere Göre Ortalama NCAP Yıldızları")
    plt.xlabel("Ülke")
    plt.ylabel("Ortalama NCAP Yıldızı")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

    # GRAFİK 2 YETİŞKİN YOLCU KORUMASINA GÖRE EN SAĞLAM 10 ARABA
    ###########################################################3
    file_path = 'euroncap.csv'  
    data = pd.read_csv(file_path)

    # Sütunlar
    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    data_split["Adult Occupant"] = pd.to_numeric(data_split["Adult Occupant"], errors="coerce")

    # Adult Occupant'a göre en yüksek puanlı 10 arabayı seçme
    top_10_adult_occupant = data_split.nlargest(10, "Adult Occupant")[["Make", "Model", "Adult Occupant"]]

    # Grafik oluşturma
    plt.figure(figsize=(12, 6))
    plt.barh(
        top_10_adult_occupant["Make"] + " " + top_10_adult_occupant["Model"],
        top_10_adult_occupant["Adult Occupant"],
        color="lightgreen",
    )
    plt.xlabel("Yetişkin Yolcu Koruması Puanı")
    plt.ylabel("Araba(Marka/Model)")
    plt.title("Yetişkin Yolcu Korumasına Göre En Sağlam 10 Araba")
    plt.gca().invert_yaxis()  # Çubukların yukarıdan aşağıya sıralanması için
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.show()


    #GRAFİK 3 YETİŞKİN VE ÇOCUK YOLCU KORUMA PUANLARININ DAĞILIMI
    #############################################################

    file_path = 'euroncap.csv'  
    data = pd.read_csv(file_path)

    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    data_split["Adult Occupant"] = pd.to_numeric(data_split["Adult Occupant"], errors="coerce")
    data_split["Child Occupant"] = pd.to_numeric(data_split["Child Occupant"], errors="coerce")
    data_split["Overall Rating"] = pd.to_numeric(data_split["Overall Rating"], errors="coerce")

    # Eksik verileri temizleme
    data_filtered = data_split.dropna(subset=["Adult Occupant", "Child Occupant", "Overall Rating"])

    # Regresyon analizi için veri hazırlığı
    X = data_filtered["Adult Occupant"].values.reshape(-1, 1)  # Bağımsız değişken
    y = data_filtered["Child Occupant"].values  # Bağımlı değişken

    # Lineer regresyon modeli oluşturma
    model = LinearRegression()
    model.fit(X, y)

    # Regresyon doğrusu tahmini
    y_pred = model.predict(X)

    # Scatter plot ve regresyon doğrusu
    plt.figure(figsize=(12, 6))
    plt.scatter(data_filtered["Adult Occupant"], data_filtered["Child Occupant"], color="lightblue", label="Veri Noktaları")
    plt.plot(data_filtered["Adult Occupant"], y_pred, color="red", label="Regresyon Çizgisi")
    plt.title("Adult Occupant vs Child Occupant (Regresyon Analizi)")
    plt.xlabel("Adult Occupant Score")
    plt.ylabel("Child Occupant Score")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

    # Regresyon katsayıları
    print(f"Regresyon Denklem: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
    print(f"R-Kare Değeri: {model.score(X, y):.2f}")


    #GRAFİK 4 YILLARA GÖRE GÜVENLİK ORTALAMASINDAKİ DEĞİŞİM
    file_path = 'euroncap.csv'  
    data = pd.read_csv(file_path)

    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    data_split["Overall Rating"] = pd.to_numeric(data_split["Overall Rating"], errors="coerce")
    data_split["Year"] = pd.to_numeric(data_split["Year"], errors="coerce")

    # Yıllara göre ortalama Overall Rating hesaplama
    yearly_avg_rating = data_split.groupby("Year")["Overall Rating"].mean()

    # Çizgi grafiği oluşturma
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_avg_rating.index, yearly_avg_rating.values, marker="o", linestyle="-", color="b")
    plt.title("Yıllara Göre Güvenlik Ortalamasındaki Değişim")
    plt.xlabel("Yıl")
    plt.ylabel("Ortalama Güvenlik Puanı")
    plt.grid(alpha=0.3)
    plt.xticks(yearly_avg_rating.index, rotation=45)
    plt.tight_layout()
    plt.show()

    #GRAFİK 5 YILDIZ PUANLARINA GÖRE ARAÇ SAYISI DAĞILIMI HİSTOGRAMI
    ##########################################
    file_path = 'euroncap.csv'  
    data = pd.read_csv(file_path)

    # Veriyi sütunlara ayırın
    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    data_split["Overall Rating"] = pd.to_numeric(data_split["Overall Rating"], errors="coerce")

    # Histogram oluşturma
    plt.figure(figsize=(10, 6))
    plt.hist(data_split["Overall Rating"].dropna(), bins=range(1, 7), align="left", color="skyblue", edgecolor="black")
    plt.title("Yıldız Puanlarına Göre Araç Sayısı Dağılımı")
    plt.xlabel("Yıldız Puanı (Overall Rating)")
    plt.ylabel("Araç Sayısı")
    plt.xticks(range(1, 6))  # Yıldız puanları 1'den 5'e
    plt.grid(axis="y", alpha=0.3)
    plt.show()

    #GRAFİK 6 SINIFLARA GÖRE ARAÇ SAYISI
    ##################################################################
    file_path = 'euroncap.csv'  
    data = pd.read_csv(file_path)

    # Veriyi sütunlara ayırın
    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sınıflara göre araç sayısını hesaplama
    class_counts = data_split["Class"].value_counts()

    # Bar grafiği oluşturma
    plt.figure(figsize=(12, 6))
    class_counts.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Araç Sayılarının Sınıflara Göre Dağılımı")
    plt.xlabel("Araç Sınıfı")
    plt.ylabel("Araç Sayısı")
    plt.xticks(rotation=45)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()
    #GRAFİK 7 KORELASYON ANALİZİ
    ###########################################
    file_path = 'euroncap.csv'  # Dosya yolunuzu kontrol edin
    data = pd.read_csv(file_path)

    # Veriyi sütunlara ayırın
    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    numeric_columns = ["Adult Occupant", "Child Occupant", "Vulnerable Road Users", "Safety Assist", "Overall Rating"]
    for col in numeric_columns:
        data_split[col] = pd.to_numeric(data_split[col], errors="coerce")

    # Korelasyon matrisi
    correlation_matrix = data_split[numeric_columns].corr()

    # Heatmap ile görselleştirme
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Korelasyon Matrisi (Heatmap)")
    plt.show()
    redirect_to_menu(5)

def en_guvenli_ve_en_guvensiz_markalar(df):
    ortalama_puanlar = df.groupby('Make')['Overall Rating'].mean()
    
    en_guvenli_marka = ortalama_puanlar.idxmax()
    print("En güvenli marka:", en_guvenli_marka)

    en_guvensiz_marka = ortalama_puanlar.idxmin()
    print("En güvensiz marka:", en_guvensiz_marka)
    print("Not: Verisetindeki EuroNCAP yıldızları ortalaması alınarak belirlenmiştir.")

df = pd.read_csv("euroncap.csv", sep=";")


def reports():
    print("RAPORLAR\n----------------------")
    print("En Güvenli Ve En Güvensiz Markalar:")
    en_guvenli_ve_en_guvensiz_markalar(df)
    time.sleep(1)
    print("\nMOD,MEDYAN VE DİĞER DEĞERLER\n-----------------------")
    for column in df.select_dtypes(include=['int64', 'float64']).columns:
        print(f"Sütun: {column}")
        print(f"Ortalama: {df[column].mean()}")
        print(f"Medyan: {df[column].median()}")
        print(f"Mod: {df[column].mode()}")
        print(f"Standart Sapma: {df[column].std()}")
        print(f"Varyans: {df[column].var()}\n")
        time.sleep(1)
    print("SUV ve SUV Olmayan Araçlara Göre t-Testi\n---------------------------------------------")
    file_path = 'euroncap.csv'
    data = pd.read_csv(file_path)

    # Veriyi sütunlara ayırın
    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    data_split["Adult Occupant"] = pd.to_numeric(data_split["Adult Occupant"], errors="coerce")

    # SUV ve Non-SUV Grupları Oluşturma
    data_split["Group"] = data_split["Class"].apply(lambda x: "SUV" if "SUV" in x else "Non-SUV")

    # Grupları Filtreleme
    suv_scores = data_split[data_split["Group"] == "SUV"]["Adult Occupant"].dropna()
    non_suv_scores = data_split[data_split["Group"] == "Non-SUV"]["Adult Occupant"].dropna()

    # Gruplardaki Veri Sayısını Kontrol Et
    print("SUV Veri Sayısı:", len(suv_scores))
    print("Non-SUV Veri Sayısı:", len(non_suv_scores))

    # t-Testi
    if len(suv_scores) > 1 and len(non_suv_scores) > 1:
        t_stat, p_value = ttest_ind(suv_scores, non_suv_scores)
        print(f"t-İstatistiği: {t_stat:.2f}")
        print(f"p-Değeri: {p_value:.5f}")
        if p_value < 0.05:
            print("Sonuç: SUV ve Non-SUV araçlar arasında istatistiksel olarak anlamlı bir fark var.\n")
        else:
            print("Sonuç: SUV ve Non-SUV araçlar arasında anlamlı bir fark yok.\n")
    else:
        print("Yeterli veri yok. Gruplardan birinin örneklem boyutu çok küçük.")
    print("Araç Sınıfı ile Yıldız Puanı Arasındaki Ki-Kare Testi\n-----------------------------------------------------------")
    time.sleep(2)
    file_path = 'euroncap.csv'
    data = pd.read_csv(file_path)

    # Veriyi sütunlara ayırın
    columns = [
        "Origin",
        "Make",
        "Model",
        "Year",
        "Adult Occupant",
        "Child Occupant",
        "Vulnerable Road Users",
        "Safety Assist",
        "Class",
        "Overall Rating",
    ]
    data_split = data.iloc[:, 0].str.split(";", expand=True)
    data_split.columns = columns

    # Sayısal verilere dönüştürme
    data_split["Overall Rating"] = pd.to_numeric(data_split["Overall Rating"], errors="coerce")

    # Sınıf ve Yıldız Puanı için çapraz tablo oluşturma
    contingency_table = pd.crosstab(data_split["Class"], data_split["Overall Rating"])

    # Ki-Kare Testi
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Sonuç
    print(f"Ki-Kare Değeri: {chi2:.2f}")
    print(f"p-Değeri: {p:.5f}")
    if p < 0.05:
        print("Sonuç: Araç sınıfı ile yıldız puanı arasında anlamlı bir ilişki var.")
    else:
        print("Sonuç: Araç sınıfı ile yıldız puanı arasında anlamlı bir ilişki yok.")
    redirect_to_menu(3)
        
def dataset():
    df = pd.read_csv("euroncap.csv", sep=";")
    pd.set_option('display.max_rows', None)
    print(df)
    redirect_to_menu(2)


def menu():
    title = "Euro NCAP VERİ SETİ\n-----------------------------"
    menu_text = """1. Konu Özeti
2. Veri Setini Göster
3. Raporlar
4. Grafikler"""
    print(title)
    print(menu_text)

    while True:
        try:
            secim = int(input("Seçim yapınız: "))
            if secim == 1:
                clear()
                summary()
                break
            elif secim == 2:
                clear()
                dataset()
                break
            elif secim == 3:
                clear()
                reports()
                break
            elif secim == 4:
                clear()
                graphics()
                break
            else:
                print("Yanlış seçim yaptınız. Lütfen 1-4 arasında bir değer giriniz.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı giriniz.")

          

def summary():
    print("KONU ÖZETİ\n----------------")
    ozet = """Genel Bakış
Bu veri seti, Avrupa Yeni Otomobil Değerlendirme Programı (Euro NCAP) tarafından gerçekleştirilen çarpışma testlerinin sonuçlarını içermektedir. Veri setinde, farklı marka ve modellerdeki araçların çeşitli çarpışma senaryolarındaki performansları, güvenlik özellikleri ve elde ettikleri yıldız dereceleri yer almaktadır. Bu veri seti, otomobil güvenliği konusunda çalışmalar yapan araştırmacılar, mühendisler ve tüketiciler için değerli bir kaynak niteliğindedir.

Veri Setinin Kapsamı
Veri seti, 1997-2024 arasında Euro NCAP tarafından test edilen 773 farklı araç modelini içermektedir.
Veri setindeki değişkenler arasında araç markası, modeli, üretim yılı, yetişkin yolcu güvenliği, çocuk yolcu güvenliği,güvenlik asistanı analizi, yaya güvenliği ve genel yıldız derecesi bulunmaktadır. 
Bu kapsamlı veri seti, otomobil güvenliği ile ilgili çeşitli analizler yapma imkanı sunmaktadır.

Veri Setinin Amaçları
Bu veri seti, aşağıdaki amaçlarla oluşturulmuştur:

Otomobil güvenliği trendlerini analiz etmek
Farklı araç segmentleri arasındaki güvenlik performanslarını karşılaştırmak
Güvenlik özellikleri ile yıldız derecesi arasındaki ilişkiyi incelemek
Tüketicilere araç seçimlerinde güvenilir bir veri kaynağı sunmak
Otomobil üreticilerine güvenlik iyileştirmeleri için veri desteklemek

Veri Setinin Potansiyel Kullanım Alanları
Bu veri seti, aşağıdaki alanlarda kullanılabilir:

Araştırma: Otomobil güvenliği, istatistik, veri madenciliği gibi alanlarda akademik çalışmalara temel oluşturmak
Endüstri: Otomobil üreticileri tarafından yeni ürün geliştirme ve mevcut ürünlerin iyileştirilmesi süreçlerinde
Hükümet: Otomobil güvenliği düzenlemeleri ve politikaları oluşturmak için
Sivil toplum kuruluşları: Tüketici bilinçlendirme çalışmaları yapmak için
Medya: Otomobil güvenliği ile ilgili haber ve analizler hazırlamak için
"""
    print(ozet)
    redirect_to_menu(3)

if __name__ == '__main__':           
    menu()
