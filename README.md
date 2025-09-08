# 🦠 COVID-19 Dashboard  
https://covid19-dashboard-1-kinq.onrender.com/

---

## 📌 Overview
This project is an **interactive COVID-19 dashboard** built to analyze and visualize the impact of the pandemic across countries and time periods.  
The dashboard provides **real-time insights** into confirmed cases, deaths, recoveries, and testing data using interactive charts and visualizations.

---

## 🛠️ Tools & Technologies
- **Python**
  - `pandas`, `numpy` → Data cleaning & preprocessing  
  - `plotly`, `matplotlib`, `seaborn` → Data visualization  
  - `dash` / `streamlit` → Interactive dashboard  
- **SQL** (if applicable) for structured queries  
- **Jupyter Notebook** for experimentation and EDA  
- **CSV / API datasets** (Johns Hopkins, WHO, or Kaggle sources)

---

## ⚙️ Features
✔️ Interactive dashboard for COVID-19 trends  
✔️ Country & date-wise filtering  
✔️ Daily vs. cumulative case visualization  
✔️ Heatmaps and trend lines for global spread  
✔️ Mortality & recovery analysis  
✔️ Exportable charts and insights  

---

## 📂 Project Structure
```
covid19-dashboard/
│── data/                 # Raw and cleaned datasets
│── notebooks/            # Jupyter notebooks for EDA
│── app.py / dashboard.py # Main dashboard script
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## 🚀 How to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/ranavikas1998/covid19-dashboard.git
   cd covid19-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run app.py
   ```
   or (if using Dash):
   ```bash
   python app.py
   ```

4. Open the given **local URL** in your browser.

---

## 📊 Output
- **Global summary cards** (Confirmed, Recovered, Deaths, Active)  
- **Line charts** showing daily & cumulative cases  
- **Bar plots** for top affected countries  
- **Heatmap / Choropleth map** to visualize spread  
- **Interactive filters** for countries & time periods  

---

## 📥 Data Sources
- Kaggle COVID-19 dataset

---

## 🤝 Contribution
Contributions are welcome!  
- Fork the repo  
- Create a new branch (`feature/your-feature`)  
- Commit changes and open a Pull Request  

---

✍️ Author: **Vikas Rana**  
📅 Year: 2025  
