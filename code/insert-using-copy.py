import psycopg2

#connect to postrgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")
cur = conn.cursor()

#create table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users_using_copy(
        id serial PRIMARY KEY,
        email text, 
        name text,
        phone text,
        postal_code text
    )
    """
)

with open(r'D:\DIGITALSKOLA\PROJECT 3\source\users_w_postal_code.csv') as f:
    next(f)
    cur.copy_from(f,'users_using_copy', sep=',', columns=('email','name','phone','postal_code'))

conn.commit()

cur.execute(
    """
    SELECT * FROM users_using_copy
    """
)
all = cur.fetchall()
print(all)