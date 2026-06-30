from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/apply", methods=["GET", "POST"])
def apply():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        pass_type = request.form["pass_type"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email, phone, route) VALUES (?, ?, ?, ?)",
            (name, email, mobile, pass_type)
        )

        conn.commit()
        conn.close()

        return f"""
        <h2>Application Submitted Successfully!</h2>

        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Mobile: {mobile}</p>
        <p>Pass Type: {pass_type}</p>

        <a href="/">Go Home</a>
        """

    return render_template("apply.html")

if __name__ == "__main__":
    app.run(debug=True)