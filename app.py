from flask import Flask
from housing.logger import lg

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def sample():
    lg.info("We are testing logging module")
    return "This is ML Project. This content added to test working of CI/CD pipeline."

if __name__=="__main__":
    app.run(debug=True)