import pandas as pd
from sqlalchemy import create_engine
import os

df = pd.read_csv(r'D:\DIGITALSKOLA\PROJECT 3\source\users_w_postal_code.csv', sep=',')
engine = create_engine('postgresql://postgres:digitalskola@127.0.0.1:5432/postgres')

df.to_sql("from_file_table", engine)

df_read = pd.read_sql("select * from from_file_table",engine)