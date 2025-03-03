from datetime import datetime

class DocumentAfipDto:
    def __init__(self, cant_reg: int, pos: int, document_type :int, concept :int, client_type_id : int, id_number :str, client_tax_condition :str,
            document_from :int, document_to :int, document_date :datetime,document_date_serv_from :datetime,document_date_serv_to :datetime,
            document_expiration_date :datetime, total_amount :float, no_grav_amount :float,
            taxable_amount :float, exempt_amount: float, tax_amount :float, tributes_amount: float, currency :str,
            exchange_rate :float, iva_list=None):

        self.CantReg = 1
        self.Pos = pos
        self.document_type = document_type
        self.concept = concept
        self.client_type_id = client_type_id
        self.id_number = id_number
        self.client_tax_condition = client_tax_condition
        self.document_from = document_from
        self.document_to = document_to
        self.document_date = document_date
        self.document_date_serv_from = document_date_serv_from
        self.document_date_serv_to = document_date_serv_to
        self.document_expiration_date = document_expiration_date
        self.total_amount = total_amount
        self.no_grav_amount = no_grav_amount
        self.taxable_amount = taxable_amount
        self.exempt_amount = exempt_amount
        self.tax_amount = tax_amount
        self.tributes_amount = tributes_amount
        self.currency = currency
        self.exchange_rate = exchange_rate
        self.iva_list = iva_list or []


    def __eq__(self, other):
        if not isinstance(other, DocumentAfipDto):
            return False
        return (self.CantReg == other.CantReg and
                self.Pos == other.Pos and
                self.document_type == other.document_type  and
                self.concept == other.concept and
                self.client_type_id == other.client_type_id and
                self.id_number == other.id_number and
                self.client_tax_condition == other.client_tax_condition and
                self.document_from == other.document_from and
                self.document_to == other.document_to and
                self.document_date == other.document_date and
                self.document_date_serv_from == other.document_date_serv_from and
                self.document_date_serv_to == other.document_date_serv_to and
                self.document_expiration_date == other.document_expiration_date and
                self.total_amount == other.total_amount and
                self.no_grav_amount == other.no_grav_amount and
                self.taxable_amount == other.taxable_amount and
                self.exempt_amount == other.exempt_amount and
                self.tax_amount == other.tax_amount and
                self.tributes_amount == other.tributes_amount and
                self.currency == other.currency and
                self.exchange_rate == other.exchange_rate and
                self.iva_list == other.iva_list)

    def __str__(self):
        return (f"DocumentAfipDto(CantReg={self.CantReg}\n"
                f"PtoVta={self.Pos}\n"
                f"Comprobante Tipo={self.document_type}\n"
                f"Concepto={self.concept}\n"
                f"Tipo Documento={self.client_type_id}\n"
                f"Numero de ID Cliente={self.id_number}\n"
                f"Condicion Fiscal={self.client_tax_condition}\n"
                f"Documento desde={self.document_from}\n"
                f"Documento hasta={self.document_to}\n"
                f"Fecha del Documento={self.document_date}\n"
                f"Fecha Servicio desde={self.document_date_serv_from}\n"
                f"Fecha Servicio hasta={self.document_date_serv_to}\n"
                f"Fecha vencimiento documento={self.document_expiration_date}\n"
                f"Importe Total={self.total_amount}\n"
                f"Importe no Gravado={self.no_grav_amount}\n"
                f"Importe Neto={self.taxable_amount}\n"
                f"Importe exento={self.exempt_amount}\n"
                f"Importe Iva={self.tax_amount}\n"
                f"Importe Total de Tributos={self.tributes_amount}\n"
                f"Moneds={self.currency}\n"
                f"Cotizacion Moneda={self.exchange_rate}\n"
                f"Iva list={self.iva_list}\n")

    def to_dict(self):
        return {"CantReg": self.CantReg,
                "PtoVta": self.Pos,
                "CbteTipo": self.document_type,
                "Concepto":self.concept,
                "DocTipo": self.client_type_id,
                "DocNro": self.id_number,
                "CondicionIVAReceptorId": self.client_tax_condition,
                "CbteDesde": self.document_from,
                "CbteHasta": self.document_to,
                "CbteFch": self.document_date,
                "FchServDesde": self.document_date_serv_from,
                "FchServHasta": self.document_date_serv_to,
                "FchVtoPago": self.document_expiration_date,
                "ImpTotal": self.total_amount,
                "ImpTotConc": self.no_grav_amount,
                "ImpNeto": self.taxable_amount,
                "ImpOpEx": self.exempt_amount,
                "ImpIVA": self.tax_amount,
                "ImpTrib": self.tributes_amount,
                "MonId": self.currency,
                "MonCotiz": self.exchange_rate,
                "Iva":self.iva_list}

    @classmethod
    def builder(cls):
        return cls.DocumentAfipDtoBuilder()

    class DocumentAfipDtoBuilder:
        def __init__(self):
            self._cant_reg = None
            self.pto_vta = None
            self._document_type = None
            self._concept = None
            self._client_type_id = None
            self._id_number = None
            self._client_tax_condition = None
            self._document_from = None
            self._document_to = None
            self._document_date = None
            self._document_date_serv_from = None
            self._document_date_serv_to = None
            self._document_expiration_date = None
            self._total_amount = None
            self._no_grav_amount = None
            self._taxable_amount = None
            self._exempt_amount = None
            self._tax_amount = None
            self._tributes_amount = None
            self._currency = None
            self._exchange_rate = None
            self._iva_list = []

        def cant_reg(self, cant_reg: int):
            self._cant_reg = cant_reg
            return self

        def pos(self, pos: int):
            self._pos = pos
            return self

        def document_type(self, document_type: int):
            self._document_type = document_type
            return self

        def concept(self, concept :int):
            self._concept = concept
            return self

        def client_type_id(self, client_type_id :int):
            self._client_type_id = client_type_id
            return self

        def id_number(self,id_number :str):
            self._id_number = id_number
            return self

        def client_tax_condition(self,client_tax_condition :str):
            self._client_tax_condition = client_tax_condition
            return self

        def document_from(self,document_from :int):
            self._document_from = document_from
            return self

        def document_to(self,document_to :int):
            self._document_to = document_to
            return self

        def document_date(self,document_date :datetime):
            self._document_date = document_date
            return self

        def document_date_serv_from(self, document_date_serv_from: datetime):
            self._document_date_serv_from = document_date_serv_from
            return self

        def document_date_serv_to(self, document_date_serv_to: datetime):
            self._document_date_serv_to = document_date_serv_to
            return self

        def document_expiration_date(self, document_expiration_date: datetime):
            self._document_expiration_date = document_expiration_date
            return self

        def total_amount(self,total_amount):
            self._total_amount = total_amount
            return self

        def no_grav_amount(self,no_grav_amount):
            self._no_grav_amount = no_grav_amount
            return self

        def taxable_amount(self,taxable_amount):
            self._taxable_amount = taxable_amount
            return self

        def exempt_amount(self,exempt_amount):
            self._exempt_amount = exempt_amount
            return self

        def tax_amount(self,tax_amount):
            self._tax_amount = tax_amount
            return self

        def tributes_amount(self,tributes_amount):
            self._tributes_amount = tributes_amount
            return self

        def currency(self,currency):
            self._currency = currency
            return self

        def exchange_rate(self,exchange_rate):
            self._exchange_rate = exchange_rate
            return self

        def iva_list(self, iva_list):
            self._iva_list = iva_list
            return self

        def build(self):

            return DocumentAfipDto(
                cant_reg=self._cant_reg,
                pos=self._pos,
                document_type=self._document_type,
                concept=self._concept,
                client_type_id=self._client_type_id,
                id_number=self._id_number,
                client_tax_condition=self._client_tax_condition,
                document_from=self._document_from,
                document_to=self._document_to,
                document_date=self._document_date,
                document_date_serv_from=self._document_date_serv_from,
                document_date_serv_to=self._document_date_serv_to,
                document_expiration_date=self._document_expiration_date,
                total_amount=self._total_amount,
                no_grav_amount=self._no_grav_amount,
                taxable_amount=self._taxable_amount,
                exempt_amount=self._exempt_amount,
                tax_amount=self._tax_amount,
                tributes_amount=self._tributes_amount,
                currency=self._currency,
                exchange_rate=self._exchange_rate,
                iva_list=self._iva_list)
