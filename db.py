import mysql.connector 
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect (
    host = os.getenv("DB_HOST"),
    user =os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)
cursor = conn.cursor()
print("Connected to MySQL Successfully!")

def close_db():
    print("closing database connections...")
    cursor.close()
    conn.close()
