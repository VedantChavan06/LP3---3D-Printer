# 📦 3D Printer Fault Prediction Using Machine Learning

This project uses machine learning to predict faults in 3D printing based on ADXL345 accelerometer sensor data (X, Y, Z directions). It includes a trained model and a Flask-based web app to make real-time predictions.

---

## 🚀 Features
- Predicts faults during 3D printing using motion data.
- Web interface to input sensor values.
- Reduces material waste and improves print reliability.

---

## 🧠 Machine Learning Model
- **Input**: `X-direction`, `Y-direction`, `Z-direction` (from ADXL345)
- **Output**: `Fault` (0 = Normal, 1 = Fault)
- **Algorithm**: Random Forest Classifier
- **Dataset**: `ADXL345_SensorData.csv`

---

## 📁 Project Structure
```
3d_printer_fault_prediction/
├── app.py
├── train_model.py
├── fault_predictor_adxl345.pkl
├── printer_movement_data.csv
├── templates/
│   └── index.html
```

---

## 🛠️ How to Run

### 1. Install dependencies
```bash
pip install flask pandas scikit-learn joblib
```

### 2. Train the model (optional)
```bash
python train_model.py
```

### 3. Run the web app
```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 📊 Example Input
```
X: 0.12
Y: 1.01
Z: -9.02
```

**Result**: ✅ Normal or ⚠️ Fault Detected

---

## 📈 Model Performance
- Accuracy: ~77%
- Precision (Fault): ~85%
- Recall (Fault): ~85%

---

## 📌 Future Scope
- Add 3D movement graph
- Use LSTM for time-sequence prediction
- Real-time data collection from printer

---

## 📄 License
Academic/Research use only. Modify freely for learning purposes.
