from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def my_form():
   return render_template("hello.html")

@app.route("/",methods=["POST"])
def my_form_post():
    text=request.form["text"]
    return text

