# Update (pojedynczy wiersz)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
state_fact = Table(
    'state_fact',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Zadanie polega na aktualizacji pola fips_state
# dla Nowego Jorku w tabeli fact_state (na wartość 32).

# 1. Najpierw sprawdź jaką ma aktualnie wartość w polu
# fips_state wpis dla Nowego Jorku

# 1. Zbuduj zapytanie o wpis z tabeli state_facts
# dla którego wartość w polu name wynosi 'New York'
select_stmt = select([____]).where(____ == ____)

# Wykonaj zapytanie i pobierz wynik (fetchall)
results = connection.____(____).____()

# Wyświetl kod FIPS wyniku
print(results[0]['___'])  # -> 36

# 2. Teraz zaktualizuj tą wartość (zmień na 32)

# Zaimportuj funkcję update z sqlalchemy
from sqlalchemy import ____

# Zbuduj zapytanie, które zaktualizauje wartości w kolumnie
# fips_state tabeli state_facts na 32
update_stmt = update(state_fact).values(____ = ____)

# Aktualizacja ma dotyczyć tylko rekordu dla Nowego Jorku
update_stmt = update_stmt.where(____ == ____)

# Wykonaj zapytanie
update_results = connection.execute(____)

# 3. Sprawdź, czy wartość została zmieniona
# Ponownie wykonaj zapytanie o wpis dla Nowego Jorku
# (sqlke mamy już przygotowaną - select_stmt, więc nie
# trzeba jej ponownie tworzyć, możemy ją wykorzystać)
new_results = ____.____.____

# Wyświetl kod FIPS wyniku
print(results[0]['___'])  # -> 32
