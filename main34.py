# XML
import sqlalchemy as db
import xmltodict

with open('census.xml') as xml_file:
    data = xml_file.read()

fixtures = xmltodict.parse(data, dict_constructor=dict)
fixtures = fixtures['data']['row']

engine = db.create_engine("sqlite:///census10.sqlite")
connection = engine.connect()

metadata = db.MetaData()
new_table = db.Table(
    'census',
    metadata,
    db.Column('state', db.String(30)),
    db.Column('sex', db.String(1)),
    db.Column('age', db.Integer()),
    db.Column('pop2000', db.Integer()),
    db.Column('pop2008', db.Integer())
)
new_table.create(bind=engine)

stmt = db.insert(new_table)

result = connection.execute(stmt, fixtures)
print(result.rowcount)