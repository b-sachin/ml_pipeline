from flask import Flask

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def sample():
    return "This is ML Project. This content added to test working of CI/CD pipeline."

if __name__=="__main__":
    app.run(debug=True)