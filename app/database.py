import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="shreya",
        database="employee_db"
    )