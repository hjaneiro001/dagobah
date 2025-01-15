from sqlalchemy import QueuePool

from app.entities.company import Company, CompanyBuilder
from app.entities.enums.status import Status
from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.typeId import TypeId
from app.utils.connection_manager import ConnectionManager
from app.utils.cursor_manager import CursorManager


class CompanyRepository:

    def __init__(self, pool_connection: QueuePool):
        self.pool_connection: QueuePool = pool_connection

    def create(self, company :Company):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql :str = """INSERT INTO companies (company_name,company_address, company_city, company_state, company_country, company_email, 
                company_phone, company_type_id, company_tax_id, company_tax_condition,company_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                values = (
                    company.company_name, company.company_address, company.company_city, company.company_state, company.company_country,
                    company.company_email,company.company_phone,company.company_type_id.get_type(),company.company_tax_id,
                    company.company_tax_condition.get_condition(),company.company_status.get_value())

                cur.execute(sql, values)
                company_id = cur.lastrowid
                conn.commit()

        return company_id


    def save(self,company: Company):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = """
                        UPDATE companies
                        SET company_name = %s, company_address = %s, company_city = %s, company_state = %s,
                            company_country = %s, company_email = %s, company_phone = %s, company_type_id = %s,
                            company_tax_id = %s, company_tax_condition = %s, company_status = %s
                        WHERE company_id = %s
                    """

                values = (
                    company.company_name, company.company_address, company.company_city, company.company_state, company.company_country,
                    company.company_email, company.company_phone, company.company_type_id.get_type(), company.company_tax_id,
                    company.company_tax_condition.get_condition() , company.company_status.get_value(), company.company_id
                )

                cur.execute(sql, values)
                conn.commit()

    def get_tax_id(self, taxId :str):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:
                sql: str = f"SELECT * FROM companies WHERE company_tax_id = %s AND company_status = '{Status.ACTIVE.get_value()}'"
                cur.execute(sql, taxId)
                row = cur.fetchone()

                if row is None:
                    return None

                company = (CompanyBuilder()
                          .company_id(row.get('company_id'))
                          .company_name(row.get('company_name'))
                          .company_address(row.get('company_address'))
                          .company_city(row.get('company_city'))
                          .company_state(row.get('company_state'))
                          .company_country(row.get('company_country'))
                          .company_email(row.get('company_email'))
                          .company_phone(row.get('company_phone'))
                          .company_type_id(TypeId.get_type_id(row.get('company_type_id')))
                          .company_tax_id(row.get('company_tax_id'))
                          .company_tax_condition(TaxCondition.get_tax_condition(row.get('company_tax_condition')))
                          .company_status(Status.get_status(row.get('company_status')))
                          .build())

            return company

    def get_all(self):

        print("entro repositorio")

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = f"SELECT * FROM companies WHERE company_status = '{Status.ACTIVE.get_value()}'"
                cur.execute(sql)
                rows = cur.fetchall()

                if rows is None:
                    return []

                companies: list[Company] = []

                for row in rows:
                    company :Company = (CompanyBuilder()
                              .company_id(row.get('company_id'))
                              .company_name(row.get('company_name'))
                              .company_address(row.get('company_address'))
                              .company_city(row.get('company_city'))
                              .company_state(row.get('company_state'))
                              .company_country(row.get('company_country'))
                              .company_email(row.get('company_email'))
                              .company_phone(row.get('company_phone'))
                              .company_type_id(TypeId.get_type_id(row.get('company_type_id')))
                              .company_tax_id(row.get('company_tax_id'))
                              .company_tax_condition(TaxCondition.get_tax_condition(row.get('company_tax_condition')))
                              .company_status(Status.get_status(row.get('company_status')))
                              .build())
                    companies.append(company)

        return companies

    def get_id(self, id :int):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:
                sql: str = f"SELECT * FROM companies WHERE company_id = %s AND company_status = '{Status.ACTIVE.get_value()}'"
                cur.execute(sql, id)
                row = cur.fetchone()

                if row is None:
                    return None

                company :Company = (CompanyBuilder()
                          .company_id(row.get('company_id'))
                          .company_name(row.get('company_name'))
                          .company_address(row.get('company_address'))
                          .company_city(row.get('company_city'))
                          .company_state(row.get('company_state'))
                          .company_country(row.get('company_country'))
                          .company_email(row.get('company_email'))
                          .company_phone(row.get('company_phone'))
                          .company_type_id(TypeId.get_type_id(row.get('company_type_id')))
                          .company_tax_id(row.get('company_tax_id'))
                          .company_tax_condition(TaxCondition.get_tax_condition(row.get('company_tax_condition')))
                          .company_status(Status.get_status(row.get('company_status')))
                          .build())

            return company



    def save_certificado(self, id, cert):
        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = ("""UPDATE companies SET company_cert = %s
                                 WHERE company_id = %s """)

                values = (
                    cert, id
                )

                cur.execute(sql, values)
                conn.commit()


    def save_key(self, id, key):
        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql: str = ("""UPDATE companies SET company_key = %s
                                 WHERE company_id = %s """)

                values = (
                    key, id
                )

                cur.execute(sql, values)
                conn.commit()




