from flask import Flask, render_template,request,redirect,url_for
from pymongo import MongoClient # Database connector
from forms import SignupForm
from models import User

#database config
mongo_uri = 'MONGO URI'
client = MongoClient(mongo_uri)    #Configure the connection to the database
#db = client["flask_api_test"]
users = client["users"]

app = Flask(__name__)

app.secret_key = "dev-key"
@app.route("/")
def index():
    #print(users.find_one({"firstname": "Michael"}))
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    sform = SignupForm()
    if request.method == "POST":
        if sform.validate() == False:
            return render_template("signup.html",form= sform)
        #create a user instlance
        user = User(sform.firstname, sform.lastname, sform.email, sform.password)
        users.insert_one({"username":user.fn, "lastname": user.ln, "email":user.email, "password":user.pwd})
        return "success"
    return render_template("signup.html",form= sform)

@app.route("/signin", methods = ["GET", "POST"])
def signin():
    sform = SignupForm()
    if request.method == "POST":
        if sform.validate() == False:
            return render_template("signin.html",form= sform)
        return "success"
    return render_template("signin.html",form= sform)

if __name__ == "__main__":
    app.run(debug=True)
