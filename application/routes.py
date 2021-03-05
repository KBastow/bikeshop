from application import app, db
from application.models import 

first_customer=Customer(first_name="Kelvin", last_name="Bastow", email_address= 'Kelvinb97@outlook.com')
db.session.add(first_customer)
db.session.commit()

# second_order=Orders(fk_user_id= "1", product_ordered= "Canyon Ultimate CF SLX 8 Disc eTap", price= "5499", order_date= "2020/12/25")
# db.session.add(second_order)
# db.session.commit()

# from application import app, db
# from application.models import Games

# @app.route('/add')
# def add():
#     new_game = Games(name="New Game")
#     db.session.add(new_game)
#     db.session.commit()
#     return "Added new game to database"

# @app.route('/read')
# def read():
#     all_games = Games.query.all()
#     games_string = ""
#     for game in all_games:
#         games_string += "<br>"+ game.name
#     return games_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name

# @app.route('/delete/<name>')
# def delete(name):
#     game_to_delete = Games.query.first()
#     db.session.delete(game_to_delete)
#     db.session.commit()
#     return "Game Deleted From Database"