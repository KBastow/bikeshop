from application import app, db
from application.models import Products, Customer, Orders

# CREATE
@app.route('/add/customer')
def add_customers():
    new_customer = Customer(first_name= "Kelvin", last_name="Bastow", email_address="kelvinb97@outlook.com")
    db.session.add(new_customer)
    db.session.commit()
    return "New Customer Has Been Added"

@app.route('/add/product')
def add_products():
    new_product = Products(product="Canyon Ultimate CFR Di2", quantity="20", price="8649")
    db.session.add(new_product)
    db.session.commit()
    return "New Product Has Been Added"

# READ
@app.route('/customerlist')
def read_customers():
    customer_table = customer.query.all()
    table = customer(customer_table)
    return table.__html__()

@app.route('/productlist')
def read_products():
    product_table = product.query.all()
    table = product(product_table)
    return table.__html__()

# UPDATE
@app.route('/customerupdate/<name>')
def update_customers(name):
    first_customer = customer.query.first()
    first_customer.name = name
    db.session.commit()
    return first_customer.name

@app.route('/productupdate/<name>')
def update_products(name):
    first_product = product.query.first()
    first_product.name = name
    db.session.commit()
    return first_product.name

# DELETE
@app.route('/customer/delete/<name>')
def delete_customers(name):
    customer_to_delete = customers.query.first()
    db.session.delete(customer_to_delete)
    db.session.commit()
    return "Customer Has Been Deleted"

@app.route('/product/delete/<name>')
def delete_products(name):
    products_to_delete = product.query.first()
    db.session.delete(product_to_delete)
    db.session.commit()
    return "Product Has Been Deleted"