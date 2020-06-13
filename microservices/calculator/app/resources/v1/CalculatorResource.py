from flask_restful import Resource

class CalculatorResource(Resource):
    def get(self, operation, num1, num2):
        if operation == "suma":
            return { "status": "success", "data": (float(num1) + float(num2)) }, 200
        elif operation == "resta":
            return { "status": "success", "data": (float(num1) - float(num2)) }, 200
        elif operation == "multiplicación":
            return { "status": "success", "data": (float(num1) * float(num2)) }, 200
        elif operation == "división":
            if float(num2) == 0:
                return { "status": "failed", "message": "No se puede dividir por cero." }, 200
            return { "status": "success", "data": (float(num1) / float(num2)) }, 200
        else:
            return { "status": "failed", "message": "Esta operación es desconocida." }, 400
