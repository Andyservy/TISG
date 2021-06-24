import mysql.connector

# SELECT firstname, lastname, age FROM students WHERE age = @maxage;

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="76743571mysql",
    database="boost_mannager"
)

cursor = db.cursor()

name = "señora"

cursor.execute("SELECT Contraseña FROM login_history WHERE Nombre_User = '%s'" % name)
login_history = cursor.fetchall()

print(type(login_history[0][0]))
print(login_history[0][0])
