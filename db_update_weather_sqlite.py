import sqlite3 as lite

con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:

    cur = con.cursor()
    cur.execute("INSERT INTO weather VALUES('New York City', 2013, 'July', 'January', '62')")
    cur.execute("INSERT INTO weather VALUES('Boston', 2013, 'July', 'January', '59')")
    cur.execute("INSERT INTO weather VALUES('Chicago', 2013, 'July', 'January', '59')")
    cur.execute("INSERT INTO weather VALUES('Miami', 2013, 'August', 'January', '84')")
    cur.execute("INSERT INTO weather VALUES('Dallas', 2013, 'July', 'January', '77')")
    cur.execute("INSERT INTO weather VALUES('Seattle', 2013, 'July', 'January', '61')")
    cur.execute("INSERT INTO weather VALUES('Portland', 2013, 'July', 'December', '63')")
    cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December', '64')")
    cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December', '75')")
