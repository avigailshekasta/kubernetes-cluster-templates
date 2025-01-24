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
    current_price = get_bitcoin_price()  # חישוב המחיר הנוכחי
    bitcoin_prices.append(current_price)  # עדכון המחיר בתור המחירים
    average_price = calculate_average()  # חישוב המחיר הממוצע
    return render_template('index.html', current_price=current_price, average_price=average_price)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)