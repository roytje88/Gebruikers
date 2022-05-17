import pandas as pd
import sqlite3
from sqlite3 import Error


def tableToDf(table, dbFile):
    import pandas as pd
    con = sqlite3.connect(dbFile)
    return pd.read_sql_query("SELECT * from "+table, con)





