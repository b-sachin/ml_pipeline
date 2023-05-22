from flask import Flask
from housing.logger import lg
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def sample():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        # housing = HousingException(e, sys)
        raise HousingException(e, sys) from e
        lg.info(housing.error_message)
        lg.info("We are testing logging module")
    return "This is ML Project. This content added to test working of CI/CD pipeline."

if __name__=="__main__":
    app.run(debug=True)