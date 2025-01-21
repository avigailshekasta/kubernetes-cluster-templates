import time
import requests
from flask import Flask, jsonify,render_template
from collections import deque
from urllib.parse import quote as url_quote




app = Flask(__name__)

# רשימה שתשמור את הערכים שנמשכו כל 10 דקות
bitcoin_prices = deque(maxlen=10)  # שומר עד 10 ערכים, ערך ישן יימחק כשיתווסף חדש

# פונקציה שמבצעת קריאה ל-API של הביטקוין ומחזירה את הערך הנוכחי
def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"  # ה-API שמחזיר את מחירי הביטקוין
    response = requests.get(url)
    data = response.json()
    price = data['bpi']['USD']['rate']  # מחזיר את המחיר בדולרים
    return float(price.replace(",", ""))  # ממיר את המחיר למספר ומסיר פסיקים

# פונקציה שתחישוב את ממוצע המחירים
def calculate_average():
    if len(bitcoin_prices) == 0:
        return 0
    return sum(bitcoin_prices) / len(bitcoin_prices)

# הגדרת קריאה לפורט 8080
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/current-price', methods=['GET'])
def current_price():
    price = get_bitcoin_price()  # משיכת מחיר הביטקוין הנוכחי
    return jsonify({'current_price': price})

@app.route('/average-price', methods=['GET'])
def average_price():
    average = calculate_average()  # חישוב ממוצע המחירים
    return jsonify({'average_price_last_10_minutes': average})

# פונקציה שתעדכן את המחירים כל דקה
def update_prices():
    while True:
        price = get_bitcoin_price()  # משיכת המחיר הנוכחי
        bitcoin_prices.append(price)  # הוספת המחיר לרשימה
        time.sleep(60)  # המתנה של דקה

if __name__ == '__main__':
    # הרצה של פונקציית עדכון המחירים ברקע
    from threading import Thread
    thread = Thread(target=update_prices)
    thread.daemon = True
    thread.start()
    
    app.run(host='0.0.0.0', port=8080)
