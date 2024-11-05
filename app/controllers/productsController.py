
from flask import Blueprint
from flask import request, jsonify
from app.dtos.requestProductDto import RequestProductDTO
from app.dtos.responseProductDto import ResponseProductDTO
from app.entities.enums.currency import Currency
from app.entities.enums.productIva import ProductIva
from app.entities.enums.productType import ProductType
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

@productsBp.route("/<int:id>")
@handle_exceptions
def get_id(id :int):
    product: Product = productService.get_id(id)
    result = ResponseProductDTO().dump(product.to_dict())
    return jsonify(result), 200

@productsBp.route("/code/<string:code>")
@handle_exceptions
def get_code(code :str):
    product: Product = productService.get_code(code)
    result = ResponseProductDTO().dump(product.to_dict())
    return jsonify(result), 200

@productsBp.route("/", methods=['POST'])
@handle_exceptions
def create():
    request_product_dto = RequestProductDTO().load(request.json)
    product = (ProductBuilder()
               .code(request_product_dto['code'])
               .bar_code(request_product_dto['bar_code'])
               .name(request_product_dto['name'])
               .description(request_product_dto['description'])
               .pack(request_product_dto['pack'])
               .price(request_product_dto['price'])
               .currency(Currency.get_currency(request_product_dto['currency']))
               .iva(ProductIva.get_product_iva(request_product_dto['iva']))
               .product_type(ProductType.get_product_type(request_product_dto['product_type']))
               .build())

    product_id: int = productService.create(product)
    return jsonify({"product_id" : product_id}), 201


@productsBp.route("/<int:id>", methods=['PUT'])
@handle_exceptions
def modify(id :int):
    modify_product_dto = RequestProductDTO().load(request.json)
    product = (ProductBuilder()
               .code(modify_product_dto['code'])
               .bar_code(modify_product_dto['bar_code'])
               .name(modify_product_dto['name'])
               .description(modify_product_dto['description'])
               .pack(modify_product_dto['pack'])
               .price(modify_product_dto['price'])
               .currency(Currency.get_currency(modify_product_dto['currency']))
               .iva(ProductIva.get_product_iva(modify_product_dto["iva"]))
               .product_type(ProductType.get_product_type(modify_product_dto['product_type']))
               .build())

    productService.modify(id, product)

    return jsonify({"message": "Product modify successfully"}), 200

@productsBp.route("/<int:id>", methods=['DELETE'])
@handle_exceptions
def delete(id :int):
    productService.delete((id))
    return jsonify({"message": "Product deleted successfully"}), 200