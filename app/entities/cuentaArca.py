class CuentaArca:

    def __init__(self,user,password,cert_name, company_id):
        self.user = user
        self.password = password
        self.cert_name = cert_name
        self.company_id = company_id

    def __str__(self):

        return(
            f"Usuario : {self.user}\n"
            f"Password : {self.password}\n"
            f"Certificado : {self.cert_name}\n"
            f"Company ID : {self.company_id}\n"
        )

    def __repr__(self):
        return (f"user={self.user},password={self.password},"
                f"cert_name= {self.cert_name}, company_id={self.company_id}")

    def __eq__(self, other):
        if isinstance(other,CuentaArca):
         return(
             self.user == other.user and
             self.password == other.password and
             self.cert_name == other.cert_name and
             self.company_id == other.company_id
         )
        return False

    def to_dict(self):
        return {
            "user" : self.user,
            "password" : self.password,
            "cert_name": self.cert_name,
            "cpmpany_id" : self.company_id
        }

class CuentaArcaBuilder:

    def __init__(self):

        self._user = None
        self._password = None
        self._cert_name = None
        self._company_id = None

    def user(self, user :str):
        self._user :str = user
        return  self

    def password(self,password :str):
        self._password :str = password
        return self

    def company_id(self,company_id :int):
        self._company_id :int = company_id
        return self

    def cert_name(self,cert_name :int):
        self._cert_name :int = cert_name
        return self


    def build(self):
        return CuentaArca(
            user=self._user,
            password=self._password,
            cert_name=self._cert_name,
            company_id=self._company_id
        )
