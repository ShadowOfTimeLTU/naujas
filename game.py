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

    def update_values(self):
        object_id = int(input('Enter the ID to update: '))
        object_to_update = self.get_value_by_id(object_id)

        if object_to_update:
            try:
                update_fields = {
                    'name': input('Enter the updated object name (press Enter to keep current): '),
                    'price': input('Enter the updated object price (press Enter to keep current): '),
                    'is_in_stock': input('Is the object in stock? (True/False) (press Enter to keep current): '),
                    'location': input('Enter the updated object location (press Enter to keep current): ')
                }

                for field, value in update_fields.items():
                    if value:
                        if field == 'price':
                            value = float(value)
                            if value <= 0:
                                raise ValueError('Price must be a positive number.')
                        elif field == 'is_in_stock':
                            value = value.strip().lower()
                            if value not in ("true", "false"):
                                raise ValueError('is_in_stock. Please enter True or False.')

                        setattr(object_to_update, field, value)

                self.commit_changes()
                print(f'Object with ID {object_id} updated successfully!')

            except ValueError as e:
                print(f'Invalid input: {str(e)} Please enter valid data.')
        else:
            print(f'Object with ID {object_id} not found.')

    def run(self):
        while True:
            print('Menu:')
            print('1. Add a new object')
            print('2. Delete an object by ID')
            print('3. Update an object by ID')
            print('4. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':
                self.insert_data_in_db()
            elif choice == '2':
                self.delete_object()
            elif choice == '3':
                self.update_values()
            elif choice == '4':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please choose a valid option.')
