import peewee

db = peewee.SqliteDatabase('codigo_avulso.db')

class Users(peewee.Model):
    name = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()

    class Meta:
        database = db