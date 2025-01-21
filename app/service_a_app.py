import time
import requests
from flask import Flask, jsonify,render_template
from collections import deque
from urllib.parse import quote as url_quote




app = Flask(__name__)


bitcoin_prices = deque(maxlen=10)  


def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"  
    response = requests.get(url)
    data = response.json()
    price = data['bpi']['USD']['rate']  
    return float(price.replace(",", ""))  


def calculate_average():
    if len(bitcoin_prices) == 0:
        return 0
    return sum(bitcoin_prices) / len(bitcoin_prices)


@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/current-price', methods=['GET'])
def current_price():
    price = get_bitcoin_price()  
    return jsonify({'current_price': price})

@app.route('/average-price', methods=['GET'])
def average_price():
    average = calculate_average()  
    return jsonify({'average_price_last_10_minutes': average})


def update_prices():
    while True:
        price = get_bitcoin_price()  
        bitcoin_prices.append(price)  
        time.sleep(60)  

if __name__ == '__main__':
   
    from threading import Thread
    thread = Thread(target=update_prices)
    thread.daemon = True
    thread.start()
    
    app.run(host='0.0.0.0', port=8080)
