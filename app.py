from application import app, models, db
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, IntegerField, DecimalField
from datetime import datetime
import sys

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

#CUSTOMER PAGE

class CustomerForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email_address = StringField('Email Address')

    submit = SubmitField('Add Customer to Database')

#This then creates the main directory aka the homepage where everything falls back onto
@app.route('/', methods =['GET', 'POST'])
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
            try:
                new_customer = models.Customer(first_name= form.first_name.data, last_name=form.last_name.data, email_address=form.email_address.data)
                db.session.add(new_customer)
                db.session.commit()
                return redirect('/customerlist')
            except:
                error = "This Name Has Already Been Added"

    return render_template('addcustomer.html', form=form, message=error)

#PRODCUTS PAGE

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

        if len(product) == 0 or len(str(quantity)) == 0 or len(str(price)) == 0:
            error = "Please Input both Product, Quantity and Price"
        else:
            
            new_product = models.Products(product=form.product.data, quantity=form.quantity.data, price=form.price.data)
            db.session.add(new_product)
            db.session.commit()

            return redirect('/productlist')

    return render_template('addproduct.html', form=form, message=error)

#ORDER PAGE

class OrderForm(FlaskForm):
    product_id = IntegerField('Product iD')
    customer_id = IntegerField('Customer iD')
    quantity = IntegerField('Quantity')
    total_price = IntegerField('Total Price')
    date_ordered = DateTimeField('Date Ordered')

    submit = SubmitField('Submit Order')

@app.route('/addorder/<int:pid>/<int:cid>', methods=['GET', 'POST'])
def add_order(pid, cid):
    error = ""
    form = OrderForm()
    form.product_id.data = pid
    form.customer_id.data = cid
    form.date_ordered.data = datetime.now()

    if request.method == 'POST':
        product_id = form.product_id.data
        customer_id = form.customer_id.data
        quantity = form.quantity.data
        total_price = form.total_price.data
        date_ordered = form.date_ordered.data

        if len(str(quantity)) == 0 or len(str(total_price)) == 0:
            error = "Please Add Quantity and Price"
            
        else:
            new_order = models.Orders(product_id= form.product_id.data, customer_id= form.customer_id.data, quantity= form.quantity.data, total_price= form.total_price.data, date_ordered= form.date_ordered.data)
            db.session.add(new_order)
            db.session.commit()

            return redirect('/orderlist')

    return render_template('addorder.html', form=form, message=error)

#CUSTOMER LIST

@app.route("/customerlist")
def customer_list():
    customer = models.Customer.query.all()
    # return render_template()
    # return redirect('/productlist')
    return render_template("customerlist.html", customer=customer)

# PRODUCT LIST

@app.route("/productlist")
def product_list():
    product = models.Products.query.all()
    customer = models.Customer.query.all()
    return render_template("productlist.html", product=product, customer=customer)

# PRODUCT LIST FOR CUSTOMER

@app.route("/productlist/<int:cid>")
def product_list_for_customer(cid):
    product = models.Products.query.all()
    return render_template("productlist_c.html", product=product, cid=cid)

#ORDER LIST

@app.route("/orderlist")
def order_list():
    order = models.Orders.query.all()
    return render_template("orderlist.html", order=order)

#UPDATE ORDER

@app.route('/updateorder/<int:oid>', methods=['GET','POST'])
def update_order(oid):
    order_to_update = models.Orders.query.filter_by(id=oid).first()
    error = ""
    form = OrderForm()

    if request.method == 'POST':
        order_to_update.product_id = form.product_id.data
        order_to_update.customer_id = form.customer_id.data
        order_to_update.quantity = form.quantity.data
        order_to_update.total_price = form.total_price.data
        order_to_update.date_ordered = form.date_ordered.data

        if len(str(form.quantity.data)) == 0 or len(str(form.total_price.data)) == 0:
            error = "Please Add Quantity and Price"
            
        else:
            db.session.commit()
            return redirect('/orderlist')

    else:
        form.product_id.data = order_to_update.product_id
        form.quantity.data = order_to_update.quantity
        form.total_price.data = order_to_update.total_price
        form.date_ordered.data = order_to_update.date_ordered
    

    return render_template('addorder.html', form=form, message=error)

#DELETE CUSTOMER

@app.route("/deletecustomer/<int:cid>")
def delete_customer(cid):
    customer_to_delete = models.Customer.query.filter_by(id=cid).first()
    db.session.delete(customer_to_delete)
    db.session.commit()
    return redirect("/customerlist")

#DELETE PRODUCT

@app.route("/deleteproduct/<int:pid>")
def delete_product(pid):
    order_to_delete = models.Products.query.filter_by(id=pid).first()
    db.session.delete(order_to_delete)
    db.session.commit()
    return redirect("/productlist")

#DELETE ORDER

@app.route("/deleteorder/<int:oid>")
def delete_order(oid):
    order_to_delete = models.Orders.query.filter_by(id=oid).first()
    db.session.delete(order_to_delete)
    db.session.commit()
    return redirect("/orderlist")

#This code then allows the application to run from the app.py code
if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
#You then type python3 app.py in the termainal and voila