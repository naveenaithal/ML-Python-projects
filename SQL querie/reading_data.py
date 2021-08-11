import pandas as pd
import sqlite3


con = sqlite3.connect("customer_data.db")
df = pd.read_sql_query("SELECT * from patient_details1", con)


print(df.head())

con.close()
