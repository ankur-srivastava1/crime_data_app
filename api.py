import os
import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

import query_data

app = Flask(__name__)
CORS(app)
api = Api(app)

# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("city")
parser.add_argument("start_time")
parser.add_argument("end_time")

class queryData(Resource):
    def post(self):
        args = parser.parse_args()
        city = args["city"]
        start_time = args["start_time"]
        end_time = args["end_time"]
        
        return {'data': query_data.get_crime_data(city, start_time, end_time)}

api.add_resource(queryData, "/data")
if __name__ == "__main__":
  app.run(debug=True)