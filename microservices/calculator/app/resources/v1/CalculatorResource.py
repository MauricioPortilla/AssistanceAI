from flask_restful import Resource

class CalculatorResource(Resource):
    def get(self, operation, num1, num2):
        return { "status": "success", "data": "Calculator response" }, 200
