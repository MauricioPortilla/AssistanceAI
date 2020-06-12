from flask import Flask, Blueprint, request
from flask_restful import Api
from resources.v1.WikipediaResource import WikipediaResource as WikipediaResourceV1

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(WikipediaResourceV1, "/v1/wikipedia/<search>")
