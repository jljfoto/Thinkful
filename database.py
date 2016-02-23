import sqlite3 as lite
import csv
import pandas as pd

con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:

    # Open a connection to the database and drop the cities and weather tables if they exist
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    
    # Create the cities and weather tables
    cur.execute("create table cities (name text, state text)")
    cur.execute("create table weather (city text, year integer, warm_month text, cold_month text, average_high integer)")

    # populate the cities table from the saved cities.csv files
    #csvReader = csv.reader(open('cities.csv'), delimiter=',', quotechar='"')
    #for row in csvReader:
    #    con.execute('insert into cities (name, state) values (?, ?)', row)

    # populate the weather table from the weather.csv files
    #csvReader = csv.reader(open('weather.csv'), delimiter=',', quotechar='"')
    #for row in csvReader:
    #    con.execute('insert into weather (city, year, warm_month, cold_month, average_high) values (?, ?, ?, ?, ?)', row)

    # populate the cities table 
    cur.execute("INSERT INTO cities (name, state) VALUES ('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'), ('Miami', 'FL'), ('Dallas', 'TX'), ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA'), ('Los Angeles', 'CA')")

    # populate the weather table 
    cur.execute("INSERT INTO weather VALUES('New York City', 2013, 'July', 'January', '62')")
    cur.execute("INSERT INTO weather VALUES('Boston', 2013, 'July', 'January', '59')")
    cur.execute("INSERT INTO weather VALUES('Chicago', 2013, 'July', 'January', '59')")
    cur.execute("INSERT INTO weather VALUES('Miami', 2013, 'August', 'January', '84')")
    cur.execute("INSERT INTO weather VALUES('Dallas', 2013, 'July', 'January', '77')")
    cur.execute("INSERT INTO weather VALUES('Seattle', 2013, 'July', 'January', '61')")
    cur.execute("INSERT INTO weather VALUES('Portland', 2013, 'July', 'December', '63')")
    cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December', '64')")
    cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December', '75')")

    # Write a script called "database.py" to print out the cities with the July being the warmest month
    cur.execute("select name from cities inner join weather on name = city where warm_month = 'July'")

    # Grap the results from the query
    rows = cur.fetchall()

    # Print out the results of the query
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    print df
