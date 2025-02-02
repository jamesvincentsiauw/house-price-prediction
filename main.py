from flask import Flask, request, jsonify
from controller import process_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict_price():
   json_data = request.form.to_dict(flat=False)
   result = process_data(json_data)
   return jsonify(result), result['status']

if __name__ == "__main__":
    app.run(host='0.0.0.0')