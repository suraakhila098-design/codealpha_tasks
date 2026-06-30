from flask import Flask, render_template, request, jsonify

app = Flask(__name__,template_folder="templates",static_folder="static")

responses = {
    "hello": "Hi! How can I help you?",
    "bye": "Goodbye!",
    "python": "Python is a programming language.",
    "cloud": "Cloud Computing provides computing services over the internet."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"].lower()
    reply = responses.get(message, "Sorry, I don't understand.")
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)