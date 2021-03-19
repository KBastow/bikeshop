# Bike Shop
Author: Kelvin Bastow

# Project

My project is to build an application allowing a bike shop to organise their customers, products and orders. With a list of bikes in stock, a customer list with relevant information, and then an order list to allow easy referencing to completed orders.

# Requirements

A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project.

A relational database used to store data persistently for the project, this database needs to have at least 2 tables in it, to demonstrate your understanding, you are also required to model a relationship.

Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment. A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board.

Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach.

A functioning front-end website and integrated API's, using Flask. Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

# Trello Board

![Trello Board](/images/trelloboard.jpg)

My Trello Board Progression, with a link to the most recent version [here][trello-link]!

This shows you my backlog of tasks, what is currently being worked on and also what has been completed.

[trello-link]: https://trello.com/b/I7coDWDj/bikeshop

# Database Diagram

![Database Diagram](/images/bikeshoptables.png)

This is a diagram showing how my databases interact with each other, whilst this diagram shows 6 databases, there are only three. 'Add Customer' and 'Add Product' are separate tables, and then when you input the data into the text boxes and completing the required Info this will then update the data base and take you to the relevant page (Customer/Product List), then you can create an 'Order', again inputting the required data and this will then create an order and then once the order has been created, will take you to the 'Order List' Page.

# My Development Pipeline

![BikeShopPipeline](/images/bikeshoppipeline.png)

This is a diagram showing you the flow of my pipeline and how I have integrated all that we have been taught.
MySQL database is hosted on GCP along with my Virtual Machine (VM). All my code is then written in VsCode, which is installed on my VM, and this is linked to my GitHub repository. All my changes are pushed to my develop branch to make sure that there are no conflicts between branches. Then my testing is again written in VsCode and is tested using pytest, this is to make sure that there are no errors in my code and that the pass rate returns at 80% or above. If successful and the pass rate is above 80%, the code is then pushed to my develop branch before merging with the master branch. If unsuccessful, or the pass rate is lower than 80% then I return to the previous step and check the errors in my code and fix any issues. Once the code has been pushed to my master branch, Jenkins can run and host the live application.

# Test Results

![pytestapplication](/images/pytestapplication.jpg)

![pytestapp](/images/pytestapp.jpg)

Here are a few images showing you the test results for my application folder and also my app.py file, this shows the amount of tests I have created and also the pass rates for each file as well.

# Risk Assessment

![riskassesment](/images/riskassessment.jpg)


# Refrences

- All my knowledge has been given to me from my teacher Dara Oladapo :)
- All me teaching had been from https://qa-community.co.uk/~/_/learning
- For any HTML querys I used https://www.w3schools.com/html/default.asp
- For any of my python querys I used https://thepythonguru.com/ and https://www.w3schools.com/python/default.asp
