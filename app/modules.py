from app.config import Config
from pymysql import connect,cursors

from app.repositories.clientRepository import ClientRepository
from app.services.clientService import ClientService

connection = connect(host=Config.HOST,
                     port= Config.PORT,
                     user= Config.USER,
                     password= Config.PASSWORD,
                     db= Config.DB,
                     cursorclass=cursors.DictCursor)

clientRepository = ClientRepository(connection)
clientService = ClientService(clientRepository)