import peewee
from models.Users import Users


try:
    Users.create_table()
except peewee.OperationalError:
    print('Tabela Users ja existe!')