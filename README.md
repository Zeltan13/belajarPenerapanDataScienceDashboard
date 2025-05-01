# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

### Latar Belakang
Jaya Jaya Maju adalah perusahaan multinasional dengan lebih dari 1.000 karyawan di seluruh Indonesia. Meskipun terus berkembang, perusahaan menghadapi masalah serius dengan tingkat attrition (turnover) karyawan yang tinggi (>10%). Tim HR membutuhkan solusi untuk memahami penyebab utama dan mengambil tindakan yang tepat.


### Permasalahan

Apa saja faktor utama yang memengaruhi tingginya attrition di Jaya Jaya Maju?

### Tujuan Proyek:

- Mengidentifikasi faktor-faktor kunci yang berhubungan dengan attrition.
- Membuat dashboard interaktif untuk monitoring dan insight HR.
- (Opsional) Mengembangkan model prediksi sederhana untuk risiko attrition.

### Kriteria Sukses:
- Identifikasi faktor utama penyebab attrition berhasil dilakukan
- Pembuatan Dashboard interaktif dan mudah dipahami telah disediakan untuk tim HR
- (Opsional) Model prediktif dengan akurasi yang cukup baik dikembangkan untuk membantu HR dalam upaya retensi karyawan secara proaktif

## Business Dashboard

Dashboard dibangun menggunakan **Metabase** dan mencakup:

- **Attrition by Department**
- **Attrition by Job Role**
- **Overtime vs Attrition**
- **Job Level, Income, Satisfaction vs Attrition**
- **Age, Tenure, Travel Frequency vs Attrition**
- **Income Gap (Attrited vs Stayed)**
- **Environment Satisfaction vs Attrition**

Ekspor database:
```
docker cp metabase:/metabase.db/metabase.db.mv.db ./
```
## Credentials Metabase:
- Email: root@mail.com
- Password: root123

## Insight Utama dari Dashboard

📉 **Fokus retensi pada Sales Representatives** – tingkat attrition tertinggi sebesar 28.99%<br>
🕒 **Kurangi lembur** – Karyawan yang bekerja lembur memiliki risiko attrition 3 kali lebih tinggi<br>
💸 **Gaji bukan segalanya** – Peran dengan gaji tinggi seperti Research Director tetap menunjukkan tingkat keluar yang tinggi meskipun bergaji lebih besar dibanding yang bertahan. Namun secara umum, gaji yang lebih rendah = attrition yang lebih tinggi<br>
📊 **Opsi Saham** – Skor Stock Option yang rendah sangat berkorelasi dengan kecenderungan untuk keluar<br>
👩‍💼 **Usia muda & kurang pengalaman** – Risiko attrition lebih tinggi pada karyawan muda dan kurang berpengalaman<br>

### Rekomendasi untuk HR

✅ **Luncurkan program retensi** khusus untuk Sales Representatives dan Lab Technicians<br>
🧭 **Tinjau dan optimalkan kebijakan lembur** untuk mencegah burnout<br>
📊 **Lakukan stay interviews** untuk karyawan dengan gaji tinggi guna memahami pemicu keluar non-finansial<br>
🧠 **Bangun sistem umpan balik keterlibatan** — seperti pulse survey dan sesi 1-on-1<br>
👥 **Investasi dalam pelatihan manajer** — terutama untuk membangun hubungan awal manajer-karyawan yang sehat<br>
📈 **Pantau peningkatan setiap kuartal** melalui dashboard ini dan sesuaikan strategi secara proaktif<br>


## Data Preparation & EDA
- Pembersihan data dari nilai NaN pada Attrition.
- Korelasi fitur numerik & visualisasi eksploratif.
- Visualisasi 15 fitur dengan korelasi tertinggi

## Modeling & Evaluation (Optional)

Model klasifikasi dibangun menggunakan algoritma **XGBoost (Extreme Gradient Boosting)** untuk memprediksi kemungkinan karyawan akan keluar dari perusahaan.

### Konfigurasi Model
Model dioptimasi menggunakan **GridSearchCV** dengan parameter:

- `learning_rate`: 0.005  
- `max_depth`: 5  
- `n_estimators`: 2000  
- `subsample`: 0.1  

Parameter terbaik dipilih berdasarkan skor **ROC AUC** menggunakan 3-fold cross-validation.

### Hasil Evaluasi

- **Akurasi**: 88%
- **ROC AUC**: 0.857
- **Confusion Matrix**:
 [[86  2]
 [11  7]]
- **Classification Report**:

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| 0 (Stay) | 0.89 | 0.98 | 0.93 |
| 1 (Attrited) | 0.78 | 0.39 | 0.52 |

Model sangat baik dalam mengidentifikasi karyawan yang bertahan (0), namun performa untuk memprediksi karyawan yang keluar (1) masih kurang dan masih bisa ditingkatkan lagi.

### Fitur Penting dari Model (Feature Importance)

Berdasarkan grafik feature importance, faktor-faktor yang paling berpengaruh adalah:

1. `OverTime_Yes`
2. `EducationField_Technical Degree`
3. `StockOptionLevel`
4. `Department_Sales`
5. `JobRole_Sales Representative`
6. `BusinessTravel_Travel_Frequently`
7. `JobLevel`
8. `EnvironmentSatisfaction`
9. `WorkLifeBalance`
10. `JobInvolvement`

## Kesimpulan

- Perusahaan perlu fokus pada karyawan muda, berpenghasilan rendah, dan yang sering lembur.
- Insight dari dashboard membantu HR dalam mengambil tindakan berbasis data.
- Strategi retensi yang ditargetkan berdasarkan jabatan, pengalaman, dan kepuasan kerja akan mengurangi attrition secara signifikan.


### Persiapan

Sumber data: employee_data.csv

Setup environment:

1. Buat dan aktifkan virtual environment (opsional)
```
python -m venv venv
source venv/bin/activate  # Gunakan 'venv\Scripts\activate' jika di Windows
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Jalankan Jupyter Notebook

### Tools yang digunakan:
- Python (Jupyter Notebook)
- Metabase (untuk membuat dashboard)
- Pandas, scikit-learn, XGBoost (untuk analisis dan modeling)
- Lihat requirements.txt untuk daftar pustaka.
