class Client:
    def __init__(self, name, address, city, state, country, email, phone, tax_id, tax_condition):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.email = email
        self.phone = phone
        self.tax_id = tax_id
        self.tax_condition = tax_condition

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Country: {self.country}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n"
                f"Tax ID: {self.tax_id}\n"
                f"Tax Condition: {self.tax_condition}")
