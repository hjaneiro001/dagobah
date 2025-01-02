
from afip import Afip

from app.dtos.documentAfipDto import DocumentAfipDto
from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.entities.document import Document
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

    def create_pdf(self, document : ResponseDocumentMM):

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
                'code': '321',  # Codigo
                'name': 'Cafe Americano',  # Nombre
                'quantity': '1,00',  # Cantidad
                'measurement_unit': 'Unidad',  # Unidad de medida
                'price': '1500,00',  # Precio
                'tax_percent': '21%',  # Precio
                'percent_subsidized': '0,00',  # Precio subsidiado
                'impost_subsidized': '0,00',  # Impuestos subsidiado
                'subtotal': '1500,00'  # Subtotal
            },
            {
                'code': '321',  # Codigo
                'name': 'Cafe Americano',  # Nombre
                'quantity': '1,00',  # Cantidad
                'measurement_unit': 'Unidad',  # Unidad de medida
                'price': '1500,00',  # Precio
                'tax_percent': '21%',  # Precio
                'percent_subsidized': '0,00',  # Precio subsidiado
                'impost_subsidized': '0,00',  # Impuestos subsidiado
                'subtotal': '1500,00'  # Subtotal
            }
        ]

        billing_data = {
            'tax_id': document["client_tax_id"],
            'name': document["client_name"],
            'vat_condition': document["client_tax_condition"],
            'address': document["client_address"] + " - " + document["client_city"] + " - " + document["client_state"],
            'payment_method':  'N/A'
        }

        overall = {
            'subtotal': document["taxable_amount"],
            'impost_tax': document["tax_amount"],
            'total': document["total_amount"]
        }

        qr_code_image = self.create_qr()

        base_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta al directorio del script
        html_path = os.path.join(base_dir, 'bill.html')  # Ruta absoluta a 'bill.html'

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
            "width": 8,  # Ancho de pagina en pulgadas. Usar 3.1 para ticket
            "marginLeft": 0.4,  # Margen izquierdo en pulgadas. Usar 0.1 para ticket
            "marginRight": 0.4,  # Margen derecho en pulgadas. Usar 0.1 para ticket
            "marginTop": 0.4,  # Margen superior en pulgadas. Usar 0.1 para ticket
            "marginBottom": 0.4  # Margen inferior en pulgadas. Usar 0.1 para ticket
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

    def create_qr(self):

        qr_code_data = {
            'ver': 1,  # Versión del formato de los datos (1 por defecto)
            'fecha': '2017-10-25',  # Fecha de emisión del comprobante
            'cuit': 12345678912,  # Cuit del Emisor del comprobante
            'ptoVta': 1,  # Punto de venta utilizado para emitir el comprobante
            'tipoCmp': 6,  # Tipo de comprobante
            'nroCmp': 32,  # Tipo de comprobante
            'importe': 150,  # Importe Total del comprobante (en la moneda en la que fue emitido)
            'moneda': 'ARS',  # Moneda del comprobante
            'ctz': 1,  # Cotización en pesos argentinos de la moneda utilizada
            'tipoDocRec': 80,  # Código del Tipo de documento del receptor
            'nroDocRec': 12345678912,  # Número de documento del receptor
            'tipoCodAut': 'E',  # “A” para comprobante autorizado por CAEA, “E” para comprobante autorizado por CAE
            'codAut': 12345678912345  # CAE o CAEA, segun corresponda
        }

        qr_code_text = 'https://www.afip.gob.ar/fe/qr/?p=' + base64.urlsafe_b64encode(
            json.dumps(qr_code_data).encode('utf-8')).decode('utf-8')

        qrcode = segno.make_qr(qr_code_text)

        qr_code_image = qrcode.png_data_uri(scale=4)

        return(qr_code_image)


