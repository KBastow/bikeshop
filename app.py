from application import app, models, db
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, DecimalField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

#BASKET

# class BasicForm(FlaskForm):
#     first_name = StringField('First Name')
#     last_name = StringField('Last Name')
#     contact_number = IntegerField('Mobile Number')

#     submit = SubmitField('Add Customer to Database')

# @app.route('/customerprofile', methods=['GET', 'POST'])
# def register():
#     error = ""
#     form = BasicForm()

#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         contact_number = form.contact_number.data

#         if len(first_name) == 0 or len(last_name) == 0:
#             error = "Please supply both first and last name"
#         else:
#             return ('thank_you', first_name)

#         if IntegerField(contact_number) == '0':
#             error = "Please Add Mobile Number"
#         else:
#             return ('Customer Has Been Added')

#     return render_template('customerprofile.html', form=form, message=error)

#CUSTOMER PROFILE

class CustomerForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email_address = StringField('Email Address')

    submit = SubmitField('Add Customer to Database')

@app.route('/addcustomer', methods=['GET', 'POST'])
def add_customer():
    error = ""
    form = CustomerForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email_address = form.email_address.data

        if len(first_name) == 0 or len(last_name) == 0 or len(email_address) == 0:
            error = "Please supply both first, last name and email"
        else:
            
            new_customer = models.Customer(first_name= form.first_name.data, last_name=form.last_name.data, email_address=form.email_address.data)
            db.session.add(new_customer)
            db.session.commit()

            return ('Done and Dusted, Another New Customer!')

    return render_template('addcustomer.html', form=form, message=error)

#Order

# class BasicForm(FlaskForm):
#     first_name = StringField('First Name')
#     last_name = StringField('Last Name')
#     contact_number = IntegerField('Mobile Number')

#     submit = SubmitField('Add Customer to Database')

# @app.route('/customerprofile', methods=['GET', 'POST'])
# def register():
#     error = ""
#     form = BasicForm()

#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         contact_number = form.contact_number.data

#         if len(first_name) == 0 or len(last_name) == 0:
#             error = "Please supply both first and last name"
#         else:
#             return ('thank_you', first_name)

#         if IntegerField(contact_number) == '0':
#             error = "Please Add Mobile Number"
#         else:
#             return ('Customer Has Been Added')

#     return render_template('customerprofile.html', form=form, message=error)

#PRODCUTS

class ProductForm(FlaskForm):
    product = StringField('Product Name')
    quantity = IntegerField('Product Quantity')
    price = IntegerField('Product Price')

    submit = SubmitField('Add Product to Database')

@app.route('/addproduct', methods=['GET', 'POST'])
def add_product():
    error = ""
    form = ProductForm()

    if request.method == 'POST':
        product = form.product.data
        quantity = form.quantity.data
        price = form.price.data

        if len(product) == 0 or len(quantity) == 0 or len(price) == 0:
            error = "Please Input both Product, Quantity and Price"
        else:
            
            new_product = Products(product=form.product.data, quantity=form.quantity.data, price=form.price.data)
            db.session.add(new_product)
            db.session.commit()

            return ('Nice One More Bikes Are On The Way!')

    return render_template('addproduct.html', form=form, message=error)


#CUSTOMER LIST

@app.route("/customerlist")
def customer_list():
    customer = models.Customer.query.all()
    return render_template("customerlist.html", customer=customer)

# PRODUCT LIST

@app.route("/productlist")
def product_list():
    product = models.Product.query.all()
    return render_template("productlist.html", product=product)

#ORDER LIST

@app.route("/orderlist")
def order_list():
    order = models.Order.query.all()
    return render_template("orderlist.html", order=order)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')