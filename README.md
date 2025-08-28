# 📊 Math Score Prediction Model

Unlocking **educational insights** through advanced analytics.  
This project predicts **student mathematics performance** using socio-demographic and academic factors, providing a tool for **early intervention** and **personalized learning strategies**.

---

## 🎯 Problem Statement

Educational institutions often struggle to identify students **at risk of poor mathematics performance**.  
Our regression-based model leverages socio-demographic and academic features to predict math scores, enabling educators to:

- Detect students needing additional support.  
- Design personalized learning strategies.  
- Make **data-driven decisions** to improve overall learning outcomes.  

---

## 🔬 Model Approach

- Uses **regression techniques** to model relationships between student characteristics and math performance.  
- Considers **demographics, parental education, lunch program status, test preparation**, and other academic indicators.  
- Provides accurate predictions and interpretable insights into factors influencing mathematics achievement.  

---

## 📂 Dataset Overview & Features

The dataset contains student demographic and academic details. Key features:

- 👤 **Gender** – Male vs Female performance patterns.  
- 🌍 **Race/Ethnicity Groups** – 5 groups (A–E).  
- 🎓 **Parental Education Level** – From "some high school" to "master's degree".  
- 🍽️ **Lunch Program** – Standard vs free/reduced (proxy for socioeconomic status).  
- 📚 **Test Preparation Course** – Completed vs not completed.  
- 📈 **Multi-Subject Scores** – Math, Reading, Writing (for correlation analysis).  

**Stats**:
- `8` features  
- `32+` samples (extendable dataset)  
- Score range: `0–100`  
- `5` ethnic groups  

---

## 🛠️ Tech Stack

- **Python** 🐍  
- **Flask** (Web app)  
- **Pandas, NumPy** (Data processing)  
- **Scikit-learn** (ML model building)  
- **Matplotlib, Seaborn** (Visualization)  

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/math-score-prediction.git
   cd math-score-prediction
