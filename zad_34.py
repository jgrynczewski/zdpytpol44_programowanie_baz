# Drop (usuwanie wszystkich tabel)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///census4.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)
state_fact = Table(
    'state_fact',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Usuń tablę state_fact (metoda drop obiektu Table)
____

# Sprawdź czy tabela state_fact istnieje w bazie
print(____)

# Usuń wszystkie tabele bazy (metoda drop_all obiektu MetaData)
____

# Sprawdź czy tabela census istnieje
print(____)
