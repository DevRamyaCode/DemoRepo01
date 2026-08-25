from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="student-db.c582isu0m6qe.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="YOUR-RDS-PASSWORD",
        database="student-db"
    )

@app.route("/")
def home():
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]

        db = get_db_connection()
        cursor = db.cursor()

        sql = "INSERT INTO students (name, course) VALUES (%s, %s)"
        cursor.execute(sql, (name, course))

        db.commit()

        cursor.close()
        db.close()

        return redirect("/")

    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete_student(id):

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()

    cursor.close()
    db.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
