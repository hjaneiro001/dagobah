
from flask import Blueprint
from flask import request, jsonify
from app.dtos.requestProductDto import RequestProductDTO
from app.dtos.responseProductDto import ResponseProductDTO
from app.entities.product import Product, ProductBuilder

from app.exceptions.wrapperExceptions import handle_exceptions
from app.modules import productService

productsBp = Blueprint('products', __name__)

@productsBp.route("/", methods=['GET'])
@handle_exceptions
def get_all():
    products :list[Product] = productService.get_all()
    products_data = [product.to_dict() for product in products]
    response = ResponseProductDTO(many=True).dump(products_data)
    return jsonify(response), 200
