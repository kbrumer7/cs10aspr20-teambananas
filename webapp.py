
from flask import Flask, render_template, request
import app
import json
import requests
app = Flask(__name__)

global state
state = {'current_currency':"", 'current_amount':"", 'goal_currency':"", 'final_amount':""}

@app.route('/')
@app.route('/main')
def main():
    return render_template('currencyconverter.html')


@app.route('/convert')
def convert_currency():
    global state


    return render_template('convert.html',state=state)


@app.route('/results',methods=['GET','POST'])
def results():
    global state
    current_currency = request.form['current_currency']
    current_amount = request.form['current_amount']
    goal_currency = request.form['goal_currency']
    state['current_currency'] = current_currency
    state['current_amount'] = current_amount
    state['goal_currency'] = goal_currency

    currency_exchange = requests.get('https://api.ratesapi.io/api/latest?base=USD')
    currency_exchange = currency_exchange.text
    currency_exchange = json.loads(currency_exchange)
    """take out base USD and rates"""
    currency_exchange = currency_exchange['rates']

    print(currency_exchange)


    return render_template('results.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
