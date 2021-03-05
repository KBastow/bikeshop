from application import app, db
from application.models import Products, Customer

# first_customer=Customer(first_name="Kelvin", last_name="Bastow", email_address= 'Kelvinb97@outlook.com')
# db.session.add(first_customer)
# db.session.commit()

# second_order=Orders(fk_user_id= "1", product_ordered= "Canyon Ultimate CF SLX 8 Disc eTap", price= "5499", order_date= "2020/12/25")
# db.session.add(second_order)
# db.session.commit()

# from application import app, db
# from application.models import Games

# CREATE
@app.route('/add/customers')
def add_customers():
    new_customer = Customers(first_name= "Kelvin", last_name="Bastow", email_address="kelvinb97@outlook.com")
    db.session.add(new_customer)
    db.session.commit()
    return "New Customer Has Been Added"

@app.route('/add/products')
def add_products():
    new_product = Products(product="Canyon Ultimate CFR Di2", quantity="20", price="8649")
    db.session.add(new_product)
    db.session.commit()
    return "New Product Has Been Added"

# READ
@app.route('/customerlist')
def read_customers():
    customers_table = Customer.query.all()
    # games_string = ""
    # for game in all_games:
    #     games_string += "<br>"+ game.name
    # return games_string
    table = Customers(customers_table)
    return table.__html__()

@app.route('/productlist')
def read_products():
    products_table = Product.query.all()
    table = Products(products_table)
    return table.__html__()

# UPDATE
@app.route('/customerupdate/<name>')
def update_customer(name):
    first_customer = Customers.query.first()
    first_customer.name = name
    db.session.commit()
    return first_customer.name

@app.route('/productupdate/<name>')
def update_product(name):
    first_product = Products.query.first()
    first_product.name = name
    db.session.commit()
    return first_product.name

# DELETE
# @app.route('/product/delete/<name>')
# def delete(name):
#     game_to_delete = Games.query.first()
#     db.session.delete(game_to_delete)
#     db.session.commit()
#     return "Item Deleted From Product Database"