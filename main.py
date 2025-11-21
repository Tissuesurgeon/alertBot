import requests
import json

def get_binance_btc_price():
    global price
    """
    Fetches the current price of Bitcoin (BTC/USDT) from the Binance API.
    """
    # The public API endpoint for a specific symbol's price
    url = "https://api.binance.com/api/v3/ticker/price"
    
    # Parameters to specify the trading pair (symbol)
    params = {
        'symbol': 'BTCUSDT'
    }
    
    try:
        # Send a GET request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            data = response.json()
            
            # Extract and print the price
            price = data.get('price')
            if price:
                print(f"Current Bitcoin (BTC/USDT) price: ${float(price):,.2f}")
                return float(price)
            else:
                print("Price not found in the response.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        # Handle any potential errors during the request
        print(f"An error occurred during the API request: {e}")

def get_binance_ar_price():

    url = "https://api.binance.com/api/v3/ticker/price"
    
    # Parameters to specify the trading pair (symbol)
    params = {
        'symbol': 'ARUSDT'
    }
    
    try:
        # Send a GET request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            data = response.json()
            
            # Extract and print the price
            price = data.get('price')
            if price:
                print(f"Current Arweave (AR/USDT) price: ${float(price):,.2f}")
                return float(price)
            else:
                print("Price not found in the response.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        # Handle any potential errors during the request
        print(f"An error occurred during the API request: {e}")


if __name__ == "__main__":
    get_binance_btc_price()
    get_binance_ar_price()
    
  
    
