from sqlalchemy.pool import QueuePool

from app.config import Config
from pymysql import connect,cursors

from repositories.clientRepository import ClientRepository
from repositories.companyRepository import CompanyRepository
from repositories.documentRepository import DocumentRepository
from repositories.itemRepository import ItemRepository
from repositories.productRepository import ProductRepository
from repositories.sdkAfipRepository import SdkAfipRepository
from services.clientService import ClientService
from services.companyService import CompanyService
from services.documentService import DocumentService
from services.productService import ProductService

def get_connection():
    try:
        connection = connect(host=Config.HOST,
                             port= Config.PORT,
                             user= Config.USER,
                             password= Config.PASSWORD,
                             db= Config.DB,
                             cursorclass=cursors.DictCursor)
    except Exception as e:
        connection = None
    return connection

pool_connection = QueuePool(get_connection, max_overflow=0, pool_size=5, recycle=3600)

clientRepository = ClientRepository(pool_connection)
clientService = ClientService(clientRepository)

productRepository = ProductRepository(pool_connection)
productService = ProductService(productRepository)

itemRepository = ItemRepository(pool_connection)

sdkAfipRepository = SdkAfipRepository(pool_connection)

companyRepository = CompanyRepository(pool_connection)
companyService = CompanyService(companyRepository, sdkAfipRepository)

documentRepository = DocumentRepository(pool_connection)
documentService = DocumentService(documentRepository, itemRepository, sdkAfipRepository, companyRepository, clientRepository,
                                  productRepository)
