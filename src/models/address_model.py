from database.db import db


class Address(db.Model):
    """Address db model class."""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    company_name = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    address_detail = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    country_region = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # TODO
    # def __init__(self, **kwargs):
    #     self.first_name = kwargs.get("first_name")
    #     self.last_name = kwargs.get("last_name")
    #     self.company_name = kwargs.get("company_name")
    #     self.address = kwargs.get("address")
    #     self.address_detail = kwargs.get("address_detail")
    #     self.city = kwargs.get("city")
    #     self.city = kwargs.get("city")
    #     self.country = kwargs.get("country")
    #     self.country_region = kwargs.get("country_region")
    #     self.postal_code = kwargs.get("postal_code")
    #     self.phone_number = kwargs.get("phone_number")
    #     self.user_id = kwargs.get("user_id")

    def __repr__(self):
        return (f"<{self.first_name}>"
                f"<{self.last_name}>"
                f"<{self.company_name}>"
                f"<{self.address}>"
                f"<{self.address_detail}>"
                f"<{self.city}>"
                f"<{self.country}>"
                f"<{self.country_region}>"
                f"<{self.postal_code}>"
                f"<{self.phone_number}>"
                f"<{self.user_id}>"
                )

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
