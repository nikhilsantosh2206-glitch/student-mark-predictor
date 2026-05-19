# Student Mark Predictor 🎓📊

An end-to-end Machine Learning web application that predicts a student's marks or percentage based on the number of hours they study. The core model is built using **Linear Regression** and served via a **Flask** backend.

## 🔗 Live Project Link
*Check out the live running application here:* [Add your Render Live URL here]

---

## ✨ Features
- **Instant Predictions:** Input study hours and get the predicted marks in real-time.
- **Data-Driven:** Trained on clean student academic performance datasets.
- **Lightweight Backend:** Built with Flask for rapid request-response handling.
- **Production Ready:** Pre-packaged with `gunicorn` for seamless deployment on Render.

---

## 🛠️ Technology Stack
- **Languages:** Python, HTML, CSS
- **Data Science / ML:** Jupyter Notebook, Scikit-Learn, Pandas, NumPy
- **Web Framework:** Flask
- **Deployment & Hosting:** Render / GitHub

---

## 📂 Project Directory Structure
```text
├── student_mark_predictor.ipynb  # Jupyter Notebook for Model Training
├── student_mark_predictor.pkl    # Serialized Trained Machine Learning Model
├── Desktop.pkl                   # Backup Model File
├── app1.py                        # Main Flask Application Code
├── flask practise.py              # Practice script / experimental routes
├── requirements.txt               # App dependencies & python packages
├── student_info.csv               # Dataset used for training
├── smp_data_from_app.csv          # Logged dataset from application inputs
└── README.md                      # Project documentation
```

---

## 🚀 Local Installation & Setup

To run this application locally on your computer, follow these simple steps:

1. **Download the code:**
   Download the repository ZIP file from GitHub and extract it, or run:
   ```bash
   git clone https://github.com
   cd student-mark-predictor
   ```

2. **Install Required Libraries:**
   Make sure you have Python installed. Open your terminal inside the project folder and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask App:**
   Execute the main python script:
   ```bash
   python app1.py
   ```
   Open your browser and navigate to `http://127.0.0` to view your project locally.

---

## ☁️ Deployment Configurations (For Render)
If you are deploying this repository on Render, use the following exact configurations to prevent build errors:
- **Environment/Language:** `Python`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app1:app`
