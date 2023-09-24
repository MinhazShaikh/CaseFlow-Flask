import pickle
from flask import Flask, request, jsonify
import json
import numpy as np 
import scheduleFun

app = Flask(__name__)

# Load the RandomForest Classifier model
# with open('model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

# @app.route('/')
# def home():
#     return 'Welcome to the RandomForest Classifier API!'

@app.route('/predict', methods=['POST'])
def predict():
    # try:
    #     # Get input data from the request
    #     input_data = request.get_json()

    #     # Ensure that you have the expected attributes in the input data
    #     # You may need to validate and preprocess the input data here

    #     # Example: Extracting attributes 'attr1', 'attr2', 'attr3', 'attr4', 'attr5'
    #     attr1 = input_data.get('attr1')
    #     attr2 = input_data.get('attr2')
    #     attr3 = input_data.get('attr3')
    #     attr4 = input_data.get('attr4')
    #     attr5 = input_data.get('attr5')

    #     # Make predictions using the loaded model
    #     predictions = model.predict([[attr1, attr2, attr3, attr4, attr5]])

    #     # Return the predictions as a JSON response
    #     return jsonify({'prediction': predictions[0]})

    # except Exception as e:
    #     return jsonify({'error': str(e)})
    # jsondata = {'values':[1,1,3,2,4]}

    requested_data = request.json['jsonData']
    # print(type(requested_data))
    # values=requested_data.values()
    # print(type(values))
    values_list = [values for values in requested_data.values()]
    input_data = np.array([values_list])
    model_loaded=pickle.load(open('save','rb'))
    answer = model_loaded.predict(input_data)
    answerlist = answer.tolist()
    # json_data = json.dumps(answerlist)
    # return json_data
    json_data = {"priority": answerlist[0]}
    # print(type(answerlist[0]))
    return jsonify(json_data)
    # modelSave=joblib.load('model.joblib')

@app.route('/schedule',methods = ['GET'])
def schedule():
    df = scheduleFun.call()
    return jsonify(df)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)