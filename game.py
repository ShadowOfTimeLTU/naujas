from sql_alchemy.Models import Projektas
from sql_alchemy.db_management import DbManagement


class Game(DbManagement):

    def insert_data_in_db(self):
        try:
            name = input('Enter the object name: ')
            price = float(input('Enter object price: '))
            is_in_stock = input('Is the object in stock? (True/False): ')
            is_in_stock = is_in_stock.strip().lower()

            if is_in_stock == "true":
                is_in_stock = True
            elif is_in_stock == "false":
                is_in_stock = False
            else:
                raise ValueError('is_in_stock. Please enter True or False.')
            location = input('Enter the object location: ')

            project = Projektas(name=name, price=price, is_in_stock=is_in_stock, location=location)
            self.add_value(project)
            print('Project added successfully!')
        except ValueError as e:
            print(f'Invalid input: {str(e)} Please enter a valid data.')

    def delete_object(self):
        object_id = int(input('Enter the ID to delete: '))
        object = self.get_value_by_id(object_id)
        if object:
            self.delete_value(object_id)
            print(f'Object with ID {object_id} deleted successfully!')
        else:
            print(f'Object with ID {object_id} not found.')

    def run(self):
        while True:
            print('Menu:')
            print('1. Add a new object')
            print('2. Delete an object by ID')
            print('3. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':
                self.insert_data_in_db()
            elif choice == '2':
                self.delete_object()
            elif choice == '3':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please choose a valid option.')
