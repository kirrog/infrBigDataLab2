from flask import Flask, request

from src.loggers import create_logger
from src.predict import Predictor

cstm_logger = create_logger(__name__)

app = Flask(__name__)


@app.route('/')
def check():
    return 'Flask is running!'


@app.route('/predict', methods=['POST'])
def predict_by_model():
    data = request.json
    model = Predictor()
    area = float(data["area"])
    perimeter = float(data["perimeter"])
    compactness = float(data["compactness"])
    kernel_length = float(data["kernel_length"])
    kernel_width = float(data["kernel_width"])
    asymmetry_coeff = float(data["asymmetry_coeff"])
    kernel_groove = float(data["kernel_groove"])
    floats = [[area, perimeter,
               compactness, kernel_length,
               kernel_width, asymmetry_coeff,
               kernel_groove]]
    y_result_data = model.predict_by_model(floats)
    cstm_logger.info(y_result_data)
    return f'{y_result_data}'


if __name__ == '__main__':
    app.run(debug=True)
