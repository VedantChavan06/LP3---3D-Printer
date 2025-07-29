from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('fault_predictor.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        pred = model.predict([[x, y, z]])[0]
        result = "⚠️ Fault Detected" if pred else "✅ Normal"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)