import csv
abbreviations = list(csv.DictReader(open('abrreviations.csv','r'),delimiter=','))
abbreviations

import requests
import json
currency_exchange = requests.get('https://api.ratesapi.io/api/latest?base=USD')
currency_exchange = currency_exchange.text
currency_exchange = json.loads(currency_exchange)
"""take out base USD and rates"""
currency_exchange = currency_exchange['rates']


"""Ask for their current currency"""
def convert_currency():
    print("Convert your currency!!")
    current_currency=input("What is the country of the currency that you currently have?\n>>>")
    for i in abbreviations:
        if current_currency.upper() == (i['Country']).upper() or current_currency.upper() == (i['Currency']).upper():
            code = i['Code']
    current_amount=input("How much do you have?\n>>>")
    for a in currency_exchange:
        if code in a:
            unit_dollar=currency_exchange[a]
    current_dollar=float(current_amount)/float(unit_dollar)
    goal_currency=input("What country's currency would you like to convert it to?\n>>>")
    for w in abbreviations:
        if goal_currency.upper() == (w['Country']).upper() or goal_currency.upper() == (w['Currency']).upper():
            goal_code = w['Code']
    for b in currency_exchange:
        if goal_code in b:
            goal_unit_dollar=currency_exchange[b]
    goal_amount=float(goal_unit_dollar)*float(current_dollar)
    goal_amount=round(goal_amount,4)
    print("Your final amount is",str(goal_amount)+"!")
    return

if __name__ == '__main__':
    convert_currency()
