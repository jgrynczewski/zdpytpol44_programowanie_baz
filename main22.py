# Zasilanie bazy skryptem SQL
from sqlalchemy import create_engine

engine = create_engine('sqlite:///new_census2.sqlite')
connection = engine.connect()

with open('census.sql') as sql_file:
    stmt = sql_file.read()

stmt_list = [item.strip() for item in stmt.split(';')] # To zadziała ale
# tylko wtedy kiedy nie ma komentarzy w skrypcie. Sprawa się komplikuje

# Można zrobić brudny hack
result_proxy = connection.connection.connection.executescript(stmt)
# Poprawnie to trzebaby było napisać funkcje
# (conajmniej kilkunasto-linikową) parsującą skrypt sql
