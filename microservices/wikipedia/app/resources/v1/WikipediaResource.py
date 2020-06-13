from flask_restful import Resource
import wikipedia

class WikipediaResource(Resource):
    def get(self, search):
        wikipedia.set_lang("es")
        result = wikipedia.summary(search, sentences=3)
        return { "status": "success", "data": result }, 200
