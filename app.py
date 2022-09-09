from flask import Flask
from flask_restful import Api

from endpoints.users import  Users
from endpoints.locations import Locations

app = Flask(__name__)
api = Api(app)


api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations


# if __name__ == '__main__':
#     app.run()  # run our Flask app
    

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello Sammy!'