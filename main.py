from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Welcome to Home Page </h1>" 

@app.route("/add",methods=['POST'])
def addition():
    if request.method == "POST":
        result = request.json["num1"] + request.json["num2"]
        return jsonify("The summation is {}".format(result))
    


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)