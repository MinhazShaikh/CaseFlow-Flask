import pickle
import json
from flask import Flask, request, jsonify

# Load the pre-trained model
with open('model1.pkl', 'r') as models:
    model = pickle.load(models)

# with open('model.pkl','w') as json_file:
#     json.dump(model,json_file)

# print(json_file)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()

        # Ensure that the input data matches the features expected by the model
        # You may need to preprocess the data here

        # Make predictions using the loaded model
        predictions = model.predict(data)

        # Return the predictions as a JSON response
        return jsonify({'predictions': predictions.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})