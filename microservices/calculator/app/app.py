from flask import Flask, Blueprint, request
from flask_restful import Api
from resources.v1.CalculatorResource import CalculatorResource as CalculatorResourceV1

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(CalculatorResourceV1, "/v1/calcualtor/<operation>/<num1>/<num2>")
