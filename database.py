import pymysql as mysql
from dotenv import load_dotenv
import os

load_dotenv()

database = mysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'), 
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create database
cursorObject.execute("CREATE DATABASE gastosempleado")

print("Database Created")
