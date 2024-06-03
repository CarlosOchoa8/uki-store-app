from database.db import db


class Address(db.Model):
    """Address db model class."""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    company_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False, unique=True)
    address_detail = db.Column(db.String, nullable=True, unique=True)
    city = db.Column(db.String, nullable=True, unique=True)
    country = db.Column(db.String, nullable=True, unique=True)
    country_region = db.Column(db.String, nullable=True, unique=True)
    postal_code = db.Column(db.String, nullable=True, unique=True)
    phone_number = db.Column(db.String, nullable=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # TODO Averiguar como mandar un null a la base de datos
    def __init__(self, **kwargs):
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.password = kwargs.get("password")
        self.email = kwargs.get("email")
        self.phone_number = None if kwargs.get("phone_number") == '' else kwargs.get("phone_number")

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
            "email": self.email,
            "phone_number": self.phone_number
        }
