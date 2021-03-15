from flask import url_for
from flask_testing import TestCase
from application import db
from application.models import Customer, Products, Orders
from datetime import datetime
from app import app

class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test registree
        customer = Customer(first_name = "Kelvin", last_name = "Bastow", email_address = "kelvinbastow@outlook.com")
        product = Products(product = "Canyon Ultimate CFR Disc Di2", quantity = "20", price = "8649")
        order = Orders(product_id = "1", customer_id = "1", quantity = "1", total_price = "8649", date_ordered = datetime.now())

        # save users to database
        db.session.add(customer)
        db.session.add(product)
        db.session.add(order)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestAddCustomer(TestBase):
    def test_add_customer(self):
        response = self.client.get(url_for('add_customer'))
        self.assertEqual(response.status_code, 200)

class TestAddProduct(TestBase):
    def test_add_products(self):
        response = self.client.get(url_for('add_product'))
        self.assertEqual(response.status_code, 200)

class TestAddOrder(TestBase):
    def test_add_order(self):
        response = self.client.get(url_for('add_order'))
        self.assertEqual(response.status_code, 200)

# # Test adding 
class TestAddCustomerDB(TestBase):
    def test_add_customer_db(self):
        response = self.client.post(
            url_for('add_customer'),
            data = dict(first_name = "Nathan", last_name = "Phillips", email_address = "nathanphillips@gmail.com"),
            follow_redirects=True
        )
        self.assertIn(b'Nathan',response.data)

class TestAddProductDB(TestBase):
    def test_add_product_db(self):
        response = self.client.post(
            url_for('add_product'),
            data = dict(product = "Canyon Ultimate CFR Disc EPS", quantity = "20", price = "9749"),
            follow_redirects=True
        )
        self.assertIn(b'Canyon Ultimate CFR Disc EPS',response.data)

class TestAddOrderDB(TestBase):
    def test_add_order_db(self):
        response = self.client.post(
            url_for('add_order'),
            data = dict(product_id = "2", customer_id = "2", quantity = "1", total_price = "9749", date_ordered = datetime.now()),
            follow_redirects=True
        )
        self.assertIn(b'2',response.data)