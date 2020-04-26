
from flask import Flask, render_template, request
import app
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
    current_currency = request.form['current_currency']
    current_amount = request.form['current_amount']
    goal_currency = request.form['goal_currency']

	return render_template('convert.html',state=state)


@app.route('/results')
def results():
    global state


    return render_template('results.html',state=state)




if __name__ == '__main__':
	app.run('0.0.0.0',port=3000)
