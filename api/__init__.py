from flask_restful import Api
from api.Customer.views import CustomerGraph
from app import flaskAppInstance

api = Api(flaskAppInstance)
api.add_resource(CustomerGraph,'/api/v1/customer/graph')