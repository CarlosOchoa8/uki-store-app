from database.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.String(13), nullable=True, unique=True)
    address = db.relationship("Address", backref="user")

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
                f"<{self.email}>"
                f"<{self.phone_number}>"
                )

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number
        }

"""
Tambien la migracion se puede realizar con
    db.create_all()
"""