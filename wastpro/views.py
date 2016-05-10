"""
Routes and views for the flask application.
"""
from datetime import datetime
from iapws import IAPWS97
from flask import render_template,request,url_for
from wastpro import app

@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title = 'Home',
        year = datetime.now().year,
        solution = "the solution shows here!")

@app.route('/solution', methods=['POST'])
def solution():
    """Renders the home page with the results."""
    param1, param2, findparam = getparams()
    calculatedValue = IAPWS97(T=param1, P=param2)
    #findparameter = calculate(parameters)
    return render_template(
        'index.html',
        title = 'Results',
        year = datetime.now().year,
        viewsolution = findparameter)

def getparams():
    if request.method == 'POST':
        parameter1 = int(request.form['param1'])
        parameter2 = int(request.form['param2'])
        findparameter = str(request.form['findparam'])
        return parameter1, parameter2, findparameter
    else:
        pass

def calculate(tuple):
    calculatedValue = IAPWS97(T=tuple[0], P=tuple[1])
    return calculatedValue.tuple[2]

