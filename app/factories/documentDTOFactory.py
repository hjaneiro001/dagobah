from datetime import datetime

from app.dtos.responseDocumentDto import ResponseDocumentDto


class ResponseDocumentDtoFactory:
    @staticmethod
    def from_dict(data: dict) -> ResponseDocumentDto:

        return ResponseDocumentDto(
            document_id=data.get("document_id"),
            client_id=data.get("client_id"),
            pos=data.get("pos"),
            document_type=data.get("document_type"),
            document_concept=data.get("document_concept"),
            number=data.get("number"),
            date=ResponseDocumentDtoFactory._parse_date(data.get("date")),
            date_serv_from=ResponseDocumentDtoFactory._parse_date(data.get("date_serv_from")),
            date_serv_to=ResponseDocumentDtoFactory._parse_date(data.get("date_serv_to")),
            expiration_date=ResponseDocumentDtoFactory._parse_date(data.get("expiration_date")),
            total_amount=data.get("total_amount"),
            taxable_amount=data.get("taxable_amount"),
            exempt_amount=data.get("exempt_amount"),
            no_grav_amount=data.get("no_grav_amount"),
            tributes_amount=data.get("tributes_amount"),
            tax_amount=data.get("tax_amount"),
            currency=data.get("currency"),
            exchange_rate=data.get("exchange_rate"),
            status=data.get("status"),
            client_name=data.get("client_name"),
            client_address=data.get("client_address"),
            client_city=data.get("client_city"),
            client_state=data.get("client_state"),
            client_country=data.get("client_country"),
            client_type_id=data.get("client_type_id"),
            client_tax_id=data.get("client_tax_id"),
            client_tax_condition=data.get("client_tax_condition"),
            cae= data.get("cae"),
            cae_vto = data.get("cae_vto")
        )

    @staticmethod
    def from_list(rows):
        dtos = []
        for row in rows:
            dto = ResponseDocumentDto(
                document_id=row['document_id'],
                client_id=row['client_id'],
                pos=row['pos'],
                document_type=row['document_type'],
                document_concept=row['document_concept'],
                number=row['number'],
                date=row['date'],
                date_serv_from=row['date_serv_from'],
                date_serv_to=row['date_serv_to'],
                expiration_date=row['expiration_date'],
                total_amount=row['total_amount'],
                taxable_amount=row['taxable_amount'],
                exempt_amount=row['exempt_amount'],
                no_grav_amount=row['no_grav_amount'],
                tributes_amount=row['tributes_amount'],
                tax_amount=row['tax_amount'],
                currency=row['currency'],
                exchange_rate=row['exchange_rate'],
                status=row['status'],
                client_name=row['client_name'],
                client_address=row['client_address'],
                client_city=row['client_city'],
                client_state=row['client_state'],
                client_country=row['client_country'],
                client_type_id=row['client_type_id'],
                client_tax_id=row['client_tax_id'],
                client_tax_condition=row['client_tax_condition'],
                cae=row["cae"],
                cae_vto=row["cae_vto"]
            )
            dtos.append(dto)

        return dtos

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        if not date_str:
            return None

        # Si ya es un objeto datetime, no lo parseamos
        if isinstance(date_str, datetime):
            return date_str

        # Si no es una cadena, lanzamos una excepción
        if not isinstance(date_str, str):
            raise TypeError(f"El valor debe ser str o datetime, pero se recibió {type(date_str).__name__}: {date_str}")

        try:
            return datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
        except ValueError:
            raise ValueError(f"Fecha inválida: {date_str}")

    @staticmethod
    def from_entity(entity) -> ResponseDocumentDto:

        return ResponseDocumentDto(
            document_id=entity.document_id,
            client_id=entity.client_id,
            pos=entity.pos,
            document_type=entity.document_type.name if entity.document_type else None,
            document_concept=entity.document_concept.name if entity.document_concept else None,
            number=entity.number,
            date=entity.date,
            date_serv_from=entity.date_serv_from,
            date_serv_to=entity.date_serv_to,
            expiration_date=entity.expiration_date,
            total_amount=entity.total_amount,
            taxable_amount=entity.taxable_amount,
            exempt_amount=entity.exempt_amount,
            no_grav_amount=entity.no_grav_amount,
            tributes_amount=entity.tributes_amount,
            tax_amount=entity.tax_amount,
            currency=entity.currency.name if entity.currency else None,
            exchange_rate=entity.exchange_rate,
            status=entity.status.name if entity.status else None,
            client_name=entity.client.name,
            client_address=entity.client.address,
            client_city=entity.client.city,
            client_state=entity.client.state,
            client_country=entity.client.country,
            client_type_id=entity.client.type_id.name if entity.client.type_id else None,
            client_tax_id=entity.client.tax_id,
            client_tax_condition=entity.client.tax_condition.name if entity.client.tax_condition else None,
            cae=entity.cae if entity.cae else None,
            cae_vto=entity.cae_vto
        )
