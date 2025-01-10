
from sqlalchemy import QueuePool, values

from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.entities.document import Document, DocumentBuilder
from app.entities.enums.currency import Currency
from app.entities.enums.documentConcept import DocumentConcept
from app.entities.enums.documentType import DocumentType
from app.entities.enums.typeId import TypeId
from app.factories.documentDTOFactory import ResponseDocumentDtoFactory
from app.entities.enums.status import Status
from app.utils.connection_manager import ConnectionManager
from app.utils.cursor_manager import CursorManager

class DocumentRepository:

    def __init__(self, pool_connection: QueuePool):
        self.pool_connection: QueuePool = pool_connection

    def get_document(self, document :Document):
         with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = (f"SELECT * FROM documents WHERE number = %s AND pos = %s and "
                            f"document_type = %s AND status = %s")

                values = (document.number, document.pos, document.document_type.get_type(), Status.ACTIVE.get_value())

                cur.execute(sql,values)
                row = cur.fetchone()

                if not row:
                    return None

                return True

    def create(self, document :Document):
        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql :str = """ 
                INSERT INTO documents (client_id, pos,  document_type, document_concept, number, date, 
                expiration_date, total_amount, taxable_amount, exempt_amount, tax_amount, currency, exchange_rate, cae, cae_vto, status ) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                """

                values = (
                    document.client_id, document.pos, document.document_type.get_type(), document.document_concept.get_concept(), document.number,
                    document.date,  document.expiration_date, document.total_amount, document.taxable_amount,
                    document.exempt_amount, document.tax_amount, document.currency.get_value(), document.exchange_rate, document.cae, document.cae_vto, document.status
                )

                cur.execute(sql,values)

                document_id = cur.lastrowid

                conn.commit()

            return document_id

    def get_all(self):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql = f"SELECT * FROM documents d inner join clients c on d.client_id = c.client_id WHERE  client_status = '{Status.ACTIVE.get_value()}'"

                cur.execute(sql)
                rows = cur.fetchall()

                if len(rows) == 0:
                    return(None)

                data =  ResponseDocumentDtoFactory.from_list(rows)

        return (data)

    def get_id(self, id: int):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:
                sql: str = f"SELECT * FROM documents d inner join clients c on d.client_id = c.client_id  WHERE document_id = %s AND status = %s"

                values = (id, Status.ACTIVE.get_value())

                cur.execute(sql, values)
                row = cur.fetchone()

                if row is None:
                    return None

                document: Document = (DocumentBuilder()
                                      .document_id((row["document_id"]))
                                      .client_id(row["client_id"])
                                      .pos(row["pos"])
                                      .document_type(DocumentType.get_document_type(row["document_type"]))
                                      .document_concept(DocumentConcept.get_document_concept(row["document_concept"]))
                                      .client_type_id(TypeId.get_type_id(row["client_type_id"]))
                                      .client_tax_id(row["client_tax_id"])
                                      .client_name(row["client_name"])
                                      .client_address(row["client_address"])
                                      .client_city(row["client_city"])
                                      .client_state(row["client_state"])
                                      .date(row["date"])
                                      .expiration_date(row["expiration_date"])
                                      .total_amount((row["total_amount"]))
                                      .taxable_amount(row["taxable_amount"])
                                      .exempt_amount(row["exempt_amount"])
                                      .no_grav_amount(row["no_grav_amount"])
                                      .tributes_amount(row["tributes_amount"])
                                      .tax_amount(row["tax_amount"])
                                      .currency(Currency.get_currency(row["currency"]))
                                      .exchange_rate(row["exchange_rate"])
                                      .cae(row["cae"])
                                      .cae_vto(row["cae_vto"])
                                      .number(row["number"])
                                      .build())

            return document

    def save(self, document :Document):

         with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = ("""UPDATE documents SET pos = %s, document_type= %s, document_concept= %s, number= %s, 
                               date = %s, expiration_date = %s, total_amount= %s, taxable_amount = %s, exempt_amount = %s,
                               tax_amount = %s, currency = %s, exchange_rate = %s, cae = %s, cae_vto = %s, status = %s
                               WHERE document_id = %s """)

                values = (
                    document.pos, document.document_type.get_type(),
                    document.document_concept.get_concept(), document.number,
                    document.date, document.expiration_date, document.total_amount, document.taxable_amount,
                    document.exempt_amount, document.tax_amount, document.currency.get_value(), document.exchange_rate,
                    document.cae, document.cae_vto, document.status, document.document_id
                )

                cur.execute(sql, values)
                conn.commit()




