
from app.config import Config
from pymysql import connect,cursors

from app.repositories.clientRepository import ClientRepository
from app.repositories.productRepository import ProductRepository
from app.services.clientService import ClientService
from app.services.productService import ProductService

connection = connect(host=Config.HOST,
                     port= Config.PORT,
                     user= Config.USER,
                     password= Config.PASSWORD,
                     db= Config.DB,
                     cursorclass=cursors.DictCursor)

clientRepository = ClientRepository(connection)
clientService = ClientService(clientRepository)

productRepository = ProductRepository(connection)
productService = ProductService(productRepository)