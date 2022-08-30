
from flask import Flask, jsonify,request
from project_app.utils import MedicalInsurance
import config

app = Flask(__name__)

@app.route('/') 
def hello_flask():
    print("Welcome to Flask")
    return "Welcome to Flask"


@app.route('/predict_charges')
def get_insurance_charges():

    print("We are using GET method")
    data = request.form
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predicted_charges()

    return jsonify({"Result": f"Predicted Medical Insurance Charges are : {charges}"})

if __name__ == "__main__":    
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)