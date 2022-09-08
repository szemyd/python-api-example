from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)



class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code
    
class Locations(Resource):
    # methods go here
    pass
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations


if __name__ == '__main__':
    app.run()  # run our Flask app
