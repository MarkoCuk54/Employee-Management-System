from db_data import conn

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS admin;')
cur.execute('CREATE TABLE admin (id serial PRIMARY KEY, username varchar (20) NOT NULL, password varchar (50) NOT NULL)')

# Insert data into the table

cur.execute('INSERT INTO admin (username, password)'
            'VALUES (%s, %s)',
            ('marko54',
#https://x-team.com/blog/storing-secure-passwords-with-postgresql/ adding STORING PASSWORDS SECURELY WITH POSTGRESQL AND PGCRYPTO after deployment, dont work on windows 
             'emerus2705')
            )



conn.commit()
cur.close()
conn.close()