import datetime

from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length=100)
	joined_at = DateTimeField(default=datetime.now)
	is_admin = BooleaanField(default=False)

	class meta:
		database = DATABASE
		order_by = ('-joined_at',)