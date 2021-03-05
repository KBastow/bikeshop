from application import app, db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(50), nullable=False)
    orders = db.relationship('orders', backref= 'customer')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

class OrderLineItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship('Products', backref= 'products')
    order = db.relationship('Order', backref= 'order')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products_ordered = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    date_ordered = db.Column(db.Date, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))