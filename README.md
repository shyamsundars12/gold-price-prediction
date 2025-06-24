# 🟡 Gold Price Prediction

An interactive machine learning app built with **Streamlit** that predicts the price of gold (per gram) based on the USD to INR exchange rate using a trained regression model.

## 📸 Demo

🔗 **Live App**: [Click to Try on Streamlit Cloud](https://shyamsundars12-gold-price-prediction-app-nydva6.streamlit.app/)

## 📊 Overview

This project demonstrates how **machine learning** can be used to predict gold prices using just the **USD-INR exchange rate**. It uses:
- 💻 `Streamlit` for a sleek and interactive web UI
- ⚙️ A pre-trained regression model (`regressor.pkl`)
- 📏 Feature scaling using `StandardScaler` (`scaler.pkl`)

---

## 🧰 Features

✔️ Simple, clean UI for inputting USD-INR  
✔️ Real-time prediction of gold price  
✔️ Powered by trained `LinearRegression` model  
✔️ Model and scaler are saved and reused (`.pkl` files)

---

## 🛠️ Project Structure

gold-price-prediction/
├── app.py # Main Streamlit app
├── scaler.pkl # Saved StandardScaler
├── regressor.pkl # Trained regression model
├── train_model.py # Script to train the model
├── gold_vs_usdinr.csv # Input data for training
└── requirements.txt # Python dependencies
---
## ▶️ How to Run Locally

### 1️⃣ Clone the Repo

git clone https://github.com/shyamsundars12/gold-price-prediction.git
cd gold-price-prediction
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit App
streamlit run app.py
🧠 How it Works
The train_model.py script loads historical data (gold_vs_usdinr.csv)
It trains a LinearRegression model using the USD-INR rate to predict gold price
A StandardScaler is used to normalize input values
Both the model and scaler are saved as .pkl files
The Streamlit app (app.py) loads these .pkl files and predicts in real-time
📦 Requirements
streamlit
numpy
pandas
scikit-learn

Install them via:
pip install -r requirements.txt

🙋‍♂️ Author
Shyam Sundar
🔗 GitHub: https://github.com/shyamsundars12
If you found this project helpful, don’t forget to ⭐ star the repo and share it!
