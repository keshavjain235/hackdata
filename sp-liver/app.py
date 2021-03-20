# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['Age'])
        glucose = int(request.form['Gender'])
        bp = int(request.form['Total_Bilirubin'])
        st = int(request.form['Direct_Bilirubin'])
        insulin = int(request.form['Alkaline_Phosphotase'])
        bmi = float(request.form['Alamine_Aminotransferase'])
        dpf = float(request.form['Aspartate_Aminotransferase'])
        age = int(request.form['Total_Protiens'])
        dataa = int(request.form['Albumin'])
        datab = int(request.form['Albumin_and_Globulin_Ratio'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)