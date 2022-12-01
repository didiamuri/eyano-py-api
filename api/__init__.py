from flask_restful import Api
from api.Graph.views import GraphImage
from api.Network.views import NetworkGraphList
from app import flaskAppInstance

api = Api(flaskAppInstance)
api.add_resource(NetworkGraphList,'/api/v1/network/graph')
api.add_resource(GraphImage, '/api/v1/graph/<string:image>')