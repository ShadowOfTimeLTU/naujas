from game.game import Game
from sql_alchemy.db_management import DbManagement
from sql_alchemy.Models import Projektas

game = Game()
game.run()

# projektas = Projektas(name='Spinta', price=150, is_in_stock=True, location='Not given')

# db = DbManagement()
# # db.add_value(projektas)
# project_id = 1
# projektas = db.get_value_by_id(project_id)
# print(projektas)
# projektas = db.filter_by_name("Karve")
# print(projektas)
# projektas = db.update_value(2, "Karve", 1000)
# projektas = db.delete_value(2)

# attributes_to_filter = {
#     'name': 'Čiužinys',
#     'is_in_stock': True
# }
#
# matching_projektas = db.filter_by_attributes(attributes_to_filter)
#
# for projektas in matching_projektas:
#     print(f"Project Name: {projektas.name}")
#     print(f"Price: {projektas.price}")
#     print(f"Is in Stock: {projektas.is_in_stock}")
#     print(f"Location: {projektas.location}")
#     print(f"Create Date: {projektas.create_date}")
