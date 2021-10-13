from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Stwórz połączenie z bazą
connection = engine.connect()

# Zbuduj instrukcję select do tabeli census
stmt = 'SELECT * FROM census'

# Wykonaj zapytanie i pobierz wynik
results = connection.execute(stmt).fetchall()

# Wyświetl wynik
print(results)
