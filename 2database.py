import sqlite3 as lite
import csv
import pandas as pd

con = lite.connect('jj_test.db')

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
    csvReader = csv.reader(open('cities.csv'), delimiter=',', quotechar='"')    
    for row in csvReader:
        con.execute('insert into cities (name, state) values (?, ?)', row)

    # populate the weather table from the weather.csv files 
    csvReader = csv.reader(open('weather.csv'), delimiter=',', quotechar='"')
    for row in csvReader:
        con.execute('insert into weather (city, year, warm_month, cold_month, average_high) values (?, ?, ?, ?, ?)', row)

#    cur.execute(".separator ","")
#    cur.execute(".import cities.csv cities")
#    cur.execute(".import weather.csv weather")

    # Write a script called "database.py" to print out the cities with the July being the warmest month
    cur.execute("select name from cities inner join weather on name = city where warm_month = 'July'")

    # Grap the results from the query
    rows = cur.fetchall()

    # Print out the results of the query
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    print df
