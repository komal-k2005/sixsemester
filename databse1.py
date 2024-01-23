import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="your_password",
  database="mydatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Get the results
myresult = mycursor.fetchall()

# Print the results
for x in myresult:
  print(x)

# Close the connection
mydb.close()