from sqlalchemy import create_engine
from game import Game

db_file_path = 'sql_alchemy/projektai.db'

engine = create_engine(f'sqlite:///{db_file_path}')

game = Game(engine)

game.run()
