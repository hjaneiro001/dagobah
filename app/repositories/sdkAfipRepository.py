from locale import currency

from afip import Afip

from app.dtos.documentAfipDto import DocumentAfipDto
from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.entities.document import Document
from app.entities.enums.currency import Currency
from app.entities.enums.documentType import DocumentType
from app.entities.enums.typeId import TypeId
from app.entities.item import Item
from app.exceptions.errorCreateDocumentAfipException import ErrorCreateDocumentAfipException

import json
import base64
import segno

import os

import requests

from jinja2 import Template

class SdkAfipRepository:

    def __init__(self):
        self.afip = Afip({"CUIT": 20409378472})

    def next_number(self,document :Document, items :list[Item]):

        document_number = self.afip.ElectronicBilling.getLastVoucher(document.pos,document.document_type.get_value())
        next_number = document_number + 1

        return next_number

    def create_document_afip(self,documentDTO :DocumentAfipDto):

        return_full_response = False

        try:
            res = self.afip.ElectronicBilling.createVoucher(documentDTO.to_dict(), return_full_response)
            return(res)
        except Exception as e:
            raise ErrorCreateDocumentAfipException

    def create_pdf(self, document : ResponseDocumentMM, mode="bill"):

        page_width = 8
        margins = 0.4

        if mode=="ticket":
            page_width = 3.1
            margins= 0.1


        business_data = {
            'business_name': 'Empresa imaginaria S.A.',  # Nombre / Razon social
            'address': 'Calle falsa 123',  # Direccion
            'tax_id': 12345678912,  # CUIL/CUIT
            'gross_income_id': 12345432,  # Ingresos brutos
            'start_date': '25/10/2017',  # Fecha inicio de actividades
            'vat_condition': 'Responsable inscripto'  # Condicion frente al IVA
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
                'tax_percent': item['tax_rate'],
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

        res = self.afip.ElectronicBilling.createPDF({
            "html": template_html,
            "file_name": name,
            "options": options
        })

        print(res["file"])

        response = requests.get(res['file'])

        open("./Comprobante.pdf", 'wb').write(response.content)

        return(response)


    def create_qr(self, document : ResponseDocumentMM):


        qr_code_data = {
            'ver': 1,  # Versión del formato de los datos (1 por defecto)
            'fecha': document["date"],  # Fecha de emisión del comprobante
            'cuit': document["client_tax_id"],  # Cuit del Emisor del comprobante
            'ptoVta': document["pos"],  # Punto de venta utilizado para emitir el comprobante
            'tipoCmp': DocumentType.get_document_type(document["document_type"]).get_value(),  # Tipo de comprobante
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


