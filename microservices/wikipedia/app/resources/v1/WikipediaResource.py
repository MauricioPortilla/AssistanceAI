from flask_restful import Resource

class WikipediaResource(Resource):
    def get(self, search):
        return { "status": "success", "data": "Wikipedia response" }, 200
