import requests
import json

#this function fetches the price from the binance API

def get_binance_btc_price():

    
    #this is the public API endpoints 
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    try:
        # sends a GET request to the API

        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")  
    except requests.exceptions.RequestException as e:
        # Handle any potential errors during the request
        print(f"An error occurred during the API request: {e}")

    return float(data["price"])


price = get_binance_btc_price()

print(f"Current Bitcoin (BTC/USDT) price: ${price}")