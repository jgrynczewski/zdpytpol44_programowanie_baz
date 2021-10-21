# SQL Injection 2 - prezentacja
import sqlalchemy as db

given_username = input("Podaj swój login: ")
given_password = input("Podaj hasło: ")

# Sprwadzamy na bazie czy wprowadzone przez użytkownika
# dane są poprawne (tj. czy istnieje taki user o nazwie
# <given_username> w bazie w tabeli user i jeżeli tak
# to czy hasło <given_password> zgadza się z tym hasłem
# w bazie.
engine = db.create_engine('sqlite:///users.sqlite')
connection = engine.connect()

metadata = db.MetaData()
user = db.Table(
    'user',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Tego nie wolno robić
# stmt = f"SELECT * FROM user WHERE username='{given_username}' AND password='{given_password}'"
# stmt = "SELECT * FROM user WHERE username='{}' AND password='{}'".format(given_username, given_password)
# stmt = "SELECT * FROM user WHERE username='%s' AND password='%s'" % (given_username, given_password)
# Wstrzyknięcie sql
# 'SELECT * FROM user WHERE username='sdvs' AND password='aegfaeg' OR 1=1--'

# Robimy tak
stmt = db.sql.text("SELECT * FROM user WHERE username=:username AND password=:password")
print(stmt)

results = connection.execute(
    stmt,
    username=given_username,
    password=given_password
).fetchall()

if results:
    print(f"\nWitaj {results[0].username}!")
else:
    print("\nBłędne poświadczenia")
