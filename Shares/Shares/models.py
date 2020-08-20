from Shares import db

class Company(db.Model):
    __tablename__="company"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self,name,price,quantity,total):
        self.name  = name
        self.price = price
        self.quantity = quantity
        self.total = total

    def __repr__(self):
        return f"name is {self.name} price is {self.price} quantity is {self.quantity} total is {self.total}"
