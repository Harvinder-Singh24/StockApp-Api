
from flask import Flask,request,jsonify
import yfinance
app = Flask(__name__)

#variables
nse_symbol = ".NS"

# get the current price of the stock
def get_current_price(symbol):
    global nse_symbol
    ticker = yfinance.Ticker(symbol + nse_symbol)
    if (ticker.info['regularMarketPrice'] is None) :
        return 0
    else:
        todays_data = ticker.history(period='1d')
        print(todays_data)
        price = f"{todays_data['Close'][0]:.2f}"
        print(f"Price {int(float(price))}")
        return int(float(price))

@app.route('/stock',methods=['GET']) 
def stock_route():
    name = request.args.get('name')
    market_price = get_current_price(name)
    if market_price == 0:
        return '''<h1>Invalid Stock </h1>'''
    else :
        return jsonify({"Price": market_price})

@app.route('/')
def welcome():
    return "Hello World"

if __name__ == '__main__' :
    app.run(debug=True)