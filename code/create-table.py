import psycopg2
import csv


#connect to postrgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")
cur = conn.cursor()

#create table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS latihan_users(
        id serial PRIMARY KEY,
        email text, 
        name text,
        phone text,
        postal_code text
    )
    """
)

#naro data csv ke table
with open(r'D:\DIGITALSKOLA\PROJECT 3\source\users_w_postal_code.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        cur.execute('INSERT INTO latihan_users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING', row)

conn.commit()

cur.execute(
    """
    SELECT * FROM latihan_users
    """
)

# result
one = cur.fetchone()
all = cur.fetchall()