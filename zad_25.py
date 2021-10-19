# Obsługa dużych wyników
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census])

result_proxy = connection.execute((stmt))

# Zmienne pomocnicze
state_count = {}  # Słownik, w którym zliczamy liczbę
# wystąpień poszczególnych stanów w wyniku. Przykład
# {'New York': 234, 'Georgia': 423 ... }
# Zmienna pomocnicza pętli
more_results = True

# Pęlta while będzie iterowała dopóki wartość zmiennej more_results po zrzutowaniu
# na typ boolean ma wartość True
while more_results:
    # pobierz piersze 100 wpisów wykorzystujące do tego obiekt klasy ResultProxy
    partial_results = result_proxy.fetchmany(100)

    # Jeżeli wynik jest pustą listą ustaw more_result na False
    # (to spowoduje wyjście z pętli przy następnej iteracji)
    if partial_results == []:
        more_results = False

    # Przeiteruj się po rekordach w częściowym wyniku.
    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        # Jeżeli nazwa stanu z aktualnego wpisu znaduje się w słowniku
        if row.state in state_count:
            # Zwiększ licznik (wartość pod kluczem odopwiadającym nazwie stanu) dla
            # aktualnego stanu o 1
            state_count[row.state] += 1
        # W przeciwnym razie
        else:
            # Dodaj nowy klucz (nazwa stanu) i ustaw jego wartość na 1
            state_count[row.state] = 1

# Zamknij ResultProxy (a tym samym połączenie)
result_proxy.close()

# Wyświetl state_count
print(state_count)
