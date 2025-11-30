import requests
import time



TOKEN = "Your_Telegram_Token"
URL = f"https://api.telegram.org/bot{TOKEN}/"

ticker = {

    'btc': ['BTCUSDT', 'Bitcoin'],
    'eth': ['ETHUSDT', 'Ethereum'],
    'ar' : ['ARUSDT', 'Arweave'],
    'ada': ['ADAUSDT','Cardano']

}



def get_btc_price(message):

    

    try:

        if message in ticker:

            url = f"https://api.binance.com/api/v3/ticker/price?symbol={ticker[message][0]}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return float(data['price'])
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
        else:
            return "Error"     
    except requests.exceptions.RequestException as e:
        # Handle any potential errors during the request
        print(f"An error occurred during the API request: {e}")
    
    
    


def get_updates(offset=None):
    url = URL + "getUpdates"
    params = {"offset": offset}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    url = URL + "sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.get(url, params=params)

def main():
    last_update_id = None

    print("The Bot is running >>>>🤖<<<......")

    while True:
        updates = get_updates(last_update_id)

        if "result" in updates:
            for update in updates["result"]:

                message = update["message"]["text"].lower()

                chat_id = update["message"]["chat"]["id"]

                update_id = update["update_id"]


                

                price = get_btc_price(message)

                if price == 'Error':
                    reply_text = "An Error occured.. check what you typed!!!"
                    send_message(chat_id, reply_text)
                else:
                    reply_text = f"The price of {ticker[message][1]} is: ${price}"
                    send_message(chat_id, reply_text)

                last_update_id = update_id + 1

        time.sleep(1)

if __name__ == "__main__":
    main()