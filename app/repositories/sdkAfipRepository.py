
from afip import Afip
from sqlalchemy import QueuePool

from app.dtos.documentAfipDto import DocumentAfipDto
from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.entities.company import Company, CompanyBuilder
from app.entities.cuentaArca import CuentaArca
from app.entities.document import Document
from app.entities.enums.currency import Currency
from app.entities.enums.documentType import DocumentType
from app.entities.enums.typeId import TypeId
from app.exceptions.certificateNotFoundException import CertificateNotFoundException
from app.exceptions.errorCreateDocumentAfipException import ErrorCreateDocumentAfipException

import json
import base64
import segno

import os

import requests

from jinja2 import Template

from app.exceptions.keyNotFoundException import KeyNotFoundException
from app.utils.connection_manager import ConnectionManager
from app.utils.cursor_manager import CursorManager


class SdkAfipRepository:

    def __init__(self, pool_connection :QueuePool):
        self.afip_instances = {}
        self.pool_connection: QueuePool = pool_connection

    def get_afip_instance(self, company: Company):
        if company.company_tax_id not in self.afip_instances:

            # cert = self.get_certificado(company.company_id)

            tax_id = company.company_tax_id

            self.afip_instances[company.company_tax_id] = Afip({"CUIT": tax_id,
                                                                # "cert": cert["cert"],
                                                                # "key": cert["key"],
                                                                # "access_token": "4FufbwHcegtwPnkwgJ1RfgHBOlkef5YQFH97sOqGoQpzqPPZMHqdMqj8Jk5a7XeA",
                                                                # "production": True
                                                                })

        return self.afip_instances[company.company_tax_id]

    def next_number(self,document :Document, company:Company):

        afip_instance = self.get_afip_instance(company)
        document_number = afip_instance.ElectronicBilling.getLastVoucher(document.pos,document.document_type.get_value())

        next_number = document_number + 1

        return next_number

    def create_document_afip(self,documentDTO :DocumentAfipDto, company :Company):

        afip_instance = self.get_afip_instance(company)
        return_full_response = False

        res = afip_instance.ElectronicBilling.createVoucher(documentDTO.to_dict(), return_full_response)

        return(res)

    def create_pdf(self, document : ResponseDocumentMM,company :Company, mode ):

        afip_instance = self.get_afip_instance(company)

        page_width = 8
        margins = 0.4

        if mode=="ticket":
            page_width = 3.1
            margins= 0.1


        business_data = {
            'business_name': company.company_name,
            'address': company.company_address +" " + company.company_city + " " + company.company_state,
            'tax_id': company.company_tax_id,
            'gross_income_id': company.company_tax_id,
            'start_date': "",
            'vat_condition': company.company_tax_condition.get_condition()
        }

        bill = {
            'number': str(document["number"]),
            'point_of_sale': str(document["pos"]),
            'date':  document["date"],
            'expiration':  document["expiration_date"] ,
            'type': 'B',
            'concept': document["document_concept"],
            'CAE': document["cae"],
            'CAE_expiration': document["cae_vto"]
        }

        items = [
            {
                'code': item['product_code'],
                'name': item['product_name'],
                'quantity': f"{item['quantity']:.2f}".replace('.', ','),
                'measurement_unit': item.get('unit_measurement', 'Unidad'),
                'price': f"{item['unit_price']:.2f}".replace('.', ','),
                # 'tax_percent': item['tax_rate'],
                'percent_subsidized': "0,00",
                'impost_subsidized': "0,00",
                'subtotal': f"{item['unit_price']:.2f}".replace('.', ',')
            }
            for item in document["items"]
        ]

        billing_data = {
            'tax_id': document["client_tax_id"],
            'name': document["client_name"],
            'vat_condition': document["client_type_id"],
            'address': document["client_address"]  + " - " + document["client_city"] + " - " + document["client_state"],
            'payment_method':  'N/A'
        }

        overall = {
            'subtotal': document["taxable_amount"],
            'impost_tax': document["tax_amount"],
            'total': document["total_amount"]
        }

        qr_code_image = self.create_qr(document)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(base_dir, f"{mode}.html")

        with open(html_path, 'r') as f:
            html = f.read()

            template = Template(html)

            template_html = template.render(
                business_data=business_data,
                bill=bill,
                items=items,
                billing_data=billing_data,
                overall=overall,
                qr_code_image=qr_code_image
            )

        name = "PDF de prueba"

        options = {
            "width": page_width,  # Ancho de pagina en pulgadas. Usar 3.1 para ticket
            "marginLeft": margins,  # Margen izquierdo en pulgadas. Usar 0.1 para ticket
            "marginRight": margins,  # Margen derecho en pulgadas. Usar 0.1 para ticket
            "marginTop": margins,  # Margen superior en pulgadas. Usar 0.1 para ticket
            "marginBottom": margins # Margen inferior en pulgadas. Usar 0.1 para ticket
        }

        res = afip_instance.ElectronicBilling.createPDF({
            "html": template_html,
            "file_name": name,
            "options": options
        })

        print(res["file"])

        response = requests.get(res['file'])

        open("./Comprobante.pdf", 'wb').write(response.content)

        return(response.content)


    def create_qr(self, document : ResponseDocumentMM):

        qr_code_data = {
            'ver': 1,  # Versión del formato de los datos (1 por defecto)
            'fecha': document["date"],  # Fecha de emisión del comprobante
            'cuit': document["client_tax_id"],  # Cuit del Emisor del comprobante
            'ptoVta': document["pos"],  # Punto de venta utilizado para emitir el comprobante
            'tipoCmp': document["document_type"]["value"],
            'nroCmp': document["number"],  # Tipo de comprobante
            'importe': document["total_amount"],  # Importe Total del comprobante (en la moneda en la que fue emitido)
            'moneda': Currency.get_currency(document["currency"]).get_id(),  # Moneda del comprobante
            'ctz': document["exchange_rate"],  # Cotización en pesos argentinos de la moneda utilizada
            'tipoDocRec': TypeId.get_type_id(document["client_type_id"]).get_code(),  # Código del Tipo de documento del receptor
            'nroDocRec': document["client_tax_id"],  # Número de documento del receptor
            'tipoCodAut': 'E',  # “A” para comprobante autorizado por CAEA, “E” para comprobante autorizado por CAE
            'codAut': document["cae"]  # CAE o CAEA, segun corresponda
        }

        qr_code_text = 'https://www.afip.gob.ar/fe/qr/?p=' + base64.urlsafe_b64encode(
            json.dumps(qr_code_data).encode('utf-8')).decode('utf-8')

        qrcode = segno.make_qr(qr_code_text)

        qr_code_image = qrcode.png_data_uri(scale=4)

        return(qr_code_image)

    def create_certificado(self, company :Company,cuentaArca :CuentaArca ):

        tax_id = int(company.company_tax_id)
        username = cuentaArca.user

        password = cuentaArca.password

        cert_alias = cuentaArca.cert_name

        afip = Afip({"CUIT": tax_id,
                     "access_token": "4FufbwHcegtwPnkwgJ1RfgHBOlkef5YQFH97sOqGoQpzqPPZMHqdMqj8Jk5a7XeA",
                     "production": True
                     })
        res = afip.createCert(username, password, cert_alias)

        print(res["cert"])
        print(res["key"])

        return res

    def get_certificado(self,id):

        with ConnectionManager(self.pool_connection) as conn:
            with CursorManager(conn) as cur:

                sql = f"SELECT * FROM companies WHERE company_id = %s"

                cur.execute(sql, (id,))
                row = cur.fetchone()

                company :Company = (CompanyBuilder()
                                    .company_cert(row["company_cert"])
                                    .company_key(row["company_key"])
                                    .build()
                                    )
                if company.company_cert is None:
                    raise CertificateNotFoundException

                if company.company_key is None:
                    raise KeyNotFoundException

                cert_base64 = base64.b64encode(company.company_cert ).decode('utf-8')
                cert = base64.b64decode(cert_base64).decode('utf-8')

                key_base64 = base64.b64encode(company.company_key).decode('utf-8')
                key = base64.b64decode(key_base64).decode('utf-8')

                return {"cert": cert, "key": key}



