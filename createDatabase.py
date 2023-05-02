import sqlite3


connection = sqlite3.connect('Job_Offers.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Offers
    (JobID TEXT, Job TEXT)''')

#try:
    #call api_pole_emploi.py
listOffers = ["test", "test", "test"]

cursor.executemany('INSERT INTO Offers VALUES (?,?,?)', listOffers)
records = cursor.execute("SELECT * FROM Offers")

print(cursor.fetchall())
for record in records:
    print(record)

#except:
    #print("problem when fetch out data from pole emploi .....")

connection.commit()
connection.close()