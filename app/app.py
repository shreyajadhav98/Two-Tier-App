from flask import Flask, render_template, request, redirect
from database import get_connection

app = Flask(__name__)

# DATABASE = "employee.db"


# def get_connection():
#     conn = sqlite3.connect(DATABASE)
#     conn.row_factory = sqlite3.Row
#     return conn


# def create_table():
#     conn = get_connection()

#     conn.execute("""
#         CREATE TABLE IF NOT EXISTS employees(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             department TEXT NOT NULL,
#             salary INTEGER NOT NULL
#         )
#     """)

#     conn.commit()
#     conn.close()


# create_table()


@app.route("/")
def home():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
        """
        INSERT INTO employees
        (name,email,department,salary)
        VALUES(%s,%s,%s,%s)
        """,
        (name,email,department,salary)
        )

        conn.commit()

        cursor.close()
        conn.close()

        # conn.commit()
        # conn.close()

        return redirect("/")

    return render_template("add_employee.html")


@app.route("/delete/<int:id>")
def delete_employee(id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
    "DELETE FROM employees WHERE id=%s",
    (id,)
)

    conn.commit()

    cursor.close()
    conn.close()

    # conn.commit()
    # conn.close()

    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    conn = get_connection()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET
                name=%s,
                email=%s,
                department=%s,
                salary=%s
            WHERE id=%s
        """, (name, email, department, salary, id))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/")

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM employees WHERE id=%s",
        (id,)
    )

    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("edit_employee.html", employee=employee)


if __name__ == "__main__":
    app.run(debug=True)