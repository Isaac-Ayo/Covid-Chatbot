from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

# decorating and linking html
@app.get("/")
def index_get():
    return render_template("base.html")


# decorating and getting return for the messages
@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)





