from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('titanic_model.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
    pclass = int(request.form['pclass'])
    sex = request.form['sex']
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    embarked_q = int(request.form['embarked_q'])
    embarked_s = int(request.form['embarked_s'])

    sex_num = 0 if sex == "female" else 1

    features = np.array([[pclass, sex_num, age, sibsp, parch, fare,
                           embarked_q, embarked_s]])

    result = model.predict(features)[0]
    prediction = "Survived" if result == 1 else "Did not survive"

    return render_template('index.html', prediction=prediction)

"""
@app.route('/predict', methods=['POST'])
def predict():
    pclass = int(request.form['pclass'])
    sex = request.form['sex']
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    embarked_q = int(request.form['embarked_q'])
    embarked_s = int(request.form['embarked_s'])

    sex_num = 0 if sex == "female" else 1  # matches LabelEncoder's alphabetical order from Step 3
    family_size = sibsp + parch + 1
    is_alone = 1 if family_size == 1 else 0

    features = np.array([[pclass, sex_num, age, sibsp, parch, fare,
                           embarked_q, embarked_s, family_size, is_alone]])

    result = model.predict(features)[0]
    prediction = "Survived" if result == 1 else "Did not survive"

    return render_template('index.html', prediction=prediction)
"""
    
if __name__ == '__main__':
    app.run(debug=True)