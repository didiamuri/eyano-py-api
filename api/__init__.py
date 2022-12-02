from flask_restful import Api
from api.Customer.views import CustomerGraph
from application import application

api = Api(application)
api.add_resource(CustomerGraph,'/api/v1/customer/graph')