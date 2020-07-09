from flask import Flask


# create flask app instance
app = Flask(__name__)

# single route /ping 
@app.route("/ping")
def ping():
    return "pong"

# set flask to bind on 0.0.0.0 so it can accept requests from any endpoint
if __name__ == "__main__":
    app.run(host='0.0.0.0')
