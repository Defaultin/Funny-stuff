import mysql.connector as MySql
import datetime 
import yaml
import ast

__author__ = 'Kirill Klimenko'
__all__ = ('YAMLDB', 'yaml')


class YAMLDB:
	'''
	Some custom YAML to MySQL API.
	Each table must be in a separate YAML file.

	.yaml
	table_name:
	  - field1: ...
		field2: ...
		...
	  - field1: ...
		field2: ...
		...
	  - ...

	.py
	db = YAMLDB(username, password, database_name)
	db.create_yaml_table(table_name, '*.yaml')
	'''

	def __init__(self, user, password, db_name, *, host='localhost'):
		self.db_name = db_name
		self.tables = []
		self.db_name = db_name
		try:
			self.database = MySql.connect(
				host=host,
				user=user,
				password=password
			)
			self.cursor = self.database.cursor()
			self.cursor.execute(f'drop database if exists {db_name}')
			self.cursor.execute(f'create database {db_name}')
			self.cursor.execute(f'use {db_name}')
		except Exception as err:
			raise ConnectionError(f'Failure to connect to MySQL server!\n{err}')


	def create_yaml_table(self, table_name, yaml_file):
		'''Create table by YAML file'''
		self.tables.append(table_name)
		with open(yaml_file, 'r') as file:
			yaml_table = yaml.load(file)
			types = [i for i in yaml_table[table_name][0].values()]
			types = self.types_mapping(types[1:]) 		# without an id
			fields = yaml_table[table_name][0].keys()
			fields = list(fields)[1:] 					# without an id

			self.create_table(table_name)
			for field_name, field_type in zip(fields, types):
				self.add_column(table_name, field_name, field_type)

			params = ','.join([str(i) for i in fields])
			for vals in yaml_table[table_name]:
				vals_lst = list(vals.values())[1:]
				v = ','.join([f'"{i}"' for i in vals_lst])
				self.insert(table_name, params, v)

			self.database.commit()


	def create_table(self, table_name):
		self.cursor.execute(f'create table {table_name} (id int auto_increment primary key)')
		self.database.commit()


	def add_foreign_key(self, table_name, ref_table, ref_field):
		self.add_column(table_name, ref_field, 'int')
		self.cursor.execute(f'alter table {table_name} add foreign key ({ref_field}) references {ref_table}(id)')
		self.database.commit()


	def add_column(self, table_name, column, column_type):
		self.cursor.execute(f'alter table {table_name} add column {column} {column_type}')
		self.database.commit()


	def delete_column(self, table_name, column):
		self.cursor.execute(f'alter table {table_name} drop column {column}')
		self.database.commit()


	def update_table(self, table_name, field, value, id):
		self.cursor.execute(f'update {table_name} set {field} = {value} where id = {id}')
		self.database.commit()


	def insert(self, table_name, params, values):
		self.cursor.execute(f'insert into {table_name} ({params}) values ({values})')
		self.database.commit()


	def select(self, table_name, query):
		self.cursor.execute(f'select {query} from {table_name}')
		return self.cursor.fetchall()


	def types_mapping(self, types):
		sql_types = []
		for t in types:
			if isinstance(t, int):
				sql_types.append('int')
			elif isinstance(t, float):
				sql_types.append('float')
			elif isinstance(t, bool):
				sql_types.append('boolean')
			elif isinstance(t, str):
				sql_types.append('text')
			elif isinstance(t, datetime.date):
				sql_types.append('date')
			elif isinstance(t, datetime.datetime):
				sql_types.append('datetime')
			else:
				sql_types.append('blob')

		return sql_types