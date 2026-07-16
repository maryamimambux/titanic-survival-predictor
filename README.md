<div align="center">

# 🚢 Titanic Survival Predictor

**A machine learning web app that predicts whether a Titanic passenger would have survived — trained on real historical passenger records.**

[![Live Demo](https://img.shields.io/badge/🌊_Live_Demo-Visit_App-0B1F3A?style=for-the-badge)](https://titanic-survival-predictor-gamma.vercel.app)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-C9A227?style=flat-square)

**[🔗 Try it live → titanic-survival-predictor-gamma.vercel.app](https://titanic-survival-predictor-gamma.vercel.app)**

</div>

---

## 📖 What is this?

On April 15, 1912, the Titanic sank — and survival wasn't random. Passenger class, age, sex, and family size all quietly shaped who made it and who didn't.

This project trains a machine learning model on real passenger records from the Titanic, then wraps that model in a live web app: enter any hypothetical passenger's details, and get an instant prediction of whether they'd have survived.

> Enter a passenger's class, sex, age, fare, and family details → the model predicts **Survived** or **Did not survive**, based on patterns learned from 891 real passengers.

---

## ✨ Features

- 🧠 **Trained ML model** (Random Forest, tuned via grid search + cross-validation)
- 🌐 **Live interactive web app** built with Flask
- 📊 **Evaluated properly** — not just accuracy, but precision, recall, and F1
- 🎨 **Clean, custom UI** — no default Bootstrap look
- ☁️ **Deployed for free**, fully reproducible via a pinned `requirements.txt`

---

## 🖥️ Try It Yourself

<div align="center">

**👉 [titanic-survival-predictor-gamma.vercel.app](https://titanic-survival-predictor-gamma.vercel.app) 👈**

</div>

Fill in a passenger's class, sex, age, fare, and family details, then click **Predict outcome**.

---

## 🛠️ How It Was Built

| Stage | What Happened |
|---|---|
| **1. Data** | [Titanic dataset](https://github.com/datasciencedojo/datasets) — 891 real passenger records |
| **2. EDA** | Explored survival patterns by class, sex, and family size |
| **3. Cleaning** | Handled missing `Age`/`Embarked`, encoded categorical features |
| **4. Baseline model** | Logistic Regression → **F1: 0.764** |
| **5. Cross-validation** | 5-fold CV for an honest performance estimate → **Average F1: 0.719** |
| **6. Model tuning** | Random Forest + `GridSearchCV` → **Tuned F1: 0.752** |
| **7. Deployment** | Flask app, version-pinned dependencies, deployed on Vercel |

**Final model performance (test set):**

| Metric | Score |
|---|---|
| Accuracy | 81% |
| Precision | 79% |
| Recall | 74% |
| F1 Score | 0.752–0.764 |

---

## ⚙️ Tech Stack

`Python` · `pandas` · `scikit-learn` · `Flask` · `Vercel`

---

## 🚀 Run It Locally

```bash
git clone https://github.com/maryamimambux/titanic-survival-predictor.git
cd titanic-survival-predictor
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## 📁 Project Structure

```
titanic-survival-predictor/
├── app.py                 # Flask app
├── titanic_model.pkl      # Trained Random Forest model
├── requirements.txt       # Pinned dependencies
├── train_model.ipynb      # Full training notebook (EDA → tuning)
└── templates/
    └── index.html         # Frontend
```

---

<div align="center">

### 👤 About

**Maryam Imam**

[![GitHub](https://img.shields.io/badge/GitHub-maryamimambux-181717?style=flat-square&logo=github)](https://github.com/maryamimambux)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maryam_Imam-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/maryam-imam-394455342/)

*Built as a hands-on machine learning project — from raw data to a live deployed app.*

</div>
