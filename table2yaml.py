import mysql.connector
import yaml


database = mysql.connector.connect(
	host='localhost',
	user='root',
	password='1210525',
	database='world'
)


def table_to_yaml(table_name, file_name):
	cur = database.cursor()
	cur.execute(f'desc {table_name}')
	query = cur.fetchall()

	titles = [item[0] for item in query]

	cur.execute(f'select * from {table_name}')
	query = cur.fetchall()

	countries = {country[1]: {k: v for k, v in zip(titles, country)} for country in query}

	with open(file_name, 'w') as file:
		yaml_doc = {'Countries': countries}
		yaml.dump(yaml_doc, file)


def read_yaml(file_name, country):
	with open(file_name, 'r') as file:
		countries = yaml.load(file)
		return countries['Countries'][country]


if __name__ == '__main__':
	yaml_file = 'countries.yaml'
	table_to_yaml('world.country', yaml_file)
	print(read_yaml(yaml_file, 'Belarus'))