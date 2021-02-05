import sys
sys.path.append('.')

from flask import Flask
from flask_restful import Api

from src.view.api.resources.product_resource import ProductResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/api/product', endpoint='products')
api.add_resource(ProductResource, '/api/product/<int:id_>', endpoint='product')

app.run(debug=True)