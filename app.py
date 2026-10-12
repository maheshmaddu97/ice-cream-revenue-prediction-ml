import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle

with open('revenue_project.PKL', 'rb') as f:
    m = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    temp = float(data['temp'])

    values = [temp]
    values = np.array(values)

    sol = m.predict([values])[0]

    return jsonify({
        'prediction': float(sol)
    })

if __name__ == '__main__':
    app.run(debug=True)
