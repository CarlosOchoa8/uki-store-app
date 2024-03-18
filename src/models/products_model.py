from database.db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    main_picture = db.Column(db.Text, nullable=False)

    def __init__(self, name, category, price, main_picture):
        self.name = name
        self.category = category
        self.price = price
        self.main_picture = main_picture

    def __repr__(self):
        return (f"<{self.id}>"
                f"<{self.name}>"
                f"<{self.category}>"
                f"<{self.price}>")
