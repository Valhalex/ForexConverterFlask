from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbar
from forex_python.converter import CurrencyRates
from handleForm import Survey
app = Flask(__name__)
c = CurrencyRates()
result=[]
msg=''
@app.route("/")
def home_page():
    """Loads home page where user can enter their first conversion"""
    return render_template('index.html')

@app.route("/conversion")
def show_conversion():
    """shows the users conversion"""
    
    return render_template('convSubmit.html', result=result, msg=msg)

@app.route("/conversion/new", methods=["POST"])
def add_conversion():
    """clear old conversion from list and add new"""
    survey = Survey(request.form["convertFrom"], request.form["convertTo"], request.form["value"])
    
    try:
        result.append(survey.convertCurrency())
 
    except:
        msg= "invalid"
        return render_template("convSubmit.html", msg=msg)
    
    
    return redirect("/conversion")