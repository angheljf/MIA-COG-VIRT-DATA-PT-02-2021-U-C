from flask import Flask, jsonify


app = Flask(__name__)

hello_dict = {"Hello": "World!"}


@app.route("/")
def home():
    return "Hi"


@app.route("/normal")
def normal():
    print('we are running normal')
    return hello_dict


@app.route("/jsonified")
def jsonified():
    print('we are running jsonified')
    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)
