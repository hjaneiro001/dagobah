class Client:
    def __init__(self, pk_client, name, address, city, state, country, email, phone, type_id,tax_id, tax_condition, status):
        self.pk_client = pk_client
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.email = email
        self.phone = phone
        self.type_id = type_id
        self.tax_id = tax_id
        self.tax_condition = tax_condition
        self.status = status

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Country: {self.country}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n"
                f"Phone: {self.type_id}\n"
                f"Tax ID: {self.tax_id}\n"
                f"Tax Condition: {self.tax_condition}")

    def to_dict(self):
        return {
            "pk_client": self.pk_client,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "email": self.email,
            "phone": self.phone,
            "type_id": self.type_id,
            "tax_id": self.tax_id,
            "tax_condition": self.tax_condition,
            "status": self.status
        }