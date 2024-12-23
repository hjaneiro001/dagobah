from afip import Afip

from app.dtos.documentAfipDto import DocumentAfipDto
from app.entities.document import Document
from app.entities.item import Item

class SdkAfipRepository:

    def __init__(self):
        self.afip = Afip({"CUIT": 20409378472})

    def next_number(self,document :Document, items :list[Item]):

        document_number = self.afip.ElectronicBilling.getLastVoucher(document.pos,document.document_type.get_value())
        next_number = document_number + 1

        return next_number

    def create_document_afip(self,documentDTO :DocumentAfipDto):

        return_full_response = False
        res = self.afip.ElectronicBilling.createVoucher(documentDTO.to_dict(), return_full_response)

        res["CAE"]
        res["CAEFchVto"]

        return(res)