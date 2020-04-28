
from flask import Flask, render_template, request
import app
import json
import requests
import csv
app = Flask(__name__)

global state
state = {'current_currency':"",
        'current_amount':"",
        'goal_currency':"",
        'final_amount':"",
        'code':"",
        'unit_dollar':"",
        'current_dollar':"",
        'goal_code':"",
        'goal_unit_dollar':"",
        'final_currency':"",
        'this_currency':""
        }

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

    abbreviations = list(csv.DictReader(open('abrreviations.csv','r'),delimiter=','))
    for i in abbreviations:
        if state['current_currency'].upper() == (i['Country']).upper() or state['current_currency'].upper() == (i['Currency'].upper()):
            state['code'] = i['Code']
            state['this_currency'] = i['Currency']
    for a in currency_exchange:
        if state['code'] in a:
            state['unit_dollar']=currency_exchange[a]
    state['current_dollar']=float(state['current_amount'])/float(state['unit_dollar'])
    for w in abbreviations:
        if state['goal_currency'].upper() == (w['Country']).upper() or state['goal_currency'] == (w['Currency']).upper():
            state['goal_code'] = w['Code']
            state['final_currency'] = w['Currency']
    for b in currency_exchange:
        if state['goal_code'] in b:
            state['goal_unit_dollar']=currency_exchange[b]
    state['final_amount']=float(state['goal_unit_dollar'])*float(state['current_dollar'])
    state['final_amount']=round(state['final_amount'],4)


    return render_template('results.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
