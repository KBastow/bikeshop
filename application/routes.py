from application import app, db
from application.models import Products, Customer, OrderLineItems, Order

# from application import app, db
# from application.models import Games

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
    # games_string = ""
    # for game in all_games:
    #     games_string += "<br>"+ game.name
    # return games_string
    table = customer(customer_table)
    return table.__html__()

@app.route('/productlist')
def read_products():
    product_table = product.query.all()
    table = product(product_table)
    return table.__html__()

# UPDATE
@app.route('/customerupdate/<name>')
def update_customer(name):
    first_customer = customer.query.first()
    first_customer.name = name
    db.session.commit()
    return first_customer.name

@app.route('/productupdate/<name>')
def update_product(name):
    first_product = product.query.first()
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