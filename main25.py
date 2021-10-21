# SQL Injection 1 - stworzenie bazy do prezentacji sql injection
import sqlalchemy as db

engine = db.create_engine("sqlite:///users.sqlite")
connection = engine.connect()

metadata = db.MetaData()
user = db.Table(
    'user',
    metadata,
    db.Column('id', db.Integer(), primary_key=True),
    db.Column('username', db.String(128)),
    db.Column('password', db.String(256))
)
metadata.create_all(engine)

data = [
    {
        "id": 1,
        "username": "Joe",
        "password": "12345"
    },
    {
        "id": 2,
        "username": "Bob",
        "password": "abcdef"
    },
    {
        "id": 3,
        "username": "Eva",
        "password": "qwerty"
    },
]

stmt = db.insert(user)

result_proxy = connection.execute(stmt, data)
print(result_proxy.rowcount)
