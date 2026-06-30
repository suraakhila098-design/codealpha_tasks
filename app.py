from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    message = ""

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        cursor.execute(
            "SELECT * FROM users WHERE email=? OR phone=?",
            (email, phone)
        )

        data = cursor.fetchone()

        if data:
            message = "Duplicate Record Found!"

        else:
            cursor.execute(
                "INSERT INTO users(name,email,phone) VALUES(?,?,?)",
                (name, email, phone)
            )

            conn.commit()
            message = "Record Saved Successfully!"

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("index.html",
                           users=users,
                           message=message)

if __name__ == "__main__":
    app.run(debug=True)